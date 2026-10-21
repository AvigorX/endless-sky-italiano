# REVIEW — L221 · `successor ships.txt` (quarto lotto)

Coppie EN→IT rilette in `translation.json` (`b7a2199bbf3b9e42…`). Tutte le 24 unità sono **`PENDING`**.

## 1. Le 17 unità copiate

15 `TEXT` (`"Ryuit" Fusion Core`, `"Byiaa" Shield Cortex`, `3-"Kaska" Betavoltaic Cell`…) e 2 `VALUE` (`Stolsaqran`,
`Veusaden`), **generati dal sorgente** e verificati carattere per carattere.

## 2. Le tre formule condivise

| inglese | resa unica | unità |
|---|---|---|
| *sports a surprising amount of firepower for a ship of its size* | «sfoggia una potenza di fuoco sorprendente per una nave delle sue dimensioni» | 15, 17 |
| *plagued with power and propulsion issues* | «afflitto da problemi di energia e propulsione» | 15, 17 |
| *albeit with significantly downgraded systems compared to the military-exclusive model* | «anche se con sistemi notevolmente depotenziati rispetto al modello riservato ai militari» | 16, 17 |

Sono le stesse navi descritte due volte: se le formule divergono, il giocatore legge due specifiche diverse dello stesso
vascello. Verificate in **entrambe** le unità, in `check.py` e in `verify.py`.

## 3. Decisioni di resa

1. **`vessel of choice`** → «la nave che le Alte Case prediligono»: non «nave preferita», che è piatto.
2. **`less spacious than a dedicated civilian freighter`** → «meno spaziosa di un cargo o di un trasporto civile dedicato».
3. **`flexible internals`** → «interni flessibili» (in L220 `restrictive internals` era «interni poco flessibili»: la coppia
   resta coerente).
4. **`growing ubiquity`** → «crescente diffusione».
5. **`limited experience in making warships this small`** → «poca esperienza nella costruzione di navi da guerra così piccole».
6. **`either too large or not powerful enough`** → «troppo ingombrante o non abbastanza potente».
7. **`a challenge` / `a deathtrap`** → «una sfida» / «una trappola mortale»: l'ironia è nell'opposizione, non nelle parole.
8. **`the only purpose-built warship … made available to the general public`** → «l'unica nave da guerra progettata
   appositamente … a essere messa a disposizione del pubblico».
9. **`drag cannon`** → «cannone a trascinamento». Non è un nome di equipaggiamento nel database (verificato con una query:
   nessun `Drag` fra gli outfit), quindi si traduce come descrizione, e «trascinamento» tiene il legame con «effetti di
   rallentamento» già fissato in L220.
10. **`Blessed with the honor of being named with the Successor word for swiftness`** → «Onorata di portare il nome che
    nella lingua dei Successori significa rapidità»: `Veusade` resta, il significato si spiega.
11. **`earned renown … catching and killing ships many times their size`** → «si guadagnarono fama … raggiungendo e
    distruggendo navi molte volte più grandi».
12. **`auxiliary or police craft`** → «unità ausiliarie o di polizia»; **`intercept and immobilize fleeing ships`** →
    «intercettare e immobilizzare rapidamente le navi in fuga».

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 24 unità `PENDING`.
- **Nessuna nave vista nel gioco**: la resa di `drag cannon` è dedotta dal testo e dalla meccanica descritta (immobilizzare),
  non osservata in partita.
- **Nessuna revisione umana**, **nessuna correzione al sorgente**.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì |
| ESEGUITO | sì |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (28), `verify.py` exit **0** (18) |
