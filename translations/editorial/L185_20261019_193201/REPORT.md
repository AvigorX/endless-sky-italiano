# REPORT — L185 · `gegno outfits.txt`

## 1. Contenuto

Primo lotto di un **universo nuovo** (i Gegno) e primo file aperto dopo la chiusura di `human outfits.txt`.

| blocco | unità | righe | contenuto |
|---|---|---|---|
| batterie Vi | 1-8 | 17-76 | `R01` → `R04`: dalla batteria comune alla `Crusade`, "immensa" |
| celle e reattori | 9-12 | 91-139 | `Scrap Cell`, `Brawl Cell` (girata di lato), `Warzone Core`, `Campaign Core` |
| cellula Scin | 13 | 157 | la `I70 Ameliorate Cell` dei caccia `Halite` |

## 2. Scelte

| nodo | IT | unità |
|---|---|---|
| very common outfits | **equipaggiamenti molto comuni** | 2 |
| a cheaper alternative than upgrading to a larger reactor | **un'alternativa più economica all'aggiornamento a un reattore più grande** | 2 |
| medium-range combat vessels | **navi da combattimento a medio raggio** | 4 |
| large, sturdy battery packs | **pacchi batteria grandi e robusti** | 6 |
| inefficient at increasing density with size | **inefficienti nell'aumentare la densità con la dimensione** | 8 |
| radiothermal generator | **generatore radiotermico** | 9 |
| fail-safes | **sicurezze** | 11 |
| generation ship era | **epoca delle loro astronavi generazionali** | 12 |

## 3. Difficoltà

1. **I quattro `VALUE` sono plurali** (`R01 Skirmish Batteries`) mentre i contesti sono singolari (`outfit:R01 Skirmish Battery`): il nome si copia com'è, il contesto non si tocca.
2. **I codici non si traducono**: `R01`, `C3`, `C7`, `C17`, `C27`, `I70`. Due di essi (`C17`, `C27`) vivono **solo nei contesti** e non compaiono nel testo inglese: il controllo verifica i codici **presenti nel testo**, non l'elenco intero.
3. **Un'asserzione sbagliata (mia)**: avevo scritto «quattro `Gegno's`»; il quinto apice è `Halite's`. Misurato: **tre** `Gegno's` + `It's` + `Halite's`.
4. Zero tab e zero virgolette: due asserzioni vuote scritte comunque.

## 4. Numeri osservati

```
unita' 13 · 9 DESCRIPTION · 4 VALUE · tutte PENDING
token 0 · 0 tab · 0 virgolette · 5 apici EN · 6 apici IT
13 testi distinti · 9 contesti · righe 17/157
parole 469 -> 483 · rapporto 1.0 - 1.19, media 1.07
FAIL totale: 0 (27 controlli) · verify exit 0 (20 controlli) · sha256[:16] c2fcd9f6a88e97cc
```

## 5. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (27 controlli), `verify.py` exit **0** (20 controlli) |

## 6. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 13 unità `PENDING`.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**, **nessuna revisione umana**.
