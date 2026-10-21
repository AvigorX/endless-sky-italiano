# REPORT — L156 · `weapons.txt` (laser pesanti, mining laser, raggi traenti e antimissili)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| laser pesanti | 1-2 | 341-370 | `Heavy Laser`, `Heavy Laser Turret` |
| estrazione | 3-6 | 407-441 | `Mining Laser` e `Mining Laser Turret` (2 unità ciascuno) |
| raggi traenti | 7 | 465 | `Tractor Beam` |
| Deep Sky | 8-9 | 496-525 | `Electron Beam`, `Electron Turret` |
| antimissili | 10-11 | 557-589 | `Anti-Missile Turret`, `Heavy Anti-Missile Turret` |

## 2. Scelte

| nodo | IT | unità |
|---|---|---|
| `mid-2400s` | **metà degli anni 2400** | 3 |
| `24th century` | **XXIV secolo** | 7 |
| `tractor beams` | **raggi traenti** | 7 |
| `Deep Sky labs` | **laboratori Deep Sky** | 8 |
| `electron beam weapons` | **armi a fascio di elettroni** | 9 |
| `its smaller sibling` | **la sua sorella minore** | 11 |
| `firing in clusters` | **sparano in grappolo** | 11 |

## 3. Difficoltà

1. **2 unità con tab iniziale** (idx 4 e 6): il tab è nel sorgente e va riprodotto, non aggiunto a mano.
2. **Due epoche diverse** nello stesso lotto: `mid-2400s` è un decennio, `24th century` un secolo; rese in modo diverso.
3. **`Lovelace Labs` e `Deep Sky`** restano inglesi, ma `Syndicate` e `Southern Rim` no (fazioni e regioni si traducono, come nei lotti precedenti).

## 4. Numeri osservati

```
unita' 11 · 11 DESCRIPTION · tutte PENDING
token 0 (asserzione vuota) · 2 tab · 0 virgolette
11 testi distinti · 9 contesti · tab 2 · virgolette 0
parole 527 -> 548 (1.040) · rapporto 1.02 - 1.17
righe 341/589
FAIL totale: 0 (22 controlli) · verify exit 0 (17 controlli) · sha256[:16] ecb449525eca318b
```

## 5. Stato del progetto (dopo L156)

```
TOTALE staging: 27864 unità · 877265 EN · 833651 IT
residuo traducibile (formula state.py): 4066
file completi: 51
endless-sky HEAD b4aa3bac3, 0 modifiche
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (22 controlli), `verify.py` exit **0** (17 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 11 unità `PENDING`.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Lotto del batch L154–L160**: contratto = piano del batch, nessun `HANDOFF_L156` separato.
