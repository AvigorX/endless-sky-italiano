# REPORT — L254 (`data/wanderer/wanderer jobs.txt`, righe 458–888)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **32 controlli**; `verify.py` esce 0 con **28 controlli** (invariante di
segmento: 50 prima, 41 qui, **1** dopo). `state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Cosa contiene il lotto

| blocco | unità | contenuto |
|---|---|---|
| `Wanderer Invasive Species [1]` | 2 `DIALOG` | la coda della quarantena, variante **pianta** (L253 aveva l'animale) |
| `phrase:wanderer cargo delivery payment` | 1 `TEXT` | la battuta di consegna dei carichi: `<commodity>` consegnato, ringraziamento, `<payment>` |
| `Wanderer Cargo [0..4]` | 5 `VALUE` + 5 `DESCRIPTION` | `Delivery to <planet>` + scheda generica |
| `Wanderer Rush Delivery [0..3]` | 4 + 4 | `Rush delivery to <planet>` + scheda con `<date>` |
| `Wanderer Bulk Delivery [0..2]` | 3 + 3 | `Bulk delivery to <planet>` + scheda generica |
| `Wanderer Captured Unfettered` | 1 + 1 + 1 | `<bunks>` soldati Slegati catturati |
| `Wanderer Governor Transport` | 1 + 1 | il governatore locale, in tutta comodità |
| `Wanderer Kor Efreti: Equipment` / `Cargo [0..1]` | 3 + 3 | forniture ai **Kor Efreti** |
| `Wanderers to Kor Efreti` | 1 + 1 + 1 | spedizione di studio su un mondo **Kor Efret** |

## 2. Misure

```
unità             41            (18 VALUE + 18 DESCRIPTION + 4 DIALOG + 1 TEXT)
parole            426 EN -> 434 IT       rapporto 0,94 - 1,17 (media 1,06)
contesti          20            19 missioni + 1 blocco `phrase`
tab / virgolette  0 / 0         due asserzioni negative scritte
apici             3 EN / 1 IT
segnaposto        83 in 9 famiglie; <cargo> e <destination> 15 e 15
stringhe distinte 17            6 gruppi con 8, 8, 4, 4, 3, 3 copie
```

## 3. Le tre cose che il lotto ha di proprio

1. **Il `TEXT` è un blocco `phrase:`.** Non è un nome da copiare né una scheda di missione: è la frase che il gioco compone
   quando consegni un carico (`You drop off your cargo of <commodity>. The Wanderers thank you…`). Va **tradotta**, e il
   controllo la isola dagli altri tipi; il `verify.py` pretende che resti una frase intera (inizia con «Scarichi» e finisce
   con il punto), così un frammento non passa.
2. **Le schede generiche sono ripetute 8 e 4 volte**, e la resa è quella che il corpus usa **39 e 17 volte**. Il controllo
   **calcola la forma dominante a runtime** leggendo i `translation.json`: se domani il corpus cambia, il test lo dice.
3. **`Unfettered` sopravvive solo nel `VALUE`.** Il nome del lavoro `Captured Unfettered to <planet>` è un **dato** e resta
   inglese; nella prosa la fazione è «**Slegati**». Il controllo asserisce **entrambe** le cose — e la prima versione
   falliva proprio perché guardava l'intero lotto invece della sola prosa.

## 4. Le decisioni editoriali

| punto | decisione | perché |
|---|---|---|
| `Delivery to <planet>` e gli altri nomi di lavoro | **copiati** | sono `VALUE`; il corpus ha 13 «Consegna a `<planet>`» e 11 «Consegna urgente…» da lotti antichi: divergenza **storica dichiarata**, non replicata |
| `Deliver <cargo> to <destination>. Payment is <payment>.` | **«Consegna `<cargo>` su `<destination>`. Il pagamento è `<payment>`.»** | forma dominante (39) |
| `… by <date> …` | **«… entro il `<date>` …»** | forma dominante (17) |
| `the Kor Efreti on <destination>` | **«ai Kor Efreti su `<destination>`»** | prima occorrenza nel corpus |
| `captured Unfettered soldiers` | **soldati Slegati catturati** | |
| `you'll need suitable facilities to transport them` | **«ti servono strutture adatte al loro trasporto»** | |
| `the local governor` | **il governatore locale** | |
| `the capital city of <planet>` | **la capitale di `<planet>`** | |
| `They expect a comfortable journey` | **«Si aspetta un viaggio confortevole»** | `they` singolare: «si aspetta» evita il pronome di genere |
| `this mix of … scientists, botanists, and terraforming experts` | **«questo gruppo misto di … scienziati, botanici ed esperti di terraformazione»** | |
| `Kor Efret world of <stopovers>` | **«mondo Kor Efret di `<stopovers>`»** | `Kor Efret` e `Korath` invariati |
| `plant elsewhere` | **«perché le piantino altrove»** | |

## 5. Difetti trovati

Due rossi, **entrambi d'asserzione**:

1. il controllo del lessico cercava `Unfettered` **assente da tutto il lotto**, ma il `VALUE` copiato lo contiene per
   costruzione: riscritto perché l'assenza valga **nella prosa** e la presenza sia **asserita nel `VALUE`**;
2. lo stesso controllo pretendeva almeno 10 occorrenze di `Wanderer` nella prosa: misurate **6** (le altre sono nei `VALUE`
   o nei nomi di contesto). Corretto il numero.

## 6. Copertura del file

```
L252   26 unità   righe  15 - 261
L253   24 unità   righe 264 - 442
L254   41 unità   righe 458 - 888
---------------------------------
91 unità su 92 (98,9%)

residuo 1 unità, riga 891   → lotto TERMINALE
```

## 7. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: le 41 unità sono `PENDING`.
- **Nessun testo visto nel gioco**.
- **Nessuna revisione umana**.
- **Il file non è completo**: 91/92; resta una unità.
