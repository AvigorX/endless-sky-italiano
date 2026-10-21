# review.md — L257 (`data/human/post-war reactions.txt`, righe 76–151)

Registro delle decisioni editoriali del **secondo lotto**: la coda dei gemelli minatori e l'apertura delle **due capitane
sorelle**, una della Marina e una dei Free Worlds.

## 1. Le due metà

| metà | unità | contesto | contenuto |
|---|---|---|---|
| prima | 1–9 | `Asteroid Miners` | i gemelli reagiscono, fanno il saluto, tornano alle navi |
| seconda | 10–23 | `Navy and Free Worlds Captains` | in un bar, due capitane di mezza età si presentano |

La **10** è l'unica senza tab: è la descrizione d'ambiente che apre la nuova missione, e in italiano resta **senza rientro**
(«Ti stai rilassando in un bar mentre la tua nave fa rifornimento…»).

## 2. Scelte

| inglese | resa | perché |
|---|---|---|
| `Have you been under a rock the whole war?` | **«Sei vissuto sotto un sasso per tutta la guerra?»** | idioma reso, non letterale |
| `a disheveled hamster stuck to my upper lip` | **«un criceto arruffato incollato al labbro superiore»** | la battuta è sui baffi, e deve restare ridicola |
| `Pardon us if we keep our eyes open and trust to our own guns.` | **«Perdonaci se teniamo gli occhi aperti e ci affidiamo ai nostri cannoni.»** | `guns` → cannoni, come nei lotti navali |
| `their facial hair is halting any emotive power` | **«i loro peli del viso bloccano ogni capacità espressiva»** | |
| `a pair of middle-aged captains` | **«due capitani di mezza età»** | |
| `they bear a striking resemblance` | **«si somigliano in modo impressionante»** | prepara la rivelazione delle sorelle |
| `the war's most accomplished captain` | **«il capitano più valente della guerra»** | |
| `Joint police operation` | **«Un'operazione di polizia congiunta»** | |
| `galactic Spider Funk smuggling operation` | **«un'operazione di contrabbando di Spider Funk su scala galattica»** | nome della droga invariato |
| `Not addictive, but still dangerous.` | **«Non dà dipendenza, ma resta pericoloso.»** | |
| `That's rough, buddy` | riga **215**, fuori lotto | sarà L258 |

## 3. Genere e numero delle due capitane

`Captain Rain` e `Captain Fiona` sono **sorelle** (lo dice l'unità 17) e sono **due donne**:

- «dice l'**altra**» (unità 12), «**sono sicura**» (unità 21: `I'm sure`), «Ti abbiamo **visto** entrambi» — il participio
  resta al maschile perché l'oggetto è il giocatore, non le capitane;
- `One is Navy, the other is Free Worlds` → «Uno è della **Marina**, l'altro dei **Free Worlds**»: qui `uno/l'altro` è
  corretto, perché il soggetto è il **capitano** come ruolo, e il genere della persona non è ancora rivelato.

## 4. Il registro

Il giocatore parla alle due capitane con il **«tu»** plurale («Avete trovato nuovi alieni?», «Avete combattuto su fronti
opposti?»), e loro rispondono con lo stesso registro. `Thank you for your service` → **«Grazie per il tuo servizio»**: il
«Lei» non esiste in questa traduzione, e la formalità militare si rende con il tono, non con il pronome.

## 5. La citazione non chiusa

L'unità 12 finisce con `!` e **non chiude** la citazione aperta: tre virgolette in tutto. La resa italiana ha le stesse tre,
e il `check.py` e il `verify.py` lo asseriscono. È l'unico caso in cui «correggere» sarebbe un errore: il testo del gioco è
quello, e chiuderlo cambierebbe una stringa visibile.

## 6. Struttura

| cosa | inglese | italiano |
|---|---|---|
| tab | **22** (tutte tranne la 10) | **22**, stesse unità, primo carattere |
| virgolette | **45** | **45**, mappa per unità identica |
| apici | **17** su 12 unità | **5** su 4 unità (10, 12, 22, 23) |
| segnaposto | 5 | 5, **ordine identico** |

Gli apici italiani sono un terzo degli inglesi: `I'm`, `don't`, `We've`, `twins'`, `It's`, `How's`, `You're`, `war's`,
`should've` non hanno equivalente, e restano solo le elisioni (`l'altro`, `un'operazione`, `L'organizzazione`).

## 7. Cosa resta aperto (dichiarato)

- **Nessuna approvazione**: 23 unità `PENDING`.
- **Nessun testo visto nel gioco**.
- **Nessuna revisione umana**.
- **Il file è a 45/87**: L258 riparte dalla riga 152 e attraversa un altro cambio di missione (a `Syndicate Orphan`).
