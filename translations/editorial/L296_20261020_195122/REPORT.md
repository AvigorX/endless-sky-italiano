# REPORT — L296 (`data/human/marauders.txt`, righe 884–1146) — **LOTTO TERMINALE**

**Esito: lotto CHIUSO, file CHIUSO a 29/29.** `check.py` esce 0 con **21 controlli**; `verify.py` esce 0 con **23 controlli**.
`state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 8 (tutte `DESCRIPTION`) | 8 |
| parole | 505 | **532** (1,05) |
| tab / virgolette / segnaposto / alternative | 0 / 0 / 0 / 0 | **0 / 0 / 0 / 0** |
| apici | 10 | 10 |

Rapporto per unità **1,03 – 1,21**.

## 2. Invariante di FILE

```
FILE         29/29 (100%) · 29 righe distinte · prima 62 · ultima 1146 · zero dopo
SOMMA LOTTI  12 (L294) + 9 (L295) + 8 (L296) = 29
OVERLAP      nessun altro lotto rivendica le righe 884-1146
```

## 3. La ripetizione 884/910

Le unità 1 e 2 sono **lo stesso testo** (già previsto dal contratto, come 831/858 in L295). La resa è **identica** e il test lo
verifica in **entrambe le lingue**. Con questa, le ripetizioni riprodotte nel file sono **due coppie**: 831/858 e 884/910.

## 4. La seconda persona: tre unità, non una

| unità | inglese | resa |
|---|---|---|
| 3 | `that you expect` | «che **ti** aspetti» |
| 5 | `making you wonder` | «il che fa chiedere» |
| 7 | `You're not likely to find` | «Non è probabile che **tu** trovi» |

Il contratto prevedeva **una** sola occorrenza (riga 1114). Il test **elenca le tre righe** e il documento lo dichiara: una
regola «niente seconda persona» avrebbe fallito su un testo corretto, e una regola «seconda persona libera» avrebbe mancato il
controllo.

## 5. Le formule delle serie

- **`Raven`** (968, 996, 1026): tutte e tre dicono che lo scafo centrale si riconosce **solo grazie alle ali**;
- **`Splinter`** (1083, 1114, 1146): tutte e tre parlano di **ampie sezioni dello scafo** coperte di emettitori e corazzatura.

Il test verifica la presenza in **tutte** le varianti: se una sola l'avesse persa, la serie sarebbe diventata tre schede
scollegate.

## 6. Terminologia

| inglese | resa |
|---|---|
| `even bigger gun ports` | **porti per cannoni ancora più grandi** |
| `apparently-flimsy bulkheads` | **paratie apparentemente fragili** |
| `lithe Raven` | **snella Raven** |
| `Two more engine bays` | **Due baie motore in più** |
| `new engine port` | **nuovo porto motore** |
| `sub-kiloton warship` | **nave da guerra sotto il kilotonnellaggio** |
| `two new forward hard points on either side of the bridge` | **due nuovi punti di attacco anteriori ai lati del ponte di comando** |
| `agile and flexible war machine` | **macchina bellica agile e versatile** |
| `pretty unappealing` | **piuttosto poco invitante** |

## 7. Verifica

```
check.py   21 controlli · FAIL totale: 0 · exit 0
verify.py  23 controlli · FAIL: 0 · exit 0
FILE       29/29 (100%) · venticinquesimo file completo
```

**Un rosso al primo giro** (controllo mio, non la resa): il test dichiarava la seconda persona in **due** unità (5, 7); misurate
**tre** (3, 5, 7). Corretto l'elenco.

## 8. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 8 unità `PENDING`; il file è **finito in staging**, non approvato.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Il file è completo al 100%** solo in staging.
- **Le due coppie ripetute** (831/858, 884/910) sono **nel sorgente**: riprodotte, non corrette.
