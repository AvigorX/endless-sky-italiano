# REVIEW — L58 · `data/human/culture conversations.txt`

Revisione del lotto dopo la chiusura dei controlli. Elenca ciò che si è scelto, ciò che resta dubbio e
ciò che va tenuto presente in fase di approvazione.

## 1. Coerenza interna

- **Una sola voce narrante**: seconda persona, presente, osservativa. Vale per tutte e nove le scene,
  anche quando cambia il luogo (spazioporto, strada, cantiere, ristorante).
- **Nessun giudizio aggiunto.** Dove l'inglese dice «you pity the man», l'italiano dice «compatisci», e
  non aggiunge «ingiustamente» né «con rabbia». Il testo lascia al lettore la valutazione morale.
- **Le tre scelte del ristorante** restano distinte: offrire (38), compatire in silenzio (40), sorridere
  (37). Sorridere non è compatire, e la traduzione non le confonde.

## 2. Nodi traduttivi aperti (dichiarati)

- **«12th division win»** (unità 1) → «vincita di dodicesima categoria». La lotteria di Endless Sky ha
  divisioni: «categoria» è la parola italiana corretta per una classe di premio, ma nessun documento del
  gioco la definisce. Se un giorno il glossario la fisserà diversamente, va cambiata in blocco.
- **«void deck»** (unità 15) → «pianterreno aperto». È un termine architettonico dell'Asia sudorientale
  (il piano terra aperto dei palazzi HDB): l'italiano non ha un equivalente, e la perifrasi è onesta.
- **«slippers for their bare feet»** (unità 16) → «pantofole per i piedi scalzi». Il dettaglio è culturale
  (si tolgono le scarpe al funerale) e resta un dettaglio, non viene spiegato.
- **«chain link fence»** (unità 18) → «recinzione a maglie metalliche». **«grinders»** → «molatrici».
- **«bumper crop»** (unità 31) → «raccolto eccezionale», ripetuto due volte come nell'inglese.
- **«a chip in it»** (unità 13) → «che ha una scheggiatura»: la tazza vecchia del giocatore. Il
  riferimento è al testo precedente della stessa missione, non a L58.

## 3. Duplicati

| Gruppo | Unità | Perché |
|---|---|---|
| Sad Gamblers (due fazioni) | 1, 3 | Stesso testo, `Republic` e `Syndicate` |
| Idem, seconda unità | 2, 4 | Stesso commento alla scena |
| «(Leave them be.)» | 21, 24 | Stessa scelta in due punti dell'albero |

Resa identica, verificata. Nessuna resa italiana ripetuta fra unità con inglese diverso.

## 4. Cosa NON è stato fatto

- **Nessuna scrittura su `state.db`**: le 43 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: verifica sui file, non sul runtime.
- **Nessuna deroga sui simboli**: qui non ce n'erano da concedere (0 token, 0 `UI_LABEL`), ma le assenze
  sono state **asserite**, non semplicemente ignorate.

## 5. Rischi residui

- **La verifica automatica non misura la voce.** Questo lotto è il primo della serie in cui il rischio
  dominante è stilistico: un traduttore diverso potrebbe rendere le stesse unità con un registro più
  letterario e passare tutti i controlli. La revisione umana serve esattamente a questo.
- **Il file è aperto**: 331 unità dopo la 209. Una modifica al registro fissato qui (per esempio
  «categoria» per le divisioni della lotteria) va propagata a L59 e successivi.

## 6. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 3 parti, `translation.json`, `check.py`, `verify.py`, documenti |
| ESEGUITO | sì — entrambi gli script lanciati, output letto |
| VERIFICATO | sì — `check.py` `FAIL totale: 0` (33 controlli), `verify.py` exit 0 (35 controlli) |
