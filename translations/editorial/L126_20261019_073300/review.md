# REVIEW — L126 · `incipias first contact.txt` (il Guardiano, i Quarg, il relitto)

Coppie EN→IT rilette in `translation.json` (`c928bf1d8815cac5…`). Tutte le 55 unità sono **`PENDING`**.

## 1. Voce e registro

- **Il Guardiano** parla in modo **alto e arcaico**, con inversioni e immagini: «Qui giacciono i fiori non ancora
  nati, che devono ancora schiudersi del tutto», «Le vite degli altri sono come un quadro che non smette mai di
  essere dipinto, ma è cosa tragica vedere il quadro fermarsi».
- **I Quarg** parlano in modo **cerimoniale e leggermente stucchevole**: «I tuoi lunghi vagabondaggi ti hanno
  condotto fin qui», «non peregrinare per questo quarto di spazio con leggerezza», «A un intervallo minimo da questa
  luna la specie vicina ha iniziato il suo viaggio verso le stelle».
- **La narrazione** resta al presente e al «tu»: «Allarmato, ti guardi attorno ma non c'è nessuno».
- **Gli alieni del relitto** non parlano: comunicano con gradienti di colore, e la resa lo tiene fermo («Pulsano di
  colori vivaci», «i suoi colori passano a un verde debole»).

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `unborn flowers` | **fiori non nati** | 9, 10, 13, 15, 18, 22 |
| `dead end` | **vicolo cieco** | 1, 4, 7 |
| `traveler` | **viaggiatore** | 1, 6 |
| `Ignoring these words is only but folly` | **Ignorare queste parole è pura follia** | 6 |
| `the continuum` | **il continuum** | 13 |
| `I am the guardian of this space` | **sono il guardiano di questo spazio** | 20 |
| `Your lengthy wanderings have brought forth you here` | **I tuoi lunghi vagabondaggi ti hanno condotto fin qui** | 31 |
| `do not perambulate` | **non peregrinare** | 38 |
| `nomadic voyagings` | **vagabondaggi nomadi** | 41 |
| `a trifling interval` | **un intervallo minimo** | 41 |
| `hail request` | **richiesta di collegamento** | 45 |
| `color gradients` | **gradienti di colore** | 45, 46, 52 |
| `half octopod, half jellyfish` | **in parte polpi e in parte meduse** | 46 |
| `gunner` | **artigliere** | 46, 50 |
| `the crate` | **la cassa** | 51 |
| `hyperdrive` | **iperguida** | 44, 55 |

## 3. Nodi aperti (da non dedurre dopo)

1. **Le 4 `UI_LABEL`** sono testi di nodo e restano identici. Il lotto successivo (`Help The Stranded 1`) ha un
   `VALUE` e **2 token**: la forma cambia di nuovo.
2. **I due registri vanno tenuti separati** anche nei lotti successivi: il file è lo stesso, e il Guardiano ricompare
   nelle missioni «Help The Stranded».
3. **L'unità 23 ha 3 virgolette**: la terza è un refuso del sorgente riprodotto. Non è una svista della resa.
4. **Le due voci di diario** (18 e 22) si sovrappongono: la seconda ripete la prima e aggiunge «Accettato di starne
   lontano». La mappa `EXACT` del costruttore è dichiarata.
5. **`ut divitas` e `spec inci`** sembrano latino o pseudolatino: sono etichette di condizione, non testo da
   tradurre.
6. **Le tre scelte del relitto** (47–49) sono opzioni fra parentesi: restano fra parentesi, come nel sorgente.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 55 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: la missione del primo contatto non è stata vista, e i nomi dei Quarg non sono
  stati verificati a schermo.
- **Nessuna revisione umana**.
- **Il file non è completo**: 106 unità residue (righe 224–439).

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (31 controlli), `verify.py` exit **0** (28 controlli) |
