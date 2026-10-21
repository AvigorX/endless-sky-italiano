# REVIEW — L108 · `korath missions.txt` (frammenti composti, un Quarg in registro alto)

Coppie EN→IT rilette in `translation.json` (`c429ddeb0b22241c…`).

## 1. Voce e registro

- **Il Quarg di `Distress Call 1`** (21, 25, 28) non è quello storpiato di L107: qui parla **bene e in registro
  alto**, con un arcaismo leggibile («Salute, Capitano…», «esigono il vostro zelo più diligente, perché molte
  famiglie non abbiano a piangere i morti», «si patisce assai», «quando non ci si cura di ciò che gli altri
  soffrono»). Due Quarg, due voci: la traduzione non le appiattisce.
- **Il giocatore** risponde per opzioni brevi e secche: «Vado subito lì.», «Non possono intervenire i Quarg?»,
  «I Korath non mi interessano.», «Non rischio la mia nave per i Korath.». La durezza delle due ultime è del
  sorgente e non va ammorbidita: la replica del Quarg («La vita è rara e preziosa…») esiste **per rispondere** a
  quella durezza.
- **I frammenti `phrase:`** non hanno voce propria: sono la voce del **gioco che descrive** un Korath che chiede un
  favore con i gesti. Il registro è neutro e concreto, e le quattro frasi finali sono variazioni sullo stesso
  concetto («non occupa spazio»).

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità | nota |
|---|---|---|---|
| `A Korath` | **Un Korath** | 1 | soggetto, maiuscola |
| `A Kor Efret` | **Un Kor Efret** | 2 | |
| `A local` | **Un locale** | 3 | |
| `communicates using gestures that it wants you to` | **con gesti ti comunica che devi** | 4 | regge l'infinito |
| `uses gestures to ask you to` | **con gesti ti chiede di** | 5 | |
| `bring a small crate` | **portare una piccola cassa** | 6 | |
| `bring a package` | **portare un pacco** | 7 | |
| `take a shipment weighing less than one ton` | **accettare una spedizione che pesa meno di una tonnellata** | 8 | verbo distinto |
| `carry a box` | **portare una scatola** | 9 | «trasportare» superava il gate (2,09) |
| `to <destination> for <payment>.` | **a <destination> per <payment>.** | 10 | unico punto della frase principale |
| `It shouldn't take up any significant room on your ship.` | **Non dovrebbe occupare spazio di rilievo sulla vostra nave.** | 11 | |
| `It's small enough to fit below your seat.` | **È abbastanza piccolo da stare sotto il vostro sedile.** | 12 | |
| `The item is small enough for you to hold in your hands.` | **L'oggetto è abbastanza piccolo da stare nelle vostre mani.** | 13 | |
| `It's small enough that it won't take up any cargo space.` | **È abbastanza piccolo da non occupare spazio di carico.** | 14 | |
| `Package to <planet>` | **identico** | 15 | `VALUE` |
| `Take a small delivery … for a Kor Efret.` | **Porta una piccola consegna … per un Kor Efret.** | 16 | |
| `outstretch their hands as if waiting to receive the package` | **tende le mani come se aspettasse di ricevere il pacco** | 17 | |
| `Distress call from the <EDC-ship>` | **identico** | 18 | `VALUE` |
| `which has crashed on <destination>` | **precipitata su <destination>** | 19 | |
| `There are 40 survivors to rescue.` | **Ci sono 40 superstiti da salvare.** | 19 | numero in cifre, come il sorgente |
| `The occasional blue flashes` | **I lampi azzurri occasionali** | 20 | |
| `the enigmatic aliens` | **questi alieni enigmatici** | 20 | |
| `Salutations, Captain of the <ship>.` | **Salute, Capitano della <ship>.** | 21 | |
| `waylayed` | **hanno teso un agguato** | 21 | errore del sorgente (*waylaid*), reso senza commento |
| `Two score` | **Quaranta** | 21 | *score* = venti |
| `ere it could elude` | **prima che potesse sottrarsi** | 21 | |
| `We vanquished the Mereti` | **Abbiamo vinto i Mereti** | 25 | |
| `Without strong plate, we fare ill on a heavy world.` | **Senza una corazza robusta, su un mondo pesante si patisce assai.** | 25 | *plate* = corazzatura |
| `days before an expedition from Kuwaru Efreti` | **giorni prima di una spedizione da Kuwaru Efreti** | 25 | toponimo invariato |
| `Life is rare and precious across the vastness of space.` | **La vita è rara e preziosa nella vastità dello spazio.** | 28 | |
| `Return the <EDC-ship> survivors` | **identico** | 29 | `VALUE` |
| `Transport the <bunks> survivors … to <planet>.` | **Trasporta i <bunks> superstiti … su <planet>.** | 30 | |
| `you forgot the <bunks> bunks you need for the evacuees` | **avete dimenticato le <bunks> cuccette che vi servono per gli evacuati** | 31 | |
| `expected a beacon of some sort` | **vi aspettavate un qualche faro di segnalazione** | 32 | |
| `they are keeping radio silence` | **tacciono** | 32 | |
| `staring down a thermal rifle` | **vi trovate di fronte un fucile termico puntato** | 32 | |
| `keeps the weapon trained on you` | **tiene l'arma puntata su di voi** | 33 | |
| `makeshift hospital` | **ospedale di fortuna** | 34 | |
| `running on emergency power` | **vanno con l'energia di emergenza** | 34 | |
| `spaceworthy` | **in grado di volare nello spazio** | 34 | |
| `more than half are incapacitated or unconscious` | **più della metà è inabile o incosciente** | 34 | |
| `shows you his palms, and makes quick circles` | **vi mostra i palmi e traccia cerchi rapidi** | 35, 36 | gesto Korath coerente con L107 |

## 3. Nodi aperti (da non dedurre dopo)

1. **I frammenti si controllano sulla forma, non sul senso**: maiuscola nel soggetto, minuscola in verbo e oggetto,
   infinito in testa all'oggetto, `a ` iniziale e punto finale nella destinazione, maiuscola e punto nella frase
   finale. Se una revisione futura «abbellisce» un frammento con un punto o una maiuscola, rompe la composizione.
2. **Le 24 combinazioni sono verificate** (3 soggetti × 2 verbi × 4 oggetti): nessuna deve produrre `..`, doppie
   maiuscole o `di di`. È il controllo che sostituisce la prova a schermo, che non è stata fatta.
3. **`carry a box` ha superato il gate solo dopo due tentativi**: «trasportare una scatola» dava 2,09. Il gate
   **non si allarga**: si riscrive il frammento.
4. **`<EDC-ship>` è un nome proprio di nave**: non si traduce, non si spezza, e compare in tre `VALUE` identici.
5. **`<bunks>` è un numero** in tre unità (30, 31) e regge sia «i <bunks> superstiti» sia «le <bunks> cuccette».
6. **`Distress Call 2` è aperto**: 8 unità su 13 in questo lotto. Chi riprende non deve contare il contesto come
   chiuso.
7. **Due Quarg, due registri**: lo storpiato di L107 (unità 16 di quel lotto) e l'arcaico di qui. Non uniformare.
8. **`Two score` = 40**, e l'unità 19 dice già «40 superstiti» in cifre: i due numeri devono coincidere.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 36 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: nessuna di queste scene è stata vista a schermo, e **la composizione dei
  frammenti non è stata osservata nel runtime**.
- **Nessuna revisione umana**.
- **Il file non è completo**: 59 unità residue su 6 contesti.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (33 controlli), `verify.py` exit **0** (36 controlli) |
