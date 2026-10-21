# STATO — L236 (`data/avgi/avgi news.txt`, righe 301–344) · **CHIUSO**

**Quarto lotto del file**: 23 notizie di studenti Avgi in due contesti. Il file **non** è chiuso: restano 35 unità dopo
la riga 344, e l'invariante è di **segmento**.

| voce | valore misurato |
|---|---|
| file | `data/avgi/avgi news.txt` (115 unità · 2.164 parole, tutte `NEWS`) |
| righe | 301–344 |
| unità | **23** |
| parole | **348 EN → 320 IT** |
| rapporto | 0,88 – 1,58 (media 1,04) |
| tipi | **23 `NEWS`**, zero `VALUE`, zero `UI_LABEL` |
| contesti | **2** — `student happy` 13, `student frustrated` 10 |
| tab | **0** |
| virgolette | **46**, esattamente **2 per unità** |
| apici | **18 EN** su 15 unità / **14 IT** su 10 unità |
| segnaposto | **0** |
| identiche | **0** (23 tradotte) |
| etichette | **19 in testa** + **4 unità senza** (10, 11, 20, 21) + **2 etichette in coda** (11, 21) |
| `check.py` | **36 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **21 controlli, `FAIL: 0`**, exit 0 |
| `sha256[:16]` di `translation.json` | **`df51440678f593e2`** |
| stato | **CHIUSO** (file aperto a 80/115) |

## Copertura del file

| lotto | righe | unità | EN → IT | check / verify | sha256[:16] |
|---|---|---|---|---|---|
| L233 | 32–91 | 22 | 447 → 441 | 32 / 20 | `14b34f5d9e29558c` |
| L234 | 115–180 | 20 | 439 → 433 | 32 / 21 | `a1598c95777cbd57` |
| L235 | 197–280 | 15 | 72 → 68 | 31 / 21 | `d6825410bf2929d6` |
| **L236** | **301–344** | **23** | **348 → 320** | **36 / 21** | **`df51440678f593e2`** |
| residuo | 369–507 | 35 | — | — | — |
| **totale file** | **32–507** | **115** | **958 → 942** | | |

`22 + 20 + 15 + 23 + 35 = 115`: copertura **80/115 (69,6%)**. Confine misurato: **riga 369**, `news:avgi physicist`.

## Cosa cambia rispetto a L235

1. **Si torna alla citazione intera**: 2 virgolette per unità, 46 in tutto.
2. **Tre coppie di inglese identico** dentro la finestra (10/20, 12/22, 13/23): resa **identica** dentro la coppia,
   verificata confrontando le stringhe.
3. **Una coppia quasi identica** (11/21) con l'**etichetta in coda**, minuscola: `…, divertimento.` / `…, scoramento.`
   È l'unico punto del file in cui la modalità non apre la frase.
4. **Quattro unità senza etichetta** (10, 11, 20, 21): due domande e due battute.

## Comandi di verifica

```bash
python staging/editorial/L236_20261020_130628/check.py     # FAIL totale: 0 (36 controlli)
python staging/editorial/L236_20261020_130628/verify.py    # FAIL: 0 (21 controlli), segmento 80/115
```
