# REVIEW — L61 · `data/human/culture conversations.txt`

Revisione del lotto dopo la chiusura dei controlli.

## 1. Coerenza con L58–L60

- Stesso narratore e stessa voce; cambia solo la fonte delle battute (una giornalista, non un passante).
- Le scelte del giocatore sono **sei**, tutte brevi: aspettare / sperare / evitare, e poi quattro coppie di
  risposte con follow-up. La struttura è quella di un dialogo a imbuto, e la traduzione la rispetta:
  nessuna risposta è stata accorciata o fusa.
- Il lessico politico si allinea alle campagne Free Worlds già tradotte (L32–L41): `Parliament`,
  `Navy`, `Free Worlds`.

## 2. Nodi traduttivi aperti (dichiarati)

- **`<origin>`** dentro il discorso diretto: resta il simbolo, non viene sostituito da un nome. In italiano
  la frase regge («Sono qui su `<origin>`…») perché il simbolo è un complemento di luogo.
- **`between trips`** (11): «tra un viaggio e l'altro». È una formula da cronaca, non da narrativa.
- **`gain traction`** (16): «ottenere risultati». Letteralmente «fare presa»; nel contesto politico
  «ottenere risultati per i canali normali» è più chiaro e non tradisce il senso.
- **`proper channels for presenting grievances`** (22): «canali adeguati per presentare le proprie
  lamentele». «Grievances» è più formale di «lamentele», ma in italiano «doglianze» sarebbe arcaico.
- **`ungrateful`** (23): «ingrata». La frase è un giudizio politico esplicito; la traduzione non lo
  attenua con «poco riconoscente», che suonerebbe più educato dell'originale.

## 3. Duplicati

| Gruppo | Unità | Perché |
|---|---|---|
| `"I would prefer to not answer."` | 18, 24 | La stessa opzione di rifiuto in due punti dell'albero |
| Coda dei droni | 20, 26 | Stessa chiusura di scena dopo le due diramazioni |

Resa identica, verificata. Nessuna resa ripetuta fra unità con inglese diverso.

## 4. Cosa NON è stato fatto

- **Nessuna scrittura su `state.db`**: le 26 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: verifica sui file.
- **Nessuna verifica di runtime**: l'intervista ha sei esiti possibili e non è stata provata nel gioco; il
  testo è verificato, la ramificazione no.

## 5. Rischi residui

- **Il tono politico**: le risposte del giocatore sono giudizi espliciti sul Parlamento e sulle Free
  Worlds. Una revisione umana dovrebbe controllare che nessuna risposta risulti più o meno favorevole di
  quanto sia in inglese — è l'unico punto del lotto in cui una sfumatura cambierebbe il senso politico.
- **Il file è al 38%**: restano 232 unità, tra cui `Scientists at the Pub after a Conference` e
  `Sol-Bound Shuttle`. Il formato «intervista» non va importato nelle scene di cronaca.

## 6. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 2 parti, `translation.json`, `check.py`, `verify.py`, documenti |
| ESEGUITO | sì — entrambi gli script lanciati, output letto |
| VERIFICATO | sì — `check.py` `FAIL totale: 0` (33 controlli), `verify.py` exit 0 (35 controlli) |
