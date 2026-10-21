# STATO — L82 · `data/successors/predecessors.txt`

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L82_20261018_203543` |
| Righe / unità | **208–381** (finestra 201–400) / **15** |
| Parte | **1** — 15 unità |
| Contesti | **4** — `ship:Hasur, Vowsworn` (208), `ship:Queru, Luminous Gaze` (220–307), `outfit:"Iasa," Lethal Word` (348), `outfit:"Kis," Lethal Wish` (359–381) |
| Tipi | **8 `TEXT` + 5 `DESCRIPTION` + 2 `VALUE`** |
| Parole | 220 EN → 220 IT (**1,00**) |
| Rapporto per unità | **0,97 – 1,10** |
| Dato identico | **10 unità** — 2 nomi di nave/arma (3, 14) e 8 nomi di equipaggiamento |
| Prosa tradotta | **5 unità** (1, 2, 12, 13, 15) |
| Tab / virgolette | **1** (unità 2) / **8** — 0 dispari |
| Token · duplicati | **0 = 0** · **0 gruppi** |
| sha256 | `3a179de373b2fe67…` |
| `check.py` | **26 controlli**, `FAIL totale: 0` |
| `verify.py` | **32 controlli**, exit **0** |

## Dove siamo nel file

| Voce | Valore |
|---|---|
| Unità prima della riga 208 | **22** (L81) |
| Unità dopo la riga 381 | **22** |
| File | **59 unità**, `max(line) = 782` |
| Confine dopo | riga **446** apre `outfit:"Torji," Lethal Sight` |
| Copertura | **37/59 (62,7%)** |

## Cosa contiene e cosa è stato deciso

**L'avvertimento dei costrutti** (1–2): i costrutti della «sciocca Myiara» restano nelle stelle, «eternamente
morenti ma mai morti», e manterranno la promessa: «Ti uccideranno. Lo faranno in fretta.» La prosa è
allitterante e cupa; resa con lo stesso ritmo, senza spezzarla.

**Queru** (3, 12): la nave `Querun, Luminous Gazes` (dato) e la scheda: «venne per ultimo, ed era il più
ispirato dei tre: sventrava a distanza prima ancora di poter essere visto». Resja «lo odiavano», ma il loro
destino era già segnato.

**Iasa** (4–13): il nome dell'arma `"Iasa," Lethal Word` (dato), otto voci di equipaggiamento, e la scheda:
«il cannone a bobina perfetto di una nave drone», temibile e affamato, ancora efficiente dopo
**millecinquecento anni**.

**Kis** (14–15): `"Kis," Lethal Wishes` (dato) e la scheda: una «bestia fredda e famelica» che squarcia le
difese a corto raggio e, a lungo raggio, perde penetrazione ma resta un danno rispettabile.

**Regola applicata**: i nomi di nave e di equipaggiamento restano **identici** (decisione 259); le cinque
`DESCRIPTION` sono prosa e sono tradotte. `coilgun` → **cannone a bobina** (in prosa), mentre `"Sarija"
Heirloom Coilgun` resta dato.

## Verifica

```bash
cd staging/editorial/L82_20261018_203543
python check.py   # FAIL totale: 0   (26 controlli)
python verify.py  # exit 0           (32 controlli)
```

## Prossimo passo

**L83**: righe **401–520** (prima unità **446**), **11 unità**, **153 parole**, **4 contesti**
(`outfit:"Torji," Lethal Sight`, `outfit:Crimson Halo`, `outfit:Visions of Rime`,
`ship:Valkkyiara-Khorasaqra`), tipi `7 TEXT + 3 DESCRIPTION + 1 VALUE`, **0 tab**, virgolette **12**.
