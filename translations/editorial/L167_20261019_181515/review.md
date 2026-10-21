# REVIEW — L167 · `paradise world jobs.txt` (nove lavori)

Coppie EN→IT rilette in `translation.json` (`58330ce6689b1aed…`). Tutte le 28 unità sono **`PENDING`**.

## 1. Voce

I lavori di Paradise sono **commedie sociali brevi**: la madre ansiosa che manda un pacco al figlio studente, la coppia
anziana che contribuisce al compleanno del nipote, il ragazzino imbronciato che fa una scenata in giardino, i due
festaioli con «farmaci del tutto legali», la missione di misericordia con gli scaricatori ben pasciuti. La resa tiene
il tono **leggero e ironico**, senza appiattirlo.

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `Care package to <planet>` | **identico** (`VALUE`) | 1 |
| `pacco di generi di conforto` | *care package* | 2, 3 |
| `scenata fin troppo visibile` | *very conspicuous fit* | 6 |
| `complesso da reggia` | *palatial complex* | 9 |
| `piccioncini` | *lovebirds* | 12 |
| `farmaci del tutto legali` | *completely legal pharmaceuticals* | 20, 21 |
| `piantagrane chiassosi e maleducati` | *rowdy and uncouth troublemakers* | 22 |
| `anime denutrite` | *undernourished souls* | 27 |

## 3. Nodi aperti (da non dedurre dopo)

1. **62 token**: la verifica è per simbolo **e** per unità; il multiset da solo non basta.
2. **`Party-goers to <planet>` è lo stesso `VALUE` in due missioni** (19 e 23): la resa è identica, il che è banale
   perché è un `VALUE`, ma il controllo lo rende esplicito.
3. **Le due `Transport partiers`** differiscono per la coda: «farmaci» vs «snack e materiale scolastico».
4. **Il confine di riga 225 è un `VALUE`**: chi apre L168 trova prima il nome del lavoro e poi la descrizione.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 28 unità `PENDING`.
- **Nessun lavoro visto a schermo**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Primo lotto di `paradise world jobs.txt`**.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (23 controlli), `verify.py` exit **0** (21 controlli) |
