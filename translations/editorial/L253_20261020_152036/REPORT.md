# REPORT — L253 (`data/wanderer/wanderer jobs.txt`, righe 264–442)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **34 controlli**; `verify.py` esce 0 con **29 controlli** (invariante di
segmento: 26 prima, 24 qui, 42 dopo). `state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`: le 24 unità
restano `PENDING`.

## 1. Cosa contiene il lotto

| missione | unità | contenuto |
|---|---|---|
| `Wanderer Biologists` | 2 `VALUE` + 2 `DESCRIPTION` + 2 `DIALOG` | `<bunks>` biologi a studiare una specie animale appena scoperta |
| `Wanderer Botanists` | 2 + 2 + 2 | `<bunks>` botanici a studiare una specie vegetale |
| `Wanderer Harvest` | 2 + 2 + 2 | `<bunks>` Wanderer alla raccolta del cibo |
| `Wanderer Invasive Species` | 2 + 2 (+2 `DIALOG` nel solo `[0]`) | quarantena: schede diverse per **animale** e **pianta**, battute in due parti |

## 2. Misure

```
unità             24            (8 VALUE + 8 DESCRIPTION + 8 DIALOG)
parole            427 EN -> 406 IT       rapporto 0,84 - 1,12 (media 1,03)
contesti          8             quattro missioni × due contatori
tab               0             asserzione negativa scritta
virgolette        0             asserzione negativa scritta
apici             0 EN / 1 IT   (unità 21, `un'ora`)
segnaposto        56 in 8 famiglie, multiset E ordine per unità
stringhe distinte 14            10 gruppi da 2 copie + 4 singolari
```

## 3. Le tre cose che il lotto ha di proprio

1. **Le due schede degli invasivi differiscono per una parola.** `invasive animal species` / `invasive plant species`: sono
   **stringhe diverse**, quindi **non** un gruppo — il `verify.py` asserisce che i loro testi inglesi siano diversi
   (`animal` / `plant`) e che anche le rese lo siano. Un controllo basato solo sul conteggio dei gruppi le avrebbe trattate
   come una copia sola.
2. **`<stopovers>` è un simbolo intero, e `<planet stopovers>` non compare.** Il controllo verifica l'identità di
   `<stopovers>` (2) **e l'assenza** dell'altro, in entrambe le lingue: due simboli diversi che un `split` sbagliato
   confonderebbe.
3. **La forma del pagamento segue il tempo inglese**: «Il pagamento **sarà**» nelle quattro schede degli studiosi (`Payment
   will be`), «Il pagamento **è**» nelle due del raccolto (`Payment is`), «in cambio di **un pagamento di**» nelle due degli
   invasivi (`for a payment of`). Tre formule, tre tempi, nessuna sinonimia arbitraria.

## 4. Le decisioni editoriali

| punto | decisione | perché |
|---|---|---|
| `biologists` / `botanists` | **biologi** / **botanici** | |
| `recently discovered animal species` | **specie animale scoperta di recente** | |
| `food harvest` | **raccolta del cibo** | |
| `contain an invasive species` | **contenere una specie invasiva** | «contenere» è il verbo della quarantena, non «fermare» |
| `cargo hold` | **stiva** | |
| `cages` | **gabbie** | |
| `Return the Wanderers to <origin> … for a payment of <payment>` | **«Riporta i Wanderer a `<origin>` … in cambio di un pagamento di `<payment>`»** | |
| `You wish … the best of luck` | **«Fai gli auguri ai …»** | stessa resa di L252 (dove era stata corretta da un frammento nominale) |
| `You wish the Wanderers the best of luck … and collect your payment` | **«Fai gli auguri ai Wanderer … e riscuoti il pagamento di `<payment>`»** | «riscuoti» per `collect`, come «Incassi» altrove: verbo di riscossione |

## 5. Difetti trovati

Nessun rosso: `check.py` e `verify.py` sono passati **al primo giro** (34 e 29 controlli). Le uniche correzioni sono state
editoriali, prima della verifica: la battuta del raccolto era «…e incassi il pagamento…» con rapporto 0,83; riscritta con
«riscuoti» (0,84) per restare più vicina a `collect` senza perdere scorrevolezza.

## 6. Copertura del file

```
L252   26 unità   righe  15 - 261
L253   24 unità   righe 264 - 442
---------------------------------
50 unità su 92 (54,3%)

residuo 42 unità, righe 458 - 891
```

## 7. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: le 24 unità sono `PENDING`.
- **Nessun testo visto nel gioco**.
- **Nessuna revisione umana**.
- **Il file non è completo**: 50/92 (54,3%).
