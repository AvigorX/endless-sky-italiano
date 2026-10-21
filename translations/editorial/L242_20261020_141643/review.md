# review.md — L242 (`data/successors/successor jobs.txt`, righe 306–802)

Registro delle decisioni editoriali del **secondo e ultimo lotto** di `successor jobs.txt`: diciannove lavori, quattordici
formule, un segnaposto nuovo.

## 1. Le quattordici formule

| inglese | resa | n. |
|---|---|---|
| `A courier is needed for <tons> of supplies from <origin> to <planet>. You will be paid <payment> on delivery.` | **Serve un corriere per `<tons>` di provviste da `<origin>` a `<planet>`. Riceverai `<payment>` alla consegna.** | 4 |
| `These <bunks> workers are looking for jobs on <destination> and will pay you <payment> to take them there by <date>.` | **Questi `<bunks>` operai cercano lavoro su `<destination>` e ti pagheranno `<payment>` per portarli lì entro il `<date>`.** | 2 |
| `A courier is needed for a rush shipment of <tons> of supplies … by <date>. You will be paid <payment> on delivery.` | **Serve un corriere per una spedizione urgente di `<tons>` di provviste … entro il `<date>`. Riceverai `<payment>` alla consegna.** | 2 |
| `These <bunks> students are returning to their university on <destination> …` | **Questi `<bunks>` studenti tornano alla loro università su `<destination>` …** | 1 |
| `A courier is needed to transport <cargo> from <origin> to <planet>. …` | **Serve un corriere per trasportare `<cargo>` da `<origin>` a `<planet>`. …** | 1 |
| `A courier is needed to deliver <tons> of aid supplies … by <date>. …` | **Serve un corriere per consegnare `<tons>` di provviste di soccorso … entro il `<date>`. …** | 1 |
| `After a minor earthquake on <planet>, <tons> of seismic stabilizers have been requested for delivery by <date>. You will be paid <payment>.` | **Dopo un lieve terremoto su `<planet>`, sono stati richiesti `<tons>` di stabilizzatori sismici per la consegna entro il `<date>`. Riceverai `<payment>`.** | 1 |
| `Confidential data stored on <tons> of databanks needs to get from <origin> to <planet> by <date>. …` | **Dati riservati conservati su `<tons>` di banche dati devono arrivare da `<origin>` a `<planet>` entro il `<date>`. …** | 1 |
| `These <bunks> researchers studying the Predecessors will pay you <payment> to bring them to <stopovers> and return them here.` | **Questi `<bunks>` ricercatori che studiano i Predecessori ti pagheranno `<payment>` per portarli su `<stopovers>` e riportarli qui.** | 1 |
| `This large research team of <bunks> that is studying the Predecessors …` | **Questa grande squadra di ricerca di `<bunks>` persone che studia i Predecessori ti pagherà `<payment>` per portarla …** | 1 |
| `These <bunks> researchers studying <stopovers> will pay you <payment> to transport them there for research and return them home.` | **Questi `<bunks>` ricercatori che studiano `<stopovers>` ti pagheranno `<payment>` per trasportarli lì per le ricerche e riportarli a casa.** | 1 |
| `These <bunks> researchers going to a symposium on <destination> … before it starts on <date>.` | **Questi `<bunks>` ricercatori diretti a un simposio su `<destination>` ti pagheranno `<payment>` per portarli lì prima che inizi, il `<date>`.** | 1 |
| `The Old Houses require <tons> of high-grade supplies …` | **Le Vecchie Casate richiedono che `<tons>` di provviste di alta qualità siano trasportate …** | 1 |
| `The New Houses require <tons> of high-grade supplies …` | **Le Nuove Casate richiedono che `<tons>` di provviste di alta qualità siano trasportate …** | 1 |

La quarta e la quattordicesima sono **la stessa frase con due soggetti**: `Old Houses` / `New Houses` cambiano il nome
dell'istituzione, non la formula. Sono due `DESCRIPTION` distinte e due rese distinte, per un carattere.

## 2. `<tons>`: si usa e non si tocca

`<tons>` è una **quantità prodotta dal motore** (`11 tons`), e in italiano non si può anteporre un articolo né far
concordare un aggettivo: la frase si costruisce **intorno** al segnaposto.

| tentazione | perché è sbagliata | forma scelta |
|---|---|---|
| «le `<tons>` di provviste» | il valore può essere «1 ton»: l'articolo femminile plurale presuppone una forma che non conosciamo | «`<tons>` di provviste» |
| «circa `<tons>` di…» | aggiunge una approssimazione che l'inglese non ha | niente avverbi davanti |
| «`<tons>` di provviste» con l'unità tradotta | l'unità è dentro il token, non nel testo | dichiarato: **l'unità resta inglese**, come `<destination>` che contiene «in the Sol system» |

Il `check.py` vieta `il/lo/la/i/gli/le/un/uno/una` davanti a `<tons>`: è un controllo che può fallire, quindi esiste.

## 3. Vecchie e Nuove Casate

`Old Houses` → **Vecchie Casate** e `New Houses` → **Nuove Casate**, con la maiuscola: sono istituzioni (decisione 164),
non descrizioni. Nei `VALUE` restano inglesi (`Old Houses courier to <planet>`, `New Houses courier to <planet>`), perché
il `VALUE` è il nome del lavoro e si copia.

Il lotto mette le due richieste una accanto all'altra (righe 774 e 802): chi traduce la seconda «a memoria» rischia di
lasciare «New Houses» nella prosa, e il `check.py` lo intercetta perché cerca la stringa inglese **dentro il testo
italiano**.

## 4. Lessico

| inglese | resa | nota |
|---|---|---|
| `a courier is needed` | **serve un corriere** | impersonale, non «è necessario un corriere»: il registro è da bacheca |
| `you will be paid <payment> on delivery` | **riceverai `<payment>` alla consegna** | «Riceverai» 23 precedenti nel corpus |
| `high-grade supplies` | **provviste di alta qualità** | |
| `aid supplies` | **provviste di soccorso** | |
| `seismic stabilizers` | **stabilizzatori sismici** | nessun precedente: composto trasparente |
| `minor earthquake` | **lieve terremoto** | |
| `confidential data` | **dati riservati** | |
| `databanks` | **banche dati** | forma dominante (7) |
| `researchers studying the Predecessors` | **ricercatori che studiano i Predecessori** | «Predecessori» 81 |
| `research team of <bunks>` | **squadra di ricerca di `<bunks>` persone** | «persone» rende il numero senza genere |
| `symposium` | **simposio** | 2 precedenti |
| `before it starts on <date>` | **prima che inizi, il `<date>`** | la virgola evita «inizi il 12 marzo» che suonerebbe come un inizio del simposio il giorno detto |

## 5. Struttura e assenze

- **Zero tab, zero virgolette, zero apici**: tre asserzioni negative scritte.
- **Diciannove contesti da due unità**, nessuno spezzato fra lotti.
- **Nessuna ripetizione anomala**: le uniche copie sono le quattro «provviste» e le due «spedizioni urgenti», che il
  sorgente ripete davvero.
- **Il file è chiuso**: 124/124, `max(line) = 802`.
