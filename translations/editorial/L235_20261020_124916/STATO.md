# STATO — L235 (`data/avgi/avgi news.txt`, righe 197–280) · **CHIUSO**

**Terzo lotto del file, e il primo di sola composizione.** Le due notizie di questa finestra non sono frasi: sono
**pezzi** che il gioco concatena senza separatore (`Phrase::Get()`: `result += ...`). Il lotto traduce 6 prefissi e 7
messaggi — **42 testi composti** — più le due unità di punteggiatura della seconda notizia.

| voce | valore misurato |
|---|---|
| file | `data/avgi/avgi news.txt` (115 unità · 2.164 parole, tutte `NEWS`) |
| righe | 197–280 |
| unità | **15** |
| parole | **72 EN → 68 IT** |
| rapporto | 0,69 – 1,30 (media 1,00) |
| tipi | **15 `NEWS`** |
| contesti | **2** — `safety advisory` 13, `missing advisory` 2 |
| struttura | **6 prefissi** (`"Cautela. `…`"Vigilanza. `, spazio finale) × **7 messaggi** (`. "` in coda) = **42 combinazioni** |
| tab | **0** |
| virgolette | **14** (una per prefisso, una per messaggio, una per la virgoletta aperta) |
| identiche | **2**, dichiarate: `"` e `.` (punteggiatura) |
| segnaposto | **0** |
| `check.py` | **32 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **21 controlli, `FAIL: 0`**, exit 0 |
| `sha256[:16]` di `translation.json` | **`d6825410bf2929d6`** |
| stato | **CHIUSO** (file aperto a 57/115) |

## Copertura del file

| lotto | righe | unità | EN → IT | check / verify | sha256[:16] |
|---|---|---|---|---|---|
| L233 | 32–91 | 22 | 447 → 441 | 32 / 20 | `14b34f5d9e29558c` |
| L234 | 115–180 | 20 | 439 → 433 | 32 / 21 | `a1598c95777cbd57` |
| **L235** | **197–280** | **15** | **72 → 68** | **31 / 21** | **`d6825410bf2929d6`** |
| residuo | 301–507 | 58 | — | — | — |
| **totale file** | **32–507** | **115** | **2.164** | | |

`22 + 20 + 15 + 58 = 115`: copertura **57/115 (49,6%)**. Confine misurato: **riga 301**, `news:avgi student happy`.

## La lacuna dichiarata

`news "avgi missing advisory"` compone il suo testo con **tredici** blocchi `word` (`"`, `Caution./Warning./Alert.`,
`" "`, `Convoy/Fleet/Patrol/…`, `reported lost/…`, `", "`, `last sighted/…`, `" "`, `leaving/entering/transiting`,
`the Ensemble system/…`, `.`). Il database conserva **solo il primo e l'ultimo** (righe 230 e 280): le parole interne
**non sono inventariate**, quindi quella notizia resterà quasi tutta in inglese anche con lo staging tradotto. Non è
riparabile da un lotto (`tools/l10n.py` e `state.db` sono protetti): si dichiara qui, nel `review.md` §5 e nel
`verify.py`, che la verifica con una query (`0 unità fra la 231 e la 279`) **e** con una lettura del file del gioco.

## Comandi di verifica

```bash
python staging/editorial/L235_20261020_124916/check.py     # FAIL totale: 0 (32 controlli)
python staging/editorial/L235_20261020_124916/verify.py    # FAIL: 0 (21 controlli), segmento 57/115
```

**Nota di ciclo**: `HANDOFF_L235_20261020.md` e `RIPRESA_L235_20261020.md` **non sono stati emessi** — L234 e L235 sono
stati chiusi nello stesso ciclo di lavoro, e il contratto d'ingresso usato per questa finestra è quello di
`HANDOFF_L234_20261020.md` più il piano misurato nel `REPORT.md` di L234. Il contratto del lotto successivo
(`HANDOFF_L236_20261020.md`) e la ripresa (`RIPRESA_L236_20261020.md`) esistono e danno `FAIL: 0 / 21`.
