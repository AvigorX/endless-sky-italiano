# REPORT — L178 · `avgi ships.txt` (quinto lotto: quattro mezzi, due boilerplate)

## 1. Contenuto

Quattro schede di mezzi `Avgi` — una **capsula di servizio**, un **bombardiere silurante**, un **intercettore
d'attacco** e un **silo orbitale** — più le due righe di boilerplate che il gioco ripete sotto ogni caccia e ogni drone.

## 2. Scelte

| nodo | IT | unità |
|---|---|---|
| `utility pod` · `personal craft` | **capsula di servizio** · **mezzo personale** | 1 |
| `flitting about the orbitals` | **svolazzare intorno agli orbitali** | 1 |
| `low gravity bodies` | **corpi a bassa gravità** | 1 |
| `cornerstone of ... carrier doctrine` | **pietra angolare della dottrina delle portaerei** | 3 |
| `point defense weapons` | **armi di difesa puntuale** | 3 |
| `gun platforms` | **piattaforme d'arma** | 4 |
| `deployed in large swarms` | **schierati in grandi sciami** | 9 |
| `storing and launching nuclear-tipped missiles` | **immagazzinare e lanciare missili a testata nucleare** | 12 |

## 3. Difficoltà

1. **Due coppie di boilerplate**: rese identiche a due a due, e mai scambiate fra caccia e droni. Un controllo le isola.
2. **Nomi di mezzi e armi invariati**: `Akoustiki Excursion Vehicle`, `Photikon`, `Vibratia`, `Undulon`,
   `Speckle Turret`, `Ophrys`, `Avgi`.
3. **6 tab** (idx 2, 4, 5, 10, 13, 14): il massimo in questo file, uno per unità.
4. **6 virgolette**, tutte nei 3 `TEXT` (2 ciascuno).
5. **Nessun errore in corsa**: `check.py` e `verify.py` sono passati **al primo tentativo**. I due script sono stati
   scritti nello scratch e **copiati** nella cartella del lotto (trappola 46), poi verificati con `ls`.
6. **Gate**: 1,06–1,24, media 1,11.

## 4. Numeri osservati

```
unita' 14 · 10 DESCRIPTION · 3 TEXT · 1 VALUE · tutte PENDING
token 0 · 6 tab · 6 virgolette · 0 apici
12 testi distinti · 4 contesti (2/5/3/4) · righe 2424/2667
parole 418 -> 448 (1.072) · rapporto 1.06 - 1.24, media 1.11
FAIL totale: 0 (25 controlli) · verify exit 0 (23 controlli) · sha256[:16] 7cf03810fb0ffea8
```

## 5. Stato del progetto (dopo L178)

```
TOTALE staging: 28224 unità · 887764 EN · 844679 IT
avgi ships.txt: 97/102 (95,1%) · 5 lotti — restano 5 unità, si chiude in L179
residuo traducibile (formula state.py): 3706
residuo misurato: 4375 unità / 89340 parole su 112 file
endless-sky HEAD b4aa3bac3, 0 modifiche
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (25 controlli), `verify.py` exit **0** (23 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 14 unità `PENDING`.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Quinto lotto del file**: resta **L179**, che chiude `avgi ships.txt` (`HANDOFF_L179_20261019.md`).
