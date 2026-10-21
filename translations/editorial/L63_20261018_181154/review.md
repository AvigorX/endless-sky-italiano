# REVIEW — L63 · `data/human/culture conversations.txt`

Revisione del lotto dopo la chiusura dei controlli.

## 1. Coerenza con L58–L62

- Stesso narratore e stessa voce asciutta. `Sol-Bound Shuttle` è il primo ritratto del file in cui un altro
  pilota **spiega le proprie scelte di vita**: il testo non lo giudica e la traduzione nemmeno.
- `Earth Day Blackout` riprende il tema della classe e della storia già presente in L58 (Paradise) e lo
  porta su scala planetaria: la tradizione è collettiva, l'addetto però lavora.
- Il lessico fissato resta: «spazioporto», «capitano», «Parlamento», «Shuttle», «blackout».

## 2. Nodi traduttivi aperti (dichiarati)

- **`Luna` / `Moon`** (5): vedi REPORT. La battuta sul termine arcaico non è riproducibile in italiano
  perché «Luna» è il termine corrente. Dichiarato, non nascosto.
- **`hyperdrive`** (1): «iperguida». Termine tecnico del gioco, già usato altrove.
- **`spaceworthiness`** (12): «idoneità spaziale della nave». Parola burocratica in inglese, resa con
  analoga burocrazia.
- **`datapad`** (23): resta invariato: è un oggetto del gioco, non un tablet.
- **`supertall buildings and skyscrapers`** (11): «i grattacieli enormi». L'inglese distingue due categorie
  (supertall / skyscraper); l'italiano le fonde. Accettato, con perdita dichiarata.
- **`the 22nd of April`** (32): «il 22 aprile». Data reale, nessuna conversione di calendario.

## 3. Virgolette dispari

Le unità **18, 29, 31** aprono un discorso diretto e **non lo chiudono** nel sorgente (51 virgolette totali,
3 dispari). Riprodotte identiche: `verify.py` confronta l'insieme `(18, 29, 31)`. Chiudere quelle virgolette
«per pulizia» romperebbe la parità e, nel gioco, il rendering del dialogo.

## 4. Duplicati

**Nessuno.** Quarto lotto del file con 0 gruppi; l'asserzione negativa resta in `verify.py`.

## 5. Cosa NON è stato fatto

- **Nessuna scrittura su `state.db`**: le 37 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: verifica sui file.
- **Nessuna verifica di runtime**: le due scene hanno scelte minime (2/3/4, 13/14, 16/17, 19/20, 24/25,
  27/28, 33/34) e non sono state provate nel gioco.

## 6. Rischi residui

- **Il testo delle unità 18, 29, 31 è lungo e non chiuso**: se in futuro un revisore «aggiusta» le
  virgolette, il controllo diventa rosso — ed è il controllo che deve difendere il dato.
- **La spiegazione della Giornata della Terra** è il primo brano del file con un contenuto storico
  inventato (XX secolo, auto primitive, centrali): la traduzione non deve sembrare una lezione, e la resa
  mantiene il tono di chi racconta una cosa sentita a scuola («la mia vecchia lezione di storia mi dice»).
- **Il file è al 55,9%**: restano 165 unità, tra cui `Burthen Triathlon` e `CCOR Guerrilla Standoff`.

## 7. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 2 parti, `translation.json`, `check.py`, `verify.py`, documenti |
| ESEGUITO | sì — entrambi gli script lanciati, output letto |
| VERIFICATO | sì — `check.py` `FAIL totale: 0` (33 controlli), `verify.py` exit 0 (36 controlli) |
