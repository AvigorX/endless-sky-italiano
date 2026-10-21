# REPORT — L111 · `_ui/tooltips.txt` (primo lotto: 52 approvate riprodotte, 52 tradotte)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| `APPROVED` (dal DB) | 1–52 | 16–172 | `parked`, accelerazione, raffreddamento attivo, 14 voci del `postbruciatore`, asteroidi, automaton, bunks, ustione, cattura, carico (7 voci), cloak (4 voci), raffreddamento |
| `PENDING` (tradotte qui) | 53–104 | 175–328 | corrosione (5), costo, flotta, scarica (5), disruzione (5), resistenza, droni, capacità energetica, spazio motori, energia (3), caccia, detrito, forza d'urto, carburante (7), porti per cannoni (2), dissipazione/generazione di calore, protezione dal calore, capacità termica, scafo (8) |

## 2. Scelte (solo per le 52 unità nuove)

| nodo | scelta | perché |
|---|---|---|
| `burn` | **ustione** | termine del **blocco approvato** (`danni da ustione`), non «bruciatura» |
| `corrosion` · `discharge` · `disruption` | **corrosione** · **scarica** · **disruzione** | coerenti con «scarica accumulata sugli scudi» già approvato |
| `scramble` · `ion` · `leakage` | **disturbo** · **ionizzazione** · **perdita** | idem, dal blocco del postbruciatore |
| `slowing` | **interferenza sui motori** | |
| `Protection provided against … damage` | **Protezione contro i danni da …** | calco della formula approvata (unità 23) |
| `Increases by the given factor how much …` | **Aumenta del fattore indicato la quantità di danni … che la nave sopporta** | idem |
| `resisted per second` | **resistiti al secondo** | participio concordato con «danni», come l'approvato |
| `drag` · `drag reduction` | **resistenza** · **Riduce la resistenza** | |
| `flagship` | **ammiraglia** | come l'unità 21 approvata, non «nave ammiraglia» |
| `fleet capacity` | **capacità della flotta** | |
| `outfit space` · `engine space` | **spazio per gli equipaggiamenti** · **spazio motori** | *spazio carico* è già approvato in 37 |
| `flotsam` | **detrito** | |
| `hit force` | **forza d'urto** | |
| `gun ports` | **porti per cannoni** | |
| `heat capacity` | **capacità termica** resa come «calore massimo» | il testo approvato parla di «surriscaldarsi» |
| `disabled` | **messa fuori uso** | il gioco non dice «distrutta» |
| `hyperdrive jump` | **salto con iperguida** | |

## 3. Difficoltà

1. **Il lotto attraversava due stati.** Le prime 52 unità erano **`APPROVED`** con testo italiano nel database; il
   contratto non lo diceva e il primo `check.py` è fallito su «unità del lotto in PENDING» — **il controllo aveva
   ragione e la premessa del contratto torto**. Il lotto è stato rifatto: `mkparts2.py` legge le 52 approvate in
   **sola lettura** e le riproduce alla lettera.
2. **Il registro del pannello è già fissato dal testo approvato**: «tu», non «voi». Le 52 unità nuove sono state
   riscritte per allinearvisi, e il `check.py` verifica l'assenza di forme di cortesia plurale.
3. **Terminologia contro il proprio istinto**: il blocco approvato usa **«ustione»**, non «bruciatura»; la prima
   stesura diceva «bruciatura» e sarebbe stata incoerente con la riga sopra nello stesso pannello.
4. **Il gate di lunghezza su testi brevi**: nessun outlier, ma il rapporto migliore/peggiore è 1,021 globale, con
   punte locali: i tooltip sono frasi singole e una resa più lunga del 60% sarebbe visibile.
5. **104 contesti, uno per unità**: il `verify.py` verifica che siano **104 distinti** e tutti `tip:…`.
6. **Zero token, zero tab, zero quadre, zero ripetizioni**: quattro assenze verificate come fatti positivi.
7. **`mkparts.py` non era sovrascrivibile** (write-guard): il lotto porta `mkparts.py` (prima stesura, che legge
   solo il proprio dizionario) e `mkparts2.py` (quella buona, che legge il DB). **Va usato `mkparts2.py`**, e il
   documento lo dice.

## 4. Numeri osservati

```
unita' 104/104 · TUTORIAL_TIP 104 · 52 APPROVED riprodotte + 52 PENDING tradotte
contesti 104, tutti distinti, tutti tip: · tab 0 · token 0 · quadre 0 · ripetizioni 0
virgolette 14 = 14 (tutte doppie)
parole EN 1810 -> IT 1848 (1.021)
righe 16/328 · file 667 unita · max(line) 1865 · 0 prima / 563 dopo
FAIL totale: 0 (31 controlli) · verify exit 0 (28 controlli)
sha256[:16] dee204e785c7d01b · copertura file 104/667 (15,6%)
```

## 5. Stato del progetto

```
TOTALE staging: 25731 unita · 823864 EN · 781264 IT
tooltips.txt: 104/667 (15,6%) · 1 lotto
file completi: quarantuno · residuo traducibile (formula state.py): 6199
residuo misurato: 6830 unità / 153118 parole su 125 file
avanzamento: 25731/32924 unità (78,2%) · 823864/979975 parole (84,1%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 4 parti, `translation.json`, `mkparts2.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (31 controlli), `verify.py` exit **0** (28 controlli), incluse le 52 approvate confrontate col DB |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione nuova**: 52 unità restano `PENDING`; le 52 `APPROVED` sono state **riprodotte**, non
  riapprovate, e nessun `UPDATE` è stato eseguito sul database.
- **Nessun caricamento nel gioco**: nessun tooltip è stato visto nel pannello.
- **Il file non è completo**: **563 unità** residue; prossimo contratto `HANDOFF_L112_20261018.md` (righe 331–688,
  **120 unità**, tutte `PENDING`).
- **Nessuna revisione umana**.
