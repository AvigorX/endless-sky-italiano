# REVIEW — L211 · `coalition news.txt` (sesto e ultimo lotto)

Coppie EN→IT rilette in `translation.json` (`2a3bcc367bdd3978…`). Tutte le 16 unità sono **`PENDING`**.

## 1. Decisioni di resa

1. **La citazione spezzata non si «normalizza»**: le unità 6 e 11 restano una virgoletta ciascuna, e i paragrafi 7–10
   restano senza. È una scelta di fedeltà alla struttura del file, non un'omissione.
2. **`'Beyond the Hyperdrive'` resta inglese** e fra apici singoli: è il titolo di un libro, e il titolo non si traduce
   quando l'autrice è un personaggio del gioco e il libro è un oggetto di mondo.
3. **`Anna Fangvin`** invariato: nome proprio di persona.
4. **`amenity goods and services` → «beni e servizi essenziali»**: rende il senso del soccorso senza l'eco turistica di
   «comfort».
5. **`charity` → «beneficenza»**, **`charity goods` → «beni di beneficenza»**: registro dell'opera pia, coerente.
6. **`Arach Houses` → «Case Arach»**: istituzione, come «our Houses» → «le nostre Case» in L209.
7. **`trinkets` → «ninnoli»**: già scelto in L210 per lo stesso venditore.
8. **`flyers` → «volantini»**: lessico da strada, non da ufficio.
9. **`school supplies` → «materiale scolastico»**: più naturale di «forniture scolastiche».
10. **`the job board` → «bacheca delle missioni»**: termine fissato.

## 2. Tre difetti dei miei controlli, corretti prima di chiudere

1. **`l'ho` non era riconosciuto** come verbo finale: la regex dei token spezza sull'apostrofo e tagging «l'ho» come
   parola intera richiede di elencarlo. Senza la correzione, l'unità 7 sarebbe risultata un'eccezione falsa al registro.
2. **Il controllo dei residui inglesi segnalava `'Beyond the Hyperdrive'`**: il titolo contiene ` the `. Ora la
   scansione esclude esplicitamente titolo e nome proprio — sono testi da conservare, e il controllo lo **dichiara**
   invece di ignorarli in silenzio.
3. **`endswith('gioia')` falliva** perché la stringa finisce `gioia!"`: serviva `rstrip` di virgoletta e punto
   esclamativo. Stessa famiglia di errore di L210 (`acquisto."`) — è la seconda volta, e ora è annotata fra le trappole.

## 3. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 16 unità `PENDING`; il file è tradotto, non approvato.
- **Nessuna schermata vista**, **nessuna revisione umana**: la resa del registro resta una proposta.
- **Nessuna correzione al sorgente**: la citazione spezzata e i titoli inglesi restano come sono.

## 4. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì |
| ESEGUITO | sì |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (25), `verify.py` exit **0** (19), invariante di file 112/112 |
