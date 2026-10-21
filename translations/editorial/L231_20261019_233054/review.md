# REVIEW — L231 · `korath outfits.txt` (quarto lotto)

Coppie EN→IT rilette in `translation.json` (`39c7cbdeb1825d8b…`). Tutte le 21 unità sono **`PENDING`**.

## 1. La voce dei Korath sull'efficienza

*The Korath have the dubious distinction of relying on propulsion systems that produce more waste heat than the weapon
systems of most other species.* → «I Korath hanno il dubbio primato di affidarsi a sistemi di propulsione che producono più
calore disperso dei sistemi d'arma della maggior parte delle altre specie.»

`dubious distinction` è ironico e «dubbio primato» lo conserva senza spiegarlo. `waste heat` è «calore disperso», termine
già fissato.

## 2. La leggenda dei Quarg

Unità 7, la più lunga del lotto. *A legend among the Korath claims that when they were first testing out their latest
generation of plasma thrusters, a concerned Quarg fleet approached and volunteered to help evacuate the Korath crew from what
they assumed was a dying ship. The Quarg were surprised to learn that the flames shooting out the back of the ship were in
fact its intended mode of propulsion.*

Reso: «Una leggenda dei Korath racconta che, quando stavano provando la loro ultima generazione di propulsori al plasma, una
flotta Quarg preoccupata si avvicinò e si offrì di aiutare a evacuare l'equipaggio Korath da quella che credevano essere una
nave in fin di vita. I Quarg rimasero sorpresi nello scoprire che le fiamme che uscivano dalla parte posteriore della nave
erano in realtà il suo sistema di propulsione previsto.» — L'ordine degli eventi è quello dell'inglese, e `intended` →
«previsto» è il punto della battuta: le fiamme **dovevano** esserci.

## 3. Gli Efreti e la fisica

1. **`begun to grudgingly take inspiration from their not-entirely-welcome Quarg guardians`** → «hanno iniziato a trarre
   ispirazione, malvolentieri, dai loro tutori Quarg, non del tutto graditi». `not-entirely-welcome` non si risolve con un
   aggettivo solo: «non del tutto graditi» conserva la litote.
2. **`at the cost of even higher energy use`** → «al prezzo di un consumo energetico ancora maggiore».
3. **`The forced retreat from research into interstellar jump drive technology`** → «Il ritiro forzato dalla ricerca sulla
   tecnologia del jump drive interstellare». `jump drive` resta invariato.
4. **`little else to tinker with than subluminal propulsion`** → «poco altro con cui armeggiare se non la propulsione
   subluminale».
5. **`Synthesizing gravitational propulsion with more traditional plasma thrusters moderates the heat output`** →
   «Sintetizzare la propulsione gravitazionale con i più tradizionali propulsori al plasma modera il calore emesso».
6. **`mathematically self-consistent, but stubbornly unfalsifiable, conjectures of String Theory`** → «le congetture
   matematicamente coerenti ma ostinatamente non falsificabili della Teoria delle Stringhe».
7. **`maintain the traditional Korath emphasis on speed in a small package while keeping heat output down`** → «mantenere la
   tradizionale enfasi Korath sulla velocità in un pacchetto compatto, tenendo basso il calore prodotto».
8. **`concrete aspects of the unity that underlies both quantum gravity and the forces that bind quarks and gluons`** →
   «aspetti concreti dell'unità che sta alla base sia della gravità quantistica sia delle forze che tengono insieme quark e
   gluoni».
9. **`this technological synthesis lags behind comparable Quarg technology`** → «questa sintesi tecnologica è indietro
   rispetto alla tecnologia Quarg comparabile».

## 4. Terminologia

| EN | IT | nota |
|---|---|---|
| thruster (`Thrusters (…)`) | nome invariato / **propulsore** | due usi distinti |
| steering (`Steerings (…)`) | nome invariato / **sistema di sterzata** | mai «sterzo» |
| waste heat | **calore disperso** | da L203 |
| heat output | **calore prodotto / emesso** | secondo il contesto |
| gravitational propulsion | **propulsione gravitazionale** | |
| gravitoplasma-based | **a gravitoplasma** | composto conservato |
| jump drive | **jump drive** | invariato |
| String Theory | **Teoria delle Stringhe** | nome di teoria, tradotto |
| Quarg, Efreti | **invariati** | popoli |

## 5. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 21 unità `PENDING`.
- **Nessun equipaggiamento visto nel gioco**: nessuna delle rese tecniche è stata osservata nell'interfaccia.
- **Nessuna revisione umana**, **nessuna correzione al sorgente**.

## 6. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì |
| ESEGUITO | sì |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (27), `verify.py` exit **0** (19) |
