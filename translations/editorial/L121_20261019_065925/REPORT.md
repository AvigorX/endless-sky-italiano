# REPORT — L121 · `campaign events.txt` (schieramento, empori, Zug, Greenrock)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| schieramento iniziale | 1–10 | 282–357 | Ingot, New Wales, New Austria, le basi della Marina |
| Central Outfitters | 11–25 | 664–689 | l'emporio, la merce di Kraz e Delta V, la cassetta delle Javelin |
| Zug | 26–29 | 975–984 | Vecchio Porto, Il Porto, Porto Nuovo, «L'Ampliamento» |
| Kornephoros e Clink | 30–35 | 1002–1069 | avamposto occupato, porto sull'isola vulcanica, minatori |
| Oathkeepers e conservatorio | 36–39 | 1156–1244 | Farpoint, la branca neutrale, Winter e il Conservatorio |
| Thule | 40–44 | 1261–1266 | mondo montuoso, fine della pirateria, Smuggler's Den, gli anarchici |
| Greenrock | 45–56 | 1300–1332 | occupata, abbandonata, recuperata: schiavi e «Mike's Mustelids» |

## 2. Scelte

| nodo | scelta | perché |
|---|---|---|
| `new stock` | **identico** | è una `UI_LABEL`: nome di nodo, non prosa |
| `Southern Rim` | **Bordo Meridionale** | regione; dichiarata qui per la prima volta |
| `Kraz Cybernetics` · `Delta V` · `Syndicated Systems` | **invariati** | nomi di aziende |
| `Javelins` · `Lovelace Sidewinders` | **Javelin** · **Lovelace Sidewinder** | nomi di armi e navi |
| `outfitter` | **emporio** | coerenza con L113 |
| `afterburners` · `cooling equipment` · `generators` | **postbruciatori · sistemi di raffreddamento · generatori** | L114, L120 |
| `nuke-happy secessionists` | **secessionisti amanti delle bombe atomiche** | |
| `Old Port / The Port / New Port / The Expansion` | **Vecchio Porto / Il Porto / Porto Nuovo / L'Ampliamento** | fra virgolette come nel sorgente |
| `chief ship foundry` | **principale fucina di navi** | |
| `Poseidon Industries` | **la Poseidon Industries** | azienda, invariata |
| `Navy Oathkeepers` | **gli Oathkeepers della Marina** | nome di branca, invariato |
| `Free Worlds Conservatory` | **il Conservatorio dei Mondi Liberi** | |
| `terraforming technology and expertise` | **tecnologia e competenze di terraformazione** | |
| `Smuggler's Den` · `Grendel Station` | **Smuggler's Den** · **la stazione Grendel** | nomi di stazione |
| `privateers` · `smugglers` | **corsari** · **contrabbandieri** | |
| `refurbished starships` | **astronavi ricondizionate** | |
| `Mike's Mustelids` | **«Mike's Mustelids»** | insegna di bottega, invariata |
| `weasels, ferrets, wolverines` | **donnole, furetti, ghiottoni** | |
| `slave markets` · `slaves` | **mercati di schiavi** · **schiavi** | |

## 3. Difficoltà

1. **La `UI_LABEL` va isolata**: se entra in «tutte tradotte», il lotto è rosso su una traduzione corretta. Va
   esclusa e verificata **identica**, con l'asserzione che sia una sola.
2. **Due battute non chiuse dal sorgente** (unità 22 e 24): la resa riproduce una virgoletta sola, e il `check.py`
   verifica che siano **esattamente quelle due**.
3. **46 virgolette di dialogo** contro **28 unità con tab**: due assi di forma da misurare separatamente, per
   unità.
4. **Contesti molto sbilanciati** (15 / 10 / 5 / 4×3 / 3×2 / 2×4): la distribuzione si misura, non si «corregge».
5. **Una firma ambigua, di nuovo**: `closest thing that the pirates` combaciava con l'apertura di Greenrock (45/49)
   **e** con `Greenrock recovered` (53). Sostituita con `at least until the Free Worlds occupied it`.
6. **Una distribuzione attesa sbagliata**: il primo `mkparts.py` elencava i contesti come `{2: 3, 3: 2, 1: 1, …}`,
   mentre il dato è `{15: 1, 10: 1, 5: 1, 4: 3, 3: 2, 2: 4}`. Corretto l'atteso.
7. **Un solo token** (`<origin>`) e nessuna quadra: le asserzioni «vuote» sono scritte, non saltate.
8. **Gate**: minimo 0,87 (unità 24, la battuta del dépliant), massimo **1,28** (unità 3, la base della
   Marina su Ingot); rapporto complessivo 1,04.

## 4. Numeri osservati

```
unita' 56/56 · DESCRIPTION 41 · MISSION_TEXT 14 · UI_LABEL 1 (identica) · tutte PENDING
contesti 12 (15/10/5/4x3/3x2/2x4) · testi distinti 52 (4 coppie ripetute)
tab 28 unita · virgolette 46 (2 unita con una sola, come il sorgente) · token 1 · quadre 0
parole EN 2486 -> IT 2404 (0.967) · rapporto 0.87 - 1.28, media 1.05
righe 282/1332 · file 108/150 (72,0%) · 52 prima / 42 dopo · confine riga 1338
FAIL totale: 0 (32 controlli) · verify exit 0 (29 controlli)
sha256[:16] 292f0d3b327b16f9
```

## 5. Stato del progetto

```
TOTALE staging: 26681 unita · 843659 EN · 801243 IT
campaign events.txt: 108/150 (72.0%) · 2 lotti · 4741 EN -> 4597 IT
file completi: quarantatre · residuo traducibile (formula state.py): 5249
residuo misurato: 5881 unità / 133325 parole su 123 file
avanzamento: 26681/32924 unità (81,0%) · 843659/979975 parole (86,1%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (32 controlli), `verify.py` exit **0** (29 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: le 56 unità restano `PENDING`; nessun evento è stato caricato nel gioco.
- **Nessuna revisione umana**.
- **Il file non è completo**: **42 unità** residue (righe 1338–3468). Il prossimo lotto lo chiude
  (`HANDOFF_L122_20261019.md`: 42 unità, 2.220 parole, 18 contesti, **zero token**).
- **`Bordo Meridionale` è una scelta nuova**: nessun lotto precedente aveva tradotto `Southern Rim`.
