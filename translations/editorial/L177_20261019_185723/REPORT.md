# REPORT — L177 · `avgi ships.txt` (quarto lotto: cinque navi, 29 nomi da copiare)

## 1. Contenuto

**39 unità in 467 parole** (≈12 a unità): il lotto più nominale della campagna. Cinque navi `Avgi` — la fregata
**Interferos**, la portaerei di scorta **Diaspersi**, il cacciatorpediniere laser **Refraktos** (con due note tecniche in
tab), l'incrociatore **Difraktos** e la portaerei di flotta **Atenuatia**. Il resto sono nomi di equipaggiamento.

## 2. Scelte

| nodo | IT | unità |
|---|---|---|
| `easy to build and disposable enough for mass production` | **facile da costruire e abbastanza sacrificabile per la produzione di massa** | 3 |
| `licensing its sale to independent merchant captains` | **concederne la vendita in licenza ai capitani mercantili indipendenti** | 3 |
| `attrition rates leave something to be desired` | **i tassi di perdita lasciano a desiderare** | 3 |
| `escort carrier` | **portaerei di scorta** | 10 |
| `two wings of combat drones ... a single wing of larger fighters` | **due stormi di droni ... un singolo stormo di caccia più grandi** | 10 |
| `directed energy weapons` | **armi a energia diretta** | 18 |
| `mirror-cell fusion torch` | **torcia a fusione a celle a specchio** | 19 |
| `anemic damage output` | **resa di danno anemica** | 20 |
| `kinetic weapon battlecruiser` | **incrociatore da battaglia con armi cinetiche** | 26 |
| `flight deck` → `battlefleets` | **flotte da battaglia** | 36 |

## 3. Difficoltà

1. **58 virgolette in 29 nomi**: la verifica è **per unità** (2 ciascuna) e impone zero virgolette fuori dai `TEXT`.
2. **Cinque nomi ripetuti** con conteggi diversi (11 / 6 / 5 / 5 / 2): il controllo li conta **per nome**, non in blocco.
3. **`Z-666 "Zap" Fusion Torch`** compare qui per la prima volta come `TEXT` (in L164 era un `VALUE` di equipaggiamento):
   stesso nome, tipo diverso — si copia in entrambi i casi.
4. **2 tab** (idx 19, 20) nelle due note del Refraktos.
5. **Errori in corsa (miei, due)**: (a) un controllo con **parentesi non chiusa** (`SyntaxError`), riscritto in forma più
   semplice con una costante `PAIRS`; (b) il **`verify.py` non è stato scritto su disco** per la seconda volta in due
   lotti — lo strumento rispondeva «ok». Risolto scrivendo nello scratch e **copiando** con `cp`, poi verificando con
   `ls`. Da ora: ogni `verify.py` si scrive così.
6. **Gate**: 1,06–1,30, media 1,16.

## 4. Numeri osservati

```
unita' 39 · 29 TEXT (nomi) · 7 DESCRIPTION · 3 VALUE · tutte PENDING
token 0 · 2 tab · 58 virgolette · 0 apici
15 testi distinti · 5 contesti (7/8/7/11/6) · righe 1415/2337
parole 467 -> 509 (1.090) · rapporto 1.06 - 1.30, media 1.16
FAIL totale: 0 (24 controlli) · verify exit 0 (23 controlli) · sha256[:16] e962a9325deb075f
```

## 5. Stato del progetto (dopo L177)

```
TOTALE staging: 28210 unità · 887346 EN · 844231 IT
avgi ships.txt: 83/102 (81,4%) · 4 lotti — restano 19 unità
residuo traducibile (formula state.py): 3720
residuo misurato: 4389 unità / 89758 parole su 112 file
endless-sky HEAD b4aa3bac3, 0 modifiche
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (24 controlli), `verify.py` exit **0** (23 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 39 unità `PENDING`.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Quarto lotto del file**: contratto successivo in `HANDOFF_L178_20261019.md`.
