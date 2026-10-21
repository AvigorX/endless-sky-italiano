# REVIEW — L213 · `deep jobs.txt` (secondo lotto)

Coppie EN→IT rilette in `translation.json` (`a1c19c89ae374d9f…`). Tutte le 22 unità sono **`PENDING`**.

## 1. Decisioni di resa

1. **I `DIALOG` non usano il registro Saryd.** Sono missioni umane o generiche: italiano naturale, seconda persona, nessuna
   inversione. È la prima volta che un lotto contiene due registri diversi, e la distinzione è verificata.
2. **`<npc>` resta nudo**: l'articolo e la preposizione articolata stanno **fuori** dal segnaposto («La `<npc>`»,
   «della `<npc>`»), perché il segnaposto è sostituito dal nome della nave e non può portare la morfologia italiana.
3. **`science vessel` → «nave scientifica»**, **`escort` → «scorta»**: lessico fissato e riusabile.
4. **`research lab` → «laboratorio di ricerca»**, **`facility` → «struttura»**: la seconda parola è quella già usata in
   L212 per lo stesso `<stopovers>`, e la coerenza è verificata.
5. **`credentials` → «credenziali»** (unità 10 e 13): in questo contesto sono accrediti d'accesso, non password.
6. **`panelists` → «relatori»**: rende chi parla a una conferenza senza l'ambiguità di «panelisti».
7. **`cutting-edge topics` → «temi all'avanguardia»**: registro alto, coerente con l'unità 11, che parla di scienze e
   discipline umanistiche.
8. **`giddily` → «con entusiasmo»**: l'avverbio inglese è quasi intraducibile in modo compatto; «con entusiasmo» rende la
   sostanza senza il tono infantile che «tutta allegria» aggiungerebbe.
9. **`baggage counter` → «banco bagagli sorvegliato»** e **`security desk` → «banco di sicurezza»**: due alternative dello
   stesso frammento, e devono restare distinguibili.
10. **`built-in secure antigrav trolley` → «carrello antigravità di sicurezza integrato»**: tre aggettivi in inglese, tre
    modificatori in italiano, nello stesso ordine di lettura.
11. **`disquieting sound` → «suono inquietante»**, non «sgradevole»: il pacco deve fare impressione.

## 2. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 22 unità `PENDING`.
- **Nessuna missione giocata**: non ho visto i frammenti comporre a schermo né il `<npc>` essere sostituito dal nome
  della nave. La verifica è testuale.
- **Nessuna revisione umana**, **nessuna correzione al sorgente**.

## 3. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì |
| ESEGUITO | sì |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (25), `verify.py` exit **0** (18) |
