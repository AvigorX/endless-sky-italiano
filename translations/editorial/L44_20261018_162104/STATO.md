# L44 — stato di avanzamento (CHIUSO 2026-10-18)

Lotto `L44_20261018_162104` · `data/sheragi/archaeology missions.txt` · righe 16–1718 ·
**625/625 unità**. Ventiquattresimo file completo dello staging. Tutti i numeri sono misurati, non stimati.

## Fatto

- `source.json`: 625 unità, 33 contesti (`Deep Archaeology 1` … `Sheragi Archaeology: Epilogue`), kind
  535 `MISSION_TEXT` / 30 `DESCRIPTION` / 28 `VALUE` / **12 `LOGBOOK`** / 10 `DIALOG` / 10 `UI_LABEL`.
  Nessun `CONVERSATION`, nessun `TEXT`, nessuna quadra.
- `check.py` derivato da L43 con **`NT` = 10 `UI_LABEL`** e il **controllo `LOGBOOK` positivo** (12 attese,
  12 tradotte, nessuna identica all'inglese) al posto dell'asserzione di assenza; costruttore dei tab
  riusato tal quale.
- 13 parti, tutte a fine contesto: 50 · 50 · 50 · 50 · 50 · 50 · 50 · 50 · 50 · 50 · 50 · 50 · 25.
- `translation.json`: 625 unità, 18.966 EN → 17.522 IT (0,924), rapporto per unità 0,61–1,77,
  sha256[:16] `2a83b689b3604483`.
- `verify.py`: **37 controlli**, `FAIL: 0`, exit 0. Copertura **625/625**, coppia di righe **(16, 1718)**,
  controllo `LOGBOOK` positivo con identificazione delle 5 righe a tre argomenti, insieme delle 17
  virgolette dispari.
- `review.md`, `REPORT.md`, questo `STATO.md`.

## Regole applicate

- **10 `UI_LABEL`, indici nuovi** (204, 216, 244, 286, 290, 453, 459, 510, 569, 576): lista rimisurata,
  nessun indice in comune con i 36 di L43.
- **`LOGBOOK` 12**: il controllo è stato **riscritto in positivo**. Cinque righe sono
  `log "Categoria" "Nome" `testo``: l'unità è solo il testo, categoria e nome restano in inglese (lacuna
  di inventario di `tools/l10n.py`, protetto). Le cinque sono 49 (People/Albert Foster), 180
  (Factions/Sheragi), 409 (People/Desyo), 410 (People/Rakei), 411 (People/Eyama) — tutte con nomi propri
  invarianti, quindi il difetto è cosmetico ma **dichiarato**.
- **Tab 483**: nessuna traduzione scritta con `\t`; il costruttore li aggiunge e la parità è verificata
  per unità (483 unità su 625 iniziano con tab).
- **17 virgolette dispari** (209, 249, 260, 262, 269, 302, 322, 367, 369, 379, 383, 388, 477, 478, 502,
  522, 542): battute aperte nel sorgente, riprodotte aperte; confronto come insieme di idx.
- **Lessico nuovo registrato**: `the Deep` → **il Deep** (invariato, come nei lotti precedenti), `Dirt
  Belt` invariato, `the Rim` → **il Bordo**, `Sheragi` / `Emerald Sword` → **Spada di Smeraldo** (nome
  tradotto perché il testo stesso lo spiega come traduzione), `Dragonflame Cannon` → **Cannone Fiamma di
  Drago**, `GRASER` invariato, `black box` → **scatola nera**, `hatchery` → **cova**, `the Unfettered` →
  **gli Slegati**, `Quarg ringworld` → **ringworld dei Quarg**.

## Verifica

```
python staging/editorial/L44_20261018_162104/check.py    → FAIL totale: 0 (25 controlli)
python staging/editorial/L44_20261018_162104/verify.py   → exit 0, 37 controlli, FAIL: 0
```

## Non fatto (dichiarato)

- **Nessuna approvazione nel database**: le 625 unità sono `PENDING`.
- **Nessun caricamento nel gioco**: la traduzione non è mai stata letta da Endless Sky né vista a
  schermo. In particolare non è verificato il percorso Deep Archaeology → Spada di Smeraldo (33 contesti,
  molti `goto`) né che la Spada di Smeraldo compaia con il nome tradotto nel cantiere.
- **Nessun test di gameplay** della linea Sheragi.
