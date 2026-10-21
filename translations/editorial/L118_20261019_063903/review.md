# REVIEW — L118 · `pirate jobs.txt` (schiavi, scorte, eliminazioni, razzie)

Coppie EN→IT rilette in `translation.json` (`31bb9438bee96230…`). Tutte le 104 unità sono **`PENDING`**.

## 1. Voce e registro

- **Descrizioni dei lavori**: impersonali, con il committente che parla («Una flotta del Sindacato vicino al
  sistema `<system>` ha fermato le nostre razzie. Distruggila e torna su `<planet>` entro `<day>` per un compenso
  di `<payment>`.»).
- **Dialoghi di incasso**: «tu», passato prossimo, tono dei pirati («I pirati di `<planet>` ti pagano con
  gratitudine `<payment>` per aver eliminato la flotta della Marina.»).
- **Trasporto di schiavi**: registro fattuale, senza compiacimento («La schiavitù è punita con la morte in tutta
  la galassia, quindi potrebbe essere un lavoro pericoloso da accettare.»).
- Nessun «voi» (verificato nei due script).

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità | nota |
|---|---|---|---|
| `Transfer slaves to <planet>` | **identico** | 9, 11, 13, 15, 17 | nome di missione |
| `a local warlord` | **un signore della guerra locale** | 10–18 | |
| `secure cells` | **celle sicure** | 10–18 | |
| `punishable by death throughout the galaxy` | **punita con la morte in tutta la galassia** | 10–18 | |
| `Protection to <planet>` · `Protect cargo` · `Protect ship` | **identici** | 19–36 | nomi di missione |
| `The captain of the <npc> will pay you <payment>` | **Il capitano della `<npc>` ti pagherà `<payment>`** | 20–36 | |
| `escape local law enforcement` | **sfuggire alle forze dell'ordine locali** | 20, 26, 32 | |
| `law-enforced space` | **spazio controllato dalle forze dell'ordine** | 22, 28, 34 | |
| `by <date>` · `by <day>` | **entro `<date>`** · **entro `<day>`** | molte | senza articolo |
| `Navy` · `Syndicate` · `militia` | **Marina** · **Sindacato** · **milizia** | 37–60 | |
| `Marauders` | **predoni** (nei testi) | 85–96 | nei nomi resta inglese |
| `rival gang` | **banda rivale** | 61–84 | |
| `a large rival gang is gaining too much power` | **una grande banda rivale sta diventando troppo potente** | 66, 74, 82 | |
| `the ruling Marauder gang` | **la banda di predoni che lo governa** | 94 | |
| `bounty payment` | **compenso** | 39–96 | |
| `gratefully pay you <payment>` | **ti pagano con gratitudine `<payment>`** | 40–96 | 8 occorrenze |
| `cut of the loot` | **una parte del bottino** | 98–104 | |
| `in Republic space` · `in Syndicate space` | **in spazio della Repubblica** · **in spazio del Sindacato** | 98, 102 | |
| `After counting up the loot … you are given your cut.` | **Dopo aver contato il bottino … ti viene data la tua parte.** | 100, 104 | |

## 3. Nodi aperti (da non dedurre dopo)

1. **Zero virgolette in tutto il segmento**: il controllo è un'asserzione vuota (`0 = 0`). Un cambio di inventario
   che introducesse una citazione deve far fallire il lotto, non passare in silenzio.
2. **I nomi contengono token** (`Merchants near <system>`, `Competition near <system>`): restano identici e il
   token è protetto dal nome stesso.
3. **Tre testi sono ripresi da L117** e la resa è la **stessa** su 8 unità: il `check.py` e il `verify.py` la
   confrontano con il `translation.json` di L117. Se in futuro un lotto cambia uno di quei testi, il confronto
   diventa rosso e segnala l'incoerenza.
4. **`entro <date>` e `entro <day>`**: niente articolo davanti al token, che porta già il numero o la data.
5. **Il numero «181 dopo» era sbagliato**: è il residuo dopo la riga **1624**, non dopo la 2955 (che è **77**).
   L'errore era in prosa e il checker dell'handoff non lo vedeva; l'ha visto il `verify.py`, e la correzione è
   stata fatta **nei documenti**.
6. **Prossimo lotto = coda del file**: 77 unità, con **12 `CONVERSATION`** (tipo mai visto in questo file),
   **9 tab** iniziali e **6 virgolette**. Il `check.py` cambia ancora una volta forma, e il `verify.py` deve
   passare a invariante **di file**.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 104 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: nessuna missione è stata vista; i token non sono stati osservati sostituiti.
- **Nessuna revisione umana**.
- **Il file non è completo**: 77 unità residue (righe 2958–3706).

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 4 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (28 controlli), `verify.py` exit **0** (38 controlli) |
