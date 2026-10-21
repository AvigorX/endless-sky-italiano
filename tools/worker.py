#!/usr/bin/env python3
"""Resumable production worker for the Italian localization.

Two engines
-----------
* ``api``  — calls a DeepSeek-compatible /chat/completions endpoint with
  `DEEPSEEK_API_KEY` taken from the environment. Never prints the key.
* ``file`` — writes the prompt bundle and waits for an external translator
  (agent, human, or another tool) to produce ``batches/<id>/output.json``.

Both paths end in the same importer, so the blocking validators always run.

Usage
-----
    python tools/worker.py --engine api  --batch B005 --where "path='data/_ui/help.txt'" --limit 40
    python tools/worker.py --engine file --batch B005 --where "..." --limit 40
    python tools/worker.py --import B005
    python tools/worker.py --status

Exit codes: 0 ok, 1 validation failure, 2 configuration/setup problem.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import subprocess
import sys
import time
import urllib.error
import urllib.request

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(WS, "state.db")
DEFAULT_BASE = "https://api.deepseek.com/v1"
DEFAULT_MODEL = "deepseek-chat"

SYSTEM = """You are a senior Italian game localizer working on Endless Sky.
Translate the user's JSON array of units into natural, contemporary Italian.

Hard rules:
- Return ONLY a JSON object {"results":[{"id":"<same id>","it":"<translation>"}]}.
- Keep every <placeholder> token EXACTLY as-is (<planet>, <payment>, <ship>, <View star map>...).
- Keep a leading tab if the source has one; never add or remove tabs.
- Never add double quotes unless the source already contains them.
- Never use a backtick character.
- Do not translate identifiers, and do not add or drop information.
- Follow the glossary; keep the same tone in related strings.
"""


def connect():
    if not os.path.exists(DB):
        sys.exit("FATAL: state.db missing")
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    return con


def run(cmd, **kw):
    return subprocess.run(cmd, cwd=WS, capture_output=True, text=True, **kw)


def ensure_runs_table(con):
    con.execute("""CREATE TABLE IF NOT EXISTS runs (
        id INTEGER PRIMARY KEY AUTOINCREMENT, batch TEXT, engine TEXT, model TEXT,
        units INTEGER, src_words INTEGER, out_words INTEGER,
        prompt_tokens INTEGER, completion_tokens INTEGER, duration_s REAL,
        retries INTEGER, status TEXT, at TEXT)""")
    con.commit()


def build_batch(con, batch, where, limit, name):
    con.execute("INSERT OR REPLACE INTO batches (id,name,selector,units,words,token_estimate,"
                "status,source_hash,created_at,updated_at) VALUES (?,?,?,0,0,0,'PENDING','',?,?)",
                (batch, name, where, time.strftime("%Y-%m-%dT%H:%M:%SZ"),
                 time.strftime("%Y-%m-%dT%H:%M:%SZ")))
    con.commit()
    proc = run([sys.executable, "tools/l10n.py", "build", "--batch", batch,
                "--name", name, "--where", where] + (["--limit", str(limit)] if limit else []))
    if proc.returncode != 0:
        print(proc.stdout, proc.stderr)
        return False
    print(proc.stdout.strip())
    return True


def export(con, batch):
    proc = run([sys.executable, "tools/l10n.py", "export", batch])
    print(proc.stdout.strip())
    return proc.returncode == 0


def build_prompt(con, batch):
    payload = json.load(open(os.path.join(WS, "batches", batch, "input.json"), encoding="utf-8"))
    units = payload["units"]
    glossary = []
    gpath = os.path.join(WS, "glossary.csv")
    if os.path.exists(gpath):
        import csv as _csv
        with open(gpath, encoding="utf-8", newline="") as fh:
            for row in _csv.DictReader(fh):
                en, it = row["english_term"].strip(), row["recommended_italian"].strip()
                if en and it:
                    glossary.append(f"{en} = {it}")
    style = open(os.path.join(WS, "style_guide.md"), encoding="utf-8").read()
    # style guide is long: keep the rules that matter for a batch, drop the preamble
    style_core = style[style.find("## 2."):] if "## 2." in style else style
    user = (
        "GLOSSARY (binding):\n" + "\n".join(glossary[:120]) + "\n\n"
        "STYLE RULES:\n" + style_core[:4000] + "\n\n"
        "UNITS (translate every 'english' value, keep the id):\n"
        + json.dumps([{"id": u["id"], "english": u["english"]} for u in units],
                     ensure_ascii=False, indent=1)
    )
    return payload, SYSTEM, user


def call_api(system, user, base, model, timeout=300):
    key = os.environ.get("DEEPSEEK_API_KEY") or os.environ.get("OPENAI_API_KEY")
    if not key:
        return None, ("DEEPSEEK_API_KEY is not set in this environment. "
                      "Hermes stores the credential internally (source: env:DEEPSEEK_API_KEY) "
                      "and it is not readable from the shell; export it for this process "
                      "or run the worker with --engine file.")
    body = json.dumps({
        "model": model,
        "messages": [{"role": "system", "content": system},
                     {"role": "user", "content": user}],
        "temperature": 0.2,
        "response_format": {"type": "json_object"},
        "max_tokens": 8000,
    }).encode()
    req = urllib.request.Request(base.rstrip("/") + "/chat/completions", data=body,
                                 headers={"Content-Type": "application/json",
                                          "Authorization": "Bearer " + key})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode())
    except urllib.error.HTTPError as exc:
        return None, f"HTTP {exc.code}: {exc.read()[:200].decode(errors='replace')}"
    except (urllib.error.URLError, TimeoutError) as exc:
        return None, f"network error: {exc}"
    text = data["choices"][0]["message"]["content"]
    usage = data.get("usage", {})
    return {"text": text, "usage": usage}, None


def parse_results(text, expected_ids):
    """Extract the JSON object even if the model wrapped it in prose/fences."""
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        return None, "no JSON object in response"
    try:
        obj = json.loads(match.group(0))
    except json.JSONDecodeError as exc:
        return None, f"invalid JSON: {exc}"
    results = obj.get("results") if isinstance(obj, dict) else None
    if not isinstance(results, list):
        return None, "missing 'results' array"
    got = [r.get("id") for r in results if isinstance(r, dict)]
    if sorted(got) != sorted(expected_ids):
        missing = set(expected_ids) - set(got)
        extra = set(got) - set(expected_ids)
        return None, f"id mismatch (missing {len(missing)}, extra {len(extra)})"
    return [{"id": r["id"], "it": r.get("it", "")} for r in results], None


def import_batch(batch):
    proc = run([sys.executable, "tools/l10n.py", "import", batch])
    print(proc.stdout.strip())
    return proc.returncode


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--engine", choices=["api", "file"], default="file")
    ap.add_argument("--batch")
    ap.add_argument("--where")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--name", default="")
    ap.add_argument("--model", default=os.environ.get("DEEPSEEK_MODEL", DEFAULT_MODEL))
    ap.add_argument("--base", default=os.environ.get("DEEPSEEK_BASE_URL", DEFAULT_BASE))
    ap.add_argument("--retries", type=int, default=3)
    ap.add_argument("--import", dest="do_import", default=None)
    ap.add_argument("--status", action="store_true")
    args = ap.parse_args()

    con = connect()
    ensure_runs_table(con)

    if args.status:
        for row in con.execute("SELECT * FROM runs ORDER BY id DESC LIMIT 10"):
            print(dict(row))
        for row in con.execute("SELECT state, COUNT(*) n FROM units GROUP BY state"):
            print(f"{row['state']:12s} {row['n']}")
        return 0

    if args.do_import:
        return import_batch(args.do_import)

    if not (args.batch and args.where):
        ap.error("--batch and --where are required (or use --import/--status)")

    name = args.name or f"batch {args.batch}"
    if not build_batch(con, args.batch, args.where, args.limit, name):
        return 2
    if not export(con, args.batch):
        return 2

    payload, system, user = build_prompt(con, args.batch)
    ids = [u["id"] for u in payload["units"]]
    prompt_path = os.path.join(WS, "batches", args.batch, "prompt.md")
    with open(prompt_path, "w", encoding="utf-8") as fh:
        fh.write("<!-- system -->\n" + system + "\n\n<!-- user -->\n" + user)
    print(f"prompt: {prompt_path} ({len(user)} chars, {len(ids)} units)")

    if args.engine == "file":
        print("engine=file: waiting for an external translator to write "
              f"batches/{args.batch}/output.json, then run --import {args.batch}")
        return 0

    t0 = time.time()
    attempts = 0
    last_error = None
    results = None
    usage = {}
    while attempts <= args.retries:
        attempts += 1
        out, err = call_api(system, user, args.base, args.model)
        if err:
            last_error = err
            print(f"attempt {attempts} failed: {err}")
            if "DEEPSEEK_API_KEY is not set" in err:
                return 2
            time.sleep(min(30, 2 ** attempts))
            continue
        parsed, perr = parse_results(out["text"], ids)
        if parsed:
            results, usage = parsed, out.get("usage", {})
            break
        last_error = perr
        print(f"attempt {attempts}: {perr}")
        time.sleep(min(30, 2 ** attempts))

    if not results:
        con.execute("INSERT INTO runs (batch,engine,model,units,src_words,out_words,prompt_tokens,"
                    "completion_tokens,duration_s,retries,status,at) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                    (args.batch, "api", args.model, len(ids), 0, 0, 0, 0,
                     round(time.time() - t0, 1), attempts - 1, "FAILED",
                     time.strftime("%Y-%m-%dT%H:%M:%SZ")))
        con.commit()
        print(f"FAILED after {attempts} attempts: {last_error}")
        return 1

    with open(os.path.join(WS, "batches", args.batch, "output.json"), "w", encoding="utf-8") as fh:
        json.dump({"batch": args.batch, "results": results}, fh, ensure_ascii=False, indent=1)

    src_words = sum(len(u["english"].split()) for u in payload["units"])
    out_words = sum(len(r["it"].split()) for r in results)
    duration = round(time.time() - t0, 1)
    code = import_batch(args.batch)
    con.execute("INSERT INTO runs (batch,engine,model,units,src_words,out_words,prompt_tokens,"
                "completion_tokens,duration_s,retries,status,at) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                (args.batch, "api", args.model, len(results), src_words, out_words,
                 usage.get("prompt_tokens", 0), usage.get("completion_tokens", 0),
                 duration, attempts - 1, "APPROVED" if code == 0 else "NEEDS_REVIEW",
                 time.strftime("%Y-%m-%dT%H:%M:%SZ")))
    con.commit()
    print(f"{args.batch}: {len(results)} units · {src_words}→{out_words} words · {duration}s · "
          f"retries {attempts - 1} · status {'APPROVED' if code == 0 else 'NEEDS_REVIEW'}")
    return code


if __name__ == "__main__":
    sys.exit(main())
