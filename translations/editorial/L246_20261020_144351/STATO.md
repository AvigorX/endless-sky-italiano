# STATO — L246 (`data/hai/hai ships.txt`, righe 1517–1860)

**Stato: CHIUSO — LOTTO TERMINALE.** Quarto e ultimo lotto del file, **37 unità** (32 `TEXT` + 5 `DESCRIPTION`). Con
questo lotto **`data/hai/hai ships.txt` è COMPLETO a 157/157 (100%)**: **undicesimo file chiuso** della campagna.

| voce | valore |
|---|---|
| directory | `staging/editorial/L246_20261020_144351/` |
| file | `data/hai/hai ships.txt` (157 unità · 1.686 parole) — **CHIUSO 157/157** |
| righe | 1517–1860 |
| unità | **37** |
| parole | **327 EN → 324 IT** |
| rapporto | **0,99 – 1,23** (media 1,02), gate 0,55–1,90 |
| contesti | **4** — `Emperor Beetle` 1, `Solifuge` 19, `Violin Spider` 6, `Water Bug` 11 |
| tab | **2**, all'inizio delle unità 1 e 24 |
| virgolette | **66** (2 per i 32 nomi + 2 intorno a `"Giftbringer"`) |
| apici | **2 EN** (unità 1, 5) / **5 IT** (unità 1, 30) |
| segnaposto | **0** (asserzione negativa scritta) |
| copiati | **32** `TEXT` |
| tradotti | **5** `DESCRIPTION` |
| `check.py` | **33 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **27 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di FILE**: 120 prima · 37 qui · **0 dopo** la 1860 · 157 righe distinte su 157 |
| copertura del file | **157/157 (100%)** |
| `sha256[:16]` | **`2b2115dc3e8187c7`** |

## Comandi

```bash
python staging/editorial/L246_20261020_144351/check.py     # FAIL totale: 0 (33 controlli)
python staging/editorial/L246_20261020_144351/verify.py    # FAIL: 0 (27 controlli, FILE 157/157)
```

## Cosa contiene

La chiusura del file: il **secondo paragrafo del relitto/scheda dell'Emperor Beetle** (col tab), la **Solifuge** (il
porta-caccia degli Slegati costruito dopo aver visto il `"Giftbringer"` degli Alphas), la **Violin Spider** (caccia Hai con
la nota sui caccia col tab) e il **Water Bug** (il mercantile Hai più diffuso, cresciuto sulle aggressioni degli Slegati).
Le altre 32 unità sono nomi di equipaggiamento.

## Il conto del file

```
L243   29 unità   righe   15 -  332
L244   45 unità   righe  362 -  885
L245   46 unità   righe  901 - 1516
L246   37 unità   righe 1517 - 1860
----------------------------------
157 unità = 157 righe distinte · completo
```

## Limiti dichiarati

Nessuna approvazione (37 unità `PENDING`), nessuna scheda vista nel gioco, nessuna revisione umana. Il file è **completo in
staging**, non nel gioco: 157 unità `PENDING` come tutte le altre.
