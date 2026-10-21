# REPORT — L160 · `weapons.txt` (Heavy Rocket Pod, il Nuclear Missile e la Gatling (chiude il file))

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| razzi pesanti | 1-3 | 1640-1642 | pod: descrizione, nota sui pod, munizioni |
| missile nucleare | 4-5 | 1715-1716 | la descrizione e la nota fra parentesi quadre |
| Gatling | 6-13 | 1751-1844 | `VALUE` delle munizioni, cartuccia, `VALUE` delle scatole, scatole, `Gatling Gun`, `Gatling Turret` |

## 2. Scelte

| nodo | IT | unità |
|---|---|---|
| `Gatling Gun Ammo` · `Bullet Boxes` | **identici** (2 `VALUE`) | 6, 8 |
| `one-shot weapon` | **arma a colpo singolo** | 5 |
| `depleted nuclear fuel` | **combustibile nucleare esaurito** | 7 |
| `muzzle velocity` | **velocità alla bocca** | 7 |
| `19th century` | **XIX secolo** | 10 |
| `spin in his grave` | **rotolare nella tomba** | 12 |
| `tear apart the hulls` | **squarciare gli scafi** | 12 |

## 3. Difficoltà

1. **L'ellissi `...` di idx 4 resta tre punti ASCII** (mai `…`) e il **trattino ` - `** di idx 10 resta un trattino semplice (mai em/en dash): due controlli distinti, perché la tipografia li tratta diversamente.
2. **La nota fra parentesi quadre** di idx 5 conserva le quadre: è un testo tecnico per il giocatore, non una frase di narrazione.
3. **Il lotto chiude il file**: l'invariante è di **file**, 6 finestre = 90 righe distinte, `min(line) = 36`, `max(line) = 1844`, zero unità dopo.
4. **Riuso verificato**: idx 1 è la stessa stringa di L159 (idx 21) e la riga munizioni è quella di L157/L158/L159; entrambi i controlli leggono la resa **già scritta**.

## 4. Numeri osservati

```
unita' 13 · 11 DESCRIPTION · 2 VALUE · tutte PENDING
token 0 (asserzione vuota) · 5 tab · 0 virgolette
11 testi distinti · 6 contesti · tab 5 · virgolette 0
parole 408 -> 421 (1.032) · rapporto 1.00 - 1.27
righe 1640/1844
FAIL totale: 0 (27 controlli) · verify exit 0 (23 controlli) · sha256[:16] b2663bd3f42fddc7
```

## 5. Stato del progetto (dopo L160)

```
TOTALE staging: 27933 unità · 879405 EN · 835864 IT
residuo traducibile (formula state.py): 3997
file completi: 52
endless-sky HEAD b4aa3bac3, 0 modifiche
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (27 controlli), `verify.py` exit **0** (23 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 13 unità `PENDING`.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Lotto del batch L154–L160**: contratto = piano del batch, nessun `HANDOFF_L160` separato.
