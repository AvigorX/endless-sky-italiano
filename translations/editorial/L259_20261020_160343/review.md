# review.md — L259 (`data/human/post-war reactions.txt`, righe 222–250)

Registro delle decisioni editoriali del **quarto lotto**: Gus e il capitano, il fratello, la scuola, il Sindacato e la
guerra raccontata da un ragazzo di dodici anni.

## 1. Le due voci

| voce | registro | esempi |
|---|---|---|
| **Gus** (1–3, 7–10, 15) | **entusiasta, semplice, con parole grosse ripetute male** | «Ci scommetto!», «Uau», «Dev'essere fantastico!», «i Pug cattivi e malvagi» |
| **il capitano** (4–6, 11–14) | **breve, asciutto, a tratti duro** | «Sì, sono il capitano `<first>` `<last>`.», «La guerra è un inferno, ragazzo.» |

Il contrasto è il punto della scena: il ragazzo sogna la guerra, il veterano la racconta. Le battute del capitano sono di
**poche parole in inglese** e questo alza il rapporto (unità 6: 1,53), ma accorciarle oltre toglierebbe l'enfasi del «io».

## 2. Le istituzioni del Sindacato

Il contratto di L259 lasciava aperta la scelta: tradurre o lasciare in inglese i nomi degli organismi. **Scelta: tradurre**,
perché sono **nomi comuni** («servizio», «dispositivo»), non nomi propri di persona o di luogo, e il lettore italiano li
capisce senza glossa:

| inglese | resa |
|---|---|
| `the Syndicate's Ancillary Security Service` | **il Servizio di Sicurezza Ausiliario del Sindacato** |
| `Syndicate Childcare Device` (etichetta su un tablet) | **Dispositivo per l'Infanzia del Sindacato** |
| `the Syndicate` | **il Sindacato** (come in tutti i lotti) |

Restano **invariati**: `Pug`, `Maker` (pianeta), `Gus`, `Captain` → «capitano».

## 3. Scelte puntuali

| inglese | resa | nota |
|---|---|---|
| `a private, third class` | **un soldato semplice di terza classe** | grado reso, non traslitterato |
| `clearly having practiced that delivery` | **si vede che ha provato quella battuta** | |
| `got a break for the repair shop` | **si siano presi una pausa dall'officina** | |
| `In return they give us better schooling, nicer housing, and doctor's visits` | **In cambio ci dà una scuola migliore, una casa più bella e le visite mediche** | il «noi» del Sindacato diventa «dà» impersonale: in italiano «ci danno» sarebbe stato ambiguo |
| `He puffs himself up.` | **Si gonfia di orgoglio.** | |
| `big dangerous equipment` | **macchinari grandi e pericolosi** | |
| `big edu-screen` | **grande schermo didattico** | |
| `I blew up my share of Pug ships.` | **Ho fatto saltare la mia parte di navi Pug.** | |
| `War is hell, kid.` | **La guerra è un inferno, ragazzo.** | |
| `Their 'war' was a ploy` | **La loro 'guerra' era un trucco** | apici semplici conservati: la parola è fra virgolette **nel testo** |
| `A lot of Pug gave their lives willingly` | **Molti Pug hanno dato la vita di buon grado** | |
| `the most exhilarating feeling I've ever felt` | **la sensazione più esaltante che abbia mai provato** | |
| `Like one of those sensible experts in the vids!` | **Come uno di quegli esperti assennati dei video!** | `vids` → «video» |
| `I still reckon you were the best` | **Resta il fatto che sei stato il migliore** | `reckon` reso con una perifrasi, non con «credo» |

## 4. La citazione non chiusa (unità 2)

`… Only the cleverest of us get to do it. … Just ordinary stuff, like hammers, soldering irons, or sewing machines.`

Cinque virgolette: due coppie chiuse, l'ultima aperta e **mai chiusa**. La resa italiana ne ha cinque e finisce in
«macchine da cucire.». **Terzo caso** del file (L257 u12, L258 u5, L259 u2): è una forma del sorgente, non un errore da
riparare.

## 5. Le unità 7 e 8

Due rami della **stessa** scena, dove il tablet riconosce il capitano. Cambia **una** battuta:

| unità | battuta | resto |
|---|---|---|
| 7 | «Sei il capitano `<first>` `<last>`! Wow!» | identico |
| 8 | «Hai guidato tu l'attacco! Wow!» | identico |

Il `check.py` verifica testa, coda e la battuta diversa; il `verify.py` lo ripete in forma indipendente. Senza questi
controlli, una resa «unificata» passerebbe tutti i conteggi.

## 6. Struttura

| cosa | inglese | italiano |
|---|---|---|
| tab | **15** (tutte) | **15** |
| virgolette | **45** | **45**, per unità identiche |
| apici | **19** su 10 unità | **17** su 8 unità |
| segnaposto | 2 + 2 | 2 + 2, ordine identico |

Gli apici italiani sono **quasi** tanti quanti gli inglesi per la prima volta nel file: le elisioni (`dell'aria`,
`l'etichetta`, `d'allarme`, `l'attacco`, `Dev'essere`, `Com'era`, `d'autodistruzione`) compensano le contrazioni perse.

## 7. Cosa resta aperto (dichiarato)

- **Nessuna approvazione**: 15 unità `PENDING`.
- **Nessun testo visto nel gioco**.
- **Nessuna revisione umana**.
- **Il file è a 80/87**: L260 è **terminale** (righe 253–264, 7 unità) e chiuderà il file a **87/87**.
