#!/usr/bin/env python3
"""Generate REPORT.md and qa/pilot_translations.md from the pipeline state."""

import json
import os
import sqlite3
from datetime import datetime, timezone

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(WS, "state.db")


def main() -> int:
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    units = con.execute(
        "SELECT * FROM units WHERE state='APPROVED' ORDER BY path, line").fetchall()
    batches = con.execute("SELECT * FROM batches ORDER BY id").fetchall()
    total = con.execute("SELECT COUNT(*) FROM units").fetchone()[0]
    issues = con.execute(
        "SELECT code, severity, COUNT(*) n FROM issues GROUP BY code, severity ORDER BY n DESC").fetchall()
    non_ascii = sum(1 for u in units if any(ord(c) > 127 for c in (u["italian"] or "")))
    words_done = sum(len(u["english"].split()) for u in units)
    progress = json.load(open(os.path.join(WS, "progress.json"), encoding="utf-8"))
    apply_report = json.load(open(os.path.join(WS, "qa", "apply_report.json"), encoding="utf-8"))

    # per-unit table for human review
    with open(os.path.join(WS, "qa", "pilot_translations.md"), "w", encoding="utf-8") as fh:
        fh.write("# Lotto pilota — traduzioni approvate\n\n")
        fh.write(f"{len(units)} unità · {words_done} parole · generato {datetime.now(timezone.utc):%Y-%m-%d %H:%M UTC}\n\n")
        fh.write("| file | riga | inglese | italiano |\n|---|---:|---|---|\n")
        for u in units:
            en = u["english"].replace("|", "\\|").replace("\n", " ")
            it = u["italian"].replace("|", "\\|").replace("\n", " ")
            fh.write(f"| `{u['path']}` | {u['line']} | {en} | {it} |\n")

    with open(os.path.join(WS, "REPORT.md"), "w", encoding="utf-8") as fh:
        fh.write("# Pipeline di localizzazione IT — stato e risultati\n\n")
        fh.write(f"Generato: {datetime.now(timezone.utc):%Y-%m-%d %H:%M UTC}\n\n")
        fh.write("## 1. Cosa fa il pipeline\n\n")
        fh.write("Stato in SQLite, batch deterministici, traduzione, validazione meccanica, "
                 "applicazione su **copia** con verifica strutturale. "
                 "Il repository di gioco è aperto in sola lettura.\n\n")
        fh.write("## 2. Numeri\n\n")
        fh.write(f"- Unità in inventario: **{total}**\n")
        fh.write(f"- Approvate: **{len(units)}** ({progress['coverage']*100:.3f}%)\n")
        fh.write(f"- Parole tradotte: **{words_done}**\n")
        fh.write(f"- Con caratteri accentati (bloccati dal font attuale): **{non_ascii}**\n")
        fh.write(f"- Batch: {len(batches)}\n\n")
        fh.write("| batch | ambito | unità | stato |\n|---|---|---:|---|\n")
        for b in batches:
            fh.write(f"| {b['id']} | {b['name']} | {b['units']} | {b['status']} |\n")
        fh.write("\n## 3. Validazione\n\n")
        fh.write("| codice | severità | occorrenze |\n|---|---|---:|\n")
        for i in issues:
            fh.write(f"| {i['code']} | {i['severity']} | {i['n']} |\n")
        fh.write("\nControlli bloccanti: `UNKNOWN_ID`, `EMPTY`, `CONTROL_CHAR`, `BACKTICK`, "
                 "`DOUBLE_QUOTE`, `PLACEHOLDER_MISMATCH`, `TAB_LOST`, `MISSING_RESULT`, `DUPLICATE_ID`.\n"
                 "Consultivi: `UNTRANSLATED`, `LENGTH_RATIO`, `NON_ASCII`, `GLOSSARY`.\n\n")
        fh.write("## 4. Integrazione\n\n")
        fh.write("| file | unità | esito |\n|---|---:|---|\n")
        for f in apply_report["files"]:
            fh.write(f"| `{f['path']}` | {f['units']} | {'OK' if f['ok'] else 'FALLITO'} — {f['detail']} |\n")
        fh.write("\nVerifica: dopo la sostituzione il file viene ri-tokenizzato e confrontato riga per riga "
                 "con l'originale. Deve cambiare **un solo token per riga**, con lo stesso delimitatore e lo "
                 "stesso numero di token. Un fallimento annulla la scrittura del file.\n\n")
        fh.write("## 5. Limiti (dichiarati)\n\n")
        fh.write("1. **Il gioco non è stato avviato**: nessuna build disponibile. La validazione è strutturale, non visiva.\n")
        fh.write("2. **Il font non renderizza le lettere accentate** (audit IT-002): i testi sono corretti ma "
                 "illeggibili finché l'atlante non viene esteso. Il pipeline lo segnala come `NON_ASCII`.\n")
        fh.write("3. **Nessun selettore di lingua** nel motore: l'output è una copia modificata dei dati, non un plugin attivo.\n")
        fh.write("4. La copertura è **0,86%** (lotto pilota): non è una localizzazione completa.\n")
        fh.write("5. I giudizi di qualità linguistica sono miei, non di un revisore umano.\n\n")
        fh.write("## 6. Prossimo passo\n\n")
        fh.write("Estendere l'atlante font e il selettore lingua (fase 1 del piano di remediation), poi "
                 "proseguire con i lotti per famiglia: `_ui/` è già coperto al 26% (284/1089), "
                 "il resto è `PENDING` e ripartibile con `l10n.py build`.\n")

    print(f"REPORT.md + qa/pilot_translations.md · {len(units)} units · {words_done} words")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
