# review.md — L328 (`data/_ui/help.txt`, righe 72–116)

Revisione del **testo approvato**: venticinque istruzioni sull'interfaccia, dal pannello della mappa alla gestione della flotta.

## 1. `map advanced`: la rotta che si disegna da sola

| inglese | approvato |
|---|---|
| `Clicking on a distant system will automatically plot the quickest route to it.` | **Cliccando su un sistema lontano verrà tracciata automaticamente la rotta più rapida.** |
| `You can Shift+click on systems to plot a route between them, or Control+click to select a system without setting a route to it.` | **Puoi usare Shift+clic sui sistemi per tracciare una rotta tra loro, oppure Control+clic per selezionare un sistema senza impostare una rotta.** |
| `There are many other useful modes the map can be set to.` | **Ci sono molte altre modalità utili.** |

`plot (a route)` → **«tracciare»**: è il verbo italiano della navigazione, e il testo lo usa in modo coerente in tutto il file. La
differenza fra `Shift+clic` (rotta **tra** due sistemi) e `Control+clic` (selezionare **senza** rotta) è resa **esplicita**: sono due
azioni diverse sul mouse, e confonderle renderebbe l'istruzione inutile.

## 2. `ports`: ogni clic ha un effetto

> `Clicking on the name of the system, the government of the system, the lines under the name of each planet, or any trade commodity will
> color the map differently, the key to which can be seen on the right side of the screen.`
> → **Cliccando sul nome del sistema, sul governo, sulle righe sotto il nome di ogni pianeta o su una merce, la mappa si colora in modo
> diverso; la legenda è sul lato destro dello schermo.**

`the key to which can be seen on the right side` → **«la legenda è sul lato destro»**: il testo inglese usa `key` nel senso di
**legenda** (chiave di lettura), e tradurlo «la chiave» avrebbe fatto pensare a un tasto. `government` → **«governo»**, non
«governatorato»: è la scheda politica del sistema.

E su questa riga compare **«fornitore»**: `outfitter` **non** è «emporio», come spiega il REPORT.

## 3. `shops`: categorie che si chiudono

> `Ships and outfits are displayed in categories which can be collapsed by clicking on the category name. Using Shift+click on a
> category name will collapse or uncollapse all the categories at once.`
> → **Sono raggruppati per categoria e puoi chiudere una categoria cliccandone il nome. Con Shift+clic sul nome di una categoria chiudi o
> apri tutte le categorie insieme.**

`collapse` → **«chiudere»** e `uncollapse` → **«aprire»**: l'alternativa («comprimere»/«espandere») sarebbe più tecnica e meno chiara in
un testo di aiuto. Il testo approvato sceglie la **lingua del giocatore**, non quella del programmatore.

## 4. `stars` e `danger`: due pannelli che spiegano la mappa

| inglese | approvato |
|---|---|
| `The stars present in a system affect the amount of solar power and solar wind available for use by solar collectors and ramscoops respectively.` | **Le stelle presenti in un sistema influenzano la quantità di energia solare e di vento solare disponibile rispettivamente per i pannelli solari e per i ramscoop.** |
| `Pirates raid some systems more frequently or in greater strength than others, and a poorly defended convoy risks attracting them in many systems.` | **I pirati attaccano alcuni sistemi più spesso o con forze maggiori, e un convoglio mal difeso rischia di attirarli in molti sistemi.** |
| `click on the alert icon next to the system name` | **clicca sull'icona di allarme accanto al nome del sistema** |

`respectively` è reso con **«rispettivamente»** e la corrispondenza è tenuta: energia solare → pannelli solari, vento solare → ramscoop.
`ramscoop` resta **`ramscoop`** (nome di equipaggiamento). `raids` → **«attaccano»**, non «razziano»: registro didattico.

## 5. `multiple ships`: la prima nave è l'ammiraglia

> `you can reorder the ships in your fleet by clicking and dragging them in the shipyard, outfitter, or player info panel, as long as you
> are landed. You will use the first ship in the list as your flagship.`
> → **puoi riordinarle nella flotta trascinandole nel cantiere, nel fornitore o nel pannello dati pilota, purché tu sia atterrato. La
> prima nave della lista sarà la tua ammiraglia.**

