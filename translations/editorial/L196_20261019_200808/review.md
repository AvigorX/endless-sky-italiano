# REVIEW — L196 · `hai jobs.txt` (apre il file)

Coppie EN→IT rilette in `translation.json` (`e69389281fc1e23f…`). Tutte le 39 unità sono **`PENDING`**.

## 1. Decisioni di resa

1. **`VALUE` identici all'inglese (17/17)**. Sono nomi di lavoro mostrati nella bacheca: `Human vacationer to <planet>`, `Festival at <planet>`, `Special Delivery to <planet>`. Non si traducono — precedente misurato: 300+ `VALUE` identici da L117 a L195.
2. **`TEXT` tradotti (6/6)**. Sono tre battute di dialogo (`phrase:…`): il pagamento del festival, la consegna degli aiuti e le due frasi degli scaricatori. Il precedente è L108…L152.
3. **`Hai` e `Unfettered` restano invariati**: fazione e popolo secondo glossario e uso dei lotti precedenti («gli Unfettered», «gli Hai»).
4. **`tributo` fra virgolette**: `(o come preferiscono chiamarli, "tributo")` conserva le due virgolette dritte, come l'inglese, dentro il delimitatore backtick.
5. **`consanguinei` vs `fratelli e sorelle`**: `kinfolk` e `brothers and sisters` sono due espressioni distinte e restano distinte; appiattirle su «fratelli» cancellerebbe la differenza del testo.
6. **`all'anno`** (unità 19, 21, 23): l'elisione italiana introduce **3 apici** dove l'inglese ne ha **1** (`didn't`). L'apice non è un dato da conservare: è un fatto della lingua di arrivo, e il controllo lo lega alla causa.
7. **`strano mondo Hai`**: l'aggettivo resta in tutte e tre le occorrenze (6, 8, 10, 12) — è la voce del listino Hai, non una ripetizione da variare.

## 2. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 39 unità `PENDING`.
- **Nessun lavoro accettato nel gioco**, **nessun testo visto a schermo**, **nessuna revisione umana**.
- **Nessuna correzione al sorgente**: le incoerenze del gioco si conservano.

## 3. Cosa il documento d'ingresso sbagliava

- `Token` dichiarato **0**, misurati **72** segnaposto su 32 unità: riga corretta nel documento d'ingresso prima di aprire il lotto.
- Regola «`VALUE` e `TEXT` restano inglesi»: vera per i `VALUE`, **falsa per i `TEXT` in prosa**. Il lotto segue i dati (6/6 `TEXT` tradotti) e lo dichiara qui.

## 4. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (26 controlli), `verify.py` exit **0** (19 controlli) |
