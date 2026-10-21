# STATO — L121 · `data/human/campaign events.txt` (secondo lotto: 56 unità, 12 contesti)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L121_20261019_065925` |
| Righe / unità | **282–1332** / **56** |
| Tipi | **41 `DESCRIPTION`** · **14 `MISSION_TEXT`** · **1 `UI_LABEL`** |
| Stati | **56 `PENDING`** — misurato e **asserito** in `mkparts.py` |
| Contesti | **12** — 15 / 10 / 5 / 4×3 / 3×2 / 2×4 unità |
| Testi distinti | **52** per 56 unità — **4 coppie** ripetono l'inglese |
| Parole | **2486 EN → 2404 IT** (0,967); per unità 0,87–1,28, media 1,05 |
| Tab | **28 unità** con `\t` iniziale |
| Virgolette | **46** — due battute (unità 22 e 24) restano **aperte** come nel sorgente |
| Token | **1**: `<origin>` |
| Quadre · backtick | 0 · 0 |
| sha256 | `292f0d3b327b16f9…` |
| `check.py` | **32 controlli**, `FAIL totale: 0` |
| `verify.py` | **29 controlli**, exit **0** — invariante di **segmento** |

## La `UI_LABEL`, trattata come tale

L'unità 20 è `new stock`, una **label di nodo** e non prosa: resta **identica al sorgente**. È esclusa dal
controllo «tutte tradotte» e verificata in un controllo suo, con l'asserzione esplicita che sia l'unica `UI_LABEL`
del lotto e che il testo coincida. Senza questa distinzione, due controlli su tre sarebbero rossi su un lotto
corretto.

## Le due battute lasciate aperte

Le unità 22 e 24 aprono una battuta e **non la chiudono** (una sola virgoletta ciascuna): è il sorgente, e la resa
lo riproduce. Il `check.py` verifica che **siano esattamente quelle due** ad avere una virgoletta sola, così una
svista futura (o una «correzione» tipografica) fa fallire il lotto.

## Le 4 coppie ripetute

| testo | unità |
|---|---|
| `(Move on.)` | 13, 17 |
| primo paragrafo di Zug | 26, 28 |
| paragrafo di Poseidon Industries | 31, 35 |
| apertura di Greenrock | 45, 49 |

**52 testi distinti** per 56 unità, con una sola resa per testo.

## Contenuto

- **Schieramento iniziale** (1–10): Ingot, New Wales, New Austria, le basi della Marina.
- **Central Outfitters** (11–25): l'emporio con la merce di Kraz e Delta V, il commercio del Sindacato, le battute
  del proprietario.
- **Zug** (26–29): il Vecchio Porto, il Porto, il Porto Nuovo e «L'Ampliamento».
- **Kornephoros** (30–35): l'avamposto occupato, il porto sull'isola vulcanica, Clink e i suoi minatori.
- **Oathkeepers e conservatorio** (36–39): Farpoint, la branca neutrale della Marina, Winter e il Conservatorio dei
  Mondi Liberi.
- **Thule** (40–44): il mondo montuoso, la rinuncia alla pirateria, Smuggler's Den, gli anarchici che puzzano.
- **Greenrock** (45–56): occupata, abbandonata e recuperata, con i mercati di schiavi e «Mike's Mustelids».

## Verifica

```bash
cd staging/editorial/L121_20261019_065925
python mkparts.py   # 56 unità · 52 testi distinti · 1 UI_LABEL identica · 28 tab · 46 virgolette
python check.py     # FAIL totale: 0 (32 controlli)
python verify.py    # exit 0 (29 controlli)
```
