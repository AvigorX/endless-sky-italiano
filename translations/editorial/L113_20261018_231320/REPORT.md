# REPORT — L113 · `_ui/tooltips.txt` (scanner, pannelli outfitter e shipyard, consumi)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| scudi e motori | 1–8, 23–52 | 691–845 | protezione e resistenza agli scudi, suoni silenziosi, raccolta solare, spinta e virata con dodici voci di consumo e danno |
| scanner | 11–22 | 721–758 | strategico, tattico, mobilità ×3, equipaggio, energia, carburante, manovra, telemetro, termico, armi |
| alloggiamenti e spazio armi | 53–56 | 848–857 | torrette montabili, spazio armi occupato e disponibile |
| scansione del carico | 57–58 | 860–863 | visibilità e occultamento, multa evitata |
| pannelli outfitter e shipyard | 59–76 | 869–909 | sei azioni ×2 (azione + scorciatoia), vendita di scafi, prezzi |
| consumi | 77–90 | 915–952 | inattiva, in movimento, spinta, spinta inversa, postbruciatore, virata, sparo, scudi+scafo, riparazione, ricarica, variazione netta, capacità, picco |
| categorie armi | 91–96 | 958–973 | Cannoni, Torrette, Armi secondarie, Munizioni, Sistemi, Energia |

## 2. Scelte

| nodo | scelta | perché |
|---|---|---|
| `shield protection` | **Protezione contro i danni agli scudi** | «tanti scudi quanto una nave non protetta» |
| `silent jumps` · `silent scans` | **suoni dell'iperguida o del motore di salto** · **suoni della scansione** | |
| `slowing damage` | **danni da interferenza sui motori** | coerenza con L111/L112 |
| `solar collection` · `solar heat` | **raccolta solare** · **calore solare** | «in base alla distanza … dalla stella al centro del sistema» |
| `strategic / tactical scanners` | **scanner strategici / tattici** | |
| `crew complement` | **equipaggio a bordo** | |
| `range finders` | **telemetri** | «non c'è limite di portata» |
| `thermal level` | **livello termico** | |
| `gun hardpoint` · `turret hardpoint` | **alloggiamento per cannoni** · **per torrette** | |
| `weapon offset` | **scostamento dell'arma** | |
| `thrust` · `turn` · `turn rate` | **spinta** · **forza di virata** · **velocità di virata** | |
| `turret mounts` | **alloggiamenti per torrette** | |
| `weapon space` | **spazio armi** | |
| `scan brightness` · `scan concealment` | **visibilità** · **occultamento** | «evitandoti la multa» |
| `outfitter` · `shipyard` | **emporio** · **cantiere** | contesti `tip:outfitter: b` ecc. |
| `planetary storage` | **deposito planetario** | |
| `selected ship(s)` | **nave selezionata (o sulle navi selezionate)** | il gioco permette la selezione multipla |
| `retain the outfits in storage` | **conserva gli equipaggiamenti nel deposito** | |
| `empty hull` · `+ outfits` | **senza equipaggiamenti installati** · **tutti gli equipaggiamenti di questa nave** | |
| `idle` | **inattiva** | etichetta citata fra virgolette |
| `net change` | **variazione netta** | citata due volte nell'unità 89 |
| `surge` | **picco** | «il massimo di energia … in un solo istante» |
| `Guns / Turrets / Secondary Weapons / Ammunition / Systems / Power` | **Cannoni / Torrette / Armi secondarie / Munizioni / Sistemi / Energia** | intestazioni di categoria |

## 3. Difficoltà

1. **I contesti sono meno delle unità** (87 su 96): la forma «un contesto per unità» dei due lotti precedenti qui
   fallisce. Il controllo è «87 contesti, nove doppi, nessuno triplo», con i nove elencati; il `verify.py` li
   ricalcola dal database.
2. **Il primo `mkparts.py` è abortito** su un'attesa sbagliata dei contesti doppi: avevo previsto `turning` e
   `capacity` ma non `shipyard: b`, e avevo messo una coppia inesistente. Corretto **l'atteso**, non il dato: i nove
   doppi misurati sono `turning`, sei `outfitter`, `shipyard: b`, `capacity`.
3. **22 virgolette** dopo **zero** nel lotto precedente: sono etichette del pannello citate (`"inattiva"`,
   `"variazione netta"`), e il controllo è per unità — nove unità con due, una con quattro.
4. **Refuso del sorgente normalizzato**: unità 4 dice «before it **as** slowed as an unprotected ship»; tradotto
   «prima di essere rallentata». Il refuso non si propaga e si dichiara qui.
5. **Sei coppie azione + scorciatoia** (outfitter `b/s/i/u/c/r`): stesso contesto, due unità, e la seconda è sempre
   identica nella formula («Tieni premuto Shift, Control o Alt per … 5, 20 o 500 … alla volta. Tieni premuta una
   combinazione di questi tasti per quantità maggiori.») con il verbo che cambia. Le sei coppie sono **distinte fra
   loro** solo nel verbo: acquistare, vendere, installare, disinstallare, spostare, immagazzinare.
6. **`the currently selected target`** ricorre in cinque scanner e nelle torrette: reso sempre «il bersaglio
   attualmente selezionato».
7. **`The range is proportional to the square root of this value.`** chiude **dieci** delle **dodici** unità degli
   scanner (le altre due hanno formule diverse: il telemetro non ha portata, quello delle armi parla di «portata
   dello scanner»): reso identico in tutte e dieci, e il `check.py` non lo segnala come ripetizione perché il resto
   della frase differisce.

## 4. Numeri osservati

```
unita' 96/96 · TUTORIAL_TIP 96 · tutte PENDING (misurato)
contesti 87 · nove doppi (18 unita) · 78 unita con contesto singolo
tab 0 · virgolette 22 = 22 · token 0 · quadre 0 · ripetizioni 0
parole EN 1808 -> IT 1864 (1.031) · rapporto 0.87 - 1.54, media 1.16
righe 691/973 · file 667 unita · max(line) 1865 · 224 prima / 347 dopo
FAIL totale: 0 (30 controlli) · verify exit 0 (38 controlli)
sha256[:16] dc0775e3161aa2b4 · copertura file 320/667 (48,0%)
```

## 5. Stato del progetto

```
TOTALE staging: 25947 unita · 827485 EN · 785172 IT
tooltips.txt: 320/667 (48,0%) · 3 lotti
file completi: quarantuno · residuo traducibile (formula state.py): 5983
residuo misurato: 6614 unità / 149497 parole su 125 file
avanzamento: 25947/32924 unità (78,8%) · 827485/979975 parole (84,4%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (30 controlli), `verify.py` exit **0** (38 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 96 unità restano `PENDING`; nessun tooltip è stato visto nel pannello.
- **Il file non è completo**: **347 unità** residue; prossimo contratto `HANDOFF_L114_20261018.md` (righe 976–1309,
  **110 unità**, **4 coppie di ripetizioni**, **12 virgolette**).
- **Nessuna revisione umana**.
