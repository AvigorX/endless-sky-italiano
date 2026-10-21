# REPORT — L86 · `data/successors/successor outfits.txt` (primo lotto)

## 1. Contenuto

Ventuno unità in quindici contesti, tutte schede di equipaggiamento dei Successori: due licenze, una chiave
quantistica armonica, quattro cortex di scudi e la loro interfaccia, quattro celle betavoltaiche, due riserve
di energia, un reattore a fusione.

## 2. Scelte

| nodo | scelta | perché |
|---|---|---|
| `"Byiaa" Shield Cortices` (×4) | **identici** | `VALUE`: plurali dei nomi d'oggetto |
| `shield cortex` | **cortex di scudi** | termine tecnico, non «corteccia» (decisione 264) |
| `shield-softening effect` | **effetto di rammollimento degli scudi** | `softening` è la riduzione di resistenza, non di capacità |
| `outlast them` | **li logoravano** | l'idea è la durata, non la fuga |
| `twenty-fold` | **venti volte** | non «ventuplo» |
| `betavoltaic cell` | **cella betavoltaica** | termine tecnico coerente |
| `stellarator fusion reactors` | **reattori a fusione stellator** | `stellarator` è nome proprio di macchina |
| `power budget` | **budget di energia** | uso tecnico corrente, non «bilancio» |
| `bimodal engines` | **motori bimodali** | letterale e tecnico |
| `hull repair systems` | **sistemi di riparazione dello scafo** | `hull` → scafo (L82) |
| `eschew` | **evitano** | registro piano, come il resto della scheda |
| trattino lungo (unità 3) | **virgola** | em dash vietato |

## 3. Difficoltà

1. **Un solo tab** (unità 3) dopo un lotto a zero: il costruttore lo antepone, e il controllo lo verifica.
2. **Otto virgolette**, tutte nei nomi dei `VALUE`: nessuna nel testo tradotto.
3. **Un errore mio nel `check.py`**: una riga di `rows` aveva **due** elementi invece di tre, e lo script è
   andato in `ValueError` dopo aver stampato metà tabella. Corretto prima di dichiarare il verde.
4. **`VALUE` non sono nomi isolati ma plurali** (`Cortices`): restano identici, e il controllo positivo lo
   asserisce sul testo inglese.

## 4. Numeri osservati

```
unita' 21/21 · tab 1 · virgolette 8 = 8 · dispari 0
token 0 · duplicati 0 · rapporto 0.98 - 1.23
parole EN 1021 -> IT 1042 · righe 19/235
FAIL totale: 0 (26 controlli) · verify exit 0 (24 controlli)
sha256[:16] c3947926c8e088f1
```

## 5. Stato del progetto

```
TOTALE staging: 24838 unita · 791091 EN · 750015 IT
successor outfits.txt: 21/56 (37,5%) · 1021 EN -> 1042 IT · 1 lotto
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | parte, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (26 controlli) **e** `verify.py` exit **0** (24 controlli) |
