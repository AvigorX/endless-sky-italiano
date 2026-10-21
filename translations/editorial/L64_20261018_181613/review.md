# REVIEW — L64 · `data/human/culture conversations.txt`

Revisione del lotto dopo la chiusura dei controlli.

## 1. Coerenza con L58–L63

- Stesso narratore in seconda persona; qui torna l'**azione** (camminare, ordinare, assistere) dopo i lotti
  più statici di L61–L62. La voce resta asciutta.
- Il lessico politico è ancorato ai lotti delle campagne: «Sindacato», «Mondi del Paradiso», «Bordo
  Esterno», «Repubblica», «Consigli Confederati», «gendarmi».
- Il lessico di Burthen (alta gravità, repulsori, droni-fotocamera) riprende quello di L62 e L63: i droni
  «che faticano con la gravità» e i repulsori «calibrati per la gravità di Burthen» sono già stati usati.

## 2. Nodi traduttivi aperti (dichiarati)

- **«Burthen»** e **«Burthenian»** → «Burthen» e «burtheniano»: il toponimo resta, l'etnico si forma in
  italiano. È una scelta, non un dato del gioco.
- **«munted foot»** (13): «piede maciullato». È slang australiano-tingue; «maciullato» rende il registro
  colloquiale senza cadere nel volgare.
- **«repulsor»** (14): «repulsore». Termine tecnico del gioco.
- **«lingonberry»** (14): «mirtillo rosso». In italiano il *lingonberry* non ha un nome corrente distinto
  dal mirtillo rosso: la perdita è minima e dichiarata.
- **«CCOR»** resta l'acronimo, con l'uniforme «rosa» (*rosy*): il colore è nel testo, non un mio
  aggiunta.
- **«gendarme»** (30, 39, 40): resta «gendarme», non «poliziotto»: è un corpo armato con funzione di
  ordine pubblico, e il testo lo distingue dalla polizia.

## 3. Virgolette dispari

Unità **35, 36, 37**: tre incipit di discorso aperto e non chiuso. Riprodotti; `verify.py` confronta
l'insieme `(35, 36, 37)`. Le unità 38–39 hanno invece le virgolette bilanciate: il discorso «si chiude»
solo alla fine del comizio.

## 4. Duplicati

**Nessuno** dopo la correzione: le unità 7 e 29 erano state fuse per errore e sono state separate.
Il caso è registrato come trappola: **due scelte simili non sono la stessa scelta** se l'inglese le
distingue.

## 5. Cosa NON è stato fatto

- **Nessuna scrittura su `state.db`**: le 42 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: verifica sui file.
- **Nessuna verifica di runtime** delle quattro diramazioni del tendone (5/6/7, 10/11/12, 17) e delle due
  del comizio (28/29, 32/33).

## 6. Rischi residui

- **Il comizio** è il primo testo del file con un contenuto politico esplicito e nomi propri reali del
  mondo di gioco (Korban, Novo Minho, Belenos). La traduzione non deve attenuare né inasprire: chi legge
  deve poter riconoscere la posizione politica senza che il traduttore la commenti.
- **Le etichette `no credits` / `leave tent` / `after tent` / `end`** sono chiavi: se un domani si
  decidesse di localizzarle, servirebbe una modifica al formato dei dati.
- **Il file è al 67,1%**: restano 123 unità, quasi tutte `Exotic Life`.

## 7. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 2 parti, `translation.json`, `check.py`, `verify.py`, documenti |
| ESEGUITO | sì — entrambi gli script lanciati, output letto |
| VERIFICATO | sì — `check.py` `FAIL totale: 0` (33 controlli), `verify.py` exit 0 (36 controlli) |
