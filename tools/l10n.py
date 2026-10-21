#!/usr/bin/env python3
"""Endless Sky IT — incremental localization pipeline (state, batches, QA).

Design
------
* SQLite is the job state (safe for restarts and partial writes); JSON files are
  only exports for humans and for the translator step.
* Every unit has a stable id (from the audit inventory) and a hash of the English
  source. Work is detected by id + hash, never by file position alone.
* A batch is APPROVED only if mechanical validation passes with zero errors.
* The game repository is only read. Integration writes into ./output/.

Subcommands
-----------
  init        build state.db from the audit inventory
  build       create batches (deterministic, by family)
  status      progress summary
  export B    write batches/<id>/input.json for the translator
  import B    import batches/<id>/output.json, validate, set state
  validate B  re-run validation on an imported batch
  report      write progress.json + qa/summary.json + final report

Usage
-----
  python tools/l10n.py init --audit <audit dir> --repo <game repo>
  python tools/l10n.py build --batch B001 --name "UI labels" --where "path='data/_ui/interfaces.txt' AND kind='UI_LABEL'"
  python tools/l10n.py export B001
  python tools/l10n.py import B001
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import sqlite3
import sys
from collections import Counter
from datetime import datetime, timezone

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(WS, "state.db")
PLACEHOLDER = re.compile(r"<[a-z][a-z0-9 ']{0,28}>")
CONTROL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")
# Terms kept identical in Italian (brands, acronyms, words the game treats as
# names). Used by the "untranslated remnant" check.
ALLOW_IDENTICAL = {"laser", "radar", "scanner", "missile", "drone", "fighter",
                   "CPU", "GPU", "MEM", "HUD", "ID", "OK", "A", "UI", "_+", "_-", "_Audio"}
GLOSSARY_TERMS = {}


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def connect() -> sqlite3.Connection:
    if not os.path.exists(DB):
        sys.exit(f"FATAL: {DB} missing — run 'init' first")
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    return con


def cmd_init(args) -> int:
    audit = os.path.abspath(args.audit)
    coverage = os.path.join(audit, "LOCALIZATION_COVERAGE.csv")
    if not os.path.exists(coverage):
        sys.exit("FATAL: LOCALIZATION_COVERAGE.csv not found in audit dir")
    os.makedirs(os.path.join(WS, "batches"), exist_ok=True)
    os.makedirs(os.path.join(WS, "qa"), exist_ok=True)
    os.makedirs(os.path.join(WS, "output"), exist_ok=True)

    if os.path.exists(DB):
        os.remove(DB)
    con = sqlite3.connect(DB)
    con.executescript("""
        CREATE TABLE units (
            id TEXT PRIMARY KEY,
            path TEXT, line INTEGER, kind TEXT, context TEXT,
            english TEXT, english_hash TEXT, italian TEXT,
            state TEXT DEFAULT 'PENDING', batch_id TEXT,
            non_ascii INTEGER DEFAULT 0, updated_at TEXT
        );
        CREATE INDEX idx_units_state ON units(state);
        CREATE INDEX idx_units_batch ON units(batch_id);
        CREATE TABLE batches (
            id TEXT PRIMARY KEY, name TEXT, selector TEXT,
            units INTEGER, words INTEGER, token_estimate INTEGER,
            status TEXT, source_hash TEXT, created_at TEXT, updated_at TEXT
        );
        CREATE TABLE issues (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            batch_id TEXT, unit_id TEXT, code TEXT, severity TEXT,
            detail TEXT, created_at TEXT, resolved INTEGER DEFAULT 0
        );
        CREATE TABLE events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            at TEXT, batch_id TEXT, kind TEXT, detail TEXT
        );
    """)
    rows = 0
    with open(coverage, encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh):
            if row["classification"] != "MISSING":
                continue
            english = row["english"]
            con.execute(
                "INSERT OR REPLACE INTO units (id, path, line, kind, context, english,"
                " english_hash, italian, state, non_ascii, updated_at)"
                " VALUES (?,?,?,?,?,?,?,NULL,'PENDING',?,?)",
                (row["unit_id"], row["path"], int(row["line"]), row["kind"], row["context"],
                 english, hashlib.sha256(english.encode()).hexdigest()[:16],
                 1 if any(ord(c) > 127 for c in english) else 0, now()))
            rows += 1
    con.commit()

    manifest = {
        "project": "Endless Sky — Italian localization",
        "repo": os.path.abspath(args.repo),
        "audit_workspace": audit,
        "created_at": now(),
        "source_units": rows,
        "unit_id_scheme": "<context>|<key>|<line>|<index> (from the audit inventory)",
        "hash": "sha256(english)[:16]",
        "states": ["PENDING", "TRANSLATING", "TRANSLATED", "VALIDATING",
                   "APPROVED", "NEEDS_REVIEW", "FAILED"],
        "non_ascii_source_units": con.execute(
            "SELECT COUNT(*) FROM units WHERE non_ascii=1").fetchone()[0],
    }
    with open(os.path.join(WS, "manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2)

    con.execute("INSERT INTO events (at,batch_id,kind,detail) VALUES (?,?,?,?)",
                (now(), None, "init", f"{rows} units imported"))
    con.commit()
    print(f"initialized {DB} with {rows} units")
    return 0


def cmd_build(args) -> int:
    con = connect()
    rows = con.execute(
        f"SELECT id, english, kind FROM units WHERE state='PENDING' AND ({args.where}) ORDER BY path, line"
    ).fetchall()
    if not rows:
        sys.exit("no units matched the selector")
    if args.limit:
        rows = rows[: args.limit]
    words = sum(len(r["english"].split()) for r in rows)
    tokens = int(sum(len(r["english"]) for r in rows) / 4)  # crude but honest
    source_hash = hashlib.sha256(
        "".join(sorted(r["id"] + r["english"] for r in rows)).encode()).hexdigest()[:16]
    con.execute(
        "INSERT OR REPLACE INTO batches (id,name,selector,units,words,token_estimate,status,source_hash,created_at,updated_at)"
        " VALUES (?,?,?,?,?,?,?,?,?,?)",
        (args.batch, args.name, args.where, len(rows), words, tokens,
         "PENDING", source_hash, now(), now()))
    con.executemany("UPDATE units SET batch_id=? WHERE id=?", [(args.batch, r["id"]) for r in rows])
    con.execute("INSERT INTO events (at,batch_id,kind,detail) VALUES (?,?,?,?)",
                (now(), args.batch, "build", f"{len(rows)} units, {words} words, ~{tokens} tokens"))
    con.commit()
    print(f"{args.batch}: {len(rows)} units · {words} words · ~{tokens} tokens · hash {source_hash}")
    return 0


def cmd_export(args) -> int:
    con = connect()
    batch = con.execute("SELECT * FROM batches WHERE id=?", (args.batch,)).fetchone()
    if not batch:
        sys.exit("unknown batch")
    rows = con.execute(
        "SELECT id,path,line,kind,context,english FROM units WHERE batch_id=? ORDER BY path,line",
        (args.batch,)).fetchall()
    out_dir = os.path.join(WS, "batches", args.batch)
    os.makedirs(out_dir, exist_ok=True)
    payload = {
        "batch": batch["id"], "name": batch["name"], "source_hash": batch["source_hash"],
        "instructions": "return JSON array [{\"id\": ..., \"it\": ...}] with one entry per id",
        "units": [dict(r) for r in rows],
    }
    path = os.path.join(out_dir, "input.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=1, ensure_ascii=False)
    con.execute("UPDATE batches SET status='TRANSLATING', updated_at=? WHERE id=?", (now(), args.batch))
    con.execute("UPDATE units SET state='TRANSLATING' WHERE batch_id=?", (args.batch,))
    con.execute("INSERT INTO events (at,batch_id,kind,detail) VALUES (?,?,?,?)",
                (now(), args.batch, "export", f"{len(rows)} units -> {path}"))
    con.commit()
    print(f"exported {len(rows)} units to {path}")
    return 0


def validate_batch(con, batch_id: str, results: list[dict]) -> list[dict]:
    """Mechanical validation. Returns a list of issue dicts."""
    rows = {r["id"]: r for r in con.execute(
        "SELECT * FROM units WHERE batch_id=?", (batch_id,)).fetchall()}
    issues = []
    seen = Counter()
    for item in results:
        uid = item.get("id")
        it = item.get("it", "")
        if uid not in rows:
            issues.append({"unit_id": uid, "code": "UNKNOWN_ID", "severity": "error",
                           "detail": "id not in batch"})
            continue
        seen[uid] += 1
        src = rows[uid]["english"]
        if not isinstance(it, str) or not it.strip():
            issues.append({"unit_id": uid, "code": "EMPTY", "severity": "error", "detail": "empty translation"})
            continue
        if CONTROL.search(it) or "\n" in it or "\r" in it:
            issues.append({"unit_id": uid, "code": "CONTROL_CHAR", "severity": "error",
                           "detail": "newline or control character"})
        if "`" in it:
            issues.append({"unit_id": uid, "code": "BACKTICK", "severity": "error",
                           "detail": "backtick would break the data tokenizer"})
        if '"' in it and '"' not in src:
            # a quote is only safe when the source itself is backtick-delimited
            issues.append({"unit_id": uid, "code": "DOUBLE_QUOTE", "severity": "error",
                           "detail": "quote added to a value that used the quote delimiter"})
        want = Counter(PLACEHOLDER.findall(src))
        got = Counter(PLACEHOLDER.findall(it))
        if want != got:
            issues.append({"unit_id": uid, "code": "PLACEHOLDER_MISMATCH", "severity": "error",
                           "detail": f"expected {dict(want)} got {dict(got)}"})
        if src.startswith("\t") and not it.startswith("\t"):
            issues.append({"unit_id": uid, "code": "TAB_LOST", "severity": "error",
                           "detail": "leading paragraph tab lost"})
        if it.strip().lower() == src.strip().lower() and src not in ALLOW_IDENTICAL:
            issues.append({"unit_id": uid, "code": "UNTRANSLATED", "severity": "warning",
                           "detail": "identical to source"})
        ratio = len(it) / max(1, len(src))
        if not 0.45 <= ratio <= 2.2:
            issues.append({"unit_id": uid, "code": "LENGTH_RATIO", "severity": "warning",
                           "detail": f"ratio {ratio:.2f}"})
        if any(ord(c) > 127 for c in it):
            issues.append({"unit_id": uid, "code": "NON_ASCII", "severity": "warning",
                           "detail": "accented characters need the extended font atlas (audit IT-002)"})
        for en, it_term in GLOSSARY_TERMS.items():
            if not re.search(rf"\b{re.escape(en)}\b", src, re.IGNORECASE):
                continue
            # accept inflected forms: compare on the stem (drop the final vowel)
            stem = it_term.lower().rstrip("aeiou")
            if it_term.lower() not in it.lower() and (not stem or stem not in it.lower()):
                issues.append({"unit_id": uid, "code": "GLOSSARY", "severity": "info",
                               "detail": f"'{en}' -> '{it_term}' not found"})
    for uid in rows:
        if seen[uid] == 0:
            issues.append({"unit_id": uid, "code": "MISSING_RESULT", "severity": "error",
                           "detail": "no translation returned"})
        elif seen[uid] > 1:
            issues.append({"unit_id": uid, "code": "DUPLICATE_ID", "severity": "error",
                           "detail": f"{seen[uid]} results for the same id"})
    return issues


def cmd_import(args) -> int:
    con = connect()
    batch = con.execute("SELECT * FROM batches WHERE id=?", (args.batch,)).fetchone()
    if not batch:
        sys.exit("unknown batch")
    path = os.path.join(WS, "batches", args.batch, "output.json")
    if not os.path.exists(path):
        sys.exit(f"missing {path}")
    payload = json.load(open(path, encoding="utf-8"))
    results = payload["results"] if isinstance(payload, dict) else payload
    con.execute("UPDATE batches SET status='VALIDATING' WHERE id=?", (args.batch,))
    issues = validate_batch(con, args.batch, results)

    errors = [i for i in issues if i["severity"] == "error"]
    warnings = [i for i in issues if i["severity"] in ("warning", "info")]
    if not errors:
        for item in results:
            con.execute("UPDATE units SET italian=?, state='APPROVED', updated_at=? WHERE id=?",
                        (item["it"], now(), item["id"]))
        status, unit_state = "APPROVED", "APPROVED"
    else:
        for item in results:
            con.execute("UPDATE units SET italian=?, state='NEEDS_REVIEW', updated_at=? WHERE id=?",
                        (item["it"], now(), item["id"]))
        status, unit_state = "NEEDS_REVIEW", "NEEDS_REVIEW"

    con.execute("DELETE FROM issues WHERE batch_id=?", (args.batch,))
    for i in issues:
        con.execute("INSERT INTO issues (batch_id,unit_id,code,severity,detail,created_at)"
                    " VALUES (?,?,?,?,?,?)",
                    (args.batch, i["unit_id"], i["code"], i["severity"], i["detail"], now()))
    con.execute("UPDATE batches SET status=?, updated_at=? WHERE id=?", (status, now(), args.batch))
    con.execute("INSERT INTO events (at,batch_id,kind,detail) VALUES (?,?,?,?)",
                (now(), args.batch, "import", f"{len(results)} results, {len(errors)} errors, {len(warnings)} warnings"))

    qa = {"batch": args.batch, "at": now(), "results": len(results),
          "errors": len(errors), "warnings": len(warnings), "status": status,
          "issues": issues}
    qa_path = os.path.join(WS, "batches", args.batch, "qa.json")
    with open(qa_path, "w", encoding="utf-8") as fh:
        json.dump(qa, fh, indent=1, ensure_ascii=False)

    if not errors:
        with open(os.path.join(WS, "translation_memory.jsonl"), "a", encoding="utf-8") as fh:
            for item in results:
                unit = con.execute("SELECT * FROM units WHERE id=?", (item["id"],)).fetchone()
                fh.write(json.dumps({
                    "id": item["id"], "en": unit["english"], "it": item["it"],
                    "hash": unit["english_hash"], "batch": args.batch,
                    "approved_at": now(), "context": unit["context"],
                }, ensure_ascii=False) + "\n")
    con.commit()
    print(f"{args.batch}: {status} · {len(errors)} errors · {len(warnings)} warnings -> {qa_path}")
    return 0 if not errors else 1


def cmd_status(args) -> int:
    con = connect()
    print("state            units")
    for state, n in con.execute("SELECT state, COUNT(*) FROM units GROUP BY state ORDER BY 2 DESC"):
        print(f"{state:16s} {n}")
    print("\nbatch    status          units   errors")
    for b in con.execute("SELECT * FROM batches ORDER BY id"):
        err = con.execute("SELECT COUNT(*) FROM issues WHERE batch_id=? AND severity='error'",
                          (b["id"],)).fetchone()[0]
        print(f"{b['id']:8s} {b['status']:15s} {b['units']:5d} {err:8d}")
    return 0


def cmd_report(args) -> int:
    con = connect()
    total = con.execute("SELECT COUNT(*) FROM units").fetchone()[0]
    approved = con.execute("SELECT COUNT(*) FROM units WHERE state='APPROVED'").fetchone()[0]
    review = con.execute("SELECT COUNT(*) FROM units WHERE state='NEEDS_REVIEW'").fetchone()[0]
    words_total = con.execute("SELECT SUM(LENGTH(english)-LENGTH(REPLACE(english,' ',''))+1) FROM units").fetchone()[0]
    non_ascii = sum(1 for (it,) in con.execute(
        "SELECT italian FROM units WHERE italian IS NOT NULL") if any(ord(c) > 127 for c in it))
    progress = {
        "generated_at": now(),
        "units_total": total,
        "approved": approved,
        "needs_review": review,
        "pending": total - approved - review,
        "coverage": round(approved / total, 6) if total else 0,
        "words_total_estimate": words_total,
        "approved_with_non_ascii": non_ascii,
        "batches": [dict(b) for b in con.execute("SELECT * FROM batches ORDER BY id")],
    }
    with open(os.path.join(WS, "progress.json"), "w", encoding="utf-8") as fh:
        json.dump(progress, fh, indent=2)
    print(json.dumps({k: progress[k] for k in ("units_total", "approved", "needs_review", "pending", "coverage")}, indent=2))
    return 0


def cmd_validate(args) -> int:
    con = connect()
    path = os.path.join(WS, "batches", args.batch, "output.json")
    payload = json.load(open(path, encoding="utf-8"))
    results = payload["results"] if isinstance(payload, dict) else payload
    issues = validate_batch(con, args.batch, results)
    errors = [i for i in issues if i["severity"] == "error"]
    print(json.dumps({"batch": args.batch, "errors": len(errors),
                      "warnings": len(issues) - len(errors), "issues": issues[:20]}, indent=2))
    return 0 if not errors else 1


def load_glossary() -> None:
    path = os.path.join(WS, "glossary.csv")
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh):
            en = (row.get("english_term") or "").strip()
            it = (row.get("recommended_italian") or "").strip()
            if en and it and en.lower() != it.lower():
                GLOSSARY_TERMS[en] = it


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("init"); p.add_argument("--audit", required=True); p.add_argument("--repo", required=True)
    p.set_defaults(func=cmd_init)

    p = sub.add_parser("build")
    p.add_argument("--batch", required=True); p.add_argument("--name", required=True)
    p.add_argument("--where", required=True); p.add_argument("--limit", type=int)
    p.set_defaults(func=cmd_build)

    for name, fn in (("export", cmd_export), ("import", cmd_import), ("validate", cmd_validate)):
        p = sub.add_parser(name); p.add_argument("batch"); p.set_defaults(func=fn)

    p = sub.add_parser("status"); p.set_defaults(func=cmd_status)
    p = sub.add_parser("report"); p.set_defaults(func=cmd_report)

    args = ap.parse_args()
    load_glossary()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
