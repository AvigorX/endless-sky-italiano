# L52 — revisione editoriale

`data/avgi/avgi 0 first contact.txt` · righe 873–1120 · 135 unità · chiuso il 2026-10-18.
Questo file registra le **decisioni di traduzione** e i **limiti osservati**, non le lodi.

## 1. Il lotto che chiude un arco: tre ritorni

Il file si chiude con tre ritorni che sono tre registri diversi, e la traduzione li distingue:

| ritorno | scena | registro |
|---|---|---|
| **Sora** | la fattoria dei genitori su Memory | caldo, breve, con un rimprovero affettuoso a Darius |
| **Darius** | la casa sul fiume su Valhalla | teso fino alla porta, poi sfogo; il testo rallenta |
| **la via d'uscita** | il magnetar di Decet | tecnico, descrittivo, senza dialoghi |

La scena di Valhalla è la più delicata: il testo costruisce la delusione in tre passaggi (porta
sbagliata → registri in biblioteca → indirizzo in campagna). La traduzione non ha anticipato nulla:
unità 111–114 restano **secche** («C'è... c'è una Katrina, qui?»), e la speranza compare solo dove
compare nell'inglese (unità 120: «Almeno ha tenuto il nostro cognome.»).

## 2. La Dissonanza: un nome che è già una presa di posizione

`Dissonance` è il nome che **la Consonanza** dà ai dissidenti: è un'etichetta data da una parte, non un
nome neutro. In italiano resta **«la Dissonanza»** (decisione 168 e uso del corpus), e il testo lo dice
esplicitamente in unità 12: «il loro movimento è stato etichettato collettivamente come 'Dissonanza'» —
con `etichettato`, che rende il `labeled` inglese e segnala che il nome viene da fuori.

`Dissonance mining station` → **stazione mineraria della Dissonanza** (unità 16): la preposizione
italiana basta, senza virgolette, perché il nome è ormai un nome proprio nel testo.

## 3. Il varco e i suoi termini tecnici

- `gateway` → **varco** (unità 49, 50, 51, 52, 53): non «portale», che in italiano evoca la fantasia e
  non un manufatto alieno.
- `ancient alien artifact built by an unknown Antecessor species` → **«un antico manufatto alieno
  costruito da una specie Antecessors sconosciuta»**: `Antecessors` resta **invariato**, come nel corpus
  (3 occorrenze), perché è il nome della specie precorritrice e non ha glossa nel testo.
- `magnetar` **invariato**: è un termine astronomico internazionale, e il corpus lo usa così.
- `ionizing entire systems` → **«ionizzano interi sistemi»**; `red nebula suffusing it` → **«una
  nebulosa rossa che lo pervade»**.
- `Ember Waste` **invariato** (unità 55 e `label` 57): è il nome della regione, con 5 occorrenze nel
  corpus, e l'etichetta di salto non si tocca mai.

## 4. Decisioni puntuali

1. **`price controls`** → **«controlli sui prezzi»** (unità 13, 21): non «calmiere», che è un istituto
   diverso e in italiano suona come un prezzo fissato dallo Stato al dettaglio.
2. **`iron`, `titanium`** → **ferro**, **titanio**; `cheap steel` → **«acciaio a buon mercato»** (unità
   29): Sora parla di industria, non di metallurgia d'arte.
3. **`backpay`** (unità 131) → **«arretrati»**: la battuta di Darius è burocratica e va tenuta tale.
4. **`skinsuits`** (unità 129) → **«tute di pelle»**: la battuta del giocatore è surreale e la parola
   inglese non ha equivalente migliore; «tute mimetiche» avrebbe spiegato la battuta e l'avrebbe uccisa.
5. **`Outpost Tekis`** → **«Avamposto Tekis»**: `outpost` è un nome comune, `Tekis` resta.
6. **`Antecessors`** e **`Dissonanza`** convivono nello stesso periodo (unità 49–12) senza che uno dei
   due venga «normalizzato»: il primo è un nome di specie senza glossa, il secondo un nome di movimento
   con glossa in scena.
7. **`Katrina... Caldwell. Our name.`** (unità 120) → **«Katrina... Caldwell. Il nostro cognome.»**:
   `name` qui è il cognome di famiglia, e «il nostro nome» in italiano suonerebbe come il nome proprio.
8. **Errore del sorgente riprodotto**: unità 79 scrive **`Darious`** invece di `Darius`. Il nome proprio
   in italiano è **Darius** in tutta la serie: non ho replicato il refuso, che è un errore di battitura
   inglese e non una variante del personaggio (a differenza di `Caldwell`/`Calwell`, dove la differenza
   è nel cognome e resta in entrambe le grafie).
9. **`supposed 'death'`** (unità 130) → **«presunta 'morte'»** con le virgolette singole del sorgente:
   Katrina cita la parola usata dai burocrati, e il segno va tenuto.

## 5. Il controllo che cambia natura: «di file» invece di «di segmento»

Dopo L46 la copertura era stata riscritta **per segmento**, perché un lotto interno diventava rosso
quando il file proseguiva (decisione 166). L52 **chiude** il file, quindi l'invariante «di file» torna
legittimo — ma solo in presenza di **tre** condizioni, tutte asserite:

```
chiude il file: 271 prima della 873, 0 dopo la 1120    OK
max(line) del file = 1120                              OK
copertura del file 406 / 406 (tre lotti)               OK
```

Se il file crescesse di una sola unità, i primi due controlli diventerebbero rossi. È la differenza fra
un invariante vero e un'asserzione che passa per caso.

## 6. Cosa il lotto **non** dimostra

- Non dimostra che le cinque missioni siano giocabili: i `goto` non sono stati percorsi.
- Non dimostra la resa **a schermo** dei tre messaggi `dialog` di blocco né della scena finale del
  ricongiungimento, che è il punto emotivo del file.
- Non dimostra che il **magnetar** funzioni come descritto (unità 134–135): il testo è tradotto, il
  comportamento in gioco non è stato provato.
- Il rapporto lunghezze (0,68–1,60) è dentro il gate ma **non è un giudizio di qualità**.
