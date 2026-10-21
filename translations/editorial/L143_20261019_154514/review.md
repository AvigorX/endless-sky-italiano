# REVIEW — L143 · `unfettered 0 prologue.txt` (due vendite e il segreto dei mondi perduti)

Coppie EN→IT rilette in `translation.json` (`a6fdd67b2067eb90…`). Tutte le 30 unità sono **`PENDING`**.

## 1. Voce

- **Gli Slegati** trattano come una casta che concede onori: «Ti abbiamo fatto conoscere a tutti i nostri fratelli e
  sorelle come una delle poche creature che hanno scelto di aiutare i veri Hai a conquistare la libertà».
- **Il disprezzo** per chi abita i mondi perduti è fisiologico: «una specie di sciacalli, che banchettano sulle rovine di
  civiltà orgogliose… divoratori di carogne». La parola «sciacalli» è già un verdetto.
- **Il giocatore** resta cortese e curioso: «"Potete dirmi a cosa vi servono?"», «"Che cosa farete alla specie che
  possiede quei mondi adesso?"».
- **La narrazione** interviene una volta sola, e basta: «Sospetti che stiano parlando del territorio oggi abitato dai
  Wanderer.»

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `More Jump Drives` | **identico** | 1 |
| `another million credits` | **un altro milione di crediti** | 6, 16 |
| `our frail brothers` | **i nostri fragili fratelli** | 6 |
| `job boards` | **bacheche dei lavori** | 9, 30 |
| `galactic fringe` | **margini della galassia** | 19 |
| `nearly uninhabited` | **quasi disabitati** | 19, 21 |
| `scavengers` · `carrion-feeders` | **sciacalli** · **divoratori di carogne** | 28 |
| `by right` | **di diritto** | 28 |
| `(No.)` · `(Yes.)` | **`(No.)`** · **`(Sì.)`** | 4, 14 · 5, 15 |

## 3. Nodi aperti (da non dedurre dopo)

1. **Due contesti chiusi** (12/12, 18/18): il file resta con la sola `Jump Drive Trading`.
2. **`(No.)` identico e `(Sì.)` tradotto**: due controlli distinti, e il secondo confronta le **due occorrenze
   italiane** fra loro.
3. **`More Jump Drives` ricompare**: verificato nel lotto, non ereditato da L142.
4. **I Wanderer non si traducono** e non si spiegano: il giocatore li conosce, e la narrazione li nomina una volta.
5. **`scavenger` → «sciacallo»**, non «spazzino»: è un giudizio, non un mestiere.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 30 unità restano `PENDING`.
- **Nessuna missione giocata**: le due vendite non sono state viste a schermo.
- **Nessuna revisione umana**.
- **`unfettered 0 prologue.txt` è al 64,6%**: 52 unità da fare, tutte in `Jump Drive Trading`.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 4 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (30 controlli), `verify.py` exit **0** (25 controlli, invariante di segmento) |
