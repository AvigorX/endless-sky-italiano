# STATO — L81 · `data/successors/predecessors.txt` (file nuovo: descrizioni di navi)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L81_20261018_203012` |
| Righe / unità | **17–196** (finestra 1–200) / **22** |
| Parte | **1** — 22 unità |
| Contesti `ship:` | **2** — `Resja, of the Nine Eyes` (17–112), `Hasur, Vowsworn` (123–196) |
| Tipi | **15 `TEXT` + 5 `DESCRIPTION` + 2 `VALUE`** |
| Parole | 106 EN → 106 IT (**1,00**) |
| Rapporto per unità | **1,00 – 1,21** |
| Dato identico | **17 unità** — nomi di nave (2 `VALUE`) e di equipaggiamento (15 `TEXT`) |
| Prosa tradotta | **5 unità** — la poesia di Resja (10–14), **rimata** |
| Tab / virgolette | **0** / **12** — 0 dispari |
| Token | **0 = 0** (assenza asserita) |
| Duplicati | **5 gruppi** (3/17, 4/18, 6/20, 7/21, 9/22) — gli stessi nomi su due navi |
| sha256 | `26f957d5edbd1958…` |
| `check.py` | **30 controlli**, `FAIL totale: 0` |
| `verify.py` | **34 controlli**, exit **0** |

## Dove siamo nel file

| Voce | Valore |
|---|---|
| Unità prima della riga 17 | **0** (il lotto apre il file) |
| Unità dopo la riga 196 | **37** |
| File | **59 unità**, `max(line) = 782` |
| Confine dopo | riga **208** apre `ship:Hasur, Vowsworn` |
| Copertura | **22/59 (37,3%)** |

## La decisione che governa il lotto

**Diciassette unità su ventidue sono dati, non prosa**: `Resjan, of the Nine Eyes` e `Hasuran, Vowsworn` sono
nomi di nave, e `Hyperdrive`, `"Jiita" Heirloom Shielding`, `Heirloom Cooling`, `Multimodal Armor: Regen`
sono nomi di equipaggiamento **definiti altrove** nel gioco. Tradurli solo qui creerebbe una scheda in
italiano che cita oggetti in inglese, o peggio un nome tradotto che non corrisponde all'oggetto. Restano
**identici** e sono dichiarati uno per uno (`DATA` in `check.py`, `NT` in `verify.py`).

**Le cinque `DESCRIPTION` sono prosa** e sono tradotte: l'introduzione e i **quattro versi** incisi da Resja
sugli scafi. L'inglese rima (`there / flare / light / night`); l'italiano rima **sulle stesse quattro
strofe** (`dimora / divora / ancora / ignora`) e il `verify.py` verifica le desinenze.

## Verifica

```bash
cd staging/editorial/L81_20261018_203012
python check.py   # FAIL totale: 0   (30 controlli)
python verify.py  # exit 0           (34 controlli)
```

## Prossimo passo

**L82**: righe **201–400** (prima unità alla **208**), **15 unità**, **220 parole**, **4 contesti**
(`ship:Hasur, Vowsworn`, `ship:Queru, Luminous Gaze`, `outfit:"Iasa," Lethal Word`,
`outfit:"Kis," Lethal Wish`), tipi `8 TEXT + 5 DESCRIPTION + 2 VALUE`, **1 tab**, virgolette **8**, 0 token.
