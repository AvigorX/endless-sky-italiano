# REVIEW — L138 · `data/starts.txt` (quarto inizio: gli Hai)

Coppie EN→IT rilette in `translation.json` (`ab536b2d9a5a2c29…`). Tutte le 47 unità sono **`PENDING`**.

## 1. Voce

- **Il venditore Hai** è cerimoniale e stanco: «Mi ha servito bene nell'ultimo secolo, ma sono certo che sarà al sicuro
  nelle tue mani», e poi: «Direi che ci rivedremo un giorno, ma preferisco non mentire.»
- **Il mondo Hai** è spiegato in tono da enciclopedia: «Gli Hai sono una specie di roditori giganti e intelligenti, che
  vivono a nord dello spazio umano.»
- **Gli Unfettered** hanno la loro voce dura e la loro teoria: «Sostengono che molto tempo fa i Drak alterarono gli Hai
  per renderli docili e pacifici.»
- **Il giocatore** risponde secco, come nei menu di scelta: «"Sì, è così."», «"Chi ha detto che potevi guardare?"»,
  «"Preferisco cavarmela da solo."»

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `Hai Origins` (×2) | **identico** | 1, 5 |
| `This start is locked.` | **Questo inizio è bloccato.** | 4 |
| `To unlock this start, you must complete the main human campaign.` | **Per sbloccare questo inizio devi completare la campagna umana principale.** | 8 |
| `1.431 million credits` · `0.3%` · `4,836 credits per day` | **1,431 milioni** · **0,3%** · **4.836** | 19 |
| `"Unfettered"` · `"prison"` | **«Unfettered»** · **«prigione»** | 16 |
| `"Sheragi"` | **«Sheragi»** | 17 |
| `pay it forward` | **restituire il favore** | 31 |
| `a tough ask` | **un osso duro** | 37 |
| `1.132 million credits` | **1,132 milioni di crediti** | 36, 37, 38, 43 |

## 3. Nodi aperti (da non dedurre dopo)

1. **Due inizi, un nome**: se un revisore «corregge» uno dei due `Hai Origins`, rompe l'identità fra i due blocchi e il
   controllo lo segnala.
2. **Quattro battute aperte** (26, 36, 37, 38): sono del sorgente. Chiuderle è un errore, non una gentilezza.
3. **`Pristine Jewel` è un nome proprio di nave**: resta, come `Grasshopper`, `Aphid`, `Sheragi`, `Drak`.
4. **I numeri sono in milioni**: 1,431 e 1,132 — con la virgola decimale italiana, non il punto inglese.
5. **Il gate è largo ma non infinito**: l'unità 40 (`"We do!"` → «"Affare fatto!"») sta a 1,78, sotto il tetto di 1,90.
   Accorciarla ancora («Sì!») perderebbe il registro cerimoniale del patto.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 47 unità restano `PENDING`.
- **Nessun inizio avviato**: Greenwater, la folla e il venditore non sono stati visti nel gioco.
- **Nessuna revisione umana**.
- **`starts.txt` è al 98,2%**: restano due nomi di equipaggiamento, che chiudono il file in L139.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 5 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (32 controlli), `verify.py` exit **0** (31 controlli, invariante di segmento) |
