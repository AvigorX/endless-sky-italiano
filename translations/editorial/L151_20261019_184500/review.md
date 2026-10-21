# REVIEW — L151 · `coalition jobs.txt` (corriere, carichi, medici, allievi)

Coppie EN→IT rilette in `translation.json` (`8faf5d133a5b433c…`). Tutte le 37 unità sono **`PENDING`**.

## 1. Voce

Frasi amministrative, quasi telegrafiche, più un `DIALOG` narrativo:

- «Consegna `<cargo>` a `<destination>` entro il `<date>`. Il compenso è `<payment>`.»
- «`<destination>` ha bisogno di una partita di `<cargo>` entro il `<date>`. Il compenso sarà `<payment>`.»
- «I medici ripongono metodicamente la loro attrezzatura e lasciano la nave. Dalla loro mancanza di fretta sembra che si
  tratti di un evento di routine, non di una crisi. Pochi minuti dopo ricevi un bonifico di `<payment>`.»

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `Deliver <cargo> to <destination>. Payment is <payment>.` | **Consegna … Il compenso è …** | **8 copie**, una resa |
| `by <date>` | **entro il `<date>`** | 3 + 3 copie |
| `needs a shipment of <cargo>` | **ha bisogno di una partita di `<cargo>`** | 3 copie |
| `a viral outbreak` | **un'epidemia virale** | 31 |
| `lack of urgency` | **mancanza di fretta** | 32 |
| `cadets` · `recruits` | **allievi** · **reclute** | 34, 37 |

## 3. Nodi aperti (da non dedurre dopo)

1. **Le 8 copie devono restare una resa**: se una divergesse, il gioco mostrerebbe due testi per lo stesso lavoro.
2. **`<cargo>` ≠ `<commodity>`**: carico della missione contro merce del `TEXT`.
3. **«corriere» non esiste nel testo tradotto**: vive solo nel `VALUE` inglese. Il controllo lo verifica **in negativo**.
4. **`DIALOG`**: tono osservativo («metodicamente», «di routine, non di una crisi»), non burocratico.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 37 unità `PENDING`.
- **Nessun lavoro completato nel gioco**.
- **Nessuna revisione umana**.
- **Eseguito in batch** con L150 e L152: contratto = piano del batch, nessun handoff separato.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (27 controlli), `verify.py` exit **0** (24 controlli) |
