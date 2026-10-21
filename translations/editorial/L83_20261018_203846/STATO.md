# STATO — L83 · `data/successors/predecessors.txt`

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L83_20261018_203846` |
| Righe / unità | **446–520** (finestra 401–520) / **11** |
| Parte | 1 |
| Contesti | **4** — `outfit:"Torji," Lethal Sight` (446), `outfit:Crimson Halo` (461), `outfit:Visions of Rime` (475), `ship:Valkkyiara-Khorasaqra` (483–520) |
| Tipi | **7 `TEXT` + 3 `DESCRIPTION` + 1 `VALUE`** |
| Parole | 153 EN → 166 IT (**1,085**) |
| Rapporto per unità | **1,00 – 1,19** |
| Dato identico | **8 unità** (4–11): nome `Valkkyiara-Khorasaqran` + 7 nomi di equipaggiamento |
| Prosa tradotta | **3 unità** (1–3) |
| Tab · virgolette | **0** · **12** (0 dispari) |
| Token · duplicati | **0 = 0** · **0** |
| sha256 | `5c427d01bb9c39a0…` |
| `check.py` | **22 controlli**, `FAIL totale: 0` |
| `verify.py` | **27 controlli**, exit **0** |

## Dove siamo

| Voce | Valore |
|---|---|
| Unità prima della riga 446 | **37** (L81 + L82) |
| Unità dopo la riga 520 | **11** |
| File | **59 unità**, `max(line) = 782` |
| Confine dopo | riga **534** apre `ship:Valkkyiara-Khorasaqra` |
| Copertura | **48/59 (81,4%)** |

## Contenuto e decisioni

Tre schede in prosa: il **sistema di caricamento** di Torji (la nave drone Queru «costruita intorno» all'arma);
il **cortex di scudi** di Resja, che non serve a difendere ma a «restituire energia ai sistemi»; il **sistema di
raffreddamento** che irradia calore «attraverso la matrice degli scudi», efficientissimo sulle navi drone e
costoso in resistenza sulle navi minori. La quarta scheda apre la nave **Valkkyiara-Khorasaqra** con i suoi
sette equipaggiamenti.

**Regola applicata** (decisione 259): i nomi restano identici — `Valkkyiara-Khorasaqran`, `"Veusa" Inductive
Thruster`, `"Sarija" Heirloom Coilgun`… — mentre le tre `DESCRIPTION` sono prosa e sono tradotte. La grafia
`Valkkyiara-Khorasaqran` (nome) e `Valkkyiara-Khorasaqra` (contesto) convivono nel sorgente: **non unificate**.

## Verifica

```bash
cd staging/editorial/L83_20261018_203846
python check.py   # FAIL totale: 0
python verify.py  # exit 0
```

## Prossimo passo

**L84**: righe **521–620** (prima unità **534**), **4 unità**, **169 parole**, **2 contesti**
(`ship:Valkkyiara-Khorasaqra`, `outfit:"Sarija" Heirloom Coilgun`), tipi `3 DESCRIPTION + 1 TEXT`, **1 tab**.
