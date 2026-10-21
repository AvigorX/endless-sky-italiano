# STATO — L84 · `data/successors/predecessors.txt`

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L84_20261018_204134` |
| Righe / unità | **534–608** (finestra 521–620) / **4** |
| Contesti | **2** — `ship:Valkkyiara-Khorasaqra` (534–569), `outfit:"Sarija" Heirloom Coilgun` (608) |
| Tipi | **1 `TEXT` (dato) + 3 `DESCRIPTION` (prosa)** |
| Parole | 169 EN → 177 IT (1,047); per unità 1,00–1,07 |
| Tab · virgolette | **1** (unità 3) · **2** (0 dispari) |
| Token · duplicati | **0 = 0** · **0** |
| sha256 | `4107161eef110612…` |
| `check.py` | **24 controlli**, `FAIL totale: 0` |
| `verify.py` | **22 controlli**, exit **0** |

## Dove siamo

| Voce | Valore |
|---|---|
| Unità prima della riga 534 | **48** (L81–L83) |
| Unità dopo la riga 608 | **7** |
| File | **59 unità**, `max(line) = 782` |
| Confine dopo | riga **648** apre `outfit:"Tijra" Heirloom Lance` |
| Copertura | **52/59 (88,1%)** |

## Contenuto e decisioni

Le **Alte Casate dei Myiara** misero da parte beni e **flotte private** durante il crollo: navi da guerra
«tramandate per oltre mille anni come inestimabili cimeli di famiglia», che «non lasciano quasi mai il suolo»
perché non si vogliono rischiare. La **Valkkyiara-Khorasaqra** era già un progetto collaudato: «corazza
specchiata e compatta», alta velocità, armi a lungo raggio, impiegata nei conflitti **fra le Casate**. Il
**cannone a bobina** di Sarija, nascosto dalle Alte Casate, è «molto più potente di qualunque tecnologia
moderna dei Successori».

`"Tijra" Heirloom Lance` resta identico (dato). `coilgun` in prosa → «cannone a bobina» (come in L82).

## Verifica

```bash
cd staging/editorial/L84_20261018_204134
python check.py   # FAIL totale: 0
python verify.py  # exit 0
```
