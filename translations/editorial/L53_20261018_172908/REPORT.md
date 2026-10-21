# L53 — rapporto del lotto

`data/gegno/gegno intro missions.txt` · righe **17–230** · lotto `L53_20261018_172908` ·
**89/89 unità** · **apre il file** (0 prima / 187 dopo; file di 276) · chiuso il 2026-10-18.

## Numeri

| voce | valore |
|---|---|
| unità | **89 / 89** del segmento; file a **89 / 276** (32,2%) |
| parole | 4.287 EN → **3.896 IT** (0,909) |
| contesti | 2 — `First Contact: Gegno Vi` (77) · `Visit Quarg in Gegno Space` (12) |
| parti | 3 — 30 · 30 · 29 |
| tab | **75 = 75** |
| virgolette | **6 = 6** (3 coppie: il minimo della serie) |
| virgolette dispari | **0** (asserzione di assenza dichiarata) |
| token `<...>` | **27 = 27** (5 famiglie: `<alien>` 17, `<aliens>` 6, `<designated system>` 2, `<Alien>` 1, `<origin>` 1) |
| quadre `[` `]` · backtick | **0 / 0** (assenze dichiarate) |
| `LOGBOOK` | **0** (assenza dichiarata, non controllo positivo) |
| `DIALOG` | **0** (assenza dichiarata) |
| `TEXT` / `CONVERSATION` | **0 / 0** (assenze dichiarate) |
| `UI_LABEL` | **5** (34, 63, 67, 85, 87) → `NT` = 5 |
| duplicati inglesi | **8 gruppi** (16 unità) |
| rapporto per unità | 0,81 – 1,63 |
| `check.py` | **FAIL totale: 0** (33 controlli) |
| `verify.py` | **41 controlli**, exit 0, `FAIL: 0` |
| sha256[:16] | `translation.json` `7e2899a23c7c3c8e` · `source.json` `39692d3758ac1300` · `check.py` `9c90dd3961751243` · `verify.py` `47b4a8914f60eb35` |

Il segmento **apre il file**: `verify.py` asserisce `(first, last) == (17, 230)`, **0** unità prima,
**187** dopo, `tot = 276`, `max(line) = 954`.

## Tipi

80 `MISSION_TEXT` · 5 `UI_LABEL` · 2 `VALUE` · 2 `DESCRIPTION` · **0 `LOGBOOK`** · **0 `DIALOG`** ·
**0 `TEXT`** · **0 `CONVERSATION`**.

## Unità non traducibili (`NT`) — 5

| idx | riga | label |
|---:|---:|---|
| 34 | 98 | `second encounter` |
| 63 | 150 | `return encounter` |
| 67 | 158 | `search again` |
| 85 | 224 | `has met quarg` |
| 87 | 228 | `hostile quarg` |

Tutte sono `label "…"` di salto: **nessun riferimento di dato**, e nessun diario da tradurre in questo
segmento.

## I 5 token distinti

| token | occorrenze | uso |
|---|---:|---|
| `<alien>` | 17 | il passeggero Gegno, singolare |
| `<aliens>` | 6 | il gruppo di Gegno, plurale |
| `<designated system>` | 2 | destinazione della missione |
| `<Alien>` | 1 | **solo** nel nome della missione (unità 1), con la maiuscola |
| `<origin>` | 1 | il pianeta dove hai incontrato l'alieno |

`<Alien>` e `<alien>` sono **due famiglie diverse**: il controllo dei token confronta i multiset esatti e
non normalizza le maiuscole.

## Le 8 coppie di duplicati inglesi

| inglese | unità | nota |
|---|---|---|
| la descrizione del pianeta | 3, 35 | la seconda visita ripete la prima scena |
| `(Approach the alien.)` | 11, 20 | due punti della stessa scena |
| `(Turn back to my ship.)` | 12, 44 | primo e secondo incontro |
| la caduta dopo il colpo rimbalzato | 18, 49 | stessa scena, due rami |
| `(Get up and run to my ship.)` | 21, 52 | primo e secondo incontro |
| `(Accept their request.)` | 24, 55 | primo e secondo incontro |
| `(Ask about their request.)` | 25, 56 | primo e secondo incontro |
| `(Reject their request.)` | 26, 57 | primo e secondo incontro |

La resa italiana è identica dove l'inglese è identico; `verify.py` lo asserisce gruppo per gruppo
(`duplicati inglesi (8 gruppi): resa italiana identica`) e controlla che **non** ci siano rese ripetute
fra unità con inglese diverso.

## Verifica

```
python staging/editorial/L53_20261018_172908/check.py    → FAIL totale: 0
python staging/editorial/L53_20261018_172908/verify.py   → exit 0, FAIL: 0
```

Dopo la chiusura: **23.344 unità · 744.462 EN · 706.128 IT**, **57 directory** con `translation.json`,
integrità dei file protetti e del repository (`b4aa3bac3`, nessuna modifica).

## Non fatto (dichiarato)

- **Nessuna approvazione nel database**: 89 unità `PENDING`.
- **Nessun caricamento nel gioco**: la tempesta di sabbia, la bestia del deserto, il combattimento al
  fianco del Vi e l'uccisione con la lancia (unità 77) non sono mai stati visti a schermo.
- **Il file resta aperto**: 187 unità (dalla riga 280 in poi) non sono state toccate.
