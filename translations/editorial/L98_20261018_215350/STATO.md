# STATO — L98 · `data/hai/hai culture conversations.txt` (file nuovo, primo lotto)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L98_20261018_215350` |
| Righe / unità | **1–105** / **39** |
| Tipi | **39 `MISSION_TEXT`** — **0 `UI_LABEL`** (premessa asserita) |
| Contesti | **3** in ordine di riga: `Theater Chat` (26–33), `Musical Entertainment Expo` (47–69), `The Meme Wars 1` (83–105) |
| Parole | **1262 EN → 1180 IT** (0,935); per unità 0,89–1,50 |
| Tab · virgolette · token | **36** · **58** · **1** (`<destination>`, unità 7) |
| Quadre | **6** = **3 coppie** nell'unità 30 (voce del dispositivo di traduzione) |
| Ripetizioni | **20/37**, **27/31**, **29/39** — rese identiche; **28 e 32 differiscono per una virgola** |
| sha256 | `8df01d63f077d9a2…` |
| `check.py` | **29 controlli**, `FAIL totale: 0` |
| `verify.py` | **28 controlli**, exit **0** |

## Invariante di segmento (primo lotto del file)

| Voce | Valore |
|---|---|
| Unità prima della riga 26 | **0** — nessun lotto precedente su questo file |
| Unità dopo la riga 105 | **108** |
| Confine | riga **119** apre `mission:Wrestling Star` |
| File | **147 unità**, `max(line) = 386` |
| Copertura | **39/147 (26,5%)** |

## Contenuto

Tre scene nello spazioporto Hai:

- **Theater Chat**: una donna umana e una Hai di nome **Gemanari** davanti all'annuncio olografico di uno
  spettacolo. Il dialogo gira su una disputa di interpretazioni — quella **germontiana** («darwinista sociale»,
  per l'umana) e la **centottantatreesima versione**, l'unica vera secondo la zia di Gemanari — intorno a
  un'opera su un Hai preistorico alato trovato congelato nel ghiaccio.
- **Musical Entertainment Expo**: il bar pieno di tifosi in merchandising, il cameriere esasperato e la
  spiegazione dell'industria musicale Hai: la **ME2**, le etichette che allevano band, «facciamo pop music da
  più tempo di quanto la vostra gente abbia conosciuto il fuoco».
- **The Meme Wars 1**: lo spazioporto invaso da ologrammi e striscioni, l'**anziano triangolare** contro
  l'**ortaggio a radice**, il traduttore che interviene con le sue alternative fra quadre, e la guardia che
  spiega la battuta dei tre principi contro i quattro delle nuove priorità educative.

## Verifica

```bash
cd staging/editorial/L98_20261018_215350
python check.py   # FAIL totale: 0 (29 controlli)
python verify.py  # exit 0 (28 controlli)
```
