# review.md — L322 (`data/human/frontier jobs.txt`, righe 16–318)

Registro delle decisioni editoriali del primo lotto a **cinque tipi**: sei lavori di frontiera e un casinò.

## 1. I lavori: tre coppie di ripetizioni e due eccezioni

| contesto | unità | struttura |
|---|---|---|
| `Frontier delivery [0/1/2]` | 6 | **tre volte lo stesso testo**: `Deliver <cargo> to the frontier world of <destination>…` |
| `Frontier Emigration [0/1/2]` | 6 | **tre volte lo stesso testo**: `These <bunks> passengers have finally saved up…` |
| `Disaster Relief` | 3 | descrizione + **dialogo** di consegna |
| `Instruct Novice Pilot` | 4 | descrizione + **tre dialoghi**, uno dei quali è un **ammonimento** |
| `Small Pirate gambling` | 26 | il casinò |

Le ripetizioni sono **del sorgente** e la resa le riproduce **identiche**: sei unità con due testi, non sei testi diversi. Se le avessi
variate per «eleganza», il giocatore che prende tre consegne uguali leggerebbe tre descrizioni diverse — un'incongruenza che il test
avrebbe dovuto **impedire** e che invece avrei introdotto io.

## 2. Le tre scelte di registro

**Consegne** — imperativo diretto, come il briefing di un datore di lavoro:

> «**Consegna** `<cargo>` al mondo di frontiera `<destination>`. I sistemi di frontiera hanno un alto tasso di pirateria, quindi
> **preparati a difenderti**. Il pagamento è di `<payment>`.»

**Emigrazioni** — terza persona, come una scheda:

> «**Questi** `<bunks>` **passeggeri** hanno finalmente messo da parte abbastanza denaro…»

**Casinò** — seconda persona narrativa, al presente:

> «**Stai bevendo** qualcosa in un bar dello spazioporto in penombra quando **noti** un gruppo di giovani…»

Tre registri in un file solo, e **ognuno va tenuto**: il briefing è **imperativo**, la scheda passeggeri è **descrittiva**, il casinò è
**narrativo**. Il test non controlla il registro (sarebbe fragile), ma la **struttura**: chi traduce deve vedere che sono tre cose
diverse.

## 3. Il dialogo più lungo: il giro dello spazioporto

La riga 208 è **didattica** e **comica** insieme:

> «Dopo un atterraggio morbido, guidi il tuo allievo attraverso una parte particolarmente malfamata dello spazioporto, piena di
> **rifiuti, vagabondi senza casa e vicoli poco illuminati**. Gli spieghi i trucchi per evitare i **borseggiatori**, per tenersi fuori
> dalle **risse nei bar** e per riconoscere un **affare losco** nell'emporio di un fornitore.»

