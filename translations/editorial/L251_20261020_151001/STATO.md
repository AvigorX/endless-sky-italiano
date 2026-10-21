# STATO — L251 (`data/human/syndicate jobs.txt`, righe 701–814) — LOTTO TERMINALE

**Stato: CHIUSO — LOTTO TERMINALE.** Quinto e ultimo lotto del file, **12 unità** (5 `VALUE` + 5 `DESCRIPTION` + 2 `DIALOG`).
Con questo lotto **`data/human/syndicate jobs.txt` è COMPLETO a 94/94 (100%)**: **dodicesimo file chiuso** della campagna.

| voce | valore |
|---|---|
| directory | `staging/editorial/L251_20261020_151001/` |
| file | `data/human/syndicate jobs.txt` (94 unità · 1.927 parole · righe 19–814) — **CHIUSO 94/94** |
| righe | 701–814 |
| unità | **12** |
| parole | **139 EN → 150 IT** |
| rapporto | **0,88 – 1,28** (media 1,08), gate 0,55–1,90 |
| contesti | **5** — `Megaparsec Shipment [0]/[1]/[2]`, i due trasporti di hovercraft |
| tab / virgolette / apici | **0 / 0 / 0** in entrambe le lingue (tre asserzioni negative scritte) |
| segnaposto | **24** in **6** famiglie, multiset **e ordine per unità** identici |
| copiati | **5** `VALUE` (3 distinti) |
| tradotti | **7** (5 `DESCRIPTION` + 2 `DIALOG`) |
| `check.py` | **30 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **25 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di FILE**: 82 prima · 12 qui · **0 dopo** la 814 · 94 righe distinte su 94 |
| copertura del file | **94/94 (100%)** |
| `sha256[:16]` | **`2462a6148f0bcfcd`** |

## Comandi

```bash
python staging/editorial/L251_20261020_151001/check.py     # FAIL totale: 0 (30 controlli)
python staging/editorial/L251_20261020_151001/verify.py    # FAIL: 0 (25 controlli, FILE 94/94)
```

## Cosa contiene

Le **tre spedizioni Megaparsec** (schede identiche, un solo `VALUE`: `Shipment to <planet>`) e i **due trasporti di
hovercraft** per la gara: un pilota solo, e una squadra di `<passengers>` membri con il loro carico di `<cargo>`.

## Il conto del file

```
L247   16 unità   righe  19 - 153
L248   20 unità   righe 157 - 275
L249   19 unità   righe 291 - 431
L250   27 unità   righe 435 - 678
L251   12 unità   righe 701 - 814
----------------------------------
94 unità = 94 righe distinte · completo
```

## Limiti dichiarati

Nessuna approvazione (12 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Il file è **completo in
staging**, non nel gioco.
