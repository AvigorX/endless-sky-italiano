# REVIEW — L150 · `coalition jobs.txt` (turisti e corriere veloce)

Coppie EN→IT rilette in `translation.json` (`160a1592a36efff5…`). Tutte le 14 unità sono **`PENDING`**.

## 1. Voce

Avvisi amministrativi, con una sola frase di cortesia:

- «Questi `<bunks>` turisti ti pagheranno `<payment>` per portarli a `<destination>` e desiderano viaggiare su una nave
  molto confortevole. Il compenso decade se non arrivano entro il `<date>`.»
- «I turisti ti ringraziano per averli riportati a casa e ti pagano `<payment>`.»
- «Il destinatario ti ringrazia per aver portato il `<commodity>` qui così in fretta e ti paga `<payment>`.»

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `Vacationers to <planet>` | **identico** | 1, 3, 5, 8, 10, 12 |
| `bring them to` vs `bring them home to` | **portarli a** vs **riportarli a casa a** | 2–6 vs 9–13 |
| `travel in a very comfortable ship` | **viaggiare su una nave molto confortevole** | tutte le `DESCRIPTION` |
| `Payment is void` | **Il compenso decade** | tutte le `DESCRIPTION` |
| `the recipient thanks you` | **il destinatario ti ringrazia** | 14 |

## 3. Nodi aperti (da non dedurre dopo)

1. **Le due famiglie hanno rese diverse** e un controllo lo pretende: se qualcuno «uniformasse» i due testi, il
   `verify.py` sarebbe rosso.
2. **`<commodity>` va isolato**: una sola occorrenza su 33 token, altrimenti invisibile nei totali.
3. **`Payment is void`** non è «il pagamento è nullo»: «il compenso decade» dice la stessa cosa in italiano corrente.
4. **Nessun nome proprio** in questo lotto: né specie né mondi, solo segnaposto.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 14 unità `PENDING`.
- **Nessun trasporto effettuato nel gioco**.
- **Nessuna revisione umana**.
- **Eseguito in batch** con L151 e L152: il contratto è il piano del batch.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (27 controlli), `verify.py` exit **0** (24 controlli) |
