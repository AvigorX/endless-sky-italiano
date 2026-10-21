# REVIEW — L169 · `paradise world jobs.txt` (turisti, crociera, passeggeri)

Coppie EN→IT rilette in `translation.json` (`150e46846747c2d3…`). Tutte le 17 unità sono **`PENDING`**.

## 1. Voce

Due registri: la **satira del turismo di lusso** (le brochure patinate contro la realtà, l'esotismo che delude) e il
**cinismo amministrativo** (i recidivi «non violenti», i debitori mandati a «rendersi utili», i pensionati che rovesciano
drink ma pagano bene). Il narratore non condanna nessuno: descrive.

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `They'll only consider thinking about your ship` | **Considereranno la tua nave solo se...** | 1, 3 |
| `memories ... give way to reality` | **i ricordi ... lasciano il posto alla realtà** | 2, 4 |
| `oohing and aahing` | **esclamare estasiate** | 6 |
| `under the watchful eye of a local security force` | **sotto lo sguardo vigile di una forza di sicurezza locale** | 11 |
| `a grinning job service provider` | **un sorridente fornitore di servizi per il lavoro** | 14 |
| `morally questionable anecdotes` | **aneddoti ... moralmente discutibili** | 17 |

## 3. Nodi aperti (da non dedurre dopo)

1. **Gli apici non si contano fra le lingue**: `They'll` sparisce in italiano, quindi 3 apici inglesi → 2 italiani. La
   cosa giusta da verificare è che **la frase fra apici resti fra apici**.
2. **`<npc>` non è un nome proprio**: si lascia intatto e non si adatta con articoli («il <npc>», non «la <npc>»: il
   genere lo decide il motore).
3. **Le missioni `tourists` e `tourist group`** hanno lo stesso testo: se una delle due cambia, il controllo sulle coppie
   fallisce — ed è voluto.
4. **Il confine di riga 526 è un `VALUE`**: chi apre L170 parte dal `VALUE` di `Pirate Retirees (Illegal)`.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 17 unità `PENDING`.
- **Nessuna missione vista a schermo**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Terzo lotto di `paradise world jobs.txt`**.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (26 controlli), `verify.py` exit **0** (22 controlli) |
