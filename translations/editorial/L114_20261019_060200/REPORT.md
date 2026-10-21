# REPORT — L114 · `_ui/tooltips.txt` (armi: danni per secondo e per colpo, avvisi del cantiere)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| armi, danni per secondo | 10–47 | 1009–1120 | scudi, scafo, estraibili, carburante, calore, energia, ionizzazione, disturbo, interferenza, disruzione, scarica, corrosione, perdita, ustione; varianti in percentuale; voci allo sparo |
| cadenza e torrette | 48–51 | 1123–1132 | colpi al secondo e note sulle batterie, virata della torretta e moltiplicatore, arco |
| inseguimento | 52–56 | 1135–1147 | tipo di guida, aggancio, ottico, infrarossi, radar |
| armi, danni per colpo | 57–94 | 1150–1258 | la stessa serie misurata per colpo, con le quattro coppie identiche |
| precisione e area | 95–100 | 1261–1276 | imprecisione, raggio di esplosione, robustezza del missile, anti-missile, raggio traente, precisione di estrazione |
| avvisi del cantiere | 101–110 | 1282–1309 | cuccette, surriscaldamento, energia, carburante, propulsori, governo, nave fredda, solo postbruciatore, solo retromarcia |
| intestazioni e portata | 1–9 | 976–1006 | motori e governo, armi da abbordaggio, oggetti speciali, munizioni e loro uso, portata, velocità iniziale, modificatore e portata di attenuazione |

## 2. Scelte

| nodo | scelta | perché |
|---|---|---|
| `thrusters` · `steering systems` | **propulsori** · **sistemi di governo** | glossario L112–L113 (`thrust` = spinta, `turn rate` = velocità di virata) |
| `Hand to Hand` | **armi da abbordaggio** | il contesto è la cattura di una nave |
| `outfits that can be installed in a ship` | **equipaggiamenti installabili su una nave** | `outfits` = equipaggiamenti (glossario) |
| `ammo` · `ammo usage` | **munizioni** · **unità di munizioni** | |
| `range` | **portata** | coerente con «portata del salto» e «portata massima dei cannoni» (L113) |
| `dropoff modifier` · `dropoff range` | **modificatore di attenuazione** · **portata massima di attenuazione** | `dropoff` = caduta dei danni con la distanza |
| `minable damage` · `minable objects` | **danni agli oggetti estraibili** | comprende asteroidi e altro materiale estraibile |
| `total health` | **salute totale** | è l'integrità dell'oggetto estraibile, non lo scafo |
| `Only half as effective when the target's shields are up` | **Efficace solo a metà quando gli scudi del bersaglio sono attivi** | stessa formula in 14 unità |
| `weapon failure` | **avaria delle armi** | non «inceppamento»: vale anche per energia e torrette |
| `Ionization / Scrambling / Slowing / Shield disruption` | **ionizzazione / disturbo / interferenza sui motori / disruzione degli scudi** | glossario L111–L113 |
| `wears off over time` | **svanisce col tempo** | |
| `leak through` | **«passare»** | fra virgolette come nel sorgente |
| `dealt over time` | **inflitti nel tempo** | distingue il danno continuo dal danno istantaneo |
| `damage per second` · `damage per shot` | **… al secondo** · **… per colpo** | verifica automatica: ogni `per second` inglese contiene «al secondo», ogni `per shot` «per colpo» |
| `turret turn rate` · `turret turn multiplier` · `arc` | **velocità di virata della torretta** · **moltiplicatore** · **ampiezza angolare** | |
| `homing type` · `direct` · `leading` | **tipo di guida** · **«diretta»** · **«anticipata»** | `leading` = puntare alla posizione futura |
| `tracking` | **aggancio** | «mantenere l'aggancio al bersaglio» |
| `optical / infrared / radar tracking` | **aggancio ottico / a infrarossi / radar** | |
| `inaccuracy` | **imprecisione** | «un valore di uno = al massimo un grado fuori bersaglio» |
| `blast radius` | **raggio di esplosione** | |
| `missile strength` · `anti-missile` | **robustezza del missile** · **anti-missile** | |
| `tractor beam` · `flotsam` | **raggio traente** · **detrito** | `flotsam` = detrito (glossario) |
| `mining precision` · `yields` | **precisione di estrazione** · **raccolto** | |
| `bunks` | **cuccette** | L112 |
| `unresponsive at random times` | **non rispondere ai comandi in momenti imprevedibili** | |
| `overheat the moment it takes off` | **surriscalderà appena decolla** | |
| `too cold to use some of its engines while idle` | **troppo fredda per usare alcuni motori da ferma** | |

