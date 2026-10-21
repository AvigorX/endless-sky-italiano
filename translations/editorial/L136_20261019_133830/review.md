# REVIEW — L136 · `data/starts.txt` (secondo inizio: `Birthday Surprise`)

Coppie EN→IT rilette in `translation.json` (`adbc2022515e8753…`). Tutte le 15 unità sono **`PENDING`**.

## 1. Voce

- **Il padre** parla con affetto e soldi: «So che vuoi essere capitano di un'astronave da molto tempo… come regalo di
  compleanno, che ne dici di andare a prenderti una licenza di pilota e una nave al cantiere?».
- **La narrazione** resta al presente e al «tu»: «Entri nel cantiere navale, con la licenza di pilota appena ottenuta
  stretta in una mano e i 500.000 crediti di tuo padre nell'altra».
- **L'impiegata** è formale e poi corruttibile: «"Mi dispiace," comincia a dire la persona dietro al banco, "ma deve
  prima presentare domanda tramite la rete…"» → al secondo gettone: «Firmi qui, prego.»
- **La voce di diario** è entusiasta: «Per il mio compleanno ho ricevuto una licenza di pilota e 500.000 crediti per
  comprare un'astronave. Ora la galassia è a portata di mano.»

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `Birthday Surprise` | **identico** | 1 |
| `500,000 credits` | **500.000 crediti** | 4, 15 |
| `Mainsail` · `Dirt Belt` | **invariati** | 2, 6 |
| `Mondo del Paradiso` | da `Paradise World` | 2, 6 |
| `has no mortgage` | **non prevede mutui** | 3 |
| `credit chip` | **gettone di credito** | 11, 13 |
| `through the net` | **tramite la rete** | 12 |
| `stylus and a pad` | **stilo e una tavoletta** | 13 |
| `child` | **figlio** | 11 |

## 3. Nodi aperti (da non dedurre dopo)

1. **`child` è reso al maschile generico**: l'italiano non ha forma neutra. Il gioco conosce il genere del giocatore:
   se si vuole una resa variabile, è una decisione editoriale da prendere **una volta**, non un errore di questo lotto.
2. **La battuta dell'unità 12 è troncata dal sorgente** (`before-"`): non va «riparata».
3. **Cinque frasi condivise** (unità 5–9) sono rilette da L135: se un revisore le modifica qui, va modificato anche là,
   o i due inizi diranno cose diverse.
4. **`distinti` dentro il lotto ≠ `nuovi` rispetto ai lotti**: erano 15 e 15, ma cinque erano già tradotte.
5. **I nomi di regione restano inglesi**: `Deep`, `Dirt Belt`.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 15 unità restano `PENDING`.
- **Nessun inizio avviato**: non ho visto la scena del padre né il cantiere.
- **Nessuna revisione umana**.
- **`starts.txt` è al 41,6%**: 66 unità da fare (cinque inizi).

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (28 controlli), `verify.py` exit **0** (28 controlli, invariante di segmento) |
