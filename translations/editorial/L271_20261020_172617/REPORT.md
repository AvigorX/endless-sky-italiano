# REPORT — L271 (`data/dialog phrases.txt`, righe 16–98)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **27 controlli**; `verify.py` esce 0 con **20 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 29 (tutte `TEXT`) | 29 |
| parole | 430 | **400** (0,93) |
| contesti | 20 | 20 |
| segnaposto | 45 in 10 famiglie | **45 in 10 famiglie** |
| tab / virgolette | 0 / 0 | 0 / 0 |
| apici | 17 | 0 |

Le 20 **frasi** stanno nel gate **0,83 – 1,11**; i **frammenti** 4 (2,417) e 8 (0,50) sono fuori gate **per costruzione**
(sono pezzi di frase, non frasi) e l'eccezione è misurata e dichiarata.

## 2. Il lotto

Frasi **amministrative** che il gioco mostra quando la missione non si chiude come previsto:

| gruppo | frasi |
|---|---|
| **arrivo senza la nave scorta** | «Hai raggiunto <planet>, ma hai lasciato indietro <npc>!» |
| **scorta riuscita** | il capitano ringrazia e paga |
| **pagamento dei pirati** | 9 **frammenti** composti in 12 varianti |
| **consegne** | carico, passeggeri, minerali (con pagamento) |
| **carico/passeggeri non ancora nel sistema** | 3 varianti (carico, passeggeri, entrambi) |
| **qualcosa manca** | 7 varianti: tappa o scorta, tappa o carico, punto di passaggio o carico… |
| **tappe e punti di passaggio** | «non hai ancora visitato tutti i pianeti / sistemi» |
| **taglia eliminata** | «<npc> è stata eliminata… il governo di <planet> ti invia <payment>» |

Il registro è quello del **pilota che parla al giocatore**: seconda persona singolare, frasi brevi, nessun tono epico. Le 13
frasi che aprono con «Hai raggiunto <planet>» e le 6 con «Meglio ripartire» sono verificate come **conteggi**: se una resa
avesse cambiato formula, il controllo sarebbe rosso.

## 3. La composizione del phrase dei pirati

Il sorgente costruisce la frase da **sei blocchi** con alternative:

```
"Il governo di <planet>" · [ " " | " ti ringrazia sentitamente e " ] · "ti paga <payment> per aver contribuito a"
                        · [ " cacciare " | " sconfiggere " ] · "i " · [ "pirati." | "predoni." | "razziatori." ]
```

`Phrase::Get()` **concatena senza separatore**: gli spazi sono dentro i frammenti. Il test compone **12 combinazioni** e
verifica, per ognuna: nessun doppio spazio, punto finale, un solo `<payment>` e un solo `<planet>`, inizio con «Il governo
di <planet>».

Esempio composto, variante con ringraziamento e `sconfiggere`:

> «Il governo di <planet> ti ringrazia sentitamente e ti paga <payment> per aver contribuito a sconfiggere i razziatori.»

**Il terzo sostantivo è «razziatori»**, non «aggressori»: l'articolo `i` è un frammento **condiviso** dai tre sostantivi, e
«gli aggressori» avrebbe richiesto un articolo diverso — cioè un blocco in più che il sorgente non ha.

## 4. La lacuna dell'estrattore, dichiarata

La riga **24** contiene un frammento fatto di **un solo spazio** (`` ` ` ``): l'estrattore non lo espone come unità, quindi non
compare in `state.db` e non è traducibile. Non è stato «riparato» (gli strumenti sono protetti): è **dichiarato qui** e nella
resa, che funziona anche con quello spazio — è il motivo dello spazio finale del blocco ringraziamento.

## 5. Verifica

```
check.py   27 controlli · FAIL totale: 0 · exit 0
verify.py  20 controlli · FAIL: 0 · exit 0
segmento   0 prima (apre il file) · 29 qui · 25 dopo la 98 · copertura 29/54 (53,7%)
```

Quattro rossi al primo giro, tutti su **numeri miei non misurati**: «Hai raggiunto» 13 volte (non 10), «Meglio ripartire» 6
(non 7), spazi finali strutturali in **quattro** frammenti (4, 6, 7, 8, non solo 4), e la riga massima del file (**172**, non
297). Un quinto rosso su un arrotondamento: `round(1.625, 2)` fa **1.62**, non 1.63 — il confronto ora è sui valori esatti.

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 29 unità `PENDING`.
- **Nessun testo visto nel gioco**: la composizione è verificata **per costruzione**, non a schermo.
- **Nessuna revisione umana**.
- **Il file resta aperto**: 29/54.
