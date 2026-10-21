# REVIEW — L111 · `_ui/tooltips.txt` (pannelli di nave: il registro lo detta il testo approvato)

Coppie EN→IT rilette in `translation.json` (`dee204e785c7d01b…`). **52 unità sono approvate** e non si toccano:
la revisione editoriale riguarda le **52 nuove** (53–104).

## 1. Voce e registro

- **Il registro dei tooltip non l'ho scelto io**: le 52 unità già approvate danno del **«tu»** («non puoi usarla
  come ammiraglia», «ti occulti», «la tua nave») e usano **«danni da …»** al plurale. Le unità nuove si sono
  allineate. Un pannello che alterna «tu» e «voi» è un difetto che il giocatore vede subito, perché le righe stanno
  una sopra l'altra.
- **Il tono è strumentale**: nessuna narrazione, nessun «voi» narrativo, frasi che iniziano con «Energia»,
  «Carburante», «Calore», «Protezione contro…». Il testo descrive **un valore**, non un'azione.
- **Nessun pathos e nessuna enfasi**: dove il sorgente dice «must temporarily shut down to cool itself off», la resa
  è «deve spegnersi temporaneamente per raffreddarsi».

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità | nota |
|---|---|---|---|
| `(parked)` | **(parcheggiata)** | 1 | approvata: riprodotta |
| `burn protection` / `burn resistance` | **Protezione contro i danni da ustione** / **Danni da ustione resistiti al secondo** | 23, 24 | approvate |
| `corrosion protection` | **Protezione contro i danni da corrosione. Aumenta del fattore indicato la quantità di danni da corrosione che la nave sopporta prima di perdere tanto scafo quanto una nave non protetta.** | 55 | calco dell'unità 23 |
| `corrosion resistance` | **Danni da corrosione resistiti al secondo.** | 56 | participio concordato con «danni» |
| `Cost, in credits.` | **Costo, in crediti.** | 60 | |
| `you can buy them back for the same price you sold them for` | **puoi ricomprarli allo stesso prezzo a cui li hai venduti** | 60 | «tu», come il blocco approvato |
| `fleet capacity` | **capacità della tua flotta** | 61 | |
| `Your flagship and parked escorts do not count` | **L'ammiraglia e le scorte parcheggiate non contano** | 61 | *flagship* → **ammiraglia** (unità 21 approvata) |
| `You may exceed your capacity while landed` | **Puoi superare la capacità mentre sei atterrato** | 61 | |
| `shield discharge damage` | **danni da scarica** | 62–66 | non «scarica degli scudi» nel titolo: il tipo di danno è `scarica` |
| `shield disruption damage` | **danni da disruzione degli scudi** | 67–71 | |
| `Accumulated …` | — | — | non ricorre nelle unità nuove |
| `Limits the maximum speed of a ship.` | **Limita la velocità massima di una nave.** | 72 | |
| `drag reduction` | **Riduce la resistenza.** | 73 | *drag* → **resistenza** |
| `drone bays` / `fighter bays` | **categoria "Drone"** / **categoria "Caccia"** | 74, 81 | virgolette conservate |
| `energy capacity` | **capacità energetica** | 75 | |
| `You will probably also need batteries` | **probabilmente serviranno anche batterie** | 77 | impersonale: qui non serve «tu» |
| `engine capacity needed` / `engine capacity` | **spazio motori** | 78, 79 | coerente con «spazio carico» approvato |
| `energy protection` | **Protezione contro i danni da energia** | 80 | |
| `flotsam` | **detrito** | 82 | |
| `hit force` | **forza d'urto** | 83 | |
| `An ordinary hyperdrive jump consumes 100 fuel.` | **Un salto normale con iperguida consuma 100 di carburante.** | 84, 85 | ripetuto, reso **identico** |
| `Fuel is replenished for free when you land on an inhabited planet.` | **Il carburante si rifornisce gratis quando atterri su un pianeta abitato.** | 85 | «atterri», non «atterrate» |
| `gun ports` | **porti per cannoni** | 91, 92 | |
| `Guns always fire straight forward` | **I cannoni sparano sempre dritto in avanti** | 91 | |
| `heat dissipation` | **irradia il calore in eccesso** | 93 | verbo del sorgente (*radiates*) |
| `heat generation` | **generazione di calore** | 94 | |
| `must temporarily shut down` | **deve spegnersi temporaneamente** | 94 | |
| `heat capacity` | **calore massimo … prima di surriscaldarsi** | 96 | reso per funzione, non letterale |
| `hull (repair)` | **Robustezza totale dello scafo e velocità di riparazione** | 97 | *disabled* → «messa fuori uso» |
| `the smallest of ships are disabled when their hull strength drops below about 45%` | **le navi più piccole vengono messe fuori uso quando la robustezza dello scafo scende sotto circa il 45%** | 97, 98 | ripetuto nelle due unità, reso identico |
| `repair delay period` | **periodo di ritardo della riparazione** | 100, 103 | |
| `Modifies … by the given factor` | **Modifica del fattore indicato …** | 101, 104 | |

## 3. Nodi aperti (da non dedurre dopo)

1. **Le 52 unità `APPROVED` non si riscrivono.** Se una revisione futura «migliora» il testo approvato, rompe
   l'accordo con il database e il `check.py` va rosso: è voluto.
2. **«ustione» è il termine approvato**, non «bruciatura». La prima stesura diceva «bruciatura» ed era sbagliata per
   coerenza interna al pannello.
3. **«tu» e non «voi»** nei tooltip: il registro del pannello è fissato dal blocco approvato.
4. **«danni da …» al plurale** con participio concordato («resistiti»), anche dove l'inglese usa il singolare
   (`damage resisted per second`).
5. **`ammiraglia`, `spazio carico`, `spazio motori`**: tre lessemi già fissati; non introdurre «nave ammiraglia» né
   «spazio per i motori».
6. **Zero token in tutto il file**: nessun `<ship>`, nessun `<planet>`. Se ne comparisse uno, va riprodotto.
7. **104 contesti = 104 unità**: qui il contesto **non** raggruppa più unità, e il `verify.py` lo verifica.
8. **`mkparts.py` e `mkparts2.py`**: il primo è la stesura superata (non legge il DB), il secondo è quello valido.
   Chi riprende deve eseguire **`mkparts2.py`**.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 52 unità restano `PENDING`, 52 `APPROVED` sono state **lette** e riprodotte.
- **Nessun caricamento nel gioco**: nessun tooltip è stato visto nel pannello, **e la resa a schermo non è
  verificata** (il testo può essere troncato dal pannello, e questo lo si scopre solo giocando).
- **Nessuna revisione umana**.
- **Il file non è completo**: 563 unità residue.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 4 parti, `translation.json`, `mkparts2.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (31 controlli), `verify.py` exit **0** (28 controlli) |
