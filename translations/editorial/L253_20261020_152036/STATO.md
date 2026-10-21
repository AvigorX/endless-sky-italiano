# STATO — L253 (`data/wanderer/wanderer jobs.txt`, righe 264–442)

**Stato: CHIUSO.** Secondo lotto del file, **24 unità** (8 `VALUE` + 8 `DESCRIPTION` + 8 `DIALOG`). Il file sale a
**50/92 (54,3%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L253_20261020_152036/` |
| file | `data/wanderer/wanderer jobs.txt` (92 unità · 1.303 parole · righe 15–891) |
| righe | 264–442 |
| unità | **24** |
| parole | **427 EN → 406 IT** |
| rapporto | **0,84 – 1,12** (media 1,03), gate 0,55–1,90 |
| contesti | **8** — quattro missioni × due contatori |
| tab / virgolette | **0** / **0** (asserzioni negative scritte) |
| apici | **0 EN** / **1 IT** (unità 21, `un'ora`) |
| segnaposto | **56** in **8** famiglie, multiset **e ordine per unità**; `<stopovers>` (2), **nessun** `<planet stopovers>` |
| copiati | **8** `VALUE` (4 distinti) |
| tradotti | **16** — **14 stringhe distinte**, **10 gruppi** da due copie + **4 singolari** |
| `check.py` | **34 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **29 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 26 prima · 24 qui · 42 dopo · confine riga **458** |
| copertura del file | **50/92 (54,3%)** |
| `sha256[:16]` | **`be58cd9fe1075809`** |

## Comandi

```bash
python staging/editorial/L253_20261020_152036/check.py     # FAIL totale: 0 (34 controlli)
python staging/editorial/L253_20261020_152036/verify.py    # FAIL: 0 (29 controlli, 50/92)
```

## Cosa contiene

Quattro missioni dei **Wanderer**, ognuna con `VALUE` + scheda + battuta in due contesti: **biologi** a studiare una specie
animale appena scoperta, **botanici** a studiare una specie vegetale, la **raccolta del cibo**, e la **quarantena di una
specie invasiva** — quest'ultima con due schede che differiscono per **una parola** (animale / pianta) e due battute
diverse, che sono i **quattro singolari** del lotto.

## Limiti dichiarati

Nessuna approvazione (24 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Il file **non** è
completo: 50/92 (54,3%); restano 42 unità.
