# STATO — L123 · `data/human/ships.txt` (primo lotto: 54 unità, 33 navi)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L123_20261019_071206` |
| Righe / unità | **78–2044** / **54** — il lotto **apre** il file (0 unità prima) |
| Tipi | **48 `DESCRIPTION`** · **6 `VALUE`** |
| Stati | **54 `PENDING`** — misurato e **asserito** in `mkparts.py` |
| Contesti | **33** — 18×1, 11×2, 3×3, 1×5 |
| Testi distinti | **48** per 54 unità — la nota sui caccia compare **5 volte** |
| Parole | **2364 EN → 2483 IT** (1,050); per unità 0,97–1,28, media 1,08 |
| Tab | **14 unità** con `\t` iniziale |
| Virgolette | **16**, nelle unità 13, 21, 27, 36 e 42 |
| Token · quadre | **0** · **0** — asserzioni scritte |
| sha256 | `dce934d804256232…` |
| `check.py` | **29 controlli**, `FAIL totale: 0` |
| `verify.py` | **29 controlli**, exit **0** — invariante di **segmento** |

## La forma di un file di navi

| | `campaign events` (L122) | **`ships.txt` (L123)** |
|---|---|---|
| contesti per unità | 0,43 (18 su 42) | **0,61 (33 su 54)**, 18 da **una sola** nave |
| `VALUE` | 0 | **6** (nomi di nave al plurale) |
| token | 0 | **0** |
| virgolette | 8 | **16** (citazioni di nomi e di battute commerciali) |
| ripetizioni | 3 testi ×3 | **1 testo ×5** (la nota sui caccia) |

Un contesto per nave, non per blocco narrativo: le ripetizioni strutturali dei file di lavori qui non esistono, e
i `VALUE` sono **nomi propri al plurale** che restano inglesi (decisione 259).

## I 6 `VALUE` identici al sorgente

`Argosies` · `Auxiliaries` (×3) · `Finches` · `Furies` — nomi di nave al plurale, non prosa. Il `check.py` li
elenca esattamente (`VAL == [2, 6, 9, 10, 45, 53]`) e verifica che siano **identici** al sorgente; il resto del
lotto è tradotto.

## La nota dei caccia, cinque volte

«Fighters do not come equipped with a hyperdrive. You cannot carry a fighter unless you have a ship in your fleet
with a fighter bay.» compare nelle unità **15, 22, 38, 41 e 47**, sempre **identica**: una sola resa, verificata
dalla memoria di traduzione interna al lotto. Lo stesso vale per i tre `Auxiliaries`.

## Contenuto

- **Portatrici e navi capitali**: Aerie, Carrier, Cruiser, Dreadnought, Bactrian.
- **Navi da carico**: Bulk Freighter, Container Transport, Freighter, Class C «Freighter» (la Q-ship).
- **Caccia e droni**: Barb, Dagger, Finch, Combat Drone, Dropship, Boxwing.
- **Navali della Marina**: Auxiliary, Bastion, Frigate, Enforcer, Corvette.
- **Civili e pirati**: Argosy, Arrow, Blackbird, Bounder, Clipper, Cutthroat, Falcon, Flivver, Fury, Bulwark.

## Verifica

```bash
cd staging/editorial/L123_20261019_071206
python mkparts.py   # 54 unità · 48 testi distinti · 6 VALUE identici · 14 tab · 16 virgolette
python check.py     # FAIL totale: 0 (29 controlli)
python verify.py    # exit 0 (29 controlli)
```
