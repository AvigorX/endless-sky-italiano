# REVIEW — L104 · `quarg missions.txt` (Coalizione e avvertimento)

Coppie EN→IT rilette in `translation.json` (`1186c7b9ae462081…`).

## 1. Voce e registro

- **Il Quarg della Coalizione** (5–10): formale e sprezzante senza alzare la voce — «la stolta Coalizione»,
  «quei miseri Heliarch». Dà del **«tu»** («Non sottovalutarci, umano»).
- **Il Quarg della nave Pug** (14–25): parla per immagini («un bambino in fasce che ha addomesticato un drago») e
  poi passa all'avvertimento, con l'inversione finale («a dirigere questo potere, e non lui a dirigere voi»). Dà
  del **«voi»**.
- **Il giocatore** ha battute brevi: due domande nel primo contesto, quattro risposte dichiarate nel secondo
  («atto di giusta ribellione», «Dio è morto», «me la sono presa»).
- **Il narratore** (1, 4, 11, 12, 13, 26, 27) resta descrittivo e chiude sul dettaglio degli sguardi torvi
  nell'anello.

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità | nota |
|---|---|---|---|
| `ask for their side of the story` | **chiedere la loro versione della storia** | 1 | |
| `usurpation of the great deeds of others` | **usurpare le grandi imprese altrui** | 5 | |
| `petty thieves` | **ladruncoli** | 6 | |
| `wretched Heliarchs` | **miseri Heliarch** | 6 | |
| `hindered their development` | **ostacolavate il loro sviluppo** | 8 | |
| `clicks its teeth together` | **fa scattare i denti l'uno contro l'altro** | 9 | resa già fissata in L102 |
| `frowns a bit` | **si acciglia un po'** | 9 | |
| `blank expression` | **espressione vuota** | 9 | |
| `we just know better than to slaughter billions` | **sappiamo solo che è meglio non massacrare miliardi di esseri** | 9 | |
| `jump drive` | **motore a salto** | 10 | |
| `the Pug Arfecta` | **il Pug Arfecta** | 12 | nome di nave, invariato |
| `imposing` | **imponente** | 13 | |
| `piercing stare` | **sguardo penetrante** | 12, 13 | |
| `a baby in swaddling` | **un bambino in fasce** | 14, 22 | ripetuto dal Quarg |
| `righteous defiance` | **giusta ribellione** | 16 | |
| `the Pug fancy themselves gods` | **i Pug si credono dèi** | 17 | |
| `God is dead` | **Dio è morto** | 17 | |
| `scoffs` | **sbuffa** | 19 | |
| `deign to prove them wrong` | **ti degni di dimostrare che si sbagliano** | 21 | |
| `burdens and dangers` | **fardelli e pericoli** | 24 | |
| `be the one who directs` | **essere voi a dirigere** | 24 | |
| `curt farewell motion` | **breve cenno di commiato** | 26 | |
| `glares` | **sguardi torvi** | 27 | |

## 3. Nodi aperti (da non dedurre dopo)

1. **`(No.)` è identico al sorgente** e va lasciato così: in italiano la parola è la stessa. Il `check.py`
   asserisce «identica **solo** l'unità 3» — non è un permesso generico, è un'eccezione nominata. Se un revisore
   la «traduce» in `(No, grazie.)` il controllo diventa rosso, ed è voluto: quel testo è una scelta del giocatore
   e la sua lunghezza conta nel layout.
2. **Le cinque citazioni aperte** non si chiudono: il gioco unisce i messaggi. Chiudere l'unità 23 aggiungerebbe
   una virgoletta a metà dell'avvertimento.
3. **Il trattino dell'unità 23** è un `-` con spazi, non un em dash. La regola tipografica del progetto vieta `—`;
   qui il carattere è nel sorgente e va riprodotto com'è.
4. **`il Pug Arfecta`** è una nave, non un equipaggiamento: resta invariato come i nomi di classe.
5. **`Dio è morto`** è una citazione nietzscheana nel testo inglese: non è un errore di maiuscole italiane.
6. **I due arrivi** (12 e 13) non sono varianti stilistiche: la prima scena ha la scorta Pug, la seconda no.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 27 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: nessuna di queste scene è stata vista a schermo.
- **Nessuna revisione umana**.
- **Il file non è completo**: 61 unità residue, un solo contesto.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (27 controlli), `verify.py` exit **0** (27 controlli) |
