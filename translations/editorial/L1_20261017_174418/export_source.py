#!/usr/bin/env python3
"""L1 — esporta il blocco da tradurre con tracciabilita' fino alla riga originale.

Sola lettura su state.db e sul repository del gioco. Verifica che il testo
dell'unita' compaia nella riga indicata e ne registra delimitatore e tab iniziale.
"""
import json
import os
import sqlite3
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WS = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
GAME = os.path.join(os.path.dirname(WS), "endless-sky")
PATH = "data/map planets.txt"
LO, HI = 3851, 4295


def main() -> int:
    con = sqlite3.connect("file:%s?mode=ro" % os.path.join(WS, "state.db"), uri=True)
    con.row_factory = sqlite3.Row
    rows = con.execute(
        "SELECT id,path,line,kind,context,english,english_hash,state FROM units"
        " WHERE path=? AND line BETWEEN ? AND ? AND state='PENDING' ORDER BY line",
        (PATH, LO, HI)).fetchall()

    lines = open(os.path.join(GAME, PATH), encoding="utf-8").read().splitlines()
    units, problems = [], []
    for r in rows:
        raw = lines[r["line"] - 1]
        en = r["english"]
        delim = "backtick" if "`" + en + "`" in raw else ("quote" if '"' + en + '"' in raw else "?")
        if en not in raw:
            problems.append(f"{r['line']}: testo non trovato nella riga")
        units.append({
            "idx": len(units) + 1,
            "id": r["id"],
            "path": r["path"],
            "line": r["line"],
            "kind": r["kind"],
            "context": r["context"],
            "english": en,
            "delimiter": delim,
            "leading_tab": en.startswith("\t"),
            "raw": raw,
            "english_hash": r["english_hash"],
        })

    source = {
        "phase": "L1 — traduzione editoriale diretta",
        "block": {"path": PATH, "line_from": LO, "line_to": HI, "units": len(units)},
        "note": "unita' consecutive per riga; le righe intermedie sono struttura del file",
        "units": units,
    }
    with open(os.path.join(HERE, "source.json"), "w", encoding="utf-8") as fh:
        json.dump(source, fh, indent=1, ensure_ascii=False)

    print(f"unita': {len(units)} · parole: {sum(len(u['english'].split()) for u in units)}")
    print("delimitatori:", {d: sum(1 for u in units if u['delimiter'] == d) for d in ('backtick', 'quote', '?')})
    print("con tab iniziale:", sum(1 for u in units if u["leading_tab"]))
    print("problemi:", problems or "nessuno")
    return 0 if not problems and len(units) == 120 else 1


if __name__ == "__main__":
    sys.exit(main())
