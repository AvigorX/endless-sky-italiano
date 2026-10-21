#!/usr/bin/env python3
"""L1 — assembla translation.json e applica un controllo temporaneo del blocco.

Non e' un validatore di pipeline: nessun database, nessuno stato, nessuna regola
nuova. Confronta soltanto source.json con le traduzioni prodotte a mano.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PARTS = sorted(f for f in os.listdir(os.path.join(HERE, "parts")) if f.endswith(".json"))
TOKEN = re.compile(r"<[^<>\n]{1,50}>")
ENGLISH = re.compile(r"\b(the|and|of|that|with|from|was|were|is|are|this|which|their)\b", re.I)


def main() -> int:
    source = json.load(open(os.path.join(HERE, "source.json"), encoding="utf-8"))
    units = {u["idx"]: u for u in source["units"]}

    tr = {}
    for name in PARTS:
        part = json.load(open(os.path.join(HERE, "parts", name), encoding="utf-8"))
        for k, v in part.items():
            idx = int(k)
            if idx in tr:
                print(f"FATAL: indice {idx} duplicato ({name})")
                return 1
            tr[idx] = v

    missing = sorted(set(units) - set(tr))
    extra = sorted(set(tr) - set(units))
    if missing or extra:
        print(f"FATAL: mancanti {missing[:10]} estranei {extra[:10]}")
        return 1

    rows, problems, notes = [], [], []
    for idx in sorted(units):
        u, it = units[idx], tr[idx]
        if not it.strip():
            problems.append({"idx": idx, "code": "EMPTY"})
        if it.count("\t") != u["english"].count("\t"):
            problems.append({"idx": idx, "code": "TAB", "detail": f"{u['english'].count(chr(9))}->{it.count(chr(9))}"})
        if u["leading_tab"] != it.startswith("\t"):
            problems.append({"idx": idx, "code": "LEADING_TAB"})
        if it.count('"') != u["english"].count('"'):
            problems.append({"idx": idx, "code": "QUOTE", "detail": f"{u['english'].count(chr(34))}->{it.count(chr(34))}"})
        if sorted(TOKEN.findall(it)) != sorted(TOKEN.findall(u["english"])):
            problems.append({"idx": idx, "code": "TOKEN"})
        if "  " in it or it != it.rstrip():
            problems.append({"idx": idx, "code": "WHITESPACE"})
        # residuo inglese: parole funzionali inglesi nel testo italiano
        hits = [w.lower() for w in ENGLISH.findall(it)]
        if hits:
            notes.append({"idx": idx, "code": "ENGLISH_WORD", "words": sorted(set(hits))})
        ratio = len(it) / max(1, len(u["english"]))
        rows.append({
            "idx": idx, "id": u["id"], "path": u["path"], "line": u["line"],
            "context": u["context"], "english": u["english"], "italian": it,
            "ratio": round(ratio, 2),
        })

    with open(os.path.join(HERE, "translation.json"), "w", encoding="utf-8") as fh:
        json.dump({"block": source["block"], "units": rows}, fh, indent=1, ensure_ascii=False)

    words_en = sum(len(r["english"].split()) for r in rows)
    words_it = sum(len(r["italian"].split()) for r in rows)
    ratios = [r["ratio"] for r in rows]
    result = {
        "units": len(rows), "words_en": words_en, "words_it": words_it,
        "ratio_min": min(ratios), "ratio_max": max(ratios),
        "problems": problems, "notes": notes,
        "checks": {
            "ids_complete": not missing and not extra,
            "tabs": not any(p["code"] in ("TAB", "LEADING_TAB") for p in problems),
            "quotes": not any(p["code"] == "QUOTE" for p in problems),
            "tokens": not any(p["code"] == "TOKEN" for p in problems),
            "no_empty": not any(p["code"] == "EMPTY" for p in problems),
        },
    }
    with open(os.path.join(HERE, "check_results.json"), "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=1, ensure_ascii=False)

    print(f"unità {len(rows)} · parole {words_en} -> {words_it} · ratio {min(ratios)}-{max(ratios)}")
    print("controlli:", result["checks"])
    print(f"problemi: {len(problems)} · note inglese: {len(notes)}")
    if problems:
        print(json.dumps(problems[:5], ensure_ascii=False, indent=1))
    if notes:
        print("parole inglesi residue:", [(n["idx"], n["words"]) for n in notes])
    return 0


if __name__ == "__main__":
    sys.exit(main())
