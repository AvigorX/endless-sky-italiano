# REVIEW — L171 · `paradise world jobs.txt` (dodici evacuazioni da Martini)

Coppie EN→IT rilette in `translation.json` (`d494b88bbb2ea449…`). Tutte le 24 unità sono **`PENDING`**.

## 1. Voce

Il lotto è **uniforme per costruzione**: dodici missioni generate dallo stesso stampo, con la stessa formula e lo
stesso finale («dove ti pagheranno»). La ripetizione è del gioco, non della traduzione: la resa mantiene **una sola
formula** e varia solo dove varia l'inglese (lusso, singolare/plurale, «case» vs «casa»).

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `destroyed in the nuclear bombing` | **distrutta nel bombardamento nucleare** | 2, 4, 6, 8 |
| `where they have accommodation` | **dove hanno un alloggio** | 2, 4, 6, 8 |
| `when the nuclear bombings occurred` | **quando sono avvenuti i bombardamenti nucleari** | 10-16 |
| `back to their homes` | **alle loro case** | 16, 18 |
| `back to their home` | **a casa loro** | 22, 24 |
| `in Martini's capital city` | **nella capitale di Martini** | 24 |

## 3. Nodi aperti (da non dedurre dopo)

1. **Gli apici non si contano fra le lingue**: qui sono **1 in inglese e 2 in italiano**. Chi rifà questo controllo
   partendo dal presupposto «stesso numero» sbaglia due volte su due (L169 e L171).
2. **`Martini's` non diventa un possessivo italiano**: «la capitale di Martini», senza apostrofo.
3. **`residents` (plurale) e `resident` (singolare)** sono due `VALUE` distinti che si ripetono in due contesti ciascuno:
   non vanno fusi in una forma sola.
4. **Il salto 988–1229 è reale**, non un buco di esportazione: è verificato sul database.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 24 unità `PENDING`.
- **Nessuna missione vista a schermo**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Quinto lotto di `paradise world jobs.txt`**.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (27 controlli), `verify.py` exit **0** (22 controlli) |
