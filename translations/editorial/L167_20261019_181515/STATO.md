# STATO — L167 · `paradise world jobs.txt` (nove lavori «di lusso», 62 token)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L167_20261019_181515` |
| Righe / unità | **16–221** / **28** — file al **28/131 (21,4%)** |
| Tipi | **9 `VALUE`** · **9 `DESCRIPTION`** · **9 `DIALOG`** · **1 `MISSION_TEXT`** |
| `UI_LABEL` | **0** — asserzione vuota scritta |
| Token | **62** su **9** simboli (18 `<payment>`, 10 `<planet>`, 9 `<destination>`, 7 `<commodity>`, 6 `<date>`, 5 `<tons>`, 4 `<cargo>`, 2 `<bunks>`, 1 `<origin>`) |
| Contesti | **9** · **27 testi distinti** su 28 unità |
| Parole | **566 EN → 604 IT** (1,067); **0,89–1,30**, media **1,08** |
| Tab · virgolette | **0** · **2** (in idx 21) |
| sha256 | `58330ce6689b1aed…` |
| Esiti | `check.py` **23** (`FAIL 0`) · `verify.py` **21**, exit **0** |

## Cosa contiene

| blocco | unità | righe | contenuto |
|---|---|---|---|
| nove lavori «di lusso» | 1-28 | 16-221 | pacco premuroso, compleanno, arte, sposi, teatro, cibo pregiato, due festaioli, donazioni |

## Token: il lotto più «tokenizzato» della campagna

| simbolo | occorrenze |
|---|---|
| `<payment>` | 18 |
| `<planet>` | 10 |
| `<destination>` | 9 |
| `<commodity>` | 7 |
| `<date>` | 6 |
| `<tons>` | 5 |
| `<cargo>` | 4 |
| `<bunks>` | 2 |
| `<origin>` | 1 |

Verificati come **multiset** e come **ordine per unità** (28/28), con l'**assenza incrociata** `<destination>`/`<planet>`.

## Rese che contano

| EN | IT |
|---|---|
| `care package` | **pacco di generi di conforto** |
| `pouty young sprout throwing a fit` | **ragazzino imbronciato che fa una scenata** |
| `the two lovebirds` | **i due piccioncini** |
| `completely legal pharmaceuticals` | **farmaci del tutto legali** (virgolette conservate) |
| `rowdy and uncouth troublemakers` | **piantagrane chiassosi e maleducati** |
| `undernourished souls` | **anime denutrite** |

## Verifica

```bash
cd staging/editorial/L167_20261019_181515
python check.py     # FAIL totale: 0 (23 controlli)
python verify.py    # exit 0 (21 controlli)
```

**Il lotto apre il file**: 0 unità prima della riga 16, 103 dopo la 221, confine alla riga 225 (`VALUE`).

**Non verificato**: nessun lavoro visto a schermo; i testi non sono stati caricati nel gioco.
