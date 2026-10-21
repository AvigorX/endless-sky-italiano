# REVIEW — L225 · `remnant outfits.txt` (terzo lotto)

Coppie EN→IT rilette in `translation.json` (`66b157150c05ada7…`). Tutte le 11 unità sono **`PENDING`**.

## 1. La famiglia di «ion»

| inglese | italiano | unità | nota |
|---|---|---|---|
| *energy draining effects of ionization* | «effetti di drenaggio energetico della ionizzazione» | 2 | `draining` = drenaggio, non «consumo» |
| *ion dissipation effects* | «effetti di dissipazione ionica» | 4 | lega i cristalli di Viminal ai generatori |
| *ion resistance* | «resistenza ionica» | 6 | |
| *ion storms* | «tempeste ioniche» | 6 | al secondo riferimento il testo dice solo «dalla tempesta» |

Misura: «ionica» **2**, «ionizzazione» **1**, «ioniche» **1**. Il controllo verifica il numero, non l'impressione.

## 2. Le «branchie»

*While this risk is non-existent in Remnant ships due to their "gills," which are effectively built-in ramscoops…* →
«A bordo delle navi dei Remnant questo rischio non esiste, grazie alle loro "branchie", che sono in pratica dei ramscoop
integrati…». Le virgolette restano perché sono il segnale che «branchie» è un soprannome di bordo, e `ramscoop` resta
invariato come nome tecnico.

## 3. Decisioni di resa

1. **`radiothermal generator`** → «generatore radiotermico»; **`isotopes so radioactive … so tightly packed together`** →
   «isotopi così radioattivi, e così strettamente addensati».
2. **`could almost be classified as a nuclear reactor`** → «potrebbe quasi essere classificato come reattore nucleare»:
   `quasi` tiene l'approssimazione, che è il punto della scheda.
3. **`not very impressive in terms of how much energy they produce`** → «non impressionino granché per la quantità di
   energia che producono».
4. **`converted into electricity instead of becoming waste heat`** → «convertito in elettricità invece di diventare calore
   disperso».
5. **`replicated them for their generators`** → «li hanno replicati nei propri generatori».
6. **`did not trust the finicky and unpredictable nuclear reactors`** → «non si fidavano dei reattori nucleari capricciosi
   e imprevedibili».
7. **`perfecting the art of radioisotope thermoelectric power`** → «perfezionare l'arte dell'energia termoelettrica a
   radioisotopi».
8. **`not only allows them to bounce back … but also gives their ships a window of time`** → «non solo permette loro di
   riprendersi … ma dà anche alle loro navi una finestra di tempo».
9. **`before becoming debilitated by the storm`** → «prima di restare paralizzate dalla tempesta»: `debilitated` è la
   paralisi da ionizzazione del gioco.
10. **`wired so it can run in reverse`** → «collegato in modo da funzionare al contrario».
11. **`replenishing hyperspace fuel`** → «rifornire il carburante per l'iperspazio».
12. **`commissioned these directly from their inventor`** → «li commissionarono direttamente all'inventore».
13. **`a robotic counterpart`** → «una controparte robotica»; **`boarding actions`** → «azioni di abbordaggio».
14. **`built onto the side of a cargo bay, mess hall, or other larger room`** → «costruito sul fianco di una stiva, di un
    refettorio o di un altro locale più ampio».
15. **`expands out to convert it into a fully fledged laboratory`** → «si espande e lo trasforma in un laboratorio a tutti
    gli effetti».

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 11 unità `PENDING`.
- **Nessun equipaggiamento visto nel gioco**: né il funzionamento della resistenza ionica né l'espansione del laboratorio
  sono stati osservati in partita.
- **Nessuna revisione umana**, **nessuna correzione al sorgente**.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì |
| ESEGUITO | sì |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (25), `verify.py` exit **0** (18) |
