# REPORT — L73 · `data/successors/successor 2 ghosts aqrabe.txt`

## 1. Cosa contiene il lotto

**L'invito e il reliquiario** (unità 1–17). Un Successore in un abito scuro a pagliuzze dorate invita il
giocatore al **reliquiario** dello spazioporto orientale di Casa Aqrabe. Nella sala circolare, sotto un
serbatoio emisferico, scendono **arti recisi** di Successori, legati a filamenti dorati; il giocatore può
toccarli o lasciarli stare. Se li tocca, un coro di voci artificiali discute di lui in frammenti: «quattro
zampe? straniero?», «la curiosità, la quarantesima virtù», «può un alieno essere virtuoso? discutiamo».

**Sola e la proposta** (18–29). Arriva **Aqrabe I- Sola**, erede per matrimonio, che spiega: i «santi» sono
**reliquie**, menti non viventi conservate in parti. Chiede come il giocatore passi il wormhole, e alla
risposta evasiva ribatte che hanno già scansionato la nave. Poi l'offerta: **cinquanta pietre chiave
quantistiche** per studiarle e un giorno produrne di proprie, meno costose della formatura delle corazze.

**La consegna e Tiliia** (30–43). Con la partita a bordo, il giocatore incontra **Tiliia**, ingegnere della
Casa, in un vano di allestimento pieno di tessuti e statue astratte, dove uno scanner navale viene smontato.
Segue la consegna, il credito e un **bonus di trecentomila crediti**, e l'invito a tornare entro sera. Tre
missioni si aprono qui: pietre chiave dai **Remnant**, dagli **Hai**, e la **prova** delle pietre.

**La scorta** (44–51). Tiliia organizza un viaggio di comprensione: due navi di Aqrabe — una con una pietra
chiave, l'altra con la **corazza tessuta** — attraversano il wormhole, con la nave del giocatore come punto
di raccolta dati. Sul mondo bruciato oltre la porta, i due **Seiitejen** si posano accanto alla `<ship>`;
Tiliia raccoglie i dati e ammette una «lieve differenza» fra le pietre e la corazza, da capire a casa.

## 2. Scelte editoriali

| nodo | scelta | perché |
|---|---|---|
| `keystone` / `Quantum Key Stones` | **pietra chiave** / **Pietre Chiave Quantistiche** | forma già in staging (3 occorrenze); maiuscole come nel nome dell'oggetto |
| `reliquary` | **reliquiario** | una occorrenza già in staging; il posto è una teca, non un museo |
| `saints` | **santi** fra virgolette | il personaggio li chiama così, con ironia devota: le virgolette restano |
| `Aqrabe I- Sola` | invariato; «Sola» nel resto del lotto | nome e titolo di Casa, come `Myurej M- Khiajsore` |
| `unliving minds` / `half-sleepers` | **menti non viventi** / **dormienti a metà** | immagini del testo, non spiegate |
| `weft-weaving armor` / `multimodal armor` | **corazza tessuta** / **corazza plurimodale** | due espressioni inglesi distinte, due rese distinte |
| `data-pad` | **datapad** | forma già usata in L71 |
| `three hundred thousand-credit bonus` | **bonus di trecentomila crediti** | nel parlato la cifra va in lettere |
| `Procurati le pietre chiave dai Remnant` | titolo con verbo | forma dei nomi di missione già fissata |
| `Seiitejen` | invariato | nome di nave |
| `the fortieth virtue` | **la quarantesima virtù** | i «santi» contano le virtù: il numero è un dato |

## 3. Difficoltà incontrate

1. **`CONVERSATION` per la prima volta in un file di questa linea**: le sei unità sono il **testo** del
   blocco (backtick nel `raw`, non nell'`english`). Tradotte come prosa e verificate per **conteggio**: un
   inventario che cambiasse passerebbe inosservato senza quel controllo.
2. **Una categoria di diario in mezzo al lotto** (unità 43, `People`): in `NT`, identica. Il `check.py`
   distingue `LOG_CAT` da `LOG_TEXT` come in L68.
3. **`DIALOG` = testo** (unità 50): stessa verifica di L72, con l'asserzione che non resti in inglese.
4. **Le voci dei «santi»** (unità 8–13) sono frammenti con indentazioni diverse, che il costruttore dei tab
   riproduce. La tentazione è ricomporle in frasi compiute: sarebbe un tradimento del testo.
5. **`<ship>` sei volte** in unità diverse (scanner, cargo, plancia, atterraggio): parità per simbolo, e
   nessuna sostituzione con «la tua nave» dove il token c'è.

## 4. Numeri osservati (output letto)

```
unita' tradotte nell'intervallo   51/51
copertura del lotto               51/51
tab IT 42 / EN 42
virgolette IT 90 / EN 90
token IT 9 / EN 9
rapporto IT/EN 0.72 - 1.56
parole EN 1330 -> IT 1281
prima/ultima riga del segmento: 23/158
duplicati inglese: 0 gruppi
FAIL totale: 0                     (35 controlli)
verify.py exit 0                   (47 controlli)
sha256[:16] translation.json      1cd04c9a55a1312c
```

## 5. Stato del progetto dopo il lotto

```
TOTALE staging: 24465 unita · 781354 EN · 740531 IT
APPROVED 364 · PENDING 32560 · totale 32924
lotti con translation.json: 77
```

`successor 2 ghosts aqrabe.txt` è coperto **51/180 (28,3%)**: restano **129 unità** dopo la riga 158.

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 3 parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`/`REPORT.md`/`review.md` |
| ESEGUITO | sì | `check.py` e `verify.py` lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` → `FAIL totale: 0` (35 controlli) **e** `verify.py` → `FAIL: 0`, exit **0** (47 controlli) |
