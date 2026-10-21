# review.md — L243 (`data/hai/hai ships.txt`, righe 15–332)

Registro delle decisioni editoriali del **primo lotto** di `hai ships.txt`: quattro schede di nave, ventiquattro nomi da
copiare, un motto da tradurre.

## 1. Che cosa si copia e che cosa si traduce

| tipo | unità | trattamento | esempio |
|---|---|---|---|
| `VALUE` | 1 | **copiato** | `Anomalocarises` (nome della nave al plurale) |
| `TEXT` | 23 | **copiato** | `"Biroo" Atomic Thruster`, `"Basrem" Atomic Steering` |
| `DESCRIPTION` | 5 | **tradotto** | la scheda della nave |

I nomi degli equipaggiamenti sono **dati**: il gioco li confronta con i file degli outfit, e tradurne uno solo romperebbe
il riferimento. La regola vale anche **dentro** la prosa: le schede nominano le navi (`Anomalocaris`, `Aphid`, `Centipede`,
`Cicada`, `Scarab`) e il cantiere (`Yeer e Ki`), e quei nomi restano inglesi; si traducono le parole comuni: «nave da
guerra», «mercantile», «capacità di carico», «spazio per i motori», «spina dorsale».

## 2. Le due schede dell'Anomalocaris

Le righe 75 e 99 hanno lo stesso testo **fino all'ultima frase**, poi divergono:

| riga | coda inglese | resa |
|---|---|---|
| 75 | `…making the Anomalocaris more sturdy and able to take larger amounts of damage.` | «…il che rendeva l'Anomalocaris più robusta e capace di assorbire danni maggiori.» |
| 99 | `…making the Anomalocaris more sturdy, although this one has accrued damage after being submerged underwater for a long period of time.` | «…il che rendeva l'Anomalocaris più robusta, anche se questa ha accumulato danni dopo essere rimasta a lungo sott'acqua.» |

Non è una ripetizione da unificare: la seconda è la scheda del **relitto**, e la differenza è informazione di gioco. Il
`check.py` verifica che le due rese **comincino uguali** e **finiscano diverse**, così un copia-incolla distratto si vede.

## 3. Il motto della Cicada

> `…defining the Yeer e Ki shipyard's motto: "Service for Life."`
> «…e che ha dettato il motto del cantiere Yeer e Ki: "Al servizio per tutta la vita."»

Il motto è **tradotto** (non è un nome proprio: è una frase che il gioco mostra) e resta **fra virgolette dritte, col
punto dentro**, come in inglese. Sono 2 delle 48 virgolette del lotto, e il `verify.py` le cerca nella posizione esatta
(`endswith`), non solo nel conteggio.

## 4. I possessivi inglesi

| inglese | resa | nota |
|---|---|---|
| `the Hai's initial conflicts with the Sheragi` | «i primi conflitti **degli Hai** con gli Sheragi» | il genitivo sassone non esiste in italiano |
| `from the project's inception` | «fin dal **suo** concepimento» | possessivo implicito, niente «del progetto» |
| `the Yeer e Ki shipyard's motto` | «il motto **del cantiere** Yeer e Ki» | |
| `one of the most versatile Hai warships of its time` | «una delle navi da guerra Hai più versatili **del suo tempo**» | |

Gli apici passano da **4 a 19**: gli inglesi sono i quattro possessivi, gli italiani sono elisioni (`l'Anomalocaris`,
`l'Aphid`, `dell'economia`, `un'…`, `l'hanno`). Il `check.py` elenca le coppie `(unità, conteggio)` di entrambe le lingue,
così la differenza è dichiarata e non nascosta in un totale che non torna.

## 5. Lessico

| inglese | resa | nota |
|---|---|---|
| `freighter` | **mercantile** | nel corpus «mercantile» è la nave da carico, «trasporto» è il servizio |
| `interplanetary economy` | **economia interplanetaria** | |
| `stock` (defenses as stock) | **di serie** | |
| `backbone` | **spina dorsale** | |
| `pickled acorns` | **ghiande in salamoia** | la battuta resta: è il cibo, non un prodotto industriale |
| `luxury transport ship` | **nave da trasporto di lusso** | |
| `turn of the 31st century` | **intorno all'inizio del trentunesimo secolo** | numero in lettere (come L62: il simbolo `°` è vietato) |
| `second-hand market` | **mercato dell'usato** | |
| `lineages of Hai` | **discendenze di Hai** | |
| `passed it down through the generations` | **l'hanno tramandata di generazione in generazione** | |
| `kept the popularity … in check` | **tenuto a freno la popolarità** | |
| `submerged underwater` | **rimasta a lungo sott'acqua** | l'inglese è ridondante (`submerged` + `underwater`), l'italiano no |

## 6. Struttura e assenze

- **Zero tab**, **zero segnaposto**: due asserzioni negative scritte.
- **Nessun apice al posto dell'accento**: il controllo tipografico è ristretto alle parole che vogliono l'accento.
- **7 gruppi di nomi ripetuti** (`"Biroo" Atomic Thruster` cinque volte, `"Basrem" Atomic Steering` cinque…): tutti con la
  stessa resa, com'è ovvio quando si copia — ma il controllo c'è, perché il giorno in cui qualcuno «traduce» un nome
  ripetuto deve diventare rosso.
