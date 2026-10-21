#!/usr/bin/env python3
"""Apply approved translations to a COPY of the source data files.

Safety model
------------
* The game repository is only read. Output goes to ./output/l10n-it/ mirroring
  the source path, so a diff with the original is one command away.
* Replacement is token-exact: the English token is located on its known line,
  replaced with the same delimiter (`"` or backtick), and the whole file is then
  re-tokenized and compared line by line with the original.
* Any structural difference (token count, token kinds, untouched tokens) aborts
  the file and reports the failure. Nothing is written for a failed file.

Usage
-----
    python tools/apply_patch.py B001 B002 [--repo <game repo>]
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_REPO = r"C:\Users\Dave\PROGETTI\G-DEV\GAME-SOURCE-LAB\endless-sky"


def tokenize(line: str):
    """Same rules as source/DataFile.cpp (no escapes, # outside tokens)."""
    out = []
    i, n = 0, len(line)
    while i < n:
        c = line[i]
        if c in " \t\r\n":
            i += 1
            continue
        if c == "#":
            break
        if c in "\"`":
            end = line.find(c, i + 1)
            if end == -1:
                out.append((line[i + 1:], "quoted" if c == '"' else "backtick"))
                break
            out.append((line[i + 1:end], "quoted" if c == '"' else "backtick"))
            i = end + 1
            continue
        start = i
        while i < n and line[i] not in " \t\r\n#":
            i += 1
        out.append((line[start:i], "bare"))
    return out


def apply_file(units, src_path, dst_path):
    # keep line endings byte-identical: only the translated token may change
    src_lines = open(src_path, encoding="utf-8", newline="").read().splitlines(keepends=True)
    out_lines = list(src_lines)
    touched = {}
    for u in units:
        line_no = int(u["line"]) - 1
        if line_no >= len(src_lines):
            return False, f"line {line_no + 1} out of range"
        line = out_lines[line_no]
        en, it = u["english"], u["it"]
        replaced = False
        for delim in ("`", '"'):
            needle = delim + en + delim
            if needle in line:
                out_lines[line_no] = line.replace(needle, delim + it + delim, 1)
                replaced = True
                break
        if not replaced:
            return False, f"token not found on line {line_no + 1}: {en[:40]!r}"
        touched[line_no] = True

    # structural verification
    if len(out_lines) != len(src_lines):
        return False, "line count changed"
    for idx, (a, b) in enumerate(zip(src_lines, out_lines)):
        if idx not in touched:
            if a != b:
                return False, f"untouched line {idx + 1} changed"
            continue
        ta, tb = tokenize(a), tokenize(b)
        if len(ta) != len(tb):
            return False, f"token count changed on line {idx + 1}: {len(ta)} -> {len(tb)}"
        if [k for _, k in ta] != [k for _, k in tb]:
            return False, f"token kinds changed on line {idx + 1}"
        diffs = sum(1 for (x, _), (y, _) in zip(ta, tb) if x != y)
        if diffs > 1:
            return False, f"{diffs} tokens changed on line {idx + 1} (expected 1)"

    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
    with open(dst_path, "w", encoding="utf-8", newline="") as fh:
        fh.write("".join(out_lines))
    return True, f"{len(touched)} lines"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("batches", nargs="+")
    ap.add_argument("--repo", default=DEFAULT_REPO)
    args = ap.parse_args()

    report = {"files": [], "ok": True}
    by_file = {}
    for batch in args.batches:
        out_path = os.path.join(WS, "batches", batch, "output.json")
        in_path = os.path.join(WS, "batches", batch, "input.json")
        if not (os.path.exists(out_path) and os.path.exists(in_path)):
            print(f"FATAL: batch {batch} incomplete")
            return 2
        inputs = {u["id"]: u for u in json.load(open(in_path, encoding="utf-8"))["units"]}
        results = json.load(open(out_path, encoding="utf-8"))["results"]
        for r in results:
            u = inputs[r["id"]]
            path = u["path"]
            by_file.setdefault(path, []).append({
                "line": u["line"], "english": u["english"], "it": r["it"], "id": r["id"],
            })

    for path, units in sorted(by_file.items()):
        src = os.path.join(args.repo, path.replace("/", os.sep))
        dst = os.path.join(WS, "output", "l10n-it", path.replace("/", os.sep))
        ok, detail = apply_file(units, src, dst)
        report["files"].append({"path": path, "units": len(units), "ok": ok, "detail": detail})
        report["ok"] &= ok
        print(("OK   " if ok else "FAIL ") + f"{path}: {detail}")

    os.makedirs(os.path.join(WS, "qa"), exist_ok=True)
    with open(os.path.join(WS, "qa", "apply_report.json"), "w", encoding="utf-8") as fh:
        json.dump(report, fh, indent=2)
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
