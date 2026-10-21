# REVIEW — L76 · `data/successors/successor 2 ghosts aqrabe.txt` (ultimo lotto del file)

## 1. Coerenza con la linea Successors (L68–L75)

- **Casa X / Casate / erede / cimeli / pietre chiave / giardino di metallo stellare / nave da guerra /
  ufficiale di collegamento con la flotta / motore di salto**: forme fisse, nessuna reinvenzione.
- **Il registro di Tiliia** resta arcaico-cerimonioso (`thou mayst`, `thou'rt`, `'Tis`) reso con il «tu»
  moderno formale; nel finale passa a un tono **più intimo** («Ho delle scuse da farti»), e la traduzione lo
  segue senza cambiare le forme fisse.
- **L'osservatore di Kaatrij** resta senza colore e senza cortesia, come in L75.
- **`Aqrabe I- Sola` non compare**: Tiliia cita «Aqrabe» come Casa.

## 2. Nodi traduttivi aperti (dichiarati)

- **`its weapons are aimed right at you!`** (12): punto esclamativo mantenuto; il `DIALOG` è un avviso di
  gioco, non prosa.
- **`It cannot be deciphered at this time`** (13): «per ora» rende `at this time` senza suggerire che sarà
  decifrato — il testo non lo promette.
- **`a nest; going where we shouldn't`** (17): «devastare un nido, andando dove non dovremmo» — il punto e
  virgola inglese separa due accuse, e resta separato.
- **`No House would've left a craft like that behind`** (20): «Nessuna Casata avrebbe lasciato indietro una
  nave così» — il condizionale italiano copre il `would've`.
- **`I'll be sure to note thy helpfulness to Aqrabe`** (24): «sarò certa di segnalare ad Aqrabe la tua
  utilità» — «utilità» è più freddo di «aiuto», e il testo è freddo.
- **`the ghosts of others`** (27): «i fantasmi degli altri» — richiama il titolo della linea senza spiegarlo.
- **`aggessor`**: il testo dice `Kaatrij's aggressor` senza identificarlo; la traduzione non aggiunge
  ipotesi.

## 3. La coppia 23/25

| unità | inglese | italiano | virgolette |
|---|---|---|---|
| 23 | `"What about this ship? Do I get to keep it?"` | `"E questa nave? Posso tenermela?"` | 2 (chiude) |
| 25 | `"What about this ship? Do I get to keep it?` | `"E questa nave? Posso tenermela?` | **1 (non chiude)** |

Le due rese differiscono **solo** per la virgoletta finale. Non è un refuso: è la forma del sorgente, e il
`verify.py` lo asserisce (`rstrip('"')` uguali, chiusura diversa). Se un lotto futuro «correggesse» la 25,
il controllo diventerebbe rosso.

## 4. Chiusura del file

| fatto | prova |
|---|---|
| 0 unità dopo la riga 478 | `count(*) where line > 478` = 0 |
| `max(line) = 478` | query sul DB |
| 180 unità totali | `count(*) where path = …` |
| copertura dell'intero file | 180 `id` distinti nei `translation.json` dei lotti L73–L76, 180 righe |
| quattro lotti | L73 (51) + L74 (38) + L75 (61) + L76 (30) = 180 |

## 5. Cosa NON è stato fatto

- **Nessuna scrittura su `state.db`**: le 180 unità del file restano `PENDING`.
- **Nessun caricamento nel gioco**: il saccheggio del giardino, la nave drone e il finale con Tiliia non sono
  stati visti a schermo.
- **`not confronted` resta in inglese** per scelta: è un bersaglio di salto.
- **I due `DIALOG`** (12, 13) sono testi di avviso, non scene: nessuna verifica di regia.

## 6. Rischi residui

- **`0,75` è il minimo** (unità brevi come «"Ma che cosa?"»): dentro il gate.
- **`1,26` è il massimo**: nessuna riscrittura necessaria.
- **Il `verify.py` di questo lotto è più severo** di quelli intermedi: se un lotto futuro toccasse le righe
  404–478, diventerebbe rosso (è voluto).
- **La lacuna dell'estrattore** non tocca questo lotto (nessuna categoria di diario), ma resta aperta sui
  sette casi precedenti.

## 7. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 2 parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì — entrambi gli script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (35 controlli), `verify.py` exit 0 (49 controlli), sha256 `44a954ecdc2aac76`, **file 180/180** |
