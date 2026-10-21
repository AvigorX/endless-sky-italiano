# REVIEW — L102 · `quarg missions.txt` (primo lotto)

Coppie EN→IT rilette in `translation.json` (`d1e12262951885ee…`).

## 1. Voce e registro

Due Quarg, due voci, e non è un caso:

- **Il Quarg dello spazioporto** (5–27): frasi brevi, solenne, quasi liturgico («Molte. La maggior parte giovani,
  molto più giovani dei Quarg. Molte sciocche. Poche sagge.»). Parla al **«tu»** e si riferisce a sé come
  **«questo uno»**. È la voce della scheda e dell'incontro: chiara, un po' lenta, straniante per scelta.
- **Il Quarg di Kuwaru Efreti** (29–48): inglese **arcaico** con sintassi invertita («Whither came you»,
  «wherefore visit you us», «lest awaken in you we», «bring you can we no succor»). In italiano: lessico elevato,
  ordine marcato ma **grammaticalmente corretto** — «Donde venite, e perché ci visitate», «nessun soccorso
  possiamo recarvi», «che non si risvegli in voi il desiderio». Parla al **«voi»**.
- **I due `LOGBOOK`** (1–2) sono la voce dell'enciclopedia di gioco: terza persona, presente, nessun commento.
- **Il giocatore** ha battute brevi e dirette (6, 8, 9, 11–13, 15, 17–18, 23–24, 26, 30–31, 33–34, 36, 39, 44–46).

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità | nota |
|---|---|---|---|
| `inscrutable` | **imperscrutabili** | 1 | |
| `artificially constructed ringworlds` | **mondi ad anello costruiti artificialmente** | 1 | |
| `claim to be in communication with` | **affermano di essere in comunicazione con** | 1 | il `claim` resta un'affermazione, non un fatto |
| `supposedly the oldest living species` | **sarebbero la specie vivente più antica** | 2 | condizionale: è una voce |
| `something like galactic peacekeepers` | **una sorta di pacificatori** | 2 | |
| `the architecture is truly alien` | **l'architettura è davvero aliena** | 3 | |
| `never quite seem to meet at right angles` | **non sembrano mai incontrarsi ad angolo retto** | 3 | |
| `squats down on its haunches` | **si accovaccia sui garretti** | 5 | |
| `like an accordion or the buzz of a beehive` | **come una fisarmonica o il ronzio di un alveare** | 5 | |
| `eyelids come from the sides of its eyes` | **le palpebre vengono dai lati degli occhi** | 10 | |
| `disconcerting` | **sconcertante** | 10, 4 | |
| `the Quarg are like no other` | **i Quarg non sono come nessun altro** | 14 | |
| `very subtle lungs` | **polmoni assai delicati** | 16 | |
| `do not kill for sport or whimsy` | **non uccidiamo per diletto o per capriccio** | 16 | |
| `the eldest living` | **i più anziani fra i viventi** | 21 | |
| `prune away the paths` | **potano via le vie** | 21 | |
| `obscene technologies of war` | **oscene tecnologie di guerra** | 22 | |
| `Awakened the atom?` | **Risvegliato l'atomo?** | 25 | |
| `Snuffing out stars` | **Spegnere stelle** | 25 | |
| `this one` | **questo uno** | 10 | terza persona di sé |
| `unquiet graveyard` | **inquieto cimitero** | 29 | |
| `astonishing sojourner` | **sorprendente viaggiatore** | 29 | |
| `the unwise Korath` | **gli stolti Korath** | 32 | |
| `thinking war machines` | **macchine da guerra pensanti** | 32, 34, 39 | |
| `Ware their ships` | **Guardatevi dalle loro navi** | 35, 40 | arcaico, non «attenzione a» |
| `Korath Efreti … 'Korath Friends'` | **Korath Efreti … 'Amici dei Korath'** | 43 | il testo si autoglossa |
| `It clicks its teeth together` | **Fa scattare i denti l'uno contro l'altro** | 48 | |

## 3. Nodi aperti (da non dedurre dopo)

1. **`questo uno`** è la resa di *this one*: il Quarg non dice «io». Chi revisiona non lo corregga in «me».
2. **Il registro arcaico di Kuwaru Efreti** non è un errore di italiano: l'ordine marcato riproduce l'inversione
   inglese. La grammatica resta corretta — se una frase suona sgrammaticata, è un difetto da correggere.
3. **`tu` per il primo Quarg, `voi` per il secondo**: scelta dichiarata, non svista. Il secondo parla in un
   inglese arcaico che in italiano si sostiene meglio con il «voi».
4. **`Korath` / `Korathi`**: singolare e collettivo. La traduzione li distingue come il sorgente.
5. **Due `LOGBOOK` ora esistono** nel progetto: la regola «il tipo assente si dichiara» vale al contrario per i
   tipi presenti, che vanno **elencati**.
6. **I nomi di specie restano invariati**: Quarg, Drak, Korath, Korathi, Hai.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 48 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: nessuna di queste scene è stata vista a schermo.
- **Nessuna revisione umana**.
- **Il file non è completo**: 130 unità residue su 6 contesti.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (29 controlli), `verify.py` exit **0** (27 controlli) |
