# REVIEW — L101 · `hai culture conversations.txt` (chiude il file)

Coppie EN→IT rilette in `translation.json` (`b32aaa185052d185…`).

## 1. Voce e registro

- **Il film** (1–5): il narratore racconta al «voi» e non interpreta; le due varianti differiscono solo per
  quanto si capisce, non per il tono.
- **La cameriera** (14, 18, 26): prima imbarazzata e formale («Mi dispiace tanto», «si sieda pure»), poi
  professionale («Lei è fortunato»), poi silenziosa. Dà del **«lei»**.
- **Il vicino di sgabello** (19, 23, 25): parte risentito e generico («voi umani»), si addolcisce con le scuse,
  finisce in memoria personale («i pani con cui sono cresciuto»). Il passaggio dal «voi» al racconto in prima
  persona è nel testo e la resa lo conserva.
- **Il traduttore** (13) parla in modo impersonale e ubbidiente: «cinguetta ubbidiente», con l'alternativa fra
  quadre che è il suo modo di rendere un vocabolo ambiguo.

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità | nota |
|---|---|---|---|
| `poster for a movie in Hai` | **locandina di un film in Hai** | 1 | |
| `"The Final Rest,"` | **"L'ultimo riposo"** | 1 | gioco di parole su *Darkrest* |
| `subtitled in your language` | **sottotitolato nella vostra lingua** | 1 | |
| `(Pass.)` | **(Passo.)** | 3 | |
| `an unseen monster inhabiting the station` | **un mostro invisibile che abita la stazione** | 4, 5 | |
| `drives those it meets insane` | **fa lentamente impazzire chi incontra** | 4, 5 | |
| `cryptic references to Hai literature and philosophy` | **riferimenti criptici alla letteratura e alla filosofia Hai** | 5 | |
| `dockhands` | **addetti** | 6 | |
| `"authentic Hai cuisine,"` | **"autentica cucina Hai"** | 6 | |
| `street food vendor` | **venditore ambulante** | 6 | |
| `steamed vegetables` | **verdure al vapore** | 10 | |
| `garbage receptacle` | **contenitore della spazzatura** | 10 | |
| `jingles a short melody` | **fa un breve motivetto** | 11 | |
| `an organism with a tail` | **un organismo con la coda** | 15 | |
| `acorn bread` | **pane di ghiande** | 18, 19, 25, 26 | coerente con L100 |
| `Traditional Hai breadmaking has become a lost art.` | **La panificazione tradizionale Hai è diventata un'arte perduta.** | 19 | |
| `hayipp` · `yur ki` | **hayipp** · **yur ki** | 25 | nomi di cibi, invariati |
| `'corn'` · `'sheep'` | **'granturco'** · **'pecora'** | 25 | apici come nel sorgente |
| `from high traffic areas` | **dalle zone ad alto passaggio** | 25 | |

## 3. Nodi aperti (da non dedurre dopo)

1. **`[a sedere, a riposare]`** (unità 13) è la voce del dispositivo: le quadre sono il segnale che traduce un
   vocabolo ambiguo con due alternative. Toglierle — come aveva fatto la mia prima stesura — spegne quel
   segnale.
2. **`hostess` = cameriera** in tutto il lotto: la stessa persona accoglie, prende l'ordine e serve. Un revisore
   che distinguesse «hostess» e «cameriera» introdurrebbe due personaggi dove ce n'è uno.
3. **`pane di ghiande`** è ora la resa fissa del file; il titolo del contesto resta `Sick of Acorn Bread`.
4. **Il finale è in silenzio** («Finite i vostri pasti in silenzio e ve ne andate»): non aggiungere commenti del
   narratore, che il testo non ha.
5. **`L'ultimo riposo`** è un calco voluto: se un revisore cercasse un titolo «più naturale» perderebbe il
   legame con *Darkrest*.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 26 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: nessuna di queste scene è stata vista a schermo.
- **Nessuna revisione umana**.
- **La campagna non è finita**: 127 file con unità residue, 7.214 unità / 164.678 parole.

## 5. Rischi residui

- **Chiusura del file**: l'invariante 147/147 dipende dai quattro `translation.json`; riscrivere un lotto
  precedente renderebbe rosso il `verify.py` di L101 — ed è corretto, perché il file non sarebbe più quello
  verificato.
- **Il tipo `LOGBOOK` non è ancora stato affrontato** in questo file: arriva con L102 (`quarg missions.txt`), dove
  il diario di bordo ha testo più lungo e va trattato come prosa, non come etichetta.

## 6. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (26 controlli), `verify.py` exit **0** (29 controlli), file **147/147** |
