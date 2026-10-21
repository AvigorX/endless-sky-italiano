# REVIEW — L100 · `hai culture conversations.txt` (Academy Motto e Robotic Musical 1)

Coppie EN→IT rilette in `translation.json` (`8fb5defc43780334…`).

## 1. Voce e registro

- **La cameriera dell'Academy** (22–27) parla in Hai e il traduttore la rende: la resa tiene la differenza fra
  il **suo** discorso (registro vivace, «Se vuoi diventare un dirigente…») e il **commento del dispositivo**
  («università non tecnica»). Il dispositivo è impersonale; lei dà del «tu» al giocatore.
- **Il capitano mercantile** (36–43) è cordiale e formale: dà del **«lei»** («che scatola notevole che ha lì»,
  «si avvicini», «le consiglio»), con una punta di canzonatura («In qualche modo è più basso di quanto
  immaginassi»).
- **Il narratore** resta al «voi» e non commenta né il musical robotico né il motto.
- **Le tre `UI_LABEL`** non sono prosa: sono etichette di salto e restano inglesi.

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità | nota |
|---|---|---|---|
| `crowded beyond belief` | **affollato oltre ogni credere** | 1 | |
| `arcane confluence of chance and logistics` | **arcana confluenza di caso e logistica** | 1 | |
| `no safe departure slot` | **nessuna finestra di partenza sicura** | 1 | |
| `(Play games on my ship.)` | **(Gioco sulla mia nave.)** | 2 | |
| `(Have a look around further afield.)` | **(Do un'occhiata più in là.)** | 3 | |
| `throngs of Hai` | **frotte di Hai** | 6 | |
| `often-utilitarian architectural styles` | **stili architettonici spesso utilitaristici** | 6 | |
| `door-to-door salespeople` | **venditori porta a porta** | 6 | |
| `"No Meme Content Here Please."` | **"Niente contenuti meme qui, per favore."** | 7 | riprende le meme war di L98 |
| `terrace` | **terrazza** | 11 | |
| `spiced, or pickled` | **speziate, o sottaceto** | 11, 13 | |
| `follow-up questions` | **domande di follow-up** | 11, 13 | |
| `the city Academy` | **l'Academy cittadina** | 22 | nome proprio conservato |
| `social worker` | **assistente sociale** | 23 | |
| `leadership and communications` | **leadership e comunicazione** | 23 | |
| `revoke people's qualifications` | **revocano le qualifiche** | 24 | |
| `natural exposure` | **esposizione naturale** | 25 | |
| `main thoroughfare` | **viale principale** | 28 | |
| `haphazardly piled crates` | **casse ammucchiate alla rinfusa** | 28 | |
| `springs to life` | **prende vita** | 29 | |
| `caper about` | **sgambettare** | 30, 33 | |
| `beat rests` | **pause di battuta** | 33 | |
| `improvisational` | **improvvisato** | 33 | |
| `heckling` | **provocazioni del pubblico** | 33 | |
| `the same boxes they came out of` | **le stesse casse da cui erano usciti** | 32, 34 | |
| `merchant captains` | **capitani mercantili** | 36 | |
| `logical feature` | **funzione logica** | 39 | |
| `wry grin` | **sorriso sornione** | 41 | |
| `ambles off` | **si allontana** | 44 | |

## 3. Nodi aperti (da non dedurre dopo)

1. **Quattro citazioni restano aperte** (23, 24, 39, 41). Chi revisiona deve sapere che la virgoletta mancante
   non è un errore: il gioco unisce i due messaggi. Chiuderle aggiungerebbe caratteri che il giocatore vede.
2. **Due asserzioni della prima stesura del `check.py` erano sbagliate** («una virgoletta ciascuna» e «la
   citazione si chiude nell'unità successiva»): la 39 ne ha tre, la 25 ne ha quattro, la 43 non apre nulla.
   Sono state riscritte **sul conteggio misurato**.
3. **`Academy` resta invariato** in tutto il lotto: è un'istituzione Hai, non un nome comune.
4. **Il motto** ha una struttura a chiasmo: se un revisore la «semplifica» in quattro frasi coordinate, il
   senso (guidare→conoscere→studiare→servire→guidare) si perde.
5. **`burro di ghiande`** torna in `Sick of Acorn Bread` (righe 346–386): la resa è ora fissata.
6. **`racoon-like`** è un refuso del sorgente per *raccoon*: la traduzione dice «da procione» e non riproduce
   l'errore inglese, che è ortografico e non di senso.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 44 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: nessuna di queste scene è stata vista a schermo.
- **Nessuna revisione umana**.
- **Il file non è completo**: 26 unità residue su 2 contesti.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (30 controlli), `verify.py` exit **0** (28 controlli) |
