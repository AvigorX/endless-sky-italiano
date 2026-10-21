# STATO — L255 (`data/wanderer/wanderer jobs.txt`, riga 891) — LOTTO TERMINALE

**Stato: CHIUSO — LOTTO TERMINALE.** Quarto e ultimo lotto del file, **1 unità**. Con questo lotto
**`data/wanderer/wanderer jobs.txt` è COMPLETO a 92/92 (100%)**: **tredicesimo file chiuso** della campagna.

| voce | valore |
|---|---|
| directory | `staging/editorial/L255_20261020_153136/` |
| file | `data/wanderer/wanderer jobs.txt` (92 unità · 1.303 parole · righe 15–891) — **CHIUSO 92/92** |
| righe | 891–891 |
| unità | **1** |
| parole | **20 EN → 19 IT** |
| rapporto | **0,98** |
| contesti | **1** — `Wanderers to Kor Efreti` (lo stesso di L254) |
| tab / virgolette / apici | **0 / 0 / 0** in entrambe le lingue |
| segnaposto | **1** (`<payment>`) |
| tipi | **1 `DIALOG`** |
| `check.py` | **19 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **19 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di FILE**: 91 prima · 1 qui · **0 dopo** la 891 · 92 righe distinte su 92 |
| copertura del file | **92/92 (100%)** |
| `sha256[:16]` | **`efc5d0fa26a5605d`** |

## Comandi

```bash
python staging/editorial/L255_20261020_153136/check.py     # FAIL totale: 0 (19 controlli)
python staging/editorial/L255_20261020_153136/verify.py    # FAIL: 0 (19 controlli, FILE 92/92)
```

## Il testo

> `When you return, the Wanderers thank you for taking them to the Kor Efreti and hand you <payment> before disembarking.`
> «Al ritorno, i Wanderer ti ringraziano per averli portati dai Kor Efreti e ti consegnano `<payment>` prima di scendere.»

Chiude la missione `Wanderers to Kor Efreti` iniziata in L254: `Wanderer` e `Kor Efreti` invariati, `<payment>` al suo posto,
nessun articolo davanti al segnaposto.

## Il conto del file

```
L252   26 unità   righe  15 - 261
L253   24 unità   righe 264 - 442
L254   41 unità   righe 458 - 888
L255    1 unità   riga  891
----------------------------------
92 unità = 92 righe distinte · completo
```

## Limiti dichiarati

Nessuna approvazione (1 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Il file è **completo in
staging**, non nel gioco. **Un lotto di una sola unità ha comunque 19 + 19 controlli**: tipo, segnaposto, tab/virgolette/
apici a zero, lessico, rapporto e invariante di file.
