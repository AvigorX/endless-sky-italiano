# REVIEW — L223 · `remnant outfits.txt` (primo lotto)

Coppie EN→IT rilette in `translation.json` (`865540cb64989e26…`). Tutte le 12 unità sono **`PENDING`**.

## 1. La linea fra nome e parola comune

| inglese | italiano | perché |
|---|---|---|
| `Inhibitor Cannon`, `Thrasher Cannon`, `Point Defense Turret`, `EMP Torpedo Storage Bay` | **invariati** | sono i nomi che il giocatore vede nel negozio di equipaggiamenti |
| *cannon* / *cannons* | «cannone / cannoni» | parola comune dentro la prosa |
| *turret* / *turrets* | «torretta / torrette» | idem |
| *torpedo* / *torpedoes* (in prosa) | «siluro / siluri» | idem; il nome dell'oggetto resta `EMP Torpedoes` |

Il controllo verifica **entrambi i lati** della linea: che i nomi compaiano nella prosa italiana, e che le forme inglesi non
sopravvivano come parole comuni.

## 2. Decisioni di resa

1. **`Nearly a century ago`** → «Quasi un secolo fa»; **`came under fire`** → «fu attaccato».
2. **`The story says that the Remnant captain calmly told her crew`** → «La storia racconta che la capitana dei Remnant
   disse con calma al suo equipaggio». `captain` senza genere in inglese: qui il contesto della citazione non lo impone, e
   «capitana» è la scelta; resta dichiarata.
3. **`"We aren't going home until we steal that weapon."`** → «"Non torneremo a casa finché non ci impadroniremo di
   quell'arma."» — parlato dentro la narrazione, virgolette dritte, punto fermo dentro le virgolette come in inglese.
4. **`Instead of letting their effort go to waste`** → «Invece di lasciare che il loro sforzo andasse sprecato».
5. **`controlling engagement distances`** → «controllare le distanze di ingaggio»; **`pushing them backward with the
   impact of each shot`** → «respingendoli con l'impatto di ogni colpo».
6. **`outrun opponents rather than defeat them`** → «seminare gli avversari invece di sconfiggerli»: `outrun` è la fuga, non
   la vittoria.
7. **`unremarkable in terms of performance`** → «non abbiano prestazioni eccezionali».
8. **`strong torques … swiveling mount unfeasible`** → «le forti coppie che … rendevano impraticabile l'uso di un affusto
   girevole»: `torque` = coppia meccanica; `mount` = affusto.
9. **`reverse engineer`** → «ricostruire con l'ingegneria inversa» (unità 5).
10. **`a very satisfying amount of damage`** → «una quantità di danni molto soddisfacente»: il tono da recensione è nel
    testo e va lasciato.
11. **`vaults deep under the mountains`** → «camere profonde sotto le montagne»; **`caches of alien technology`** →
    «depositi di tecnologia aliena».
12. **`they are now considered to be much more useful than most of the items that they were guarding`** → «oggi sono
    considerati molto più utili della maggior parte degli oggetti che sorvegliavano».
13. **`an otherwise battery-less ship`** → «una nave altrimenti priva di batterie».
14. **`would overrun human space and expand beyond it`** → «travolgessero lo spazio umano e lo superassero».

## 3. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 12 unità `PENDING`.
- **Nessun equipaggiamento visto nel gioco**: la scelta di lasciare i nomi in inglese è coerente col database e con la
  regola dei `VALUE`, ma non è stata osservata nella schermata di allestimento.
- **Nessuna revisione umana**: il genere di «capitana» è una scelta, non un dato del sorgente.
- **Nessuna correzione al sorgente**.

## 4. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì |
| ESEGUITO | sì |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (28), `verify.py` exit **0** (18) |
