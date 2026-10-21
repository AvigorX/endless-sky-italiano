# review.md — L319 (`data/korath/korath weapons.txt`, righe 615–1222)

Registro delle decisioni editoriali del lotto che **chiude** le armi Korath.

## 1. Il file finisce spiegando **come funzionano** le armi, non come si usano

Le prime schede (L318) raccontavano **tattiche**: tirare, respingere, bloccare. Queste raccontano **meccanismi**, e quasi tutte hanno
la forma *«fa X, ma a prezzo di Y»*:

| arma | il guadagno | il prezzo |
|---|---|---|
| `Cluster Mine` | nube di mine immobili, danni considerevoli | **se la colpisci prima che si dispieghi**, i danni **crollano** |
| `Shield Disruptor` | scafo danneggiabile **con gli scudi attivi** | **da sola** fa pochissimi danni allo scafo |
| `Husk-Slice` | taglia la corazzatura «come carta» | **inefficace contro gli scudi** |
| `Langrage` | munizioni **improvvisate** (rottami, spazzatura) | a distanza ravvicinata **solo respinge**; la nube arriva dopo |
| `Firelight` | missile pronto al lancio | reattore **terribilmente inefficiente**, appena attivo |
| `Microbot Grinder` | **scompone in molecole** | nessuno: è pura minaccia |
| `Firestorm Battery` | esplosione che **respinge e fonde** | **nessuna** schermatura né sicurazza |

La resa conserva **ogni «ma»** con lo stesso peso dell'inglese: «Da sole, però, fanno pochissimi danni», «Sebbene meno raffinato…»,
«Benché terribilmente inefficiente…». Togliere questi incisi avrebbe reso le armi **migliori di quanto siano**, e il giocatore avrebbe
comprato sulla base di un testo falso.

## 2. `langrage` resta `langrage`

Il termine inglese indica la **ghiaia usata come mitraglia** nelle battaglie navali. In italiano non esiste un equivalente
riconoscibile («ghiaino» è arcaico e oscuro). Il testo lo usa già come **nome proprio dell'arma** (`Langrage Hyper-Heaver`) e come
**sostanza** nella seconda unità («la langrage lanciata si limita a respingere»): la resa mantiene **il nome** e lascia che sia il
contesto a spiegarlo — cosa che il testo fa benissimo («converte rottami metallici … in un campo di detriti»).

## 3. `Firestorm` e `Firelight`: due generazioni, e la citazione incrociata

| riga | che cosa dice |
|---|---|
| 1049 | «gli ingegneri Korath hanno potuto creare il **Firelight** riducendo ulteriormente l'elemento reattore» — **deriva dal Firestorm** |
| 1221 | «**meno raffinato** della più recente versione **Firelight**» — il Firestorm è la **vecchia** |

Il test verifica le **due citazioni** in entrambe le direzioni. È l'unico modo per non confondere due famiglie i cui nomi, in
italiano, restano **identici all'inglese** (come devono: sono etichette d'emporio).

E c'è un dettaglio **fisico** che le distingue: il `Firestorm` è «**completamente privo** del suo involucro protettivo e dei
dispositivi di sicurezza», il `Firelight` invece può permettersi «la schermatura completa del reattore» **perché è piccolo**. La resa
tiene il nesso: la **miniaturizzazione** è ciò che **permette** la sicurezza.

## 4. La scala delle celle e dei reattori (fuori dal lotto, ma nel file)

Il file chiude con una **seconda famiglia** che non è in questo lotto ma che convive nello stesso documento: `Biochemical Cell`,
`Red/Yellow/White/Blue Sun Reactor`, `Bright Cloud`/`Dark Storm Shielding`. Non le ho toccate; il contratto di L320 le prenderà.

## 5. La nota dei rifornimenti, tre volte

| riga | contesto | posizione |
|---|---|---|
| 659 | `Cluster Mine Layer` | nota del lanciatore |
| 1051 | `Firelight Missile Bank` | **seconda** tab dello stesso contesto (dopo la nota tecnica) |
| 1222 | `Firestorm Battery` | ultima riga del file |

