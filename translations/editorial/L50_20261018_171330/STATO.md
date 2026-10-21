# L50 — stato di avanzamento (CHIUSO 2026-10-18)

Lotto `L50_20261018_171330` · `data/avgi/avgi 0 first contact.txt` · righe 22–402 · **119/119 unità**.
Il lotto **apre il file**: 0 unità prima della riga 22, **287 dopo** la 402 (il file ne ha 406). Il file
**non è completo**: 119/406 (29,3%). Tutti i numeri sono misurati, non stimati.

## Fatto

- `source.json`: 119 unità, **4 contesti** (`Avgi: Lost in Twilight` 1–2, **`phrase:lost in twilight`** 3,
  `Avgi: First Contact` 4–44, `Avgi: Humans From the Deep` 45–119), kind 102 `MISSION_TEXT` /
  7 `LOGBOOK` / 3 `UI_LABEL` / 2 `VALUE` / 2 `DESCRIPTION` / **2 `DIALOG`** / **1 `TEXT`**.
- `check.py` derivato da L49 con **`NT` = 3** (solo `UI_LABEL`), **`LOGBOOK` positivo su 7 testi**,
  **`DIALOG` e `TEXT` trattati come tipi presenti** (controllo positivo, non assenza), assenze dichiarate
  per `CONVERSATION`, quadre, backtick e virgolette dispari, costruttore dei tab.
- 3 parti, a fine contesto: **44 · 41 · 34**.
- `translation.json`: 119 unità, 4.399 EN → 4.139 IT (0,941), rapporto per unità 0,81–1,53,
  sha256[:16] `50c003eec1b5e9a3`.
- `verify.py`: **47 controlli**, `FAIL: 0`, exit 0. Apre il file (0 prima / 287 dopo), copertura del
  segmento per righe, `NT` 3, `LOGBOOK` 7 con forme 5+1+1, `DIALOG` 2, `TEXT` 1 identico all'unità 2,
  parità di tab/virgolette/token per unità, duplicati inglesi con resa italiana identica.
- `review.md`, `REPORT.md`, questo `STATO.md`.

## Regole applicate

- **`DIALOG` e `TEXT` per la prima volta nella linea Avgi** (in L48/L49 erano 0). Le asserzioni sono
  **positive**: `DIALOG` = (43, 44), `TEXT` = (3). Un `check.py` ereditato da L49 con «`DIALOG` 0» sarebbe
  passato senza controllare nulla.
- **Il `TEXT` è la copia esatta della missione**: l'unità 3 (contesto `phrase:lost in twilight`) ripete
  parola per parola l'unità 2. Il duplicato è **nel sorgente** e la traduzione lo riproduce identico;
  `verify.py` lo asserisce in inglese **e** in italiano.
- **`LOGBOOK` 7, tutte di testo, in tre forme**: 1 diretta fra virgolette (unità 1), 1 fra backtick
  (unità 47), 5 a tre argomenti con testo fra backtick (48–52, `Factions`/`People`). Nessuna categoria
  estratta: ancora una volta la lacuna dell'estrattore **non si presenta**.
- **96 tab su 119 unità**, 118 virgolette, **0 dispari**, 14 token in 5 famiglie: parità per unità.
- **La voce Avgi** mantiene la convenzione di L48–L49 (etichetta di modalità + «, domanda?»), qui al
  **primo contatto**: «Saluti. Io essere degli Avgi. Tu umano, domanda? Importante.» — sintassi
  telegrafica, articoli e coniugazioni ridotti, come il sorgente.
- **Lessico nuovo**: `Lait`, `Asime`, `Galano`, `Prasinos`, `Aviskir`, `Monti Fel`, `Darius Calwell`,
  `Aktina Cylinder` → **Cilindro Aktina** invariati o già fissati; `ideolopoli` invariato (parola coniata
  nel testo, con la stessa radice di «entità politiche»); `Primi Portavoce`, `Assemblea della Consonanza`
  (per *Consonance Assembly*), **`Assemblea delle Entità`** (per *Assembly of Polities*, come in L48);
  `hyperdrive`, `Twilight`, `Tangled Shroud`, `Twilight Guard` invariati (decisione 168).

## Verifica

```
python staging/editorial/L50_20261018_171330/check.py    → FAIL totale: 0 (29 controlli)
python staging/editorial/L50_20261018_171330/verify.py   → exit 0, 47 controlli, FAIL: 0
```

`state.py` dopo L50: **22.968 unità · 732.323 EN · 694.888 IT**, `ESITO: OK`,
`avgi 0 first contact.txt` a **119/406 (29,3%)**, **54 directory** con `translation.json`.

## Non fatto (dichiarato)

- **Nessuna approvazione nel database**: le 119 unità sono `PENDING`.
- **Nessun caricamento nel gioco**: il primo contatto con Lait, la scena della sala conferenze e il dono
  del traduttore non sono mai stati visti a schermo.
- **Il file non è completo**: restano 287 unità dopo la riga 402, previste in L51 e oltre.
