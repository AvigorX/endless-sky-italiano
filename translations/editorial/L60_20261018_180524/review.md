# REVIEW — L60 · `data/human/culture conversations.txt`

Revisione del lotto dopo la chiusura dei controlli: scelte, dubbi dichiarati, rischi per chi prosegue.

## 1. Coerenza con L58–L59

- Stesso narratore (seconda persona, presente) e stesso registro osservativo. Il varo della nave è la
  prima scena del file in cui il giocatore **interagisce con una persona che non è un servitore**: il tono
  resta leggero, e le battute sono permesse.
- **«spazioporto»**, **«Shuttle»**, **«crediti»**, **«Deep»**: il lessico fissato nei lotti precedenti è
  rispettato.
- Il brano `Masquerade Hanging` rompe il tono: è la prima violenza esplicita del file (un corpo fatto
  rotolare, una pistola alla tempia). Il contrasto è nel sorgente e non è stato attenuato.

## 2. Nodi traduttivi aperti (dichiarati)

- **«cheesy pilot uniform»** (1): «uniforme da pilota piuttosto pacchiana». «Pacchiana» è colloquiale e
  rende il disprezzo affettuoso dell'inglese; «kitsch» sarebbe più colto e meno adatto al narratore.
- **«my psychiatrist»** (18): «il mio psichiatra». La battuta presuppone che il giocatore vada da uno
  psichiatra: è un dettaglio del personaggio, non un errore, e resta.
- **«mortgage»** (23, 24): «mutuo» / «debito della nave». Nel gioco la prima nave si compra a rate; il
  testo alterna i due termini e la traduzione fa lo stesso.
- **«dias»** (30): «palco centrale». È un termine architettonico (la pedana rialzata), reso con la parola
  che un italiano userebbe guardando la scena.
- **«masquerade»** nel nome del contesto resta nel titolo della missione, non nel testo: non è tradotto
  perché è un identificatore.

## 3. Duplicati

**Nessuno.** Secondo lotto consecutivo con 0 gruppi; l'asserzione negativa in `verify.py` resta.

## 4. Cosa NON è stato fatto

- **Nessuna scrittura su `state.db`**: le 31 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: verifica sui file.
- **Nessuna verifica di runtime** dei quattro rami del varo e dei due nodi di `Masquerade Hanging`: il
  testo c'è, l'esito nel gioco no.

## 5. Rischi residui

- **Il giudizio del narratore nel ramo `get out`** (21) è esplicito in inglese e in italiano. Se in fase di
  revisione lo si volesse attenuare, si cambierebbe il senso della scelta: il ramo esiste per far sentire
  il giocatore in colpa.
- **Il file è al 31%.** Restano 258 unità, in gran parte `News Reporter - Paradise` e
  `Scientists at the Pub after a Conference`. La scena del varo fissa un tono «brillante» che non va
  importato nelle scene di cronaca nera.

## 6. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 2 parti, `translation.json`, `check.py`, `verify.py`, documenti |
| ESEGUITO | sì — entrambi gli script lanciati, output letto |
| VERIFICATO | sì — `check.py` `FAIL totale: 0` (33 controlli), `verify.py` exit 0 (36 controlli) |
