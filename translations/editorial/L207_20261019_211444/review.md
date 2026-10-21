# REVIEW — L207 · `coalition news.txt` (secondo lotto)

Coppie EN→IT rilette in `translation.json` (`af8d352da08f8841…`). Tutte le 17 unità sono **`PENDING`**.

## 1. Decisioni di resa

1. **Inversione Saryd** applicata a tutte le 17 unità, con la stessa regola di L206: predicato o complemento in testa,
   verbo in coda, soggetto dopo.
2. **`charity workers in blue` → «volontari in blu»**: mantiene il dettaglio visivo e non aggiunge «operatori» che
   l'inglese non dice.
3. **`the trials we candidates go through` → «le prove che noi candidati affrontiamo»**: il «noi» esplicito regge
   l'inversione e suona naturale in italiano marcato.
4. **`holiday pay` → «paga vacanze»**, non «indennità ferie»: il parlante è un turista entusiasta, non un burocrate.
5. **`arcology` → «arcologia»**: prestito tecnico corrente, e serve a rendere il contrasto con «pianeta senza».
6. **`consul Aulori`**: prestito latino, coerente con `magister`. «Console» in italiano è un apparecchio: evitato.
7. **`Ring of Wisdom`** invariato: nome di stazione.
8. **`Saryd Traveler`** invariato: nome di nave.
9. **`Arachi`** invariato: il plurale è del parlante, non della fazione.
10. **`blood sample` → «campione di sangue»**, **`immune system` → «sistema immunitario»**: termini standard.
11. **`rude neighbors` → «vicini maleducati»**: «maleducati» rende *rude* meglio di «scortesi», che qui sarebbe formale.
12. **Cortesia e registro**: unità 14 con «ti dispiacerebbe» (registro unico «tu» della campagna) invece di «le
    dispiacerebbe». Dichiarato: è l'unico punto in cui la politica di registro prevale sulla cortesia del sorgente.

## 2. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 17 unità `PENDING`.
- **Nessuna schermata vista nel gioco**, **nessuna revisione umana**: il registro Saryd è una proposta editoriale, e una
  revisione umana potrebbe legittimamente preferire un'inversione più leggera.
- **Nessuna correzione al sorgente**: i plurali anomali (`Arachi`) e le frasi in ordine normale restano come sono.

## 3. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì |
| ESEGUITO | sì |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (23), `verify.py` exit **0** (17) |
