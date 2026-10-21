# STATO — L147 · `coalition jobs.txt` (i lavori dell'Anello: il lotto più denso di token)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L147_20261019_171044` |
| Righe / unità | **16–293** / **30** — file al **15,2%** (30/197) |
| Tipi | **13 `VALUE`** (identici) · **13 `DESCRIPTION`** · **4 `TEXT`** |
| `LOGBOOK` · `DIALOG` · `UI_LABEL` | **0** · **0** · **0** — tre asserzioni vuote |
| Token | **65 occorrenze** su **7 simboli**, parità **per simbolo e per unità** |
| Stati | **30 `PENDING`** — misurato e **asserito** |
| Contesti | **17** |
| Testi | **14 distinti** — **4 gruppi tripli** a resa unica |
| Parole | **437 EN → 412 IT** (0,943); per unità **0,86–1,16**, media **1,01** |
| Tab · virgolette | **0** · **0** — due asserzioni vuote |
| sha256 | `86d0e8e3b5fccb2f…` |
| `check.py` | **28 controlli**, `FAIL totale: 0` |
| `verify.py` | **27 controlli**, exit **0** — invariante di **segmento** |

## 65 token: la parità non si fa sul totale

| simbolo | occorrenze |
|---|---|
| `<planet>` | 28 |
| `<payment>` | 17 |
| `<bunks>` | 6 |
| `<tons>` | 6 |
| `<date>` | 4 |
| `<origin>` | 3 |
| `<commodity>` | 1 |

**65 in inglese e 65 in italiano** non basta: se `<payment>` e `<date>` si scambiassero di posto, il totale resterebbe
65. Per questo ci sono **tre** controlli distinti — multiset per simbolo, **ordine per unità** (`TAGS.findall(italiano)
== TAGS.findall(inglese)` su tutte e 30), e due conteggi nominati (`<payment>` = 17, `<date>` = 4).

## Tredici `VALUE` che non si traducono

`Workers to the <planet>`, `Volunteers to the <planet>`, `Materials to the <planet>`, `Supplies to the <planet>`,
`Candidate to the <planet>` — **tre volte ciascuno**. Sono nomi di lavoro mostrati in interfaccia: restano identici,
**token compreso** (un valore senza `<planet>` sarebbe un altro lavoro), e si verificano **uno per uno**, non con un
`len()`.

## Ripetizioni triple

I modelli si ripetono tre volte ciascuno, uno per livello di difficoltà della missione. La resa è **la stessa
stringa**: il controllo confronta `3 == 5 == 7`, `10 == 12 == 14`, `17 == 19 == 21`, `24 == 26 == 28`. Se una copia
divergesse, il giocatore vedrebbe tre testi diversi per lo stesso lavoro.

## Verifica

```bash
cd staging/editorial/L147_20261019_171044
python mkparts.py   # 30 unità · 13 VALUE + 13 DESCRIPTION + 4 TEXT · 65 token · zero tab · zero virgolette
python check.py     # FAIL totale: 0 (28 controlli)
python verify.py    # exit 0 (27 controlli, invariante di segmento)
```

**Non verificato**: nessun lavoro accettato nel gioco; i tre livelli della stessa missione non sono stati giocati.