`flagship` → **«ammiraglia»**; `as long as you are landed` → **«purché tu sia atterrato»** (congiuntivo, non «finché sei atterrato»).
`"park" escorts` → **«"parcheggiare" le scorte»**, con le virgolette **conservate**: è un verbo usato in modo improprio, e le virgolette
lo segnalano.

## 6. `player info` e `fleet management`: due pannelli, quattro azioni

| inglese | approvato |
|---|---|
| `their net worth, combat rating, salary, and licenses` | **patrimonio netto, valutazione di combattimento, stipendio e licenze** |
| `Your pilot's logbook and current missions` | **Il diario del pilota e le missioni attive** |
| `The player info panel can be brought up at any time by pressing <View player info>, including mid-flight.` | **Il pannello dati pilota può essere aperto in qualsiasi momento premendo <View player info>, anche in volo.** |
| `To make this order permanent, press the "Save Order" button.` | **Per rendere l'ordine permanente, premi il pulsante "Salva ordine".** |
| `Parked ships will not launch or follow you, and do not require any crew salaries.` | **Le navi parcheggiate non partono e non ti seguono, e non richiedono stipendi per l'equipaggio.** |

`net worth` → **«patrimonio netto»** (termine contabile, non «valore netto»); `combat rating` → **«valutazione di combattimento»**;
`logbook` → **«diario»** (già usato nei lotti di missione come `LOGBOOK`).

## 7. `ship info`: trascinare le armi

> `While landed on a planet, you are able to change how guns and turrets are arranged by dragging the name of a weapon to another gun or
> turret location.`
> → **Mentre sei atterrato su un pianeta puoi cambiare la disposizione di cannoni e torrette trascinando il nome di un'arma su un altro
> punto di montaggio.**

`gun or turret location` → **«punto di montaggio»**: non «posizione», che confonderebbe con la posizione della nave. `jettison` →
**«espellere»**, e `individual pieces of cargo` → **«singole partite di carico»** (unità di carico, non «pezzi»).

## 8. `multiple ship controls`: il mouse come strumento di comando

| inglese | approvato |
|---|---|
| `Right-clicking on an empty point in space will order escorts to fly to and hold position at that point` | **Il clic destro su un punto vuoto dello spazio ordina alle scorte di volare lì e mantenere la posizione** |
| `while right-clicking on a hostile ship will order your escorts to focus fire on it` | **su una nave ostile ordina di concentrare il fuoco** |
| `Escorts can be saved into control groups by pressing Control+number key.` | **Le scorte possono essere salvate in gruppi di controllo premendo Control+tasto numerico.** |
| `The list of escort order keys can be found in the preferences panel.` | **L'elenco dei tasti di comando delle scorte è nel pannello delle preferenze.** |

`focus fire` → **«concentrare il fuoco»** (espressione militare italiana). `Control+number key` → **«Control+tasto numerico»**: la forma
inglese è ambigua, e la resa la rende esplicita senza cambiare il contenuto.

## 9. Struttura

| cosa | inglese | italiano |
|---|---|---|
| segnaposto | **1** | **1**, identico |
| virgolette | **10** (3 righe) | **10** |
| tab | **0** | **0** |
| contesti | **11** | **11** |
| apici | **3** | **3** |

## 10. Cosa resta aperto (dichiarato)

- **Il testo è approvato**: questa revisione **documenta** scelte altrui.
- **`outfitter`**: «fornitore» nel testo approvato, «emporio» in 53 unità dello staging — **divergenza dichiarata**, non uniformata.
- **Prossimo lotto — L329, l'ultimo del file, e il primo MISTO**: righe **119–212**, **60 unità**, **1.322 parole**, **15 contesti**,
  **6 tab** (124, 125, 126, 129, 130, 147), **38 virgolette**, **3 apici**, **12 forme di segnaposto**.
  **Stato misto**: **15 `APPROVED`** (da **trascrivere**) e **45 `PENDING`** (da **tradurre**). È il primo lotto del ciclo in cui i due
  trattamenti convivono, e il test dovrà verificarli **per gruppo**.
