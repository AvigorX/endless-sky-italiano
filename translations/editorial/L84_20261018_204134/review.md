# REVIEW — L84 · `data/successors/predecessors.txt`

## 1. Coerenza (L81–L83)

- **Alte Casate** è forma fissa (L77, L79): qui indicano le Casate dei Myiara, non le istituzioni dei
  Successori, e il contesto lo chiarisce («le Alte Casate dei Myiara»).
- **Valkkyiara-Khorasaqra** conserva la grafia del contesto (L83, unità 4 usava `-ran` come nome): la
  discrepanza è del sorgente e resta dichiarata.
- **`coilgun`** → «cannone a bobina» in prosa, come in L82; `"Sarija" Heirloom Coilgun` resta dato.

## 2. Nodi aperti

- **`martial artistry`**: «arte marziale» è la scelta; «arte della guerra» sarebbe più militare e meno
  estetico. Il testo insiste sull'eleganza (`clean and elegant expression`), e la resa lo segue.
- **`almost never leave the ground`**: letterale. Se il gioco mostrasse queste navi in volo, la frase sarebbe
  un'iperbole del narratore, non un errore.
- **`mirrored armor`**: «corazza specchiata» — non «a specchio», che suggerirebbe un componente.
- **`High Houses`** qui è **dei Myiara**: un lotto futuro che la usasse per i Successori andrebbe distinto.

## 3. Cosa NON è stato fatto

- **Nessuna scrittura su `state.db`**: 4 unità `PENDING`.
- **Nessun caricamento nel gioco**: la scheda della nave e quella del cannone non sono state viste a schermo.
- **Nessuna verifica dei valori**: «più potente di qualunque tecnologia moderna» è testo, non confronto di
  statistiche.

## 4. Rischi residui

- **Lotto di 4 unità**: il più piccolo del progetto. Un errore qui pesa poco sul totale ma molto sulla
  leggibilità della scheda, che è tutta prosa.
- **Il `verify.py` asserisce 48 prima / 7 dopo**: se L85 non partisse dalla 648, diventerebbe rosso.
- **`TypeError` iniziale** del `verify.py` (tupla letta come `Row`): corretto prima di dichiarare il lotto.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì |
| ESEGUITO | sì |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (24 controlli), `verify.py` exit 0 (22 controlli), sha256 `4107161eef110612` |
