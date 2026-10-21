# REPORT — L81 · `data/successors/predecessors.txt`

## 1. Cosa contiene il lotto

Due **schede di nave** della linea Successors, in un file che descrive le navi dei Predecessori:

**Resja, of the Nine Eyes** (1–14). Nome della nave (`Resjan, of the Nine Eyes`), l'elenco degli
equipaggiamenti — `"Iasa," Lethal Word`, `Hyperdrive`, `"Jiita" Heirloom Shielding`, `Heirloom Cooling`,
`"Ija" Heirloom Reactor`, `Heirloom Power Reserve`, `Auxiliary Power Reserve`, `Multimodal Armor: Regen` — e
la **poesia incisa** da Resja sugli scafi delle navi che portavano il loro nome: quattro occhi, tre, due, e
uno mancante.

**Hasur, Vowsworn** (15–22). Nome (`Hasuran, Vowsworn`) e l'elenco degli equipaggiamenti, quasi identico al
primo: `"Kis," Lethal Wish`, `Hyperdrive`, `"Jiita" Heirloom Shielding`, `Successor Cooling`,
`"Ija" Heirloom Reactor`, `Heirloom Power Reserve`, `Multimodal Armor: Regen`.

**Nessuna prosa narrativa** oltre alla poesia: il resto è dato di gioco.

## 2. Scelte editoriali

| nodo | scelta | perché |
|---|---|---|
| `Resjan, of the Nine Eyes` / `Hasuran, Vowsworn` | **identici** | nomi di nave |
| `Hyperdrive`, `Heirloom Cooling`, `Multimodal Armor: Regen`… | **identici** | nomi di equipaggiamento definiti altrove: tradurli qui creerebbe un riferimento rotto |
| la poesia (10–14) | **tradotta e rimata** | è prosa: quattro versi con rima in inglese |
| `Four eyes for Houses who're no longer there` | «Quattro occhi per le Casate che non hanno più dimora» | «occhi» sono quelli del nome (Nine Eyes) e del poema |
| `the cursed stars' shimmering flare` | «la fiamma tremula delle stelle che divora» | `shimmering` + `flare` fusi, per tenere la rima |
| `the bitter rings, blinking with light` | «gli anelli amari, che brillano ancora» | `bitter` è il sapore del rimpianto, non l'amarezza chimica |
| `And a final one missing, lost to the night` | «E uno mancante, perduto nella notte che lo ignora» | l'ultimo occhio mancante è il tema del nome della nave |

## 3. Difficoltà incontrate

1. **Capire che 17 unità su 22 non sono prosa.** Il tipo `TEXT` qui non è un'etichetta di salto ma il **nome
   di un oggetto**: la tentazione era tradurlo («Iperspazio», «Raffreddamento Ereditato»), che avrebbe
   prodotto una scheda in italiano con oggetti inesistenti.
2. **Rima.** L'inglese rima `there / flare / light / night`; l'italiano rima `dimora / divora / ancora /
   ignora`. Il `verify.py` non misura la poesia, ma verifica che le quattro desinenze coincidano: è il minimo
   controllabile.
3. **Zero tab**: il file non indenta, e le parti non devono aggiungerne. Il controllo è esplicito.
4. **Cinque gruppi di duplicati**: gli stessi nomi compaiono su due navi. Resa identica, dichiarata.

## 4. Numeri osservati (output letto)

```
unita' 22/22 · copertura 22/22
virgolette IT 12 / EN 12 · dispari 0 · tab 0
token IT 0 / EN 0
rapporto IT/EN 1.00 - 1.21
parole EN 106 -> IT 106
prima/ultima riga: 17/196
duplicati inglese: 5 gruppi
FAIL totale: 0    (30 controlli)
verify.py exit 0  (34 controlli)
sha256[:16] 26f957d5edbd1958
```

## 5. Stato del progetto dopo il lotto

```
TOTALE staging: 24780 unita · 789278 EN · 748152 IT
predecessors.txt: 22/59 (37,3%) · 106 EN -> 106 IT · 1 lotto
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 1 parte, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (30 controlli) **e** `verify.py` exit **0** (34 controlli) |

## 7. Due difetti miei, corretti prima di chiudere

- **Il controllo della rima era sbagliato**: confrontava le **parole intere** (`dimora`, `divora`…) invece
  delle **desinenze**, e diventava rosso con la poesia giusta.
- **Il controllo dei token aveva condizione e dettaglio invertiti** (`ck(nome, tok, tok == 0)`): stampava
  `FAIL True` su un conteggio corretto di zero. Corretto in `ck(nome, tok == 0, tok)`.
