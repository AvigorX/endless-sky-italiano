# REPORT — L155 · `weapons.txt` (blaster e laser: le prime dieci armi (apre il file))

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| blaster | 1-7 | 36-251 | `Energy Blaster`, `Twin Blaster`, le due torrette, le due versioni modificate, `Heavy Blaster` |
| laser | 8-10 | 277-306 | `Beam Laser`, `Laser Turret` |

## 2. Scelte

| nodo | IT | unità |
|---|---|---|
| `gun port` | **alloggiamento per armi** | 2, 6 |
| `tinkerers` | **smanettoni** | 2 |
| `turret` / `gun` | **torretta** / **cannone** | 3, 4, 10 |
| `Deep` (regione) | **Deep**, invariato | 9 |
| `Firebird` · `Particle Cannon` · `Plasma Cannon` | **invariati** | 8 |
| `The Heavy Blaster is…` | **Il Heavy Blaster è…** | 8 |

## 3. Difficoltà

1. **Nessun template**: dieci prose diverse, una per `outfit`; il controllo che conta è il confronto **nome per nome** fra inglese e italiano, unità per unità.
2. **`mid-2400s`** reso «metà degli anni 2400» e non con un secolo approssimato: il testo parla di decenni, non di «XXV secolo».
3. **Articolo davanti a nomi inglesi con H iniziale**: convenzione del batch, «il Heavy Blaster» (non «l'Heavy»), coerente con L154.
4. **Errore in corsa**: il controllo del glossario cercava `cannone` in un testo che dice «cannoni»; portato sui temi (`cannon-`), non sulla parola intera.

## 4. Numeri osservati

```
unita' 10 · 10 DESCRIPTION · tutte PENDING
token 0 (asserzione vuota) · 0 tab · 0 virgolette
10 testi distinti · 10 contesti · tab 0 · virgolette 0
parole 574 -> 594 (1.035) · rapporto 0.97 - 1.23
righe 36/306
FAIL totale: 0 (20 controlli) · verify exit 0 (17 controlli) · sha256[:16] 9ff81a5de32f81b0
```

## 5. Stato del progetto (dopo L155)

```
TOTALE staging: 27853 unità · 876738 EN · 833103 IT
residuo traducibile (formula state.py): 4077
file completi: 51
endless-sky HEAD b4aa3bac3, 0 modifiche
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (20 controlli), `verify.py` exit **0** (17 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 10 unità `PENDING`.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Lotto del batch L154–L160**: contratto = piano del batch, nessun `HANDOFF_L155` separato.
