# REVIEW — L114 · `_ui/tooltips.txt` (armi: danni per secondo e per colpo, avvisi del cantiere)

Coppie EN→IT rilette in `translation.json` (`83513c92ec109aa8…`). Tutte le 110 unità sono **`PENDING`**.

## 1. Voce e registro

- **Strumentale e impersonale**, come le schede del pannello: «Danni agli scudi inflitti al secondo», «Riduce
  la velocità di virata, l'accelerazione e la velocità massima del bersaglio».
- **«tu»** al giocatore quando la scheda parla della sua nave: «Danni allo scafo inflitti **alla tua nave** al
  secondo», «**Devi** installare dei propulsori».
- **Avvisi del cantiere all'imperativo presente**, come il gioco li mostra: «Devi aggiungere altro
  raffreddamento o rimuovere parte degli equipaggiamenti che producono calore».
- Nessun «voi» (verificato nei due script): il registro del blocco approvato (L111) resta «tu».

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità | nota |
|---|---|---|---|
| `Thrusters and steering systems` | **Propulsori e sistemi di governo** | 1 | |
| `Weapons that your crew uses when trying to capture a ship` | **Armi che il tuo equipaggio usa quando tenta di catturare una nave** | 2 | |
| `not outfits that can be installed in a ship` | **non sono equipaggiamenti installabili su una nave** | 3 | |
| `Total range of this weapon` | **Portata totale di quest'arma** | 6 | `range` = portata |
| `initial velocity of projectiles` | **velocità iniziale dei proiettili** | 7 | |
| `maximum dropoff range` · `dropoff modifier` | **portata massima di attenuazione** · **modificatore di attenuazione** | 8–9 | |
| `Shield / Hull damage dealt per second` | **Danni agli scudi / allo scafo inflitti al secondo** | 10–11 | |
| `Minable damage` · `minable objects` | **danni agli oggetti estraibili** | 12, 26, 59, 73 | |
| `Only half as effective when the target's shields are up` | **Efficace solo a metà quando gli scudi del bersaglio sono attivi** | 13–15, 17–18, 27–29, 60–61, 63–65, 74–76 | 18 unità, formula unica |
| `A negative amount means fuel is added` | **Un valore negativo indica un aumento di carburante** | 13, 60 | |
| `chance of weapon failure` | **probabilità di avaria delle armi** | 17, 36, 64, 83 | non «inceppamento» |
| `wears off over time` | **svanisce col tempo** | 16–19, 35–42, 64–66, 82–85 | |
| `"leak through"` | **«passare»** | 19, 38, 66, 85 | virgolette riprodotte |
| `Shield disruption` | **disruzione degli scudi** | 19, 38, 66, 85 | glossario L111–L113 |
| `adding additional shield disruption becomes more difficult` | **aggiungere altra disruzione diventa più difficile** | 19, 66 | |
| `imparting disruption on yourself does not lose effectiveness` | **infliggerti disruzione non perde efficacia** | 38, 85 | |
| `as damage leaks past shields instead of disrupting them` | **man mano che i danni attraversano gli scudi invece di disromperli** | 19, 66 | |
| `your shields become more leaky` | **i tuoi scudi diventano più permeabili** | 38, 85 | `permeability` = permeabilità (L112) |
| `dealt over time by this weapon` | **inflitti nel tempo da quest'arma** | 20–23, 67–70, 86–89 | |
| `as a percentage of the target's total shield strength` | **come percentuale della robustezza totale degli scudi del bersaglio** | 24, 70 | |
| `total health` | **salute totale** | 26, 73 | l'oggetto estraibile non ha «scafo» |
| `Fuel loss caused per second` | **Perdita di carburante causata al secondo** | 27, 74 | |
| `maximum heat capacity` · `energy capacity` | **capacità termica massima** · **capacità energetica** | 28–29, 44, 75–76 | |
| `firing energy / heat / fuel` | **energia / calore / carburante allo sparo**, resi «consumata / generato / consumato al secondo (o per colpo)» | 30–32, 77–79 | |
| `firing hull / shields` | **danni allo scafo / agli scudi inflitti alla tua nave** | 33–34, 80–81 | |
| `firing ion / scramble / slowing / disruption / discharge / corrosion / leak / burn` | **riduce l'energia / avaria delle armi / velocità di virata / scudi disrotti / scudi / scafo / carburante / calore** | 35–42, 82–89 | verbo diverso per famiglia |
| `shot / second` | **colpi al secondo** | 48 | «proiettili sparati al secondo» |
| `turret turn rate` · `turret turn multiplier` · `arc` | **velocità di virata della torretta** · **moltiplicatore** · **ampiezza angolare della protezione** | 49–51 | |
| `homing type` · `"direct"` · `"leading"` | **tipo di guida** · **«diretta»** · **«anticipata»** | 52 | quattro virgolette |
| `tracking` · `optical / infrared / radar tracking` | **aggancio** · **aggancio ottico / a infrarossi / radar** | 53–56 | |
| `Damage dealt to minable objects per shot, in lieu of hull damage` | **Danni inflitti agli oggetti estraibili per colpo, invece dei danni allo scafo** | 59 | |
| `projectiles with "leading" will lead their trajectory` | **quelli con guida «anticipata» puntano alla posizione futura** | 52 | |
| `A weapon will not fire if the ship's batteries do not have at least this amount of energy stored` | **Un'arma non spara se le batterie della nave non hanno almeno questa quantità di energia immagazzinata** | 77 | |
| `Maximum inaccuracy … at most one degree off-target` | **Imprecisione massima … al massimo un grado fuori bersaglio** | 95 | |
| `Everything within this distance (including friendly ships)` | **Tutto ciò che si trova entro questa distanza (comprese le navi alleate)** | 96 | |
| `resistance to anti-missile shots` · `power of the anti-missile shots` | **resistenza ai colpi anti-missile** · **potenza dei colpi anti-missile** | 97–98 | |
| `tractor beam` · `flotsam` | **raggio traente** · **detrito** | 99 | |
| `mining precision` · `yields` · `higher / lower yields` | **precisione di estrazione** · **raccolto** · **raccolti più abbondanti / più scarsi** | 100 | |
| `bunks` | **cuccette** | 101, 107 | L112 |
| `unresponsive at random times` | **non rispondere ai comandi in momenti imprevedibili** | 107 | |
| `too cold to use some of its engines while idle` | **troppo fredda per usare alcuni motori da ferma** | 108 | |
| `afterburner` · `reverse thruster` | **postbruciatore** · **propulsore di spinta inversa** | 109–110 | glossario L112 |

