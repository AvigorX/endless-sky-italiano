# REVIEW — L154 · `coalition jobs.txt` (i lavori Heliarch e le nove consegne del Lunarium (chiude il file))

Coppie EN→IT rilette in `translation.json` (`38054e95406a979e…`). Tutte le 41 unità sono **`PENDING`**.

## 1. Voce

- **`Transport Prisoners`, la scorta, il pagamento**
- **indagine**: `Investigate signs of criminal activity`, gli agenti, le prove.
- **evacuazione riuscita**: `Rescue Lunarium Members`, l'imbarco, il ringraziamento.
- **evacuazione fallita**: stesso lavoro, gli Heliarch arrivati prima.
- **nove consegne Lunarium**: reattori, lanciatori, torrette, granate: nove `VALUE` + nove `DESCRIPTION` + nove `DIALOG`.

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `Transport Prisoners` · `Investigate…` · `Rescue Lunarium Members` · `X Delivery` | **identici** (13 `VALUE`) | 1, 4, 8, 12, 15…39 |
| `Payment is <payment>.` | **Il compenso è di `<payment>`.** | 2 |
| `Pick up <bunks> … by <date>.` | **Preleva `<bunks>` … entro il `<date>`.** | 9, 13 |
| `The Lunarium is offering <payment> for you to deliver …` | **Il Lunarium offre `<payment>` per consegnare …** | 16, 19, 22, 25, 28, 31, 34, 37, 40 |
| `as instructed` | **come richiesto** | 17…41 |
| `quietly transporting the reactor / the turret / the grenades / the cargo away` | **portare via il reattore / la torretta / le granate / il carico in silenzio** | 17, 20, 23, 26, 29, 32, 35, 38, 41 |

## 3. Nodi aperti (da non dedurre dopo)

1. **Zero tab e zero virgolette** nel lotto: due asserzioni vuote scritte (`== []`, `== 0`), non omesse.
2. **`<destination>` ≠ `<planet>`**: i 9 `DIALOG` di consegna hanno solo `<planet>`, le 8 `DESCRIPTION` solo `<destination>`; il controllo verifica l'**assenza incrociata**, non solo i totali.
3. **Le due `Rescue Lunarium Members`** sono lo stesso `VALUE` con descrizioni diverse per un articolo («Pick up the» / «Pick up»): la resa distingue «Preleva» da «Preleva i» e il controllo pretende che siano **diverse**.
4. **Nove famiglie regolari**: il controllo esige che tutte e nove condividano le tre giunture fisse e che ciascuna nomini il proprio oggetto e la propria coda.
5. **Errore in corsa (due volte)**: un controllo cercava `completo di` nell'inglese (che dice `complete with`) e le 7 descrizioni semplici erano confuse con le 2 con complemento. Corretto il controllo, non la resa.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 41 unità `PENDING`.
- **Nessuna missione giocata**, **nessuna arma vista a schermo**.
- **Nessuna revisione umana**.
- **Lotto del batch L154–L160**.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (29 controlli), `verify.py` exit **0** (28 controlli) |
