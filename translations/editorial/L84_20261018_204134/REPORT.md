# REPORT — L84 · `data/successors/predecessors.txt`

## 1. Cosa contiene il lotto

- **La scheda della Valkkyiara-Khorasaqra** (1–3): il nome dell'arma `"Tijra" Heirloom Lance` (dato), poi due
  paragrafi di prosa — le **Alte Casate dei Myiara** che nascondono flotte e ricchezze durante il crollo, e la
  nave stessa, «progetto collaudato dal tempo», con corazza specchiata e armi a lungo raggio, usata nei
  conflitti **fra le Casate**.
- **Il cannone di Sarija** (4): nascosto dalle Alte Casate dal crollo, «mantenuto con cura», più potente di
  qualunque tecnologia moderna dei Successori.

## 2. Scelte

| nodo | scelta | perché |
|---|---|---|
| `"Tijra" Heirloom Lance` | **identico** | dato (decisione 259) |
| `priceless family heirlooms` | **inestimabili cimeli di famiglia** | `heirloom` → «cimelio» (L76, L82) |
| `almost never leave the ground` | **non lasciano quasi mai il suolo** | letterale: sono navi, non reliquie |
| `martial artistry` | **arte marziale** | non «arte militare»: è estetica, non dottrina |
| `dense mirrored armor` | **corazza specchiata e compatta** | `dense` è la consistenza, `mirrored` il riflesso |
| `outmaneuver more lumbering warships` | **superare in manovra navi da guerra più pesanti** | `lumbering` è la lentezza, non la stazza |
| `lovingly-maintained` | **mantenuto con cura** | l'avverbio inglese è affettivo; «amorevolmente» sarebbe troppo |

## 3. Difficoltà

1. **Quattro unità su quattro contengono nomi propri**: Valkkyiara-Khorasaqra, Myiara, Alte Casate, Sarija —
   nessuno tradotto, e nessuna unificazione con le grafie di L83.
2. **Il tab torna** (unità 3): il costruttore lo aggiunge; le parti non ne hanno.
3. **Un bug mio nel `verify.py`**: leggevo `nxt['line']` su una tupla (nessun `row_factory`) e lo script è
   andato in `TypeError` prima di stampare; corretto in `nxt[0]`/`nxt[1]`.

## 4. Numeri osservati

```
unita' 4/4 · tab IT 1 / EN 1 · virgolette 2 = 2 · dispari 0
token 0 · duplicati 0 · rapporto 1.00 - 1.07
parole EN 169 -> IT 177 · righe 534/608
FAIL totale: 0 (24 controlli) · verify exit 0 (22 controlli)
sha256[:16] 4107161eef110612
```

## 5. Stato del progetto

```
TOTALE staging: 24810 unita · 789820 EN · 748715 IT
predecessors.txt: 52/59 (88,1%) · 648 EN -> 669 IT · 4 lotti
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | parte, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (24 controlli) **e** `verify.py` exit **0** (22 controlli) |
