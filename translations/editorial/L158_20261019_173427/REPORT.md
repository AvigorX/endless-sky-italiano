# REPORT — L158 · `weapons.txt` (Sidewinder e Javelin: munizioni, pod e lanciatori)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| Sidewinder | 1-9 | 1015-1116 | munizione, rack, lanciatore (3 unità), pod (4 unità) |
| Javelin | 10-18 | 1149-1228 | munizione, cassa, pod (3 unità), mini pod (4 unità) |

## 2. Scelte

| nodo | IT | unità |
|---|---|---|
| `protective casings` | **involucri protettivi** | 4, 7 |
| `saturating … anti-missile defenses` | **saturare le difese antimissile** | 13, 16 |
| `sneak through` | **riescano a passare** | 13, 16 |
| `Storage Rack` / `Storage Crate` / `Storage Tube` | **invariati** (nomi di oggetto) | 2, 11, 13 |
| `Ammunition for this weapon can be restocked at any outfitter.` | **Le munizioni per quest'arma possono essere rifornite presso qualsiasi emporio.** | 5, 9, 14, 18 |

## 3. Difficoltà

1. **10 unità con tab** su 18, il lotto più «tabbato» del file.
2. **Quattro testi ripetuti** (3/6, 4/7, 5/9/14/18, 12/15, 13/16): un controllo pretende l'identità della resa, non solo la correttezza dei singoli.
3. **Riuso verificato contro L157**: due stringhe (la riga munizioni e quella sui pod) sono le stesse del lotto precedente, e il controllo le confronta con la resa **già scritta**, non con una nuova.

## 4. Numeri osservati

```
unita' 18 · 18 DESCRIPTION · tutte PENDING
token 0 (asserzione vuota) · 10 tab · 0 virgolette
11 testi distinti · 8 contesti · tab 10 · virgolette 0
parole 564 -> 578 (1.025) · rapporto 0.98 - 1.27
righe 1015/1228
FAIL totale: 0 (23 controlli) · verify exit 0 (18 controlli) · sha256[:16] 7abe6d61b8ca79fa
```

## 5. Stato del progetto (dopo L158)

```
TOTALE staging: 27898 unità · 878421 EN · 834850 IT
residuo traducibile (formula state.py): 4032
file completi: 51
endless-sky HEAD b4aa3bac3, 0 modifiche
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (23 controlli), `verify.py` exit **0** (18 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 18 unità `PENDING`.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Lotto del batch L154–L160**: contratto = piano del batch, nessun `HANDOFF_L158` separato.
