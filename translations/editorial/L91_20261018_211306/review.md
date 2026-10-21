# REVIEW — L91 · `data/successors/successor culture conversations.txt` (secondo segmento)

Le coppie EN→IT citate sono state rilette in `translation.json` (`9a8dcdeaee3a69af…`), non ricostruite.

## 1. Coerenza con i lotti precedenti

- **«spazioporto»**, **«piazzola di atterraggio»**, **«scafo»**: forme già usate in L86–L90.
- **`<ship>`** invariato; il nome della nave è del giocatore e non si traduce.
- **`Successori`** con la maiuscola (nome di specie), **`Successore`** al singolare.
- **Il giocatore è «voi»** in tutta la narrazione («Avvicinandovi», «trovate», «siete scesi»): coerente con
  L90. Nei dialoghi i Successori danno del **«tu»** al giocatore, e il giocatore lo ricambia («Puoi mostrarmi»),
  come prescrive il glossario per `thou`/`you`.
- **`port authority`** → «autorità portuale» (unità 15, 24): non «capitaneria», che è un istituto italiano.

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità | nota |
|---|---|---|---|
| `clattering` | `tintinnio` | 1, 4 | rumore metallico leggero, non «fracasso» |
| `globs` | `grumi` | 4 | consistenza densa |
| `foul-smelling` / `pungent` / `noxious` | `maleodorante` / `acre` / `acre` | 4, 26, 27 | tre inglesi vicini, resi con due parole: l'italiano non ha tre gradazioni equivalenti |
| `dull purple` | `viola spento` | 7, 11, 19 | colore base dei Successori imbarazzati |
| `pipes up` | `interviene` | 16 | con l'avverbio «allegramente» che rende `cheerfully` |
| `rosa divertita` | `mirthful shade of pink` | 19 | vedi `REPORT.md` §2 |
| `lattine` | `cans` | 19, 25 | contenitori del prodotto, non «bidoni» |
| `bel tentativo` | `Nice try` | 21 | ironia secca, senza «bella prova» |
| `Myiara l'Immortale` | `Deathless Myiara` | 28, 30 | titolo tradotto, nome proprio invariato |

## 3. Nodi aperti (da non dedurre dopo)

1. **Due scritte murarie**: «Ryiaa è stata qui! Con gli amici.» (26) e «'Erjn'... Stupido! Niente aculei,
   niente cervello!» (27). Il nome `'Erjn'` resta invariato ed è virgolettato come nel sorgente; `quills` è
   reso «aculei» come lessico del verso infantile — **nessuna unità del lotto descrive la specie come dotata
   di aculei**, quindi la scelta è stilistica e non un dato del testo. Se un lotto successivo mostrasse una
   resa diversa di `quills`, va allineata a questa.
2. **`hull solution`** è un prodotto: la resa «soluzione per lo scafo» è usata in tutte le occorrenze del lotto,
   comprese le due dentro le virgolette (19, 27). Non è un equipaggiamento e non va in inglese.
3. **`myiara system`** (idx 29) resta identica: è il riferimento che il gioco usa per il nome del sistema.
4. **`Stage Play`** è il contesto, non un titolo da tradurre: lo spettacolo nel testo è «Myiara l'Immortale».

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 34 unità del segmento restano `PENDING`.
- **Nessun caricamento nel gioco**: nessuna di queste scene è stata vista a schermo.
- **Nessuna revisione umana**: il lotto non è approvato.
- **Il file non è chiuso**: restano 46 unità (righe 230–351) a L92.

## 5. Rischi residui

- **60 virgolette**: il totale è pari, ma le unità 19 e 27 contengono due citazioni ciascuna (una battuta e un
  termine fra virgolette). Una resa che spostasse la virgoletta di apertura del termine produrrebbe testo
  leggibile e un controllo per unità rosso: è il motivo per cui il controllo è per unità.
- **Unità cortissime** (2, 3, 18, 32, 33): il rapporto resta sopra 0,92, ma sono le unità che in questa
  campagna sfondano più spesso la banda minima; qui non è successo.
- **`rosa divertita`** è una scelta stilistica non ovvia: se il revisore la rifiuta, la sostituzione riguarda
  una sola unità (19).

## 6. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (28 controlli), `verify.py` exit **0** (28 controlli), sha256 `9a8dcdeaee3a69af` |
