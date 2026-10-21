# REVIEW — L191 · `bunrodea missions.txt`

Coppie EN→IT rilette in `translation.json` (`a1c782a568e872ed…`). Tutte le 12 unità sono **`PENDING`**.

## 1. Difficoltà e decisioni

1. **1 segnaposto `<origin>`** da conservare alla lettera (idx 3), in inglese e in italiano.
2. **6 virgolette di dialogo** (idx 5, 6, 7) e **9 tab**: le virgolette sono diritte, mai caporali.
3. **Le due varianti 11 e 12** condividono la seconda metà (mappa, sistema evidenziato, partenza) e la resa deve coincidere: il controllo confronta le due stringhe.
4. Un'asserzione sbagliata (mia): il controllo pretendeva `(Schivi` mentre l'imperativo corretto è **Schiva**.

## 2. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 12 unità `PENDING`.
- **Nessuna missione giocata**, **nessun testo visto a schermo**, **nessuna revisione umana**.

## 3. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (25 controlli), `verify.py` exit **0** (21 controlli) |
