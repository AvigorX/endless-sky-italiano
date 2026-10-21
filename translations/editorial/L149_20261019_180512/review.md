# REVIEW — L149 · `coalition jobs.txt` (scambi interspecie e trasferimenti)

Coppie EN→IT rilette in `translation.json` (`b5f2ed112da6516f…`). Tutte le 18 unità sono **`PENDING`**.

## 1. Voce

Testo amministrativo, con una sola frase «umana» alla fine:

- «Nell'ambito del Programma di Scambio tra Specie, questi `<bunks>` coloni volontari hanno bisogno di essere
  trasportati a `<destination>`. Il governo pagherà la loro tariffa di trasporto di `<payment>`.»
- «Nell'ambito del Programma di Piena Occupazione, questi `<bunks>` lavoratori hanno bisogno di essere trasportati a
  `<destination>`. Il governo pagherà la loro tariffa di trasporto di `<payment>`.»
- «I turisti ti ringraziano per averli portati su `<planet>` e ti pagano `<payment>`.»

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `Saryds to <planet>` · `Kimek to <planet>` · `Arachi to <planet>` | **identici** | 1, 3, 5, 7, 9 |
| `Transfer to <planet>` | **identico** | 12, 14, 16 |
| `As part of the Interspecies Exchange Program…` | **riletta da L148**, uguale | 2, 4, 6, 8, 10 |
| `As a part of the Full Employment Program…` | **Programma di Piena Occupazione** | 13, 15, 17 |
| `on <planet>` (senza «the») | **su `<planet>`** | 11 |
| `bringing them to <planet>` | **averli portati su `<planet>`** | 18 |

## 3. Nodi aperti (da non dedurre dopo)

1. **Le due coppie 10/10 e 8/8** rendono il multiset cieco: il `verify.py` verifica l'**ordine per unità**, e il
   `check.py` lo dice esplicitamente («il multiset da solo è cieco»).
2. **«Quasi la stessa frase» non è la stessa frase**: `on <planet>` di L149 contro `on the <planet>` di L147. La resa
   cambia di una preposizione articolata, e il costruttore **rifiuta** il riuso.
3. **Le cinque `DESCRIPTION` dei coloni sono una sola stringa**: resa unica e confronto con L148, non cinque rese libere.
4. **`Arachi` resta**: è il plurale usato dal gioco, non «Arach».
5. **Nessun tab, nessuna virgoletta**: terzo lotto consecutivo, asserzioni vuote scritte.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 18 unità restano `PENDING`.
- **Nessuna missione accettata**: i turisti non sono stati portati da nessuna parte.
- **Nessuna revisione umana**.
- **`coalition jobs.txt` è al 32,5%**: 133 unità da fare.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (31 controlli), `verify.py` exit **0** (25 controlli) |
