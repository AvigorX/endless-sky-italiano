# L21b — revisione editoriale

`data/human/intro missions.txt` **completo**: righe **23–2319**, **637 unità**,
**19.451 parole inglesi → 17.681 italiane**, 67 contesti.

È il file delle missioni introduttive: il capitano James accompagna il giocatore nei primi
lavori su quattro alberi alternativi (`Intro`, `Midgard Intro`, `Mainsail Intro`, `Delve Intro`),
ognuno con il proprio arco trasporto → turisti → merci → intercettore.

## 1. Struttura e tipi

| tipo | n | trattamento |
|---|---:|---|
| `CONVERSATION` | 209 | testo di conversazione (backtick): tradotto |
| `MISSION_TEXT` | 288 | prosa di missione: tradotta |
| `VALUE` | 50 | nome missione: tradotto |
| `DESCRIPTION` | 50 | descrizione missione: tradotta |
| `LOGBOOK` | 36 | voce di diario: tradotta |
| `DIALOG` | 4 | messaggio di dialogo: tradotto |

Nessuna `UI_LABEL`: l'unica unità non traducibile è la **113**, `label "job 2"` dentro un blocco
`conversation` (delimiter `quote`), che è un bersaglio di `goto` e resta identica.

## 2. I pronomi come token — il caso nuovo di questo file

Cinque unità contengono pronomi inglesi come segnaposto:
54 `<they've>`, 84 `<their>` + `<they're>`, 85 `<they are>`, 145 `<they>`, 148 `<they>`.
Il motore li sostituisce con parole inglesi (`he`/`she`/`they`), che in italiano rompono
l'accordo grammaticale: «<they> continua» diventa «he continua» oppure «they continuano».

**Decisione:** in quelle unità il pronome è reso con una costruzione che non richiede accordo —
possessivo italiano (che concorda con l'oggetto, non con la persona), «che», o soggetto
sottinteso. Il token sparisce e con esso 7 occorrenze su 433 (426 restano intatte).

Esempi:
- 84: «Dall'espressione sul volto, diresti che si sente fortunato…» (era `on <their> face … <they're> feeling`).
- 145: «La prima difficoltà," continua, "sarà capire…» (era `"The first challenge," <they> continues`).
- 148: «…chiacchierate ancora un po' con <captain>, e alla fine ti suggerisce…» (era `and <they> suggests`).

L'eccezione è **enumerata** in `check.py` (`TOKEN_EXC`) e `verify.py` verifica che:
(a) le sole unità con token diversi siano esattamente quelle cinque; (b) in ognuna si perdano
solo i pronomi; (c) il totale dei token persi sia 7. Nessun'altra unità può perdere un token
senza far fallire il controllo.

## 3. Decisioni terminologiche

| EN | IT | nota |
|---|---|---|
| Paradise Worlds | Mondi Paradisiaci | coerente con L19–L21a |
| Dirt Belt, Deep, Core, Rim, Far North | invariati | nomi di regione, come nei lotti precedenti |
| Earth / Earth Day | la Terra / l'Earth Day | il giorno della festa resta inglese: è un nome proprio di ricorrenza |
| Mining Drone / Mining Laser | drone minerario / laser minerario | oggetti comuni: tradotti |
| Jackal, Sparrow, Star Queen, Firebird, Caravan | invariati | classi di nave |
| Hestia, Gemstone, Skymoot, Vinci, Norn, Muspel, Vail, Procyon, Zosma, Algieba, Chiron, Burthen, Caldra, Farseer | invariati | toponimi |
| James, Olivia, Hendersons, Chuck, Sarah, Carl, Chai, Simon, Kamon, Chiaki, Sarika, Catrina, Van, Jan, Mecit, Chen, Mayumi, Eldred, McLain, Donald, Rawda, Raphael, Carlijn, Faiza | invariati | nomi propri |
| «Spaceport» (pulsante) | «Spazioporto» | 7 occorrenze; da riallineare se l'etichetta UI resta inglese |
| `flagship model`, `capacity`, `cargo`, `commodity`, `date`, `day`, `payment` | token invariati | segnaposto del motore |

## 4. Ripetizioni strutturali del file

Il file è costruito per **rami alternativi**: la stessa battuta compare in più alberi di missione.
Il controllo dei duplicati è derivato dal sorgente (`DUP_OK`), quindi la ripetizione è ammessa
solo dove l'inglese è identico. Casi in cui l'inglese **differiva di una parola** e la traduzione
era stata appiattita:

- 246 `<destination>, and deliver` vs 352 `<destination> and deliver` → virgola mantenuta / tolta.
- 249 «I'd be glad to help!» vs 468 «I'd be glad to help out!» → «Sarò felice di aiutare!» / «Sarò felice di dare una mano!».
- 55 «After taking one last glance…» vs 571 «After taking one last look…» → «un ultimo sguardo» / «un'ultima occhiata».

## 5. Correzioni effettuate

- Unità **46, 92, 129, 145, 146, 157, 163, 308, 391, 522, 625, 632**: citazioni allineate al
  conteggio dispari del sorgente (non chiuse d'ufficio).
- Unità **2 / 15 / 21**: «very first starship» distinto da «first starship» («primissima»).
- Unità **96 / 125**: `she said` / `he said` distinti («dice lei» / «dice lui»).
- Unità **258**: refuso di stesura corretto («Lo è indeed» → «Lo è davvero») prima del controllo.
- Unità **465**: la chiave era stata scritta due volte (in `part05` e in `part06`); rimossa la
  copia sbagliata, che sovrascriveva quella corretta in fase di merge.
- Unità **405 / 533**: `A old man` (refuso inglese) → «Un vecchio».

## 6. Controlli

```
check.py    FAIL totale: 0    (637/637, tab 380/380, virgolette 1089/1089, token 426/433 = 7 pronomi)
verify.py   24 controlli, 0 FAIL, exit 0
```

`verify.py` verifica in modo indipendente: riga grezza, DB (`english`/`kind`/`path`/`PENDING`),
nessuna `APPROVED`, id univoci, ordine, intervallo 23–2319, file completo prima e dopo,
copertura 637/637, unità 113 identica, token (parità + eccezioni + totale perso = 7),
tab/virgolette/backtick, vuoti, caratteri non latini, rapporti, ricostruzione delle parti.

Rapporto IT/EN: min 0,62 · max 1,54.

## 7. Cosa non è stato fatto

Nessuna scrittura in `state.db` o negli output approvati; nessuna patch K4; nessuna build o
applicazione al gioco; **rendering non verificato** (fuori dal perimetro di questo workflow).
