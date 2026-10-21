# REVIEW — L158 · `weapons.txt` (Sidewinder e Javelin: munizioni, pod e lanciatori)

Coppie EN→IT rilette in `translation.json` (`7abe6d61b8ca79fa…`). Tutte le 18 unità sono **`PENDING`**.

## 1. Voce

- **munizione, rack, lanciatore (3 unità), pod (4 unità)**
- **Javelin**: munizione, cassa, pod (3 unità), mini pod (4 unità).

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `protective casings` | **involucri protettivi** | 4, 7 |
| `saturating … anti-missile defenses` | **saturare le difese antimissile** | 13, 16 |
| `sneak through` | **riescano a passare** | 13, 16 |
| `Storage Rack` / `Storage Crate` / `Storage Tube` | **invariati** (nomi di oggetto) | 2, 11, 13 |
| `Ammunition for this weapon can be restocked at any outfitter.` | **Le munizioni per quest'arma possono essere rifornite presso qualsiasi emporio.** | 5, 9, 14, 18 |

## 3. Nodi aperti (da non dedurre dopo)

1. **10 unità con tab** su 18, il lotto più «tabbato» del file.
2. **Quattro testi ripetuti** (3/6, 4/7, 5/9/14/18, 12/15, 13/16): un controllo pretende l'identità della resa, non solo la correttezza dei singoli.
3. **Riuso verificato contro L157**: due stringhe (la riga munizioni e quella sui pod) sono le stesse del lotto precedente, e il controllo le confronta con la resa **già scritta**, non con una nuova.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 18 unità `PENDING`.
- **Nessuna missione giocata**, **nessuna arma vista a schermo**.
- **Nessuna revisione umana**.
- **Lotto del batch L154–L160**.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (23 controlli), `verify.py` exit **0** (18 controlli) |
