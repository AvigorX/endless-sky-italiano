# REVIEW — L165 · `avgi outfits.txt` (torcia Arc e propulsori RCS)

Coppie EN→IT rilette in `translation.json` (`6081a66116d706e9…`). Tutte le 13 unità sono **`PENDING`**.

## 1. Voce

La voce Avgi qui descrive **il funzionamento**: la torcia più grande e più vecchia «depotenziata» per l'uso
interplanetario, i due componenti che si inseriscono nell'ugello, i propulsori RCS che usano il calore di scarto per
manovrare. Il registro è tecnico, con un tocco di concretezza («in stile 'teiera'»).

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `Z-999 "Arc" Fusion Torches` | **identico** (`VALUE`, virgolette comprese) | 1 |
| `trading specific impulse for raw thrust` | **barattando l'impulso specifico con la spinta pura** | 2 |
| `catalyzed D-D fusion` | **fusione D-D catalizzata** | 2 |
| `a magnetic nozzle slot` | **uno slot per ugello magnetico** | 5, 7 |
| `exhaust plume` | **pennacchio di scarico** | 6 |
| `reaction control thrusters` | **propulsori per il controllo d'assetto** | 9, 11, 13 |
| `'teakettle' style` | **in stile 'teiera'** | 13 |

## 3. Nodi aperti (da non dedurre dopo)

1. **La nota sull'ugello magnetica è condivisa con L164**: index 3 qui e 6/9 là sono la stessa stringa, e il controllo
   confronta le rese fra lotti.
2. **I tab sono solo su idx 3 e 5**: un tab aggiunto a mano fa fallire il lotto (è successo, ed è stato corretto).
3. **4 `VALUE` e 2 virgolette**: i nomi restano inglesi, virgolette comprese.
4. **Restano 6 unità**: L166 chiude il file con l'invariante di file (63/63).

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 13 unità `PENDING`.
- **Nessuna nave vista a schermo**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Penultimo lotto di `avgi outfits.txt`**.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (22 controlli), `verify.py` exit **0** (19 controlli) |
