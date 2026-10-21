# REVIEW — L180 · `human outfits.txt` (raffreddamento e scudi)

Coppie EN→IT rilette in `translation.json` (`263300dbfc862221…`). Tutte le 12 unità sono **`PENDING`**.

## 1. Voce

**Scheda tecnica con una punta di ironia**: «a volte si arriva al punto in cui la nave si surriscalda a intermittenza»,
«potresti fare meglio a installare componenti più efficienti». Il resto è **scala di prodotto**: ogni pezzo è descritto
per ciò che fa e per ciò che costa. Il traduttore non deve vendere né sminuire.

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `high-powered outfits` | **equipaggiamenti potenti** | 2 |
| `circulates water` | **fa circolare acqua** | 3 |
| `anything but the heaviest of armaments` | **qualsiasi armamento, tranne i più pesanti** | 4 |
| `space this cooling system takes up` | **lo spazio che occupa questo sistema** | 5 |
| `non-combat starships` | **astronavi non da combattimento** | 6 |
| `edge` (in combat) | **vantaggio** | 7 |
| `shield capacity` | **capacità di scudo** | 8 |
| `sacrifice engine power or weaponry` | **sacrificare potenza del motore o armamento** | 10 |
| `shifts in your shield configuration` | **modifiche alla configurazione degli scudi** | 12 |

## 3. Nodi aperti (da non dedurre dopo)

1. **`Cooling Ducts` resta inglese anche in prosa**: è un nome di prodotto, non un descrittore.
2. **`spazio umano`** per `human space`: coerente con i lotti precedenti, e diverso da `human space` come nome proprio.
3. **I due rigeneratori non sono varianti della stessa frase**: `S-270` = efficienza perduta, `S-970` = potenza e calore.
4. **`shield matrix`** è «matrice dello scudo» (singolare), non «scudo»: è il termine tecnico del gioco.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 12 unità `PENDING`.
- **Nessun equipaggiamento visto a schermo**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Primo lotto di `human outfits.txt`**.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (24 controlli), `verify.py` exit **0** (20 controlli) |
