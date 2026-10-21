# review.md — L282 (`data/wanderer/wanderer missions.txt`, righe 16–41)

Registro delle decisioni editoriali del **primo lotto** delle missioni Wanderer: la **pianta malata** dei Mereti.

## 1. Che cosa succede

Il giocatore torna da un mondo Mereti e trova **serre ampliate**. Un drone più piccolo lo accoglie e lo porta in una serra
dove, in un **vaso imponente**, sta una pianta dai **petali blu intenso** e dalle **foglie verde acqua** che **non cresce
bene**. Il drone parla «molto più piano dell'ultima volta» e chiede aiuto **ricordando** al giocatore cosa ha già fatto per
loro. Arrivano due **Wanderer**, che propongono di portare la pianta su `<planet>`; il drone e gli altri la caricano e il
giocatore parte.

## 2. Le alternative: come sono state trattate

Nove `[...]` in tre unità. Tre regole:

1. **la struttura non si tocca**: parentesi quadre, separatore (` , ` oppure `? `), numero di opzioni;
2. **le opzioni si traducono** e restano **intercambiabili**: se una è un verbo riflessivo, anche l'altra lo è
   (`[difenderci, proteggerci]`), se una è un aggettivo femminile, anche l'altra (`[nativa, originaria]`);
3. **l'ordine non si cambia**: la prima opzione è quella che il gioco pesca più spesso nelle sue varianti «normali».

Il caso più delicato è `[best, most likely] [approach, solution]`: **due** alternative **adiacenti**. In inglese tutte e
quattro le combinazioni sono grammaticali (l'articolo è invariabile); **in italiano no**: con «soluzione» (femminile) l'articolo
«il» e gli aggettivi maschili non concordano, e una delle combinazioni produrrebbe «il più probabile soluzione».

La soluzione adottata è **non cambiare la struttura** (due gruppi, due opzioni ciascuno) e scegliere il secondo gruppo fra
sostantivi **maschili**: `[migliore, più probabile] [piano, approccio]`. Così tutte e quattro le combinazioni restano corrette —
«il migliore piano», «il più probabile approccio», ecc. — e il testo non può produrre una frase sgrammaticata a runtime,
qualunque opzione il gioco peschi.

## 3. Scelte

| inglese | resa |
|---|---|
| `The Mereti have clearly been expanding their greenhouses` | **I Mereti hanno chiaramente ampliato le loro serre** |
| `they welcome you as you step out` | **ti danno il benvenuto quando scendi** |
| `without giving you time to properly respond, they shepherd you` | **senza darti il tempo di rispondere come si deve, ti accompagnano** |
| `a majestic pot` | **un vaso imponente** |
| `illuminated by a shaft of light through the windows above` | **illuminata da un fascio di luce che scende dalle finestre in alto** |
| `vibrant deep blue petals and teal leaves` | **petali vibranti di blu intenso e foglie verde acqua** |
| `despite your lack of familiarity with it you can tell` | **anche se non la conosci riesci a capire** |
| `much more quietly than the last time you spoke with them` | **molto più piano dell'ultima volta che avete parlato** |
| `You helped to [defend, protect] us when we were attacked` | **Ci hai aiutato a [difenderci, proteggerci] quando siamo stati attaccati** |
| `lights flash across it` | **delle luci gli lampeggiano addosso** |
| `talking with each other in hushed tones` | **che parlano fra loro a voce bassa** |
| `it shares crucial similarities with some of the plants` | **ha somiglianze cruciali con alcune delle piante** |
| `that is the [best, most likely] [approach, solution] in the short term` | **è il [migliore, più probabile] [piano, approccio] nel breve periodo** |
| `we still seek to leave these worlds to the Unfettered` | **vogliamo comunque lasciare questi mondi agli Slegati** |
| `they hurtle by less than a meter from the Wanderers' ships at almost top speed` | **sfrecciano a meno di un metro dalle navi dei Wanderer a velocità quasi massima** |

## 4. Il registro dei Mereti

I Mereti parlano **lentamente, con pause e lampeggi di luce**: «È la nostra...» e il silenzio di qualche secondo sono parte del
personaggio. La resa conserva i **puntini di sospensione** e la ripetizione («È importante per noi»), perché la ripetizione è
ciò che il testo mostra: il drone **non riesce a dire** che cosa sia quella pianta per loro.

## 5. Struttura

| cosa | inglese | italiano |
|---|---|---|
| tab | **9** (unità 4-12) | **9**, primo carattere |
| virgolette | **16** | **16**, per unità |
| alternative | **9** | **9** (2 opzioni ciascuna) |
| apici | **4** | **5** (`'mentori'` = 2, più le tre elisioni) |
| segnaposto | **4** | **4**, stesse famiglie |

## 6. Cosa resta aperto (dichiarato)

- **Nessuna approvazione**: 13 unità `PENDING`.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Il file è a 13/54**: L283 riparte dalla riga 42 con **14 unità** in **tre contesti** (`The Plant 1`, `2`, `3`), **18
  alternative** e **7 tab**.
