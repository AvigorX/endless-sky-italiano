# REVIEW — L95 · `coalition culture conversations.txt` (terzo lotto)

Coppie EN→IT rilette in `translation.json` (`58cfe11da4d60c5c…`).

## 1. Voce e registro

- **I Kimek parlano come Saryd e Arach**: ordine invertito («Busy are you, Captain?» → «Occupato, Capitano?»;
  «Protect our farm, we must» → «Proteggere la nostra fattoria, dobbiamo»). Unità interessate: **1, 5, 9, 10,
  14**.
- **Il narratore resta piano**, anche nelle scene d'azione (19, 22, 24, 26).
- **Il giocatore è «voi»**, nessuna forma che presupponga il genere.
- **Il Saryd presente al forte** è indicato con «il Saryd» (maschile per difetto della parola, non del
  personaggio: il sorgente non ne specifica il genere).

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità | nota |
|---|---|---|---|
| `Spring Siege` | **Assedio di Primavera** | 1, 9 | titolo della fiaba, fra apici |
| `minstrel` | **menestrello** | 9 | testimone oculare della battaglia |
| `chitters` | **cinguetta** | 9, 10 | verso aviario dei Kimek |
| `keep` | **maschio** | 14 | fra virgolette: è la torre del forte |
| `farm` / `crops` | **fattoria** / **raccolti** | 13, 14 | fra virgolette: sono di plastica |
| `battlements` | **merli** | 13, 14, 15 | termine architettonico |
| `blue sashes` / `green` | **fasce blu** / **verde** | 24, 26 | colore = squadra |
| `egg you on` | **incitarvi** | 26 | non «prenderli in giro» |

## 3. Nodi aperti (da non dedurre dopo)

1. **Le etichette di salto `defend r`, `defend rw`, `defend w`** restano identiche: sono i bersagli dei `goto`
   che il gioco segue per i rami. Nel prossimo lotto ne cadono altre cinque (`defend ww`, `attack w`,
   `attack wr`, `attack r`, `attack rr`).
2. **La spiegazione del menestrello** (unità 9) è la chiave della fiaba: il vento copre la vista proprio sul
   finale, quindi la storia non ha un esito canonico. Non ho aggiunto nulla per «spiegare meglio».
3. **`Assedio di Primavera`** è un titolo: se il revisore lo volesse in inglese, cambiano due unità (1 e 9).
4. **Il gilet di cuoio** è descritto come «equivalente Kimek dell'armatura medievale»: è un'analogia del
   giocatore, non un dato del mondo.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 27 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: nessuna di queste scene è stata vista a schermo.
- **Nessuna revisione umana**: il lotto non è approvato.
- **Il file non è chiuso**: 63 unità restano (righe 192–462).

## 5. Rischi residui

- **Le tre etichette di salto** sono l'unico punto in cui «tradurre per coerenza» romperebbe il gioco: sono
  asserite identiche una per una.
- **Unità 2** ha rapporto 0,75, il minimo del lotto (una battuta di 7 parole): dentro il gate, ma è la prima
  da rivedere se la si volesse allungare.
- **La voce marcata** può sfuggire in una battuta su cinque: l'elenco delle unità interessate è nel §1.

## 6. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (28 controlli), `verify.py` exit **0** (29 controlli) |
