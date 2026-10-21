# REPORT — L318 (`data/korath/korath weapons.txt`, righe 53–603)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **22 controlli**; `verify.py` esce 0 con **20 controlli**. Il file è a **17/39
(43,6%)**. `state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 17 (`DESCRIPTION`) | 17 |
| parole | 477 | **493** (1,034) |
| tab | **2** | **2** |
| virgolette | **0** | **0** |
| segnaposto / alternative | 0 / 0 | **0 / 0** |
| apici | **3** | 11 |

Rapporto per unità **0,86 – 1,28**: il minimo è la **battuta** della riga 154 («Ai Korath piace tenere i nemici vicini... ma non
troppo.»), dove l'italiano è più **asciutto** dell'inglese; il massimo sono le due schede brevi dei `Piercer`, dove «Questo missile
viene lanciato da…» richiede l'articolo e il verbo.

## 2. Invariante di segmento (il file non è finito)

```
PRIMA     zero unità prima della 53: il lotto APRE il file
QUI       17 unità, righe distinte 53–603
DOPO      22 unità / 612 parole (la prossima alla 615)
COPERTURA 17/39 (43,6%) — STAMPATA, non asserita
```

## 3. Un errore del contratto, corretto dalla misura

Il contratto dichiarava un **refuso** alla riga 154: «due punti finali (`close..`)». **La misura dice il contrario.** Il sorgente è

```
The Korath like to keep their enemies close... but not too close.
```

un'**ellissi** legittima. I «due punti» erano un **artefatto dell'anteprima troncata** con cui avevo riassunto l'unità nel
contratto. Conseguenze:

- la resa usa `...` come tutto il progetto («vicini... ma non troppo»);
- **nessun refuso** è stato dichiarato per questo lotto, perché **non ce n'erano**;
- il test verifica l'**ellissi** e l'**assenza** di `..` residui — cioè verifica il fatto misurato, non la dichiarazione sbagliata.

È il caso in cui la regola «il workspace vince sui documenti» ha un **contenuto**: non basta ripeterla, bisogna **misurare**.

## 4. La nota dei rifornimenti: 4 rese per una frase

`Ammunition for this weapon can be restocked at any outfitter.` — **36 unità** nel database, **26** già in staging, e **quattro**
rese diverse:

| resa | unità |
|---|---|
| **«Le munizioni per quest'arma possono essere rifornite presso qualsiasi emporio.»** | **16** ← usata in L318 |
| «Le munizioni di quest'arma si possono rifornire in qualsiasi emporio.» | 5 |
| «…presso qualsiasi negozio di equipaggiamenti.» | 3 |
| «…si possono rifornire in qualsiasi negozio di equipaggiamenti.» | 2 |

La resa scelta è la **di maggioranza**, e le due varianti con «negozio di equipaggiamenti» contraddicono anche la decisione
`outfitter` → **«emporio»**. L'incoerenza è **dichiarata e non corretta**: correggere i lotti altrui non è compito di un lotto, e
avrebbe reso il test di questo lotto **dipendente** da una riscrittura.

I due script la verificano in **due modi diversi**:
- `check.py`: confronto con **una** unità precedente scelta per testo inglese;
- `verify.py`: ricerca della **stringa italiana** in tutti gli altri lotti, con soglia «≥2 occorrenze».

## 5. Il filo del lotto: il fuoco e la fisica

Le armi Korath sono **tutte** un modo di negare il movimento all'avversario:

| come | arma |
|---|---|
| **tirare** | `Grab-Strike` (verso la nave Korath) |
| **respingere** | `Expeller` (dalle portanavi e dai civili), `Banisher` («vicini… ma non troppo») |
| **bloccare** | `Detainer` (disturba la **propulsione**) |
| **sfondare** | `Piercer` (la testata piccola apre il varco, la grande passa) |
| **dissolvere** | `Shunt-Strike` (i microbot **convertono lo scafo**) |

E sopra tutte, la **scala del fuoco**: una `Fire-Lance`, due in **gestalt** (`Blaze-Pike`), tre in **sinergia** (`Inferno`), che è
«il vertice del progetto delle armi dell'Esilio». La resa tiene la progressione: **gestalt** resta invariato (è un prestito tecnico
usato in italiano), **sinergia** è tradotto.

## 6. Verifica

```
check.py   22 controlli · FAIL totale: 0 · exit 0
verify.py  20 controlli · FAIL: 0 · exit 0
copertura  17/39 (43,6%) — stampata, non asserita
```

**Nessun rosso**: primo giro verde, con la correzione del contratto fatta **prima** di scrivere il test.

## 7. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 17 unità `PENDING`; il lotto è **in staging**.
- **Nessun testo visto nel gioco**: le armi sono verificate **nei dati**, non a schermo.
- **`heat shunts` → «dissipatori di calore»**: scelta dichiarata, **senza precedente nel corpus** (la parola compare una volta sola
  in un testo lungo e non ne ho una resa consolidata).
- **L'incoerenza della nota dei rifornimenti resta aperta**: 4 rese su 26 unità.
