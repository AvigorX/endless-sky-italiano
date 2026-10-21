# REPORT — L166 · `avgi outfits.txt` (ultimo lotto: chiude il file)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| fucile laser | 1-2 | 616-617 | spettro dal vicino infrarosso al verde-blu, cecità da riflessione, cannocchiale senza parallasse |
| tavola di Trefoil | 3-4 | 631-632 | legno `Integral Wood`, intarsi d'argento, pietre di lapislazzuli, giada e granato |
| tumore radioattivo | 5 | 641 | il `Damselflyman`, la fuga dei nemici, l'avvertenza sull'«equipaggiamento» |
| lancia cerimoniale | 6 | 654 | `Lancet Adamant` in adamantino |

## 2. Scelte

| nodo | IT | unità |
|---|---|---|
| `small arm` | **arma leggera** | 1 |
| `near-infrared to blue-green` | **dal vicino infrarosso al verde-blu** | 1 |
| `eye-safe` | **sicuro per gli occhi** | 1 |
| `boarding parties` | **squadre di abbordaggio** | 1 |
| `Integral Wood` · `Speaker Wisteria` | **invariati** (nomi propri) | 3 |
| `well-worn from countless games` | **consumate da innumerevoli partite** | 3 |
| `disabled starship` | **astronave in avaria** | 5 |
| `adamantine, or nanodiamond` | **adamantino, o nanodiamante** | 6 |

## 3. Difficoltà

1. **Registro misto**: un fucile descritto in modo tecnico, una tavola da gioco affettiva, due oggetti volutamente
   assurdi (`Damselflyman`, `Lancet Adamant`). La resa deve seguire il registro di ciascuno, non uniformarlo.
2. **`'outfit.'` fra apici semplici**: è ASCII, e il controllo verifica che non diventi un apostrofo curvo.
3. **2 unità con tab** (2 e 4) e **zero `VALUE`**.
4. **Invariante di FILE**: il `verify.py` non controlla un segmento ma la somma delle sei finestre (63/63), le righe
   distinte, `min/max` e l'assenza di unità dopo la 654.
5. **Gate**: 1,02–1,40, media 1,18.

## 4. Numeri osservati

```
unita' 6 · 6 DESCRIPTION · 0 VALUE · tutte PENDING
token 0 (asserzione vuota) · 2 tab · 0 virgolette
6 testi distinti · 4 contesti · righe 616/654
parole 314 -> 343 (1.092) · rapporto 1.02 - 1.40, media 1.18
FAIL totale: 0 (21 controlli) · verify exit 0 (21 controlli) · sha256[:16] 5fbd18fba31ba060
FILE CHIUSO: 63/63 unita · 6 finestre · min(line) 18 · max(line) 654
```

## 5. Stato del progetto (dopo L166)

```
TOTALE staging: 27996 unità · 882531 EN · 839192 IT
avgi outfits.txt: 63/63 (100%) · 6 lotti — CHIUSO
residuo traducibile (formula state.py): 3934
endless-sky HEAD b4aa3bac3, 0 modifiche
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (21 controlli), `verify.py` exit **0** (21 controlli, invariante di file) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 6 unità `PENDING`.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Ultimo lotto del file**: il contratto successivo apre `paradise world jobs.txt` (`HANDOFF_L167_20261019.md`).
