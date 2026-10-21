#!/usr/bin/env python3
"""Build the distributable package: docs, overlay, font, patch, tools, zip."""

import csv
import json
import os
import shutil
import sqlite3
import subprocess
import zipfile
from datetime import datetime, timezone

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(WS, "dist")
VERSION = "0.1.0"
REPO = r"C:\Users\Dave\PROGETTI\G-DEV\GAME-SOURCE-LAB\endless-sky"


def build_coverage(con):
    units = con.execute("SELECT * FROM units").fetchall()
    total = len(units)
    by_state = {}
    for (state,) in con.execute("SELECT DISTINCT state FROM units"):
        by_state[state] = con.execute("SELECT COUNT(*) FROM units WHERE state=?", (state,)).fetchone()[0]
    approved = [u for u in units if u["state"] == "APPROVED"]
    words_done = sum(len(u["english"].split()) for u in approved)
    total_words = sum(len(u["english"].split()) for u in units)
    non_ascii = sum(1 for u in approved if any(ord(c) > 127 for c in (u["italian"] or "")))

    fam = {}
    for u in approved:
        parts = u["path"].split("/")
        key = parts[1] if len(parts) > 2 else "(file radice)"
        fam[key] = fam.get(key, 0) + 1
    kinds = {}
    for u in approved:
        kinds[u["kind"]] = kinds.get(u["kind"], 0) + 1

    lines = [
        "# Copertura — stato misurato", "",
        f"Generato: {datetime.now(timezone.utc):%Y-%m-%d %H:%M UTC} · commit `b4aa3ba`", "",
        "## Base di calcolo", "",
        "Il denominatore è l'inventario completo (`LOCALIZATION_COVERAGE.csv` dell'audit, 41.972 righe):",
        "ogni unità è una stringa con nome stabile, letto dal tokenizer che replica `DataFile.cpp`.",
        "Il numeratore è il numero di unità con stato `APPROVED` nel database del pipeline.",
        "Nessun valore qui è stimato: entrambi i numeri vengono dalle stesse strutture dati.", "",
        "| Metrica | Valore |", "|---|---:|",
        f"| Unità totali localizzabili | {total} |",
        f"| Parole totali | {total_words} |",
        f"| Unità approvate | {by_state.get('APPROVED', 0)} |",
        f"| Parole tradotte | {words_done} |",
        f"| Copertura (unità) | {by_state.get('APPROVED',0)/total*100:.3f}% |",
        f"| Copertura (parole) | {words_done/total_words*100:.3f}% |",
        f"| Approvate con caratteri accentati | {non_ascii} |", "",
        "## Stati", "", "| Stato | Unità |", "|---|---:|",
    ]
    for k, v in sorted(by_state.items(), key=lambda kv: -kv[1]):
        lines.append(f"| {k} | {v} |")
    lines += ["", "## Unità approvate per famiglia", "", "| Famiglia | Unità |", "|---|---:|"]
    for k, v in sorted(fam.items(), key=lambda kv: -kv[1]):
        lines.append(f"| `{k}` | {v} |")
    lines += ["", "## Unità approvate per tipo", "", "| Tipo | Unità |", "|---|---:|"]
    for k, v in sorted(kinds.items(), key=lambda kv: -kv[1]):
        lines.append(f"| {k} | {v} |")
    lines += ["", "## Esclusioni dichiarate", "",
              "- **Identificatori** (9.048): nomi di oggetti e chiavi di attributo. Non traducibili in place;",
              "  richiedono `display name` o una mappa chiave→etichetta.",
              "- **`data/_deprecated`** (55 unità): caricate dal motore, non incluse finché non si decide il perimetro.",
              "- **Stringhe C++** (~4.339 candidate, stima): fuori dalla portata di un overlay di dati.",
              "- **`phrase`/`word`** (868): generano nomi propri; decisione di prodotto pendente.",
              "", "## Unità approvate: elenco completo", "",
              "Vedi `pilot_translations.md` nel workspace (`qa/`), con inglese e italiano affiancati.", ""]
    return "\n".join(lines)


