# REVIEW — L105 · `quarg missions.txt` (chiude il file)

Coppie EN→IT rilette in `translation.json` (`4ae2c9e490a62867…`).

## 1. Voce e registro

- **Gohl Salyi Memt-Wrik Laz** è il primo Quarg del progetto con una voce **individuale**: parla al **«tu»**, con
  frasi lunghe, pause dichiarate e autocorrezioni («Dopo secoli... no, un millennio di combattimenti»). La resa
  conserva gli incisi invece di compattarli.
- **La sua voce è rotta**: il testo dice che ogni due parole c'è «qualcosa come uno scricchiolio o un cigolio» e
  paragona il suono a un **violoncello scordato**. Non è un dettaglio decorativo: è il motivo per cui le frasi
  sono spezzate, e la traduzione non le rende più fluide del sorgente.
- **Il narratore** resta al «voi» e osserva: le scaglie che non cambiano colore, il respiro che si ferma a metà,
  i dodici Quarg corazzati che si materializzano dalle pareti.
- **Le due domande d'apertura** (1 e 5) sono in seconda persona plurale e **non** sono intercambiabili: la prima
  presuppone il grado di Heliarch, la seconda l'adesione al Lunarium.

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità | nota |
|---|---|---|---|
| `ranks of Heliarch` | **grado di Heliarch** | 1 | |
| `remain hostile to the Quarg` | **resta ostile ai Quarg** | 1 | |
| `landing clearance` | **permesso di atterrare** | 34 | |
| `thin scales cover its fingers` | **le scaglie sottili gli coprono le dita** | 9 | |
| `patches of red-colored chains` | **macchie di catene rosse** | 9 | |
| `crimson hood` | **cappuccio cremisi e rigido** | 9 | |
| `the large scar … where its left eye should be` | **la grande cicatrice … dove dovrebbe essere l'occhio sinistro** | 9 | |
| `a lost gaze focused on the ceiling` | **lo sguardo perduto fisso sul soffitto** | 10 | |
| `crack or a creak` | **scricchiolio o un cigolio** | 14 | |
| `out-of-tune cello` | **violoncello scordato** | 14 | |
| `much too lenient` | **troppo indulgenti** | 14 | |
| `in relative rapid succession` | **in rapida successione** | 14 | |
| `invested heavily in research` | **investirono pesantemente nella ricerca** | 14 | |
| `a millennium of fighting` | **un millennio di combattimenti** | 15 | |
| `awfully protective` | **terribilmente protettivi** | 18 | |
| `jumped to conclusions` | **saltammo alle conclusioni** | 18 | |
| `lost track of wisdom and reason in favor of fearing past shames` | **perdendo di vista la saggezza e la ragione in favore del timore di passate vergogne** | 23 | |
| `defenders arose by the billions` | **A miliardi si levarono difensori** | 27 | |
| `overrun by the Coalition` | **travolti dalla Coalizione** | 27 | |
| `duty-bound` | **legati al dovere** | 37 | |
| `lest you shall be cornered yourself` | **se non vuoi trovarti tu alle strette** | 42 | |
| `the faintest of nods` | **il più impercettibile dei cenni** | 52 | |
| `sparse were my own visits` | **rare furono le mie visite** | 52 | |
| `must make do` | **dobbiamo arrangiarci** | 52 | |
| `a relic of a bygone age` | **una reliquia di un'epoca passata** | 53 | |
| `harrowing sensation` | **sensazione struggente** | 54 | |
| `machine-like formation` | **formazione da macchina** | 60 | |

## 3. Nodi aperti (da non dedurre dopo)

1. **Il `LOGBOOK` (unità 58) è tradotto** e deve restarlo: è la scheda di Gohl nel diario. Le quattro `UI_LABEL`
   invece sono etichette di salto e **non** si traducono. Sono due regole opposte nello stesso lotto.
2. **`<start planet>` e `<start system>`** (unità 49) sono token **nuovi**: contengono uno spazio e il gioco li
   sostituisce con il pianeta e il sistema **di partenza** del giocatore, non con quello corrente. Non si
   traducono e non si spostano.
3. **Le regioni restano in inglese** (`Dirt Belt`, `Deep`, `Paradise Worlds`): sono nomi di regione che il gioco
   mostra così nella mappa. `Earth` invece è «Terra», perché è un pianeta con un nome italiano.
4. **`materalized`** è un refuso del sorgente per *materialized*: la traduzione dice «materializzarsi» e non
   riproduce l'errore ortografico, che non ha significato.
5. **Le sette risposte sulla casa** (44–51) non condividono costanti: sono scelte distinte e ognuna ha la sua
   resa. Se un revisore le uniformasse, il gioco mostrerebbe sette opzioni identiche.
6. **La domanda tripla** (17/20/24) invece **deve** restare identica: è la stessa battuta in tre rami.
7. **Gohl dà del «tu»** in tutto il dialogo, ma il narratore continua a dare del «voi» al giocatore: sono due
   livelli diversi e vanno tenuti separati.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 61 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: nessuna di queste scene è stata vista a schermo.
- **Nessuna revisione umana**.
- **La campagna non è finita**: 126 file con unità residue, 7.040 unità / 159.269 parole.

## 5. Rischi residui

- **Chiusura del file**: l'invariante 178/178 dipende dai quattro `translation.json`; riscrivere un lotto
  precedente renderebbe rosso il `verify.py` di L105 — ed è corretto, perché il file non sarebbe più quello
  verificato.
- **Le `UI_LABEL`** (`heliarch 2`, `heliarch ask`, `lunarium 2`, `lunarium ask`) sono bersagli di `goto`: una
  traduzione «migliorativa» romperebbe il salto e il gioco mostrerebbe un vicolo cieco.

## 6. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (29 controlli), `verify.py` exit **0** (31 controlli), file **178/178** |
