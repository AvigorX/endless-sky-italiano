# REVIEW — L215 · `deep jobs.txt` (quarto lotto)

Coppie EN→IT rilette in `translation.json` (`0b4212a734b678ff…`). Tutte le 25 unità sono **`PENDING`**.

## 1. Decisioni di resa

1. **`at any rate` → «in ogni caso»**, fisso nelle tre occorrenze. È l'unica scelta che tiene in piedi la battuta: se al
   primo posto avessi messo «comunque» e al secondo «in ogni caso», il giocatore non avrebbe nulla da fargli notare.
2. **`one-time offer` → «un'offerta una tantum»**: locuzione italiana corrente, e mantiene l'unicità dell'offerta.
3. **`well-regarded` → «ben considerato»**: registro colloquiale da agente, non «di ottima reputazione».
4. **`with either urgency or discretion` → «con urgenza o con discrezione»**: rende la coppia di valori senza appesantire.
5. **`good catch` → «ben visto»**: idiomatico, e conserva il tono del parlante colto di sorpresa.
6. **`The question stands though` → «La domanda resta però»**: breve, come l'originale.
7. **`flick a subtle salute … or perhaps merely tips an imaginary cap` → «accenna un saluto appena percettibile … o forse
   si limita a toccarsi un berretto immaginario»**: il dubbio del narratore è parte del ritratto di Wayde.
8. **`securely wrapped` no — `bags in tow` → «con le borse al seguito»**: formula italiana naturale.
9. **`dire need of urgent transport` → «un disperato bisogno di un trasporto urgente»**: consapevolmente ridondante, come
   l'inglese.
10. **`entro <date>`** senza articolo: il segnaposto può essere una data o una durata, e l'articolo sbaglierebbe in metà
    dei casi.
11. **`Delta` — niente**: **`Basic` e `Deep Security`** nei nomi delle missioni restano nei `VALUE`, che non si traducono.

## 2. Un errore mio, corretto prima di chiudere

Il controllo sulla battuta contava **due** occorrenze di *at any rate*; sono **tre**, perché la terza è nell'unità 6 dove
il giocatore la cita. Corretto rendendo l'asserzione **simmetrica**: tre in inglese e tre in italiano, con le posizioni
verificate. Se avessi lasciato il conteggio a due, il controllo sarebbe caduto su un testo corretto — e la diagnosi
sarebbe stata «la battuta è rotta», che è la conclusione sbagliata.

## 3. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 25 unità `PENDING`.
- **Nessuna missione giocata**: la battuta è verificata come testo, non come scena.
- **Nessuna revisione umana**, **nessuna correzione al sorgente**.

## 4. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì |
| ESEGUITO | sì |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (25), `verify.py` exit **0** (19) |