def build_qa():
    checks = []
    for label, cmd in (
        ("validate_pipeline.py", ["python", "tools/validate_pipeline.py"]),
        ("validate_audit.py", ["python", "tools/validate_audit.py"]),
    ):
        try:
            proc = subprocess.run(cmd, cwd=WS if "pipeline" in cmd[1] else
                                  r"C:\Users\Dave\PROGETTI\G-DEV\GAME-SOURCE-LAB\endless-sky-l10n-audit",
                                  capture_output=True, text=True, timeout=300)
            checks.append((label, proc.returncode, proc.stdout.strip().splitlines()[-6:]))
        except Exception as exc:  # noqa: BLE001
            checks.append((label, 99, [str(exc)]))

    font = json.load(open(os.path.join(WS, "font", "font_report.json"), encoding="utf-8"))
    apply_report = json.load(open(os.path.join(WS, "qa", "apply_report.json"), encoding="utf-8"))

    lines = ["# QA — verifiche effettivamente eseguite", "",
             f"Generato: {datetime.now(timezone.utc):%Y-%m-%d %H:%M UTC}", "",
             "## 1. Validatori", ""]
    for label, code, tail in checks:
        lines.append(f"### `{label}` — exit {code}")
        lines.append("```")
        lines += tail
        lines.append("```")
        lines.append("")
    lines += ["## 2. Applicazione dell'overlay", ""]
    for f in apply_report["files"]:
        lines.append(f"- `{f['path']}`: {f['units']} unità, {'OK' if f['ok'] else 'FALLITO'} — {f['detail']}")
    lines += ["", "La verifica ri-tokenizza il file patchato e lo confronta riga per riga con l'originale:",
              "stesso numero di righe, stesso numero di token, **un solo token diverso per riga**.",
              "Un fallimento annulla la scrittura del file.", "", "## 3. Atlante font", ""]
    for a in font["atlases"]:
        lines.append(f"- `{a['atlas']}` → `{a['out']}`: {a['cells_out']} celle da {a['cell']}×{a['height']}, "
                     f"larghezza {a['new_width']} px")
        lines.append(f"  - celle ASCII identiche all'originale: **{a['base_cells_identical']}**")
        lines.append(f"  - 12 glifi critici con inchiostro: **{a['critical_ok']}**")
        for ch, st in a["critical_glyphs"].items():
            lines.append(f"    - `{ch}`: {st['ink']} px, bbox {st['bbox']}")
    lines += ["", "## 4. Cosa NON è stato verificato (e perché)", "",
              "| Verifica richiesta | Stato | Causa |", "|---|---|---|",
              "| Build del gioco | **non eseguita** | nessun compilatore, nessun CMake nell'ambiente |",
              "| Avvio e schermate | **non eseguita** | nessun binario compilato |",
              "| Rendering reale degli accenti | **non eseguito** | richiede build + screenshot |",
              "| Selettore lingua | **non implementato** | modifica al loader non testabile senza build |",
              "| Test missioni/dialoghi | **non eseguiti** | nessun runtime |", "",
              "## 5. Punto di innesto per il selettore lingua", "",
              "Se e quando sarà disponibile una build:", "",
              "1. `source/Preferences.{h,cpp}` — aggiungere `language` (string, default `en`) con getter e",
              "   persistenza, sul modello di `GetDateFormat()`.",
              "2. `source/GameData.cpp` (`BeginLoad`, ~riga 154-173) — costruire l'elenco `sources` e, se",
              "   `language != \"en\"`, accodare `Files::Resources() / \"l10n\" / language` come ultima sorgente,",
              "   così che i file di traduzione siano caricati dopo l'inglese e possano sovrascriverlo.",
              "3. `source/UniverseObjects.cpp` (`Load`, ~riga 40-80) — nessuna modifica se si usa il punto 2:",
              "   `Files::RecursiveList` percorre già ogni sorgente.",
              "4. `source/PreferencesPanel.cpp` — aggiungere il controllo UI nella sezione Interface.",
              "5. Verifica obbligatoria: avvio con `l10n/it` assente (deve restare inglese, senza errori)," ,
              "   poi con `l10n/it` presente (deve mostrare italiano), poi ritorno a `en`.", ""]
    return "\n".join(lines)


