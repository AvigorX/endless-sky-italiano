# review.md — L241 (`data/successors/successor jobs.txt`, righe 16–280)

Registro delle decisioni editoriali del **primo lotto** di `successor jobs.txt`: un file di **frammenti** dove la frase
non esiste finché il motore non sceglie un'opzione per ogni gruppo.

## 1. Come si traduce un frammento

La regola del lotto: **il frammento si traduce in modo che ogni combinazione regga**, non in modo che sia bello da solo.
Le conseguenze pratiche:

| vincolo | esempio | perché |
|---|---|---|
| **l'articolo viaggia con il nome**, non col verbo | `You deliver the ` → «Tu consegni » + `researchers ` → «i ricercatori » / `scientists ` → «gli scienziati » | l'italiano non può mettere l'articolo dopo il nome, e ce ne sono **due diversi** (`i` / `gli`) dentro lo stesso gruppo |
| il genere è **fisso per gruppo**: i nomi alternativi devono avere lo **stesso genere** | `the ` + `shipment ` / `cargo `: «il carico» / «il lotto», non «il carico» / «la partita» | `the ` e `your ` sono **condivisi**, quindi il genere lo decide il gruppo successivo |
| il verbo non porta lo spazio finale se l'oggetto lo porta in testa | `begin ` → «iniziano a» + ` catalogare…` | altrimenti la frase avrebbe **due** spazi |
| l'avverbio porta lo spazio finale, così la variante **vuota** resta corretta | «dove » + «subito » + «iniziano a…» / «dove » + «iniziano a…» | con l'opzione vuota «dove» + «iniziano» darebbe «doveiniziano» |
| l'ultimo frammento di un gruppo chiude **con il punto e uno spazio** | ` catalogare … vicine. ` | il frammento successivo comincia con la maiuscola |

## 2. I quattro blocchi, frase per frase

| blocco | esempio composto |
|---|---|
| `successor data` | «Tu consegni a mano le banche dati criptate e poi ricevi `<payment>` in pagamento.» · «Tu trasferisci i dati e poi ti viene versato un pagamento di `<payment>`.» |
| `high houses delivery` | «Tu scarichi il carico di `<commodity>` a diversi ufficiali Successors in ghingheri. Ti versano quanto pattuito, cioè il pagamento di `<payment>`.» |
| `predecessor researchers out` | «Tu consegni i ricercatori a `<planet stopovers>`, dove subito prendono a catalogare alcune formazioni rocciose vicine. Dopo qualche ora, sono pronti a tornare a casa.» · «Tu consegni gli scienziati a …» |
| `successor researchers out` | lo stesso, con «sperimentatori» e cinque oggetti invece di nove |

## 3. Le scelte di parola

| inglese | resa | nota |
|---|---|---|
| `hand over ` | **consegni a mano** | «cedi» sarebbe stato 0,50 di rapporto: la soglia non si allarga, si riscrive |
| `and ` | **e poi** | «e» da solo stava a 0,50; «e poi» tiene il senso e rientra nel gate |
| `begin ` / `start ` | **iniziano a** / **prendono a** | brevi abbastanza da rientrare nel gate (2,00 → 1,67) |
| `the databanks` | **le banche dati** | forma dominante del corpus (4 contro 1 «banca dati») |
| `well-dressed` | **in ghingheri** | non «ben vestiti»: il testo è ironico |
| `cargo ` (in quel blocco) | **lotto** | «carico» è già la resa di `shipment `: due parole inglesi, due parole italiane. «Partita» sarebbe stata più naturale ma è **femminile**, e `the `/`your ` sono condivisi: «il tuo partita» |
| `sightseers` | **gitanti** | distinto da `travelers` → «viaggiatori» e da `tourists` → «turisti» |
| `symposium` | **simposio** | 1 precedente nel corpus |
| `examining nearby ruins` | **esaminare alcune rovine vicine** | «rovine» 54 nel corpus |
| `scanning for artifacts` | **cercare manufatti con gli scanner** | «manufatti» 52; il verbo da solo non renderebbe lo strumento |
| `cross-checking the data` | **confrontare i dati** | |
| `their safety equipment` | **la loro attrezzatura di sicurezza** | |

## 4. `VALUE` e `DESCRIPTION`

I cinque `VALUE` restano inglesi (`Vacationers to <planet>`, `Extreme sightseeing on <planet stopovers>`,
`Sightseeing expedition`, `Students on break to <planet>`); le cinque `DESCRIPTION` sono tradotte, con `<planet
stopovers>` **intero** dentro il segnaposto (`Extreme sightseeing on <planet stopovers>`).

`<planet stopovers>` e `<stopovers>` sono due simboli distinti: il primo **contiene uno spazio** e non va spezzato. Il
`check.py` verifica che siano 3 + 3 e non 6.

## 5. La lacuna dichiarata

Il quarto gruppo dei due blocchi «researchers» ha **quattro** opzioni nel sorgente e **tre** nell'inventario: la quarta è
la stringa vuota (``). Non è un errore di misura — è la stessa classe di lacuna di `deep jobs.txt` (i frammenti
`phrase`), e si dichiara qui perché il `verify.py` legge il file del gioco e la trova. Non si ripara da un lotto: servono
`tools/l10n.py` e `state.db`, che sono protetti.

## 6. Struttura e assenze

- **Zero tab, zero virgolette, zero apici**: tre asserzioni negative scritte.
- **21 gruppi di inglese identico** (i frammenti condivisi fra i due blocchi «researchers» e i due turisti): tutti con
  **una sola resa**, verificata confrontando le stringhe.
- **Due `VALUE` identici** (`Vacationers to <planet>`): due lavori distinti con lo stesso nome, resi identici per
  necessità.

## 7. Due difetti trovati componendo (e il controllo che li vede)

Il primo giro del lotto era **verde** in entrambi gli script e sbagliato in due punti, visibili solo leggendo frasi
composte:

| difetto | frase che usciva | causa | correzione |
|---|---|---|---|
| articolo sbagliato | «Tu consegni **i scienziati** a …» | l'articolo stava nel frammento del verbo e non poteva adattarsi al nome del gruppo successivo | l'articolo viaggia **con il nome** (`i ricercatori`, `gli scienziati`, `gli studiosi`, `gli sperimentatori`) |
| genere sbagliato | «Tu depositi **il tuo partita** di ferro …» | `the `/`your ` sono condivisi, il nome no | due nomi dello **stesso genere**: «il carico» / «il lotto» |

Il controllo dei soli spazi non li vedeva: sono frasi ben formate e con la punteggiatura giusta. È stato aggiunto un
controllo d'**accordo articolo+nome** che enumera le coppie ammesse e rifiuta le altre; provato **al negativo** (rimessi
«il tuo partita» e «i scienziati», il controllo diventa rosso e li nomina), perché un controllo che non può fallire non
è un controllo.
