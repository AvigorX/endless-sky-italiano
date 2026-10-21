# REPORT — L180 · `human outfits.txt` (primo lotto: raffreddamento e scudi)

## 1. Contenuto

Undici schede di equipaggiamento umano, quasi tutte indipendenti (11 contesti per 12 unità): cinque impianti di
raffreddamento in scala (dalle `Cooling Ducts` all'elio liquido), cinque generatori di scudi in scala (`D14-RN` →
`D94-YV`) e due rigeneratori di scudi (`S-270`, `S-970`).

## 2. Scelte

| nodo | IT | unità |
|---|---|---|
| `sporadically overheating and shutting down` | **si surriscalda a intermittenza e si spegne** | 2 |
| `external radiator` | **radiatore esterno** | 3 |
| `dissipate the heat` | **dissipa il calore** | 4 |
| `the ultimate in cooling technology` | **il massimo della tecnologia di raffreddamento** | 5 |
| `shield matrix` | **matrice dello scudo** | 6, 11 |
| `hospitable spaceport` | **spazioporto ospitale** | 6 |
| `recharge rate` | **velocità di ricarica** | 7 |
| `depleting your shields` | **esaurire i tuoi scudi** | 9 |
| `in human space` | **nello spazio umano** | 10 |
| `shield regenerator` | **rigeneratore di scudi** | 11, 12 |
| `feedback ... heat to build up` | **un certo ritorno che fa accumulare calore** | 12 |

## 3. Difficoltà

1. **Registro nuovo**: non prosa narrativa né dottrina militare, ma **scheda tecnica da emporio**. Il lessico va tenuto
   allineato ai lotti di equipaggiamento già fatti (`avgi outfits.txt`, `weapons.txt`): `generatore di scudi`, `matrice
   dello scudo`, `spazio umano`.
2. **Due scale in parallelo** (potenza degli scudi, costo dei rigeneratori): verificate per **contenuto**, non per numero
   d'ordine — i due rigeneratori dicono cose **diverse** e il controllo lo pretende.
3. **Nomi di equipaggiamento invariati** (`Cooling Ducts`, `D14-RN`…`D94-YV`, `S-270`, `S-970`), anche quando compaiono
   dentro la prosa («i comuni Cooling Ducts»).
4. **Zero tab, zero virgolette, zero token**: quattro asserzioni vuote scritte comunque.
5. **Nessun errore in corsa**: `check.py` e `verify.py` sono passati **al primo tentativo**, scritti nello scratch e
   copiati con `cp` (trappola 46).
6. **Gate**: 1,01–1,27, media 1,10.

## 4. Numeri osservati

```
unita' 12 · 11 DESCRIPTION · 1 VALUE · tutte PENDING
token 0 · 0 tab · 0 virgolette · 1 apice inglese (idx 3)
12 testi distinti · 11 contesti (1x2 + 10x1) · righe 15/146
parole 467 -> 478 (1.024) · rapporto 1.01 - 1.27, media 1.10
FAIL totale: 0 (24 controlli) · verify exit 0 (20 controlli) · sha256[:16] 263300dbfc862221
```

## 5. Stato del progetto (dopo L180)

```
TOTALE staging: 28241 unità · 888444 EN · 845383 IT
human outfits.txt: 12/63 (19,0%) · 1 lotto
residuo traducibile (formula state.py): 3689
residuo misurato: 4358 unità / 88660 parole su 111 file
endless-sky HEAD b4aa3bac3, 0 modifiche
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (24 controlli), `verify.py` exit **0** (20 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 12 unità `PENDING`.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Primo lotto del file**: contratto successivo in `HANDOFF_L181_20261019.md`.
