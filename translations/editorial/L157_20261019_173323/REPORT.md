# REPORT — L157 · `weapons.txt` (plasma, lanciafiamme e la famiglia Meteor)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| cannoni al plasma | 1-7 | 625-796 | `Particle Cannon`, `Proton Gun`, `Proton Turret`, `Plasma Cannon`, `Plasma Turret`, `Plasma Repeater` (2 unità) |
| lanciafiamme | 8 | 834 | `Flamethrower` |
| famiglia Meteor | 9-16 | 885-983 | munizione, `VALUE` della cassa, cassa, lanciatore (2 unità), pod (3 unità) |

## 2. Scelte

| nodo | IT | unità |
|---|---|---|
| `Syndicate` | **Sindacato** | 2, 3 |
| `Southern Rim` | **Bordo Meridionale** | 6 |
| `outfitter` | **emporio** | 6, 13, 16 |
| `reverse engineer` | **ricostruire a ritroso** | 2 |
| `repeater` | **repeater**, invariato | 6 |
| `trades off its larger bursts for a much faster rate of fire` | **sacrifica le raffiche più ampie in cambio di una cadenza di fuoco molto più rapida** | 7 |

## 3. Difficoltà

1. **Due coppie identiche** in inglese (12/14 e 13/16): la resa deve restare identica, e un controllo lo verifica.
2. **Un solo `VALUE`** (`Meteor Missile Boxes`) riprodotto alla lettera; **4 unità con tab**.
3. **`outfitter` → «emporio»**: verificato sui lotti precedenti (L113), non inventato qui.
4. **Errore in corsa**: il tema del glossario era `munzion-`; in italiano è «muni**z**ione», quindi `munizion-`.

## 4. Numeri osservati

```
unita' 16 · 15 DESCRIPTION · 1 VALUE · tutte PENDING
token 0 (asserzione vuota) · 4 tab · 0 virgolette
14 testi distinti · 11 contesti · tab 4 · virgolette 0
parole 592 -> 621 (1.049) · rapporto 0.98 - 1.27
righe 625/983
FAIL totale: 0 (24 controlli) · verify exit 0 (19 controlli) · sha256[:16] 44b8d641c08a7203
```

## 5. Stato del progetto (dopo L157)

```
TOTALE staging: 27880 unità · 877857 EN · 834272 IT
residuo traducibile (formula state.py): 4050
file completi: 51
endless-sky HEAD b4aa3bac3, 0 modifiche
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (24 controlli), `verify.py` exit **0** (19 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 16 unità `PENDING`.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Lotto del batch L154–L160**: contratto = piano del batch, nessun `HANDOFF_L157` separato.
