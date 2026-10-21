# REVIEW — L176 · `avgi ships.txt` (Undsyni, Tachytia, Tremoros, Prismaios)

Coppie EN→IT rilette in `translation.json` (`e2d7853a434cdf00…`). Tutte le 20 unità sono **`PENDING`**.

## 1. Voce

Quattro schede con funzioni diverse: l'Undsyni è **difensivo e pratico** («tenere testa agli attacchi», «accelerazione
per eludere»); la Tachytia è **malinconica e storica** (mai partita per la sua missione, resa obsoleta dall'iperguida,
oggi nave-città); il Tremoros è **cinetico** («sfrecciare oltre qualsiasi avversario»); la Prismaios è **propaganda
militare** (lodata dai capitani della `Twilight Guard`, «prima linea contro gli Aberrant`).

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `Auxiliary Freighter` | **mercantile ausiliario** | 2 |
| `renounced groups` → `renegade groups` | **gruppi rinnegati** | 3 |
| `superconducting magnets` | **magneti superconduttori** | 4 |
| `sublight starship` | **astronave subluminale** | 8 |
| `cryosleep bay` | **baia di criosonno** | 9 |
| `docking bays` | **baie di attracco** | 9 |
| `raw acceleration` | **accelerazione pura** | 12 |
| `interdiction missions` | **missioni di interdizione** | 12 |
| `structural integrity` | **integrità strutturale** | 17 |

## 3. Nodi aperti (da non dedurre dopo)

1. **Un `TEXT` = un nome**: si copia. Vale per 10 delle 20 unità di questo lotto.
2. **`classe` davanti al nome**: «intercettore classe Tremoros», «fregata classe Prismaios». Ometterlo è un difetto che
   il controllo ha trovato.
3. **I decimali prendono la virgola** in italiano: `0,25c`, `0,4c`.
4. **Il refuso inglese non si copia**: `habitatation` → «cilindri abitativi».

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 20 unità `PENDING`.
- **Nessuna astronave vista a schermo**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Terzo lotto di `avgi ships.txt`**.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (27 controlli), `verify.py` exit **0** (25 controlli) |
