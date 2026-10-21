# review.md — L310 (`data/korath/korath culture conversations.txt`, righe 26–75)

Registro delle decisioni editoriali del **primo file chiuso in un solo lotto**: una preghiera Korath in 24 battute.

## 1. Perché un file intero in un lotto

La regola finora era **spezzare** i file in lotti da ~500 parole per tenere i test maneggevoli. Qui l'ho **violata di proposito**:

- il file ha **1.295 parole** ma **un solo contesto** — una **conversazione** che va letta come un tutto;
- spezzarla avrebbe reso ogni lotto **dipendente** dall'altro (le scelte della 43–56 sono **risposte** alla 41, che è **risposta**
  alla 33–37);
- il test di un file così può asserire **l'invariante forte**: `0 prima · 27 qui · 0 dopo · copertura 27/27`.

Il costo: un lotto da **1.295 parole** invece di 500. Il beneficio: **un solo passaggio** su una scena che deve avere **un tono
unico**.

## 2. Il registro: seconda persona narrante

Qui il «tu» non è un'**istruzione di gioco** (come i montaggi di L299 o gli avvisi di L307–L309): è la **voce del narratore** che
accompagna il giocatore.

> «**Avvicinandoti** al gruppo, **noti** alcuni bambini Korath…»
> «Solo a quel pensiero **noti** che oggi su `<origin>` non c'è vento di sorta.»
> «**Ti ricordi** della fotografia della tua città natale…»

È il registro di **tutti** i `MISSION_TEXT` del progetto: la scelta era **usarlo**, non evitarlo. Il test verifica che **ci sia**
(«ti serve», «noti», «Ti ricordi») — l'opposto dei lotti di equipaggiamento, dove la seconda persona andava **elencata come
eccezione**.

## 3. La scena: che cosa vede il giocatore

| elemento | che cosa significa |
|---|---|
| i **bambini** che disegnano un **pianeta** grigio-verde | nostalgia di un mondo perduto |
| le **lastre incise** con mappe stellari | il **santuario è un archivio**, non un altare |
| **piuma, conchiglia, fiore** attorno a **una candela** | tre **reliquie di mondi vivi** |
| la **candela** che brucia «da ore» e **nessun vento** | il **miracolo** che tiene in piedi la preghiera |
| le **braccia a spirale** con un punto **protetto da una barriera** | `Far'en Lai`, un mondo **ancora vivo** e **nascosto** |

La resa conserva **l'ambiguità**: il testo non dice se la candela sia un miracolo o una **manutenzione continua** («forse i Korath
la riaccendono ogni volta che una raffica la spegne»), e la traduzione **non risolve** il dubbio.

## 4. Le quattro offerte: una **scala sociale**

| scelta | risposta dei Korath |
|---|---|
| **100 crediti** | un **cenno di approvazione** |
| **10.000 crediti** | **inchini leggeri** di più Korath |
| **10.000.000 crediti** | **shock**: le mani alzate, «sembra raggiante» |
| **una fotografia di casa** | il **vecchio** la guarda a lungo, poi **tutti** alzano le palme |

La **foto vale più dei soldi**: è l'unica offerta che porta il vecchio a **riconoscere** il contributo del giocatore con un gesto
collettivo. La resa mantiene **tre gradi** distinti («con approvazione», «leggermente», «sconvolti più che infastiditi»).

## 5. `UI_LABEL`: tre etichette che non si traducono

| riga | inglese | italiano |
|---|---|---|
| 60 | `small credits` | **`small credits`** |
| 65 | `medium credits` | **`medium credits`** |
| 70 | `large credits` | **`large credits`** |

Sono le **etichette dei pulsanti di scelta** — l'interfaccia le mostra accanto alle offerte. Copiate: il giocatore le collega
mentalmente alle **cifre** (100 / 10.000 / 10.000.000), e tradurle avrebbe introdotto una **seconda nomenclatura** per la stessa
scelta.

## 6. Scelte di resa

| inglese | resa |
|---|---|
| `The gloomy feel of the local spaceport` | **L'atmosfera cupa dello spazioporto locale** |
| `as if they all had their attention elsewhere` | **come se avessero tutti l'attenzione altrove** |
| `a large, blackened side of an abandoned building` | **un grande lato annerito di un edificio abbandonato** |
| `scratching it carefully with what must be something akin to crayons` | **incidendolo con cura con qualcosa di simile a pastelli** |
| `a beige or brownish circle, with some shy spots of blue` | **un cerchio beige o brunastro, con qualche timida macchia di blu** |
| `contrasted by the onyx background of the building wall` | **sul fondo di onice del muro dell'edificio** |
| `a dusty canvas that's not large enough` | **una tela impolverata che non basta a coprire** |
| `a plethora of personal belongings` | **una miriade di oggetti personali** |
| `large fragments of cracked eggshells` | **grandi frammenti di gusci d'uovo incrinati** |
| `makes a point to pass by the shrine` | **si fa un punto di passare dal santuario** |
| `slabs, with various scratch marks over them` | **lastre … coperte di vari segni incisi** |
| `a mysteriously beautiful flower` | **un fiore di misteriosa bellezza** |
| `a shivering … agonizing, bark-like yelp in a frayed voice` | **un guaito agonizzante, simile a un latrato, con una voce roca** |
| `Standing at navel height` | **A un'altezza da ombelico** |
| `many spiral arms in white` | **molte braccia a spirale … in bianco** |
| `converging in what looks like a large maw at the center` | **che convergono in quella che sembra una grande fauce al centro** |
| `as if shielding it from the center of her spiral map` | **quasi a volerla proteggere dal centro della sua mappa a spirale** |
| `as if in disbelief of what she had just drawn herself` | **come se non credesse a ciò che ha appena disegnato lei stessa** |
| `her voice cracking slightly` | **con la voce che le si incrina un poco** |
| `what looks to be some form of communication device` | **quello che sembra una sorta di dispositivo di comunicazione** |
| `as if wondering if you would follow the gesture` | **come se si chiedesse se seguirai quel gesto** |
| `you begin to wonder if you somehow offended them` | **cominci a chiederti se in qualche modo li hai offesi** |
| `seems to nod slightly` | **sembra accennare un cenno del capo** |
| `looking thoroughly impressed` | **con un'espressione profondamente ammirata** |
| `dropping down rather noisily` | **cadono con un rumore piuttosto forte** |
| `seem in shock rather than disturbed` | **sembrano sconvolti più che infastiditi** |
| `who seems to be beaming` | **sembra raggiante** |
| `as if bidding you farewell` | **come per un congedo** |

## 7. Struttura

| cosa | inglese | italiano |
|---|---|---|
| tab | **23** | **23** |
| virgolette | **14** (6 unità) | **14** |
| segnaposto | **3** | **3** |
| alternative | **0** | **0** |
| apici | **10** | **12** |
| `UI_LABEL` | **3** | **3**, copiati |

## 8. Cosa resta aperto (dichiarato)

- **Nessuna approvazione**: 27 unità `PENDING`; **nessuna revisione umana**.
- **Il file è chiuso a 27/27** in staging: **trentesimo file completo**, **89** su 167.
- **Prossimo file**: `data/bunrodea/bunrodea outfits.txt` — righe **25–130**, **12 unità** (tutte `DESCRIPTION`), **480 parole**,
  **8 contesti**, **4 tab** (54, 70, 114, 130), **0 virgolette**, **1 apice**. Il file ha **33 unità** (32 `DESCRIPTION` + 1
  `VALUE`): la prima finestra è di **otto contesti**, quasi tutti doppi.
