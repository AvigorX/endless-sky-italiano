# REVIEW — L209 · `coalition news.txt` (quarto lotto)

Coppie EN→IT rilette in `translation.json` (`7e550942341d014e…`). Tutte le 21 unità sono **`PENDING`**.

## 1. Decisioni di resa

1. **Le tre famiglie ripetute sono rese una volta sola** e copiate: le unità 4/9/14, 5/10/15 e 6/11/16 hanno lo stesso
   testo italiano, come hanno lo stesso testo inglese. Nessuna variazione per «spezzare la ripetizione»: la ripetizione
   è del gioco, non un difetto da correggere.
2. **`jump drive`** resta inglese: è un equipaggiamento con un nome suo, non un nome comune.
3. **`our Houses` → «le nostre Case»**: istituzione al plurale, tradotta. I nomi propri (`House Ablomab`, `House Plumtab`,
   L208) restano inglesi. Stessa regola di `Coalition Games` → «Giochi della Coalizione».
4. **`Arachi`** resta invariato come nome di lingua («imparare a parlare l'Arachi»), come in L207 era il plurale dei
   parlanti.
5. **`ringworld` → «ringworld»** (unità 21): è il nome del mondo artificiale della Coalizione, non un nome comune.
6. **`longcow hide` → «pelle di longcow»**: coerenza con L206-L208.
7. **`translation boxes` → «traduttori»**: rende il dispositivo, non la scatola. In L208 avevo già scelto «traduttori».
8. **`field trip` → «gita di studio»** con virgolette singole: il viaggio di laureati Saryd che il mercante ha
   trasportato era, ironicamente, una gita scolastica finita con un arresto.
9. **`Something wrong with them` → «niente di strano in loro»**: resa negativa naturale, che conserva il senso del
   controllo senza colpa.
10. **`Mind it, I do not` → «Dargli peso, io non lo faccio»**: mantiene l'inversione senza un calco innaturale.

## 2. Due asserzioni mie, corrette prima di chiudere

1. **I contesti civilian non hanno il prefisso `coalition`**: il database dice `arach civilian`, `kimek civilian`,
   `saryd civilian`, mentre `merchant` e `vendor` lo hanno. Il controllo è stato riscritto per misurare la **forma** dei
   conteggi (3, 3, 5, 5, 5) invece di fissare chiavi che avevo indovinato.
2. **`'field trip,'` ha la virgola dentro le virgolette**: cercavo `'field trip'` e non lo trovavo. Ora il controllo
   verifica la forma reale e aggiunge che gli apici sono **2 per lato** in entrambe le lingue — così l'asserzione misura
   una corrispondenza, non la mia memoria del testo.

## 3. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 21 unità `PENDING`.
- **Nessuna schermata vista nel gioco**, **nessuna revisione umana**.
- **Nessuna correzione al sorgente**: le ripetizioni restano, le virgole dentro le virgolette restano.

## 4. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì |
| ESEGUITO | sì |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (24), `verify.py` exit **0** (19) |
