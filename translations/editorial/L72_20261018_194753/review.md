# REVIEW — L72 · `data/successors/successor 2 ghosts myurej.txt`

## 1. Coerenza con L68–L71 e chiusura del file

- **Casa Myurej**, **Casate**, **Predecessori**, **Shroud**, **ninnoli**, **sfera di dati**, **erede**:
  tutte forme già fissate, nessuna reinventata.
- **Ijaset** mantiene la voce di L71 (piana, cortese) e **non ha genere**: «dicono», «si appoggia», nessun
  participio concordato. Il congedo («Se ci incontreremo di nuovo, che sia in termini piacevoli») chiude il
  personaggio senza aggiungere fraseologie.
- **Khiajsore** è il contraltare: affettato, ridondante, si presenta due volte. La differenza di voce fra i
  due Successori si vede a occhio nelle unità 33 e 46.
- **L'ultima riga rovescia la prima immagine del file** (schermo nero / finestra sull'oceano scuro): la
  traduzione tiene il paragone, non lo spiega.

## 2. Nodi traduttivi aperti (dichiarati)

- **`biped fever`** (38): «febbre dei bipedi». È una moda raccontata con disprezzo; se un lotto futuro la
  nomina come termine ufficiale, la resa va riusata identica.
- **`Ribbons of Iret`** (31): invariato. È un fenomeno naturale, non una nave né una fazione.
- **`Myurej M- Khiajsore`**: il prefisso `M-` resta; non è spiegato nel testo e non va interpretato.
- **`the Houses smuggled 'cross the wormhole`** (10): «le Casate hanno contrabbandato attraverso il
  wormhole». `wormhole` resta in inglese (decisione di L71).
- **`esoterica`** (10): mantenuto come «esoterica», parola rara ma presente in italiano.

## 3. `DIALOG`: testo, non etichetta

Le unità 3 e 4 sono **descrizioni di evento** in un blocco `dialog` del sorgente:

- 3: «Quando la seconda nave drone esplode, trasmette alcuni dati alla tua nave. Al momento non è possibile
  decifrarli.»
- 4: «Ijaset ti ordina di atterrare sul mondo disabitato qui vicino per consegnare i manufatti…»

Sono tradotte. Il `verify.py` asserisce che **non** siano identiche all'inglese: se in un lotto futuro un
`DIALOG` fosse in realtà un'etichetta, il controllo lo segnalerebbe come «non tradotto».

## 4. Duplicati, virgolette, tab

- **0 gruppi di duplicati inglesi**; nessuna resa italiana ripetuta fra inglesi diversi.
- **96 virgolette** su 50 unità, **0 dispari**: il lotto più dialogato del file.
- **36 tab su 36 unità**; 14 unità senza (6 fra nome/descrizione, 2 `DIALOG`, 2 `log`, 4 testi non
  indentati).
- **0 quadre**, **0 backtick**.

## 5. Cosa NON è stato fatto

- **Nessuna scrittura su `state.db`**: le 50 unità restano `PENDING`, come le altre 161 del file.
- **Nessun caricamento nel gioco**: nessun test a schermo del matrimonio subacqueo o dell'inseguimento.
- **Nessuna verifica del registro**: la voce di Khiajsore è valutata come testo, non misurata.
- **Il file è completo ma non approvato**: 211 unità `PENDING` su un file chiuso.

## 6. Rischi residui

- **La chiusura è asserita in modo rigido**: `0 dopo`, `max(line) = 531`, copertura 211/211. Se il sorgente
  crescesse, il `verify.py` diventerebbe rosso — è il comportamento voluto (decisione 181).
- **Il lotto copre tre contesti** invece del solo `Myurej 6` previsto dall'handoff: scelta dichiarata, non
  silenziosa. Chi riprende deve sapere che `HANDOFF_L72` descriveva un lotto che non è stato fatto così.
- **`Khiajsore` si presenta due volte** (38 e 39): se un revisore lo leggesse come errore di traduzione,
  sbaglierebbe — è nel sorgente.

## 7. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 3 parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì — entrambi gli script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (35 controlli), `verify.py` exit 0 (46 controlli), chiusura 211/211, sha256 `bd09dd6de0b9ff04` |
