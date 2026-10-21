# REVIEW — L97 · `coalition culture conversations.txt` (chiude il file)

Coppie EN→IT rilette in `translation.json` (`cc6086592132277e…`).

## 1. Voce e registro

- **Gli Heliarch parlano invertito** come Kimek, Saryd e Arach: «Saluti, Capitano `<last>`. Un'ispezione di
  routine, stiamo facendo». Unità interessate: **13, 22, 25**.
- **Le due voci Heliarch non sono identiche**: l'agente del Punisher è burocratico e formale, il Saryd della
  torre della fame è spaventato e si scusa («Tenere calmi i locali, dobbiamo»). Il registro si ricava dalla
  scena, non dalla specie.
- **Il capitano Arach** (19, 22) è affannato e spezza le frasi: la resa mantiene gli incisi.
- **Il narratore resta piano** anche nella scena dell'anello, dove il testo accelera da solo.

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità | nota |
|---|---|---|---|
| `narrowly avoids` | **evita per un soffio** | 1 | non «quasi evita» |
| `screen of warships` | **schermo di navi da guerra** | 12 | termine militare |
| `Interdictor` / `Punisher` | invariati | 4, 12–17 | classi di nave |
| `turning your ship upside down` | **mettere la nave sottosopra** | 15–17 | è l'ispezione, non un danno |
| `keep tabs within your ship` | **tenervi d'occhio** | 17 | idiom |
| `hunger tower` | **torre della fame** | 26 | nome dell'edificio |
| `gurney` · `body bag` | **barella** · **sacco per cadaveri** | 35 | il testo è esplicito |
| `catatonic` | **catatonico** | 34 | stato clinico, non «immobile» |
| `"cooperating,"` / `"cooperating",` | virgola dentro / fuori | 15, 17 | differenza del sorgente, riprodotta |

## 3. Nodi aperti (da non dedurre dopo)

1. **`<last>`** compare una sola volta (unità 13) ed è il cognome del giocatore: resta un token.
2. **Le tre unità 7/9/11 sono identiche**: l'abbordaggio, in tre rami diversi. Una modifica va fatta nella
   costante `BOARDING` del costruttore.
3. **Le varianti 15/17 hanno la stessa frase e punteggiatura diversa**: la differenza è voluta.
4. **Il Saryd dell'anello** riceve tre nomi diversi («il Saryd», «il suo sguardo», «l'arma»): è un personaggio
   senza nome, e la traduzione non ne inventa uno.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 36 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: nessuna di queste scene è stata vista a schermo.
- **Nessuna revisione umana**: il lotto e il file non sono approvati.
- **La campagna non è finita**: 128 file con unità residue, 7.358 unità / 169.675 parole.

## 5. Rischi residui

- **Chiusura del file**: l'invariante 157/157 dipende dai cinque `translation.json`; riscrivere un lotto
  precedente renderebbe rosso il `verify.py` di L97 — ed è corretto, perché il file non sarebbe più quello
  verificato.
- **I tre `Departing Trouble`** sono varianti: una revisione che li uniformasse cancellerebbe le differenze
  volute (l'Interdictor che si scusa, il pensiero del Lunarium, le cimici).
- **`sacco per cadaveri`** è crudo: è la descrizione del giocatore, e ammorbidirla cambierebbe il tono della
  scena.

## 6. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (30 controlli), `verify.py` exit **0** (29 controlli), file **157/157** |
