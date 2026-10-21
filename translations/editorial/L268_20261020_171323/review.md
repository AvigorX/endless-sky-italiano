# review.md — L268 (`data/human/engines.txt`, righe 195–323)

Registro delle decisioni editoriali del **secondo lotto** dei motori umani: propulsori ionici grossi, sei sistemi di
sterzata e il primo **propulsore inverso**.

## 1. La struttura del lotto

Sei blocchi di due schede: la scheda del **modello** (senza tab) e la **nota ionica** (con tab), che si ripete identica. Il
modello X4700 chiude L267 con una sola unità e qui ne ha una (la nota ionica), quindi il primo blocco è monco — è la
conseguenza del confine di lotto, e il `check.py` verifica la mappa esatta (195-195, poi 212-213, …).

## 2. Scelte

| inglese | resa | nota |
|---|---|---|
| `intended for only the largest of capital ships` | **destinato solo alle più grandi navi capitali** | |
| `considered little more than a publicity stunt` | **considerati poco più che un colpo pubblicitario** | |
| `smallest set of steering thrusters` | **set di propulsori di sterzata più piccolo** | `steering` → «sterzata» |
| `tiny, pilotless drones` | **droni minuscoli e senza pilota** | |
| `some extra outfit space` | **un po' di spazio extra per gli equipaggiamenti** | `outfit` → «equipaggiamenti» |
| `the results are invariably disappointing` | **i risultati sono invariabilmente deludenti** | |
| `other small spacecraft` | **altri piccoli vascelli spaziali** | |
| `when maneuverability is not needed` | **quando la manovrabilità non serve** | |
| `enough turning force to lend agility` | **abbastanza forza di rotazione da dare agilità** | |
| `the plasma-drive alternatives` | **le alternative a propulsione al plasma** | |
| `quick steering is seldom a requirement in freighter design` | **una sterzata rapida è raramente un requisito nella progettazione dei mercantili** | |
| `so large and powerful that only a handful of ships can install it` | **così grande e potente che solo una manciata di navi può installarlo** | |
| `produced in small numbers` | **prodotto in piccole quantità** | |
| `ships turn around so that they can use their main thrusters for deceleration` | **le navi si girano, così da poter usare i propulsori principali per decelerare** | |
| `too ungainly for such maneuvers to be convenient` | **troppo goffe perché simili manovre siano comode** | |
| `sensitive cargo that must not be being swung around quickly` | **carichi delicati che non vanno fatti ruotare in fretta** | il sorgente è sgrammaticato: reso il **senso** |
| `apply thrust smoothly backwards` | **applicare la spinta dolcemente all'indietro** | |
| `must be facing forwards … installed in the weapon section` | **deve essere rivolto in avanti … nella sezione delle armi** | |

L'unità 14 ha una frase **sgrammaticata** in inglese (`must not be being swung around quickly`): la resa non la imita, ne
conserva il significato — il carico non va fatto ruotare in fretta.

## 3. Il propulsore inverso

`reverse thruster` non esisteva nel corpus. La resa **«propulsore inverso»** è coerente con `thruster` → «propulsore» e con
la funzione (spinta **all'indietro**), e la scheda conserva il dettaglio di montaggio: **sezione delle armi**, non dei
motori. È il tipo di informazione che, se persa, rende l'equipaggiamento inutilizzabile nel gioco.

## 4. Terminologia

Confermata da L267 e dal corpus: **propulsore**, **spinta**, **sterzata**, **navi capitali**, **mercantili**, **caccia**,
**droni**, **equipaggiamenti**, **motori al plasma**. Il `check.py` vieta che le parole inglesi chiave (`thruster`,
`steering`, `reverse`, `warship`, `freighter`) compaiano nelle rese.

## 5. Struttura

| cosa | inglese | italiano |
|---|---|---|
| tab | **8** | **8**, primo carattere |
| virgolette | **0** | **0** |
| apici | **0** | **6** (`all'epoca`, `un po'`, `L'X4200`, `L'X5200`, `l'uso`, `all'indietro`) |
| segnaposto | **0** | **0** |

## 6. Cosa resta aperto (dichiarato)

- **Nessuna approvazione**: 15 unità `PENDING`.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Il file è a 27/61**: L269 riparte dalla riga 342 con i propulsori e le sterzate **al plasma**.
