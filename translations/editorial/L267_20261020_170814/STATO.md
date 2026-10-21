# STATO — L267 (`data/human/engines.txt`, righe 27–194)

**Stato: CHIUSO.** Primo lotto del file dei motori umani: **12 unità** (11 `DESCRIPTION` + 1 `VALUE`) su **8
equipaggiamenti**. Il file è aperto a **12/61 (19,7%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L267_20261020_170814/` |
| file | `data/human/engines.txt` (61 unità · 1.882 parole · righe 27–717) |
| righe | 27–194 |
| unità | **12** — 11 `DESCRIPTION` + 1 `VALUE` |
| parole | **438 EN → 440 IT** |
| rapporto | **0,96 – 1,25** |
| contesti | **8** — Volcano, Caldera, Ionic Afterburner; X1050, X1700, X2700, X3700, X4700 |
| tab | **3** (righe 141, 159, 177), primo carattere |
| virgolette | **2** (riga 121, `"adeguato"`), dritte |
| apici | **1 EN** / **6 IT** su 5 unità |
| segnaposto | **0** (asserzione negativa) |
| `check.py` | **23 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **22 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 0 prima (il lotto **apre** il file) · 12 qui · **49 dopo** la 194 |
| `sha256[:16]` | **`8705fb2d52c02da2`** |

## Comandi

```bash
python staging/editorial/L267_20261020_170814/check.py     # FAIL totale: 0 (23 controlli)
python staging/editorial/L267_20261020_170814/verify.py    # FAIL: 0 (22 controlli, 12/61)
```

## La terminologia viene dal corpus, non dalla memoria

| inglese | resa | fonte |
|---|---|---|
| `afterburner` | **postbruciatore** | `tooltips.txt`, 21 unità |
| `thruster` / `thrust` | **propulsore** / **spinta** | 31 / 55 unità |
| `hyperspace fuel` | **carburante per l'iperspazio** | 17 unità |
| `ion engines` | **motori ionici** | |
| `plasma engines` | **motori al plasma** | |
| `capital ship` | **nave capitale** | 6 unità |
| `freighter` | **mercantile** | 68 unità |
| `batteries` | **batterie** | 34 unità |

## Le tre copie della scheda ionica

Le righe **141, 159, 177** hanno lo **stesso** testo (con tab iniziale): una sola resa, verificata come insieme con un solo
elemento. Se le tre copie divergessero, i conteggi di parole resterebbero identici.

## Limiti dichiarati

Nessuna approvazione (12 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Restano **49 unità**.
