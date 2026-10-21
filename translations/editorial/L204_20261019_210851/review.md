# REVIEW — L204 · `hai outfits.txt` (quarto lotto)

Coppie EN→IT rilette in `translation.json` (`12342441647f81f7…`). Tutte le 19 unità sono **`PENDING`**.

## 1. Decisioni di resa

1. **`battery pack` → «pacco batterie»** (4 volte): forma tecnica corrente, più precisa di «batteria», che nel gioco
   indica anche l'arma a ioni.
2. **`heat footprint` → «impronta termica»** (2 volte): mantiene la metafora del sorgente e resta breve.
3. **`energy capacity` → «capacità energetica»**, **`energy density` → «densità energetica»**: termini fissati.
4. **`fusion generators` → «generatori a fusione»**, **`fission reactors` → «reattori a fissione»**.
5. **`fuel cells` → «celle a combustibile»**: standard, e il paragone con la Sand Cell resta leggibile.
6. **`thruster/engine` distinti**: «propulsore» per *thruster*, «motore» per *engine*. Nell'unità 19 il testo inglese
   usa *thruster* per il pezzo e *engines* per la famiglia: la distinzione è mantenuta.
7. **`oversized engines` → «motori sovradimensionati»**: rende lo spreco voluto, non un semplice «grandi».
8. **`ion weapons`/`Ion Cannon`**: il nome dell'arma resta inglese, «armi a ioni» per la categoria.
9. **`the Deep`** e **`Deep Sky`** invariati: fazione e azienda.
10. **`Pebble Core` e `Sand Cell`** invariati: nomi di prodotto, anche quando il testo li usa come nomi comuni.
11. **`pocket of the Galaxy` → «porzione della Galassia»**: «tasca» sarebbe stato troppo colloquiale.
12. **`stand up to their ion weapons` → «resistere alle loro armi a ioni»**: resa per senso, l'inglese è idiomatico.

## 2. Un errore mio, corretto prima di chiudere

L'asserzione sul conteggio di «pacco batterie» diceva **5**; il valore misurato è **4**. Non era un errore del testo:
l'unità 10 parla di *battery model*, non di *battery pack*. Il controllo è stato riscritto per **legare i due conteggi**
(italiano e inglese) invece di fissare un numero: così l'asserzione misura una relazione, non una costante.

## 3. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 19 unità `PENDING`.
- **Nessun equipaggiamento installato nel gioco**, **nessun testo visto a schermo**, **nessuna revisione umana**.
- **Nessuna correzione al sorgente**.

## 4. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì |
| ESEGUITO | sì |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (22), `verify.py` exit **0** (18) |
