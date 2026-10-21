# L43 — stato di avanzamento (CHIUSO 2026-10-18)

Lotto `L43_20261018_160846` · `data/remnant/remnant 2 side missions.txt` · righe 17–775 ·
**299/299 unità**. Ventitreesimo file completo dello staging. Tutti i numeri sono misurati, non stimati.

## Fatto

- `source.json`: 299 unità, 11 contesti (`Remnant: Visit to Paradise 1` … `Remnant: Will Not Someone
  Please Think Of The Children`), kind 235 `MISSION_TEXT` / 36 `UI_LABEL` / 10 `VALUE` / 10 `DESCRIPTION`
  / 8 `DIALOG`. **Nessun `LOGBOOK`, nessun `CONVERSATION`, nessuna quadra.**
- `check.py` derivato da L42 con **`NT` = le 36 `UI_LABEL`** (indici nuovi, elencati uno per uno) e il
  costruttore dei tab riusato tal quale.
- 8 parti, tutte a fine contesto: 41 · 30 · 38 · 39 · 36 · 45 · 29 · 41.
- `translation.json`: 299 unità, 10.539 EN → 9.870 IT (0,936), rapporto per unità 0,65–1,40,
  sha256[:16] `018217f1aac1ba49`.
- `verify.py`: **33 controlli**, `FAIL: 0`, exit 0. Copertura **299/299**, coppia di righe **(17, 775)**,
  asserzioni di assenza per `LOGBOOK` e `CONVERSATION`, insieme delle 11 virgolette dispari.
- `review.md`, `REPORT.md`, questo `STATO.md`.

## Regole applicate

- **36 `UI_LABEL`, indici diversi da L42**: la lista è stata rimisurata sul `source.json`, non copiata.
  `shattered help` e `rather not` compaiono due volte ciascuno (idx 226/253 e 268/291) e restano
  identici, come l'inglese.
- **`LOGBOOK` 0**: nessuna riga `log` in questo file, quindi **nessuna lacuna di inventario possibile**.
  Il controllo nel `verify.py` è un'asserzione di assenza (`log == []`), non un'omissione.
- **Tab 208**: nessuna traduzione scritta con `\t`; il costruttore li aggiunge dal sorgente e la parità è
  verificata per unità (208 unità su 299 iniziano con tab).
- **11 virgolette dispari** (133, 188, 190, 225, 227, 229, 245, 247, 280, 285, 286): battute aperte nel
  sorgente, riprodotte aperte; il `verify.py` confronta l'insieme degli idx.
- **Numeri tecnici invariati**: `11D.E78`, `1.1DE79`, `299.792.458 m/s`, `2.99792458x10^8`,
  `1.1DE784Ax10^7` (le cifre sono formattate alla maniera italiana solo per le migliaia).
- **Lessico nuovo registrato**: `Primary Weft` → **Trama Primaria**, `Secondary Weft` → **Trama
  Secondaria**, `Warp` → **Ordito**, `the Warren` → **la Tana**, `Maudrakoi` / `Zitchal Maudrakoi`
  invariati, `Shattered Light` invariato, `NDR-114 Androids` → **Androidi NDR-114**.

## Verifica

```
python staging/editorial/L43_20261018_160846/check.py    → FAIL totale: 0 (21 controlli)
python staging/editorial/L43_20261018_160846/verify.py   → exit 0, 33 controlli, FAIL: 0
```

## Non fatto (dichiarato)

- **Nessuna approvazione nel database**: le 299 unità sono `PENDING`.
- **Nessun caricamento nel gioco**: la traduzione non è mai stata letta da Endless Sky né vista a schermo.
  In particolare non è verificato che la Celebrazione del Ricordo scorra con i salti `goto` intatti, né
  che le due missioni Shattered Light e Scent of Rain si incatenino correttamente.
- **Nessun test di gameplay** delle trame secondarie Remnant.
