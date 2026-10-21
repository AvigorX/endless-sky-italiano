# REPORT — L131 · `boarding missions.txt` (la coda: il relitto, le riparazioni, la trappola)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| `Turn in Tarquin` | 1 | 695 | la `DESCRIPTION` che chiude la missione di L130 |
| l'abbordaggio e la scelta | 2–4 | 723–727 | lo scafo stabile, «ripara» o «recupera» |
| riparare per gradi | 5–44 | 728–836 | tre ordini (motori, scafo, alimentazione), i successi parziali, la valvola che si apre |
| i disastri | 45–47 | 839–845 | alimentazione che si spegne, deformazione nello scafo, refrigerante nello scafo |
| la fuga | 48–58 | 850–870 | il rottame, l'esplosione, le tre corse al portello |
| la nave non vola | 59–62 | 880–889 | il saccheggio, la luce lampeggiante `"astronavi ostili"`, il virus che svuota il conto |
| il recupero | 63–76 | 892–959 | moduli, la custodia con 325.000 crediti, la mappa, la detonazione, lo scafo che cede |

## 2. Scelte

| nodo | IT | nota |
|---|---|---|
| `Deliver captain Tarquin to law enforcement` | **alle forze dell'ordine** | `DESCRIPTION` |
| `derelict hull` | **scafo abbandonato** | |
| `bigger score` | **colpo grosso** | |
| `repair the power` | **riparare l'alimentazione** | non «energia»: impianto |
| `powersurge` | **sovratensione** | |
| `wiring embedded in the hull` | **cavi rotti incassati nello scafo** | |
| `secondary valve is mechanical` | **la valvola secondaria è meccanica** | |
| `coolant` | **refrigerante** | |
| `The ship thrums to life` | **La nave vibra e prende vita** | ripetuto identico 3 volte |
| `With bated breath` | **con il fiato sospeso** | |
| `secondary valve` · `hull` · `engines` · `power` | **valvola secondaria** · **scafo** · **motori** · **alimentazione** | coerenza lessicale su 76 unità |
| `bolt for the airlock` | **scattare verso il portello** | |
| `you're sure that you look like an action hero` | **sei sicuro di sembrare un eroe d'azione** | |
| `tuck and roll` | **ti raccogli e rotoli** | |
| `loot and pilfer some outfits` | **saccheggiare e portarti via qualche modulo** | `outfits` = moduli |
| `hostile spacecraft` | **"astronavi ostili"** | virgolette **doppie**, come il sorgente |
| `malicious software` | **software malevolo** | |
| `derelict hunters` | **cacciatori di relitti** | |
| `creak and groan` | **scricchiolare e gemere** | |

## 3. Difficoltà

1. **Il lotto chiude il file**: `verify.py` passa a **invariante di file** (89 + 75 + 76 = 240, sovrapposti 0,
   `max(line) = 959`).
2. **52 testi distinti su 76**: 24 ripetizioni, il massimo finora. Le parti comuni sono costanti nel costruttore, e il
   `check.py` verifica le occorrenze delle due frasi più ripetute (4 ciascuna).
3. **Zero `VALUE` e zero `UI_LABEL`**: due asserzioni vuote **scritte**, non omesse.
4. **74 unità su 76 con tab**: quasi ogni testo è una battuta o un'opzione indentata.
5. **22 token in 2 famiglie** (`<origin>` 14, `<payment>` 8): sequenza verificata per unità.
6. **Le virgolette sono doppie nei due sensi**: il sorgente usa `"hostile spacecraft"` dentro il testo, e la resa fa
   lo stesso; il controllo confronta il numero per unità (2, entrambe nell'unità 60).
7. **Una collisione di nomi nel costruttore**: la costante `ENG` oscurava il dizionario `ENG` degli inglesi e faceva
   fallire l'asserzione sulle chiavi; rinominata `ENG_REP` (con `HULL_REP`, `POWER_REP`).
8. **Gate**: minimo 0,83 (unità 52, la corsa nei corridoi), massimo 1,80 (unità 3, «(Salvage the ship.)»).

## 4. Numeri osservati

```
unita' 76/76 · MISSION_TEXT 75 · DESCRIPTION 1 · VALUE 0 · UI_LABEL 0 · tutte PENDING
contesti 2 (1/75) · testi distinti 52 (24 ripetizioni)
tab 74 unita · virgolette 2 (unita 60) · token 22 in 2 famiglie · quadre 0
parole EN 1632 -> IT 1594 (0.977) · rapporto 0.83 - 1.80, media 1.07
righe 695/959 · 164 prima / 0 dopo · FILE CHIUSO 240/240
FAIL totale: 0 (28 controlli) · verify exit 0 (31 controlli)
sha256[:16] ec991eb6a0c3f258
```

## 5. Stato del progetto

```
TOTALE staging: 27227 unità · 860195 EN · 817482 IT
boarding missions.txt: 240/240 (100,0%) · 3 lotti · 4571 EN -> 4480 IT
file completi: quarantasette · residuo traducibile (formula state.py): 4703
residuo misurato: 5365 unità / 116892 parole su 119 file
avanzamento: 27227/32924 unità (82,7%) · 860195/979975 parole (87,8%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (28 controlli), `verify.py` exit **0** (31 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 76 unità `PENDING`, nessuna missione caricata nel gioco.
- **Nessuna revisione umana**.
- **`boarding missions.txt` è completo solo in staging**: 240 unità tradotte, zero caricate nel gioco.
- **Prossimo lotto**: `HANDOFF_L132_20261019.md` — file **nuovo**, `data/hai/unfettered side missions.txt`, righe
  **17–229** (**84 unità**, **2.055 parole**, **2 contesti**, **89 virgolette**, **74 unità con tab**).
