# REVIEW — L137 · `data/starts.txt` (terzo inizio: `Escaping Squalor`)

Coppie EN→IT rilette in `translation.json` (`24133aaf9c9f177d…`). Tutte le 17 unità sono **`PENDING`**.

## 1. Voce

- **La premessa** è amara e asciutta: «Sei cresciuto sulla Terra, un mondo sovrappopolato con poche opportunità… hai
  scoperto che non era molto meglio della Terra».
- **Il capitano** dà un consiglio secco: «Un avvertimento: se non hai voglia di morire presto, dopo il decollo punta a
  nord».
- **Il cassiere** è mellifluo: «"Per tua fortuna, i tassi adesso sono ottimi!"… "Firmi qui." Il cassiere sorride.»
- **Il diario** chiude il conto: «Un'ultima stoccata del Sindacato, avida come sempre, prima della mia libertà.»

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `Escaping Squalor` | **identico** | 1 |
| `600,000 credits` · `0.5%` · `3,580` · `706,571` · `480,000` | **600.000** · **0,5%** · **3.580** · **706.571** · **480.000** | 13, 14, 16 |
| `Earth` | **Terra** | 2 |
| `Antipode` · `Delve` | **invariati** | 2, 10 |
| `Syndicated Systems` | **invariato** | 13 |
| `crushing mortgage` | **mutuo schiacciante** | 4 |
| `scoffs` · `spiel` | **sbuffa** · **sproloquio** | 12 |
| `unrestrained glee` | **gioia sfrenata** | 13 |
| `an interceptor, a light freighter, and a transport ship` | **un intercettore, un mercantile leggero e una nave da trasporto** | 17 |

## 3. Nodi aperti (da non dedurre dopo)

1. **La cortesia resta confinata al dialogo**: il cassiere dà del lei, la narrazione dà del tu. Se un revisore
   «uniformasse» i registri, il controllo sulla cortesia lo segnalerebbe.
2. **Cinque frasi condivise** (5–9) sono rilette da L135: modificarle qui senza modificarle là crea due inizi incoerenti.
3. **`Hai Origins` compare due volte** come `VALUE` nel prossimo lotto (215 e 227): due inizi distinti con lo stesso
   nome, e vanno verificati entrambi.
4. **Le cifre non si arrotondano**: 706.571 è più di 600.000, ed è il punto della scena.
5. **`Delve`, `Antipode` e `Syndicated Systems` restano**: sono nomi.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 17 unità restano `PENDING`.
- **Nessun inizio avviato**: non ho visto Delve né la banca.
- **Nessuna revisione umana**.
- **`starts.txt` è al 56,6%**: 49 unità da fare (due inizi e una nave).

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (29 controlli), `verify.py` exit **0** (28 controlli, invariante di segmento) |
