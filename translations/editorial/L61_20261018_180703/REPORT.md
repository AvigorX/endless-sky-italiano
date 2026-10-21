# REPORT — L61 · `data/human/culture conversations.txt` (righe 511–552)

**Esito: CHIUSO.** 26/26 unità, `check.py` `FAIL totale: 0`, `verify.py` exit 0.

## 1. Che cosa contiene il lotto

Una sola scena, un'intervista: `News Reporter - Paradise` (26 unità).

| Blocco | Unità | Contenuto |
|---|---|---|
| Incontro | 1–7 | La reporter con i droni-fotocamera, tre modi di reagire (aspettare, sperare di non essere notato, evitarla), la richiesta dell'intervista |
| Intervista, prima parte | 8–14 | «Sono qui su `<origin>`…» — l'ultimatum al Parlamento, due risposte opposte, la richiesta di spiegare |
| Spiegazioni | 15–19 | Tre giustificazioni possibili (interessi di ogni mondo / rappresentanza inadeguata / tasse ingiuste) e il rifiuto di rispondere |
| Intervista, seconda parte | 20–26 | La replica della reporter, tre nuove spiegazioni (canali adeguati / ingratitudine / rifiuto), la chiusura |

## 2. Le scelte di traduzione che contano

**Il registro è giornalistico.** La reporter parla per frasi complete e cortesi; il giocatore risponde
per battute singole, alcune secche. In italiano: «Bentornati. Sono qui su `<origin>` per riferire della
situazione con le Free Worlds» — nessuna subordinata aggiunta, nessun «in merito a».

**Le due domande di follow-up sono diverse** e restano diverse: «Can you explain your answer for our
viewers?» (14) e «Can you explain that answer for our viewers?» (21) → «Può spiegare la sua risposta» /
«Può spiegare quella risposta». In italiano «la» e «quella» bastano a distinguere il riferimento.

**`I'd rather not` (9) vs `I would prefer to not answer` (18, 24)**: due formule diverse, due rese
diverse. La prima è un rifiuto garbato, la seconda è una formula burocratica: il giocatore che rifiuta due
volte ripete la stessa frase perché il sorgente la ripete.

**`Parliament`, `Navy`, `Free Worlds`**: «Parlamento», «Marina», «Free Worlds» invariato. Sono
istituzioni del gioco: cambiarle romperebbe il collegamento con i lotti delle campagne Free Worlds
(L32–L41).

**`merchant captain currently between trips`** → «un capitano mercantile attualmente tra un viaggio e
l'altro». La formula è quella di un conduttore televisivo che riempie il tempo: resta leggermente
ridondante, come in inglese.

## 3. Difficoltà

- **Nessuna tecnica.** 1 token, 0 `UI_LABEL`, 0 virgolette dispari, 2 gruppi di duplicati spiegati dal
  sorgente.
- **Un dubbio di registro**: le risposte del giocatore sono tradotte in modo diretto («Il Parlamento ha
  preso la decisione giusta rifiutando le richieste»), senza ammorbidirle. Chi legge deve poter capire
  quale risposta è filo-governativa e quale filo-Free Worlds: la differenza è nel contenuto, non nel tono,
  e la traduzione non la segnala con avverbi.

## 4. Verifica osservata

```
check.py   → 33 controlli · FAIL totale: 0
verify.py  → 35 controlli · exit 0
             unita 26 · righe 511-552 · 116 prima / 232 dopo · file 374 · max(line) 1122
             tipi 26 MISSION_TEXT · NT vuoto · DIALOG/LOGBOOK/CONVERSATION/TEXT 0
             token 1 / 1 (<origin>, unita 11) · tab 25 / 25 · virgolette 38 / 38 · dispari 0
             rapporto 0,83 - 1,24 · duplicati 2 gruppi (4 unita)
             parole 394 EN -> 355 IT
             sha256 translation.json 8b7278d41edd723f…
```

## 5. Stato del progetto dopo L61

| Voce | Prima (L60) | Dopo L61 |
|---|---|---|
| File completi | 30 | 30 |
| Unità in staging | 23.945 | **23.971** |
| Lotti con `translation.json` | 64 | **65** |
| `culture conversations.txt` | 116/374 | **142/374 (38,0%)** |

Nessuna scrittura su `state.db`: le 26 unità restano `PENDING`.

## 6. Prossimo passo

**L62**: righe **555–611**, **30 unità**, 1 contesto (`Scientists at the Pub after a Conference`),
674 parole, tab 26, virgolette 36, **3 `UI_LABEL`** (unità 4, 15, 26), 0 token. Confine: riga 624 apre
`mission:Sol-Bound Shuttle`; restano 202 unità dopo la 611.
