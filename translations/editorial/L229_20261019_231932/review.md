# REVIEW — L229 · `korath outfits.txt` (secondo lotto)

Coppie EN→IT rilette in `translation.json` (`b85fa00ea11fb613…`). Tutte le 15 unità sono **`PENDING`**.

## 1. Le tre unità quasi identiche

| unità | classe | inglese | italiano |
|---|---|---|---|
| 7 | Asteroid | *…explosion that **may** nearly melt the thruster* | «…esplosione che **può quasi fondere** il propulsore» |
| 10 | Comet | *…explosion that nearly melts the thruster* | «…esplosione che **quasi fonde** il propulsore» |
| 13 | Lunar | **identica alla 10** | **identica alla 10** |

Verificato: `t[10] == t[13]` (identità piena) e `t[7] == t[10]` con la sola sostituzione «che quasi fonde» → «che può quasi
fondere». La differenza inglese è un avverbio di possibilità, e la resa la conserva invece di appiattirla.

## 2. Le 4 unità copiate

`Afterburners (Asteroid Class)`, `Afterburners (Comet Class)`, `Afterburners (Lunar Class)`, `Afterburners (Planetary
Class)` — nomi della bacheca, copiati dal sorgente.

## 3. Decisioni di resa

1. **`during the latter half of the Korath Civil War`** → «nella seconda metà della Guerra Civile Korath».
2. **`attempted to provide for their war effort by raiding the Hai for supplies`** → «cercarono di sostenere lo sforzo
   bellico razziando gli Hai per procurarsi rifornimenti».
3. **`would often end up stranded after they had run out of fuel`** → «finivano spesso bloccate dopo aver esaurito il
   carburante».
4. **`this hybrid fuel storage and ramscoop device`** → «questo dispositivo ibrido di stoccaggio del carburante e ramscoop».
5. **`the main source of fuel for the remaining Korath in the galaxy`** → «la principale fonte di carburante per i Korath
   rimasti nella galassia».
6. **`the robotic war machines left behind after their recent conflict`** → «le macchine da guerra robotiche rimaste dopo il
   loro recente conflitto».
7. **`this minimal, spartan Command Center`** → «questo Command Center minimale e spartano».
8. **`override the AI and interface with the ship's controls`** → «scavalcare l'IA e interfacciarsi con i comandi della
   nave»; **`a single bunk for the captain`** → «una sola cuccetta per il capitano».
9. **`some sort of advanced, miniature computer`** → «una sorta di computer miniaturizzato e avanzato»; **`hyperspace
   communication relay`** → «relè di comunicazione per l'iperspazio».
10. **`controls the Mereti automata or allows them to more easily coordinate their actions with each other`** → «controlla
    gli automata Mereti o permette loro di coordinare più facilmente le proprie azioni».
11. **`connected to all the major systems of a Kor Sestor automaton`** → «collegato a tutti i sistemi principali di un
    automata Kor Sestor».
12. **`encrypted and authenticated in a way that would make it nearly impossible to spoof the control signals`** → «cifrate
    e autenticate in modo tale da rendere quasi impossibile falsificare i segnali di controllo».
13. **`as much Fuel Processor as it is afterburner`** → «è tanto un Fuel Processor quanto un postbruciatore».
14. **`squeeze a hyperdrive into otherwise intrasystem ships and dispense with conventional thrusters entirely`** →
    «infilare un'iperguida in navi altrimenti confinate all'interno di un sistema e di fare a meno del tutto dei propulsori
    convenzionali».
15. **`super-heated hyperspace fuel … into a thruster's plasma stream`** → «carburante per l'iperspazio surriscaldato …
    nel flusso di plasma di un propulsore».
16. **`reach absurd speeds`** → «raggiungere velocità assurde»; **`will require some serious cooling`** → «richieda un
    raffreddamento serio».
17. **`an incredible amount of thrust for their fuel usage`** → «una spinta incredibile rispetto al carburante consumato».
18. **`dedicated reaction chambers with cooling vents`** → «camere di reazione dedicate con prese di raffreddamento».

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 15 unità `PENDING`.
- **Nessun equipaggiamento visto nel gioco**: la resa di «iperguida» per `hyperdrive` è una scelta lessicale, non un termine
  osservato nell'interfaccia.
- **La scheda `Afterburner (Planetary Class)` è incompleta di proposito**: la seconda parte è alla riga 319, fuori dalla
  finestra, e si tradurrà in L230.
- **Nessuna revisione umana**, **nessuna correzione al sorgente**.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì |
| ESEGUITO | sì |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (27), `verify.py` exit **0** (18) |
