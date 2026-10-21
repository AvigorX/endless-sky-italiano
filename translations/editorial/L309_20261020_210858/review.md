# review.md — L309 (`data/avgi/avgi weapons.txt`, righe 716–969)

Registro delle decisioni editoriali del **lotto terminale** delle armi Avgi: tre munizioni e un magazzino.

## 1. Perché questo finale funziona

L307 e L308 nominavano le munizioni come **etichette** nei pannelli (`"Nettle" KKV`, `"Orchid" Nuclear Missile`,
`"Ophrys" Nuclear Torpedo`) senza spiegarle. Questo lotto **chiude il cerchio** e le descrive una per una, in ordine di
**crescendo tecnologico**:

| munizione | costo | effetto |
|---|---|---|
| **`Nettle`** | **economica**, produzione in serie | nuvola di barre di tungsteno: **anti-sciame**, non anti-nave |
| **`Orchid`** | **secoli di sviluppo** nucleare | testata termonucleare che **infrange gli scudi** degli `Aberrant` |
| **`Ophrys`** | **derivato** dell'`Orchid`, con corazzatura ablativa | un **drone** che minaccia una **nave capitale** |

## 2. «Non abbiamo tabù»: la differenza culturale

La 801 è la scheda più **politica** del file:

> «A differenza dell'umanità, gli Avgi **non hanno un forte tabù** contro l'uso di armi nucleari nello spazio… Sono state l'**asso
> nella manica** degli Avgi contro gli `Aberrant`…»

La resa conserva il **confronto implicito**: l'umanità ha rinunciato (802: «la lunga astensione dell'umanità dalla ricerca sulle
armi nucleari»), gli Avgi no. È un **giudizio sulla specie del giocatore**, e va lasciato leggibile.

## 3. Le tre variazioni di «ammunition for»

| riga | frase | contenitore |
|---|---|---|
| 717 | «Il Nettle KKV è munizione per il **Vertical Launch Array**…» | uno |
| 803 | «L'Orchid Missile è munizione per l'**External Launch Tube**…» | uno |
| 951 | «L'Ophrys Torpedo è munizione per l'**External Launch Rail** o un **Ophrys Stockpile**…» | **due** |

La terza ammette **due** contenitori: rendere tutte e tre con la stessa formula avrebbe **cancellato** quella differenza. Il test
verifica che ognuna citi il proprio contenitore.

Nota: la 951 dice **«an External Launch Rail or Ophrys Stockpile»** — due opzioni, e la resa le mantiene entrambe.

## 4. Refusi non riprodotti

| riga | inglese | italiano |
|---|---|---|
| 803 | `without **a External** Launch Tube` | «senza **un** External Launch Tube» |

L'articolo è sbagliato in inglese (`a` davanti a vocale). Non si copia: la regola è **tradurre il senso, non l'errore** (come per
`can altered` di L307, `Gypusm's` di L286, `Although is it lightly armed` di L287).

## 5. Scelte di resa

| inglese | resa |
|---|---|
| `a cheap, single-stage kinetic kill vehicle` | **un veicolo a impatto cinetico economico e a singolo stadio** |
| `Little more than a payload of tungsten rods` | **Poco più che un carico di barre di tungsteno** |
| `an octaazacubane thruster package` | **un pacchetto di propulsori a ottazacubano** |
| `the missile unwraps into dozens of thin tungsten rods` | **il missile si apre in dozzine di sottili barre di tungsteno** |
| `a cone-shaped area of effect` | **un'area di effetto a forma di cono** |
| `the cloud of projectiles is difficult to completely eliminate` | **la nuvola di proiettili è difficile da eliminare del tutto** |
| `a staged device with a far higher yield to weight ratio` | **un ordigno a più stadi con un rapporto resa-peso molto più alto** |
| `humanity's long abstention from nuclear weapons research` | **la lunga astensione dell'umanità dalla ricerca sulle armi nucleari** |
| `minimally-guided` | **a guida minima** |
| `a layer of ablative armor added to the front` | **uno strato di corazzatura ablativa aggiunto sul davanti** |
| `to pose a credible threat to a capital warship` | **rappresentare una minaccia credibile per una nave da guerra capitale** |
| `trading an independent propulsive capability for enough armor` | **barattando la capacità di propulsione autonoma con corazzatura sufficiente** |
| `during its terminal path` | **durante la corsa finale** |
| `A generous stockpile of torpedoes` | **Una scorta generosa di siluri** |
| `before needing to resupply` | **prima di dover essere rifornita** |
| `requires oversight by a small team of specialists` | **richiede la supervisione di una piccola squadra di specialisti** |

## 6. Struttura

| cosa | inglese | italiano |
|---|---|---|
| tab | **6** (717, 802, 803, 950, 951, 969) | **6** |
| virgolette | **4** (2 coppie) | **4** |
| segnaposto / alternative | **0 / 0** | **0 / 0** |
| apici | **3** | **17** |
| copiati (`TEXT` + `VALUE`) | **3** | **3**, verbatim |

## 7. Cosa resta aperto (dichiarato)

- **Nessuna approvazione**: 13 unità `PENDING`; **nessuna revisione umana**.
- **Il file è chiuso a 46/46** in staging: **ventinovesimo file completo**, **88** su 167.
- **Prossimo file**: `data/korath/korath culture conversations.txt` — righe **26–75**, **27 unità** (**24 `MISSION_TEXT` + 3
  `UI_LABEL`**), **1.295 parole**, **1 solo contesto** (una **conversazione**), **23 tab**, **14 virgolette**, **10 apici**. È
  l'**intero file**: sarà un **lotto terminale singolo**, con una **catena di battute** da tradurre come **un dialogo continuo**.
