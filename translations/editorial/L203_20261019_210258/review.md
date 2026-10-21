# REVIEW — L203 · `hai outfits.txt` (terzo lotto)

Coppie EN→IT rilette in `translation.json` (`81a25808d92d805f…`). Tutte le 9 unità sono **`PENDING`**.

## 1. Decisioni di resa

1. **`chiave di volta`** per *keystone*: prosegue la scelta di L200 (mai «pietra chiave»), verificata su due occorrenze.
2. **`disturbatore`** per *jammer*: il glossario ha già «disturbatore radar»; qui il termine si specializza nei nomi
   di prodotto, che restano inglesi (`Cuttlefish Jammer`, `Octopus Jammer`).
3. **`generatori di scudi`** e **`matrice dello scudo`**: termini fissati, usati alla lettera nelle unità 4 e 5.
4. **`gittata`** per *range* (unità 1), non «portata»: nel contesto delle armi il gioco usa già «gittata».
5. **`contraltare`** per *a counter to* (unità 2): sostantivo tecnico-militare, evita «una contromisura» che sarebbe
   stato un altro termine di gioco.
6. **`bersaglio illusorio`** per *illusory target* e **`aggancio`** per *lock* (unità 2): lessico dei sensori.
7. **`circuiti di sicurezza aggirati`** per *safety circuits bypassed* (unità 3): «aggirati» rende l'elusione, non la
   disattivazione pulita.
8. **Soggetto corretto in unità 5**: l'inglese dice *the shifts it makes … causes*, con il verbo al singolare su un
   soggetto plurale. La resa italiana usa «le variazioni … producono» — corregge l'accordo **nella lingua d'arrivo**
   senza toccare il gioco, e l'anomalia è dichiarata qui.
9. **`a intermittenza`** per *sporadically* (unità 6): rende l'irregolarità, non la rarità.
10. **`olofilm`** per *holo-film* (unità 8): prestito compatto coerente con `olopad`; «film olografico» sarebbe stato
    lungo e pleonastico dentro una frase già densa.
11. **`zona comune`** per *public common area* (unità 8): la parola «pubblica» è superflua in italiano, dove «comune» la
    implica.
12. **`basta a identificare`** per *it is sufficient to* (unità 9): più asciutto di «è sufficiente per», e il registro
    resta tecnico.

## 2. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 9 unità `PENDING`.
- **Nessun equipaggiamento installato nel gioco**, **nessun testo visto a schermo**, **nessuna revisione umana**.
- **Nessuna correzione al sorgente**: l'errore d'accordo su *causes* resta nel gioco.

## 3. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — `parts/part01.json`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (24 controlli), `verify.py` exit **0** (17 controlli) |
