# REVIEW — L181 · `human outfits.txt` (disturbatori, ramscoop, iperguida)

Coppie EN→IT rilette in `translation.json` (`4a13b745b4c7e37b…`). Tutte le 9 unità sono **`PENDING`**.

## 1. Voce

Il file cambia registro tre volte in nove unità: **scheda tecnica** (disturbatori), **racconto storico** (i ramscoop:
«nei primi giorni dell'esplorazione spaziale…»), **letteratura** (l'iperguida: la scatola che pensa i propri
imperscrutabili pensieri, la vespa e la foglia di quercia), e infine **mistero amministrativo** (il `Jump Drive` che non
si può ricostruire). La traduzione tiene le tre voci distinte.

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `interfere with Sidewinders` | **interferire con i Sidewinders** | 1 |
| `lose their target locks` | **perdere l'aggancio del bersaglio** | 1 |
| `track you optically` | **seguono otticamente** | 2 |
| `additional ramscoops ... not as effective as the first` | **non sono efficienti quanto il primo** | 3 |
| `measure of safety` | **misura di sicurezza** | 4 |
| `a much-improved ramscoop` | **un ramscoop molto migliorato** | 5 |
| `rides the resulting ripple` | **cavalca l'increspatura che ne risulta** | 6 |
| `inner workings` | **funzionamento interno** | 7 |
| `at the expense of using more fuel` | **al prezzo di consumare più carburante** | 8 |
| `a total mystery` | **un mistero totale** | 9 |

## 3. Nodi aperti (da non dedurre dopo)

1. **`hyperdrive` → iperguida** è l'unica traduzione di un nome di equipaggiamento in questo lotto; `scram drive` e
   `jump drive` restano inglesi perché sono **nomi di prodotto**.
2. **`Free Worlds` e `Deep` sono nomi propri**: non si traducono, come le fazioni dei lotti precedenti.
3. **La vespa resta una vespa**: se in futuro qualcuno «semplificherà» idx 6, la voce del file sparisce.
4. **`reverse engineer`** → «ricostruire a ritroso» (non «decodificare»): il senso è la ricostruzione del manufatto.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 9 unità `PENDING`.
- **Nessun equipaggiamento visto a schermo**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Secondo lotto del file**: 42 unità ancora da fare.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (25 controlli), `verify.py` exit **0** (19 controlli) |
