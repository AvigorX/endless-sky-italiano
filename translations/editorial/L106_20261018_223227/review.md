# REVIEW — L106 · `korath missions.txt` (primo lotto)

Coppie EN→IT rilette in `translation.json` (`10952e0d80f509b5…`).

## 1. Voce e registro

- **I Korath** non parlano: la loro frase (`"Humani efreti, naskoor amasavarkta."`) resta in lingua originale,
  perché il narratore dice esplicitamente che **nessuno capisce** la vostra lingua. Tradurla toglierebbe il senso
  della scena.
- **Il Wanderer** (8–25) è cortese e formale: dà del **«Lei»** («Le interesserebbe portare…», «Posso offrirle…»)
  e si scalda solo nel finale («Meraviglioso!»). La sua voce è lessicalmente prudente, e il dispositivo la rende
  con le doppie alternative.
- **Il giocatore** ha battute brevi e colloquiali («L'unico e solo», «Posso farlo. Caricate, e sarò pronto»).
- **Il narratore** resta al «voi» e osserva: il Wanderer che «si sgonfia un po'» quando rifiutate, il gruppo che
  «si separa» e va a caricare.

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità | nota |
|---|---|---|---|
| `holding up both hands with their palms toward you` | **sollevando entrambe le mani con i palmi verso di voi** | 1–4 | saluto Korath, coerente con L102 |
| `Humani efreti` | **invariato** | 1–4 | è il nome che i Korath danno agli umani «amici» |
| `Kor Efreti` · `Kor Mereti` · `Kor Sestor` | **invariati** | 5 | fazioni |
| `almost entirely in ruins` | **quasi interamente in rovina** | 5 | |
| `the shelter of a Quarg ringworld` | **al riparo di un mondo ad anello dei Quarg** | 5 | |
| `living as exiles near the galactic core` | **che vivono in esilio vicino al nucleo galattico** | 5 | |
| `unending struggle` | **lotta senza fine** | 5 | |
| `The one and only.` | **L'unico e solo.** | 10 | |
| `unusually low payment` | **pagamento insolitamente basso** | 13 | |
| `an accelerated [descent, transition] into an ice age` | **una [discesa, transizione] accelerata verso un'era glaciale** | 16 | |
| `no effective means of stopping this` | **nessun mezzo efficace per fermarla** | 16 | |
| `unless they have no other options` | **finché non avranno altre opzioni** | 16 | |
| `offset this [descent, transition]` | **compensino questa [discesa, transizione]** | 16 | |
| `terraforming assistance` | **aiuto nella terraformazione** | 16 | |
| `at the moment` | **al momento** | 15, 19 | |
| `it had hoped you wouldn't ask that` | **quasi avesse sperato che non lo chiedeste** | 20 | |
| `it seemed they could not afford to pay much more` | **sembra che non potessero permettersi di pagare molto più** | 20 | |
| `the cargo is a [collection, menagerie] of equipment` | **il carico è una [collezione, accozzaglia] di attrezzature** | 20 | |
| `it wanders off to look for another pilot` | **si allontana in cerca di un altro pilota** | 24 | |
| `starts barking orders` | **comincia a impartire ordini** | 25 | |

## 3. Nodi aperti (da non dedurre dopo)

1. **Le quadre contengono sempre due alternative** e vanno tradotte entrambe: `[provviste, aiuti]`, non
   «provviste». Il `check.py` verifica ogni coppia (virgola o punto interrogativo) perché una coppia con una
   parola sola passerebbe il conteggio totale e sarebbe un errore a schermo.
2. **`[perish? expire?]`** ha i **punti interrogativi dentro** le quadre: non sono refusi, sono il modo in cui il
   dispositivo segnala che nemmeno lui è sicuro.
3. **`Supplies to <planet>`** resta identico: è il nome della missione sul tabellone. Il token **dentro** il
   `VALUE` è una delle quattro occorrenze di `<planet>` del lotto.
4. **`Humani efreti, naskoor amasavarkta`** non si traduce: è la lingua dei Korath, e il testo dice che nessuno la
   capisce. La frase resta fra virgolette come nel sorgente.
5. **L'unità 1 dice «stazione», le 2/3/4 «spazioporto»**: non è una svista del sorgente, è il primo contatto su
   una stazione. La resa lo conserva, e il `check.py` verifica che **non** siano identiche.
6. **Il Wanderer dà del «Lei»**, il narratore dà del «voi» al giocatore: due livelli, tenuti separati.
7. **`Kor Efreti` è la fazione pacifica** e va distinta dai **Korath** in generale e dagli esuli predoni: il
   `LOGBOOK` li elenca, e la traduzione non li confonde.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 25 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: nessuna di queste scene è stata vista a schermo.
- **Nessuna revisione umana**.
- **Il file non è completo**: 133 unità residue su 13 contesti.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (31 controlli), `verify.py` exit **0** (29 controlli) |
