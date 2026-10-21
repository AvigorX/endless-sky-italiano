# REVIEW — L184 · `human outfits.txt` (licenze, le due pietre, Puny) — **chiude il file**

Coppie EN→IT rilette in `translation.json` (`cb00379ce130e0d0…`). Tutte le 13 unità sono **`PENDING`**.

## 1. Voce

Il file si chiude **in sordina**: un cane, due pietre, una mappa, una fila di licenze. È il registro più **amministrativo**
di tutto il file (tasse, permessi, privilegi) interrotto da due cose che non c'entrano nulla — la pietra fredda e la
pietra calda, e il cane che non fa i bisogni in giro. La traduzione non ha aggiunto ironia dove non c'era, ma non l'ha
nemmeno tolta (idx 3 e idx 13).

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `rescued from` | **salvato da** | 2 |
| `stick by your side` | **restarti accanto** | 2 |
| `Her history matches with Pookie's` | **La sua storia coincide con quella di Pookie** | 3 |
| `toilet-trained` | **insegnato a usare il gabinetto** | 3 |
| `lacks any power source` | **Non ha alcuna fonte di energia** | 4 |
| `data chip` | **chip dati** | 6 |
| `tax revenue` | **entrate fiscali** | 7 |
| `pilot's license` | **patente di pilota** | 7 |
| `capital ship` | **nave capitale** | 10 |
| `decommissioned` | **dismessa** | 11 |
| `fly the colors` | **volare con i colori** | 12 |

## 3. Nodi aperti (da non dedurre dopo)

1. **`"Puny"` è un `VALUE` con le virgolette**: non si normalizza togliendole. Se un futuro controllo «ripulisce» le
   virgolette dalle stringhe, rompe il nome.
2. **`Puny`, `Pookie`, `Freedom`, `Skadenga`, `Ildico Drifa`, `Free Worlds`** restano invariati; `Parliament` diventa
   «Parlamento» perché è un'istituzione descritta, non un nome di fazione.
3. **I 7 apici inglesi non hanno equivalente italiano**: `Pookie's` → «di Pookie», `Republic's` → «della Repubblica». I 3
   apici italiani nascono da elisione (`un'Ausiliaria`, `un'astronave`, `l'umanità`).
4. **Il file è chiuso**: 63/63. Il prossimo lavoro qui sarebbe una riscrittura.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 13 unità `PENDING`.
- **Nessun equipaggiamento visto a schermo**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **File chiuso ma non approvato**.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (27 controlli), `verify.py` exit **0** (21 controlli) |
