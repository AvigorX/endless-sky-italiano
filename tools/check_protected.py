"""Verifica dei file protetti: legge protected.sha256 (CRLF-safe) e confronta.

Uso: python review/check_protected.py            -> verifica
     python review/check_protected.py --update   -> riscrive i digest (solo con autorizzazione)
Exit 0 = tutti integri, 1 = almeno un file alterato o mancante.
"""
import hashlib
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIST = os.path.join(ROOT, "staging", "editorial", "tools", "protected.sha256")


def entries():
    out = []
    with open(LIST, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip().replace("\r", "")
            if not line:
                continue
            digest, path = line.split(None, 1)
            out.append((digest, path.strip()))
    return out


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main(argv):
    bad = 0
    rows = entries()
    update = "--update" in argv
    new = []
    for digest, path in rows:
        full = os.path.join(ROOT, path)
        if not os.path.exists(full):
            print(f"MISSING  {path}")
            bad += 1
            continue
        got = sha(full)
        if got != digest:
            print(f"CHANGED  {path}\n  atteso {digest}\n  reale  {got}")
            bad += 1
        else:
            print(f"OK       {path}")
        new.append((got, path))
    if update:
        with open(LIST, "w", encoding="utf-8", newline="\n") as fh:
            for d, p in new:
                fh.write(f"{d}  {p}\n")
        print("protected.sha256 aggiornato")
    print(f"\n{len(rows) - bad}/{len(rows)} integri")
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
