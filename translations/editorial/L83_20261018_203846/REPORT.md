# REPORT — L83 · `data/successors/predecessors.txt`

## 1. Cosa contiene il lotto

Quattro blocchi del file delle armi e navi dei Predecessori:

- **"Torji," Lethal Sight** (1): Resja progettarono un **complesso sistema di caricamento** per far sparare
  l'arma così in fretta; la nave drone **Queru** fu costruita *intorno* all'arma — «una coppia di nave e arma».
- **Crimson Halo** (2): il **cortex di scudi** preferito da Resja non serve a difendere ma a **restituire
  energia** ai sistemi: «le navi di Resja non avevano bisogno degli scudi per difendersi, ma solo come
  carburante».
- **Visions of Rime** (3): il **sistema di raffreddamento** che irradia calore attraverso la matrice degli
  scudi — efficientissimo sulle navi drone, costoso in resistenza sulle navi minori.
- **Valkkyiara-Khorasaqra** (4–11): il nome della quarta nave e sette equipaggiamenti (`"Veusa" Inductive
  Thruster`, `"Veusa" Inductive Steering`, `"Ija" Heirloom Reactor`, `Heirloom Power Reserve`, `"Jiita"
  Heirloom Shielding`, `"Sarija" Heirloom Coilgun`, `"Tijra" Heirloom Lance`).

## 2. Scelte editoriali

| nodo | scelta | perché |
|---|---|---|
| `Valkkyiara-Khorasaqran` e 7 nomi di equipaggiamento | **identici** | dati (decisione 259) |
| `shield cortex` | **cortex di scudi** | termine tecnico del gioco, non «corteccia» |
| `feeding energy back into a starship's systems` | «restituire energia ai sistemi della nave» | il verbo è `feed back`, non `restore` |
| `all but insignificant` | **pressoché irrilevante** | idioma reso, non letterale |
| `it may come with a cost to endurance` | «può costare in resistenza» | `endurance` è la riserva di energia, non la pazienza |
| `loading system` | **sistema di caricamento** | non «ricarica»: è il meccanismo, non l'atto |
| trattino lungo in unità 2 | **virgola** | em dash vietato; il senso concessivo resta |

## 3. Difficoltà

1. **La grafia del nome**: `Valkkyiara-Khorasaqran` (unità 4) contro `Valkkyiara-Khorasaqra` (contesto di
   riga 483). Non è un refuso mio: il sorgente le distingue, e non le unifico.
2. **`-` in unità 2** (`for defense - only as fuel`): resa con virgola.
3. **Tre schede tecnico-narrative** in tre unità consecutive: nessuna ripetizione di formula, ma stesso
   registro (spiegazione + giudizio).
4. **Il tab torna a zero** (in L82 era 1): le parti non ne hanno e il controllo lo verifica.

## 4. Numeri osservati (output letto)

```
unita' 11/11 · tab 0 · virgolette IT 12 / EN 12 · dispari 0
token 0 = 0 · duplicati 0
rapporto IT/EN 1.00 - 1.19
parole EN 153 -> IT 166
righe 446/520
FAIL totale: 0    (22 controlli)
verify.py exit 0  (27 controlli)
sha256[:16] 5c427d01bb9c39a0
```

## 5. Stato del progetto

```
TOTALE staging: 24806 unita · 789651 EN · 748538 IT
predecessors.txt: 48/59 (81,4%) · 479 EN -> 492 IT · 3 lotti
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 1 parte, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (22 controlli) **e** `verify.py` exit **0** (27 controlli) |
