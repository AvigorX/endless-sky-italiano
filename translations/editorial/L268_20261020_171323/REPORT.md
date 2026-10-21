# REPORT — L268 (`data/human/engines.txt`, righe 195–323)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **21 controlli**; `verify.py` esce 0 con **21 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 15 (tutte `DESCRIPTION`) | 15 |
| parole | 450 | **459** (1,02) |
| tab | 8 | 8 · primo carattere |
| virgolette | 0 | 0 |
| apici | 0 | 6 |
| segnaposto | 0 | 0 |

Rapporto per unità **0,96 – 1,28**.

## 2. Il lotto

Otto equipaggiamenti in sei blocchi di due schede (la scheda del modello + la nota ionica, che si ripete):

| equipaggiamento | che cosa dice |
|---|---|
| **X5700 Ion Thruster** | per le navi capitali più grandi; all'inizio era «poco più che un colpo pubblicitario» |
| **X1200 Ion Steering** | il più piccolo set di sterzata; adatto solo ai droni senza pilota |
| **X2200 Ion Steering** | caccia e piccoli vascelli; su navi grandi quando la manovrabilità non serve |
| **X3200 Ion Steering** | piccole navi da guerra e mercantili; più efficiente delle alternative al plasma |
| **X4200 Ion Steering** | potente, per le navi da guerra: nei mercantili la sterzata rapida raramente serve |
| **X5200 Ion Steering** | così grande che poche navi lo montano; prodotto in piccole quantità |
| **X1100 Ion Reverse Thruster** | per le navi troppo goffe o con carichi delicati; va montato nella **sezione delle armi** |

## 3. La scheda ionica, settima volta

> «I motori ionici consumano meno energia dei motori al plasma e producono meno calore, ma occupano anche più spazio a parità
> di spinta.»

Compare **sette volte** in questo lotto (unità 1, 3, 5, 7, 9, 11, 13) e il `check.py` la confronta con la resa **letta da
`L267/translation.json`**: se una sola copia divergesse, il test sarebbe rosso anche con conteggi identici.

## 4. `reverse thruster` → «propulsore inverso»

Termine **nuovo** nel corpus: la scheda spiega che le navi di solito **si girano** per usare i propulsori principali in
decelerazione, e che un propulsore inverso serve alle navi «troppo goffe» o con carichi sensibili. La resa conserva entrambe
le informazioni, compreso il dettaglio pratico del **montaggio** (`sezione delle armi`, non `dei motori`), che è ciò che il
giocatore deve sapere per installarlo.

## 5. Verifica

```
check.py   21 controlli · FAIL totale: 0 · exit 0
verify.py  21 controlli · FAIL: 0 · exit 0
segmento   12 prima · 15 qui · 34 dopo la 323 · copertura 27/61 (44,3%)
```

Un rosso al primo giro: cercavo la stringa letterale «sezione dei motori», mentre la resa dice «anziché in quella dei
motori» — il controllo era troppo rigido sul testo, non la resa. Corretto in un controllo sul **contenuto** (le due sezioni
e il nesso «anziché»).

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 15 unità `PENDING`.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Il file resta aperto**: 27/61.
