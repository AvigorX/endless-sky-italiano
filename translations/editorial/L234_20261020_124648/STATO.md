# STATO — L234 (`data/avgi/avgi news.txt`, righe 115–180) · **CHIUSO**

**Secondo lotto del file**: 20 notizie Avgi in tre contesti nuovi. Il file **non** è chiuso: restano 73 unità dopo la
riga 180, e l'invariante è di **segmento**.

| voce | valore misurato |
|---|---|
| file | `data/avgi/avgi news.txt` (115 unità · 2.164 parole, tutte `NEWS`) |
| righe | 115–180 |
| unità | **20** |
| parole | **439 EN → 433 IT** |
| rapporto | 0,90 – 1,28 (media 1,11) |
| tipi | **20 `NEWS`**, zero `VALUE`, zero `UI_LABEL` |
| contesti | **3** — `merchant` 10, `politician` 6, `military` 4 |
| tab | **0** |
| virgolette | **40**, esattamente **2 per unità** (citazione intera) |
| apici | **6 EN** (5, 6, 9, 10, 11, 16) / **12 IT** (5, 6, 9, 11×2, 12×2, 13, 15, 18, 19, 20) |
| segnaposto | **0** |
| identiche | **0** (20 tradotte) |
| etichette | **19 su 20**: la **177** è una domanda Avgi (`…, question?` → «…, domanda?») |
| `check.py` | **33 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **21 controlli, `FAIL: 0`**, exit 0 |
| `sha256[:16]` di `translation.json` | **`a1598c95777cbd57`** |
| stato | **CHIUSO** (file aperto) |

## Copertura del file

| lotto | righe | unità | EN → IT | check / verify | sha256[:16] |
|---|---|---|---|---|---|
| L233 | 32–91 | 22 | 447 → 441 | 32 / 20 | `14b34f5d9e29558c` |
| **L234** | **115–180** | **20** | **439 → 433** | **32 / 21** | **`a1598c95777cbd57`** |
| residuo | 197–507 | 73 | — | — | — |
| **totale file** | **32–507** | **115** | **2.164** | | |

`22 + 20 = 42` prima della 197; `42 + 20 + 73 = 115`. Confine misurato: **riga 197**, `news:avgi safety advisory`.

## Cosa cambia rispetto a L233

1. **Il registro resta l'etichetta**, ma per la prima volta **un'unità non ne ha** (la 177): è una domanda Avgi nella
   forma esplicita `…, question?`, e il `check.py` confronta la lista delle etichette **con quel `None`**.
2. **Gli apici si invertono**: 6 inglesi contro 12 italiani (in L233 erano 12 contro 5). Qui l'italiano elide più di
   quanto l'inglese contragga.
3. **Chiusa la questione aperta in L233**: `the Guard` → «la Guardia» (28 occorrenze nel corpus), e `polities` →
   «entità politiche» (10 occorrenze), non «politie».

## Comandi di verifica

```bash
python staging/editorial/L234_20261020_124648/check.py     # FAIL totale: 0 (33 controlli)
python staging/editorial/L234_20261020_124648/verify.py    # FAIL: 0 (21 controlli), segmento 42/115
```
