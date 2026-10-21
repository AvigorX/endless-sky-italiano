# REVIEW — L130 · `boarding missions.txt` (Tarquin e la nave negriera)

Coppie EN→IT rilette in `translation.json` (`53f6d41b0bfedb6c…`). Tutte le 75 unità sono **`PENDING`**.

## 1. Voce

- **Tarquin** parla affettato e si tradisce: «Ti sto offrendo i miei profitti da spilorcio. Chiamiamolo pagare per una
  lezione imparata», «Gli zotici non sono abituati a questo genere di pericolo».
- **La narrazione** è al presente e al «tu»: «Sali a bordo della <origin>, ma non trovi nessun membro
  dell'equipaggio».
- **Il tono delle scene violente** resta asciutto, come nel sorgente: «Abbatti il capitano Tarquin a sangue freddo,
  con shock di almeno un membro del tuo gruppo d'abbordaggio».
- **Le opzioni** fra parentesi tonde, senza punto interrogativo aggiunto.

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `outfits and cargo` | **dotazioni e carico** | 1 |
| `escape pod` | **capsula di salvataggio** | 2 |
| `self-destruct sequence` | **sequenza di autodistruzione** | 2 |
| `ex-pirate crew members` | **membri dell'equipaggio, ex pirati** | 3 |
| `tyrannical captain` · `servitude` | **capitano tiranno** · **servitù** | 4 |
| `sidearm` · `bulkhead` | **arma da fianco** · **paratia** | 11 |
| `princely sum` | **principesca somma** | 11 |
| `gift horse in the mouth` | **guardare in bocca al cavallo donato** | 18 |
| `perishable goods` | **merci deperibili** | 21 |
| `cheapskate` · `bumpkins` | **spilorcio** · **zotici** | 21, 23 |
| `nave negriera` | `slave ship` | 31 |
| `as tense as a steel cable` | **teso come un cavo d'acciaio** | 34, 58 |
| `in stony silence` | **in un silenzio di pietra** | 34, 58 |
| `brig` | **cella** | 50, 55, 70 |
| `good riddance to bad rubbish` | **che se ne sia andato al diavolo** | 56 |
| `a cold day in hell` | **un giorno freddo all'inferno** | 61 |
| `malnourished wretches` | **disgraziati denutriti** | 70, 73 |
| `taken into captivity` | **preso in prigionia** | 55, 73 |

## 3. Nodi aperti (da non dedurre dopo)

1. **Le 22 `UI_LABEL` erano tutte qui**: l'ultimo segmento del file (695–959) non ne ha, e la cella va scritta
   `0 = 0`.
2. **`VALUE` assente**: la verifica è un'asserzione vuota **scritta**; un lotto che introducesse un `VALUE` senza
   dichiararlo farebbe fallire la lista `== []`.
3. **Le varianti d'ingresso** (11, 13, 15) condividono un lungo testo: se un lotto futuro toccasse la parte comune,
   le tre varianti andrebbero riallineate insieme, non una per una.
4. **Due unità identiche** (35 e 59) hanno una sola resa: è la regola «stesso inglese ⇒ stessa resa».
5. **L'unità 21 con tre virgolette** è un difetto del sorgente riprodotto: non va «corretto».
6. **Il registro di Tarquin** è la ragione d'essere del lotto: se un revisore lo appiattisse, si perderebbe il
   personaggio. Le parole-spia (`spilorcio`, `zotici`, `lezione imparata`) sono nel controllo.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 75 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: la missione non è stata vista, e i quattro esiti non sono stati «giocati».
- **Nessuna revisione umana**.
- **Il file non è completo**: resta l'ultimo segmento (76 unità, righe 695–959).

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (30 controlli), `verify.py` exit **0** (30 controlli) |
