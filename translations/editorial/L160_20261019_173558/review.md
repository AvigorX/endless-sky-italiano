# REVIEW — L160 · `weapons.txt` (Heavy Rocket Pod, il Nuclear Missile e la Gatling (chiude il file))

Coppie EN→IT rilette in `translation.json` (`b2663bd3f42fddc7…`). Tutte le 13 unità sono **`PENDING`**.

## 1. Voce

- **pod: descrizione, nota sui pod, munizioni**
- **missile nucleare**: la descrizione e la nota fra parentesi quadre.
- **Gatling**: `VALUE` delle munizioni, cartuccia, `VALUE` delle scatole, scatole, `Gatling Gun`, `Gatling Turret`.

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `Gatling Gun Ammo` · `Bullet Boxes` | **identici** (2 `VALUE`) | 6, 8 |
| `one-shot weapon` | **arma a colpo singolo** | 5 |
| `depleted nuclear fuel` | **combustibile nucleare esaurito** | 7 |
| `muzzle velocity` | **velocità alla bocca** | 7 |
| `19th century` | **XIX secolo** | 10 |
| `spin in his grave` | **rotolare nella tomba** | 12 |
| `tear apart the hulls` | **squarciare gli scafi** | 12 |

## 3. Nodi aperti (da non dedurre dopo)

1. **L'ellissi `...` di idx 4 resta tre punti ASCII** (mai `…`) e il **trattino ` - `** di idx 10 resta un trattino semplice (mai em/en dash): due controlli distinti, perché la tipografia li tratta diversamente.
2. **La nota fra parentesi quadre** di idx 5 conserva le quadre: è un testo tecnico per il giocatore, non una frase di narrazione.
3. **Il lotto chiude il file**: l'invariante è di **file**, 6 finestre = 90 righe distinte, `min(line) = 36`, `max(line) = 1844`, zero unità dopo.
4. **Riuso verificato**: idx 1 è la stessa stringa di L159 (idx 21) e la riga munizioni è quella di L157/L158/L159; entrambi i controlli leggono la resa **già scritta**.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 13 unità `PENDING`.
- **Nessuna missione giocata**, **nessuna arma vista a schermo**.
- **Nessuna revisione umana**.
- **Lotto del batch L154–L160**.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (27 controlli), `verify.py` exit **0** (23 controlli) |
