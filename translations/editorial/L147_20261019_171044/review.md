# REVIEW — L147 · `coalition jobs.txt` (i lavori dell'Anello)

Coppie EN→IT rilette in `translation.json` (`86d0e8e3b5fccb2f…`). Tutte le 30 unità sono **`PENDING`**.

## 1. Voce

Il file è **burocratico**: descrizioni di lavoro scritte come avvisi, senza dialoghi. La resa deve restare
amministrativa, non narrativa.

- «Trasporta questo equipaggio di `<bunks>` operai sul `<planet>` degli Heliarch, dove aiuteranno negli sforzi per
  mantenere ed espandere il mondo ad anello. Il compenso sarà di `<payment>`.»
- «Il governo ti pagherà `<payment>` per portare questi `<bunks>` lavoratori volontari sul `<planet>`, dove daranno una
  mano nella costruzione in cambio di vitto e alloggio.»
- «Questa partita di `<tons>` di forniture è una donazione del governo di `<origin>` per sostenere il `<planet>` degli
  Heliarch.»

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `Workers to the <planet>` | **identico** (VALUE) | 2, 4, 6 |
| `the Heliarch <planet>` | **il `<planet>` degli Heliarch** | 3, 5, 7, 17… |
| `ringworld` | **mondo ad anello** | 3, 5, 7 |
| `room and board` | **vitto e alloggio** | 10, 12, 14 |
| `by <date>` | **entro il `<date>`** | 17, 19, 21 |
| `receive a transfer of <payment>` | **ricevi un bonifico di `<payment>`** | 1, 8 |
| `in payment` | **come compenso** | 15, 22 |
| `candidate for elevation` | **candidato all'elevazione** | 30 |

## 3. Nodi aperti (da non dedurre dopo)

1. **Il token passa prima del nome di fazione**: «il `<planet>` degli Heliarch», non «gli Heliarch `<planet>`». L'inglese
   mette `<planet>` dopo l'apposizione; l'italiano vuole il mondo come testa del sintagma.
2. **I `VALUE` sono inglesi per contratto**: il controllo che vieta i residui inglesi **esclude** le 13 unità `VALUE`,
   altrimenti si auto-contraddirebbe. La separazione è esplicita nel codice (`if v['kind'] != 'VALUE'`).
3. **Nessun tab, nessuna virgoletta**: primo lotto del progetto con zero in entrambi. Le asserzioni vuote sono scritte.
4. **Un'asserzione fittizia è stata tolta**: avevo aggiunto un `ck('29 unità senza spazio finale…', True)` che non
   verificava nulla. È stato rimosso invece di lasciarlo verde.
5. **`<destination>` arriva nel prossimo lotto** (interpreti): qui non c'è, e il `check.py` lo esclude per costruzione
   confrontando il multiset esatto.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 30 unità restano `PENDING`.
- **Nessun lavoro accettato nel gioco**: i tre livelli non sono stati giocati.
- **Nessuna revisione umana**.
- **`coalition jobs.txt` è al 15,2%**: 167 unità da fare.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (28 controlli), `verify.py` exit **0** (27 controlli) |
