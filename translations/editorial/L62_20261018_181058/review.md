# REVIEW — L62 · `data/human/culture conversations.txt`

Revisione del lotto dopo la chiusura dei controlli.

## 1. Coerenza con L58–L61

- Stesso narratore in seconda persona; qui il giocatore **ascolta** e non agisce, salvo due scelte di
  contorno (restare o andarsene). La voce resta asciutta: il testo non commenta ciò che sente.
- Le etichette `overheard scientists 1/2/3` segmentano la scena in tre blocchi: sono **chiavi**, e il
  numero finale non è decorativo (il gioco concatena le parti). Restano identiche.

## 2. Nodi traduttivi aperti (dichiarati)

- **«Attendee»** (1): «Partecipante». È il termine stampato sul badge: neutro, burocratico, e resta tale.
- **«Pan-galactic Conference on Interstellar Microbial Genomics and Population Dynamics»** → «Congresso
  Pan-galattico annuale di genomica microbica interstellare e dinamica delle popolazioni». Titolo lungo:
  l'italiano non ha una forma idiomatica e la resa resta una traduzione letterale, che è quello che serve
  per un nome di convegno.
- **«I guess this isn't so much a question as a comment»**: reso «Credo che questa non sia tanto una
  domanda quanto un commento». È una citazione di una frase fatta accademica: deve suonare leggermente
  lunga, come nell'originale.
- **«wannabe rockstar personalities»** → «personalità da rockstar mancate». «Wannabe» ha una sfumatura
  sprezzante che «mancate» conserva meglio di «aspiranti».
- **«The Syndicate»** → «il Sindacato»: è una delle fazioni del gioco, con la maiuscola.
- **«University of Chiron»** → «Università di Chiron»: Chiron resta invariato (toponimo).

## 3. Duplicati

**Nessuno.** Terzo lotto del file con 0 gruppi; l'asserzione negativa in `verify.py` resta esplicita.

## 4. Cosa NON è stato fatto

- **Nessuna scrittura su `state.db`**: le 30 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: verifica sui file.
- **Nessuna verifica di runtime** delle due scelte di contorno (2/3 e 13/14/24/25): il testo c'è, la
  concatenazione delle tre etichette non è stata provata nel gioco.

## 5. Rischi residui

- **La concatenazione dei tre blocchi** dipende dalle etichette, non dal testo: se un giorno si
  decidesse di tradurle, la scena si romperebbe. È il motivo per cui sono elencate una per una.
- **Il gergo accademico** è reso con termini italiani correnti; una revisione umana dovrebbe verificare
  che «ciclo di retroazione positivo» sia accettabile per un lettore non specialista (l'alternativa
  «retroazione positiva» è più comune in biologia).
- **Il file è al 46%**: restano 202 unità, tra cui `Earth Day Blackout` e le scene di `Sol-Bound`.

## 6. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 1 parte, `translation.json`, `check.py`, `verify.py`, documenti |
| ESEGUITO | sì — entrambi gli script lanciati, output letto |
| VERIFICATO | sì — `check.py` `FAIL totale: 0` (33 controlli), `verify.py` exit 0 (36 controlli) |
