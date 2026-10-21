# STATO — L233 (`data/avgi/avgi news.txt`, righe 32–91) · **CHIUSO**

**Primo lotto di `data/avgi/avgi news.txt`**: 22 notizie Avgi, tutte `NEWS`, tre contesti completi. Il file **non** è
chiuso: restano 93 unità dopo la riga 91, e l'invariante è di **segmento**.

| voce | valore misurato |
|---|---|
| file | `data/avgi/avgi news.txt` (115 unità · 2.164 parole, tutte `NEWS`) |
| righe | 32–91 |
| unità | **22** |
| parole | **447 EN → 441 IT** |
| rapporto | 0,93 – 1,25 (media 1,11) |
| tipi | **22 `NEWS`**, zero `VALUE`, zero `UI_LABEL` |
| contesti | **3** — `siege civilian` 11, `siege merchant` 5, `siege hatchling` 6 |
| tab | **0** |
| virgolette | **44**, esattamente **2 per unità** (citazione intera, mai spezzata) |
| apici | **12 EN** su 9 unità / **5 IT** su 5 unità |
| segnaposto | **0** |
| identiche | **0** (22 tradotte) |
| `check.py` | **33 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **20 controlli, `FAIL: 0`**, exit 0 |
| `sha256[:16]` di `translation.json` | **`14b34f5d9e29558c`** |
| stato | **CHIUSO** (file aperto) |

## Copertura del file

| lotto | righe | unità | EN → IT | check / verify | sha256[:16] |
|---|---|---|---|---|---|
| **L233** | **32–91** | **22** | **447 → 441** | **32 / 20** | **`14b34f5d9e29558c`** |
| residuo | 115–507 | 93 | — | — | — |
| **totale file** | **32–507** | **115** | **2.164** | | |

`22 + 93 = 115`: la 32 è la **prima** unità del file, la 91 non è l'ultima. Confine misurato: **riga 115**,
`news:avgi merchant` — fra la 92 e la 114 il file non ha unità.

## Cosa cambia rispetto a L232

1. **Da un file di equipaggiamenti a un file di notizie**: 22 dichiarazioni di civili Avgi sotto assedio, nessun
   `VALUE`, nessun riferimento di dato.
2. **La citazione è intera**: 2 virgolette per unità, aperte e chiuse dentro l'unità. In `coalition news.txt` la
   citazione si spezzava su più unità e il controllo era una **distribuzione**; qui è un `2 == count('"')` per unità.
3. **Il registro è l'etichetta**: ogni notizia comincia con la modalità dichiarata (`Scoramento.`, `Rifiuto.`,
   `Colpa.`, `Meraviglia.`…), 22 etichette, due ripetute (`Ricordo`, `Frustrazione`) perché l'inglese le ripete.
4. **Zero tab** in tutto il lotto: nessun `MISSION_TEXT`, nessun separatore di paragrafo.

## Comandi di verifica

```bash
python staging/editorial/L233_20261020_123813/check.py     # FAIL totale: 0 (33 controlli)
python staging/editorial/L233_20261020_123813/verify.py    # FAIL: 0 (20 controlli), segmento 22/115
```
