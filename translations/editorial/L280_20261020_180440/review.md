# review.md — L280 (`data/human/kestrel.txt`, righe 252–402)

Registro delle decisioni editoriali dell'**ultimo lotto** del file della Kestrel: il messaggio di ricompensa e la scheda della
nave.

## 1. Le due code della missione

La missione comincia in un bar (L278), passa per il collaudo e la scelta del nome (L279) e finisce **lontano dallo
spazioporto**: con un **messaggio** che arriva quando la nave è in vendita, e con la **scheda** che il giocatore legge nel
cantiere. Due testi con **due destinatari** diversi — il pilota e il compratore — e un solo **motivo** da mantenere coerente.

## 2. Scelte

| inglese | resa |
|---|---|
| `You receive a message from Charles Atinoda, the ship designer at Tarazed Corporation` | **Ricevi un messaggio da Charles Atinoda, il progettista di navi della Tarazed Corporation** |
| `we are pleased to inform you that our latest warship is now available for sale here on Wayfarer` | **siamo lieti di informarti che la nostra ultima nave da guerra è ora in vendita qui su Wayfarer** |
| `We've taken all your feedback into account in the final design` | **Abbiamo tenuto conto di tutti i tuoi commenti nel progetto finale** |
| `while visiting a sweat lodge in search of spiritual renewal` | **mentre visitava una capanna del sudore in cerca di rinnovamento spirituale** |
| `fell into a trance and journeyed to a reality separate from our own` | **cadde in trance e viaggiò in una realtà separata dalla nostra** |
| `visions of a strange and elegant starship` | **le visioni di un'astronave strana ed elegante** |
| `with renewed purpose` | **con rinnovato proposito** |
| `he spent the next seven years making the Kestrel a reality` | **passò i sette anni successivi a rendere reale la Kestrel** |

Il messaggio usa il **«tu»** («ti informiamo», «i tuoi commenti»), coerente con il registro fissato in L278–L279.

## 3. La scheda racconta la stessa scena del dialogo

| elemento | L278 (dialogo) | L280 (scheda) |
|---|---|---|
| il luogo | «una ricerca di visione nella loro **capanna del sudore**» | «mentre visitava una **capanna del sudore**» |
| lo stato | «Caddi in **trance**» | «cadde in **trance**» |
| la nave | «una nave scura, più aggraziata ed elegante» | «le **visioni** di un'astronave strana ed elegante» |

Tre forme identiche, verificate dal `check.py` **rileggendo** `L278/translation.json`. È il tipo di coerenza che nessun
controllo di lunghezza o di struttura può garantire: serve il confronto con il testo che l'ha raccontata prima.

## 4. `'Kestrel'` e i nomi

`Kestrel`, `Tarazed`, `Wayfarer`, `Charles Atinoda` restano **invariati**. Il segnaposto `<last>` resta al suo posto
(«Capitano `<last>`»), e le due virgolette del discorso citato sono **dritte**.

## 5. Struttura

| cosa | inglese | italiano |
|---|---|---|
| tab | **0** | **0** |
| virgolette | **2** | **2**, dritte |
| apici | **2** (`We've`, `Tarazed's`) | **1** (`un'astronave`) |
| segnaposto | **1** (`<last>`) | **1** |

## 6. Chiusura del file

`data/human/kestrel.txt` è **51/51** in staging: tre lotti (L278 16, L279 33, L280 2), righe 15–402, tutte `PENDING`.

Cosa **non** significa: non è approvato, non è stato visto nel gioco, non è stato revisionato da una persona. Significa che in
staging **non manca nessuna unità** del file — e `verify.py` lo dimostra sommando i tre lotti, contando le righe distinte e
verificando che dopo la 402 non ci sia nulla.

## 7. Cosa resta aperto (dichiarato)

- **Nessuna approvazione**: 2 unità `PENDING` (e 49 nei due lotti precedenti).
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Prossimo file**: `data/quarg/quarg news.txt` — **43 unità** nella prima finestra, **10 contesti** `news:`, 44 virgolette,
  5 apici, nessun tab e nessun segnaposto (L281).
