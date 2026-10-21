# REVIEW — L210 · `coalition news.txt` (quinto lotto)

Coppie EN→IT rilette in `translation.json` (`ee5ce8eed7ac5542…`). Tutte le 19 unità sono **`PENDING`**.

## 1. Decisioni di resa

1. **`Coalition Games` → «Giochi della Coalizione»**: nome comune di evento, coerente con L206.
2. **`arbiter`** resta prestito latino: «arbitro» in italiano è il direttore di gara e falserebbe il rango.
3. **`consuls` → «consoli»**, **`tribune` → «tribuno»**: titoli comuni con forma italiana naturale. `consul` come titolo
   personale resta prestito (`consul Aulori`, L207).
4. **`hedgelion quills` → «aculei di hedgelion»**: la creatura resta invariata, come `longcow`.
5. **`Arachi armor replicas` → «repliche di armature Arachi»**: il popolo resta invariato anche come aggettivo.
6. **`the outside` → «l'esterno»**: in questo file è lo spazio oltre la bolla della Coalizione, e «l'esterno» lo rende
   senza aggiungere maiuscole che l'inglese non ha.
7. **`inspector` → «ispettrice»**: Sedlitaris è donna (*her expedition*), e l'italiano lo marca.
8. **`girl` (al posto di `inspector`) → «ragazza»**: il disprezzo dei parlanti che non credono alla spedizione sta nella
   scelta lessicale, che va conservata.
9. **`job board` → «bacheca delle missioni»**: termine già fissato in L212 (primo lotto di `deep jobs.txt`).
10. **`on the edge` → «sul filo del rasoio»**: rende l'ansia dello spettatore meglio di «in tensione».
11. **`tapestry` → «arazzo»**, **`trinkets` → «ninnoli»**: registro del venditore, non aulico.

## 2. Due asserzioni mie, corrette prima di chiudere

1. **`'field trip,'` ha la virgola dentro le virgolette**: cercavo `'field trip'` e non lo trovavo. Ora il controllo
   verifica la forma reale e che gli apici siano due per lato in entrambe le lingue.
2. **`endswith('acquisto')` falliva perché la stringa finisce `acquisto."`**: il punto e la virgoletta fanno parte della
   stringa. Corretto con `rstrip(QUOTE + '.')` — e la stessa correzione serviva sul lato inglese (*purchase.*).

## 3. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 19 unità `PENDING`.
- **Nessuna schermata vista nel gioco**, **nessuna revisione umana**.
- **Nessuna correzione al sorgente**: le ripetizioni e la punteggiatura interna alle virgolette restano.

## 4. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì |
| ESEGUITO | sì |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (23), `verify.py` exit **0** (17) |
