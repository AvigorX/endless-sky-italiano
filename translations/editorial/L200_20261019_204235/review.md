# REVIEW — L200 · `hai jobs.txt` (quinto lotto, chiude il file)

Coppie EN→IT rilette in `translation.json` (`3ff06bf4f8b326c1…`). Tutte le 23 unità sono **`PENDING`**.

## 1. Decisioni di resa

1. **`VALUE` identici (11/11)**: `Superstitious Hai to <planet>` — nome del lavoro, inglese per convenzione, `<planet>`
   risolto dal motore.
2. **`chiave di volta`** per *keystone*: scelto fra le due rese presenti in staging («chiave di volta» nelle missioni
   che introducono l'oggetto, «pietra chiave» altrove). Motivo: è la resa del lavoro `Fetching keystones`
   («Recuperare le chiavi di volta»), cioè lo stesso oggetto; ed è quella che rende leggibile «nave dotata di chiave
   di volta».
3. **`Ha chiesto` / `Hanno chiesto`**: l'inglese usa *they* anche per il singolare (matriarca, anziano). In italiano
   l'accordo segue il soggetto: «Ha chiesto» per i due singolari, «Hanno chiesto» per famiglie e gruppi. La frase non è
   identica in tutte e sei le unità, ed è corretto così.
4. **`sulla propria nave`** per *their ship*: evita il pronome possessivo plurale riferito a un soggetto singolare
   («la loro nave» suonerebbe sbagliato per la matriarca).
5. **`braccianti`** per *farm workers*: mestiere preciso, distinto da `allevatori` (*ranchers*) e da `operai tessili`
   (L198). Tre soggetti, tre parole, nessuna sovrapposizione.
6. **`casa di riposo`** per *retirement home*: resa già presente in staging.
7. **`Questo anziano Hai`** e **`Un gruppo di <bunks> Hai anziani`**: due costruzioni diverse per due soggetti diversi
   (singolo / gruppo), non variazione stilistica.

## 2. Due asserzioni corrette

1. **Conteggio delle occorrenze di «chiave di volta»**: avevo scritto `== 12`; il valore reale è **18** (2 nelle sei
   unità con la frase, 1 nelle sei senza). Corretto **prima** di eseguire.
2. **Controllo dei contesti**: confrontavo la lista per **unità** (23 voci, con i nomi ripetuti) con la lista dei
   **contesti distinti** (12). È uscito `FAIL 1`; corretto il confronto con `dict.fromkeys`, non il testo. Il resto del
   `check.py` era già verde.

## 3. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 23 unità `PENDING`.
- **Nessun lavoro accettato nel gioco**, **nessun testo visto a schermo**, **nessuna revisione umana**.
- **Nessuna correzione al sorgente**: le incoerenze del gioco si conservano.
- **`hai jobs.txt` è chiuso in staging, non approvato**: 175/175 tradotte, 0 approvate.

## 4. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — `parts/part01.json`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, compreso il `FAIL 1` intermedio |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (25 controlli), `verify.py` exit **0**, `FILE CHIUSO: 175/175` |
