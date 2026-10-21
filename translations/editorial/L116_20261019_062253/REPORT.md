# REPORT — L116 · `_ui/tooltips.txt` (chiude il file: interfaccia, regole di gioco, abbordaggio)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| sovrapposizioni di stato | 1–7 | 1569–1587 | ammiraglia, scorte, nemici, neutrali, missili, torrette con angoli morti, scanner per asteroidi |
| HUD e radar | 8–24 | 1590–1618 | evidenziazione, rotazione dell'icona, etichette dei pianeti, mini-mappa, radar cliccabile, allarme, messaggi di flotta |
| mira e fuoco | 25–33 | 1621–1637 | virata col mouse, torrette col mouse, mira automatica (3), fuoco automatico, inseguimento delle torrette |
| scelte automatiche | 34–50 | 1640–1662 | asteroidi (4 strategie), priorità di abbordaggio (4), munizioni delle scorte (4), detrito (5) |
| caccia e flotta | 51–60 | 1665–1684 | riparazione (2), ritiro dei caccia danneggiati (3), carico, equipaggio, parcheggio, priorità dell'ammiraglia |
| interfaccia | 61–93 | 1687–1763 | scadenze, mappa, scorciatoie, aiuto, avanzamento rapido, vendite, zoom, font, notifiche, registro, tema |
| regole di gioco | 94–131 | 1769–1856 | svalutazione, navi personaggio, NPC, ramscoop universale, distanze, flotte di razzia, limiti di flotta, morte permanente, salvataggi |
| abbordaggio | 132–133 | 1862–1865 | oggetto nel carico, oggetto installato |

## 2. Scelte

| nodo | scelta | perché |
|---|---|---|
| `status overlay` | **sovrapposizione di stato** | L115 |
| `blindspots` | **angoli morti** | le torrette con arco cieco |
| `mini-map` · `radar` | **mini-mappa** · **radar** | |
| `alert indicator` | **indicatore di allarme** | sonoro, visivo o entrambi |
| `fixed weapons` · `non-homing` | **armi fisse** · **armi non a inseguimento** | |
| `HP` · `health` | **punti vita** · **salute** | L114–L115 |
| `expected value` · `quality` | valori invariati | `"expected value"`, `"quality"` |
| `boarding target priority` | **priorità di abbordaggio** | valore citato invariato |
| `ammo` · `frugal` | **munizioni** · `"frugal"` invariato | è una personalità del gioco |
| `carrier` · `carried ships` · `docked` | **portatrice** · **navi trasportate** · **attraccate** | L115 |
| `series` · `parallel` | invariati | valori di impostazione |
| `permadeath` | **morte permanente** | |
| `snapshots` · `autosaves` | **istantanee** · **salvataggi automatici** | |
| `person ship` | **nave personaggio** | nave unica legata a un personaggio |
| `weight` | invariato fra virgolette | termine della definizione delle navi personaggio |
| `gamerule` | **regola di gioco** | ricorre 11 volte |
| `raid fleets` | **flotte di razzia** | |
| `cargo attractiveness` · `deterrence` | **attrattiva del carico** · **deterrenza** | meccanica delle razzie |
| `administrative cost` · `administrative capacity` | **`"administrative cost"`** invariato · **capacità amministrativa** | il primo è citato fra virgolette, il secondo è prosa |
| `lock on death` ecc. | invariati | valori di impostazione |
| `(unset)` | invariato | marcatore del gioco |

## 3. Difficoltà

1. **Il file si chiude**: 133 unità sono **tutte** quelle che restavano. Il `verify.py` non poteva restare
   «di segmento» (L115 pretendeva un'unità successiva): l'invariante è diventato **di file** e legge i sei
   `translation.json` del path, dimostrando **667/667 unità coperte, `sovrapposti = 0`**.
2. **80 contesti su 133 unità**, con **8 quaterne** e **5 gruppi da cinque**: il `check.py` di L115 (72 contesti,
   distribuzione 56/7/5/2/1/1) qui è rosso con la traduzione giusta.
3. **I primi quattro contesti hanno tre spazi iniziali** (`tip:   Show flagship overlay`): riprodurli esatti era
   necessario per l'handoff e per il verify.
4. **144 virgolette**, tutte chiavi/valori/gamerule: il controllo è l'identità dei testi citati **per unità**.
   Tre unità (122–124) hanno la **virgola dentro le virgolette** (`"ship cap,"`): il `mkparts.py` è abortito una
   volta perché l'avevo messa fuori, e la correzione è stata **riprodurre il sorgente**, non allentare il
   controllo.
5. **Zero `VALUE` e zero `UI_LABEL` in questo blocco**: i tipi sono 133 `TUTORIAL_TIP` e basta, quindi ogni
   unità è stata tradotta. La regola di L113 («`UI_LABEL` e `VALUE` identici al sorgente») resta valida per gli
   altri file, non qui.
6. **Zero ripetizioni**: 133 inglesi distinti, verificato; nessun duplicato italiano da giustificare.
7. **Gate**: minimo 0,77 (unità 28, `Automatic aiming`), massimo 1,59 (unità 13, `Show planet labels`), media
   1,09; nessuna unità fuori dalla banda comoda.

## 4. Numeri osservati

```
unita' 133/133 · TUTORIAL_TIP 133 · tutte PENDING (misurato)
contesti 80 · 62/1/4/8/5 · massimo cinque unita · primi quattro con tre spazi iniziali
tab 0 · virgolette 144 = 144 (66 unita) · token 1 = 1 (<shift>) · quadre 0 · backtick 0
ripetizioni 0 (asserito)
parole EN 3018 -> IT 2995 (0.992) · rapporto 0.77 - 1.59, media 1.09
righe 1569/1865 · file 667 unita · max(line) 1865 · 534 prima / 0 dopo
FAIL totale: 0 (38 controlli) · verify exit 0 (47 controlli, invariante di file)
sha256[:16] 9a630cfede888bed · copertura file 667/667 (100,0%)
```

## 5. Stato del progetto

```
TOTALE staging: 26294 unita · 834138 EN · 791911 IT
tooltips.txt: 667/667 (100.0%) · 12084 EN -> 12495 IT · 6 lotti · FILE COMPLETO
file completi: quarantadue · residuo traducibile (formula state.py): 5636
residuo misurato: 6267 unità / 142844 parole su 124 file
avanzamento: 26294/32924 unità (79,9%) · 834138/979975 parole (85,1%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 4 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (38 controlli), `verify.py` exit **0** (47 controlli, 667/667 coperte) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 133 unità restano `PENDING`; nessun tooltip è stato visto nel pannello.
- **Il file è completo in staging, non nel gioco**: `_ui/tooltips.txt` non è mai stato caricato.
- **Prossimo file**: `data/human/pirate jobs.txt` (279 unità, 4.780 parole), primo segmento righe **20–1624**
  (**98 unità**, **1.804 parole**, **31 contesti**, 6 famiglie di token) nel contratto `HANDOFF_L117_20261019.md`.
- **Nessuna revisione umana**.
