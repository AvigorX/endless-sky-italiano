# L54 — rapporto del lotto

`data/gegno/gegno intro missions.txt` · righe **280–676** · lotto `L54_20261018_173515` ·
**159/159 unità** · segmento interno (89 prima / 28 dopo; file di 276) · chiuso il 2026-10-18.

## Numeri

| voce | valore |
|---|---|
| unità | **159 / 159** del segmento; file a **248 / 276** (89,9%) |
| parole | 5.975 EN → **5.274 IT** (0,883) |
| contesti | 6 — `Discover Hostile Quarg` (9) · `Giaru Gegno: Quarg Contact` (40) · `Gegno Quarg Direction to Ringworld` (5) · `Giaru Gegno: Revisit` (8) · `Suspicious Scin` (4) · `First Contact: Gegno Scin` (93) |
| parti | 4 — 49 · 17 · 46 · 47 |
| tab | **126 = 126** |
| virgolette | **129 = 129** |
| virgolette dispari | **1** (unità 59), stesso idx in italiano |
| token `<...>` | **0** (assenza dichiarata, prima volta nella serie) |
| quadre `[` `]` · backtick | **0 / 0** (assenze dichiarate) |
| `LOGBOOK` | **3** (2 a tre argomenti, 1 fra backtick) |
| `DIALOG` | **0** (assenza dichiarata) |
| `TEXT` / `CONVERSATION` | **0 / 0** (assenze dichiarate) |
| `UI_LABEL` | **19** → `NT` = 19 |
| duplicati inglesi | **20 gruppi** (43 unità) |
| rapporto per unità | 0,73 – 1,58 |
| `check.py` | **FAIL totale: 0** (33 controlli) |
| `verify.py` | **41 controlli**, exit 0, `FAIL: 0` |
| sha256[:16] | `translation.json` `5ac7ae01fd74ae15` · `source.json` `cf2b44aab95bb044` · `check.py` `f71bccf3ea01ca0b` · `verify.py` `f18a728b9d53d797` |

Il segmento è **interno**: `verify.py` asserisce `(first, last) == (280, 676)`, **89** unità prima
(L53), **28** dopo, `tot = 276`, `max(line) = 954`.

## Tipi

134 `MISSION_TEXT` · 19 `UI_LABEL` · 3 `LOGBOOK` · 2 `VALUE` · 1 `DESCRIPTION` · 0 `DIALOG` ·
0 `TEXT` · 0 `CONVERSATION`.

## Unità non traducibili (`NT`) — 19

| idx | riga | label | idx | riga | label |
|---:|---:|---|---:|---:|---|
| 7 | 291 | `sent` | 97 | 567 | `imagery` |
| 13 | 312 | `has met gegno` | 109 | 586 | `quiet` |
| 16 | 322 | `walking` | 117 | 598 | `no thoughts` |
| 25 | 339 | `intrigued quarg` | 123 | 609 | `reach` |
| 27 | 342 | `the gegno` | 126 | 617 | `approach` |
| 42 | 379 | `wrap up` | 140 | 643 | `images` |
| 47 | 392 | `interacted with outsider` | 151 | 661 | `pistol` |
| 60 | 436 | `trouble` | 154 | 668 | `silence` |
| 75 | 526 | `leave` | | | |
| 77 | 532 | `follow` | | | |
| 87 | 549 | `sit` | | | |

Tutte sono `label "…"` di salto: **nessun riferimento di dato**.

## Le 3 righe `log`

| idx | riga | forma | contenuto |
|---:|---:|---|---|
| 1 | 280 | 3 argomenti | **Factions / Gegno**: specie umanoide a est del nucleo, divisa in Vi e Scin |
| 10 | 301 | 3 argomenti | **Factions / Gegno**: i due rami e i civili indifferenti |
| 11 | 302 | backtick | i Quarg hanno spiegato che i Gegno non vogliono contatti |

## I 20 gruppi di duplicati

Le ripetizioni non sono un difetto del testo: il gioco ripropone **le stesse scene** nel primo e nel
secondo incontro con gli Scin. I gruppi principali:

| inglese | unità | cosa si ripete |
|---|---|---|
| `(Do nothing.)` | 91, 94, 113, 134, 137 | cinque opzioni identiche in punti diversi |
| i tre ritratti e le parole `Dueyu`/`Gegno` | 98–105 e 141–148 | la sequenza dei disegni sul dispositivo |
| la minaccia della lama alla gola | 107 e 115 | identica, con `(Reach for my pistol.)` 86/130 e 119/156 |
| la misurazione della mano | 89/132, 92/135 | la stessa procedura |
| la descrizione del mercantile | 83 e 127 | la stessa nave vista da due posizioni |
| il rientro alla nave | 96/108 e 114/116 | la stessa uscita |

`verify.py` verifica che **ogni** gruppo abbia una sola resa italiana e che non ci siano rese ripetute
fra unità con inglese **diverso**.

## Verifica

```
python staging/editorial/L54_20261018_173515/check.py    → FAIL totale: 0
python staging/editorial/L54_20261018_173515/verify.py   → exit 0, FAIL: 0
```

Dopo la chiusura: **23.503 unità · 750.437 EN · 711.402 IT**, **58 directory** con `translation.json`,
integrità dei file protetti e del repository (`b4aa3bac3`, nessuna modifica).

## Non fatto (dichiarato)

- **Nessuna approvazione nel database**: 159 unità `PENDING`.
- **Nessun caricamento nel gioco**: l'interrogatorio dei Quarg e i tre rami dell'incontro con gli Scin
  non sono mai stati visti a schermo.
- **Il file resta aperto**: 28 unità (dalla riga 706 in poi) non sono state toccate.
