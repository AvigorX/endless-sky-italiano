# L55 — revisione editoriale

`data/gegno/gegno intro missions.txt` · righe 677–954 · 28 unità · chiuso il 2026-10-18.
Questo file registra le **decisioni di traduzione** e i **limiti osservati**, non le lodi.

## 1. Il Quarg che giudica: un registro diverso da quello cerimonioso

In L54 il Quarg parlava con inversioni solenni («Non è con frequenza significativa che i possenti Gegno
interagiscono con audaci estranei»). Qui parla **freddo e amministrativo**, e la traduzione cambia di
conseguenza:

| inglese | resa | nota |
|---|---|---|
| `It was incredibly unwise to engage in the unnecessary destruction of noncombatants` | **È stato incredibilmente imprudente darsi alla distruzione superflua di non combattenti** | nessun «purtroppo»: accusa, non rimprovero |
| `It is greatly unlikely for violence upon unarmed victims to be accidental` | **È molto improbabile che la violenza su vittime inermi sia accidentale** | il Quarg **non** accetta la scusa |
| `You are no longer welcome in their space` | **Non sei più gradito nel loro spazio** | `welcome` è formula burocratica, non ospitalità |
| `the end of our patience` | **il limite della nostra pazienza** | non «la fine»: è una soglia |
| `It is a great shame` | **È una grande vergogna** | il Quarg parla della **perdita** dei Gegno, non del giocatore |
| `an unpleasant sound - one you have not heard from any Quarg before` | **un suono sgradevole, uno che non hai mai sentito da nessun Quarg** | è l'unica volta che il testo dà un suono al disappunto |

Il punto delicato è che il Quarg **si rammarica per i Gegno**, non per il giocatore: «Il tempo che
avrebbero usato per risolvere i loro conflitti interni è ora sprecato in ostilità verso gli stranieri per
la tua negligenza». La traduzione non ha spostato quell'enfasi.

## 2. Le tre risposte del giocatore e le tre repliche

Le unità 8–10 e 18–19 offrono risposte brevi («È stato un incidente!», «Di che cosa stai parlando?»,
«Non mi importa.») e il Quarg risponde con un testo **lungo e ripetitivo**. La ripetizione è voluta: i
due rami (civili morti / guardiani colpiti) usano quasi le stesse frasi, e le ho tradotte con la stessa
struttura, cambiando solo ciò che il sorgente cambia. Non ho «variato» per eleganza: variare avrebbe
rotto il parallelismo che il testo cerca.

Nota: le unità 10 e 19 sono **identiche** in inglese (`"I do not care."`). La resa è identica
(«Non mi importa.») e `verify.py` lo verifica gruppo per gruppo. Il primo tentativo dello script assumeva
«0 duplicati» ed è stato corretto sul dato misurato — il duplicato è nel sorgente, non nella traduzione.

## 3. La morte del giocatore: come si traduce una sconfitta

Unità 25–27: il giocatore atterra sul mondo natale Gegno dopo aver colpito dei civili, viene circondato e
ucciso. Il testo è **breve e fisico**:

- `several squads in numbers you can't quickly determine` → **«diverse squadre in numero che non riesci a
  valutare in fretta»**: la difficoltà del giocatore è parte della scena;
- `countless ships begin to descend in formations` → **«innumerevoli navi cominciano a scendere in
  formazione»**;
- `It probably wasn't the smartest plan` → **«Probabilmente non era il piano più intelligente»**: il
  narratore è ironico, e l'ironia va tenuta;
- `the last thing you experience is a cold, sharp pain through your upper body` → **«l'ultima cosa che
  provi è un dolore freddo e acuto attraverso la parte superiore del corpo»**: nessuna
  drammatizzazione, nessun «ti trafigge il cuore» che il testo non dice.

L'unità 26 è la variante con i Gegno **nominati** (Vi e Scin) invece che «alieni»: il testo distingue le
due versioni, e la traduzione mantiene la differenza («un grande gruppo di Gegno» / «una grande forza di
alieni», «navi appartenenti sia alla fazione Vi sia a quella Scin»).

## 4. La conversazione (unità 28)

È l'unica `CONVERSATION` del file, e ha un tono diverso da tutto il resto: non c'è un Quarg che giudica,
ci sono **navi ostili che chiamano**. `aggravated in tone` → **«dal tono molto esasperato»**;
`you've interrupted a tradition rather important to them` → **«hai interrotto una tradizione piuttosto
importante per loro»**, con il `piuttosto` che rende l'understatement inglese senza sminuirlo.

Il testo lascia intendere che il duello fosse una **tradizione Vi**: la traduzione non aggiunge la parola
«duello», che compare solo nel nome del contesto (`conversation:interfered with duel`) e non nel testo
visibile.

## 5. Decisioni puntuali

1. **`corroboration provocation`** e **`corroboration provocation homeworld`** sono `label` e restano
   **invariate in blocco**: sono nomi tecnici di salto, non testo.
2. **`noncombatants`** → **non combattenti**; `unarmed victims` → **vittime inermi**: due formule
   diverse nel sorgente, due in italiano.
3. **`guardians of the Gegno homeworld`** → **guardiani del mondo natale dei Gegno** (unità 17, 23): è il
   titolo che il Quarg dà alle navi che il giocatore ha colpito.
4. **`quell unease`** → **sedare il malcontento**; `foreign involvement` → **coinvolgimento straniero**.
5. **`no longer have reason to be here`** → **«non hai più motivo di restare»** (unità 20): non «non sei
   più il benvenuto», che è la formula usata in altre unità — il testo cambia, e la traduzione con lui.
6. **`the same sentiment`** → **«lo stesso sentimento»** (unità 15): è una minaccia detta con una parola
   astratta, e la traduzione non la rende esplicita.

## 6. Cosa il lotto **non** dimostra

- Non dimostra che le quattro missioni siano giocabili: i `goto` e le condizioni sui 4 `label` non sono
  stati percorsi.
- Non dimostra la resa **a schermo** della scena di morte (unità 27), che è il punto in cui il testo
  punisce una scelta del giocatore.
- Non dimostra l'innesco della **conversazione** (unità 28): è tradotta, ma il suo contesto in gioco non è
  stato verificato.
- Il rapporto lunghezze (0,88–1,09) è molto stretto, ma **non è un giudizio di qualità**: il lotto è
  corto e composto in gran parte da battute brevi.
