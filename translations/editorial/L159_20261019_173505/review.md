# REVIEW — L159 · `weapons.txt` (siluri, Typhoon e razzi pesanti)

Coppie EN→IT rilette in `translation.json` (`9e0b0c5d6a3f6cd3…`). Tutte le 22 unità sono **`PENDING`**.

## 1. Voce

- **`Javelin Turret`, `VALUE` `Torpedoes`, munizione, rack, lanciatore, pod**
- **Typhoon**: `VALUE` `Typhoon Torpedoes`, munizione, tubo, lanciatore, pod.
- **razzi pesanti**: munizione, rack, `Heavy Rocket Launcher`.

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `Torpedoes` · `Typhoon Torpedoes` | **identici** (2 `VALUE`) | 3, 11 |
| `torpedoes` (prosa) | **siluri** | 4, 6, 8, 9 |
| `capital ships` | **navi capitali** | 6, 14 |
| `proximity trigger` | **detonatore di prossimità** | 21 |
| `blast radius` | **raggio d'esplosione** | 21 |
| `Heavy Rockets are…` | **I Heavy Rocket sono…** | 19, 21 |

## 3. Nodi aperti (da non dedurre dopo)

1. **Sei copie** della riga munizioni nello stesso lotto, più il riuso da L157/L158: un solo controllo per tutte e tre le cose.
2. **idx 8 è un prefisso di idx 6**, non una stringa uguale: si verifica come sotto-stringa (`startswith`), mai come uguaglianza.
3. **Errore in corsa**: avevo asserito 15 testi inglesi distinti; il dato dice **16** (22 − 6 copie + 1 − 1 duplicato). Corretto a 16 in `check.py` e `verify.py` dopo averlo misurato.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 22 unità `PENDING`.
- **Nessuna missione giocata**, **nessuna arma vista a schermo**.
- **Nessuna revisione umana**.
- **Lotto del batch L154–L160**.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (25 controlli), `verify.py` exit **0** (20 controlli) |
