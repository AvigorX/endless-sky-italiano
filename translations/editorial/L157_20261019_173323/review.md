# REVIEW — L157 · `weapons.txt` (plasma, lanciafiamme e la famiglia Meteor)

Coppie EN→IT rilette in `translation.json` (`44b8d641c08a7203…`). Tutte le 16 unità sono **`PENDING`**.

## 1. Voce

- **`Particle Cannon`, `Proton Gun`, `Proton Turret`, `Plasma Cannon`, `Plasma Turret`, `Plasma Repeater` (2 unità)**
- **lanciafiamme**: `Flamethrower`.
- **famiglia Meteor**: munizione, `VALUE` della cassa, cassa, lanciatore (2 unità), pod (3 unità).

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `Syndicate` | **Sindacato** | 2, 3 |
| `Southern Rim` | **Bordo Meridionale** | 6 |
| `outfitter` | **emporio** | 6, 13, 16 |
| `reverse engineer` | **ricostruire a ritroso** | 2 |
| `repeater` | **repeater**, invariato | 6 |
| `trades off its larger bursts for a much faster rate of fire` | **sacrifica le raffiche più ampie in cambio di una cadenza di fuoco molto più rapida** | 7 |

## 3. Nodi aperti (da non dedurre dopo)

1. **Due coppie identiche** in inglese (12/14 e 13/16): la resa deve restare identica, e un controllo lo verifica.
2. **Un solo `VALUE`** (`Meteor Missile Boxes`) riprodotto alla lettera; **4 unità con tab**.
3. **`outfitter` → «emporio»**: verificato sui lotti precedenti (L113), non inventato qui.
4. **Errore in corsa**: il tema del glossario era `munzion-`; in italiano è «muni**z**ione», quindi `munizion-`.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 16 unità `PENDING`.
- **Nessuna missione giocata**, **nessuna arma vista a schermo**.
- **Nessuna revisione umana**.
- **Lotto del batch L154–L160**.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (24 controlli), `verify.py` exit **0** (19 controlli) |
