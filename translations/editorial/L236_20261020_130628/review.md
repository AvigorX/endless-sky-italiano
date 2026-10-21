# review.md — L236 (`data/avgi/avgi news.txt`, righe 301–344)

Registro delle decisioni editoriali del **quarto lotto** di `avgi news.txt`: ventitré studenti Avgi, sei discipline, una
battuta ripetuta e due etichette che stanno in fondo alla frase.

## 1. Le etichette

| inglese | resa | nota |
|---|---|---|
| `Happiness.` (×6) | **Felicità.** (×6) | sei unità, sei discipline: la formula è identica, cambia solo la parola finale |
| `Enthusiasm.` | **Entusiasmo.** | |
| `Gratitude.` | **Gratitudine.** | |
| `Joy.` | **Gioia.** | |
| `Annoyance.` (×2 + ×2 ripetute) | **Fastidio.** | distinta da `Frustration` e da `Anger` |
| `Frustration.` | **Frustrazione.** | |
| `Depression.` | **Abbattimento.** | «depressione» in italiano è clinica: qui è lo scoraggiamento dello studente |
| `Anger.` (×2) | **Rabbia.** | ripresa da L233 |
| `Worry.` (×2) | **Preoccupazione.** | ripresa da L233 |
| `amusement.` (in coda) | **divertimento.** | minuscola, dopo la virgola |
| `dejection.` (in coda) | **scoramento.** | minuscola; `Dejection` in testa è «Scoramento», qui è la stessa parola in coda |

**Quattro unità non hanno etichetta** (10, 11, 20, 21): due sono domande («Hai visto i miei compiti, domanda?»), due sono
la stessa battuta con l'etichetta **in coda**. Il `check.py` confronta la lista completa con i `None` in quelle
posizioni: un controllo che pretendesse ventitré etichette sarebbe rosso su un lotto corretto.

## 2. Il lessico universitario

| inglese | resa | nota |
|---|---|---|
| `mastery in physics` (e le altre cinque) | **laurea magistrale in fisica** | «mastery» non ha precedenti nello staging; «laurea» 8, «specializzazione» 3: la forma piena è la più chiara e la ripetizione è voluta (è la stessa formula sei volte) |
| `xenology mastery` | **laurea magistrale in xenologia** | «xenologia» già nel corpus (2) |
| `go into academia` | **entrare nell'accademia** | «accademia» 13 occorrenze |
| `Midterms` | **esami intermedi** | `midterms` non ha precedenti; «esami di metà corso» sarebbe un calco più lungo |
| `the university made me go into engineering` | **l'università mi ha fatto passare a ingegneria** | niente participio concordato: il genere dello studente non è nel testo (decisione 133) |
| `I was ridiculed and accused` | **mi hanno deriso e accusato** | idem: terza persona plurale invece di un participio sul soggetto |
| `work in the shipyards` | **lavorare nei cantieri** | «cantiere» 133 occorrenze |
| `political science` | **scienze politiche** | |
| `a dead weight on society` | **un peso morto per la società** | |
| `Fools, the lot of them!` | **Sciocchi, tutti quanti!** | |

**Il genere non si inventa**: tre frasi (336, 337, 340) sarebbero state naturali con un participio («costretto»,
«deriso», «andato bene»), ma il testo non dice se lo studente è maschio o femmina. La resa evita l'accordo — «mi ha
fatto passare», «mi hanno deriso», «di aver fatto bene» — come già fatto per Gavriil (L42) e per Ijaset (L71).

## 3. I nomi e la Guerra

| inglese | resa | nota |
|---|---|---|
| `Aviskir`, `Livloua` | invariati (2 + 2) | toponimi (`Livloua` già nel corpus, L14) |
| `the Assembly` | **l'Assemblea** | |
| `the War` (maiuscolo) | **la Guerra** | istituzione del conflitto in corso, non «la guerra» generica |
| `the Aberrant` | **un Aberrant** | un solo nome per la fazione (decisione 25) |
| `Aberrant`, `Tangled Shroud`… | invariati | |

## 4. Le virgolette semplici e i tre punti

- L'unità 335 porta `'pratiche'` e l'unità 338 `'utile'`: sono **citazioni dentro la citazione** e si riproducono con
  l'apostrofo dritto, come l'inglese `'practical'` e `'useful'`.
- L'unità 335 finisce con `...` (tre punti, non l'ellissi tipografica): riprodotta, e il `check.py` vieta `…`.
- Il punto finale sta **dentro** la virgoletta doppia in tutte e 23 le unità.

## 5. Apici: 18 inglesi, 14 italiani

| unità | EN | causa | IT | causa |
|---|---|---|---|---|
| 1–6 | 6 | `I'm` (×6) | 0 | — |
| 7 | 1 | `can't` | 2 | `l'ora`, `l'accademia` |
| 8 | 0 | — | 1 | `L'arrivo` |
| 12, 13, 22, 23 | 4 | `isn't` | 4 | `dell'istruzione` |
| 14 | 2 | `'practical'` | 3 | `'pratiche'` (2) + `l'Assemblea` (1) |
| 15 | 0 | — | 1 | `l'università` |
| 17 | 3 | `isn't` + `'useful'` | 2 | `'utile'` |
| 18 | 1 | `I'm` | 0 | — |
| 19 | 1 | `don't` | 1 | `all'ultimo` |

Il controllo elenca le coppie `(unità, conteggio)`: il totale (18 contro 14) da solo non distinguerebbe questa
distribuzione da uno scambio.

## 6. Un refuso del sorgente

`Frustation.` (unità 370 e 371) invece di `Frustration.`: è un refuso inglese, **non si replica** in italiano —
«Frustrazione» è scritto correttamente — e non si corregge nel gioco (il repository resta intatto). Il `check.py`
registra l'etichetta inglese **come sta nel sorgente** (`Frustation`), così un cambio futuro del testo diventa rosso.

## 7. Struttura e lacune

- **Zero tab**, **zero segnaposto**: due asserzioni negative scritte.
- **Nessuna riga `log`**, nessun riferimento di dato: `NT` vuoto per misura.
- **Tre coppie di inglese identico** dentro la finestra (10/20, 12/22, 13/23): la resa è identica **per necessità**, e il
  controllo la confronta invece di dedurla.