Tre infiniti in serie nell'inglese (`avoiding`, `keeping out`, `how to spot`), tre infiniti in italiano. `outfitter's shop` →
**«emporio di un fornitore»**: la parola `outfitter` è resa **sempre** con «emporio» nel progetto, e qui il genitivo inglese chiede un
secondo termine per non dire «l'emporio di un emporio».

## 4. Le sei etichette di salto

```
good luck   bad luck   shoot and die   shoot and run   grab and die   grab and run
```

**Copiate**. Non sono testo per il giocatore: sono i **bersagli** dei `goto` della conversazione. Tradurle avrebbe rotto sei salti su
sei, e il gioco avrebbe mostrato una conversazione che si **ferma**. È il caso in cui «tradurre tutto» sarebbe stato un **errore
grave**, e in cui il tipo (`UI_LABEL`) è l'unica avvertenza disponibile.

## 5. I quattro finali

| scelta | finale «male» | finale «bene» |
|---|---|---|
| **spara per primo** | 296: «il tuo corpo straziato cade a terra con un tonfo sordo» | 302–303: **due pirati abbattuti**, fuga con i crediti, e i due rimasti che **insultano via radio** |
| **prendi la posta** | 311: ferito, «una pozza del tuo stesso sangue», finito con un colpo | 317–318: fuga a zigzag, il **barista** che riduce un teppista «a carne trita» con un fucile a canne mozze, e le **autorità** che avvisano |

La simmetria è **del sorgente**: due scelte, due esiti, quattro testi. La resa la conserva, e il test verifica che i due finali «bene»
**condividano l'esordio** e **divergano** dopo — cioè che la simmetria sia **strutturale** e non solo tematica.

Il dettaglio più brutale del lotto — `reduce one of the ruffians to hamburger meat` → «ridurre uno dei teppisti a **carne trita**» — è
**volgare di proposito**, e ammorbidirlo avrebbe cambiato il tono della scena.

## 6. Scelte di resa

| inglese | resa |
|---|---|
| `Deliver <cargo> to the frontier world of <destination>` | **Consegna `<cargo>` al mondo di frontiera `<destination>`** |
| `have a high rate of piracy` | **hanno un alto tasso di pirateria** |
| `prepare to defend yourself` | **preparati a difenderti** |
| `have finally saved up enough money to start a new life` | **hanno finalmente messo da parte abbastanza denaro per iniziare una nuova vita** |
| `are willing to pay you <payment> to transport them` | **sono disposti a pagarti `<payment>` per trasportarli** |
| `A disaster has occurred in a colony` | **Una catastrofe ha colpito una colonia** |
| `Deliver <cargo> to the planet by <date>` | **Consegna `<cargo>` sul pianeta entro `<date>`** |
| `drop off your cargo of <commodity> and collect your payment` | **Scarichi il tuo carico di `<commodity>` e ritiri il pagamento** |
| `bid you farewell` | **ti saluta** |
| `a novice pilot seeks instruction from an experienced captain` | **Un pilota alle prime armi cerca istruzione da un capitano esperto** |
| `requests an escort to <stopovers>` | **chiede di essere scortato fino a `<stopovers>`** |
| `you guide your student through an especially rough part of the spaceport` | **guidi il tuo allievo attraverso una parte particolarmente malfamata dello spazioporto** |
| `homeless drifters` | **vagabondi senza casa** |
| `poorly-lit alleyways` | **vicoli poco illuminati** |
| `the ins and outs of avoiding pickpockets` | **i trucchi per evitare i borseggiatori** |
| `a lousy deal` | **un affare losco** |
| `one of the seedier parts of the galaxy` | **una delle zone più squallide della galassia** |
| `in crimson leather outfits` | **in tute di pelle cremisi** |
| `neither of them looks older than 19` | **nessuno di loro sembra avere più di 19 anni** |
| `sport fearsome tattoos and dangerous-looking sidearms` | **sfoggiano tatuaggi impressionanti e armi corte dall'aria pericolosa** |
| `they're cheating, and making little effort to hide this` | **stanno barando, e che si sforzano poco di nascondertelo** |
| `you're starting to bleed money` | **Cominci a perdere soldi a vista** |
| `gloat over their "winnings"` | **si godono le loro "vincite"** |
| `the meanest-looking one growls at you` | **il più cattivo del gruppo ti ringhia** |
| `You'd better shut your big mouth if you know what's good for you!` | **Meglio che chiudi quella boccaccia, se sai cosa ti conviene!** |
| `We can make this ugly real fast` | **Possiamo renderla brutta molto in fretta** |
| `(Let them fleece me.)` | **(Lascia che mi spennino.)** |
| `your mutilated corpse hits the floor with a wet thump` | **il tuo corpo straziato cade a terra con un tonfo sordo** |
| `your hand flies toward the pistol at your thigh` | **la mano ti scatta verso la pistola alla coscia** |
| `reduce one of the ruffians to hamburger meat` | **ridurre uno dei teppisti a carne trita** |
| `blast off in a hurry` | **decolli in fretta** |
| `count your spoils` | **conti il bottino** |
| `hurl obscenities over the comms` | **ti urlano insulti via radio** |

## 7. Struttura

| cosa | inglese | italiano |
|---|---|---|
| tab | **19** | **19** |
| virgolette | **4** (277, 281) | **4** |
| segnaposto | **10 tipi** | **10** identici |
| alternative | **0** | **0** |
| apici | **18** (12 unità) | **13** |

## 8. Cosa resta aperto (dichiarato)

- **Nessuna approvazione**: 45 unità `PENDING`; **nessuna revisione umana**.
- **Il file è chiuso a 45/45** in staging: **trentaseiesimo file completo**, **95** su 167.
- **Prossimo file**: `data/rulei/rulei.txt` — **l'INTERO file** (41 unità, 919 parole, righe 38–157, **5 contesti**), **38
  `MISSION_TEXT` + 3 `LOGBOOK`**: prima occorrenza del tipo `LOGBOOK` in un lotto. **32 tab**, **34 virgolette** (in 16 unità, con
  **151 che ne ha quattro**), **12 apici**, **0 segnaposto**. È la storia dei `Rulei` e del **vuoto** a est del nucleo.
