# REPORT — L85 · `data/successors/predecessors.txt` (chiude il file)

## 1. Contenuto

Sette `DESCRIPTION`, una per equipaggiamento, senza alcun dato da lasciare identico — la prima volta in questo
file. È il lotto con la più alta densità di prosa: 250 parole in 7 unità.

## 2. Scelte

| nodo | scelta | perché |
|---|---|---|
| `coilgun` | **cannone a bobina** | forma usata in L82/L84 per la prosa |
| `a sizable fraction of the speed of light` | **una frazione considerevole della velocità della luce** | `sizable` è vago, e resta vago |
| `mastery of technology as an art rather than a science` | **padronanza della tecnologia un'arte più che una scienza** | l'opposizione arte/scienza è il tema del reattore |
| `stellar metal foam` | **schiuma di metallo stellare** | coerente con «metallo stellare» (L74) |
| `yearns to see combat once again` | **anela a vedere di nuovo il combattimento** | il generatore è personificato |
| `that pang-ridden emptiness` | **quel vuoto carico di dolore** | `pang` è fitta, non semplice tristezza |
| `a black spot in one's vision` | **una macchia nera nella vista** | non «nel campo visivo»: è più fisico |
| `Stolen Cloak (Deactivated)` | contesto invariato | nome di dato: parentesi comprese |

## 3. Difficoltà

1. **Nessun dato nel segmento**: la distinzione dato/prosa di L81–L84 qui non ha oggetto, e il `check.py` la
   dichiara come assenza (sette tipi a zero, uno positivo).
2. **Un brano di Resja fra virgolette** (unità 6): 4 virgolette in tutto il lotto, tutte sue; reso senza
   appiattire il ritmo lungo.
3. **`1-`/`OC-`/`3-`/`6-` nei nomi dei contesti**: prefissi di serie che restano nei nomi, non nel testo.
4. **Chiusura del file**: invariante di file con copertura dell'intero file letta da tutti i `translation.json`.

## 4. Numeri osservati

```
unita' 7/7 · tab 0 · virgolette 4 = 4 · dispari 0
token 0 · duplicati 0 · rapporto 1.07 - 1.15
parole EN 250 -> IT 258 · righe 648/782
CHIUDE il file: 0 dopo · 59 unita · max(line) 782 · copertura 59/59
FAIL totale: 0 (21 controlli) · verify exit 0 (29 controlli)
sha256[:16] 3fad23a16aeaa834
```

## 5. Stato del progetto

```
TOTALE staging: 24817 unita · 790070 EN · 748973 IT
predecessors.txt: 59/59 (100%) · 898 EN -> 927 IT · 5 lotti
file completi: trentacinque
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | parte, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` **e** `verify.py` exit **0**, **file 59/59** |
