"""Estrae il testo delle news/hail che l'estrattore ufficiale non vede.

Perche' esiste: `l10n_inventory.py` scarta le righe composte da una sola stringa
(le alternative dei blocchi `word`), che sono il corpo delle notizie e degli hail.
Qui quelle righe diventano unità di un NUOVO lotto di staging, senza toccare
`tools/l10n.py`, `l10n_inventory.py` né `state.db`.

Le unità hanno la stessa forma di quelle ufficiali
(`<contesto>|<chiave>|<riga>|<indice>`) così `apply_translations.py` le applica
senza modifiche.

Uso:
  python review/extract_news_units.py <file1> [<file2> ...] --lot <nome> [--dry-run]
"""
import argparse
import json
import os
import re
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.abspath(os.path.join(ROOT, "..", "endless-sky"))


class Scan:
    def __init__(self, text):
        self.s = text
        self.i = 0
        self.n = len(text)
        self.line = 1

    def tokens(self):
        """Token (testo, tipo) della riga corrente, tipo in quoted/backtick/bare."""
        out = []
        while self.i < self.n:
            c = self.s[self.i]
            if c == "\n":
                break
            if c in " \t\r":
                self.i += 1
                continue
            if c == "#":
                while self.i < self.n and self.s[self.i] != "\n":
                    self.i += 1
                break
            if c in "\"`":
                q = c
                self.i += 1
                buf = []
                while self.i < self.n and self.s[self.i] != q:
                    if self.s[self.i] == "\\" and self.i + 1 < self.n:
                        buf.append(self.s[self.i])
                        self.i += 1
                    buf.append(self.s[self.i])
                    self.i += 1
                self.i += 1
                out.append(("".join(buf), "quoted" if q == '"' else "backtick"))
                continue
            start = self.i
            while self.i < self.n and self.s[self.i] not in " \t\r\n#":
                self.i += 1
            out.append((self.s[start:self.i], "bare"))
        return out


def units_for(path_rel):
    path = os.path.join(REPO, *path_rel.split("/"))
    text = open(path, encoding="utf-8").read()
    sc = Scan(text)
    stack = []           # (indent, key)
    rows = []
    while sc.i < sc.n:
        start = sc.i
        toks = sc.tokens()
        line = text.count("\n", 0, start) + 1
        indent = len(text[start:start + 80]) - len(text[start:start + 80].lstrip(" \t"))
        if sc.i < sc.n and text[sc.i] == "\n":
            sc.i += 1
        if not toks:
            continue
        key = toks[0][0]
        while stack and stack[-1][0] >= indent:
            stack.pop()
        chain = [k for _, k in stack if k]
        ctx = ""
        # contesto = oggetto radice (news "nome" / phrase "nome")
        for k in chain:
            if k:
                ctx = k
                break
        parent = chain[-1] if chain else ""
        if len(toks) == 1 and toks[0][1] in ("quoted", "backtick") and parent in ("word", "sentence"):
            value = toks[0][0]
            # Le `phrase` tecniche (orologio Remnant: "00".."07", cifre, cifre esadecimali)
            # non sono testo: senza almeno due lettere non c'e' nulla da tradurre.
            if value.strip() and value.strip() != '"' and re.search(r"[A-Za-z]{2}", value):
                rows.append({"path": path_rel, "line": line, "key": parent,
                             "context": ctx, "english": value})
        else:
            stack.append((indent, key))
    return rows


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--lot", required=True)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args(argv)

    allrows = []
    for f in a.files:
        r = units_for(f)
        allrows += r
        if r:
            w = sum(len(x["english"].split()) for x in r)
            print(f"  {f:44s} {len(r):5d} unità · {w:6d} parole")
    print(f"totale: {len(allrows)} unità · {sum(len(x['english'].split()) for x in allrows)} parole")
    print("per blocco:", dict(Counter(x["key"] for x in allrows)))
    if a.dry_run:
        return 0

    lot = os.path.join(ROOT, "staging", "editorial", a.lot)
    os.makedirs(os.path.join(lot, "parts"), exist_ok=True)
    units = []
    for idx, x in enumerate(allrows, 1):
        stem = os.path.splitext(os.path.basename(x["path"]))[0].replace(" ", "_")
        units.append({"idx": idx, "id": f"N|{stem}|{x['key']}|{x['line']}|0",
                      "path": x["path"], "line": x["line"], "kind": "NEWS",
                      "context": x["context"], "english": x["english"]})
    json.dump({"block": {"path": ", ".join(a.files), "line_from": 0, "line_to": 0,
                         "units": len(units)},
               "note": "estrazione delle alternative `word` non viste dall'estrattore ufficiale",
               "units": units},
              open(os.path.join(lot, "source.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print(f"lotto creato: {os.path.relpath(lot, ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
