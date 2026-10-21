# REPORT — L124 · `ships.txt` (dal Gunboat alla Raven)

## 1. Contenuto

| blocco | unità | righe | navi |
|---|---|---|---|
| Marina | 1, 11–12, 20–21, 28 | 2102–3364 | Gunboat, Lance, Monitor, Rainmaker |
| navi da carico | 2–4, 22–23 | 2162–3071 | Hauler, Hauler II, Hauler III, Mule, Nest |
| droni | 16–17 | 2816–2817 | Mining Drone |
| pirati e contrabbandieri | 10, 14, 18–19, 24 | 2541–3131 | Jackal, Mammoth, Modified Argosy, Nighthawk |
| civili | 5–9, 13, 15, 25–27, 29 | 2335–3422 | Hawk, Headhunter, Heavy Shuttle, Hogshead, Leviathan, Manta, Osprey, Protector, Quicksilver, Raven |

## 2. Scelte

| nodo | IT | nota |
|---|---|---|
| `mobile sensor platform` | **piattaforma sensoristica mobile** | |
| `bounty hunting` | **caccia ai ricercati** | |
| `composite fiber` | **fibra composita** | |
| `bunk` · `crew's quarters` | **cuccetta** · **alloggi dell'equipaggio** | |
| `freelancer pilots` | **piloti "freelance"** | fra virgolette come il sorgente |
| `one-hit-wonder` | **unico successo** | reso, non calcato |
| `space bus` | **"spazio-bus"** | fra virgolette come il sorgente |
| `peace among the stars` | **"pace tra le stelle"** | motto della Repubblica |
| `fighter docking arms` | **bracci di attracco per caccia** | |
| `missile boat` | **lanciamissili** | |
| `durability to cost ratio` | **rapporto durabilità-costo** | |
| `reverse thrusters` | **propulsori inversi** | coerente con `reverse thrust` (L112) |
| `Particle Cannons` · `Mining Laser` | invariati | nomi di equipaggiamento |
| `Stars and Starships Magazine` | **la rivista Stars and Starships** | testata, nome invariato |

## 3. Difficoltà

1. **Un solo `VALUE`**: il controllo lo elenca esattamente (`[18]`) e verifica che il testo sia `Modified Argosies`,
   non «tutti i `VALUE` tranne…».
2. **Due note tecniche riprese da L123**: resa riletta dal suo `translation.json` e confrontata; il `check.py`
   verifica le unità 12 e 17 una per una.
3. **Tre unità con tab**: poche, e proprio per questo facili da dimenticare; il controllo le elenca (`[9, 12, 17]`).
4. **29 testi distinti su 29 unità**: nessuna memoria interna al lotto, nessun gruppo da confrontare — la
   ripetizione, qui, non esiste.
5. **Le virgolette sono citazioni** ("freelance", "spazio-bus", "brutte", "pace tra le stelle", "Hauler I: Type F",
   "Nest", "la nave più brutta del cielo"): 14 in sei unità, contate per unità.
6. **Nomi di nave neutralizzati prima** della scansione dei residui inglesi: trentatré nomi, altrimenti rossa su
   una traduzione corretta.

## 4. Numeri osservati

```
unita' 29/29 · DESCRIPTION 28 · VALUE 1 (Modified Argosies) · tutte PENDING
contesti 24 (19x1, 5x2) · testi distinti 29 (nessuna ripetizione)
tab 3 unita (9, 12, 17) · virgolette 14 (unita 8, 9, 10, 20, 23, 26) · token 0 · quadre 0
parole EN 1539 -> IT 1603 (1.042) · rapporto 0.88 - 1.29, media 1.07
righe 2102/3422 · file 83/103 (80,6%) · 54 prima / 20 dopo · confine riga 3491
FAIL totale: 0 (28 controlli) · verify exit 0 (27 controlli)
sha256[:16] 5b6c5456b299d979
```

## 5. Stato del progetto

```
TOTALE staging: 26806 unita · 849782 EN · 807520 IT
ships.txt: 83/103 (80.6%) · 2 lotti · 3903 EN -> 4086 IT
file completi: quarantaquattro · residuo traducibile (formula state.py): 5124
residuo misurato: 5756 unità / 127202 parole su 122 file
avanzamento: 26806/32924 unità (81,4%) · 849782/979975 parole (86,7%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 2 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (28 controlli), `verify.py` exit **0** (27 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: le 29 unità restano `PENDING`; nessuna nave è stata caricata nel gioco.
- **Nessuna revisione umana**.
- **Il file non è completo**: **20 unità** residue (righe 3491–4266), un solo lotto: **L125 lo chiude**
  (`HANDOFF_L125_20261019.md`: 20 unità, 1.180 parole, 15 contesti, **zero token**, **zero `VALUE`**).
