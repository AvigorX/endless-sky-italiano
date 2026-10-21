# STATO — L96 · `data/coalition/coalition culture conversations.txt` (quarto lotto)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L96_20261018_214303` |
| Righe / unità | **192–234** (finestra 191–250) / **27** |
| Tipi | **22 `MISSION_TEXT`** + **5 `UI_LABEL`** (`defend ww`, `attack w`, `attack wr`, `attack r`, `attack rr`: etichette di salto, **identiche**) |
| Contesti | **1** (`Coalition Folklore: Kimek`, **chiuso**) |
| Parole | **2248 EN → 2023 IT** (0,900); per unità 0,92–1,45 |
| Tab · virgolette · token | **22** (tutte tranne le 5 etichette) · **26** (12 nell'unità 6) · **0** (asserzione) |
| Ripetizioni | **12/19** `(Prova a trovare un altro modo per entrare.)` · **14/21** il paragrafo dell'assalto |
| sha256 | `0c863a3843dd5f4e…` |
| `check.py` | **28 controlli**, `FAIL totale: 0` |
| `verify.py` | **29 controlli**, exit **0** |

## Dove siamo

| Voce | Valore |
|---|---|
| Unità prima della riga 192 | **94** (L93 + L94 + L95) |
| Unità dopo la riga 234 | **36** (riga 251, apre `Departing Trouble - A`) |
| File | **157 unità**, `max(line) = 462` |
| Copertura | **121/157 (77,1%)** · 7695 EN → 6996 IT · 4 lotti |

## Contenuto

La battaglia dal lato degli **attaccanti**: l'accampamento con le fasce blu, la «tenda da guerra» e il tronco
che farà da ariete, la spiegazione delle regole (e la battuta involontaria sul «legati al suolo»), la carica
lungo il pendio reso scivoloso dai secchi, gli Arach che avanzano scavando, i tre rami d'attacco (centrale,
lato lungo e lato lungo con la variante del cancello piccolo) e i tre esiti. Poi il **banchetto**: la poltiglia
Kimek, il piatto Saryd come cosa più vicina alla cucina umana, e il congedo dell'organizzatore («Un peccato,
è, che la battaglia la vostra squadra abbia perso»).

**Le cinque `UI_LABEL`** completano la serie dei salti della battaglia e sono rimaste identiche.

## Verifica

```bash
cd staging/editorial/L96_20261018_214303
python check.py   # FAIL totale: 0 (28 controlli)
python verify.py  # exit 0 (29 controlli)
```
