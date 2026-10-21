# REPORT — L295 (`data/human/marauders.txt`, righe 548–858)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **19 controlli**; `verify.py` esce 0 con **22 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 9 (tutte `DESCRIPTION`) | 9 |
| parole | 494 | **534** (1,08) |
| tab / virgolette / segnaposto / alternative | 0 / 0 / 0 / 0 | **0 / 0 / 0 / 0** |
| apici | 8 | 14 |

Rapporto per unità **1,08 – 1,21**.

## 2. La ripetizione del sorgente

Le unità 8 e 9 (righe **831** e **858**) sono **lo stesso testo**. Non è un artefatto dell'estrazione: il file contiene
davvero la stessa scheda due volte.

Conseguenza per la resa: **le due traduzioni devono essere identiche**, e il test lo verifica **in entrambe le lingue**. Un
traduttore che avesse reso le due unità «meglio» l'una dell'altra avrebbe introdotto una differenza inesistente nel gioco.

## 3. Le frasi condivise

Il file usa **formule ricorrenti** dentro le serie, e il test verifica le chiusure esatte:

- **`Manta`**: la 5 e la 6 finiscono con «Se il suo tonnellaggio a vuoto fosse appena più alto, sarebbe classificata come nave da
  guerra pesante.»; la 4 ha la variante «È solo il tonnellaggio a vuoto a impedirle di essere classificata…»;
- **`Quicksilver`**: la 7 e la 8 contengono entrambe «forse in risposta alla `Headhunter` della Lionheart» (in inglese la 7 dice
  `in an answer to`, la 8 `in response to`: **due formule diverse, una sola resa** — è la regola del corpus applicata a una
  variante minima).

## 4. Terminologia: due parole inglesi, due rese

| inglese | resa | nota |
|---|---|---|
| `shield projectors` | **proiettori di scudi** | |
| `shield emitters` | **emettitori di scudi** | L294 |

Il gioco usa **due termini distinti** per due componenti diverse: appiattirli su un'unica parola italiana avrebbe confuso due
oggetti del gioco. Il test verifica che **entrambe** le forme esistano e che la 4 (che dice `emitters`) **non** contenga
«proiettori».

## 5. Verifica

```
check.py   19 controlli · FAIL totale: 0 · exit 0
verify.py  22 controlli · FAIL: 0 · exit 0
segmento   12 prima · 9 qui · 8 dopo la 858 · 3 serie da 3
```

**Primo giro verde**: il contratto aveva già individuato la ripetizione 831/858, le chiusure condivise e la distinzione
`projectors`/`emitters`.

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 9 unità `PENDING`.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Il file resta aperto**: 21/29; restano **8 unità** (`Quicksilver` ×2, `Raven` ×3, `Splinter` ×3) — sarà il lotto
  **terminale**.
- **La ripetizione 831/858 è nel sorgente**: non è stata «corretta» né segnalata come errore, perché il testo visibile nel gioco
  è quello.
