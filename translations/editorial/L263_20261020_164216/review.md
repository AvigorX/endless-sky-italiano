# review.md — L263 (`data/remnant/remnant jobs.txt`, righe 491–682)

Registro delle decisioni editoriali del **terzo lotto**: sei missioni di soccorso, tutte nella regione dei Remnant, con la
nave dispersa come filo conduttore.

## 1. La struttura del lotto

Sei missioni in tre coppie: `Rescue 2`/`2B`, `Rescue 3`/`3B`, `Rescue 4`, `Rescue 5` (che si apre qui e continua fuori dal
lotto). La **A** è il soccorso riuscito, la **B** il ramo in cui la nave **è distrutta**: la stessa `DESCRIPTION`, e poi il
testo del lutto.

| momento | inglese | resa |
|---|---|---|
| scheda (2/2B) | `The <npc> has gone missing during a tech retrieval mission in the Ember Waste.` | «La `<npc>` **è scomparsa** durante una missione di **recupero tecnologico** nell'Ember Waste.» |
| scheda (3/3B) | `…during a supply run…` | «…durante una missione di **rifornimento**…» |
| ritorno a vuoto | `You have returned, yet the <npc> is still missing.` | «Sei tornato, ma la `<npc>` **risulta ancora dispersa**.» |
| lutto | `The <npc> has been destroyed. You frantically spend the next few hours searching for survivors…` | «La `<npc>` **è stata distrutta**. Passi le ore successive a cercare **affannosamente** superstiti…» |
| lutto | `…report that the <npc> was lost with all hands.` | «…riferisci che la `<npc>` **è andata perduta con tutto l'equipaggio**.» |

## 2. `<npc>`: una nave, quindi femminile

Diciassette occorrenze, e **nessuna** può essere neutra: l'italiano obbliga a scegliere. La scelta è **nave = femminile**,
coerente con «la nave Korath» dei lotti precedenti:

- «**la** `<npc>`», «**della** `<npc>`»;
- «è **scomparsa**», «è stata **distrutta**», «è **andata perduta**», «risulta ancora **dispersa**», «**sana e salva**»;
- «**Trovala** e **aiutala**», «per trovarla e aiutar**la**».

I due script vietano le forme maschili: un «scomparso» riferito a `<npc>` sarebbe il tipo di errore che nessun conteggio di
segnaposto intercetta.

## 3. I luoghi

| inglese | resa | perché |
|---|---|---|
| `the Graveyard` | **il Cimitero** | il corpus lo traduce così in **48** unità su 51 |
| `Terminus` | **Terminus** | nome proprio di sistema |
| `Ember Waste` | **`Ember Waste`** | **per contratto**, benché il corpus usi «Distesa di Braci» in 69 unità — divergenza dichiarata, non sanata qui |

## 4. Il lessico del soccorso e del disastro

| inglese | resa |
|---|---|
| `a resource allocation of <payment>` | **un'assegnazione di risorse di `<payment>`** |
| `along with a brief note of thanks` | **insieme a un breve biglietto di ringraziamento** |
| `and also a thank you from the captain of the <npc>` | **e anche un ringraziamento dal capitano della `<npc>`** |
| `a distress signal` | **un segnale di soccorso** |
| `follow the telemetry data` | **segui i dati di telemetria** |
| `help return them safely` | **aiutala a tornare sana e salva** |
| `May the Embers burn bright for you.` | **«Che le Braci ardano luminose per te.»** |
| `has stopped reporting in` | **ha smesso di dare notizie** |
| `was lost with all hands` | **è andata perduta con tutto l'equipaggio** |
| `your hope sinking with every passing minute` | **con la speranza che affonda minuto dopo minuto** |

`Embers` con la maiuscola, e **«Braci»** in italiano: è il modo in cui i Remnant chiamano la loro regione, e la frase del
capitano è un **congedo rituale**, non una descrizione del tempo.

## 5. La voce

Le `MISSION_TEXT` sono **prosa di diario in seconda persona** («entri», «passi», «atterri», «riferisci»), e il lotto tiene
questo registro: nessun «noi», nessun passato remoto. Il ramo del lutto resta **sobrio**: l'emozione è nei fatti
(«affannosamente», «con il cuore pesante»), non negli aggettivi.

## 6. Struttura

| cosa | inglese | italiano |
|---|---|---|
| tab | **1** (unità 21) | **1**, primo carattere |
| virgolette | **2** (unità 20) | **2** |
| apici | **0** | **13** su 11 unità (elisioni: `nell'`, `Un'`, `l'`, `un'`) |
| segnaposto | 28 | 28, ordine per unità identico |

## 7. Cosa resta aperto (dichiarato)

- **Nessuna approvazione**: 24 unità `PENDING`.
- **Nessun testo visto nel gioco**.
- **Nessuna revisione umana**.
- **Divergenza `Ember Waste` / «Distesa di Braci»**: 69 contro 16 unità nel corpus, da decidere in una passata globale
  autorizzata, non dentro un lotto.
- **Il file è a 78/87**: L264 chiude le ultime 9 unità (`Rescue 5` coda e `Disable 1`).
