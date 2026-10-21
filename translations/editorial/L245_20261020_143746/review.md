# review.md — L245 (`data/hai/hai ships.txt`, righe 901–1516)

Registro delle decisioni editoriali del **terzo lotto** di `hai ships.txt`: cinque schede, quarantuno nomi da copiare,
nessun valore.

## 1. Che cosa si copia e che cosa si traduce

| tipo | unità | trattamento | esempio |
|---|---|---|---|
| `TEXT` | 41 | **copiato** | `"Bondir" Atomic Thruster`, `"Bufaer" Atomic Steering` |
| `DESCRIPTION` | 5 | **tradotto** | le schede |
| `VALUE` | **0** | — | il secondo `VALUE` del file è passato in L244 (`Geocoris`) |

## 2. Le cinque schede

| nave | inglese | resa |
|---|---|---|
| **Sea Scorpion** | `The Sea Scorpion was designed several decades ago to serve as a mobile platform to launch Trackers…` | «La Sea Scorpion fu progettata parecchi decenni fa come piattaforma mobile per lanciare i Tracker…» |
| **Scarab** | `The hard-working cousin to the Lightning Bug, the Scarab has only ever grown in popularity, never declined…` | «Cugina laboriosa della Lightning Bug, la Scarab non ha mai fatto che guadagnare popolarità, senza mai calare…» |
| **Shield Beetle** | `This ship was first built millennia ago, near the end of a more violent time in Hai history…` | «Questa nave fu costruita per la prima volta millenni fa, verso la fine di un periodo più violento della storia Hai…» |
| **Emperor Beetle** (1) | `The Emperor Beetle is a Titan coated with many layers of modern armor…` | «L'Emperor Beetle è un Titan rivestito con molti strati di corazzatura moderna…» |
| **Emperor Beetle** (2) | `\tAs it is not meant to plunder but to lead in glorious battle…` | «\tNon essendo pensata per saccheggiare ma per guidare in una battaglia gloriosa…» |

## 3. Le scelte che non sono ovvie

| punto | decisione | perché |
|---|---|---|
| `Trackers` | **«i Tracker»** | nome dell'arma: resta inglese, l'articolo porta il plurale |
| `Shield Beetles` | **«gli Shield Beetle»** | regola dei plurali: il nome non si pluralizza all'inglese (`Fleas` → «i Flea», L244) |
| `their brethren` | **«i loro fratelli»** | «confratelli» sarebbe da ordine religioso |
| `materially inferior Unfettered` | **«gli Slegati, materialmente inferiori»** | «materialmente» copre sia i materiali sia la sostanza |
| `immaterial to the title` | **«irrilevante ai fini del titolo»** | il «titolo» è il primato di popolarità; «immateriale» in italiano significa altro |
| `the pick for Grasshopper pilots` | **«la scelta dei piloti di Grasshopper»** | |
| `odd job` | **«lavoretto»** | non «lavoro occasionale»: la frase è colloquiale |
| `flagships and trophy ships` | **«ammiraglie e navi trofeo»** | |
| `cargo bays` | **«baie di carico»** | coerente con «baia per droni» (L244) |
| `modern armor` | **«corazzatura moderna»** | |
| `a Titan` | **«un Titan»** | è il troncamento di `Titan Beetle`, usato come nome proprio nella frase |
| `plunder` | **«saccheggiare»** | |

## 4. Il tab e i due paragrafi

La scheda dell'Emperor Beetle è **spezzata in due unità**: la 45 (testo normale) e la 46, che comincia con un **tab** e che
il gioco mostra rientrata. Il tab:

- è verificato come **primo carattere** in inglese **e** in italiano;
- è **uno solo** in tutto il lotto (`sum(tab) == 1`);
- non è un tab di formattazione: è parte del testo, e uno `strip()` lo cancellerebbe senza spostare parole o rapporto.

Il controllo di contenuto («baie di carico» + punto finale) serve a impedire che una traduzione «pulita» passi perdendo la
frase.

## 5. I plurali inglesi

| inglese | italiano | verifica |
|---|---|---|
| `Shield Beetles` | «Shield Beetle» | il plurale **esiste** in inglese (unità 11) e **non esiste** in italiano |
| `Trackers` | «i Tracker» | idem |
| `Fleas` (L244) | «i Flea» | già fissato |

Il controllo guarda **le due direzioni**: se un giorno il sorgente smettesse di usare il plurale, la stringa
`'Shield Beetles' in prosa_inglese` diventerebbe falsa e il test rosso — cosa che un semplice «non c'è in italiano» non
farebbe.

## 6. Struttura e assenze

- **Nessun `VALUE`**: il `Counter` dei tipi non ha la chiave.
- **Zero segnaposto**, **zero tab fuori dall'unità 46**, **zero virgolette nella prosa**.
- **2 apici italiani** in 2 schede (`l'unica`, `L'Emperor`), **0 inglesi**.
- **6 gruppi di nomi ripetuti** (`"Bondir" Atomic Thruster` dodici volte, `"Bufaer" Atomic Steering` otto…), tutti con la
  stessa resa.