La resa è quella **di maggioranza** del corpus (16 su 26), già usata in L318. `check.py` la confronta con le altre tre del lotto e con
la stringa attesa; `verify.py` **cerca la stringa italiana** in tutti gli altri lotti e pretende almeno **due** occorrenze. Due
meccanismi diversi per la stessa garanzia.

## 6. Scelte di resa

| inglese | resa |
|---|---|
| `store extra ammunition` | **immagazzinare munizioni supplementari** |
| `split into a cloud of stationary mines` | **si aprono in una nube di mine immobili** |
| `if a ship crashes into them` | **se una nave ci si schianta contro** |
| `before it has a chance to deploy` | **prima che abbia il tempo di dispiegarsi** |
| `allowing a ship's hull to be damaged even when shields are up` | **permettono di danneggiarne lo scafo anche quando gli scudi sono attivi** |
| `cuts through hull armor like it's made of paper` | **taglia la corazzatura dello scafo come se fosse carta** |
| `a tightly focused energy beam` | **un raggio di energia molto concentrato** |
| `re-engineered this ancient, robust design` | **riprogettarono questo antico e robusto modello** |
| `the mild shield disruption effect` | **il lieve effetto di disturbo sugli scudi** |
| `a cloud of fighter-sized miners` | **una nube di minatori delle dimensioni di un caccia** |
| `raise the use of improvised ammunition to a fine art` | **elevano l'uso di munizioni improvvisate a una forma d'arte** |
| `the launch field collapses` | **il campo di lancio collassa** |
| `it is rent into a rapidly-expanding cloud of deadly projectiles` | **si lacera in una nube di proiettili letali in rapida espansione** |
| `must be kept minimally active` | **deve restare attivo al minimo** |
| `a trickle of power` | **un filo di energia** |
| `full reactor shielding or safety interlocks` | **la schermatura completa del reattore né i dispositivi di sicurezza** |
| `scaling down the reactor element to fit in a missile casing` | **riducendo ulteriormente l'elemento reattore per farlo stare in un involucro di missile** |
| `a seemingly omnicidal swarm of microbots` | **uno sciame di microbot apparentemente omicida** |
| `tear apart the hulls of heavy warships` | **squarciare lo scafo di una nave da guerra pesante** |
| `any captain would be foolish to fly within reach of` | **un capitano sarebbe sciocco a volare a portata** |
| `massive in both size and destructive capability` | **enorme per dimensioni e capacità distruttiva** |
| `a large cage-like rack` | **un grande rack a gabbia** |
| `augmented … completely stripped of its protective casing` | **potenziato … del tutto privo del suo involucro protettivo** |
| `generate a tremendous explosion of heat and force` | **genera un'esplosione tremenda di calore e forza** |
| `will even melt their hulls` | **arriva a fonderne lo scafo** |

## 7. Struttura

| cosa | inglese | italiano |
|---|---|---|
| tab | **5** (659, 930, 1050, 1051, 1222) | **5** |
| virgolette | **0** | **0** |
| segnaposto / alternative | **0 / 0** | **0 / 0** |
| apici | **4** su 3 unità (743 ×2, 781, 1159) | **11** |

## 8. Cosa resta aperto (dichiarato)

- **Nessuna approvazione**: 22 unità `PENDING`; **nessuna revisione umana**.
- **Il file è chiuso a 39/39** in staging: **trentaquattresimo file completo**, **93** su 167.
- **Prossimo file**: `data/wanderer/wanderer outfits.txt` — righe **40–450**, **18 unità** (tutte `DESCRIPTION`), **478 parole**,
  **17 contesti**, **1 tab** (271, la nota dei rifornimenti **di nuovo**), **0 virgolette**, **2 apici** (436, 450). Il lotto attraversa
  **raggi** (`Sunbeam`, `Moonbeam`), **missili** (`Thunderhead`), **reattori** (`Red/Yellow/White/Blue Sun`) e **scudi**
  (`Bright Cloud`, `Dark Storm`).
