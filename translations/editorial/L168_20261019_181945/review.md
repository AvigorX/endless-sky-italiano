# REVIEW — L168 · `paradise world jobs.txt` (beneficenza, aste, braccianti, rifiuti)

Coppie EN→IT rilette in `translation.json` (`f7f0a3fc5708fb85…`). Tutte le 24 unità sono **`PENDING`**.

## 1. Voce

Il lotto ha **tre registri**: la **satira della beneficenza** (i cittadini illustri che donano ai «poveri» e gli
scaricatori che ne escono vestiti meglio), l'**ironia sull'eredità** (casse su casse di oggetti inutili) e il
**cinismo sui braccianti** (giovani vestiti male che non sembrano felici di partire). La resa tiene il distacco del
narratore: non commenta, fa vedere.

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `under-dressed and fashion-deprived` | **malvestite e prive di stile** | 2 |
| `the quality of the clothes, jewelry, and personal electronics` | **abiti, gioielli ed elettronica personale** | 9 |
| `novelty castles are being constructed` | **si stanno costruendo castelli decorativi** | 14 |
| `individual portions of ... estate` | **singole porzioni del patrimonio** | 16 |
| `shuffle wearily up the ramp` | **si trascinano stanchi su per la rampa** | 20 |
| `the scruffy foreman` | **il caposquadra sciatto** | 21 |

## 3. Nodi aperti (da non dedurre dopo)

1. **`<planet stopovers>` è un segnaposto unico**: idx 10 e 18. Chi apre L169 troverà `<npc>`, altro simbolo da non
   spezzare.
2. **Le `DESCRIPTION` 2/5/8 sono quasi identiche**: la differenza è una sola frase, e il controllo la isola.
3. **`Paradise Worlds` → «Mondi del Paradiso»** (idx 19), con la maiuscola: è un nome di regione, non un sostantivo.
4. **Il confine di riga 376 è un `DESCRIPTION`**: chi apre L169 parte da una descrizione, non da un `VALUE`.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 24 unità `PENDING`.
- **Nessun lavoro visto a schermo**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Secondo lotto di `paradise world jobs.txt`**.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (24 controlli), `verify.py` exit **0** (21 controlli) |
