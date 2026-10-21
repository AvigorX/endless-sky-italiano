# REPORT — L174 · `avgi ships.txt` (primo lotto: quattro astronavi)

## 1. Contenuto

Quattro schede di astronavi `Avgi`, ognuna con la descrizione principale (senza tab) e due note tecniche (con tab
iniziale): `Koryfi` (trasporto passeggeri pre-iperguida), `Melodikos` (grande trasporto passeggeri), `Avlaki`
(mercantile medio), `Harmonikos` (grande mercantile). È il primo lotto di **prosa lunga** dopo sei lotti di formule:
≈34 parole per unità contro le ≈20 di `paradise world jobs.txt`.

## 2. Scelte

| nodo | IT | unità |
|---|---|---|
| `predates the invention of the hyperdrive` | **precede l'invenzione dell'iperguida** | 1 |
| `spin gravity system` | **sistema di gravità per rotazione** | 1 |
| `gravity plating` | **piastre gravitazionali** | 1 |
| `high maintainability` | **facile manutenibilità** | 1, 8 |
| `modular centrifuge` | **centrifuga modulare** | 2 |
| `magnetoplasmadynamic thrusters` | **propulsori magnetoplasmadinamici** | 3, 7, 10, 14 |
| `generously described as sluggish` | **generosamente descritta come fiacca** | 3, 7, 10, 14 |
| `constant thrust flight profile` | **profilo di volo a spinta continua** | 3, 7, 10, 14 |
| `solar array` | **distesa solare** | 5, 6, 12, 13 |
| `interplanetary cycler` | **ciclatore interplanetario** | 5 |
| `cargo modules towed behind the main truss` | **moduli cargo trainati dietro la trave principale** | 12 |

## 3. Difficoltà

1. **La formula dei propulsori, quattro volte**: stesso testo, nave diversa. La resa deve essere **una sola** a meno del
   nome, e il controllo lo dimostra per sostituzione.
2. **La coppia speculare 2/9**: «centrifuga → container» contro «container → centrifuga». Invertirle è l'errore
   naturale, quindi ognuna è verificata per il proprio verso.
3. **Il rimando incrociato 6/13**: Melodikos→Harmonikos e Harmonikos→Melodikos. Un controllo verifica che non siano
   scambiati.
4. **8 tab iniziali** da conservare esattamente (un solo tab, nessuno raddoppiato).
5. **4 possessivi inglesi** (`Koryfi's`, `Melodikos'`, `Avlaki's`, `Harmonikos'`) che in italiano diventano «di + nome»:
   verificata la **causa**, non l'uguaglianza degli apici.
6. **Errore in corsa (mio)**: la regex che neutralizza i nomi scriveva `'|'.join(SHIPS) + "'?s?"`, e per la precedenza
   di `|` il suffisso possessivo si applicava **solo all'ultimo** nome → 4 stringhe invece di 1. Corretto con un gruppo
   non catturante `(?:…)`.
7. **Gate**: 0,94–1,21, media 1,08.

## 4. Numeri osservati

```
unita' 14 · 12 DESCRIPTION · 2 VALUE · tutte PENDING
token 0 · 8 tab · 0 virgolette · 4 apici inglesi
14 testi distinti · 4 contesti (3/4/3/4) · righe 120/522
parole 477 -> 489 (1.025) · rapporto 0.94 - 1.21, media 1.08
FAIL totale: 0 (26 controlli) · verify exit 0 (21 controlli) · sha256[:16] c734fd303220cc1b
```

## 5. Stato del progetto (dopo L174)

```
TOTALE staging: 28141 unità · 885926 EN · 842725 IT
avgi ships.txt: 14/102 (13,7%) · 1 lotto
residuo traducibile (formula state.py): 3789
endless-sky HEAD b4aa3bac3, 0 modifiche
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (26 controlli), `verify.py` exit **0** (21 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 14 unità `PENDING`.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Primo lotto del file**: contratto successivo in `HANDOFF_L175_20261019.md`.
