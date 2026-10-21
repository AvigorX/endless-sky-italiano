# REPORT — L239 (`data/avgi/avgi jobs.txt`, righe 20–656)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **30 controlli** (`FAIL totale: 0`); `verify.py` esce 0 con **22 controlli**
(invariante di segmento: 0 prima, 62 qui, 40 dopo). `state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su
`state.db`: le 62 unità restano `PENDING`.

## 1. Cosa contiene il lotto

| famiglia | contesti | unità | cosa sono |
|---|---|---|---|
| `Cargo to <planet>` | 9 | 18 | carico piccolo, tre taglie × tre gruppi merce (`Generic`, `Avgi Cargo`, `Avgi Nuclear`) |
| `Bulk cargo to <planet>` | 6 | 12 | carico sfuso, tre taglie × due gruppi |
| `Rush delivery to <planet>` | 9 | 18 | consegna urgente con `<date>`, tre taglie × tre gruppi |
| `Specialists to <planet>` | 2 | 4 | specialisti con competenze specifiche |
| `Researchers to <planet>` | 2 | 4 | ricercatori per un periodo alla stazione di ricerca (Ergastirio) |
| `Diplomats to <planet>` | 3 | 6 | negoziare con operai scontenti, placare gli Avgi scontenti (×2) |

## 2. Misure

```
unità             62            (31 VALUE invariati + 31 DESCRIPTION tradotte)
parole            432 EN -> 483 IT
rapporto          0,97 - 1,22 (media 1,06)   gate 0,55-1,90
contesti          31            due unità ciascuno
tab               0             asserzione negativa scritta
virgolette        0             asserzione negativa scritta
apici             0             asserzione negativa scritta
segnaposto        133 su 6 simboli, parità per simbolo E per ordine
identiche         31 (i VALUE, per contratto) - 0 fra le DESCRIPTION
famiglie          6 DESCRIPTION (15/9/2/2/1/2) · 6 VALUE (9/6/9/2/2/3)
```

## 3. Le tre cose che il lotto ha di proprio

1. **I `VALUE` sono dati, non prosa.** I 31 nomi di lavoro si copiano **carattere per carattere** dal sorgente e il
   `verify.py` lo verifica (`italian == english` per indice). *Non* è quello che hanno fatto cinque lotti antichi:
   `Rush delivery to <planet>` era stato reso «Consegna urgente a `<planet>`» in `jobs.txt` (L22, 5 unità) e in
   `intro missions.txt` (L21b, 4), e «… su `<planet>`» in `human missions.txt` (L18) e `remnant 1 introduction.txt`
   (L24). I due lotti di **lavori** più recenti — `coalition jobs.txt` (L151) e `hai jobs.txt` (L198) — li hanno lasciati
   **invariati**, ed è la linea che questo lotto segue: la divergenza è dichiarata in `review.md` §1.
2. **Una `DESCRIPTION` ripetuta quindici volte.** La resa non si sceglie quindici volte: si sceglie **una volta** e si
   verifica come **famiglia** (indici attesi + stringa unica). La stringa scelta — «Consegna `<cargo>` su
   `<destination>`. Il pagamento è `<payment>`.» — è **già nel corpus 24 volte**, e il `check.py` la cerca nei
   `translation.json` dei lotti precedenti: la coerenza cross-lot è **misurata**, non dichiarata a parole.
3. **Due simboli con lo stesso conteggio.** `<planet>` e `<destination>` compaiono **31 volte ciascuno**: un confronto
   sui soli totali passerebbe anche se fossero stati scambiati. Il `verify.py` confronta quindi **l'ordine dei
   segnaposto dentro ogni unità**, oltre al multiset per simbolo.

## 4. Copertura del file

```
L239   62 unità   righe  20 -  656
residuo 40 unità  righe 684 - 1156
------------------------------------
62 + 40 = 102 = unità del file (min 20, max 1156)
```

Copertura **62/102 (60,8%)**. Confine misurato: **riga 684**, `mission:Avgi: Doctors 1`. Restano **40 unità in 20
contesti** (medici, materiali da costruzione, materiali sfusi, materiali nucleari, corriere di informazioni, Twilight
Guardsmen, Guard Officers, Flag Officers, Shore leave): **L240 le prende tutte e chiude il file**.

## 5. Controlli che hanno morso

Un solo rosso, e non era un controllo ma il **file stesso**: il `check.py` non compilava per una stringa con
l'apostrofo di `gia'` dentro un letterale a virgoletta singola (`SyntaxError: unterminated string literal`). Corretto il
letterale, non il testo. Il `check.py` è poi uscito verde al primo giro, e il `verify.py` pure.

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: le 62 unità sono `PENDING`.
- **Nessun lavoro visto nel gioco**: la resa dei segnaposto è verificata sul **testo**, non a schermo.
- **Nessuna revisione umana**.
- **Il file non è completo**: 62/102 (60,8%); restano 40 unità.
