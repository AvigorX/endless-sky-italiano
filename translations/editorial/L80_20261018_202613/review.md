# REVIEW — L80 · `data/successors/successor side missions.txt` (chiude il file)

## 1. Coerenza con la linea Successors (L68–L79)

- **Le Casate** senza aggettivo indica l'istituzione in generale, non le Nuove: nel lotto compaiono **solo**
  così, e la resa lo rispetta (`le Casate hanno decretato in consiglio`).
- **Il registro è burocratico-militare**: nessuna formula cerimoniosa, solo l'arcaico `thy`/`thou` dentro un
  avviso ufficiale. Reso con «tu» formale e sintassi asciutta.
- **Le tre reazioni di colore** (arancione fiammeggiante, rosso scuro, nero irto) sono l'unico commento
  emotivo: la traduzione le lascia come immagini, senza aggiungere avverbi.

## 2. Nodi traduttivi aperti (dichiarati)

- **`Unified Defense`** (nome della missione, non nel lotto come testo): se un lotto futuro lo traducesse,
  servirebbe una scelta unica — qui non compare.
- **`prone to such 'accidents'`**: le virgolette sono **ironiche**, del Successore; restano semplici, e il
  testo non le spiega.
- **`Our fleets will make sure of it`**: «le nostre flotte se ne assicureranno» — `it` è la promessa di non
  ripetere la trasgressione, non un'azione; la resa mantiene l'ambiguità.
- **`bristling black`**: «nero irto» è una scelta; «nero ispido» sarebbe più letterale e meno fisico.

## 3. Le quattro label

| unità | inglese | perché è in `NT` |
|---|---|---|
| 2 | `populated language` | bersaglio di salto per pianeta abitato |
| 9 | `uninhabited language` | bersaglio di salto per pianeta disabitato |
| 15 | `never again` | bersaglio di salto (ramo «non lo farò più») |
| 17 | `deserved it` | bersaglio di salto (ramo «se lo meritavano») |

Tradurne una sola romperebbe il ramo corrispondente. Il `verify.py` le elenca e le confronta una per una.

## 4. Chiusura del file

| fatto | prova |
|---|---|
| 0 unità dopo la riga 453 | `count(*) where line > 453` = 0 |
| `max(line) = 453` | query sul DB |
| 164 unità totali | `count(*) where path = …` |
| copertura dell'intero file | 164 `id` distinti e 164 righe nei `translation.json` di L77–L80 |
| quattro lotti | L77 (63) + L78 (53) + L79 (29) + L80 (19) = 164 |

## 5. Cosa NON è stato fatto

- **Nessuna scrittura su `state.db`**: le 164 unità del file restano `PENDING`.
- **Nessun caricamento nel gioco**: il bando, gli intercettori e le tre reazioni cutanee non sono stati visti
  a schermo.
- **Le quattro label restano in inglese** per scelta: sono bersagli di salto.
- **Nessuna verifica del tono**: l'ufficialità dell'avviso è valutata come testo.

## 6. Rischi residui

- **`0,93 – 1,14`**: il lotto più stretto del progetto, nessuna unità vicina al gate.
- **Il `verify.py` di questo lotto è più severo** di quelli intermedi: se qualcosa toccasse le righe 416–453,
  diventerebbe rosso (è voluto).
- **`Unified Defense`** non è tradotto perché non compare come testo: se comparisse in un elenco di missioni,
  servirebbe una decisione.

## 7. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 1 parte, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (32 controlli), `verify.py` exit 0 (36 controlli), sha256 `0cc5130f4bba902e`, **file 164/164** |
