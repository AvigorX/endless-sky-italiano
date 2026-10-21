# review.md — L234 (`data/avgi/avgi news.txt`, righe 115–180)

Registro delle decisioni editoriali del **secondo lotto** di `avgi news.txt`. Il registro Avgi continua; la novità è
che per la prima volta **un'unità non ha etichetta**.

## 1. Le etichette: una lista con un buco

| inglese | resa | nota |
|---|---|---|
| `Dejection.` | **Scoramento.** | ripresa identica da L233 |
| `Relief.` | **Sollievo.** | idem |
| `Secrecy.` | **Segretezza.** | |
| `Defiance.` | **Sfida.** | «Ribellione» sarebbe un atto, `defiance` è l'atteggiamento |
| `Doubt.` | **Dubbio.** | |
| `Irony.` | **Ironia.** | |
| `Intrigue.` | **Interesse.** | in italiano «intrigo» è un complotto: qui è la curiosità del mercante |
| `Pride.` (×3) | **Orgoglio.** (×3) | tre unità diverse, stessa etichetta: la ripetizione è dell'inglese |
| `Satisfaction.` | **Soddisfazione.** | |
| `Sadness.` | **Tristezza.** | |
| `Exasperation.` | **Esasperazione.** | |
| `Mocking.` | **Derisione.** | sarcasmo dichiarato, non «scherno» generico |
| `Humor.` | **Umorismo.** | distinta da `Irony` e da `Mocking` |
| `Reservation.` | **Riserva.** | il politico che accetta «con riserva» |
| `Assurance.` | **Rassicurazione.** | |
| `Pensive.` | **Riflessione.** | |
| `Resolve.` | **Determinazione.** | |
| — (unità 177) | — | **nessuna etichetta**: è una domanda Avgi (`Have you any reports …, question?`) |

La **177** è l'unico caso del file: il `check.py` confronta la lista completa **con un `None` in posizione 17**, e
verifica che la stringa finisca con «, domanda?» (dispositivo di L48: «Tu umano, domanda?»).

## 2. Istituzioni e nomi

| inglese | resa | nota |
|---|---|---|
| `the Consonance` | **la Consonance** (2) | invariato |
| `the Incursion` | **l'Incursione** (2) | forma del corpus (65 occorrenze) |
| `the Assembly` | **l'Assemblea** (2) | tradotto (42 occorrenze) |
| `the Guard` | **la Guardia** (1) | **questione chiusa**: 28 occorrenze di «la Guardia» nel corpus, lasciata aperta in L233 |
| `the Avgi` | **gli Avgi** (3) | |
| `Tangled Shroud` / `the Shroud` | **il Tangled Shroud** (2) / **lo Shroud** (3) | invariati |
| `Stilacrest` | **Stilacrest** | toponimo |
| `polities` | **entità politiche** (2) | misurato: 10 occorrenze nel corpus, nessuna di «politie» |
| `Aberrations`, `Aberrant` | **Aberrant** (7) | un solo nome per la fazione (decisione 25) |

## 3. Lessico

| inglese | resa | nota |
|---|---|---|
| `Reactor fuel` | **carburante per reattore** | |
| `run a blockade` | **forzare un blocco** | chi parla è chi lo attraversa, non chi lo impone |
| `evaded at certain ports` | **si possono evadere in certi porti** | |
| `war economy` | **economia di guerra** | |
| `economic austerity` | **austerità economica** | «austerità» già nel corpus (L52) |
| `chafe under` | **spazientirsi per** | «insofferire» è raro e suona letterario |
| `war behind the front lines` | **guerra dietro le linee del fronte** | |
| `a mere page on a courier ship` | **solo un paggetto su una nave corriere** | `page` è il ragazzo di servizio, non una pagina |
| `stacks of memory sheets` | **pile di fogli di memoria** | oggetto di scena, non nome di prodotto |
| `a credit to my name` | **un credito a mio nome** | |

## 4. Apici: 6 inglesi, 12 italiani

L'inglese contrae in sei unità (`don't`, `isn't`, `I'm`, `there's`, `It's`, `we'll`); l'italiano elide in nove
(`l'avrebbero`, `L'unica`, `dall'Incursione`, `c'è`, `dell'Incursione`, `c'erano`, `all'Assemblea`, `l'economia`,
`l'altro`). È l'inverso di L233 (12 contro 5): le due lingue non vanno nella stessa direzione e il controllo elenca le
unità, non i totali (decisione 202).

## 5. Struttura

- **Ogni unità è una citazione intera**: 2 virgolette, 40 in tutto, punto finale **dentro** le virgolette.
- **Zero tab**, **zero segnaposto**: due asserzioni negative scritte.
- **Nessuna riga `log`**.

## 6. Lacune dichiarate

- **`NT` vuoto per misura**: nessuna `UI_LABEL`, nessun riferimento di dato; il `check.py` lo scrive come asserzione.
- Il **`missing advisory`** (righe 216–280) non è in questo lotto, ma la sua lacuna d'inventario è già stata misurata
  in L235 e dichiarata lì: 13 blocchi `word`, il database ne conserva 2.
