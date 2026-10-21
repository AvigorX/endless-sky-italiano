# REVIEW — L216 · `deep jobs.txt` (quinto lotto)

Coppie EN→IT rilette in `translation.json` (`193651028d79b6bd…`). Tutte le 30 unità sono **`PENDING`**.

## 1. Decisioni di resa

1. **`capitano <last>`** senza articolo davanti al segnaposto e con il titolo prima: regge cognomi di qualunque origine e
   non richiede accordi che il segnaposto non può portare.
2. **`i <passengers>`** con l'articolo, come l'inglese *the `<passengers>`*. Se il segnaposto fosse un numero nudo, la
   frase sarebbe rotta in entrambe le lingue; il rischio è simmetrico e dichiarato.
3. **`Al mio datore di lavoro questo non va affatto bene`** per *that's just not acceptable to my employer*: rende
   l'insofferenza di Julie senza il calco «inaccettabile per».
4. **`in dire need of passage` → «un disperato bisogno di un passaggio»**: stessa enfasi, registro da viaggiatrice.
5. **`booked up for the next five days straight` → «tutto prenotato per i prossimi cinque giorni di fila»**: conserva
   l'insistenza di *straight*.
6. **`furtively glances` → «un'occhiata furtiva»**: coerente con il fatto che sta rivelando un datore di lavoro
   «indirettamente» riservato.
7. **`model passengers` → «passeggere modello»**: mantiene l'ironia, perché subito dopo il testo dice cosa lasciano a bordo.
8. **`make yourself available` → «renderti disponibile»**: formula che torna due volte (qui e nel `LOGBOOK`) e va tenuta
   identica.
9. **Le varianti umoristiche** del dropoff: «un paio di stivali sporchi», «una cravatta lasciata appesa», «documenti
   accartocciati … nell'inceneritore». Tono asciutto, nessuna spiegazione aggiunta.
10. **`ti avvisa presto`** e non «subito»: il sorgente dice *soon*, non *immediately*.

## 2. Un errore mio, corretto prima di chiudere

Avevo scritto un controllo «il `LOGBOOK` è in terza persona: nessun `tu`/`ti`», e il `check.py` è caduto. Aveva torto il
controllo: il sorgente dice *She requested emergency transport **from you** and showed **you** how to make **yourself**
available*. Il diario apre descrivendo lei e poi parla al giocatore. L'asserzione ora verifica **entrambe** le cose —
apertura in terza persona («Una consulente che…») e presenza della seconda persona — invece di imporre una regola che il
testo non segue.

## 3. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 30 unità `PENDING`.
- **Nessuna missione giocata**: non ho visto `<passengers>` né `<last>` sostituiti nel gioco, quindi l'articolo e il titolo
  sono scelte ragionate, non verificate nel runtime.
- **Nessuna revisione umana**, **nessuna correzione al sorgente**.

## 4. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì |
| ESEGUITO | sì |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (25), `verify.py` exit **0** (19) |
