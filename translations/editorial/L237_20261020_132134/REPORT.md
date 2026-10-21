# REPORT — L237 (`data/avgi/avgi news.txt`, righe 369–399)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **36 controlli** (`FAIL totale: 0`); `verify.py` esce 0 con **21
controlli** (invariante di segmento: 80 prima, 14 qui, 21 dopo). `state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura
su `state.db`: le 14 unità restano `PENDING`.

## 1. Cosa contiene il lotto

| contesto | righe | unità | contenuto |
|---|---|---|---|
| `news:avgi physicist` | 369–376 | 8 | il sapere conservato nei recessi dello spazio; gli scudi energetici che «non hanno senso»; l'iperpropulsore che nessuno capisce davvero; la tesi sulle celle solari; lo studente che ottant'anni fa aveva ragione; i wormhole come opzione più probabile; il rivestimento che riduce la resistenza aerodinamica; il diamante di memoria che sopravvive alla civiltà |
| `news:avgi astronomer` | 394–399 | 6 | la Twilight Nebula come nebulosa a riflessione di quasi mille anni luce; l'ammasso a sud-est di Stream; la nebulosa che non è in equilibrio idrostatico; la galassia tridimensionale e le mappe; i punti cardinali contro le coordinate polari; le vie stellari che collegano solo alcuni sistemi |

## 2. Misure

```
unità             14            (tutte NEWS)
parole            356 EN -> 354 IT
rapporto          0,94 - 1,21 (media 1,08)   gate 0,55-1,90
contesti          2             (physicist 8, astronomer 6)
tab               0             asserzione negativa scritta
virgolette        28            esattamente 2 per unità, in tutte e 14
apici             11 EN su 4 unità (6, 7, 12, 13) / 14 IT su 6 unità (3, 5, 6, 10, 13, 14)
segnaposto        0             asserzione negativa scritta
identiche         0             14 tradotte
etichette         14 su 14, una per unità, in testa
```

## 3. Le tre cose che il lotto ha di proprio

1. **Un refuso del sorgente, dichiarato e non replicato.** Le unità 370 e 371 portano l'etichetta `Frustation.` (senza la
   prima `r`) invece di `Frustration.`. In italiano la parola è **«Frustrazione»** in tutte e tre le unità — 370, 371 e la
   397, che ha l'etichetta scritta correttamente. Il `check.py` cita l'etichetta inglese **come sta nel sorgente**
   (`Frustation` ×2, `Frustration` ×1), così un cambio futuro del testo diventa rosso; e asserisce che in italiano
   «Frustation» non compaia mai.
2. **Una normalizzazione dichiarata.** Il sorgente scrive `The Twilight Nebula` in 394, `the Twilight nebula` **minuscolo**
   in 395 e di nuovo `The Twilight Nebula` in 396. La resa usa sempre la maiuscola: è il nome dell'oggetto, non una
   descrizione. La divergenza è asserita come **IT 3 / EN 2** con la stringa `Twilight nebula` presente solo in inglese.
3. **Otto apici in una sola unità** (398, `Annoyance`): `'Nord'`, `'Ovest'`, `'senso di rotazione'`, `'verso il bordo'`.
   Sono quattro virgolette semplici, cioè il massimo per unità della campagna, e il `check.py` le verifica **per unità**
   (`13: 8`) oltre che nel totale (11 EN / 14 IT).

## 4. Copertura del file

```
L233   22 unità   righe  32 -  91
L234   20 unità   righe 115 - 180
L235   15 unità   righe 197 - 280
L236   23 unità   righe 301 - 344
L237   14 unità   righe 369 - 399
residuo 21 unità  righe 418 - 507
------------------------------------
22 + 20 + 15 + 23 + 14 + 21 = 115 = unità del file (min 32, max 507)
```

Copertura **94/115 (81,7%)**. Confine misurato: **riga 418**, `news:avgi engineer`. Restano **21 unità in quattro
contesti** (engineer 7, artist 3, performer 3, doctor 8): L238 le prende tutte e **chiude il file**.

## 5. Controlli che hanno morso

Nessuno al primo giro: `check.py` e `verify.py` sono usciti verdi entrambi. Il `verify.py` è stato scritto **dopo** aver
misurato le tre divergenze (§3), non prima: le asserzioni su `Frustation`, su `Twilight Nebula` e sugli otto apici
sarebbero state tre rosse su un lotto corretto se le avessi derivate dal lotto precedente.

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: le 14 unità sono `PENDING`.
- **Nessuna notizia vista nel gioco**.
- **Nessuna revisione umana**.
- **Il file non è completo**: 94/115 (81,7%); restano 21 unità.
