# review.md — L247 (`data/human/syndicate jobs.txt`, righe 19–153)

Registro delle decisioni editoriali del **primo lotto** di `syndicate jobs.txt`: sei lavori, nove battute, un nome di lavoro
da copiare.

## 1. Che cosa si copia e che cosa si traduce

| tipo | unità | trattamento | esempio |
|---|---|---|---|
| `VALUE` | 1 | **copiato** | `Corporate retreat to <planet stopovers>` |
| `DESCRIPTION` | 6 | **tradotto** | la scheda del lavoro |
| `DIALOG` | 9 | **tradotto** | le battute alla consegna |

## 2. Le rese

| unità | inglese | resa |
|---|---|---|
| 1 | `A Syndicate executive needs immediate yet comfortable transportation…` | «Un dirigente del Sindacato ha bisogno di un trasporto immediato ma confortevole…» |
| 2 | `The Syndicate executive rushes off your ship without even a goodbye…` | «Il dirigente del Sindacato si precipita giù dalla tua nave senza nemmeno salutare, con una valigetta elegante in mano. Incassi il pagamento di `<payment>`.» |
| 10 | `The <npc> is about to enter this system…` | «Il `<npc>` sta per entrare in questo sistema. Intercettalo e fai scansioni dettagliate del suo carico…» |
| 12 | `"This will save us months!" you hear someone say…` | «"Ci farà risparmiare mesi!" senti dire da qualcuno in sottofondo mentre chiudi il collegamento audio.» |
| 14 | `…several silent and surprisingly well-dressed men feed the crates of documents onto a conveyor belt…` | «…diversi uomini silenziosi e sorprendentemente ben vestiti infilano le casse di documenti su un nastro trasportatore…» |
| 15 | `Syndicated Systems is looking for intrepid captains… Green Initiative!` | «Syndicated Systems cerca capitani intrepidi… nuova Iniziativa Verde!» |
| 16 | `…drop off the exceptionally smelly shipment of <commodity>…` | «…scarichi il carico di `<commodity>` dall'odore eccezionale in un edificio anonimo…» |

## 3. Le rese fisse riprese dal corpus

| formula inglese | resa | occorrenze nel corpus |
|---|---|---|
| `Payment is <payment>.` | **«Il pagamento è `<payment>`.»** | 56 |
| `You collect your payment of <payment>.` | **«Incassi il pagamento di `<payment>`.»** | 2 (già usata così) |
| `entro il <date>` | articolo davanti a `<date>` | 17+ |
| `<tons> of X` | **«`<tons>` di X»**, senza articolo | 75+ |

La seconda è una scelta: il corpus alterna «Incassi il pagamento di `<payment>`.» e «Riceverai `<payment>`.». Qui si usa la
prima **perché l'inglese dice `collect`**, e la resa esiste già 2 volte.

## 4. Che cosa succede con le missioni «Large»

Le unità **3/7**, **4/8** e **5/9** hanno lo **stesso inglese**: la variante «Large Corporate retreat» riusa la prosa della
missione normale. Una sola resa per coppia, verificata come **famiglia**: se qualcuno ne «migliora» una sola, il `check.py`
diventa rosso. Il `VALUE` della variante (`Corporate retreat to <planet stopovers>`) resta **inglese**: è il nome del
lavoro, non prosa.

## 5. Le scelte che non sono ovvie

| punto | decisione | perché |
|---|---|---|
| `Syndicate` | **Sindacato** | resa consolidata del corpus; **`Syndicated Systems`** è un nome proprio e resta |
| `Green Initiative` | **Iniziativa Verde** | nome di campagna: maiuscole conservate |
| `corporate retreat` | **ritiro aziendale** | |
| `tensile strengths` | **resistenza a trazione** | termine tecnico corretto, non «forza di trazione» |
| `thermodynamic limits` | **limiti termodinamici** | |
| `tromps out of the hatch` | **esce dal portello** | «tromps» è rumoroso e goffo: l'italiano lo rende col verbo nudo, non con un avverbio |
| `exotic corporate retreat` | **esotico ritiro aziendale** | l'ironia sta nell'aggettivo, non nel nome |
| `nondescript building` | **edificio anonimo** | |
| `burly` | **robusto** | |
| `exceptionally smelly` | **dall'odore eccezionale** | «puzzolente» avrebbe perso l'ironia burocratica |
| `well-dressed men` | **uomini … ben vestiti** | |
| `recyclable <commodity>` | **`<commodity>` riciclabili** | il segnaposto resta, l'accordo va sul nome che il motore inserisce |

## 6. Struttura e assenze

- **Zero tab**.
- **2 virgolette**, sole nell'unità 12: la citazione conserva il punto esclamativo **dentro** le virgolette.
- **6 apici inglesi** (`You're`, `team's` ×2, `<npc>'s`, `hadn't`, `You're` di nuovo) → **5 italiani**
  (`un po'`, `nell'ambito`, `dall'odore` ×2). I possessivi **non si replicano**: `<npc>'s cargo` → «il carico del `<npc>`».
- **39 segnaposto**: `<planet stopovers>` (1) è un simbolo intero con uno spazio dentro, `<stopovers>` (2) è un altro.
- **`<tons>` senza articolo** e sempre seguito da «di».
