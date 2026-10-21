# L54 — stato di avanzamento (CHIUSO 2026-10-18)

Lotto `L54_20261018_173515` · `data/gegno/gegno intro missions.txt` · righe 280–676 ·
**159/159 unità**. Con L53 (**89**) il file è a **248/276 (89,9%)**: **non completo**, restano 28 unità
dopo la riga 676 (previste in L55).

## Fatto

- `source.json`: 159 unità, **6 contesti** (`Discover Hostile Quarg` 1–9, `Giaru Gegno: Quarg Contact`
  10–49, `Gegno Quarg Direction to Ringworld` 50–54, `Giaru Gegno: Revisit` 55–62, `Suspicious Scin`
  63–66, `First Contact: Gegno Scin` 67–159), kind 134 `MISSION_TEXT` / **19 `UI_LABEL`** /
  **3 `LOGBOOK`** / 2 `VALUE` / 1 `DESCRIPTION`. **Nessun `DIALOG`, nessun `TEXT`, nessuna
  `CONVERSATION`, nessun token `<...>`**.
- `check.py` derivato da L53 con `NT` a **19** (elenco completo per indice), `LOGBOOK` di nuovo
  **positivo** su 3 testi, assenza dei token **dichiarata** con una riga dedicata, e la virgoletta
  dispari dell'unità 59 riprodotta.
- 4 parti, a fine contesto: **49 · 17 · 46 · 47**.
- `translation.json`: 159 unità, 5.975 EN → 5.274 IT (0,883), rapporto per unità 0,73–1,58,
  sha256[:16] `5ac7ae01fd74ae15`.
- `verify.py`: **41 controlli**, `FAIL: 0`, exit 0. Segmento interno (89 prima / **28** dopo), copertura
  delle righe 280–676, `NT` 19, `LOGBOOK` 3 con forme 2+1, `DIALOG`/`TEXT`/`CONVERSATION` 0,
  **0 token**, **1 virgoletta dispari ({59})**, parità di tab/virgolette per unità, **20 gruppi di
  duplicati inglesi** con resa identica.
- `review.md`, `REPORT.md`, questo `STATO.md`.

## Regole applicate

- **La voce dei Quarg è il problema centrale del lotto.** Parlano con una sintassi **invertita** e un
  lessico **aulico-marziale** («This must be for you an exhilarating day», «Not significantly often it
  is that the mighty Gegno interact with daring outsiders», «the imperious Gegno»). La traduzione
  riproduce l'inversione («Questa deve essere per te una giornata esaltante», «Non è con frequenza
  significativa che i possenti Gegno interagiscono con audaci estranei») e tiene gli aggettivi
  celebrativi: è il tratto che distingue **questo** Quarg dagli altri, che parlano piatto e ostile.
- **`NT` = 19** etichette di salto, elencate una per una; nessun riferimento di dato.
- **`LOGBOOK` 3**: due a tre argomenti (`Factions`/`Gegno`, unità 1 e 10) e una fra backtick (11).
- **`token 0`**: assenza dichiarata con una riga apposita
  (`token nel sorgente (0 attesi: assenza dichiarata)`). Senza di essa, un token perso non sarebbe
  visibile a nessuno.
- **1 virgoletta dispari** (unità 59): il Quarg apre un discorso e non lo chiude. La virgoletta è
  **riprodotta**, e `verify.py` confronta l'**insieme degli idx**, non un conteggio.
- **20 gruppi di duplicati inglesi** (43 unità): il gioco ripete le stesse scene fra il primo incontro e
  il secondo con gli Scin (opzioni, misurazioni, minaccia della lama, ritratti). La resa italiana è
  identica dove l'inglese è identico.
- **Lessico nuovo**: `Gegno Vi` / `Gegno Scin` / `Vi` / `Scin` **invariati** · `Quarg Ringworld` →
  **anello dei Quarg** · `Giaru Gegno`, `Var Oti` **invariati** (luoghi) · `Hauler`, `Behemoth`
  **invariati** (classi di nave) · `Huema` **invariato** (il tentativo Quarg di dire «umano») ·
  `Dueyu Scin` / `Dueyu human` / `Dueyu Vi` / `Vie` / `Sinn` **invariati** (parlato Scin, con la
  differenza voluta fra grafia e pronuncia) · `young traverser` → **giovane viaggiatore** ·
  `sickle-like blade` → **lama a forma di falce**.

## Verifica

```
python staging/editorial/L54_20261018_173515/check.py    → FAIL totale: 0 (33 controlli)
python staging/editorial/L54_20261018_173515/verify.py   → exit 0, 41 controlli, FAIL: 0
```

`state.py` dopo L54: **23.503 unità · 750.437 EN · 711.402 IT**, `ESITO: OK`,
`gegno intro missions.txt` a **248/276 (89,9%)**, **58 directory** con `translation.json`.

## Non fatto (dichiarato)

- **Nessuna approvazione nel database**: le 159 unità sono `PENDING`.
- **Nessun caricamento nel gioco**: l'incontro con i Quarg, la scena dell'interrogatorio e i tre rami
  dell'incontro con gli Scin (disegni, capo inclinato, lama alla gola) non sono mai stati visti a schermo.
- **Il file non è completo**: restano 28 unità dopo la riga 676, previste in L55.
