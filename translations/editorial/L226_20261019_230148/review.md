# REVIEW — L226 · `remnant outfits.txt` (quarto lotto)

Coppie EN→IT rilette in `translation.json` (`7418d831f5d6ba86…`). Tutte le 11 unità sono **`PENDING`**.

## 1. Nove contesti, due coppie

| equipaggiamento | unità | nota |
|---|---|---|
| `Salvage Scanner` | 2 | prima parte: l'origine dai Point Defense Turrets; seconda: l'utilità per i capitani |
| `Bellows-Class Afterburner` | 2 | prima parte: la filosofia; seconda: il costo in carburante |
| gli altri sette | 1 | Research Laboratory, Quantum Key Stone, Anvil, Crucible, Forge, Smelter, Steering |

Le due coppie **non** ripetono formule: ognuna delle due unità aggiunge un'informazione nuova. Non c'era quindi niente da
uniformare, e il controllo non ha inventato confronti che il testo non richiede.

## 2. Decisioni di resa

1. **`little more than a closet packed with scanners and equipment`** → «poco più di un armadio stipato di scanner e
   attrezzature»: `closet` è il giudizio di uno scienziato di pianeta, non una descrizione tecnica.
2. **`base of operations used to investigate … on-site`** → «base operativa usata per studiare sul posto».
3. **`having advanced equipment … as well as a trained scientist`** → «disporre di attrezzature avanzate … e di uno
   scienziato addestrato»; **`amount to a strong benefit`** → «è un vantaggio notevole».
4. **`attunes a ship's quantum oscillations`** → «sintonizza le oscillazioni quantistiche di una nave».
5. **`otherwise impassable wormholes`** → «wormhole altrimenti invalicabili»: `wormhole` resta invariato, come nei lotti
   precedenti.
6. **`only be mined from one location in the Waste`** → «estratte in un solo luogo della Waste».
7. **`unraveled the alien Point Defense Turrets`** → «decifrarono il funzionamento dei Point Defense Turrets alieni»:
   `unravel` qui è capire un meccanismo, non sfilare un tessuto.
8. **`the mechanisms that guided the ancient weapons`** → «i meccanismi che guidavano quelle armi antiche»; **`guidance
   systems`** → «sistemi di guida» (la stessa parola inglese, due sensi, due rese).
9. **`boost their range and power`** → «aumentarne portata e potenza».
10. **`raw materials for fuel are relatively common on the winds of the nebula`** → «le materie prime per il carburante sono
    relativamente comuni nei venti della nebulosa».
11. **`reluctant to waste fuel, they aren't afraid of using it when needed`** → «restii a sprecare carburante … non temono di
    usarlo quando serve».
12. **`it is continued life that is paramount`** → «ciò che conta è continuare a vivere».
13. **`great leaps of acceleration`** → «grandi balzi di accelerazione»; **`evasive maneuvers`** → «manovre evasive».
14. **`before completely running out of fuel`** → «prima di restare completamente a secco».
15. **`combines both thrusters and steering into one unit`** → «riunire in un'unica unità sia i propulsori sia la sterzata».
16. **`propelled at a sizable fraction of the speed of light`** → «espulso a una frazione considerevole della velocità della
    luce».
17. **`more power-hungry`** → «più avido di energia»: mantiene la metafora del consumo.
18. **`an indication, perhaps, of their preference for avoiding battle`** → «un indizio, forse, della loro preferenza per
    evitare la battaglia»: l'incertezza è nel testo e resta.

## 3. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 11 unità `PENDING`.
- **Nessun equipaggiamento visto nel gioco**: nessuna delle rese è stata osservata in partita.
- **Nessuna revisione umana**, **nessuna correzione al sorgente**.

## 4. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì |
| ESEGUITO | sì |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (26), `verify.py` exit **0** (19) |