## 3. Difficoltà

1. **Quattro coppie di ripetizioni legittime** (17/64, 18/65, 19/66, 36/83): l'inglese è identico, cambia solo
   il contesto (`/ second` contro `/ shot`). Il `check.py` le **elenca** e verifica la resa identica; le due
   coppie quasi-parallele (37/84, 38/85) hanno inglese **diverso** e rese diverse — appiattirle sarebbe stato
   un duplicato italiano non giustificato.
2. **I contesti tornano uno per unità** (110 su 110): il controllo di L113 (87 contesti, nove doppi) qui
   sarebbe rosso su un lotto corretto. La forma è stata **rimisurata**, non copiata.
3. **Dodici virgolette** in cinque unità, con una unità da **quattro** (52): la citazione è doppia
   (`"diretta"` e `"anticipata"`), e il controllo è per unità.
4. **Formule fisse**: **28** unità con `per second` e **30** con `per shot` (58 in tutto), **18** con «Only half as
   effective when the target's shields are up». La coerenza è verificata da due controlli meccanici
   (`per second → al secondo`, `per shot → per colpo`), non a occhio: 28 = 28 e 30 = 30.
5. **`shots / second`** è l'unica unità lunga del blocco (66 parole inglesi): spiega la regola delle batterie
   e il caso delle armi a fuoco intermittente. Resa 1,01.
6. **`% firing fuel / shot`** (92) parla del **carburante della nave** («the ship's total fuel»), non del
   bersaglio: la resa non usa «del bersaglio», che sarebbe un errore di senso.
7. **Il gate di lunghezza** non ha prodotto outlier: minimo 0,93 (unità 99, `tractor beam`), massimo 1,56
   (unità 12, `minable damage / second`).

## 4. Numeri osservati

```
unita' 110/110 · TUTORIAL_TIP 110 · tutte PENDING (misurato)
contesti 110 · nessun doppio · ripetizioni 4 coppie (17/64, 18/65, 19/66, 36/83) rese identiche
tab 0 · virgolette 12 = 12 · token 0 · quadre 0 · backtick 0
parole EN 1816 -> IT 1905 (1.049) · rapporto 0.93 - 1.56, media 1.18
righe 976/1309 · file 667 unita · max(line) 1865 · 320 prima / 237 dopo
FAIL totale: 0 (36 controlli) · verify exit 0 (41 controlli)
sha256[:16] 83513c92ec109aa8 · copertura file 430/667 (64,5%)
```

## 5. Stato del progetto

```
TOTALE staging: 26057 unita · 829301 EN · 787077 IT
tooltips.txt: 430/667 (64,5%) · 4 lotti
file completi: quarantuno · residuo traducibile (formula state.py): 5873
residuo misurato: 6504 unità / 147681 parole su 125 file
avanzamento: 26057/32924 unità (79,1%) · 829301/979975 parole (84,6%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (36 controlli), `verify.py` exit **0** (41 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 110 unità restano `PENDING`; nessun tooltip è stato visto nel pannello.
- **Il file non è completo**: **237 unità** residue; prossimo contratto `HANDOFF_L115_20261019.md` (righe
  1312–1566, **104 unità**, **72 contesti** con 16 gruppi ripetuti, **82 virgolette**, **8 token** `<shift>`).
- **Nessuna revisione umana**.
