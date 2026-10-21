# REPORT — L175 · `avgi ships.txt` (secondo lotto: Phononos, Frequentia, Polari, Entasi)

## 1. Contenuto

Quattro navi molto diverse: il **Phononos** è un retrofit di un bombardiere dismesso, talmente fragile da viaggiare solo
in convoglio; la **Frequentia** è una rifornitrice di carburante la cui porta di stiva è «notoriamente piccola»; la
**Polari** è un ricognitore scientifico con laboratorio e droni; l'**Entasi** è una nave mineraria con due enormi
generatori solari termici.

## 2. Scelte

| nodo | IT | unità |
|---|---|---|
| `retrofit of a decommissioned Photikon` | **retrofit di un Photikon dismesso** | 2 |
| `torpedo bomber` · `hardpoints and pylons` | **bombardiere silurante** · **punti di attacco e piloni** | 2 |
| `crammed into the ship` | **stipato a fatica nella nave** | 2 |
| `Dissonance piracy` · `Aberrant incursions` | **pirateria dei Dissonance** · **incursioni degli Aberrant** | 2 |
| `crewed vessels` | **navi con equipaggio** | 2 |
| `fuel tender` | **nave rifornitrice di carburante** | 5 |
| `cryogenic deuterium` · `dry goods` | **deuterio criogenico** · **merci secche** | 5 |
| `legacy design` | **progetto d'epoca** | 7 |
| `sensor arrays` · `sample gathering` | **dotazione di sensori** · **raccolta campioni** | 7 |
| `solar thermal generators` | **generatori solari termici** | 9 |
| `an asteroid field` | **un campo di asteroidi** | 9 |

## 3. Difficoltà

1. **Due `TEXT` che sono un nome**: `Z-333 "Spark" Fusion Torch` **non si traduce**. È la prima volta che `TEXT` non è
   prosa: la regola è ora scritta nel contratto (`HANDOFF_L176`) e verificata da due controlli.
2. **Quattordici nomi propri** da lasciare intatti (navi, droni, veicoli, fazioni). Un controllo li cerca uno per uno in
   ogni unità che li nomina, invece di fidarsi di un conteggio.
3. **3 tab iniziali** (idx 3, 8, 10), uno solo per unità.
4. **3 apici inglesi in una sola unità** (`fleet's`, `bay's`, `can't`): in italiano diventano «una piccola flotta»,
   «della stiva», «non si possa». Il controllo vieta che un `'s` sopravviva in italiano.
5. **Errore in corsa (mio)**: l'etichetta di un controllo conteneva `«'s»` dentro una stringa a virgola singola →
   `SyntaxError` immediato, nessuna esecuzione. Riscritta l'etichetta.
6. **Gate**: 1,06–1,23, media 1,13 (solo `DESCRIPTION`: i nomi hanno rapporto 1 per definizione).

## 4. Numeri osservati

```
unita' 10 · 7 DESCRIPTION · 2 TEXT (nome) · 1 VALUE · tutte PENDING
token 0 · 3 tab · 4 virgolette (nei TEXT) · 3 apici inglesi (idx 5)
9 testi distinti · 4 contesti (2/2/3/3) · righe 526/885
parole 490 -> 504 (1.029) · rapporto 1.06 - 1.23, media 1.13
FAIL totale: 0 (24 controlli) · verify exit 0 (22 controlli) · sha256[:16] 0bb78b20aa2af987
```

## 5. Stato del progetto (dopo L175)

```
TOTALE staging: 28151 unità · 886416 EN · 843229 IT
avgi ships.txt: 24/102 (23,5%) · 2 lotti
residuo traducibile (formula state.py): 3779
endless-sky HEAD b4aa3bac3, 0 modifiche
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (24 controlli), `verify.py` exit **0** (22 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 10 unità `PENDING`.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Secondo lotto del file**: contratto successivo in `HANDOFF_L176_20261019.md`.
