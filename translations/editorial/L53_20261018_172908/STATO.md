# L53 — stato di avanzamento (CHIUSO 2026-10-18)

Lotto `L53_20261018_172908` · `data/gegno/gegno intro missions.txt` · righe 17–230 · **89/89 unità**.
**Apre il file** e lo lascia aperto: **187 unità** dopo la riga 230 (il file ne ha 276, `max(line) = 954`).
File a **89/276 (32,2%)**.

## Fatto

- `source.json`: 89 unità, **2 contesti** (`First Contact: Gegno Vi` 1–77, `Visit Quarg in Gegno Space`
  78–89), kind 80 `MISSION_TEXT` / **5 `UI_LABEL`** / 2 `VALUE` / 2 `DESCRIPTION`. **Nessun `LOGBOOK`,
  nessun `DIALOG`, nessun `TEXT`, nessuna `CONVERSATION`**.
- `check.py` derivato da L52 con una differenza strutturale: poiché `LOGBOOK` e `DIALOG` sono **zero**,
  il lotto non ha controlli positivi sui diari ma **due asserzioni di assenza** aggiunte apposta
  (`righe LOGBOOK nel segmento (0 attese: assenza dichiarata)`, `nodi dialog nel segmento (0 attesi)`).
  Un `check.py` ereditato da L52 con 17 indici `LOGBOOK` avrebbe controllato unità inesistenti passando
  in silenzio.
- 3 parti: **30 · 30 · 29**.
- `translation.json`: 89 unità, 4.287 EN → 3.896 IT (0,909), rapporto per unità 0,81–1,63,
  sha256[:16] `7e2899a23c7c3c8e`.
- `verify.py`: **41 controlli**, `FAIL: 0`, exit 0. Apre il file (0 prima / **187 dopo**), copertura delle
  righe 17–230, `NT` 5, `LOGBOOK`/`DIALOG`/`TEXT`/`CONVERSATION` **0** come assenze dichiarate,
  parità di tab/virgolette/token per unità, **8 gruppi di duplicati inglesi** con resa identica.
- `review.md`, `REPORT.md`, questo `STATO.md`.

## Regole applicate

- **Primo lotto della linea Gegno**: la voce è costruita qui e registrata in `review.md`. I Gegno non
  parlano (comunicano con grugniti, gesti e un solo vocabolo, «Oukeug»): il testo è quasi tutto
  **narrazione al presente**, e la traduzione tiene il registro descrittivo senza spezzarlo.
- **Le famiglie di token sono tre, non una**: `<alien>` (17), `<aliens>` (6) e `<Alien>` (1) sono
  **famiglie distinte**, e il controllo confronta i multiset senza normalizzare le maiuscole. `<alien>`
  e `<aliens>` sono singolare e plurale; `<Alien>` con la maiuscola compare solo nel nome della missione
  (unità 1) e indica la specie come titolo.
- **`NT` = 5**: cinque `label` di salto (`second encounter`, `return encounter`, `search again`,
  `has met quarg`, `hostile quarg`), tutte identiche al sorgente. Nessun riferimento di dato.
- **Solo 6 virgolette** in 89 unità (3 coppie, tutte nel finale dell'unità 84–88 attorno a «Oukeug»):
  il minimo della serie.
- **8 gruppi di duplicati inglesi** (16 unità): le opzioni ripetute fra il primo e il secondo incontro
  (`(Approach the alien.)` ×2, `(Accept their request.)` ×2, ecc.) e le due descrizioni identiche del
  pianeta (unità 3 e 35). La resa italiana è identica dove l'inglese è identico, e `verify.py` lo
  asserisce.
- **Lessico nuovo**: `Gegno`, `Gegno Vi`, `Vi` **invariati** (nome di specie e di sotto-fazione) ·
  `Quarg ringworld` → **mondo ad anello dei Quarg** · `Firebird` **invariato** (classe di nave) ·
  `environment suit` → **tuta ambientale** · `sidearm` → **arma da fianco** · `star map` → **carta
  stellare** · `Oukeug` **invariato** (unico vocabolo Gegno) · `compass device` → **dispositivo a
  bussola**.

## Verifica

```
python staging/editorial/L53_20261018_172908/check.py    → FAIL totale: 0 (33 controlli)
python staging/editorial/L53_20261018_172908/verify.py   → exit 0, 41 controlli, FAIL: 0
```

`state.py` dopo L53: **23.344 unità · 744.462 EN · 706.128 IT**, `ESITO: OK`,
`gegno intro missions.txt` a **89/276 (32,2%)**, **57 directory** con `translation.json`.

## Non fatto (dichiarato)

- **Nessuna approvazione nel database**: le 89 unità sono `PENDING`.
- **Nessun caricamento nel gioco**: il primo contatto con il Gegno Vi, la bestia del deserto e la scena
  dell'uccisione con la lancia non sono mai stati visti a schermo.
- **Il file non è completo**: restano 187 unità oltre la riga 230, previste in L54 e oltre.
