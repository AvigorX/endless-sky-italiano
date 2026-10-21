# review.md — L273 (`data/korath/korath ships.txt`, righe 95–360)

Registro delle decisioni editoriali del **primo lotto** delle navi Korath: quattro progetti e le storie dei nomi che portano.

## 1. Il carattere del testo

Le schede Korath non descrivono prestazioni: raccontano **perdite**. Ogni nome è un **epitaffio** — una capitana che muore per
un carico di pesce rubato, un ammiraglio che resta al suo posto con le ferite aperte, un'ingegnera che si uccide per non
lasciare i propri segreti al nemico. Il registro è **solennе e duro**, e la resa non lo addolcisce.

## 2. Scelte

| inglese | resa |
|---|---|
| `efficient resource collection became a priority` | **la raccolta efficiente delle risorse divenne una priorità** |
| `World-ships were too precious to risk on dangerous forays` | **Le navi-mondo erano troppo preziose per rischiarle in sortite pericolose** |
| `raiders lacked the cargo capacity` | **ai razziatori mancava la capacità di carico** |
| `named for a respected civilian politician and economist` | **intitolata a un rispettato politico ed economista civile** |
| `the Korath warship of choice for plundering neighboring species` | **la nave da guerra Korath preferita per depredare le specie vicine** |
| `gave her life to ensure her crippled vessel made it back to port` | **diede la vita perché la sua nave menomata riuscisse a tornare in porto** |
| `with its desperately needed cargo of stolen fish` | **con il carico di pesce rubato di cui c'era disperato bisogno** |
| `continues that grim tradition` | **prosegue quella cupa tradizione** |
| `inflating its size beyond similarly armed warships` | **gonfiando le sue dimensioni oltre quelle di navi da guerra con armamento simile** |
| `allows for the ship's easy replacement` | **ne consentono una facile sostituzione** |
| `the era of shortages and desperation caused by a life in exile` | **l'era di penuria e disperazione causata dalla vita in esilio** |
| `building pressure on Korath shipyards to recover some of their ancient prowess` | **ha fatto crescere la pressione sui cantieri Korath perché recuperassero parte della loro antica abilità** |
| `he remained on his flag bridge` | **rimase sul ponte ammiraglia** |
| `the first truly unique warship design the Exiles have fielded since the Exodus` | **il primo progetto di nave da guerra davvero originale che gli Esiliati abbiano schierato dopo l'Esodo** |
| `without needing to double as a habitat or supply ship` | **senza dover servire anche da abitazione o da nave di rifornimento** |
| `must be constructed wholesale at the largest Korath facilities` | **va costruito per intero nelle più grandi strutture Korath** |
| `took their own life to avoid having their secrets captured` | **si tolse la vita per evitare che i suoi segreti finissero in mano a una forza aliena ostile** |
| `a fast and powerful patrol striker` | **un veloce e potente battitore di pattuglia** |
| `rain fire on enemies from afar` | **far piovere fuoco sul nemico da lontano** |

## 3. La traduzione dei nomi di classe navale

| inglese | resa | perché |
|---|---|---|
| `Asteroid Dredging Ship` | **nave dragante per asteroidi** | `dredging` è l'attività estrattiva, non un modello |
| `Raiding Ship` | **nave da razzia** | coerente con «flotte di razzia» già nel corpus |
| `Carried Chaser` | **cacciatore imbarcato** | `carried` = portato dalla nave madre |
| `Chaser` | **cacciatore** | `cacciator-` è già nel corpus 32 volte |
| `world-ship` | **nave-mondo** | forma già presente nel corpus |

`Ik'atilajej` e `Korsmanath A'awoj` restano **invariati**: sono nomi propri di navi Korath, come `Rano'erek`.

## 4. Nomi e apostrofi

`Rano'erek`, `'olofez`, `'nra'ret`: l'apostrofo **iniziale** in `'olofez` e `'nra'ret` è parte del nome, non una citazione.
Il `check.py` verifica che il nome compaia **dove l'inglese lo nomina** (unità 1, 7, 8) — una verifica globale avrebbe
nascosto la perdita del nome dentro una scheda.

## 5. Struttura

| cosa | inglese | italiano |
|---|---|---|
| tab | **4** (unità 2, 4, 6, 8) | **4**, primo carattere |
| virgolette | **0** | **0** |
| apici | **9** (tutti nei nomi) | **15** (`Rano'erek`, `dell'Esilio`, `c'era`, `dell'era`, `l'Esodo`, `'nra'ret` ×2, `'olofez`, `d'emergenza`…) |
| segnaposto | **0** | **0** |

## 6. Cosa resta aperto (dichiarato)

- **Nessuna approvazione**: 8 unità `PENDING`.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Il file è a 8/50**: L274 riparte dalla riga 364 con altri quattro contesti (`'olofez`, `Kas'ik Tek 7`, `Rai'alorej`,
  `Ikatila'ej`).
