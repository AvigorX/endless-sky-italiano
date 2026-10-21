# REVIEW — L94 · `coalition culture conversations.txt` (secondo lotto)

Coppie EN→IT rilette in `translation.json` (`2413e9527696c61a…`).

## 1. Voce e registro

- **Gli Arach parlano come i Saryd**: ordine invertito (`appreciate the fine arts, do you?` →
  `apprezzate le belle arti, voi?`). È la voce della Coalizione, non un refuso: le unità interessate sono
  **1, 4, 11, 12, 15, 18, 19, 20, 24, 27, 33, 36**.
- **Matlub** ha un registro più formale degli altri: «signora Matlub», i patroni, le Casate. Il narratore resta
  piano, come nei lotti precedenti.
- **Il giocatore è «voi»**: «Mi accompagnate, volete?», «Ringraziate Matlub». Nessuna forma che presupponga il
  suo genere.
- **Gli Arach sono femminili o maschili secondo il testo**: Matlub è «she» (femminile), il minatore e il
  giardiniere sono «he» (maschile). Il narratore segue il sorgente, non un'ipotesi.

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità | nota |
|---|---|---|---|
| `Moonstruck` | **Toccato dalla Luna** | 12 | titolo tradotto |
| `Babbling Bebliss` | **Bebliss Balbettante** | 18 | Casata invariata, aggettivo tradotto |
| `'Til Death` | **Fino alla Morte** | 24 | titolo-tipo |
| `soiree` | **serata** | 1, 4, 15, 27, 33 | evento culturale |
| `patrons` | **patroni** | 7, 8, 15, 19, 27, 30 | non «clienti» |
| `dress` (fra virgolette) | **abito** | 1 | il testo lo mette fra virgolette perché è un'analogia umana |
| `socks` (fra virgolette) | **calzini** | 19 | idem |
| `House Chamgar` / `House Bebliss` | **Casa Chamgar** / **Casa Bebliss** | 19, 20 | forma dominante |
| `fly tower` | **torre scenica** | 14 | termine tecnico |
| `a round of applause` | **un applauso** | 27 | «round» è l'onda, non un giro |

## 3. Nodi aperti (da non dedurre dopo)

1. **La quarta rappresentazione non ha titolo** e non viene annunciata: il testo non spiega chi la mette in
   scena. Non ho aggiunto spiegazioni: il mistero è del sorgente.
2. **«Toccato dalla Luna»** è una scelta di titolo: se il revisore preferisse lasciarlo in inglese, cambia una
   parola in due unità (12 e il richiamo interno, se ci sarà).
3. **`Bebliss Balbettante`** mantiene la Casata in italiano: coerente con `Casa Bebliss` due unità dopo.
4. **`defend r` / `defend ww`** e le altre etichette di salto **non sono in questo lotto** (cadono in L95):
   vanno lasciate identiche.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 36 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: nessuna di queste scene è stata vista a schermo.
- **Nessuna revisione umana**: il lotto non è approvato.
- **Il file non è chiuso**: 90 unità restano (righe 148–462).

## 5. Rischi residui

- **Il registro marcato può sfuggire** in una battuta su dodici: l'elenco delle unità con parlato Arach è nel
  §1, e va riletto a ogni revisione.
- **Due gruppi di scelte ripetute** (16/22, 17/23/29): una modifica a una sola delle unità rompe il controllo.
- **La scena muta finale** è la più lunga del lotto (150 + 183 parole): se il revisore volesse alleggerirla,
  sarebbero due unità da riscrivere insieme, non una.

## 6. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (29 controlli), `verify.py` exit **0** (28 controlli) |
