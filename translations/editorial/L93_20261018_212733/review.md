# REVIEW — L93 · `coalition culture conversations.txt` (primo lotto)

Coppie EN→IT rilette in `translation.json` (`f11dbf2fa0744173…`).

## 1. Voce e registro

- **I Saryd parlano invertito**: è il tratto che li distingue nel gioco. In italiano l'ordine marcato si ottiene
  spostando il predicato in fondo o il soggetto dopo (`Una celebrazione del folklore Saryd, è`;
  `scegliere il vostro sentiero, dovete`; `Che lo spettacolo vi sia piaciuto, spero`). Non si usa un italiano
  sgrammaticato: sarebbe una caricatura e renderebbe illeggibili le istruzioni di gioco.
- **Il narratore resta piano** («Lo seguite fuori dalla città-spazioporto»): la voce marcata è solo dei Saryd.
- **Il giocatore è «voi»** nella narrazione e nelle battute («Fate strada»), e i Saryd gli si rivolgono con
  «sareste». Nessuna forma che presupponga il genere del giocatore (unità 2 al plurale).

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità | nota |
|---|---|---|---|
| `Interested in participating …, would you be?` | **Interessati a partecipare …, sareste?** | 2 | plurale: niente genere |
| `A celebration of Saryd folklore, it is` | **Una celebrazione del folklore Saryd, è** | 5 | ordine marcato, non sgrammaticato |
| `timeless classics … we still celebrate` | **i classici senza tempo … ancora celebriamo** | 5 | idem |
| `choose your path, you must` | **scegliere il vostro sentiero, dovete** | 10 | idem |
| `That you enjoyed the spectacle, I hope` | **Che lo spettacolo vi sia piaciuto, spero** | 31 | idem, e chiude il lotto |
| `caskets` | **scrigni** | 9, 10, 30 | contenitori da rito |
| `hedge-lion` | **leone da siepe** | 17, 18 | nome inventato, fra virgolette nel sorgente |
| `quills` | **aculei** | 17 | coerente con L91 |
| `a third of the size of human opera stages` | **un terzo dei palcoscenici d'opera umani** | 15, 20, 25 | paragone terrestre |
| `snipe` | **colpire … con una freccia** | 16 | il verbo inglese è venatorio, non «cecchinare» |

## 3. Nodi aperti (da non dedurre dopo)

1. **La voce invertita non è negoziabile**: se una revisione la «sistema», il testo perde la specie. Le quattro
   unità interessate sono 2, 5, 10, 31.
2. **Le tre unità del palco (15/20/25) sono identiche per costruzione**: una modifica va fatta nella costante
   `STAGE` di `mkparts.py`, non in una sola parte.
3. **`Saryd`, `Arach`, `Kimek`** restano invariati (specie e fazioni).
4. **`hoofs` → «zoccoli»**: i Saryd sono ungulati; se un lotto successivo li descrivesse diversamente, va
   segnalato come incoerenza del sorgente, non corretto in traduzione.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 31 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: nessuna di queste scene è stata vista a schermo.
- **Nessuna revisione umana**: il lotto non è approvato.
- **Il file non è chiuso**: 126 unità restano (righe 81–462).

## 5. Rischi residui

- **Il registro marcato può sfuggire** in una battuta su cinque: il `check.py` non lo verifica. La difesa è
  l'elenco delle unità con parlato Saryd (2, 5, 10, 31) e la lettura di quelle quattro a ogni revisione.
- **Unità 4** ha rapporto 1,55 (dentro il gate, ma il più alto del lotto): è la risposta breve del giocatore.
- **`leone da siepe`** è un calco: se il revisore preferisse «leone di siepe», cambia una parola in due unità.

## 6. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (28 controlli), `verify.py` exit **0** (27 controlli) |
