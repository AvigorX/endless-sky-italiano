# STATO — L119 · `data/human/pirate jobs.txt` (terzo lotto, **chiude il file**: 77 unità)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L119_20261019_064438` |
| Righe / unità | **2958–3706** / **77** — ultima unità del file |
| Tipi | **32 `DIALOG`** · **17 `DESCRIPTION`** · **16 `VALUE`** · **12 `CONVERSATION`** |
| Stati | **77 `PENDING`** — misurato e **asserito** in `mkparts.py` |
| Contesti | **20** — 19 missioni da quattro unità e **uno da una sola** (`outfit:Secret Cargo`) |
| Testi distinti | **47** per 77 unità — 4 nomi + 43 testi prosaici (2 già resi in L118) |
| Parole | **1223 EN → 1246 IT** (1,019); per unità 0,86–1,31, media 1,10 |
| Tab | **9 unità** che iniziano con `\t` (le tre opzioni di ciascuna delle tre scene) |
| Virgolette | **6** — due per scena, nelle unità 13, 25, 37 |
| Token | **106** in sei famiglie: `<planet>` 28, `<payment>` 23, `<destination>` 19, `<system>` 14, `<npc>` 12, `<day>` 10 |
| Quadre · backtick | 0 · 0 |
| sha256 | `51189eab238776c8…` |
| `check.py` | **31 controlli**, `FAIL totale: 0` |
| `verify.py` | **31 controlli**, exit **0** — invariante **di file** |

## Il file è chiuso

```
data/human/pirate jobs.txt   279/279 unità (100,0%) · 3227 EN -> 3245 IT · 3 lotti
L117 20–1624 (98) · L118 1627–2955 (104) · L119 2958–3706 (77)
verify L119: 279/279 righe coperte · sovrapposti = 0 · max(line) = 3706
```

`pirate jobs.txt` è il **secondo file di missioni chiuso** della campagna recente e porta i **file completi a
quarantatré**.

## Il tipo nuovo: `CONVERSATION`

Tre scene (`northern`, `core`, `southern pirate defense`), ognuna con:

| unità | contenuto | forma |
|---|---|---|
| 13 / 25 / 37 | la battuta d'apertura con le grida fuori | **2 virgolette** per unità, nessuna tab |
| 14 / 26 / 38 | `(Stay here until the fight is over.)` | **1 tab** iniziale |
| 15 / 27 / 39 | `(Join the defense fleet.)` | **1 tab** iniziale |
| 16 / 28 / 40 | la scelta di unirsi alla flotta | **1 tab** iniziale, ricostruita per Marina/Sindacato/milizia |

Il controllo conta **unità** che iniziano con tab (**9**), non caratteri, e verifica che in ogni unità il numero
di tab sia **lo stesso** dell'inglese: le parti non contengono tab, li antepone il costruttore.

## Il refuso del sorgente, dichiarato

L'unità 73 dice «thanks you for eliminating the politician **pays** you `<payment>`»: manca «and». La resa è
**identica** a quella dell'unità 65, e invece di inventare una differenza la si **dichiara** in `EXC`; il
`check.py` ammette **un solo** doppio di resa, quello (65/73), e nessun altro.

## Contenuto

- **Raid on Merchants (South)** (1–4): la flotta mercantile meridionale, con i due dialoghi già resi in L118.
- **Difesa dei pirati** (5–40): tre regioni (Nord/Marina, Centro/Sindacato, Sud/milizia), ognuna con versione
  pagata e non pagata, e la scena in cui il giocatore decide se unirsi.
- **Cargo Theft** (41–53): il carico segreto, tre regioni, con l'atterraggio a mani vuote.
- **Assassinii politici** (54–77): Mondi Liberi, Sindacato e Repubblica, due taglie ciascuno.

## Verifica

```bash
cd staging/editorial/L119_20261019_064438
python mkparts.py   # 77 unità · 16 VALUE (4 nomi) · 43 testi prosaici (2 da L118) · 106 token
python check.py     # FAIL totale: 0 (31 controlli)
python verify.py    # exit 0 (31 controlli) — 279/279 righe coperte, sovrapposti 0
```
