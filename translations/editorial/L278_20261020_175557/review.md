# review.md — L278 (`data/human/kestrel.txt`, righe 15–54)

Registro delle decisioni editoriali del **primo lotto** del file della Kestrel: l'incontro che **avvia** la missione di
collaudo.

## 1. Chi parla, e come

**Charles Atinoda** è un uomo che parla molto di sé: si presenta con il titolo («progettista capo delle astronavi della
Tarazed Corporation»), racconta la propria **crisi personale**, la propria **visione**, e il proprio **progetto**. Il testo
oscilla fra il solenne («Le tue imprese in battaglia sono famose») e il ridicolo («un Welsh Corgi che entrava in un
computer»).

La resa conserva **entrambi**: appiattire l'oscillazione avrebbe reso la scena una normale offerta di lavoro.

## 2. Scelte

| inglese | resa |
|---|---|
| `a man recognizes you` | **un uomo ti riconosce** |
| `It's an honor to meet you. Your exploits in battle are well known.` | **È un onore conoscerti. Le tue imprese in battaglia sono famose.** |
| `He picks up his drink and walks over to sit next to you` | **Prende il suo drink e viene a sedersi accanto a te** |
| `would you be willing to help us test out a new warship?` | **saresti disposto ad aiutarci a collaudare una nuova nave da guerra?** |
| `in a time of deep personal crisis` | **in un momento di profonda crisi personale** |
| `with nothing in my backpack but a change of clothes, a canteen of water, and a few boxes of emergency rations` | **con niente nello zaino se non un cambio di vestiti, una borraccia d'acqua e qualche scatola di razioni d'emergenza** |
| `An anarchist commune on one of the fringe worlds took me in` | **Una comune anarchica su uno dei mondi di frontiera mi accolse** |
| `the village elder, sensing my inner turmoil` | **l'anziano del villaggio, intuendo il mio tumulto interiore** |
| `a vision quest in their sweat lodge` | **una ricerca di visione nella loro capanna del sudore** |
| `I saw a sword made of light. I saw a blue sun.` | **Vidi una spada fatta di luce. Vidi un sole blu.** |
| `a Welsh Corgi hacking into a computer?` | **un Welsh Corgi che entrava in un computer?** |
| `Were there illicit substances involved?` | **C'erano sostanze illecite in questa ricerca di visione?** |
| `more graceful and elegant than any I had ever designed` | **più aggraziata ed elegante di qualsiasi cosa avessi mai progettato** |
| `an alien vessel with a mottled red hull` | **un vascello alieno dallo scafo rosso maculato** |
| `I hitched a ride back to Wayfarer, begged for my old job back` | **Tornai a Wayfarer con un passaggio, implorai di riavere il mio vecchio lavoro** |
| `passed all our non-destructive testing with flying colors` | **superato tutti i nostri test non distruttivi a pieni voti** |
| `the right to purchase one of the very first units off the production line` | **il diritto di acquistare uno dei primissimi esemplari usciti dalla linea di produzione** |
| `Waivers of liability in case you die` | **Liberatorie nel caso tu muoia** |
| `the usual legal stuff` | **le solite cose legali** |

`You know, the usual legal stuff` è la battuta che chiude la scena: il tono **burocratico** («liberatorie nel caso tu muoia»)
detto con nonchalance è il punto comico, e la resa lo mantiene con «Sai com'è, le solite cose legali».

## 3. Le due battute quasi identiche

Le unità 9 e 10 ripetono quasi la stessa frase:

| unità | inglese | resa |
|---|---|---|
| 9 | `He ignores your question. "But then I saw one more thing," he says.` | **Ignora la tua domanda. "Ma poi ho visto un'altra cosa," dice.** |
| 10 | `"But then I saw one more thing," he says.` | **"Ma poi ho visto un'altra cosa," dice.** |

Non sono un errore del sorgente: la 9 risponde al giocatore che ha fatto una domanda scomoda, la 10 è la variante senza
domanda. Il `check.py` verifica che restino **distinte** e che ognuna cominci come deve.

## 4. Il `VALUE` e la `DESCRIPTION`

`Warship Testing` è il nome della missione nell'interfaccia: **copiato**. La `DESCRIPTION` è quella che il giocatore legge
nell'elenco delle missioni: **tradotta**, con la regola del collaudo in evidenza.

## 5. Struttura

| cosa | inglese | italiano |
|---|---|---|
| tab | **13** (unità 4-16) | **13**, primo carattere |
| virgolette | **42** | **42**, per unità, dritte |
| apici | **4** (`It's`, `don't`, `here's`, `I'll`) | **9** (`l'occasione`, `d'acqua`, `C'erano`, `un'altra` ×2, `all'opera`, `dell'...`) |
| segnaposto | **5** | **5**, stesse famiglie |

## 6. Cosa resta aperto (dichiarato)

- **Nessuna approvazione**: 16 unità `PENDING`.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Il file è a 16/51**: L279 riprende dalla riga 56 con **33 `MISSION_TEXT`** e il **colloquio tecnico** sul prototipo
  (32 tab, 94 virgolette, 16 apici).
