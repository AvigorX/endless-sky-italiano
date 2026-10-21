# STATO — L171 · `paradise world jobs.txt` (dodici evacuazioni da Martini, `<planet>` 28 volte)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L171_20261019_183021` |
| Righe / unità | **719–987** / **24** — file al **113/131 (86,3%)** |
| Tipi | **12 `VALUE`** · **12 `DESCRIPTION`** — nient'altro |
| `UI_LABEL` | **0** — asserzione vuota scritta |
| Token | **55** su **5** simboli: **`<planet>` 28**, `<payment>` 12, `<bunks>` 7, **`<martini house>` 4**, `<cargo>` 4 |
| Contesti | **12** · **22 testi distinti** su 24 |
| Parole | **497 EN → 470 IT** (0,946); **0,90–1,03**, media **1,00** |
| Tab · virgolette · apici | **0** · **0** · **1 EN / 2 IT** |
| sha256 | `d494b88bbb2ea449…` |
| Esiti | `check.py` **27** (`FAIL 0`) · `verify.py` **22**, exit **0** |

## Cosa contiene

| blocco | unità | righe | contenuto |
|---|---|---|---|
| residenti e famiglie | 1-8 | 719-809 | residenti, singoli, famiglia e singolo **di lusso** |
| turisti | 9-16 | 839-902 | turista, coppia, famiglia, gruppo |
| uomini d'affari | 17-20 | 922-945 | gruppo e singolo |
| personale sanitario | 21-24 | 965-987 | medici e squadra di ricerca e soccorso, congedati |

## Il salto vuoto

Fra l'ultima unità del lotto (**987**) e la successiva (**1230**) **non esiste alcuna unità**: 242 righe di sole
definizioni di missione. Il `verify.py` lo verifica esplicitamente (`count(line>987 and line<1230) == 0`), così un
confine sbagliato non può passare inosservato.

## Apici: 1 in inglese, 2 in italiano

| unità | EN | IT | causa |
|---|---|---|---|
| 24 | 1 | 0 | `Martini's capital city` → **nella capitale di Martini** (possessivo perso) |
| 18, 20 | 0 | 1 + 1 | `businessmen` → **uomini d'affari** (apostrofo necessario) |

## Verifica

```bash
cd staging/editorial/L171_20261019_183021
python check.py     # FAIL totale: 0 (27 controlli)
python verify.py    # exit 0 (22 controlli, con il salto vuoto 988-1229)
```

**Non verificato**: nessuna missione vista a schermo; i testi non sono stati caricati nel gioco.
