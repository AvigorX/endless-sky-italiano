# REVIEW — L112 · `_ui/tooltips.txt` (scafo, autoriparazione, spinta inversa, scudi)

Coppie EN→IT rilette in `translation.json` (`3ff21c44bf59b9fc…`). Tutte le 120 unità sono **`PENDING`**: nessuna
approvata in questa finestra, quindi la revisione editoriale copre tutto il lotto.

## 1. Voce e registro

- **Strumentale e impersonale**, come i pannelli: «Calore prodotto al secondo…», «Modifica del fattore indicato…»,
  «Il numero di secondi necessari…». Il «tu» compare **solo** dove il sorgente si rivolge al giocatore («puoi essere
  multato», «devi comunque pagarne la manutenzione», «mentre sei occultato», «quando provi ad abbordarla»), come nel
  blocco approvato di L111.
- **Nessun «voi»**: verificato dal `check.py` con una regex sulle forme di cortesia plurale. È la coerenza col
  pannello che contiene anche le 52 righe approvate.
- **I nove tipi di danno** hanno una resa sola: ionizzazione, disturbo, disruzione, interferenza sui motori, scarica,
  corrosione, perdita di carburante, ustione, perforazione.

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità | nota |
|---|---|---|---|
| `Heat produced per second when repairing the hull.` | **Calore prodotto al secondo quando si ripara lo scafo.** | 1 | stampo del blocco approvato (L111 unità 99–104) |
| `the repair delay period` | **il periodo di ritardo della riparazione** | 2, 6, 101, 104, 107, 110 | ripetuto, reso identico |
| `Modifies the ship's total hull strength by the given factor.` | **Modifica del fattore indicato la robustezza totale dello scafo della nave.** | 4 | |
| `Repairs usually consume energy and may generate heat as well.` | **Le riparazioni di solito consumano energia e possono generare calore.** | 5 | |
| `disabled` (ship) | **messa fuori uso** | 8–20, 21–23 | *non* «distrutta» |
| `The number of seconds it takes for …` | **Il numero di secondi necessari perché …** | 7–11, 119–120 | formula unica per sei unità |
| `The heat applied when a disabled ship repairs itself.` | **Il calore applicato quando una nave messa fuori uso si ripara da sola.** | 12 | |
| `The ion damage applied when …` | **I danni da ionizzazione applicati quando …** | 13–20 | otto varianti, stesso stampo |
| `absolute threshold` | **soglia assoluta** · «ha la precedenza sugli altri attributi» | 21 | |
| `threshold percentage` | **percentuale di robustezza dello scafo residua** | 23 | |
| `illegal` | **illegale** | 27 | «per cui puoi essere multato» |
| `income` / `operating income` | **reddito** / **reddito operativo** | 28, 61 | |
| `inertia reduction` | **riduzione dell'inerzia** | 29 | |
| `ion protection` | **Protezione contro i danni da ionizzazione** — «Modifica del fattore indicato» | 30 | il sorgente usa `Modifies`, non `Increases` |
| `landing speed` · `wormhole` | **velocità di atterraggio** · **wormhole** invariato | 36 | |
| `jump speed` | **la velocità massima alla quale la nave può saltare** | 41 | |
| `hyperdrive` / `jump drive` | **iperguida** / **motore di salto** | 42–43 | |
| `jump mass cost` · `jump base mass` | **costo di massa del salto** · **massa base del salto** | 45–46 | |
| `leak` (fuel) | **perdita di carburante** | 19, 47–51 | |
| `maintenance costs` | **costi di manutenzione** | 52 | «devi comunque pagarne la manutenzione» |
| `mass with no cargo` | **massa senza carico** | 54 | |
| `turn rate` | **velocità di virata** | 54–55 | |
| `max speed` / `w/ afterburner` | **velocità massima** / **con postbruciatore** | 56–57 | |
| `outfit scan` | **scansione degli equipaggiamenti** | 62–66 | |
| `outfit space` | **spazio equipaggiamenti** | 66, 69 | coerente con «spazio carico» approvato |
| `general-purpose space` | **spazio generico** | 67–68 | |
| `overheat damage` | **danni da surriscaldamento** | 70–71 | |
| `optical jamming` · `radar jamming` | **disturbo ottico** · **disturbo radar** | 72, 77 | i tre comparativi conservati |
| `optical size` | **dimensione ottica** | 73 | |
| `piercing` | **perforazione** | 74–76 | «armi perforanti», «danni da perforazione» |
| `ramscoop` | **ramscoop** invariato | 78 | glossario; «vento stellare» |
| `required crew / bunks` | **equipaggio richiesto e cuccette** | 79 | «cuccette in più» |
| `mandatory crew` | **equipaggio obbligatorio** | 81 | «non può essere sostituito dall'automazione» |
| `reverse thrust` | **spinta inversa** | 82–95 | «senza doversi girare» |
| `scan interference` | **interferenza di scansione** | 96 | 50% / 75% / 90% |
| `scram drive` | **motore scram** | 97 | «purché la tua velocità rientri in questo margine» |
| `self destruct` | **autodistruzione** | 98 | «quando provi ad abbordarla o a catturarla» |
| `sells for` | **valore di vendita** | 99 | «bottino … completamente deprezzato» |
| `shield generation` | **rigenerazione degli scudi** | 109–111 | |
| `shield permeability` | **permeabilità degli scudi** | 113–115 | alta / bassa / in occultamento |
| `shields (charge)` | **robustezza totale degli scudi e velocità di rigenerazione** | 116 | |
| `shield delay` · `depleted shield delay` | **ritardo degli scudi** · **scudi esauriti** | 119–120 | |

## 3. Nodi aperti (da non dedurre dopo)

1. **Otto varianti identiche nello stampo** (13–20) e **otto nella spinta inversa** (88–95): il `check.py` verifica
   che ognuna contenga la formula comune e che le otto del danno siano **tutte distinte** fra loro.
2. **`Modifies` vs `Increases`** nel sorgente: l'unità 30 dice «Modifica del fattore indicato», non «Aumenta del
   fattore indicato» come le altre protezioni. La differenza è nel testo inglese e va conservata.
3. **`A value of one`** = «un valore di uno» (unità 66): è un'unità di misura, non il numero uno come conteggio.
4. **`disabled` è «messa fuori uso»**, mai «distrutta»: una nave messa fuori uso è recuperabile, e il gioco lo dice
   in tre unità.
5. **Zero virgolette e zero token**: in L111 erano 14 virgolette; qui zero, e il controllo lo **asserisce**.
6. **`tip:    w/ afterburner:`** ha quattro spazi nel contesto: è un dettaglio del file, non del testo, e non entra
   in traduzione.
7. **`wormhole` e `ramscoop` restano invariati**; `iperguida` è solo per *hyperdrive*, `motore di salto` per
   *jump drive*.
8. **`plunder`** → **bottino**: è il carico saccheggiato, non «preda».

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 120 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: nessun tooltip è stato visto nel pannello, e il **troncamento a schermo** non è
  verificabile senza gioco.
- **Nessuna revisione umana**.
- **Il file non è completo**: 443 unità residue.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 4 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (29 controlli), `verify.py` exit **0** (33 controlli) |
