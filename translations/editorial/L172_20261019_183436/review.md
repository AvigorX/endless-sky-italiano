# REVIEW — L172 · `paradise world jobs.txt` (soccorso a Martini)

Coppie EN→IT rilette in `translation.json` (`ef8c776e39355c03…`). Tutte le 12 unità sono **`PENDING`**.

## 1. Voce

Registro **umanitario e amministrativo**: nessuna ironia, nessun personaggio. Sei missioni che dicono cosa portare, dove
e perché, con la stessa chiusura burocratica («Dovrai chiamare via radio il controllore dello spazioporto»). Dopo la
satira dei lotti precedenti, il tono cambia di colpo — ed è il gioco a cambiarlo, non la traduzione.

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `Due to the recent nuclear bombings` | **A causa dei recenti bombardamenti nucleari** | 2-12 |
| `help treat the wounded` | **aiutare a curare i feriti** | 2, 4 |
| `help keep up supply` | **aiutare a mantenere le scorte** | 8, 10, 12 |
| `hail the spaceport controller` | **chiamare via radio il controllore dello spazioporto** | 2-12 |
| `gain clearance to the planet` | **ottenere il permesso di scendere sul pianeta** | 2-12 |

## 3. Nodi aperti (da non dedurre dopo)

1. **`<martini relief occupations>`** compare in L173: altro segnaposto **composto**, da confrontare intero.
2. **`Martini's relief efforts`** (L173) contiene un apostrofo che **sparisce** in italiano: non contare gli apici fra le
   lingue.
3. **La coda comune è una sola stringa**: se in futuro si tocca una delle sei `DESCRIPTION`, il controllo sulla coda
   fallisce — ed è voluto.
4. **`Disaster relief`** resta inglese perché è dentro un `VALUE` (nome della missione).

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 12 unità `PENDING`.
- **Nessuna missione vista a schermo**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Sesto lotto di `paradise world jobs.txt`**.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (25 controlli), `verify.py` exit **0** (20 controlli) |
