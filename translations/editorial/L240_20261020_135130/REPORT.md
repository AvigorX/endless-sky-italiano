# REPORT — L240 (`data/avgi/avgi jobs.txt`, righe 684–1156)

**Esito: lotto CHIUSO, e con lui il file.** `check.py` esce 0 con **31 controlli** (`FAIL totale: 0`); `verify.py` esce 0
con **25 controlli** e l'**invariante di FILE** `62 + 40 = 102`. `state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura
su `state.db`: le 40 unità restano `PENDING`.

`data/avgi/avgi jobs.txt` è **completo in staging: 102/102 (100%)**, 902 EN → 959 IT, **due lotti** (L239–L240). È il
**nono file chiuso** della campagna.

## 1. Cosa contiene il lotto

| famiglia | unità | contenuto |
|---|---|---|
| `Doctors to <planet>` | 3 | cure e servizi medici in cambio di `<payment>` |
| `Construction materials to the <planet>` | 3 | `<cargo>` **da `<origin>`** a `<destination>`, per sostenere la costruzione |
| `Bulk materials to the <planet>` | 3 | la stessa formula, merce sfusa |
| `Special nuclear materials to <planet>` | 3 | consegna **entro il `<date>`** con l'avvertimento sui pirati |
| `Information courier to <planet>` | 2 | supporti di memoria per aggiornare la rete locale di `<planet>` |
| `Twilight Guardsmen to <planet>` | 1 | trasporto di semplici guardie |
| `Twilight Guard Officers to <planet>` | 1 | trasporto **confortevole** di ufficiali |
| `Twilight Guard Flag Officers to <planet>` | 1 | trasporto confortevole di ufficiali superiori |
| `Shore leave on <planet>` | 3 | licenza a terra per chi torna dal fronte |

## 2. Misure

```
unità             40            (20 VALUE invariati + 20 DESCRIPTION tradotte)
parole            470 EN -> 476 IT
rapporto          0,90 - 1,14 (media 0,99)   gate 0,55-1,90
contesti          20            due unità ciascuno
tab / virgolette  0 / 0         asserzioni negative scritte
apici             2 EN (`<planet>'s`) / 0 IT
segnaposto        99 su 7 simboli, parità per simbolo E per ordine
famiglie          8 DESCRIPTION (6·3·3·3·2·1·1·1) · 9 VALUE
```

## 3. Le tre cose che il lotto ha di proprio

1. **`<origin>` entra per la prima volta** (6 unità, tutte nei materiali da costruzione) e convive con `<destination>`
   nella stessa frase: la partenza e l'arrivo non si invertono, e il `verify.py` confronta le **posizioni** dei due
   segnaposto (non i totali: `<destination>` 26 contro `<origin>` 6 passerebbe anche con uno scambio).
2. **Il `the` dentro un `VALUE`**: `Construction materials to the <planet>` e `Bulk materials to the <planet>` contengono
   l'articolo inglese, e restano **identici** — sono dati. Il `check.py` asserisce che le sei unità che lo contengono lo
   conservino, così una «pulizia» futura diventa rossa.
3. **Gli unici due apostrofi del lotto sono il possessivo `<planet>'s`** (righe 988 e 1009). In italiano il possessivo non
   esiste («la rete locale di `<planet>`») e gli apostrofi sono **zero**: la differenza è dichiarata e misurata, non
   nascosta in un totale che torna per caso.

## 4. Copertura del file (invariante di FILE)

```
L239   62 unità   righe  20 -  656
L240   40 unità   righe 684 - 1156
------------------------------------
62 + 40 = 102 = unità del file (min 20, max 1156)
```

La copertura si legge dai **due** `translation.json`, si confronta con il database e pretende **102 id distinti su 102
righe distinte**, `max(line) = 1156`, `line > 1156` vuoto.

## 5. Controlli che hanno morso

Nessuno: `check.py` e `verify.py` sono usciti verdi al primo giro. Il merito è del contratto di L239, che aveva già
misurato i due punti delicati (`<origin>`, il `the` nei `VALUE`) e del fatto che le formule sono **otto**, non venti: la
resa si è scritta otto volte, non quaranta.

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: le 40 unità sono `PENDING`; il file è completo **in staging**, non nel database.
- **Nessun lavoro visto nel gioco**: i segnaposto sono verificati sul **testo**, non a schermo.
- **Nessuna revisione umana**.
- **I nomi delle famiglie di merce** (`Doctors`, `Construction materials`, …) compaiono solo nei **contesti**, non nel
  testo: non sono stringhe da tradurre.
