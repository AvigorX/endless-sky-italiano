# REVIEW — L92 · `data/successors/successor culture conversations.txt` (chiude il file)

Coppie EN→IT rilette in `translation.json` (`ac367d9586bdaad5…`).

## 1. Coerenza con L90 e L91

- **`Stage Play`** continua dal lotto precedente: stessi manifesti, stessa «Myiara l'Immortale»; il taglio alla
  riga 230 cade dentro la missione ed è l'unico ammesso, perché la finestra successiva è troppo grande per un
  lotto verificabile.
- **Il giocatore è «voi»** nella narrazione («Vi conducono», «Restate», «siete scesi»), «tu» nei dialoghi.
- **I Successori bambini** parlano con lo stesso impasto del genitore (`thou` reso «tu»), ma con sintassi più
  breve: la voce cambia, il registro no.
- **`Sosrue`** resta invariato: è il nome della creatura della poesia, non una descrizione.
- **`spazioporto`, `piazzola di atterraggio`, `Casata`** (mai «Casa» al plurale istituzionale: qui è «Casata
  locale», come `House` in L91), **`<ship>`** invariato.

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità | nota |
|---|---|---|---|
| `they` (Myiara) | femminile | 11, 12, 16, 18 | l'inglese evita il genere; l'italiano lo impone, e la scelta è dichiarata |
| `the Myiaran sort` | **I Miarani** | 4 | collettivo, non «la stirpe miarana» |
| `sepulchre'f of the deep` | **sepolcro degli abissi** | 13 | il verso è storpiato di proposito nel sorgente (`'f`): reso con un italiano leggibile, non con un refuso |
| `off'rings` | **doni** | 13 | idem: la poesia non si mutila |
| `long of arm, discerning of ear, and many of tooth` | **dalle lunghe braccia, dall'orecchio fine e dai molti denti** | 27 | la filastrocca mantiene la struttura a tre membri |
| `This little's favorite` | **Il preferito di questo piccolo** | 27 | `this little` è affettuoso: «questo piccolo» |
| `divorced from thee` | **separate da te** | 35 | il bambino parla per immagini: non «amputate» |
| `Kvelqde shuttle` | **navetta Kvelqde** | 37 | nome di modello invariato |
| `Mirja-Mirja` | invariato | 45 | nome dell'animale |
| `outfitting bay` | **hangar di allestimento** | 46 | coerente con `outfit` → equipaggiamento |

## 3. Nodi aperti (da non dedurre dopo)

1. **Le unità 13 e 21 hanno una sola virgoletta**: sono citazioni lasciate aperte dal testo. Il controllo le
   elenca; **non vanno chiuse**, nemmeno in revisione.
2. **`quills` → «aculei»** (deciso in L91, unità 27 di quel lotto) non ricorre qui: la resa resta quella.
3. **`Metamaterial armor`** (46) usa la voce di glossario «armatura in metamateriale», allineata a L89.
4. **Myiara al femminile**: se una revisione umana decidesse il neutro, servono riscritture in quattro unità
   (11, 12, 16, 18), non una sostituzione meccanica.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 46 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: nessuna di queste scene è stata vista a schermo.
- **Nessuna revisione umana**: il lotto e il file non sono approvati.
- **La campagna non è finita**: 129 file con unità residue, 7.507 unità / 179.623 parole.

## 5. Rischi residui

- **Chiusura del file**: l'invariante 114/114 dipende dai tre `translation.json`; se un lotto precedente venisse
  riscritto, il `verify.py` di L92 diventerebbe rosso — ed è corretto, perché il file non sarebbe più quello
  verificato.
- **Due virgolette dispari**: sono l'unico punto in cui «aggiustare» il testo romperebbe due controlli insieme.
- **Unità 29** è stata riscritta per il rapporto: il senso è «ne ho lottato con una», e il rimando è alla
  domanda precedente sul Sosrue.

## 6. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (28 controlli), `verify.py` exit **0** (29 controlli), file **114/114** |
