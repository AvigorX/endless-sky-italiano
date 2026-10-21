# review.md — L244 (`data/hai/hai ships.txt`, righe 362–885)

Registro delle decisioni editoriali del **secondo lotto** di `hai ships.txt`: sei schede, trentasei nomi da copiare, una
nota rientrata.

## 1. Che cosa si copia e che cosa si traduce

| tipo | unità | trattamento | esempio |
|---|---|---|---|
| `VALUE` | 1 | **copiato** | `Geocoris` |
| `TEXT` | 36 | **copiato** | `"Benga" Atomic Thruster`, `"Biroo" Reverse Thruster` |
| `DESCRIPTION` | 8 | **tradotto** | le schede |

## 2. La nota col tab

```
EN   \tDrones do not come equipped with a hyperdrive. You cannot carry a drone unless you have a ship in your fleet with a drone bay.
IT   \tI droni non escono equipaggiati con un iperpropulsore. Non puoi trasportare un drone se non hai nella tua flotta una nave con una baia per droni.
```

Il tab **non è indentazione del file**: è il rientro con cui il gioco impagina la nota sotto la scheda. Va conservato come
**primo carattere** e verificato **per unità**: uno `strip()` lo elimina senza far cambiare né le parole né il rapporto.
La resa riprende il fraseggio già presente nel corpus («…una nave con una baia per droni», 7 occorrenze), e `hyperdrive`
→ **iperpropulsore** come fissato in L237.

## 3. Le cinque schede

| nave | inglese | resa |
|---|---|---|
| **Flea** | `This combat drone is built to amplify the strength of any combat force for as few credits as possible…` | «Questo drone da combattimento è costruito per amplificare la potenza di qualunque forza da combattimento con il minor numero di crediti possibile…» |
| **Geocoris** | `After large human freighters began to out-compete traditionally smaller Hai ships…` | «Dopo che i grandi mercantili umani cominciarono a superare le tradizionalmente più piccole navi Hai…» |
| **Grasshopper** | `Designed by the Hai to serve as a fast reconnaissance craft…` | «Progettata dagli Hai come veloce nave da ricognizione…» |
| **Lightning Bug** | `The Lightning Bug, as with many insects, works best in a swarm…` | «Come molti insetti, la Lightning Bug dà il meglio di sé in sciame…» |
| **Pond Strider** | `…the Hai have cleverly innovated the Skipper Railgun to make the Pond Strider and Fleas into very efficient combat support…` | «…gli Hai hanno abilmente rielaborato la Skipper Railgun per rendere il Pond Strider e i Flea un supporto di combattimento molto efficiente…» |

## 4. Le scelte che non sono ovvie

| punto | decisione | perché |
|---|---|---|
| `ramscoop` | **invariato** | è il nome di un equipaggiamento del gioco: il corpus lo lascia inglese (50 occorrenze) |
| `collection gills` | **branchie di raccolta** | metafora dell'organo biologico che amplifica il ramscoop naturale |
| `Skipper Railgun` | **invariato** | nome proprio dell'arma; si traduce solo `Ion Cannon` → «cannone ionico» |
| `debilitating ion damage` | **danni ionici debilitanti** | «danni ionici» è già la resa del corpus (22 occorrenze) |
| `stock-fitted` / `stock` | **di serie** | resa fissata in L243 |
| `convoy escort` | **scorta ai convogli** | |
| `Unfettered` | **Slegati** | lessico consolidato del corpus (302 occorrenze) |
| `hull repair technology` | **tecnologia di riparazione dello scafo** | già nel corpus, e la resa va ripresa identica |
| `Fleas` (plurale) | **i Flea** | il nome proprio non si pluralizza all'inglese; il drone è maschile, come nel resto della scheda |
| `kite its targets` | **tenere a distanza i bersagli** | l'inglese usa il gergo dei videogiochi; l'italiano descrive la manovra |
| `these sensor-laden exploration vessels` | **queste navi da esplorazione cariche di sensori** | `sensor-laden` non ha un equivalente idiomatico: «cariche di sensori» è la soluzione più corta che regge |

## 5. Il plurale dei nomi di nave

Il Pond Strider parla di **`Fleas`**, il drone della scheda precedente. In italiano il nome resta **Flea** e il numero lo
porta l'articolo: «il Pond Strider e **i Flea**». Il `check.py` asserisce che `Fleas` **non compaia** nella traduzione, così
la regola non si perde per distrazione nella scheda successiva.

## 6. Struttura e assenze

- **Zero segnaposto**: asserzione negativa scritta.
- **Zero tab fuori dall'unità 3**: `sum(tab) == 1`.
- **Zero virgolette nella prosa**: in questo lotto le virgolette sono **solo** nei nomi (a differenza di L243, dove il
  motto della Cicada ne usava due).
- **3 apici italiani** in 3 schede diverse (`l'umanità`, `un'epoca`, `l'autonomia`), **0 inglesi**: la differenza è
  elencata per unità.
- **Nessun `'s`** in nessuna delle 45 unità.
