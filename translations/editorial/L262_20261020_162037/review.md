# review.md — L262 (`data/remnant/remnant jobs.txt`, righe 226–490)

Registro delle decisioni editoriali del **secondo lotto** dei lavori Remnant: la quinta taglia Korath, quattro linee
logistiche e l'inizio della sottotrama del soccorso.

## 1. Che cosa si è ripreso e che cosa si è scritto

| provenienza | unità | regola |
|---|---|---|
| **L261**, alla lettera | **2** (1, 2) | stessa stringa inglese → stessa resa, verificata rileggendo il file di L261 |
| **nuovo** | **19** | schede, battute e `MISSION_TEXT` mai viste |
| **copiato** (`VALUE`) | **8** | nomi dei lavori: dati |

## 2. La quinta taglia: `Bounty 5`

| inglese | resa |
|---|---|
| `Destroy Ground Assault Bounty` | **copiato** |
| `A Korath ship is hunting for our outposts in the Ember Waste.` | «Una nave Korath sta dando la caccia ai nostri **avamposti** nell'**Ember Waste**.» |
| `Track it down, eliminate it and any fighters it is carrying` | «Individuala, eliminala insieme ai **caccia** che porta con sé» |
| `You have destroyed the Korath ship and its fighters.` | «Hai distrutto la nave Korath e i suoi caccia.» |
| `…but the Korath ship and its fighters have not all been eliminated. Hunt them down and destroy them before returning.` | «…ma la nave Korath e i suoi caccia non sono stati eliminati tutti. **Dagli** la caccia e distruggili prima di tornare.» |

Il clitico cambia con il numero: **«Dalle»** per la nave sola (L261, unità della scheda), **«Dagli»** quando il soggetto è
«la nave e i suoi caccia». È lo stesso verbo, ma l'accordo non si copia.

`fighters` → **«caccia»**: nel gioco sono le navi imbarcate, e il corpus usa «caccia» in `tooltips.txt` («il numero di navi
della categoria "Caccia" che questa nave può trasportare»).

## 3. Le quattro linee logistiche

| linea | soggetto inglese | soggetto italiano | resa del pagamento |
|---|---|---|---|
| Civil | `Engineers on <planet> need <cargo> delivered.` | «Gli **ingegneri** su `<planet>` hanno bisogno di una consegna di `<cargo>`.» | «Il **compenso logistico** è `<payment>`.» |
| Industrial | `Project teams …` | «Le **squadre di progetto** …» | idem |
| Outfitter | `Outfitter repair crews …` | «Le **squadre di riparazione dell'emporio** … pezzi `<cargo>`» | idem |
| Salvage | `Deliver <cargo> components from recent salvage operations to the outfitters on <planet> for research, refurbishment, or recycling.` | «Consegna i **componenti `<cargo>` delle recenti operazioni di recupero agli empori** su `<planet>`, per studio, ripristino o riciclaggio.» | idem |

`Logistics adjustment` non è «aggiustamento» né «adeguamento»: nel gioco è la **quota** che ti spetta, e la resa è
**«compenso logistico»**, dichiarata qui e da usare in tutto il file.

`outfitter` → **«emporio»**: è la parola che il giocatore vede nel pannello di gioco (`tooltips.txt`: «Acquista
dall'emporio…»). «Fornitore» sarebbe corretto in astratto e sbagliato nel contesto dell'interfaccia.

## 4. La sottotrama del soccorso

| missione | inglese | resa |
|---|---|---|
| `Rescue` / `Rescue 1B` | `The <npc> has gone missing during a scouting mission in the Ember Waste. Find them and help them return to <destination>.` | «La `<npc>` è **scomparsa** durante una missione di **ricognizione** nell'Ember Waste. **Trovala** e **aiutala** a tornare su `<destination>`.» |
| `Rescue 2` (inizio) | `…during a tech retrieval mission…` | «…durante una missione di **recupero tecnologico**…» |
| ritorno a vuoto | `You have returned, yet the <npc> is still missing.` | «Sei tornato, ma la `<npc>` **risulta ancora dispersa**.» |
| notifica | `Your communicator notifies you of a resource allocation of <payment>.` | «Il tuo comunicatore ti notifica un'**assegnazione di risorse** di `<payment>`.» |
| lutto (`1B`) | `The <npc> has been destroyed.` | «La `<npc>` **è stata distrutta**.» |
| lutto (`1B`) | `…report that the <npc> was lost with all hands.` | «…riferisci che la `<npc>` **è andata perduta con tutto l'equipaggio**.» |

`<npc>` è una **nave**: il femminile è obbligatorio («scomparsa», «trovala», «aiutala», «dispersa», «distrutta»). È il
segnaposto più frequente del lotto (8 volte) e l'unico che impone la concordanza.

## 5. Struttura

| cosa | inglese | italiano |
|---|---|---|
| tab | **0** | **0** |
| virgolette | **0** | **0** |
| apici | **1** (`You've`) | **8** su 7 unità (`l'Ember`, `un'assegnazione`, `Un'analisi`, `l'equipaggio`…) |
| segnaposto | **43** | **43**, ordine per unità identico |

Il file non usa virgolette anche dove ci sarebbero battute: le `MISSION_TEXT` del soccorso sono **prosa di diario**, non
dialogo, e non vanno trattate come tale.

## 6. Cosa resta aperto (dichiarato)

- **Nessuna approvazione**: 29 unità `PENDING`.
- **Nessun testo visto nel gioco**.
- **Nessuna revisione umana**.
- **Il file è a 54/87**: restano 33 unità, da `Rescue 2` in poi.
