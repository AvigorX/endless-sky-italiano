# REVIEW — L145 · `unfettered 0 prologue.txt` (la loggia delle armi)

Coppie EN→IT rilette in `translation.json` (`56b7e47a1b3a8c72…`). Tutte le 13 unità sono **`PENDING`**.

## 1. Voce

- **Desneeparu** è marziale e giocosa: «Sembra che tu sappia come si usa una lama!», e ride della faccia sorpresa del
  giocatore. La didascalia lo dice senza spiegarlo: «Capisci che ti stava prendendo in giro fin dall'inizio».
- **Gli ingegneri** parlano da tecnici: «Preferiamo fare la maggior parte dei nostri collaudi sul campo di battaglia»,
  «Più interesse suscita un prototipo, più lo sviluppiamo».
- **La narrazione** usa il sarcasmo del commerciante: «tanto che potrebbe quasi passare per un fornitore Hai 'normale',
  se non fosse per la sensazione sovraccarica e opprimente delle aree di prova».
- **Il `LOGBOOK`** è la voce più asciutta del lotto: tre frasi, nessun dialogo, un giudizio su di sé.

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `<The engineer>` | **`<The engineer>`** (esatto) | 5 |
| `a blade! <learned>I am Desneeparu` | **una lama! `<learned>`Sono Desneeparu** | 2 |
| `Captain <last>!` | **capitano `<last>`!** | 2 |
| `Tripulse Shredder` · `Blaster` · `Ion Cannon` | **identici** | 6–13 |
| `Shield Beetle` · `Firelode` | **identici** | 5, 12 |
| `our sympathy` | **la nostra riconoscenza** | 6 |
| `to jam their weapons` | **inceppare le armi** | 12 |
| `a hybrid weapon` | **un'arma ibrida** | 13 |
| `turn the tide of battle` | **ribaltare le sorti di una battaglia** | 12 |

## 3. Nodi aperti (da non dedurre dopo)

1. **`<The engineer>` è case-sensitive**: contiene articolo e maiuscola, e una variante minuscola sarebbe un **simbolo
   diverso** per il motore. Il controllo vieta esplicitamente `<the engineer>`.
2. **Le due virgolette dispari non si chiudono**: unità 12 e 13, difetto del sorgente. Il controllo pretende che
   l'italiano **non** finisca con una virgoletta e che il segno finale sia lo stesso dell'inglese.
3. **Il `LOGBOOK` si traduce come diario**: niente virgolette, niente «tu» enfatico, e la resa non è identica
   all'inglese (verificato).
4. **I nomi tecnici restano**: cinque nomi, tutti verificati presenti; il `check.py` rifiuta le traduzioni inventate.
5. **`tripulse` minuscolo** in due battute del giocatore (unità 8 e 10) contro `Tripulse Shredder` maiuscolo nel nome
   completo: la differenza è nel sorgente e non si normalizza.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 13 unità restano `PENDING`.
- **Nessuna arma comprata**: la loggia non è stata aperta nel gioco.
- **Nessuna revisione umana**.
- **`unfettered 0 prologue.txt` è all'87,1%**: 19 unità da fare, l'ultimo tratto del file.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (32 controlli), `verify.py` exit **0** (27 controlli) |
