# STATO — L324 (`data/incipias/incipias outfits.txt`, righe 40–388)

**Stato: CHIUSO — LOTTO TERMINALE, FILE INTERO.** Il file è **completo: 23/23 (100%)**, **trentottesimo file interamente tradotto**
(**97** su 167). `check.py` esce 0 con **23 controlli**; `verify.py` esce 0 con **18 controlli**. `state.py` esce 0 (`ESITO: OK`, 8/8).
Nessuna scrittura su `state.db`.

| voce | valore |
|---|---|
| directory | `staging/editorial/L324_20261020_225422/` |
| file | `data/incipias/incipias outfits.txt` (**23/23 unità · 853 parole · righe 40–388**) |
| righe | 40–388 (**tutto il file**) |
| unità | **23 `DESCRIPTION`** |
| contesti | **20** — `Plasma Discharger` 2, `Stagnation Beam` 3, `Star Tail` 3, `Star Tail Storage` 2, e **tredici** singoli |
| parole | **853 EN → 831 IT** (0,974) |
| rapporto | **0,93 – 1,27** |
| tab | **6** — righe **41, 86, 87, 134, 135, 190** |
| virgolette | **0** |
| segnaposto / alternative | **0 / 0** |
| apici | **9 EN in 5 unità** (40 ×1, 85 ×2, 86 ×3, 225 ×2, 351 ×1) / 23 IT |
| `check.py` | **23 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **18 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di FILE**: 23 unità · **0 prima, 0 dopo** · prima **40** · ultima **388** |
| `sha256[:16]` | **`8bb5e39597a524ab`** |

**Nota di conteggio**: i contesti sono **20**, non 17. La distribuzione misurata è `3, 3, 2, 2` più **tredici** singoli — nel contratto
avevo scritto «17 contesti … dodici `1`», che è **falso**: 4 + 13 = 17 era una mia somma sbagliata, i contesti sono 20 e i singoli 13.
Il test ora conta **20**.

## Comandi

```bash
python staging/editorial/L324_20261020_225422/check.py     # FAIL totale: 0 (23 controlli)
python staging/editorial/L324_20261020_225422/verify.py    # FAIL: 0 (18 controlli, FILE 23/23)
```

## La quarta occorrenza della nota dei rifornimenti

La riga 135 è, per la **quarta volta** in quattro lotti:

```
\tAmmunition for this weapon can be restocked at any outfitter.
→ \tLe munizioni per quest'arma possono essere rifornite presso qualsiasi emporio.
```

Le occorrenze precedenti: **L318** (`korath weapons` 473), **L319** (`korath weapons` 659, 1051, 1222), **L320** (`wanderer outfits`
271). La resa usata è **quella di maggioranza** del corpus, e `verify.py` la cerca **nel corpus intero** (almeno **2 altri lotti** con la
stessa stringa italiana), non solo in questo file: è la regola per le note di famiglia che attraversano i file.

## La scala dei colori

| riga | colore | inglese | resa |
|---|---|---|---|
| 289 | `Blue` | `blue is the weakest color` | «il blu è il colore **più debole**» |
| 320 | `Green` | `a color of balance` | «il verde è … un colore di **equilibrio**» |
| 351 | `Red` | `this potent source of energy` | «questa fonte di energia **potente**» |

Il **rosso** non è detto «il più forte» nel testo: la sua scheda parla dell'**idrogeno metallico** e dei motori. La progressione si
deduce dal **dominio** (le tre classi `Blue`/`Green`/`Red` sono in ordine di potenza), **non** da una frase che lo dichiari — e il test
infatti verifica **ciò che c'è** (`weakest`, `balance`, `potent`), non ciò che avevo immaginato.

## Tre rossi, tutti miei, tutti da assunzioni

| # | asserzione | realtà |
|---|---|---|
| 1 | «17 contesti … dodici singoli» | **20 contesti**, **tredici** singoli |
| 2 | `at[320]['english'].count('balance') == 1` | **2**: «balance» **e** «balances» — il conteggio di sottostringa raddoppia |
| 3 | «le tre classi MH restano invariate nel testo» | solo **`Blue-Class`** compare in prosa (riga 334); `Green`/`Red` esistono **solo nei contesti** |

Il terzo è il più istruttivo: i nomi dei **contesti** (`outfit:MH Green-Class Thruster`) non sono testo e **non si traducono**, mentre
nel corpo della scheda compaiono solo dove l'autore li ha messi. Il controllo corretto è: **il nome compare dove compare nel
sorgente**, non «il nome compare».

## Cosa il test pretende

| oggetto | verifica |
|---|---|
| tipi | **23 `DESCRIPTION`** |
| contesti | **20**, distribuzione `3, 3, 2, 2` + **tredici** `1`; le sei classi `MH` nei contesti |
| tab | **6** righe esatte; `Stagnation Beam` **due** (86, 87) e `Star Tail` **due** (134, 135) |
| nota | riga 135 **identica al corpus**, e presente in **≥2 altri lotti** |
| scala | `weakest` / `balance` / `potent` con le rese «debole» / «equilibrio» / «potente» |
| nomi | `Plasma Discharger`, `Stagnation Beam`, `Star Tail`, `Horizon Grappler`, scudi, `Metallic Hydrogen Cell`, `Cloud Piercer`, `Hicemus` invariati |
| vuote | **0 virgolette**, **0 segnaposto**, **0 alternative** |
| FILE | **0 prima · 23 qui · 0 dopo** · prima 40 · ultima 388 · **23/23 asserita** |

## Limiti dichiarati

Nessuna approvazione (23 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. `Incipias` è **invariabile** in
italiano (popolo e aggettivo): «gli Incipias», «la cultura Incipias», «le navi Incipias» — scelta dichiarata, non correzione.
