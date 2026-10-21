# REPORT — L293 (`data/avgi/avgi culture conversations.txt`, righe 260–270) — **LOTTO TERMINALE**

**Esito: lotto CHIUSO, file CHIUSO a 46/46.** `check.py` esce 0 con **21 controlli**; `verify.py` esce 0 con **20 controlli**.
`state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 9 (tutte `MISSION_TEXT`) | 9 |
| parole | 274 | **270** (0,99) |
| tab | 9 | 9 (**tutte** le unità) |
| virgolette | 10 | **10**, per unità |
| apici | 5 | 14 |
| segnaposto / alternative | 0 / 0 | **0 / 0** |

Rapporto per unità **0,95 – 1,31**.

## 2. Invariante di FILE

```
FILE         46/46 (100%) · 46 righe distinte · prima 24 · ultima 270 · zero dopo
SOMMA LOTTI  8 (L290) + 12 (L291) + 17 (L292) + 9 (L293) = 46
TIPI         44 MISSION_TEXT + 2 LOGBOOK (tutti nel file)
OVERLAP      nessun altro lotto rivendica le righe 260-270
```

## 3. Le righe che non esistono

Le unità del lotto sono a **260–267** e poi **270**: le righe **268 e 269** non contengono testo esportabile. Il test elenca le
**nove righe esatte** e confronta la lista, non un intervallo: un `range(260, 271)` avrebbe cercato due unità inesistenti e
fallito su un file corretto.

## 4. Gli atti dichiarati, fino all'ultimo

| inglese | resa |
|---|---|
| `Astonishment.` | **Stupore.** |
| `Repose.` | **Riposo.** |
| `Bewilderment.` | **Sconcerto.** |
| `Hysteria.` | **Isteria.** |
| `Adoration!` | **Adorazione!** |

Quattro con il **punto**, uno con il **punto esclamativo**: la punteggiatura segue il sorgente e il test verifica
`"Adorazione! Ti amo, Zomp!"` come stringa intera.

## 5. La scommessa

`I'm up 10 to 1 on this bet!` → **«Sono in vantaggio dieci a uno su questa scommessa!»**

I numeri restano **in lettere** («dieci a uno») perché la frase è **parlata**; il test verifica sia «dieci a uno» sia la presenza
di `10 to 1` nell'inglese, così una resa numerica o un cambio di rapporto sarebbero visibili.

## 6. Terminologia

| inglese | resa |
|---|---|
| `the duelists leap into the air` | **i duellanti balzano in aria** |
| `clashing blades` | **incrociando le lame** |
| `darting in and out of each others' reach` | **entrando e uscendo dalla portata dell'altro** |
| `a loud ding` | **un ding sonoro** |
| `with their wing collapsed` | **con l'ala ripiegata** |
| `wing fluttering` | **frullare d'ali** |
| `eye-watering speed and agility` | **velocità e agilità da lacrime agli occhi** |
| `thunderous applause` | **applausi tonanti** |
| `various pink papers` | **varie carte rosa** |
| `in a chaos of cheers, boos and rumbling wing flapping` | **in un caos di acclamazioni, fischi e frullii sordi d'ali** |
| `you find no issue leaving` | **non hai problemi a lasciare** |

## 7. Verifica

```
check.py   21 controlli · FAIL totale: 0 · exit 0
verify.py  20 controlli · FAIL: 0 · exit 0
FILE       46/46 (100%) · ventiquattresimo file completo
```

**Primo giro verde**, senza correzioni: il contratto aveva già segnalato il salto 267 → 270, l'esclamativo di «Adorazione!» e la
scommessa.

## 8. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 9 unità `PENDING`; il file è **finito in staging**, non approvato.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Il file è completo al 100%** solo in staging.
- **La rima `Zomp`/`stomp`** del cartello (L292) resta persa: limite dichiarato.