## 3. Nodi aperti (da non dedurre dopo)

1. **Quattro coppie di inglese identico** — 17/64 (`scrambling`), 18/65 (`slowing`), 19/66 (`disruption`),
   36/83 (`firing scramble`) — sono la **stessa scheda** misurata per secondo e per colpo: le rese sono
   **identiche** e il `check.py` le elenca. Differenziarle per eleganza rompe il controllo.
2. **Due coppie quasi-parallele non sono coppie**: `firing slowing` (37) e `firing slowing / shot` (84)
   differiscono in inglese («of the ship **when this weapon is fired**» contro il semplice «of the ship»), e
   così `firing disruption` (38) e `/ shot` (85). Hanno **rese diverse**, e il controllo dei duplicati
   italiani lo esige.
3. **110 contesti per 110 unità**: la forma «un contesto per unità» vale qui e non in L113 (87 su 96). Il
   controllo va rimisurato a ogni finestra.
4. **`% firing fuel / shot` (92)** è l'unica voce della serie `% firing` che parla del **carburante della
   nave** e non del bersaglio: «come percentuale del carburante totale della nave».
5. **`total health`** (26, 73) si applica agli **oggetti estraibili**: reso «salute totale», non «robustezza
   dello scafo», che sarebbe un termine di nave.
6. **`/ second` e `/ shot` sono unità di misura del contesto**, non del testo: la verifica è meccanica
   (28 unità con `per second` → 28 «al secondo»; 30 con `per shot` → 30 «per colpo»), non stilistica.
7. **La prossima finestra cambia forma di nuovo**: righe 1312–1566 hanno **72 contesti per 104 unità** (fino a
   **6** unità per contesto), **82 virgolette** e **8 token** `<shift>`. Il `check.py` di L114, con «110
   contesti, max 1, zero token», è rosso su quel lotto: va riscritto, non copiato.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 110 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: nessuna scheda è stata vista nel pannello, e il troncamento a schermo non è
  verificabile senza gioco.
- **Nessuna revisione umana**.
- **Il file non è completo**: 237 unità residue.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (36 controlli), `verify.py` exit **0** (41 controlli) |
