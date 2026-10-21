# REVIEW — L170 · `paradise world jobs.txt` (pensionati, ritiro, cantieri, Martini)

Coppie EN→IT rilette in `translation.json` (`900e58542d06ef12…`). Tutte le 20 unità sono **`PENDING`**.

## 1. Voce

Il lotto è **satira amministrativa** in tre varianti: i pensionati che sono criminali ricercati e finiscono con una
multa «modesta»; le pseudo-celebrità che pagano per farsi spennare da «guide naturalistiche» in tenuta ridicola; e i
quattro `Shipment` asciutti, dove l'unica nota di colore è la descrizione del cantiere. Chiude il tono **dolente**
dell'evacuazione della famiglia Martini.

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `no-questions-asked` | **senza domande** | 2, 6 |
| `the so-called retirees` | **i cosiddetti pensionati** | 3 |
| `obtained illegally` | **ottenuti illegalmente** | 3 |
| `an anyonymous source` (refuso) | **una fonte anonima** | 7 |
| `comically overdressed` | **comicamente agghindate** | 10 |
| `one of the most advanced shipyards in human space` | **uno dei cantieri più avanzati dello spazio umano** | 12, 14 |
| `nuclear bombing` | **bombardamento nucleare** | 20 |

## 3. Nodi aperti (da non dedurre dopo)

1. **Il refuso `anyonymous` è nel sorgente**: idx 7. La resa è quella di idx 4; il controllo verifica l'identità e la
   presenza del refuso nell'inglese, così nessuno «corregge» l'italiano per riflettere un errore inglese.
2. **`if raucous`**: L169 idx 17 diceva solo «gentili e pieni di aneddoti»; qui aggiunge «anche se chiassosi». Le due rese
   si somigliano ma **non sono la stessa unità**: non vanno uniformate.
3. **`Republic Navy Yard` resta inglese**: è un'istituzione con nome proprio.
4. **Il confine di riga 719 è un `VALUE`**: L171 apre con un `VALUE` (e ne ha **12 su 24 unità**).

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 20 unità `PENDING`.
- **Nessuna missione vista a schermo**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Quarto lotto di `paradise world jobs.txt`**.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (27 controlli), `verify.py` exit **0** (23 controlli) |
