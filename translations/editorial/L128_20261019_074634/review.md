# REVIEW — L128 · `incipias first contact.txt` (la coda: gli Incipias salvati, i capi-governatori)

Coppie EN→IT rilette in `translation.json` (`2efab055b9515fde…`). Tutte le 43 unità sono **`PENDING`**. Il lotto
**chiude il file**.

## 1. Voce

- **Gli Incipias** parlano per composti: «Non saremmo sopravvissuti a un altro giorno-momento qui», «vorremmo porti
  alcune domande-quesiti», «Lascia che ti parli delle sale-nuvole del nostro cielo-casa».
- **I capi-governatori** (Hicemus) sono più formali degli altri: «Se sei d'accordo, vorremmo porti alcune
  domande-quesiti. In cambio saremmo disposti ad ascoltare le tue domande-quesiti».
- **La narrazione** resta al presente e al «tu»: «La tua nave si tuffa tra le nuvole del gigante gassoso».
- **Il traduttore** è piatto per scelta: «L'assenza di emozione nella traduzione è preoccupante, dato il contenuto del
  messaggio» — la nota è del sorgente e resta.

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `Bring Incipias back to <planet>` | **identico** (`VALUE`) | 4 |
| `has incipias ship` · `initial choice` · `odd question` · `end no time` | **identici** (`UI_LABEL`) | 11, 13, 38, 42 |
| `day-moment` | **giorno-momento** | 16 |
| `life-protector` | **protettore-di-vite** | 16 |
| `weather-calamity` | **calamità-meteo** | 16 |
| `outer-helper` | **aiutante-esterno** | 19 |
| `leader-governers` | **capi-governatori** | 21 |
| `question-queries` | **domande-quesiti** | 21 |
| `time-patience` | **tempo-pazienza** | 24 |
| `space-void` | **vuoto-spazio** | 24 |
| `observing-studying` | **osservare-studiare** | 28, 30 |
| `raise-strengthens` | **accresce-rafforza** | 28 |
| `profound-depth` | **visione-profonda** | 30 |
| `determination-will` | **determinazione-volontà** | 30 |
| `origin-world` | **mondo-origine** | 36 |
| `future-point` | **punto-futuro** | 36 |
| `aged-time values` | **valori di tempi-antichi** | 36 |
| `action-pride` · `star-bridge` | **orgoglio-azione** · **ponte-stellare** | 37 |
| `odd-reasonable` | **strano-ragionevole** | 39 |
| `reasoning-origin` | **origine-ragione** | 39 |
| `cloud-halls` · `home-sky` | **sale-nuvole** · **cielo-casa** | 39 |
| `color-sings` · `color-lifeful` | **canti-di-colore** · **color-vitali** | 39 |
| `poetic-gradient` | **gradiente-poetico** | 39 |
| `meeting-talk` | **incontro-colloquio** | 40 |
| `understanding-sad` | **comprensione-triste** | 43 |

## 3. Nodi aperti (da non dedurre dopo)

1. **Il file è chiuso** (161/161): i lotti successivi non lo toccano più, e ogni `verify.py` nuovo non deve rivendicarne
   righe.
2. **`Hicemus` e `Conlatio`** sono nomi di gruppi e restano invariati: il controllo li neutralizza prima della
   scansione dei residui inglesi.
3. **Tre battute non chiuse** nel sorgente (28, 30, 36) restano non chiuse: non è una svista della resa.
4. **Il `VALUE` ha un token dentro** (`<planet>`): confronto sulla stringa intera, non solo sul prefisso.
5. **La voce di diario condivisa con L127** è una copia dichiarata e riletta: se un lotto futuro incontrasse lo stesso
   testo, il metodo è lo stesso.
6. **File nuovo al prossimo lotto**: `boarding missions.txt` ha tipi che qui non ci sono (`TEXT` 48, `CONVERSATION` 7) e
   **43 token in 7 famiglie**: la forma va misurata da zero.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 43 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: la missione non è stata vista, e il file `incipias` completo in staging **non** è
  nel gioco.
- **Nessuna revisione umana**.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (30 controlli), `verify.py` exit **0** (33 controlli, invariante di file) |
