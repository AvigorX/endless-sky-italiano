# STATO — L242 (`data/successors/successor jobs.txt`, righe 306–802)

**Stato: CHIUSO.** Secondo e **ultimo** lotto del file, **38 unità** (19 `VALUE` + 19 `DESCRIPTION`).
**`data/successors/successor jobs.txt` è COMPLETO: 124/124 (100%)**, 908 EN → 880 IT in due lotti — **decimo file chiuso**
della campagna.

| voce | valore |
|---|---|
| directory | `staging/editorial/L242_20261020_141643/` |
| file | `data/successors/successor jobs.txt` (124 unità · 908 parole) |
| righe | 306–802 (**802 = ultima del file**) |
| unità | **38** — **19 `VALUE`** (invariati) + **19 `DESCRIPTION`** (tradotte) |
| parole | **480 EN → 435 IT** |
| rapporto | **0,92 – 1,09** (media 1,00), gate 0,55–1,90 |
| contesti | **19**, due unità ciascuno — da `Successors: Students In` a `Successors: New Houses Rush Delivery` |
| tab / virgolette / apici | **0 / 0 / 0** (tre asserzioni negative scritte) |
| segnaposto | **98** in 10 famiglie: `<planet>` 28, `<payment>` 19, `<date>` 11, **`<tons>` 11**, `<origin>` 11, `<bunks>` 7, `<destination>` 4, `<planet stopovers>` 3, `<stopovers>` 3, `<cargo>` 1 |
| famiglie `DESCRIPTION` | **14** (una da 4 copie, due da 2, undici da 1) |
| `check.py` | **30 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **24 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di FILE**: 86 + 38 = **124/124**, riga 802 ultima, 0 dopo, 0 sovrapposizioni |
| `sha256[:16]` | **`c24851e11b618bfb`** |

## Comandi

```bash
python staging/editorial/L242_20261020_141643/check.py     # FAIL totale: 0 (30 controlli)
python staging/editorial/L242_20261020_141643/verify.py    # FAIL: 0 (24 controlli, FILE 124/124)
```

## Cosa contiene

Diciannove lavori Successors: studenti che tornano all'università, operai in cerca di lavoro, consegne di provviste (quattro
copie della stessa formula), carichi preziosi, aiuti, materiali sfusi, spedizioni urgenti, **stabilizzatori sismici** dopo
un terremoto, **corriere di dati riservati**, tre lavori di **ricercatori** (Predecessori, squadra grande, ricerche sul
posto), il **simposio**, e le consegne urgenti delle **Vecchie** e **Nuove Casate**.

## Limiti dichiarati

Nessuna approvazione (38 unità `PENDING`), nessun lavoro visto nel gioco, nessuna revisione umana. Il file è completo **in
staging**, non nel database.
