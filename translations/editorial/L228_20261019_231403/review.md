# REVIEW — L228 · `korath outfits.txt` (primo lotto)

Coppie EN→IT rilette in `translation.json` (`49228f599876094f…`). Tutte le 20 unità sono **`PENDING`**.

## 1. Nome o parola comune? Il caso `Fusion Reactor`

| unità | inglese | trattamento | italiano |
|---|---|---|---|
| 7 | *This compact **Fusion Reactor** is an ancient Korath design* | **nome** → invariato | «Questo compatto Fusion Reactor…» |
| 9 | *the Korath designed a **fusion reactor** far more powerful* | **parola comune** → tradotta | «un reattore a fusione molto più potente» |

`Fusion Reactor` esiste come nome di equipaggiamento anche nelle missioni della Coalition (verificato nel database), quindi
il maiuscolo è un nome e resta. Il minuscolo è una descrizione generica e si traduce. Il `check.py` verifica che il nome sia
presente **e** che l'unità 7 non contenga «reattore a fusione».

## 2. Le 7 unità copiate

`Generators (Candle Class)`, `Generators (Furnace Class)`, `Generators (Inferno Class)`, `Systems Cores (Tiny)`,
`Systems Cores (Small)`, `Systems Cores (Medium)`, `Systems Cores (Large)` — tutti nomi mostrati nella bacheca, copiati alla
lettera dal sorgente (non trascritti a mano, regola di L220).

## 3. Decisioni di resa

1. **`produces a significant amount of energy using the heat produced by the radioactive decay`** → «produce una quantità
   notevole di energia usando il calore prodotto dal decadimento radioattivo».
2. **`power-hungry`** → «avido di energia»: stessa resa di L226, per continuità.
3. **`radiothermal generators even in their fighters and interceptors`** → «generatori radiotermici persino nei caccia e
   negli intercettori».
4. **`rather than relying on fuel cells or other comparable technology`** → «invece di affidarsi a celle a combustibile o ad
   altra tecnologia simile».
5. **`with their typical disregard for the environmental impacts`** → «con la loro tipica indifferenza per l'impatto
   ambientale».
6. **`some rather alarming isotopes`** → «isotopi piuttosto allarmanti».
7. **`Its considerable energy output is offset by the heat it produces`** → «La sua notevole resa energetica è compensata
   dal calore che produce».
8. **`served as the mainstay of their war fleets`** → «fu il pilastro delle loro flotte da guerra»: `mainstay` = «pilastro»,
   la stessa resa usata per la Myaede in L219.
9. **`the sheer inefficiency`** → «La pura e semplice inefficienza».
10. **`dealing with large amounts of waste heat`** → «gestire grandi quantità di calore disperso».
11. **`would overheat within seconds as soon as they began to fire their weapons`** → «si surriscalderebbe in pochi secondi
    non appena iniziasse a sparare».
12. **`a liquid sodium cooling loop`** → «un circuito a sodio liquido»; **`maintain a minimum temperature in order to keep
    the sodium from freezing`** → «mantenere una temperatura minima, così che il sodio non si congeli».
13. **`dispense with Systems Cores`** → «rinuncia ai Systems Core».
14. **`larger than necessary generators`** → «generatori più grandi del necessario»; **`if they take damage`** → «se
    subiscono danni».
15. **`sacrifice enough firepower to mount this shield generator, capacitor, swarm of repair microbots, and computer to
    control them`** → «sacrificare abbastanza potenza di fuoco per installare questo generatore di scudi, condensatore,
    sciame di microbot riparatori e il computer che li controlla».
16. **`houses the ship's central computer, shield generators, reserve power`** → «ospita il computer centrale della nave, i
    generatori di scudi, l'energia di riserva».
17. **`repair microbots that can move across a ship's exterior and slowly repair damage to the hull`** → «microbot
    riparatori, che possono spostarsi sull'esterno di una nave e riparare lentamente i danni allo scafo».
18. **`this massive bank of computers … holds everything needed to keep … in working condition`** → «questo imponente
    complesso di computer … contiene tutto ciò che serve per mantenere in efficienza».

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 20 unità `PENDING`.
- **Nessun equipaggiamento visto nel gioco**: la distinzione maiuscolo/minuscolo è una deduzione dal database e dal testo.
- **Nessuna revisione umana**, **nessuna correzione al sorgente**.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì |
| ESEGUITO | sì |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (27), `verify.py` exit **0** (20) |
