# REVIEW — L230 · `korath outfits.txt` (terzo lotto)

Coppie EN→IT rilette in `translation.json` (`d246b4e6c38a2e78…`). Tutte le 26 unità sono **`PENDING`**.

## 1. La frase che attraversa il lotto

*Korath afterburners pump super-heated hyperspace fuel directly into a thruster's plasma stream, resulting in a phenomenal
explosion that nearly melts the thruster.*

Compare in **unità 1 e 4** di questo lotto e in **L229 unità 10 e 13**: quattro schede, due finestre, una sola resa. Il
controllo legge il `translation.json` di L229 e confronta la stringa alla riga 300 con quella dell'unità 1: se divergessero,
lo stesso afterburner avrebbe due descrizioni in due posti.

## 2. Le cinque copie

*This Korath engine has been modified to be partially installed in a ship's weapon space, allowing it to push the ship in
reverse.* — unità **11, 14, 17, 20, 23**, cioè i Reverser Asteroid, Comet, Lunar, Planetary e Stellar. Una sola resa,
verificata come insieme con un elemento: `len({…}) == 1`.

## 3. Decisioni di resa

1. **`integrated active cooling systems, powered by the fuel-plasma explosion`** → «sistemi di raffreddamento attivo
   integrati, alimentati dall'esplosione di carburante e plasma».
2. **`to keep the reaction chambers from melting`** → «per evitare che le camere di reazione si fondano».
3. **`the prevailing Korath attitude … bigger, faster, and more powerful`** → «l'atteggiamento prevalente dei Korath …
   fare le cose più grandi, più veloci e più potenti».
4. **`the Exiles found it necessary to develop these engines`** → «gli Esuli ritennero necessario sviluppare questi
   motori». `Exiles` è una parola inglese comune usata come nome di fazione: tradotta, a differenza dei nomi propri Korath.
5. **`carry larger weapons or more cargo`** → «trasportare armi più grandi o più carico».
6. **`acts as a reverser`** → «funge da retropulsore»; **`a full range of mobility`** → «una gamma completa di mobilità».
7. **`captains with weapon space to spare`** → «capitani … con spazio per le armi da spendere».
8. **`too large to be worth sacrificing weapon space`** → «troppo grande perché valga la pena sacrificargli spazio per le
   armi».
9. **`Dwarfing any reversers in human space`** → «Surclassando qualsiasi retropulsore dello spazio umano».
10. **`Being essentially a slightly altered Planetary Class engine`** → «Essendo in sostanza un motore Planetary Class
    leggermente modificato».
11. **`Modeled on their largest engines`** → «Modellato sui loro motori più grandi»; **`unlike anything you've seen
    before`** → «diversa da qualsiasi cosa tu abbia mai visto».
12. **`produces quite a kick`** → «produce un bel calcio»; **`draws a considerable amount of power`** → «assorbe una
    quantità considerevole di energia».

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 26 unità `PENDING`.
- **Nessun equipaggiamento visto nel gioco**: la resa di `reverser` → «retropulsore» è coerente con L205, non verificata
  nell'interfaccia.
- **Nessuna revisione umana**, **nessuna correzione al sorgente**.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì |
| ESEGUITO | sì |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (27), `verify.py` exit **0** (19), con controllo inter-lotto |
