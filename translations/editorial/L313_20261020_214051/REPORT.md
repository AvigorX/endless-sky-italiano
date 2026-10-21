# REPORT — L313 (`data/bunrodea/bunrodea outfits.txt`, righe 250–402) — **LOTTO TERMINALE**

**Esito: lotto CHIUSO, file CHIUSO a 33/33.** `check.py` esce 0 con **25 controlli**; `verify.py` esce 0 con **22 controlli**.
`state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 9 (`DESCRIPTION`) | 9 |
| parole | 327 | **339** (1,037) |
| tab | **0** | **0** |
| virgolette | **0** | **0** |
| segnaposto / alternative | 0 / 0 | **0 / 0** |
| apici | **2** | 6 |

Rapporto per unità **1,02 – 1,31**: il lotto **cresce** in italiano, e la ragione è strutturale — le unità inglesi sono frasi
**compatte** con participi (`opting to make use of`, `leaving more room for`), che in italiano chiedono una **subordinata esplicita**
(«scegliendo motori che producono», «lasciando più spazio a»).

## 2. Invariante di FILE

```
FILE        33/33 (100%) · somma lotti 12 (L311) + 12 (L312) + 9 (L313) = 33
RIGHE       33 distinte · prima 25 · ultima 402 · zero dopo la 402
```

`data/bunrodea/bunrodea outfits.txt` è il **trentunesimo** file chiuso nel progetto (**90** su 167). Come in L310 e L309, il
`verify.py` **asserisce** la copertura, perché il file è **chiuso**; nei lotti non terminali la copertura resta **stampata**.

## 3. Il lotto in due metà

**Prima metà — perché i Bunrodea sparano.** La riga 250 racconta la **guerra con i Korath**: gli abbordaggi dei **predoni** in cerca
di tecnologia rendono le **armi leggere** essenziali per ogni equipaggio. È il pezzo che dà senso al `Lasher Pistol` e al fatto che
le navi Bunrodea siano piene di **cannoni frontali**.

**Seconda metà — perché i Bunrodea virano.** Le otto unità `Rift` sono un **confronto continuo con i Korath**:

| tema | Bunrodea | Korath |
|---|---|---|
| potenza | meno spinta, **molto meno calore** | **potenza bruta** |
| energia | fabbisogno **alto per unità di spinta**, ma **complessivamente inferiore** | terribilmente inefficienti |
| movimento | **velocità di virata** invece di velocità | — |
| dottrina | cannoni frontali, quindi **puntare bene** | — |

Il filo è dichiarato esplicitamente e il test lo verifica: «potenza bruta», «fabbisogno», «velocità di virata», «cannoni frontali».

## 4. La scala dei quattro nomi

```
Chiisana (piccolo)  ->  Nami (onda)  ->  Ookii (grande)  ->  Subarashii (meraviglioso)
```

Quattro propulsori e quattro timoni, **gli stessi quattro prefissi**, **invariati**. Il test li conta **per prefisso** (`2, 2, 2,
2`): se qualcuno avesse tradotto `Chiisana` in «piccolo» da una parte sola, il conteggio lo direbbe.

## 5. La voce che apre il finale

La riga 327 è l'unica unità **narrativa** del lotto:

> «Ma fra alcuni Bunrodea circolano voci di una **riserva antica** di motori, più potenti perfino di quelli dei Korath, che
> permetterebbe a qualsiasi nave di **sfrecciare fra le stelle come una cometa** e di raggiungere qualunque possibile bersaglio.»

È un **aggancio di gioco** (un motore migliore esiste, da qualche parte) e la resa lo lascia **aperto**, senza aggiungere
rivelazioni.

## 6. Verifica

```
check.py   25 controlli · FAIL totale: 0 · exit 0
verify.py  22 controlli · FAIL: 0 · exit 0
FILE       33/33 (100%) · trentunesimo file completo
```

**Nessun rosso**: primo giro verde, con **una correzione preventiva** — un controllo dei nomi era tautologico (`context ==
context.replace(...)`) e l'ho reso **falsificabile** prima di chiudere: ora verifica l'assenza di «frattura»/«spaccatura» e la
presenza di `rift` nel testo italiano.

## 7. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 9 unità `PENDING`; il file è **finito in staging**, non approvato.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Il giapponese non è verificato**: `Chiisana`, `Nami`, `Ookii`, `Subarashii` restano **come nel sorgente**; la traduzione dei
  significati («piccolo», «onda», «grande», «meraviglioso») è **glossa di lavoro**, non parte del testo di gioco.
- **Il file è completo al 100%** solo in staging.
