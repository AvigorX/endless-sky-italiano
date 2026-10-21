# REVIEW — L139 · `data/starts.txt` (due nomi di equipaggiamento)

Coppie EN→IT rilette in `translation.json` (`1ceb216ebf1e03c6…`). Entrambe le unità sono **`PENDING`**.

## 1. Cosa contiene

Nessuna prosa. Due **nomi di equipaggiamento** del Grasshopper, scritti fra virgolette perché il formato del gioco li
marca così:

| riga | testo | resa |
|---|---|---|
| 365 | `"Benga" Atomic Thruster` | **identico** |
| 366 | `"Biroo" Atomic Steering` | **identico** |

## 2. Decisioni di resa (verificate sul file)

| nodo | decisione | motivo |
|---|---|---|
| `Benga` · `Biroo` | **invariati** | produttori |
| `Atomic Thruster` · `Atomic Steering` | **invariati** | nomi di modello |
| virgolette | **conservate** | struttura del nome, non dialogo |
| tab e backtick | **assenti dal testo** | stanno nel `raw`, fuori dal campo `english` |

## 3. Nodi aperti (da non dedurre dopo)

1. **Un nome identico non è un'omissione**: sta in `ID_OK` con un controllo proprio. Se un revisore lo traducesse, il
   riferimento al bene di gioco si romperebbe e il controllo lo segnalerebbe.
2. **Le virgolette non si «ripuliscono»**: sono parte del nome.
3. **Il lotto è di 2 unità**: i numeri attesi si misurano, non si copiano dal lotto precedente.
4. **`starts.txt` è chiuso**: i lotti futuri non devono rivendicarne righe, e il `verify.py` di L139 lo verifica su
   tutti i `translation.json` dello staging.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 2 unità restano `PENDING`.
- **Nessuna nave acquistata nel gioco**: i nomi dei propulsori non sono stati visti a schermo.
- **Nessuna revisione umana**.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 1 parte, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (21 controlli), `verify.py` exit **0** (22 controlli, invariante di file) |
