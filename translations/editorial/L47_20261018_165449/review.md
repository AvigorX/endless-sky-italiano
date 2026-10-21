# L47 — revisione editoriale

`data/successors/successor 1 prologue.txt` · righe 680–1024 · 124 unità · chiuso il 2026-10-18.
Questo file registra le **decisioni di traduzione** e i **limiti osservati**, non le lodi.

## 1. Un errore vero trovato dallo strumento, non un falso positivo

Le unità **94** e **103** sono due discorsi cerimoniali quasi identici, in due versioni dello stesso
consiglio (una convocata da Sioeora, una da Kaatrij). Il primo stesura le rendeva **identiche** in
italiano, e il controllo duplicati del `check.py` le ha segnalate:

```
| duplicati italiano non spiegati dal sorgente | [('\t"Casa Sioeora. Casa Chydiyi vede bene la tua', 2, [94, 103])] | FAIL |
```

La differenza nell'inglese è **una sola parola**, il vocativo:

```
94:  "House Sioeora. House Chydiyi well sees thy perspicacity ..."
103: "House Kaatrij. House Chydiyi well sees thy perspicacity ..."
```

Nella scena, il primo rappresentante di Casa Sioeora propone il dono, quello di Casa Kaatrij gli
risponde: il vocativo dice **a chi si parla**. La 103 è stata corretta in **«Casa Kaatrij.»**.

Lezione operativa: i paragrafi cerimoniali ripetuti (in questo lotto ce ne sono sei coppie: 91/100,
93/102, 95/104, 97/106, 98/107, 99/108) **non sono copie**: la differenza sta nel nome della Casata, nel
soggetto o nel destinatario. Un `--range` non l'avrebbe vista, perché 94 e 103 stanno in parti diverse.

## 2. Limite dichiarato: la scheda di Saajret resta in inglese

L'unità **54** è un `LOGBOOK` ma il suo `english` è solo la categoria (`People`). Sorgente:

```
log "People" "Saajret, of Somber Sejra" "Saajret, of Somber Sejra is an archivist, among other things..."
```

`tools/l10n.py` (protetto) estrae come unità la **categoria** quando il testo del diario è fra
**virgolette**. Conseguenza: la scheda di Saajret **non ha testo italiano**.

- È il **sesto** caso della serie (L45: 195/305/357/418; L46: 62; L47: 54).
- Non è stato toccato nulla: `state.py` conferma `INTEGRITA'` su tutti i file protetti.
- `check.py` e `verify.py` **asseriscono** la lacuna invece di nasconderla.
- Ripararla richiede una modifica a `tools/l10n.py` e una rigenerazione di `state.db`: decisione
  dell'utente, non del lotto.

## 3. Le due versioni dello stesso incontro

Il file contiene **due rami** dello stesso evento: uno se il giocatore ha accettato il patrocinio di
Sioeora (unità 91–99), uno se ha preso quello di Kaatrij (100–108), più una variante con token
(116, `<successor patron>` / `<successor opponent>`). Le rese sono **parallele per costruzione**:

| funzione | ramo Sioeora | ramo Kaatrij |
|---|---|---|
| proposta del dono | 92 | 101 |
| sostegno di Chydiyi | 94 | 103 |
| obiezione dell'altra Casa | 96 | 105 |
| reazione al silenzio | 97 | 106 |
| voto e consegna della spilla | 111 | 115 |

Non sono state «armonizzate» con un'unica formulazione: ogni ramo nomina la Casata che parla, e la
differenza è informazione di gioco.

## 4. Decisioni puntuali

1. **`Old and New Houses` → «Casate Vecchie e Casate Nuove».** Con la maiuscola, perché nel testo è un
   nome istituzionale ricorrente («the Old Houses, which Sioeora and Chydiyi do today here represent»).
2. **`House Sejra` → «Casa Sejra»** e `line` → **«linea nobile»**: «la sobria linea nobile di Casa
   Sejra, che più non sussiste se non come uno stendardo sotto le ali vigili di Kaatrij». Le Casate
   estinte (`Jaasii`, `Vejret`, `Ijridanii`, `Sejra`) restano invariate come nomi propri.
3. **`device of tongues` → «dispositivo delle lingue»**, `pin` → **«spilla»**, `translation pin` →
   **«spilla da traduzione»**. Il dono è lo stesso oggetto in tre descrizioni diverse: la resa mantiene
   il filo (spilla di legno intagliato, non un apparecchio elettronico).
4. **`Tempest` → «la Tempesta»**, `Shakespeare` invariato: il testo dice «thine own Shakespeare's
   Tempest», quindi il titolo si traduce e l'autore no.
5. **`petty technologies` → «tecnologie minori»**, non «tecnologie da poco»: è una categoria di
   commercio, non un giudizio.
6. **`Coalition` e `Hai` invariati**: sono fazioni con nome proprio, già trattate così nel corpus.
7. **`(Try to decode it.)` / `(Maybe later.)` / `(Don't decode it.)`** (8/14, 9/15, 10/16) sono coppie
   identiche nel sorgente e restano identiche in italiano: due rami dello stesso bivio (traduzione
   Coalition / traduzione Hai), non due scelte diverse.
8. **`(Leave.)` tre volte** (27, 30, 33): stesso inglese, stessa resa. Il giocatore può uscire dalla
   scena in tre momenti diversi e il testo non cambia.
9. **`Well-met again` → «Che bello incontrarti di nuovo»**: formula di saluto arcaica, resa con un
   registro cordiale moderno; `fair travels` → **«buon viaggio»**.
10. **`concierge` → «concierge»**: prestito già in uso in italiano, evita «portiere» che in un complesso
    alieno suona domestico.

## 5. Cosa il lotto **non** dimostra

- Non dimostra che la linea *Kaatrij First Contact* sia giocabile in italiano: i 3 contesti hanno molti
  `goto` e nessuno è stato percorso nel gioco.
- Non dimostra la resa **a schermo** della scena del consiglio: la verifica è testuale.
- Non dimostra nulla sulla scheda di diario di Saajret (§2).
- Il rapporto lunghezze (0,70–1,69) è dentro la banda ma **non è un giudizio di qualità**.
- Il file è completo **in staging**, non nel database: 345 unità `PENDING`, nessuna approvata.
