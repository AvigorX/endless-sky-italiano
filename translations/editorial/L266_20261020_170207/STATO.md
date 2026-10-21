# STATO — L266 (`data/kahet/aberrant ships.txt`, righe 686–1007) — LOTTO TERMINALE

**Stato: CHIUSO — LOTTO TERMINALE.** Secondo e ultimo lotto del file, **22 unità**. Con questo lotto
**`data/kahet/aberrant ships.txt` è COMPLETO a 65/65 (100%)**: **sedicesimo file chiuso** della campagna.

| voce | valore |
|---|---|
| directory | `staging/editorial/L266_20261020_170207/` |
| file | `data/kahet/aberrant ships.txt` (65 unità · 646 parole · righe 16–1007) — **CHIUSO 65/65** |
| righe | 686–1007 |
| unità | **22** — 13 `VALUE` + 9 `DESCRIPTION` |
| parole | **217 EN → 210 IT** |
| rapporto | **0,97 – 1,33** |
| contesti | **5** — Aberrant Pike (coda), Mole, Whiskers, Trip, Triplet |
| tab / virgolette | **0** / **18** |
| apici | **0 EN** / **6 IT** |
| segnaposto | **0** (asserzione negativa) |
| `check.py` | **26 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **21 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di FILE**: 43 prima · 22 qui · **0 dopo** la 1007 · **65 righe distinte su 65** |
| `sha256[:16]` | **`4c56d5f85bae96b5`** |

## Comandi

```bash
python staging/editorial/L266_20261020_170207/check.py     # FAIL totale: 0 (26 controlli)
python staging/editorial/L266_20261020_170207/verify.py    # FAIL: 0 (21 controlli, FILE 65/65)
```

## Il conto del file

```
L265  43 · L266  22  =  65 unità = 65 righe distinte · completo
```

## Due cose che il lotto doveva fare bene

1. **La formula organo-metallica ricorre 4 volte** (Mole, Whiskers, Trip, Triplet) ed è **ripresa alla lettera da L265**:
   il `check.py` rilegge `L265/translation.json` e confronta l'insieme delle rese. Due varianti della stessa stringa
   sarebbero passate un controllo locale sui conteggi.
2. **La scheda di Trip è un difetto, non una variante**: «Qualcosa sembra essere andato terribilmente storto nella
   germinazione di questa variante. È una massa sbilenca e deforme…». Il test verifica le parole che portano il senso
   («terribilmente storto», «germinazione», «deforme», «sopravvive»).

## Limiti dichiarati

Nessuna approvazione (22 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. **«Completo» significa
completo in staging.**
