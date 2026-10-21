# REVIEW — L117 · `pirate jobs.txt` (lavori: contrabbando, droga, ricercati)

Coppie EN→IT rilette in `translation.json` (`6ed8bb0de3875183…`). Tutte le 98 unità sono **`PENDING`**.

## 1. Voce e registro

- **Descrizioni dei lavori**: impersonali e asciutte, come il pannello dei lavori («Porta `<cargo>` di
  contrabbando su `<destination>` senza farti scansionare o cogliere dalle forze dell'ordine planetarie. Il
  compenso è `<payment>`.»).
- **Dialoghi di consegna** (5): «tu», passato prossimo, ritmo rapido («Dopo l'atterraggio ti paga `<payment>`,
  poi raccoglie in fretta le sue cose e scende dalla nave.»).
- **Messaggi di fallimento**: descrittivi, con le forze dell'ordine come soggetto collettivo («Quando scansionano
  la tua nave, le forze dell'ordine notano il criminale che hai a bordo…»).
- Nessun «voi» (verificato nei due script).

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità | nota |
|---|---|---|---|
| `Smuggle <cargo> to <destination>` | **Porta `<cargo>` di contrabbando su `<destination>`** | 2, 5, 8, 11, 26… | 7 occorrenze |
| `Run <cargo> to <destination>` | **Porta `<cargo>` su `<destination>`** | 14, 17… | |
| `without being scanned or caught` | **senza farti scansionare o cogliere** | 2, 5 | |
| `Payment is <payment>` | **Il compenso è `<payment>`** | 31 unità | formula unica |
| `In addition to the fine` | **Oltre alla multa** | 26 occorrenze | |
| `your illegal cargo is confiscated` | **il tuo carico illegale viene confiscato** | 26 occorrenze | |
| `The pirates won't be happy to hear about this` | **I pirati non saranno felici di saperlo** | 26 occorrenze | |
| `fined 46,000 credits` | **multa di 46.000 crediti** | 17 | numero con il punto delle migliaia |
| `the consequences may be severe` | **le conseguenze possono essere gravi** | 44, 47… | 11 unità |
| `land away from the spaceport` | **atterrare lontano dallo spazioporto** | 59 | |
| `This wanted individual wishes…` | **Questo ricercato vuole…** | 80 | |
| `These <bunks> wanted individuals` | **Questi `<bunks>` ricercati** | 84, 88, 92 | |
| `law enforcement notice / notices` | **le forze dell'ordine notano** | 81, 85… | concordanza col plurale |
| `clutching their battle trophies and screaming "…"` | **che stringe i suoi trofei di battaglia e urla "non me li porterete mai via!"** | 81 | 2 virgolette |
| `scooping their credits into the airlock` | **a infilare i loro crediti nel portello d'ancoraggio** | 85 | |
| `firing down the hallways` · `tear gas` | **sparare nei corridoi** · **gas lacrimogeno** | 89 | |
| `passed out in their bunks rooms` | **svenuti nelle loro cuccette** | 93 | |
| `suited head to toe in armor` | **coperti di armatura dalla testa ai piedi** | 97 | |
| `no-questions-asked transporter` | **trasportatore affidabile che non fa domande** | 81, 85, 89, 93, 97 | |
| `nomi di missione` (`VALUE`) | **invariati** | 31 unità | decisione 259/L103 |

## 3. Nodi aperti (da non dedurre dopo)

1. **I 31 `VALUE` sono nomi di missione e restano in inglese**: sono elencati nel `check.py` e ricalcolati dal
   `verify.py`. Una resa italiana del nome rompe il riferimento e il controllo.
2. **26 testi per 98 unità**: la ripetizione è del sorgente e la resa **ripete**. Ogni gruppo di inglese identico
   ha **una sola** resa italiana, assegnata per firma; le rese si scrivono in `mkparts2.py`, non nei `parts/`.
3. **Il dialogo ha due numeri**: `Your <passengers> insists` (singolare) e `Your <passengers> insist` (plurale).
   Le firme `insists that` / `insist that` servono a non confonderli: con `insist` il costruttore trovava due
   corrispondenze e abortiva.
4. **108 token, sei famiglie**: `<payment>` 36 e `<cargo>` 31 convivono nella stessa descrizione; la parità è per
   simbolo e per unità, con lo stesso ordine.
5. **Una sola unità con virgolette** (81): l'urlo del criminale. Non è una citazione di etichetta: è discorso
   diretto, e va reso come tale.
6. **La seconda stesura (`mkparts2.py`)** sostituisce la prima: quella traduceva anche i nomi di missione. Il
   file `mkparts.py` resta come storia dell'errore, non va rieseguito.
7. **Il prossimo segmento cambia ancora forma**: 104 unità, **33 `VALUE`**, **36 `DIALOG`**, solo **2
   `MISSION_TEXT`**, **192 token in nove famiglie** (`<planet>` 53, `<payment>` 52, `<system>` 33, `<day>` 17,
   `<npc>` 9, `<date>` 9, `<bunks>` 5, `<cargo>` 2). I lavori diventano **razzie e missioni di sistema**, con
   `VALUE` tipo `Merchants near <system>`.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 98 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: nessuna missione è stata vista nel pannello; il testo dei token non è stato
  osservato nel gioco.
- **Nessuna revisione umana**.
- **Il file non è completo**: 181 unità residue (righe 1627–3706).

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 3 parti, `translation.json`, `mkparts2.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (29 controlli), `verify.py` exit **0** (38 controlli) |
