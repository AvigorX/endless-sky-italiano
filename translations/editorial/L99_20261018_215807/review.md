# REVIEW — L99 · `hai culture conversations.txt` (sport e gioco d'azzardo)

Coppie EN→IT rilette in `translation.json` (`545c18fca521b07f…`).

## 1. Voce e registro

- **Le tre missioni sportive** hanno tutte la voce del **narratore**, non del giocatore: presente indicativo,
  «notate», «vedete», «capite». La resa mantiene la stessa persona in tutte e tre, altrimenti le tre scene
  sembrerebbero scritte da mani diverse.
- **Il barista** (26–37) è lo stesso personaggio che parla per dodici unità di fila: prima spiega, poi si
  scalda («Siamo anzi molto bravi a bluffare»), poi si scusa con un'alzata di spalle («prima di parlarle fino a
  stordirla»). Dà del **«lei»** al giocatore in tutto il dialogo.
- **Il giocatore** interviene con quattro battute brevi (25, 30, 31, 34) e una domanda secca (28): «I principi
  della maturità?».
- Il narratore **non commenta** la morale Hai: il testo lascia che sia il barista a dire che il bluff è «molto
  immaturo e basso».

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità | nota |
|---|---|---|---|
| `trilling` | **trillare** | 1, 7, 8, 14, 15, 21 | suono di gola, distinto dal *chittering* |
| `(Ignore them and pass by.)` | **(Ignorateli e passate oltre.)** | 2, 9, 16 | «them» = gli Hai |
| `(Take a look.)` | **(Date un'occhiata.)** | 3, 10, 17 | |
| `the shorter Hai folk` | **gli Hai più bassi** | 4, 11, 18 | |
| `glossy printed photos` | **foto stampate su carta patinata** | 4, 11, 18 | |
| `a generically blurred opponent` | **un avversario volutamente sfocato** | 5 | |
| `a trick of artificially shifting perspective` | **un trucco di prospettiva spostata artificialmente** | 5, 12 | |
| `a svelte Hai in the strikingly familiar costume of a fencer` | **un Hai snello nella divisa di schermidore, di una familiarità sorprendente** | 12 | |
| `parry and riposte` | **parata e risposta** | 12 | termini della scherma |
| `out-of-frame opponent` | **avversario fuori campo** | 12 | |
| `a bladed frisbee` | **un frisbee con lame** | 19 | |
| `all the ones that affect us the least` | — | — | non in questo lotto |
| `the maturity tenets` | **i principi della maturità** | 26, 28, 29 | nome in-world |
| `'To be honest in dealings'` | **'Essere onesti negli affari'** | 29 | apici semplici |
| `'To gamble only on skill, not chance'` | **'Scommettere solo sull'abilità, non sul caso'** | 29 | |
| `'To have clear separation of fantasy and reality'` | **'Avere una chiara separazione fra fantasia e realtà'** | 32 | |
| `primitive instincts` | **istinti primitivi** | 35 | |
| `evolutionarily advantageous in the wild` | **vantaggioso per l'evoluzione allo stato brado** | 35 | |
| `more guidelines than actual rules` | **più indicazioni che regole vere** | 37 | |
| `before I talk your ears off` | **prima di parlarle fino a stordirla** | 37 | idiom, non tradotto alla lettera |

## 3. Nodi aperti (da non dedurre dopo)

1. **L'unità 32 ha una sola virgoletta**: la citazione si chiude nell'unità 33. Se un revisore «aggiustasse» la
   punteggiatura, il gioco mostrerebbe una virgoletta in più a metà discorso. Il `check.py` e il `verify.py`
   asseriscono **entrambi** `odd == [32]`.
2. **I sette gruppi di ripetizioni** sono resi da costanti: correggere una frase significa correggerla **una
   volta sola**, nel costruttore, e rigenerare. Modificare `translation.json` a mano romperebbe l'uguaglianza e
   il `verify.py` diventerebbe rosso.
3. **Le tre missioni sportive non sono un errore di duplicazione**: il gioco le usa come tre incontri diversi.
   La sola unità che cambia (5, 12, 19) è quella che descrive lo sport.
4. **I «principi della maturità»** tornano nel file: `Sick of Acorn Bread` (righe 346–386) ne parla ancora. La
   resa «principi della maturità» è ora fissata e va riusata.
5. **`tabù`** è italianizzato e accentato: non «taboo». Il `check.py` accetta l'accento (è nel range latino) ma
   rifiuta i caratteri non latini.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 38 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: nessuna di queste scene è stata vista a schermo.
- **Nessuna revisione umana**.
- **Il file non è completo**: 70 unità su 4 contesti.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (30 controlli), `verify.py` exit **0** (28 controlli) |
