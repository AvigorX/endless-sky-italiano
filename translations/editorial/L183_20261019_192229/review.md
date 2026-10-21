# REVIEW — L183 · `human outfits.txt` (quattro `VALUE`, armi, il Mug)

Coppie EN→IT rilette in `translation.json` (`c98a702886a3b041…`). Tutte le 15 unità sono **`PENDING`**.

## 1. Voce

Il lotto più **disomogeneo** del file: schede da emporio (idx 2–5, 7–8, 10), **una battuta secca** (idx 11, il `Mug`) e
**un pezzo di ambientazione** (idx 15, la spada con le iscrizioni non umane). La traduzione non livella: la battuta resta
di otto parole, la spada resta un mistero.

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `fresh water tanks` | **serbatoi d'acqua dolce** | 2 |
| `hospitality staff` | **personale di accoglienza** | 2 |
| `will fail to detect it` | **non riesca a rilevarli** | 4 |
| `for defense against pirates` | **per difendersi dai pirati** | 5 |
| `flushing out defenders` | **stanare i difensori** | 7 |
| `take over your ship` | **impadronirsi della nave** | 8 |
| `severe fine` | **multato severamente** | 10 |
| `drinking vessel` | **recipiente da bevuta** | 14 |
| `rendered useless` | **resi inutili** | 15 |

## 3. Nodi aperti (da non dedurre dopo)

1. **`Antigrav Glasses` è plurale**: il nome non si «armonizza» col contesto singolare.
2. **`...` resta `...`**: tre punti ASCII, non l'ellissi tipografica. Il resto della campagna non usa `…`.
3. **`Nerve Gas` in prosa è «gas nervino»**: il nome resta nel `VALUE`, la sostanza si traduce.
4. **La battuta non si spiega**: se in futuro idx 11 verrà «migliorato» in una frase compiuta, la voce sparisce.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 15 unità `PENDING`.
- **Nessun equipaggiamento visto a schermo**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Quarto lotto del file**: restano 13 unità, da chiudere in L184.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (27 controlli), `verify.py` exit **0** (20 controlli) |
