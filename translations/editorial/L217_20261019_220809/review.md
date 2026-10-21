# REVIEW — L217 · `deep jobs.txt` (sesto e ultimo lotto)

Coppie EN→IT rilette in `translation.json` (`379596a8a8be9b81…`). Tutte le 29 unità sono **`PENDING`**.

## 1. Decisioni di resa

1. **`Transport <fare> whose schedules have been ruined by Deep Security to <destination>`** → «Trasporta `<fare>`, i cui
   programmi sono stati rovinati dalla Deep Security, fino a `<destination>`». La relativa è anticipata per non separare
   `<fare>` dal verbo che lo regge.
2. **`Rush … Delivery`** resta nel `VALUE` inglese; la `DESCRIPTION` corrispondente dice «Consegna … entro `<date>`».
3. **`<bunks> Deep Security consultants`** → «`<bunks>` consulenti della Deep Security». L'accordo del numero è neutro.
4. **`the home of Lionheart Industries`** → «sede della Lionheart Industries»; **`the home of Deep Sky`** → «sede della
   Deep Sky». Due nomi di azienda che restano invariati, con la preposizione articolata corretta per ciascuno.
5. **`cutting-edge cybernetics, weapons, and starship equipment`** → «cibernetica, armi e attrezzature per navi spaziali
   all'avanguardia»: l'aggettivo inglese in testa va spostato in coda, perché in italiano «all'avanguardia» non regge tre
   sostantivi di generi diversi senza ambiguità.
6. **`hovercraft`** resta «hovercraft»: prestito corrente, e il gioco non ha un equivalente italiano.
7. **`<passengers>-member racing team`** → «squadra da corsa di `<passengers>` membri»: il composto inglese non ha
   corrispettivo, e il segnaposto va trattato come numero.
8. **`collect your payment of <payment>`** → «ritiri il pagamento di `<payment>`», coerente con «accetti il pagamento di»
   di L213.
9. **`taking the most direct route possible`** → «prendendo la rotta più diretta possibile»: registro da corriere.
10. **Nessuna cortesia «Lei»**: il corriere dice «Salve, capitano `<last>`» e poi dà del tu, come il resto della campagna.

## 2. Un errore mio, corretto prima di chiudere

L'asserzione sulle famiglie di `VALUE` diceva `[1, 1, 1, 1, 2, 2]`. Il valore vero è **`[1, 1, 1, 2, 2, 5]`**: «Shipment to
`<planet>`» compare **cinque** volte, non due. Il testo era corretto; il controllo sbagliava, e l'ho corretto lui.

## 3. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 29 unità `PENDING`; il file è tradotto, non approvato.
- **Nessuna missione giocata**: i 56 segnaposto sono verificati nel testo, mai visti sostituiti nel runtime.
- **Nessuna revisione umana**, **nessuna correzione al sorgente**.

## 4. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì |
| ESEGUITO | sì |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (27), `verify.py` exit **0** (18), invariante di file 187/187 |
