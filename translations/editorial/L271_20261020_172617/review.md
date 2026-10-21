# review.md — L271 (`data/dialog phrases.txt`, righe 16–98)

Registro delle decisioni editoriali del **primo lotto** delle frasi generiche: le risposte che il gioco dà quando una
missione **non** si chiude come il giocatore sperava.

## 1. Che cosa sono queste stringhe

Non sono dialoghi di personaggi: sono **messaggi di sistema** con il tono del pilota. Il giocatore arriva su un pianeta e
sente: «hai raggiunto il pianeta, ma hai lasciato indietro la nave che dovevi scortare», «non hai ancora visitato tutte le
tappe». Il testo deve essere **chiaro e breve**, e soprattutto **coerente fra le varianti**: la stessa formula per lo stesso
caso.

## 2. Formule fisse, verificate come conteggi

| formula | inglese | italiano | occorrenze |
|---|---|---|---|
| apertura | `You have reached <planet>, but …` | **«Hai raggiunto <planet>, ma …»** | **13** |
| consiglio | `Better depart and wait for …` | **«Meglio ripartire e aspettare che …»** | **6** |
| pagamento | `collect your payment of <payment>` | **«incassi il pagamento di <payment>»** | **4** |
| mancanza | `you're missing something! Either … or …` | **«ti manca qualcosa! O …, oppure …»** | **7** |

Il `check.py` conta le occorrenze: se una sola variante avesse cambiato formula, sarebbe rosso. È il tipo di coerenza che si
perde quando ogni frase viene tradotta «bene» ma isolata.

## 3. Scelte

| inglese | resa |
|---|---|
| `you left the <npc> behind` | **hai lasciato indietro <npc>** |
| `wait for them to arrive in this star system` | **aspettare che arrivi in questo sistema stellare** |
| `The captain of the <npc> thanks you for escorting them safely` | **Il capitano di <npc> ti ringrazia per aver scortato la nave sana e salva** |
| `you're missing something! Either you haven't visited <stopovers>, or …` | **ti manca qualcosa! O non hai visitato <stopovers>, oppure …** |
| `you haven't passed through <waypoints>` | **non hai attraversato <waypoints>** |
| `Better depart and make sure you visit <stopovers>` | **Meglio ripartire e assicurarti di visitare <stopovers>** |
| `not all of the cargo is in the system` | **non tutto il carico è nel sistema** |
| `you are not carrying <amount> tons of <mineral> in your cargo hold` | **non hai le <amount> tonnellate di <mineral> nella stiva** |
| `a message of gratitude` | **un messaggio di ringraziamento** |

`tons` → **tonnellate** (già nel corpus); `cargo hold` → **stiva**; `escorts` → **scorte**.

## 4. Il phrase composto: 12 frasi da 6 blocchi

Il `phrase "generic pirate attack payment dialog"` è una **frase componibile**. Il testo italiano deve restare grammaticale in
**tutte** le combinazioni, non solo in quella che sembra più naturale:

```
"Il governo di <planet>" · [" " | " ti ringrazia sentitamente e "] · "ti paga <payment> per aver contribuito a"
                        · [" cacciare " | " sconfiggere "] · "i " · ["pirati." | "predoni." | "razziatori."]
```

Tre decisioni strutturali:

1. **lo spazio finale** del blocco ringraziamento è necessario: senza, la variante che lo usa si attaccherebbe al blocco
   successivo («e ti paga» richiede lo spazio prima di «ti»);
2. **l'articolo `i`** è condiviso dai tre sostantivi, quindi **«razziatori»** e non «aggressori» (che vorrebbe `gli`);
3. **la seconda variante del modo** è « sconfiggere » con gli **spazi su entrambi i lati**, come in inglese, perché è un
   frammento inserito fra «contribuito a» e «i pirati».

## 5. `<npc>`: una nave, quindi femminile

Unità 29: «**<npc> è stata eliminata**. Poco dopo il governo di <planet> ti invia <payment> insieme a un messaggio di
ringraziamento.» L'accordo al femminile è coerente con la regola già applicata in `remnant jobs.txt` (17 occorrenze).

## 6. Struttura

| cosa | inglese | italiano |
|---|---|---|
| tab / virgolette | **0 / 0** | **0 / 0** |
| apici | **17** (`you're`, `haven't`, `You've`) | **0** (nessuna elisione necessaria) |
| spazi finali | nei frammenti | nei frammenti **4, 6, 7, 8**, per costruzione |
| segnaposto | **45** in 10 famiglie | **45**, stesse famiglie, **per unità** |

## 7. Cosa resta aperto (dichiarato)

- **Nessuna approvazione**: 29 unità `PENDING`.
- **Nessun testo visto nel gioco**: le 12 combinazioni sono verificate **componendo le stringhe**, non a schermo.
- **Lacuna dell'estrattore dichiarata**: il frammento di **solo spazio** alla riga 24 non è nel database, quindi non è
  traducibile e resta com'è.
- **Il file è a 29/54**: L272 chiude `dialog phrases.txt` (righe 102–172).
