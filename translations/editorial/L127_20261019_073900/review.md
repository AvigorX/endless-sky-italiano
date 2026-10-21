# REVIEW — L127 · `incipias first contact.txt` (il traduttore dei Quarg, il primo contatto, la stazione)

Coppie EN→IT rilette in `translation.json` (`d811d1921f891627…`). Tutte le 63 unità sono **`PENDING`**.

## 1. Voce

- **Il Quarg singolo** usa la terza persona: «Felice è questo uno che tu accetti quella condizione», «Per quanto ne sa
  questo uno», «questo uno ti assisterà su quest'ultimo punto». Sette occorrenze di «questo uno».
- **I Quarg come collettivo** passano alla prima plurale: «Ti siamo grati per la comprensione», «ti forniremo un
  traduttore», «Nessuno li danneggerà senza incorrere nella nostra ira». La compresenza delle due forme è nel
  sorgente e resta nella resa.
- **Gli Incipias** parlano per composti: «Qual è la tua intenzione-scopo qui?», «Attracca alla stazione-capitale», «Ti
  permetteremo di comprarne una, se è tutto ciò che serve a renderti un non-pericolo».
- **La narrazione** resta al presente e al «tu»: «Appena arrivi sul pianeta cerchi un Quarg che parli la tua lingua».

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `Seek help from the Incipias` | **identico** (`VALUE`) | 1 |
| `this one` | **questo uno** | 10, 16, 17, 25, 26, 32 |
| `world-traveler` | **viaggiatore-di-mondi** | 43 |
| `intention-goal(s)` | **intenzione-scopo / intenzioni-scopo** | 43, 46 |
| `capital-station` | **stazione-capitale** | 46 |
| `outer-being` | **essere-esterno** | 50, 54 |
| `far-stranger` | **straniero-lontano** | 57 |
| `not-danger` | **non-pericolo** | 60 |
| `situation-opportunity` | **situazione-opportunità** | 60 |
| `air-planet` | **pianeta-d'aria** | 62 |
| `system-places` | **luoghi-sistema** | 62 |
| `future-time` | **futuro-tempo** | 62 |
| `tumultuous planets` | **pianeti turbolenti** | 17 |
| `interlopers` | **intrusi** | 12 |
| `dissemination` | **modo di diffondere i messaggi** | 10 |
| `airlock` | **portello** | 49 |

## 3. Nodi aperti (da non dedurre dopo)

1. **Il `VALUE` è uno solo** e sta in apertura (unità 1). Il lotto successivo, che chiude il file, ha una coda di
   **43 unità** in **tre contesti**: la forma dei `VALUE` va rimisurata, non copiata.
2. **I due token** sono in una sola unità: i token non sono un totale, sono una posizione.
3. **98 virgolette senza unità dispari**: in L126 l'unità 23 ne aveva tre. Qui la simmetria è del sorgente, non una
   regola da applicare in generale.
4. **«Vi saluto» è un voi plurale** (la folla degli Incipias), non cortesia: i controlli vietano `Lei/lei`, non `voi`.
5. **Lo stile alieno per composti** va tenuto nel lotto finale: gli Incipias ricompaiono in `Help The Stranded 2`.
6. **Il Quarg e i Quarg** convivono nello stesso lotto: la terza persona è del singolo, non della specie.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 63 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: la missione non è stata vista, il traduttore non è stato «usato» in partita.
- **Nessuna revisione umana**.
- **Il file non è completo**: restano 43 unità (righe 343–439).

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (30 controlli), `verify.py` exit **0** (28 controlli) |
