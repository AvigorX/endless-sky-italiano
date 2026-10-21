# REPORT — L186 · `gegno outfits.txt`

## 1. Contenuto

Il lotto con il **rapporto più alto** della serie recente (1,12 di media): i nomi tecnici inglesi occupano spazio che l'italiano non recupera.

| blocco | unità | righe | contenuto |
|---|---|---|---|
| propulsori e timoni Vi | 1-6 | 179-285 | `RG15`, `RG18`, `RG3` — ionici, pesanti, i più antichi |
| motori Scin | 7-12 | 289-398 | `SC-1`, `SC-12`, `SC-14` — plasma, compatti, più potenti |
| la retromarcia | 13-14 | 402-427 | l'`SC-15` integra spinta inversa e diretta |

## 2. Scelte

| nodo | IT | unità |
|---|---|---|
| smallest torch thruster | **più piccolo propulsore a torcia ionica** | 1 |
| explosive exhaust causes them to run hotter | **lo scarico esplosivo li fa scaldare di più** | 3 |
| cheaply supplement their main steering engines | **integrare a buon mercato i loro motori di governo principali** | 2 |
| the Vi's bigger, more sluggish ion engines | **i motori ionici più grandi e più lenti dei Vi** | 8 |
| outmaneuver their opposing brothers | **manovrare meglio dei loro fratelli avversari** | 10 |
| reverse and forward thrust into a single engine | **spinta inversa e diretta in un unico motore** | 14 |

## 3. Difficoltà

1. **Due stirpi, due tecnologie**: il lotto alterna Vi (ionico) e Scin (plasma) e il confronto è **incrociato** — idx 3 dice che la torcia ionica scalda di più ma consuma meno, idx 9 rovescia il confronto per gli SC. Verificati separatamente.
2. **`Vi's` compare tre volte**, non due: il controllo è stato scritto con il numero sbagliato ed è stato bocciato al primo giro.
3. **Zero tab e zero virgolette** (asserzioni vuote); **5 apici** inglesi tutti possessivi, **6** italiani.

## 4. Numeri osservati

```
unita' 14 · 12 DESCRIPTION · 2 VALUE · tutte PENDING
token 0 · 0 tab · 0 virgolette · 5 apici EN · 6 apici IT
14 testi distinti · 12 contesti · righe 179/427
parole 462 -> 512 · rapporto 1.0 - 1.25, media 1.12
FAIL totale: 0 (24 controlli) · verify exit 0 (21 controlli) · sha256[:16] 6a678083062012e4
```

## 5. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (24 controlli), `verify.py` exit **0** (21 controlli) |

## 6. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 14 unità `PENDING`.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**, **nessuna revisione umana**.
