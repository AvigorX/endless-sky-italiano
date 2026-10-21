# review.md — L288 (`data/gegno/gegno ships.txt`, righe 725–1192)

Registro delle decisioni editoriali del **terzo lotto** delle navi Gegno: la flotta **Scin** entra in scena.

## 1. Che cosa raccontano queste sette navi

| nave | riga | ruolo | nota |
|---|---|---|---|
| `Rhyolite` | 725 | intercettore | **prototipo**, pochi esemplari, pilotati da «una manciata di guerrieri Vi» |
| `Eclogite` | 776 | cannoniera | «armata fino ai denti», **mordi-e-fuggi**, manovrabilità che le navi grandi Vi non hanno |
| `Diorite` | 832 | cannoniera leggera | nasce dal concetto dell'`Eclogite`, cantiere diverso, «tiene la mira» su navi della sua taglia |
| `Hornfel` | 917 | multiruolo | **bestia da soma**, la più **configurabile**, con punti di attacco per capsule da carico |
| `Gneiss` | 983 + 1061–1062 | nave da battaglia | «vera spada e vero scudo», tre supporti per `Ballistic Cannons`, **lenta** |
| `Granulite` | 1149 | trasporto | discendente delle **navi generazionali**, porta centinaia di Vi e rifornimenti |
| `Halite` | 1192 | velivolo sperimentale | dei **Gegno Scin**: primo velivolo da combattimento, primi **impulsi** e **scudi** |

## 2. La struttura militare che emerge

Il lotto disegna una **dottrina**, non solo delle navi: i Vi costruiscono **lunghi vascelli da battaglia** (uno «stile»), ma
**cantieri diversi** competono (l'`Eclogite` viene da un altro cantiere); la flotta ha un **multiruolo** (`Hornfel`), un
**picchiatore** (`Gneiss`) e una **nave di rifornimento** (`Granulite`). La resa conserva i **paragoni militari** del testo:
`workhorse` → **bestia da soma**, `sword and shield` → **spada e scudo**, `hit-and-run` → **mordi-e-fuggi**.

Il `Halite` cambia voce: è **Scin**, ed è un **esperimento** («piattaforma di prova sperimentale riuscita»), non una nave
schierata. Il testo dice «quasi metà dello scafo è dedicata a questi nuovi sviluppi»: la resa lo lascia **ammirare** senza
commento.

## 3. Il nome che non si traduce — e che va distinto dai testi

`Gneiss` compare **tre volte** nello stesso contesto:

| riga | tipo | resa |
|---|---|---|
| 983 | `VALUE` | **`Gneiss`** (copiato) |
| 1061 | `DESCRIPTION` | «Le navi da battaglia Gneiss sono la vera spada e il vero scudo…» |
| 1062 | `DESCRIPTION` | «Purtroppo, in cambio di una potenza di fuoco enorme…» |

La tentazione è tradurre anche la `VALUE` («Gneiss» è un nome di roccia, e in italiano si potrebbe dire «gneiss»): sarebbe un
errore, perché è il **nome del modello** che il gioco stampa nelle liste. Il test verifica l'identità **e la coerenza** con le due
descrizioni.

## 4. `Hornfels` plurale → `Hornfel` invariato

L'inglese usa il plurale regolare (`Hornfels are the workhorse…`, `Other variants of Hornfels…`). In italiano il nome resta
**invariato** e il plurale lo porta l'articolo: «**Gli** Hornfel sono…», «varianti **degli** Hornfel». Il test rifiuta
`Hornfels` nella resa — è la stessa regola dei `Dolomite` in L286 e degli `Schist` in L287.

## 5. Il confine del `Halite`

La riga 1192 è **la prima metà** di una descrizione che continua (1193–1194). Il `REPORT` del lotto lo dice, e il `verify.py`
verifica che la prima unità dopo la 1192 sia **ancora** `ship:Halite`. Un lotto che avesse «chiuso» la scheda qui avrebbe
prodotto un testo **spezzato** dallo staging, non dal gioco.

## 6. Scelte di resa

| inglese | resa |
|---|---|
| `Only a few have been produced` | **Ne sono stati prodotti solo pochi esemplari** |
| `either testing the vessel or owning one privately` | **che stanno collaudando il vascello o ne possiedono uno privatamente** |
| `the Vi's larger ships lack` | **che le navi più grandi dei Vi non hanno** |
| `after adjusting its position for another run` | **prima di aggiustare la posizione per un altro passaggio** |
| `This multi-role function is extremely valued` | **Questa funzione multiruolo è estremamente apprezzata** |
| `like other Gegno Scin ships` | (in L289) |
| `almost half the hull is dedicated to these new developments` | **quasi metà dello scafo è dedicata a questi nuovi sviluppi** |

## 7. Cosa resta aperto (dichiarato)

- **Nessuna approvazione**: 9 unità `PENDING`; **nessuna revisione umana**.
- **Il file è a 25/37**: L289 sarà il lotto **terminale** — righe **1193–1616**, **12 unità** (tutte `DESCRIPTION`), **647
  parole**, **8 contesti** (`Halite`, `Mica`, `Coesite`, `Tridymite`, `Felsic`, `Feldspar`, `Epidote`, `Kyanite`), **quattro
  coppie consecutive** (1193–1194, 1480–1481, 1547–1548, 1615–1616), e chiuderà il file a **37/37**.
