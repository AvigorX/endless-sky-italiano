# L52 — stato di avanzamento (CHIUSO 2026-10-18)

Lotto `L52_20261018_172541` · `data/avgi/avgi 0 first contact.txt` · righe 873–1120 ·
**135/135 unità**. **Chiude il file**: 406/406 con L50 (119) e L51 (152) — **ventottesimo file
completo** dello staging. Tutti i numeri sono misurati, non stimati.

## Fatto

- `source.json`: 135 unità, **5 contesti** (`Avgi: Dissonance Outreach` 1–16, `Avgi: Twilight Escape 1`
  17–76, `Avgi: Twilight Escape 2` 77–91, `Avgi: Twilight Escape 3` 92–133,
  `Discovery of Decet Magnetar` 134–135), kind 106 `MISSION_TEXT` / **17 `LOGBOOK`** / 4 `VALUE` /
  4 `DESCRIPTION` / 3 `DIALOG` / **1 `UI_LABEL`**.
- `check.py` derivato da L51 con `NT` di **nuovo a 1** (unità 57, `unknown ember waste`): lo zero di L51
  non si eredita e nemmeno l'uno, entrambi si rimisurano. `LOGBOOK` positivo su 17, `DIALOG` positivo su
  3, assenze dichiarate per `TEXT`, `CONVERSATION`, quadre, backtick, virgolette dispari.
- 4 parti: **40 · 36 · 33 · 26**.
- `translation.json`: 135 unità, 3.538 EN → 3.373 IT (0,953), rapporto per unità 0,68–1,60,
  sha256[:16] `d529e6f657dc9aef`.
- `verify.py`: **44 controlli**, `FAIL: 0`, exit 0. **Chiude il file** (271 prima / **0 dopo**,
  `max(line) = 1120`), copertura **406/406 su tre lotti** (119 + 152 + 135) senza sovrapposizioni,
  `NT` 1, `LOGBOOK` 17 con forme 10+7+0, `DIALOG` 3, parità di tab/virgolette/token per unità,
  **nessuna unità duplicata in inglese**.
- `review.md`, `REPORT.md`, questo `STATO.md`.

## Regole applicate

- **L'invariante «di file» torna legittimo**, ma solo perché la 1120 è l'ultima riga: `verify.py` lo
  scrive insieme a «0 unità dopo la 1120» e `max(line) = 1120`. Se il file crescesse, il controllo
  diventerebbe rosso e andrebbe riscritto per segmento (decisione 166).
- **`NT` = 1**: `label "unknown ember waste"` (unità 57) è un'etichetta di salto e resta identica.
  Nessun riferimento di dato: tutte le 17 righe `LOGBOOK` hanno il testo nell'unità.
- **`LOGBOOK` 17**, il numero più alto della linea Avgi: 10 a tre argomenti (`People`/`Factions`) e
  7 fra backtick, **0 dirette**. Nessuna categoria estratta.
- **Nessuna unità duplicata in inglese** in tutto il lotto (0 gruppi): è il primo caso nella serie Avgi.
  Il controllo «nessuna resa italiana ripetuta fra unità diverse» è quindi un invariante pieno, non
  filtrato da eccezioni.
- **Lessico**: `Dissonance` invariato come nome del movimento → **la Dissonanza** (già in L48) ·
  `polities` → **entità politiche** · `gateway` → **varco** · `magnetar` **invariato** ·
  `Antecessors` **invariato** (forma del corpus) · `Ember Waste` **invariato** (5 occorrenze nel corpus,
  e l'etichetta 57 è un `label` che non si tocca) · `Outpost Tekis` → **Avamposto Tekis** ·
  `price controls` → **controlli sui prezzi** · `backpay` → **arretrati** · `skinsuits` → **tute di pelle**.

## Verifica

```
python staging/editorial/L52_20261018_172541/check.py    → FAIL totale: 0 (31 controlli)
python staging/editorial/L52_20261018_172541/verify.py   → exit 0, 44 controlli, FAIL: 0
```

`state.py` dopo L52: **23.255 unità · 740.175 EN · 702.232 IT**, `ESITO: OK`,
`avgi 0 first contact.txt` a **406/406 (100%, 3 lotti)**, **56 directory** con `translation.json`.

## Non fatto (dichiarato)

- **Nessuna approvazione nel database**: le 135 unità sono `PENDING` (406 con L50–L51).
- **Nessun caricamento nel gioco**: l'apertura alla Dissonanza, la fuga dal Twilight, il ritorno di Sora
  e di Darius e la scoperta del magnetar non sono mai stati visti a schermo.
- **Nessun test di gameplay** della linea Avgi.