TOKEN = """# Report di esecuzione, benchmark e uso del modello

## 1. Motore di traduzione: cosa esiste davvero

| Elemento | Stato verificato |
|---|---|
| Provider configurato | DeepSeek, `base_url = https://api.deepseek.com/v1` |
| Tipo di credenziale | `api_key`, `source: env:DEEPSEEK_API_KEY` |
| Chiave leggibile dalla shell? | **No** — l'entry in `auth.json` contiene solo fingerprint e metadati; la variabile non è presente nell'ambiente del processo |
| Server locale (ollama/vLLM) | **No** — 11434, 8000, 8080, 9090 non rispondono |
| Endpoint OpenAI-compatibile raggiungibile con chiave | **Non testato**: senza chiave non è possibile autenticare |

Conseguenza: il worker è pronto per `--engine api`, ma in questa sessione non può autenticarsi.
**Requisito esatto per sbloccarlo:** esportare `DEEPSEEK_API_KEY` nel processo del worker
(`export DEEPSEEK_API_KEY=...`) oppure autorizzare la lettura del segreto dal credential store di Hermes.
Nessun segreto è stato stampato o copiato su disco.

## 2. Benchmark B004 (eseguito)

| Metrica | Valore |
|---|---|
| Unità | 25 |
| Parole sorgente | 644 |
| Parole italiane | 581 |
| Import + validazione | 0,95 s |
| Errori bloccanti | 0 |
| Avvisi | 11 (8 `NON_ASCII`, 3 `GLOSSARY`) |
| Retry | 0 |
| Modifiche al pipeline dopo il batch | nessuna |

Il batch ha confermato il comportamento atteso: tab di paragrafo preservati, segnaposto
(`<View player info>`, `<Fleet: Harvest flotsam>`) intatti, riferimenti ai pulsanti allineati
alle etichette italiane già tradotte.

## 3. Produzione cumulata

| Metrica | Valore |
|---|---|
| Batch | 5 (`B001`…`B005`) |
| Unità approvate | 352 |
| Parole inglesi tradotte | 3.530 |
| Copertura (unità) | 1,069% |
| Copertura (parole) | 0,360% |
| Errori bloccanti | 0 |
| Unità in `NEEDS_REVIEW` | 0 |

## 4. Worker (`tools/worker.py`)

- `--engine api`: chiama `/chat/completions` con `DEEPSEEK_API_KEY`, `response_format=json_object`,
  parsing tollerante (estrae il JSON anche da prose/fence), verifica **esatta** degli id,
  retry con backoff esponenziale (max 3), log in tabella `runs` (unità, parole, token se forniti,
  durata, retry, stato).
- `--engine file`: genera `batches/<id>/prompt.md` (glossario + regole di stile + unità) e attende
  un traduttore esterno; `--import` valida e applica.
- Test eseguiti: `api` senza chiave → exit 2 con messaggio esplicito; `file` → prompt da 6.666
  caratteri, exit 0; import del batch → `APPROVED`, overlay applicato.

## 5. Costo

Non determinabile: nessuna chiamata API è stata completata, quindi non esistono token fatturati
da riportare. Qualunque cifra sarebbe inventata.

## 6. Riproducibilità

```bash
python tools/worker.py --engine api --batch B006 --where "path='data/_ui/help.txt'" --limit 60
python tools/worker.py --engine file --batch B006 --where "path='data/_ui/help.txt'" --limit 60
python tools/worker.py --import B006
python tools/apply_patch.py B006
python tools/validate_pipeline.py
python tools/package.py
```
"""


def main() -> int:
    con = sqlite3.connect(os.path.join(WS, "state.db"))
    con.row_factory = sqlite3.Row

    docs = os.path.join(DIST, "docs")
    os.makedirs(docs, exist_ok=True)
    open(os.path.join(docs, "COVERAGE.md"), "w", encoding="utf-8").write(build_coverage(con))
    open(os.path.join(docs, "QA.md"), "w", encoding="utf-8").write(build_qa())
    open(os.path.join(docs, "TOKEN_REPORT.md"), "w", encoding="utf-8").write(TOKEN)

    # copy payloads
    for src, dst in (
        (os.path.join(WS, "output", "l10n-it"), os.path.join(DIST, "l10n-it")),
        (os.path.join(WS, "font"), os.path.join(DIST, "font")),
        (os.path.join(WS, "patches"), os.path.join(DIST, "patches")),
        (os.path.join(WS, "tools"), os.path.join(DIST, "tools")),
    ):
        if os.path.exists(dst):
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
    for f in ("glossary.csv", "style_guide.md", "manifest.json"):
        shutil.copy(os.path.join(WS, f), os.path.join(docs, f))

    # zip
    zip_path = os.path.join(DIST, f"endless-sky-it-{VERSION}.zip")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for root, _dirs, files in os.walk(DIST):
            if os.path.abspath(root).startswith(os.path.abspath(DIST)) and ".zip" in root:
                continue
            for f in files:
                if f.endswith(".zip"):
                    continue
                full = os.path.join(root, f)
                z.write(full, os.path.relpath(full, DIST))
    size = os.path.getsize(zip_path)
    with zipfile.ZipFile(zip_path) as z:
        count = len(z.namelist())
    print(f"{zip_path}: {count} file, {size/1024:.1f} KB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
