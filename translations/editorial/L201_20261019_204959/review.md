# REVIEW — L201 · `hai outfits.txt` (primo lotto)

Coppie EN→IT rilette in `translation.json` (`76f769f988aefc73…`). Tutte le 8 unità sono **`PENDING`**.

## 1. Decisioni di resa

1. **`olopad`** per *holopad*: la resa esiste già in staging («sul tuo olopad»). Il prestito resta invariato al
   plurale (`singoli "olopad"`), come in italiano corrente per i termini tecnici importati.
2. **`corsaro`** per *privateer* e **`contrabbandiere`** per *smuggler*: due parole distinte per due ruoli distinti,
   entrambe già in staging.
3. **`equipaggiamenti`** per *outfits*: termine del glossario, usato anche in «equipaggiamenti illegali».
4. **Nomi di prodotto invariati**: `Phantom Pallet`, `Holovid Zone`, `Pulse Cannon`, `Tripulse Shredder`,
   `Deathsticks`, `Unfettered`, `Wanderer`. **`Deathsticks`** resta inglese perché è il nome di una droga-oggetto, non
   una descrizione.
5. **`cannoni a ioni`** per *ion cannons* minuscolo: è il testo generico, non il nome del prodotto (`Ion Cannon`).
   La distinzione è verificata dal `check.py`.
6. **`campi di forza texturizzati`** e **`altoparlanti a schiera di fase`**: resa tecnica di *textured force fields* e
   *phase array speakers*, senza circonlocuzioni.
7. **`alloggiamento`** per *housing* (contenitore delle armi), **`raffiche`** per *bursts*, **`pattern di fuoco`** per
   *firing pattern*: lessico balistico standard.
8. **`arma mordi e fuggi`** per *hit-and-run weapon*: idioma italiano, non calco.
9. **`fantasmi per i sensori`** per *sensor ghosts*: l'inglese tecnico dei radar ha già «ghost»; in italiano «fantasmi»
   rende l'idea senza perdere il registro.
10. **`più di una volta`** aggiunto in unità 1 per rendere *has been known to*: l'italiano non ha un equivalente
    impersonale altrettanto asciutto, e la frase senza sarebbe risultata affermativa in modo assoluto.

## 2. Un controllo corretto, non un testo

Il primo `check.py` è uscito con **`FAIL totale: 1`** sull'asserzione «9 nomi di prodotto invariati»: `Pulse Turret` e
`Ion Cannon` **non compaiono nel testo inglese**, solo nei contesti (`outfit:Pulse Turret`, `outfit:Ion Cannon`).
L'errore era nel presupposto dell'asserzione; la traduzione non è stata toccata. Il nuovo controllo distingue i nomi
**presenti nell'inglese** (che devono restare invariati) da quelli che nel testo non ci sono, e lo dichiara.

## 3. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 8 unità `PENDING`.
- **Nessun equipaggiamento installato nel gioco**, **nessun testo visto a schermo**, **nessuna revisione umana**.
- **Nessuna correzione al sorgente**: le incoerenze del gioco si conservano.

## 4. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — `parts/part01.json`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, compreso il `FAIL 1` intermedio |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (24 controlli), `verify.py` exit **0** (15 controlli) |
