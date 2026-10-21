# REVIEW — L57 · `data/gegno/gegno I corroboration.txt`

Revisione del lotto che chiude il file. Non è un giudizio letterario: è la lista di ciò che si è scelto,
di ciò che resta dubbio e di ciò che va tenuto presente in fase di approvazione.

## 1. Coerenza con L56

- **Le scene condivise hanno la stessa resa.** `DIALOG` 22/23 di L57 e 170/171 di L56 sono lo stesso
  testo inglese: la traduzione è la **stessa stringa**, e `verify.py` la confronta letteralmente. Se un
  domani uno dei due viene ritoccato, il controllo diventa rosso: è l'unico modo per impedire la deriva.
- **Il commiato di Adrauni** (unità 21) appartiene alla stessa sequenza di L56 (unità 125 e 169): stesso
  inchino, stessa formula di augurio, stessa uscita dall'hangar. La formula «aspiro a che … si addicano
  ai saggi nel cammino che ti attende» è **identica** nei tre punti, come in inglese.
- **Il foglio di stile resta quello dei Gegno**: nessun avverbio in `-mente` gratuito, nessun
  rafforzativo, presenti narrativi, discorso diretto con virgolette dritte.

## 2. Nodi traduttivi aperti (dichiarati)

- **«turf»** in `Turf Wars`: invariato, come nella linea Avgi.
- **«Adrauni»** come titolo e non come nome: la formula «uno con il titolo di 'Adrauni'» compare identica
  in L56 (47, 59) e in L57 (implicita). Un lettore attento nota che il Quarg di L56 e quello di L57 sono
  la stessa persona: il testo non lo dice mai esplicitamente.
- **«revolution»** di nuovo in unità 8: coerente con L56, nessuna conversione in anni.
- **«cage-like platform»** → «piattaforma simile a una gabbia», poi «ascensore a gabbia»: due rese per lo
  stesso oggetto, perché il primo è la descrizione visiva e il secondo è il riferimento funzionale.
  È voluto, ma va segnalato: chi rivede potrebbe volerlo uniformare.
- **«timpani-like drums»** → «tamburi simili a timpani»: il timpano è un strumento reale, e la scena
  descrive un'orchestra rituale. Non reso con «tamburi giganti».

## 3. Duplicati

4 gruppi, 8 unità:

| Gruppo | Unità | Perché è identico |
|---|---|---|
| `DIALOG` dell'attacco alla flotta | 22, 23 | Stessa scena, due esiti della missione |
| `(Meet with the Gegno.)` | 35, 41 | Stessa scelta in due rami dell'albero |
| `(Leave the Gegno and their world.)` | 36, 42 | Idem |
| «non sei seguito mentre lasci il pianeta» | 100, 104 | Stessa coda nei due epiloghi |

Nessun duplicato italiano non spiegato dal sorgente: la riga `duplicati italiano non spiegati dal
sorgente` di `check.py` è verde.

## 4. Cosa NON è stato fatto

- **Nessuna scrittura su `state.db`.** Le 127 unità restano `PENDING`.
- **Nessun caricamento nel gioco.** La verifica è sui file, non sul runtime.
- **Nessuna deroga generica sui token.** I 13 `<…>` sono confrontati come multiset per unità.
- **Nessun ritocco ai file protetti.**

## 5. Rischi residui

- **Il file è chiuso ma non approvato.** 298 unità `PENDING` su un file completo: la fase di
  approvazione è un passaggio separato, con revisione umana, e non è stata fatta.
- **`label` non tradotte.** 45 `UI_LABEL` complessive sul file (28 in L56, 17 in L57) restano in inglese
  perché sono chiavi. Se un giorno si decidesse di localizzarle, servirebbe una modifica al formato dei
  dati, non alla traduzione.
- **`<payment>` nella riga Gegno** è il primo caso in cui un token di denaro entra in una frase con
  «somma di»: se il gioco rendesse `<payment>` come stringa con valuta già inclusa, la frase reggerebbe
  comunque. Non è verificabile senza runtime.

## 6. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 4 parti, `translation.json`, `check.py`, `verify.py`, documenti |
| ESEGUITO | sì — i due script sono stati lanciati e l'output letto |
| VERIFICATO | sì — `check.py` `FAIL totale: 0` (33 controlli), `verify.py` exit 0 (41 controlli), chiusura 298/298 |
