# REPORT — L167 · `paradise world jobs.txt` (primo lotto: nove lavori)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| nove lavori | 1-28 | 16-221 | `Care Package`, `Birthday Supplies`, `Art Delivery`, `Newlyweds`, `Theater Props`, `Fine Food`, `Transport partiers [1]` e `[2]`, `Food Donations` |

## 2. Scelte

| nodo | IT | unità |
|---|---|---|
| `care package` | **pacco di generi di conforto** | 2, 3 |
| `birthday bash` | **festa di compleanno** | 5 |
| `palatial complex` | **complesso da reggia** | 9 |
| `newlyweds` · `lovebirds` | **sposi** · **piccioncini** | 11, 12 |
| `theater troupe` | **compagnia teatrale** | 14 |
| `rear loading dock` | **banchina di carico posteriore** | 9, 15, 18 |
| `completely legal pharmaceuticals` | **farmaci del tutto legali** | 20, 21, 24 |
| `undernourished souls` | **anime denutrite** | 27 |

## 3. Difficoltà

1. **62 token su 9 simboli**: il lotto più tokenizzato della campagna. Il multiset da solo è **cieco** (due segnaposto
   scambiati danno lo stesso totale), quindi il controllo verifica l'**ordine per unità** su tutte e 28.
2. **`<destination>` ≠ `<planet>`**: nelle `DESCRIPTION` c'è `<destination>`, nei `VALUE` `<planet>`; l'assenza
   incrociata è verificata, non solo i totali.
3. **Le due missioni `Transport partiers`** hanno descrizioni quasi identiche che differiscono per la coda (farmaci /
   snack): un controllo pretende che siano **diverse** e che «farmaci» non compaia nella seconda.
4. **`"completely legal pharmaceuticals"`** conserva le **2 virgolette** nel `MISSION_TEXT` (idx 21).
5. **Errore in corsa (mio)**: nel contratto avevo scritto che il confine di riga 225 era un `MISSION_TEXT`; è un
   **`VALUE`**. Corretto misurandolo — seconda volta in due lotti, quindi la regola «il tipo si misura» resta in
   `HANDOFF_L168`.
6. **Gate**: 0,89–1,30, media 1,08.

## 4. Numeri osservati

```
unita' 28 · 9 VALUE · 9 DESCRIPTION · 9 DIALOG · 1 MISSION_TEXT · tutte PENDING
token 62 su 9 simboli · 0 tab · 2 virgolette (idx 21)
27 testi distinti · 9 contesti · righe 16/221
parole 566 -> 604 (1.067) · rapporto 0.89 - 1.30, media 1.08
FAIL totale: 0 (23 controlli) · verify exit 0 (21 controlli) · sha256[:16] 58330ce6689b1aed
```

## 5. Stato del progetto (dopo L167)

```
TOTALE staging: 28024 unità · 883097 EN · 839796 IT
paradise world jobs.txt: 28/131 (21,4%) · 1 lotto
residuo traducibile (formula state.py): 3906
endless-sky HEAD b4aa3bac3, 0 modifiche
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (23 controlli), `verify.py` exit **0** (21 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 28 unità `PENDING`.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Primo lotto del file**: contratto successivo in `HANDOFF_L168_20261019.md`.
