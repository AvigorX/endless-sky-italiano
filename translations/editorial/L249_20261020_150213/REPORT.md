# REPORT — L249 (`data/human/syndicate jobs.txt`, righe 291–431)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **32 controlli** (`FAIL totale: 0`); `verify.py` esce 0 con **28 controlli**
(invariante di segmento: 36 prima, 19 qui, 39 dopo). `state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su
`state.db`: le 19 unità restano `PENDING`.

## 1. Cosa contiene il lotto

| contesto | unità | contenuto |
|---|---|---|
| `Syndicate target practice [2]` | 4 `DIALOG` | la coda che L248 aveva lasciato aperta: scansione, errore, bersaglio distrutto, consegna |
| `Syndicate target practice [3]` | 1 `VALUE` + 1 `DESCRIPTION` + 4 `DIALOG` | la stessa missione, quarto contesto: **prosa identica** |
| `Syndicate Prisoner Transport [0]` | 1 `VALUE` + 1 `DESCRIPTION` + 1 `DIALOG` | dirigente incriminato, ai domiciliari con avvocati e `<cargo>` |
| `Syndicate Prisoner Transport [1]` | 1 `VALUE` + 1 `DESCRIPTION` + 1 `DIALOG` | sabotatore industriale condannato |
| `Syndicate Prisoner Transport [2]` | 1 `VALUE` + 1 `DESCRIPTION` + 1 `DIALOG` | `<bunks>` spie aziendali condannate |

## 2. Misure

```
unità             19            (4 VALUE + 11 DIALOG + 4 DESCRIPTION)
parole            438 EN -> 419 IT       rapporto 0,93 - 1,18 (media 1,04)
contesti          5             tutti con parentesi quadre nel nome
tab               0             asserzione negativa scritta
virgolette        2             unità 12: "arresti domiciliari"
apici             2 EN / 0 IT
segnaposto        22 in 5 famiglie, multiset E ordine per unità
ripresi da L248   9 unità di prosa (10 contando il VALUE)
stringhe distinte 15 (6 già in L248, 9 nuove)
```

## 3. La cosa che il lotto ha di proprio: la ripetizione

Dieci unità ripetono una stringa già tradotta in L248 — la missione `Syndicate target practice` continua nei contesti
`[2]` e `[3]`. Invece di riscriverle «uguali a memoria», il generatore le ha **lette dal `translation.json` di L248** e
copiate; e il `verify.py` **rilegge quel file** e confronta carattere per carattere.

È il controllo che rende la ripetizione un fatto e non una speranza: se domani una delle due copie viene «migliorata», il
lotto diventa rosso. Il `verify.py` verifica anche **quante** sono (10) e quante stringhe distinte vengono da fuori (6 su
15), così un riuso parziale o eccessivo si vede.

## 4. Le decisioni editoriali delle sei unità nuove

| punto | decisione | perché |
|---|---|---|
| `house arrest` | **«arresti domiciliari»**, fra virgolette | resa già presente nel corpus (3 occorrenze) |
| `white-collar criminal` | **«criminale dai colletti bianchi»** | |
| `indicted` | **«incriminato»** | |
| `libel lawsuits` | **«querele per diffamazione»** | |
| `their sentence` (saboteur) | **«la pena»** | evita il pronome di genere su una persona di cui il testo non dice il sesso |
| `They must be held` (spie) | **«Devono essere tenute»** | «spie» è femminile: l'accordo è verificato |
| `made for the transfer of criminals` | **«adatte al trasferimento dei criminali»** | |
| `chained together at the ankles` | **«incatenati insieme alle caviglie»** | |
| `more roughly than is strictly necessary` | **«con più rudezza del necessario»** | |
| `sunny smile` | **«sorriso radioso»** | |

## 5. Difetti trovati

Tre rossi, **tutti nelle asserzioni**:

1. «Il pagamento è `<payment>`.» elencato nelle sole unità 12, 15, 18: sono **quattro**, perché anche la scheda ripresa da
   L248 (unità 6) la contiene. Corretto l'elenco, non il testo;
2. un apostrofo italiano dentro un letterale a virgolette singole ha rotto il `check.py` (`SyntaxError`, trappola 99, quarta
   volta): letterale passato a virgolette doppie;
3. il `verify.py` dichiarava «8 stringhe nuove»: sono **9** (15 distinte − 6 già presenti). Riscritto con i tre numeri
   espliciti.

## 6. Copertura del file

```
L247   16 unità   righe  19 - 153
L248   20 unità   righe 157 - 275
L249   19 unità   righe 291 - 431
---------------------------------
55 unità su 94 (58,5%)

residuo 39 unità, righe 435 - 814
```

Confine misurato: **riga 435**, `mission:Syndicate Prisoner Transport [3]`.

## 7. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: le 19 unità sono `PENDING`.
- **Nessun testo visto nel gioco**.
- **Nessuna revisione umana**.
- **Il file non è completo**: 55/94 (58,5%).
