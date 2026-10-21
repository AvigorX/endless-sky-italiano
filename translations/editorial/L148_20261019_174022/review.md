# REVIEW — L148 · `coalition jobs.txt` (gli interpreti e il primo `DIALOG`)

Coppie EN→IT rilette in `translation.json` (`6f4f67af7faeeb38…`). Tutte le 16 unità sono **`PENDING`**.

## 1. Voce

Il file resta **burocratico**, ma il `DIALOG` introduce la prima frase narrativa:

- «Gli agenti Heliarch vengono incontro alla tua nave appena attracca e ricevono il candidato che hai trasportato, con
  una piccola cerimonia. Pochi minuti dopo ricevi un bonifico di `<payment>`.»
- Le `DESCRIPTION` restano avvisi: «Porta questi `<bunks>` agenti Heliarch, addestrati come interpreti e mediatori, a
  `<destination>`. Il compenso è di `<payment>`.»
- I `TEXT` sono la scena minima del rilascio: «Scarichi i peacekeeper su `<planet>`. Pochi minuti dopo ricevi un
  bonifico di `<payment>`.»

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `Interpreters to <planet>` | **identico**, senza «the» | 3, 5, 7 |
| `Peacekeepers to <planet>` | **identico** | 10, 12 |
| `Saryds to <planet>` | **identico** | 15 |
| `to <destination>` | **a `<destination>`** | 4, 6, 8, 11… |
| `on <planet>` | **su `<planet>`** | 2, 9, 14 |
| `peacekeepers` | **peacekeeper** (prestito) | 9, 11, 13 |
| `Interspecies Exchange Program` | **Programma di Scambio tra Specie** | 16 |
| `Lunarium activity` | **attività dei Lunarium** | 11, 13 |

## 3. Nodi aperti (da non dedurre dopo)

1. **`<destination>` ≠ `<planet>`**: il primo è la destinazione dichiarata della missione, il secondo il mondo dove si
   scarica. Il controllo verifica anche l'**assenza incrociata** nelle due unità di riferimento.
2. **`Interpreters to <planet>` non ha «the»**: chi lo aggiunge cambia il `VALUE`. Il `check.py` rifiuta `the <planet>`.
3. **`peacekeeper` resta in inglese** per coerenza col `VALUE` `Peacekeepers to <planet>`.
4. **Il `DIALOG` è tradotto come narrazione**: presente indicativo, «appena attracca», non «quando la nave attraccherà».
5. **`Lunarium`, `Heliarch`, `Saryd` restano**: nomi propri già presenti in staging in questa forma.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 16 unità restano `PENDING`.
- **Nessuna missione accettata**: la cerimonia del candidato non è stata giocata.
- **Nessuna revisione umana**.
- **`coalition jobs.txt` è al 23,4%**: 151 unità da fare.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (27 controlli), `verify.py` exit **0** (25 controlli) |
