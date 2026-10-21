# STATO — L132 · `unfettered side missions.txt` (primo lotto: 84 unità, il disertore e l'Anomalocaris)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L132_20261019_124026` |
| Righe / unità | **17–229** / **84** — il lotto **apre** il file (0 unità prima) |
| Tipi | **78 `MISSION_TEXT`** · **3 `UI_LABEL`** · **1 `DESCRIPTION`** · **1 `DIALOG`** · **1 `LOGBOOK`** |
| `VALUE` | **0** — asserzione **vuota scritta** |
| Stati | **84 `PENDING`** — misurato e **asserito** |
| Contesti | **2** — 18 / 66 |
| Testi distinti | **82** per 84 unità |
| Parole | **2055 EN → 1850 IT** (0,900); per unità 0,58–1,53, media 1,01 |
| Tab | **74 unità** su 84 |
| Virgolette | **89** — 43 unità senza, 33 con 2, **5 con 4**, **3 con una sola** (57, 62, 73) |
| Token | **8** in **4 famiglie**: `<last>` 4, `<destination>` 2, `<first>` 1, `<payment>` 1 |
| sha256 | `4fcdf80f4d1d3888…` |
| `check.py` | **30 controlli**, `FAIL totale: 0` |
| `verify.py` | **32 controlli**, exit **0** — invariante di **segmento** |

## Il valore più alto di virgolette finora

**89 virgolette in 84 unità**: più di una per unità. La distribuzione è misurata e asserita:

| virgolette per unità | unità |
|---|---|
| 0 | 43 |
| 2 | 33 |
| 4 | 5 |
| **1** | **3** (57, 62, 73) |

Le tre unità con **una sola** virgoletta sono battute che il sorgente apre e non chiude (`"We could have, but where's
the fun in that? …`): la resa le riproduce così, e il controllo verifica che le dispari siano esattamente quelle tre.

## Le 3 `UI_LABEL` e la resa identica dichiarata

`train back` · `tell me` · `try again` (unità 39, 43, 48): **nomi di nodo**, identici al sorgente.

Una **quarta** unità ha resa identica per necessità: `(No.)` (unità 4). In italiano la scelta è la stessa stringa, e
ometterla dal controllo «tutte tradotte» la farebbe bocciare: è dichiarata in `ID_OK` nel costruttore e verificata a
parte, come i frammenti di sola punteggiatura di L129.

## Le scelte dichiarate

| nodo | resa | perché |
|---|---|---|
| `Hai-home` | **Hai-home** | è il **nome del mondo**, non una descrizione: resta nome proprio |
| `the "tribute"` | **il "tributo"** | virgolette doppie, come il sorgente |
| `'Hai-home is your home too. Rejoin your people.'` | **'Hai-home è casa tua. Torna al tuo popolo.'** | virgolette **singole** dentro la battuta, come il sorgente |
| `Anomalocaris` | **Anomalocaris** | nome della nave-classe |
| `Korath` · `Unfettered` · `Hai` | invariati | nomi propri |
| `10 million credits in cash` | **dieci milioni di crediti in contanti** | numero scritto in lettere, come nel testo |

## Contenuto

- **`Unfettered returning home`** (1–18): il giovane Hai che gratta al portello, la scritta dentro l'involucro del
  tributo, il rifiuto dei suoi, il viaggio fino a Hai-home e l'accoglienza della folla.
- **`Hai Legacy 1`** (19–84): la figura incappucciata nel cantiere, il biglietto del treno, la stazione sotterranea, la
  spiaggia, la nave che emerge dal mare, la grotta con l'**Anomalocaris**, la proposta dei dieci milioni e le quattro
  strade (accettare, chiedere dell'equipaggio, chiedere della nave nascosta, rifiutare), più gli esiti dello scontro a
  fuoco.

## Verifica

```bash
cd staging/editorial/L132_20261019_124026
python mkparts.py   # 84 unità · 82 testi distinti · 3 UI_LABEL + 1 identica dichiarata · zero VALUE
python check.py     # FAIL totale: 0 (30 controlli)
python verify.py    # exit 0 (32 controlli)
```
