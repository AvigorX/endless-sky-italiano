# REVIEW — L122 · `campaign events.txt` (memoriali, Bloodsea, Geminus, Martini) · **file chiuso**

Coppie EN→IT rilette in `translation.json` (`3ff793b7a7ed6422…`). Tutte le 42 unità sono **`PENDING`**.

## 1. Voce e registro

- **Descrizioni di pianeta**: impersonali e concrete, con l'usura del tempo che si vede nel testo («i resti
  frantumati del vecchio Arsenale giacciono ancora abbandonati e si arrugginiscono lentamente…»).
- **Il memoriale**: solenne, senza retorica aggiunta («Le nove pareti completate sono già piene su entrambi i
  lati; sembra improbabile che le altre quattordici resistano fino alla fine della guerra.»).
- **Il gergo di Bloodsea**: comico e violento, reso senza addolcire («Ehi, ti taglierò le dita una per una finché
  non compri una polpetta!»).
- **Poisonwood**: la taverna come racconto per immagini, con la frase che chiude il cerchio («È una sensazione
  strana vedersi tra gli eroi di una storia su cui hai avuto solo un effetto minimo.»).
- Un solo registro: «tu». Nessuna cortesia «lei» (verificato).

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `Free Worlds War Memorial` | **il Memoriale di Guerra dei Mondi Liberi** | 2, 7, 34 |
| `names of the fallen` | **nomi dei caduti** | 2, 7, 34 |
| `dust masks` · `particulate matter` | **maschere antipolvere** · **particolato** | 4, 27 |
| `prison colony` | **colonia penale** | 8 |
| `The Parting Glass` | invariato | 11, 13 |
| `hodgepodge` | **guazzabuglio** | 10, 12 |
| `rhodophyte algae` | **alghe rodofite** | 14, 16, 20 |
| `saw the writing on the wall` | **hanno capito come stavano le cose** | 15 |
| `meat patty` | **polpetta** | 19 |
| `protection rackets` | **organizzazioni che vendevano protezione** | 23 |
| `weapons-grade uranium and plutonium` | **uranio e plutonio a livello militare** | 24, 25 |
| `"Checkmate" plan` | **piano "Checkmate"** | 32 |
| `electric carts` · `food court` | **carrelli elettrici** · **area ristorazione** | 37, 38 |
| `deflector shields` | **scudi deflettori** | 42 |
| `'will-do' attitude` | **atteggiamento di 'si può fare'** | 40 |
| `old capital city` | **vecchia capitale** | 39 |

## 3. Nodi aperti (da non dedurre dopo)

1. **Zero token è un'asserzione**: il controllo è `== {}` su entrambi i lati. Un token che comparisse in un lotto
   futuro di questo file deve farlo fallire.
2. **`The Parting Glass` resta inglese**: un nome proprio con « The » dentro. La scansione dei residui inglesi lo
   neutralizza **prima** di cercare parole inglesi; allentare il controllo sarebbe stato un errore.
3. **Cinque unità condividono il testo con L120/L121**: la resa è confrontata con quei `translation.json`. Se un
   lotto futuro li modificasse, il confronto diventa rosso e segnala l'incoerenza.
4. **I tre stadi del memoriale** (9 pareti → anello esterno da 50 → due anelli attorno a 23 e 50) sono
   **progressivi e coerenti fra loro**: non sono varianti da uniformare.
5. **`Bordo Meridionale`** compare anche qui (unità 28), a conferma della scelta di L121.
6. **`Martini` è descritta tre volte nella campagna** (L120, L121 per la ricostruzione, L122): i testi sono
   **diversi** e tali restano.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 42 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: nessuno degli eventi è stato visto.
- **Nessuna revisione umana**.
- **`campaign events.txt` è completo in staging, non nel gioco**: 150/150 tradotte, zero caricate.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (32 controlli), `verify.py` exit **0** (30 controlli), 150/150 righe coperte |
