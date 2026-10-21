#!/usr/bin/env python3
"""Validate the localization workspace end to end.

Checks
------
1. state.db exists and its unit count matches the audit inventory.
2. Every batch has input.json, output.json and qa.json; batch state matches QA.
3. Every APPROVED unit has Italian text and no blocking issue.
4. Output files exist for every patched source and differ from the original
   only in the expected number of tokens, keeping line and token counts.
5. The game repository is clean and its HEAD matches the audited commit.

Exit 0 = valid, 1 = failures, 2 = setup error.
"""

import csv
import json
import os
import sqlite3
import subprocess
import sys

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(WS, "state.db")
REPO = r"C:\Users\Dave\PROGETTI\G-DEV\GAME-SOURCE-LAB\endless-sky"
AUDIT = r"C:\Users\Dave\PROGETTI\G-DEV\GAME-SOURCE-LAB\endless-sky-l10n-audit"
EXPECTED_COMMIT = "b4aa3bac3fcfa43d6c5a6497f9551d4362867856"

failures = []


def check(ok, name, detail):
    print(("[PASS] " if ok else "[FAIL] ") + f"{name}: {detail}")
    if not ok:
        failures.append(name)


def tokenize(line):
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
                out.append((line[i + 1:], "q"))
                break
            out.append((line[i + 1:end], "q"))
            i = end + 1
            continue
        start = i
        while i < n and line[i] not in " \t\r\n#":
            i += 1
        out.append((line[start:i], "b"))
    return out


def main() -> int:
    if not os.path.exists(DB):
        print("FATAL: state.db missing")
        return 2
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row

    summary = json.load(open(os.path.join(AUDIT, "tools", "inventory_summary.json"), encoding="utf-8"))
    units = con.execute("SELECT COUNT(*) FROM units").fetchone()[0]
    check(units == summary["translatable_units"], "UNIT_COUNT",
          f"{units} units (audit says {summary['translatable_units']})")

    approved = con.execute("SELECT * FROM units WHERE state='APPROVED'").fetchall()
    empty = [u["id"] for u in approved if not (u["italian"] or "").strip()]
    check(not empty, "APPROVED_HAVE_TEXT", f"{len(approved)} approved, {len(empty)} empty")

    blocked = con.execute(
        "SELECT DISTINCT unit_id FROM issues WHERE severity='error' AND resolved=0").fetchall()
    approved_ids = {u["id"] for u in approved}
    conflict = approved_ids & {r["unit_id"] for r in blocked}
    check(not conflict, "NO_BLOCKING_ISSUES_ON_APPROVED", f"{len(conflict)} conflicts")

    batches = con.execute("SELECT * FROM batches ORDER BY id").fetchall()
    check(len(batches) > 0, "BATCHES", f"{len(batches)} batches")
    for b in batches:
        d = os.path.join(WS, "batches", b["id"])
        files_ok = all(os.path.exists(os.path.join(d, f)) for f in ("input.json", "output.json", "qa.json"))
        qa = json.load(open(os.path.join(d, "qa.json"), encoding="utf-8")) if files_ok else {}
        check(files_ok, "BATCH_FILES", b["id"])
        check(qa.get("status") == b["status"], "BATCH_STATE", f"{b['id']}: {b['status']} vs QA {qa.get('status')}")

    # Units whose Italian is intentionally identical (hotkeys, symbols, acronyms)
    # cannot change a line: expected changed lines = units with it != en.
    expected_changed = {}
    for b in batches:
        inp = {u["id"]: u for u in json.load(
            open(os.path.join(WS, "batches", b["id"], "input.json"), encoding="utf-8"))["units"]}
        for r in json.load(open(os.path.join(WS, "batches", b["id"], "output.json"),
                                encoding="utf-8"))["results"]:
            u = inp[r["id"]]
            if r["it"] != u["english"]:
                expected_changed[u["path"]] = expected_changed.get(u["path"], 0) + 1

    apply_report = json.load(open(os.path.join(WS, "qa", "apply_report.json"), encoding="utf-8"))
    for f in apply_report["files"]:
        path = f["path"]
        src = os.path.join(REPO, path.replace("/", os.sep))
        dst = os.path.join(WS, "output", "l10n-it", path.replace("/", os.sep))
        if not os.path.exists(dst):
            check(False, "OUTPUT_EXISTS", path)
            continue
        a = open(src, encoding="utf-8", newline="").read().splitlines()
        b = open(dst, encoding="utf-8", newline="").read().splitlines()
        same_shape = len(a) == len(b) and all(
            len(tokenize(x)) == len(tokenize(y)) for x, y in zip(a, b))
        changed = sum(1 for x, y in zip(a, b) if x != y)
        check(same_shape, "STRUCTURE", f"{path}: line/token counts identical")
        want = expected_changed.get(path, 0)
        check(changed == want, "CHANGED_LINES",
              f"{path}: {changed} lines changed, {want} differ from English")

    status = subprocess.run(["git", "-C", REPO, "status", "--porcelain"],
                            capture_output=True, text=True, timeout=60)
    check(status.stdout.strip() == "", "REPO_CLEAN", "repository untouched")
    head = subprocess.run(["git", "-C", REPO, "rev-parse", "HEAD"],
                          capture_output=True, text=True, timeout=60).stdout.strip()
    check(head == EXPECTED_COMMIT, "REPO_COMMIT", head[:12])

    print()
    if failures:
        print(f"RESULT: FAIL — {len(failures)} problems")
        return 1
    print(f"RESULT: PASS — {units} units · {len(approved)} approved · {len(batches)} batches · repository clean")
    return 0


if __name__ == "__main__":
    sys.exit(main())
