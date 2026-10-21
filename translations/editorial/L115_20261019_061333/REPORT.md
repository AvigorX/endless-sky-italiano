# REPORT — L115 · `_ui/tooltips.txt` (avvisi del cantiere, comandi di volo e flotta, opzioni)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| avvisi del cantiere | 1–11 | 1312–1345 | batterie, spinta e virata limitate, energia solare, carburante, iperguida, baie, energia per sparare, equipaggiamento atroce |
| comandi di volo | 12–20 | 1351–1374 | spinta, virata, retromarcia, postbruciatore, mira automatica, atterraggio, salto nell'iperspazio |
| selezione e interazione | 21–33 | 1374–1402 | piano, nave più vicina, scorte, chiamata, abbordaggio, asteroide, scansione |
| armi e torrette | 34–40 | 1405–1423 | armi primarie e secondarie, inseguimento delle torrette, occultamento, puntamento col mouse, virata col mouse |
| pannelli e sistema | 41–47 | 1426–1444 | menu, schermo intero, avanzamento rapido, pausa, aiuto, registro messaggi, carico CPU/GPU |
| flotta | 48–58 | 1447–1471 | schierare i caccia (3 unità), fuoco concentrato, cessate il fuoco, radunata (2), posizione, munizioni, detrito, scansione |
| zoom e testo | 59–66 | 1477–1490 | zoom principale, zoom della vista, allineamento del testo (5 varianti), carattere dell'interfaccia |
| schermo e prestazioni | 67–76 | 1493–1514 | modalità schermo, vsync, accelerazione della camera (4), carico CPU/GPU, sfocatura, grafica, caricamento differito |
| sfondo | 77–86 | 1517–1538 | foschia, campo stellare, zoom fisso, parallasse (4), animazione del menu, lampo dell'iperspazio, effetti di salto |
| contorni, texture, stato | 87–104 | 1541–1566 | contorni nel cantiere (3), nell'HUD (3), navi occultate (3), filtro texture (3), sovrapposizioni di stato (6) |

## 2. Scelte

| nodo | scelta | perché |
|---|---|---|
| `thrusters` · `steering` | **propulsori** · **governo** | L114; «azionare il governo alla massima potenza» |
| `top speed` · `turn rate` · `acceleration` | **velocità massima** · **velocità di virata** · **accelerazione** | glossario |
| `batteries` | **batterie** | L113–L114 |
| `bays` | **baie** | spazio per le navi trasportate |
| `flagship` · `fleet` · `escorts` · `carriers` | **ammiraglia** · **flotta** · **scorte** · **navi portatrici** | glossario |
| `atrocity` | **equipaggiamento atroce** | il contesto è `This outfit is considered an atrocity.` |
| `surge` | **picco** | L113, citato fra virgolette |
| `travel plan` | **piano di viaggio** | |
| `hail` | **chiamare** | «chiama la nave o il pianeta» |
| `right clicking` | **facendo clic col tasto destro** | |
| `hold fire` | **cessate il fuoco** | ordine di flotta |
| `gather around me` | **radunarsi intorno all'ammiraglia** | |
| `hold position` | **mantenere la posizione** | |
| `harvest flotsam` | **raccogliere il detrito** | `flotsam` = detrito |
| `fast-forward` | **avanzamento rapido** | «a velocità tripla» |
| `message log` | **registro messaggi** | |
| `haze` · `starfield` · `parallax` | **foschia** · **campo stellare** · **parallasse** | |
| `motion blur` | **sfocatura da movimento** | |
| `sobel filter` | **filtro di Sobel** | nome proprio dell'algoritmo |
| `status overlays` | **sovrapposizioni di stato** | mostrano scudi e scafo |
| `VRAM` · `vsync` · `HUD` · `CPU` · `GPU` | invariati | acronimi |
| nomi e valori fra virgolette | **identici all'inglese** | sono chiavi di `Preferences` e valori del menu; l'unica eccezione è `surge` → «picco» |

## 3. Difficoltà

1. **72 contesti per 104 unità**, con sei unità nello stesso contesto: è la forma opposta a L114 e vicina a
   L113. Il `check.py` di L114 («max 1») sarebbe rosso su un lotto corretto; qui il controllo è il `Counter`
   esatto con la distribuzione 56/7/5/2/1/1 e l'elenco dei sedici contesti ripetuti.
2. **Le 82 virgolette non sono prosa**: sono chiavi e valori di preferenza. Il controllo utile non è il totale
   ma l'**identità dei testi citati**, per unità: `re.findall(r'"([^"]*)"', it) == ...` sull'inglese. Con una
   sola eccezione dichiarata (unità 10, `"surge"` → `"picco"`, già tradotto da L113).
3. **8 token `<shift>`** dopo quattro finestre a zero. Il testo si costruisce intorno al token («Con `<shift>`,
   …»), e la parità è verificata per unità: le stesse 8 unità, lo stesso ordine.
4. **Tre registri**: avviso all'imperativo («Devi installare…» non serve qui, ma «Se partisse, non potrebbe
   lasciare questo sistema stellare»), etichetta di comando («Accelera l'ammiraglia in avanti.») e descrizione
   di opzione («Imposta l'allineamento orizzontale dei paragrafi nell'interfaccia.»).
5. **23 unità sono voci di elenco** (`- "…": …`): il trattino, i due punti e la citazione fanno parte del
   formato e sono riprodotti in tutte e 23.
6. **Una ripetizione identica** (89/92, `Ship outlines in shops` e `in HUD`): resa identica e dichiarata.
7. **Gate**: minimo 0,88 (unità 4, `limited movement?`), massimo 1,74 (unità 23, `View player info`), media
   1,14; nessuna unità fuori dalla banda comoda 0,70–1,75.

## 4. Numeri osservati

```
unita' 104/104 · TUTORIAL_TIP 104 · tutte PENDING (misurato)
contesti 72 · 56/7/5/2/1/1 · sedici ripetuti · massimo sei (Show status overlays)
tab 0 · virgolette 82 = 82 (38 unita) · token 8 = 8 (<shift>) · quadre 0 · backtick 0
ripetizioni 1 coppia (89/92) resa identica
parole EN 1819 -> IT 1839 (1.011) · rapporto 0.88 - 1.74, media 1.14
righe 1312/1566 · file 667 unita · max(line) 1865 · 430 prima / 133 dopo
FAIL totale: 0 (38 controlli) · verify exit 0 (47 controlli)
sha256[:16] 1c8c5a0ff94ca5b2 · copertura file 534/667 (80,1%)
```

## 5. Stato del progetto

```
TOTALE staging: 26161 unita · 831120 EN · 788916 IT
tooltips.txt: 534/667 (80,1%) · 5 lotti
file completi: quarantuno · residuo traducibile (formula state.py): 5769
residuo misurato: 6400 unità / 145862 parole su 125 file
avanzamento: 26161/32924 unità (79,5%) · 831120/979975 parole (84,8%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (38 controlli), `verify.py` exit **0** (47 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 104 unità restano `PENDING`; nessun tooltip è stato visto nel pannello.
- **Il file non è completo**, ma resta un solo segmento: **133 unità** (righe 1569–1865, **3018 parole**,
  **80 contesti**, 144 virgolette, 1 token `<shift>`). Prossimo contratto `HANDOFF_L116_20261019.md`: chiude il
  file con **un lotto unico** — 1,7 volte la dimensione abituale, deviazione dichiarata, perché un secondo lotto
  da 133 unità costerebbe un ciclo intero per un file che resta a 20%.
- **Nessuna revisione umana**.
