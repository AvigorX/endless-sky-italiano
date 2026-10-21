# REVIEW — L113 · `_ui/tooltips.txt` (scanner, emporio, consumi: 87 contesti per 96 unità)

Coppie EN→IT rilette in `translation.json` (`dc0775e3161aa2b4…`). Tutte le 96 unità sono **`PENDING`**.

## 1. Voce e registro

- **Strumentale**, come i pannelli: «Gli scanner strategici ti permettono di vedere…», «Tieni premuto Shift,
  Control o Alt per…», «La somma dell'energia consumata e del calore generato…».
- **«tu»** al giocatore, come il blocco approvato: «ti permettono di vedere», «evitandoti la multa», «Occupano uno
  degli alloggiamenti per torrette **della tua nave**», «Per installare un'arma **devi** anche avere…».
- **Imperativo nei pannelli d'azione** (emporio e cantiere): «Acquista…», «Vendi…», «Installa…», «Disinstalla…»,
  «Trasferisci…», «Sposta…». È la forma del gioco, non una scelta di stile.

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità | nota |
|---|---|---|---|
| `Protection provided against shield damage` | **Protezione contro i danni agli scudi** | 1 | |
| `before it loses as much shields as an unprotected ship` | **prima di perdere tanti scudi quanto una nave non protetta** | 1 | formula approvata |
| `Prevents a ship from making … sounds` | **Impedisce a una nave di produrre i suoni …** | 2–3 | |
| `before it as slowed` (refuso del sorgente) | **prima di essere rallentata** | 4 | refuso normalizzato e dichiarato |
| `Energy produced depending on how far … from the star` | **Energia prodotta in base alla distanza … dalla stella al centro del sistema** | 9–10 | |
| `Strategic scanners allow you to view … when it is within range` | **Gli scanner strategici ti permettono di vedere, quando il bersaglio è a portata, …** | 11–22 | ordine della subordinata anticipato per leggibilità |
| `crew complement` | **equipaggio a bordo** | 12, 14 | |
| `Range finders` | **telemetri** | 19 | «non c'è limite di portata» |
| `thermal level` | **livello termico** | 20 | |
| `gun hardpoint` · `turret hardpoint` | **alloggiamento per cannoni** · **per torrette** | 22 | |
| `weapon offset` | **scostamento dell'arma** | 22 | |
| `Higher thrust increases …` | **Una spinta maggiore aumenta …** | 23 | |
| `Turn rate, in degrees per second` | **Velocità di virata, in gradi al secondo** | 38 | |
| `It uses up one of your ship's turret mounts` | **Occupano uno degli alloggiamenti per torrette della tua nave** | 53 | |
| `Tons of weapon space …` | **Tonnellate di spazio armi …** | 55–56 | |
| `scan brightness` · `scan concealment` | **visibilità** · **occultamento** | 57–58 | |
| `Buy from the outfitter and install onto …` | **Acquista dall'emporio e installa sulla nave selezionata (o sulle navi selezionate)** | 59 | |
| `Hold Shift, Control, or Alt to … 5, 20, or 500 …` | **Tieni premuto Shift, Control o Alt per … 5, 20 o 500 …** | 60, 62, 64, 66, 68, 70, 72 | sette occorrenze, verbo diverso |
| `Sell from cargo, storage, or the currently selected ship(s), in that order` | **Vendi dal carico, dal deposito o dalla nave selezionata …, in quest'ordine** | 61 | |
| `Uninstall … to cargo if there is space or to storage if there isn't` | **Disinstalla … verso il carico se c'è spazio, altrimenti verso il deposito** | 65 | |
| `Transfer the outfit from planetary storage to cargo if possible` | **Trasferisci l'equipaggiamento dal deposito planetario al carico se possibile** | 67 | |
| `Sell the hulls … but retain the outfits in storage` | **Vendi gli scafi … ma conserva gli equipaggiamenti nel deposito** | 74 | |
| `Price the ship itself would sell for without any outfits installed` | **Il prezzo a cui si venderebbe la nave stessa senza equipaggiamenti installati** | 75 | |
| `idle` | **inattiva** | 77–86 | citata fra virgolette in nove unità |
| `This is in addition to the "idle" amount` | **Si somma alla quantità "inattiva"** | 78–86 | nove occorrenze identiche |
| `the average value over time` | **il valore medio nel tempo** | 83 | |
| `net change` | **variazione netta** | 87, 89 | citata due volte nell'89 |
| `Energy capacity` · `Heat capacity` | **capacità energetica** · **capacità termica** | 88–89 | |
| `surge` | **picco** | 90 | «il massimo di energia … in un solo istante» |
| `Guns` · `Turrets` · `Secondary Weapons` · `Ammunition` · `Systems` · `Power` | **Cannoni · Torrette · Armi secondarie · Munizioni · Sistemi · Energia** | 91–96 | intestazioni di categoria |

## 3. Nodi aperti (da non dedurre dopo)

1. **87 contesti per 96 unità**: i nove contesti doppi sono `turning`, i sei `outfitter`, `shipyard: b`, `capacity`.
   Un controllo «un contesto per unità» boccia un lotto corretto.
2. **Le sei coppie «azione + scorciatoia»** hanno lo stesso contesto e la seconda unità ripete la formula con il
   verbo cambiato: acquistare, vendere, installare, disinstallare, spostare, immagazzinare. Sei verbi distinti, sei
   rese distinte.
3. **`Si somma alla quantità "inattiva"`** compare **nove volte identica** (unità 78–86) e la ripetizione è
   legittima: il sorgente ripete, l'italiano ripete.
4. **`"variazione netta"` due volte nella stessa unità** (89): quattro virgolette, e il conteggio per unità lo
   verifica.
5. **Refuso del sorgente** (unità 4, «before it as slowed»): normalizzato, non propagato.
6. **`emporio` e `cantiere`** sono le due schermate (outfitter, shipyard): non sono «negozio» e «cantiere navale».
7. **`nave selezionata (o sulle navi selezionate)`**: il gioco permette la selezione multipla, e la resa non
   sceglie arbitrariamente il singolare.
8. **`The range is proportional to the square root of this value.`** chiude **dieci** delle dodici unità degli
   scanner: il telemetro (19) non ha portata e quello delle armi (22) usa una formula diversa.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 96 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: nessun tooltip è stato visto nel pannello, e il troncamento a schermo non è
  verificabile senza gioco.
- **Nessuna revisione umana**.
- **Il file non è completo**: 347 unità residue.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (30 controlli), `verify.py` exit **0** (38 controlli) |
