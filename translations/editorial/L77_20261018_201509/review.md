# REVIEW — L77 · `data/successors/successor side missions.txt`

## 1. Coerenza con la linea Successors (L68–L76)

- **Casa X / Casate / Alte Casate / Predecessori / Successori / pietre chiave / dispositivo di traduzione /
  cimeli / wormhole**: forme fisse, nessuna reinvenzione.
- **Sieasej** era già comparso (primo contatto, Casa Sioeora): nome invariato, e il testo lo cita come
  traduttore, coerente con L45.
- **Il registro degli studiosi** è arcaico-cerimonioso (`thou was to arrive`, `were't`, `thou coulds't`),
  reso con il «tu» moderno formale come da L45–L76.
- **Kaatiora** parla con entusiasmo didattico; la traduzione non lo rende né infantile né professorale.

## 2. Nodi traduttivi aperti (dichiarati)

- **`the sort of things that poke and prod at places that must remain untouched`**: reso «che fruga e punge
  in luoghi che devono restare intatti» — `poke and prod` è quasi un modo di dire, e la resa resta concreta.
- **`What caused the collapse?` you ask? Hubris, methinks.** → «'Che cosa ha causato il crollo?' chiedi?
  Tracotanza, direi.» — la domanda ripetuta fra virgolette è **citazione interna**, e resta fra virgolette.
- **`were't` / `coulds't`**: forme contratte arcaiche, rese con il condizionale italiano corrente.
- **`divorce from biological sex`** (57): reso «divorzio dal sesso biologico», letterale: è un'espressione
  dell'autore, non un errore.
- **`Katiiora`** (61): refuso del sorgente, **non replicato** (Kaatiora).
- **`High Houses`** → «Alte Casate»: forma nuova; se un lotto futuro la usasse per un'altra istituzione,
  andrebbe distinta.

## 3. Il punto delicato: 22 contro 50

| unità | inglese | italiano |
|---|---|---|
| 22 | `(Don't ask them anything.)` | `(Non chiedere loro nulla.)` |
| 50 | `(Don't ask anything.)` | `(Non chiedere nulla.)` |

Il primo giro le aveva rese **uguali** («Non chiedere nulla.») e il `check.py` è diventato rosso: due
inglesi diversi non sono la stessa scelta (decisione 216). La differenza è minima — un pronome — ma è quella
che il sorgente mette.

## 4. Le tre coppie identiche

7/42 (`"Sure, I would be happy to."`), 9/43 (`"Sorry, but you'll have to find someone else to take you."`),
28/55 (`"I have no more questions."`): le stesse opzioni compaiono in due missioni. Resa identica **voluta**,
dichiarata come gruppo, e il `verify.py` verifica che **solo** quei gruppi si ripetano.

## 5. Virgolette

Unità **56** e **57** aprono la virgoletta e non la chiudono; la chiusura arriva in **58**. Il testo è una
spiegazione del biologo in tre parti, e il gioco le mostra in sequenza. Riprodotto esattamente: il `verify.py`
verifica l'insieme `(56, 57)` **e** che entrambe aprano senza chiudere.

## 6. Cosa NON è stato fatto

- **Nessuna scrittura su `state.db`**: le 63 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: le due missioni, il pianeta primordiale e le domande al biologo non sono
  state viste a schermo.
- **`has deferred` resta in inglese** per scelta: è un bersaglio di salto.
- **Nessuna verifica del registro**: i tre parlanti (Sieasej, il capo ricercatore, Kaatiora) sono valutati
  come testo.

## 7. Rischi residui

- **`0,78` è il minimo** (unità brevi come «(Sì.)»): dentro il gate.
- **`1,30` è il massimo**: nessuna riscrittura.
- **Il `verify.py` asserisce 0 prima / 101 dopo**: sono i conteggi veri del file (164 unità). Se un lotto
  futuro coprisse le righe 17–220, diventerebbe rosso.
- **«Alte Casate»** è una forma nuova: un revisore umano potrebbe preferire «Case Alte», ma servirebbe una
  decisione sull'intero gioco.
- **`Tracotanza`** per `Hubris` è una scelta di tono: «hybris» sarebbe più dotto e meno naturale in bocca a
  un ricercatore che scherza.

## 8. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 4 parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì — entrambi gli script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (32 controlli), `verify.py` exit 0 (45 controlli), sha256 `5e8d1c0e38c05612` |
