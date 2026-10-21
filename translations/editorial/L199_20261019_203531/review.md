# REVIEW — L199 · `hai jobs.txt` (quarto lotto)

Coppie EN→IT rilette in `translation.json` (`6af91de2eec66a88…`). Tutte le 26 unità sono **`PENDING`**.

## 1. Decisioni di resa

1. **`VALUE` identici all'inglese (9/9)**: `<planet> film festival`, `<planet> music festival`,
   `<planet> computer security conference`, `<planet> science fiction convention`, `Superstitious Hai to <planet>`.
   Nota: tre di questi iniziano con un segnaposto — la convenzione li lascia comunque inglesi, perché sono nomi di
   lavoro e il motore sostituisce `<planet>` a runtime.
2. **Unità 1 riusata alla lettera** da L198 unità 49 (stessa stringa inglese): nessuna variante.
3. **`festival del cinema` / `musicale` / `conferenza sulla sicurezza informatica` / `convention di fantascienza`**:
   quattro nomi distinti per quattro eventi distinti, con `convention` tenuto per gli eventi «di settore» come in L198
   e `festival` per quelli popolari.
4. **`grande`** traduce *large* in tutte e quattro le coppie: nessuna variazione sinonimica, perché il confronto del
   `check.py` si basa sulla sua presenza/assenza. Variare (`grande`, `ampio`, `importante`) avrebbe rotto la struttura
   verificabile senza aggiungere nulla.
5. **`appassionati di cinema`** per *movie buffs*, con `Hai` dopo il numero (`<bunks> Hai appassionati di cinema`) per
   tenere la cornice già usata in L196–L198 (`Un gruppo di <bunks> Hai …`).
6. **`ti sono per lo più passate sopra la testa`** per *went mostly over your head*: idioma italiano, non calco.
7. **`una vecchia serie di fantascienza umana`** per *an old human sci-fi program*: «serie» copre il programma TV e
   conserva l'aggettivo `umana` che distingue la produzione terrestre.

## 2. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 26 unità `PENDING`.
- **Nessun lavoro accettato nel gioco**, **nessun testo visto a schermo**, **nessuna revisione umana**.
- **Nessuna correzione al sorgente**: le incoerenze del gioco si conservano.
- **`Superstitious Hai [1]` è aperta**: il `VALUE` è nel lotto, la `DESCRIPTION` e il resto sono in L200.

## 3. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — `parts/part01.json`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (28 controlli), `verify.py` exit **0** (21 controlli) |
