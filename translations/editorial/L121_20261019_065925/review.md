# REVIEW — L121 · `campaign events.txt` (schieramento, empori, Zug, Greenrock)

Coppie EN→IT rilette in `translation.json` (`292f0d3b327b16f9…`). Tutte le 56 unità sono **`PENDING`**.

## 1. Voce e registro

- **Descrizioni di pianeta**: impersonali, al presente, con il dettaglio tecnico che caratterizza questo file
  («I gusci degli edifici hanno più strati, progettati per autoripararsi in caso di impatto…»).
- **Dialogo dell'emporio**: cordiale e commerciale, che scivola nel cinico («Ma sai, è sbagliato rifornirsi da chi
  ha fatto quegli attentati…»).
- **Descrizioni di stazione**: ironiche, con la voce del giocatore («In pratica, sospetti che una buona dose di
  pirateria continui comunque qui.»).
- Un solo registro: «tu». Nessuna cortesia «lei» (verificato).

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `new stock` | **new stock** | 20 — `UI_LABEL` identica |
| `Southern Rim` | **Bordo Meridionale** | 11, 18–21 |
| `(Move on.)` · `(Ask the proprietor…)` | **(Vai avanti.)** · **(Chiedi al proprietario…)** | 12–17 |
| `Kraz Cybernetics` · `Delta V` · `Syndicated Systems` | invariati | 11–23 |
| `Lovelace Sidewinders` | **Lovelace Sidewinder** | 21 |
| `Old Port / The Port / New Port / The Expansion` | **Vecchio Porto / Il Porto / Porto Nuovo / L'Ampliamento** | 26–29 |
| `chief ship foundry` | **principale fucina di navi** | 29 |
| `Poseidon Industries` | **la Poseidon Industries** | 31, 35 |
| `Navy Oathkeepers` | **gli Oathkeepers della Marina** | 37 |
| `Free Worlds Conservatory` | **il Conservatorio dei Mondi Liberi** | 39 |
| `terraforming` | **terraformazione** | 39 |
| `Smuggler's Den` · `Grendel Station` | **Smuggler's Den** · **la stazione Grendel** | 42 |
| `privateers` · `smugglers` | **corsari** · **contrabbandieri** | 42 |
| `Mike's Mustelids` | **«Mike's Mustelids»** | 48, 52, 56 |
| `weasels, ferrets, wolverines` | **donnole, furetti, ghiottoni** | 48, 52 |
| `slave markets` | **mercati di schiavi** | 45–55 |
| `militia` (a Greenrock) | **miliziani** | 47 |

## 3. Nodi aperti (da non dedurre dopo)

1. **`Bordo Meridionale` è una scelta nuova**: nessun lotto precedente traduceva `Southern Rim`. Se un lotto
   futuro usasse «Orlo Meridionale» o lasciasse l'inglese, la campagna avrebbe due nomi per la stessa regione.
2. **`new stock` resta inglese**: è una `UI_LABEL`, e il controllo la isola. Non è una dimenticanza.
3. **Le unità 22 e 24 hanno una sola virgoletta**: il sorgente lascia la battuta aperta (la chiude il nodo
   successivo). La resa riproduce, e il `check.py` verifica che siano **esattamente quelle due**.
4. **Le quattro coppie ripetute** non sono ridondanze del lotto: sono lo stesso testo in due contesti (Zug prima e
   dopo l'ampliamento, Greenrock occupata e abbandonata) o la stessa opzione ripetuta (`(Move on.)`).
5. **Il testo di Greenrock cambia tre volte** (occupata / abbandonata / recuperata) e le tre versioni sono
   **deliberatamente diverse**: non vanno uniformate.
6. **Il registro «tu» vale anche per i commercianti**: l'unità 22 usa «Ma sai…» e non «Ma sa…».

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 56 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: nessuno degli eventi è stato visto; il token `<origin>` non è stato osservato
  sostituito.
- **Nessuna revisione umana**.
- **Il file non è completo**: 42 unità residue (righe 1338–3468), **zero token**, 18 contesti.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (32 controlli), `verify.py` exit **0** (29 controlli) |
