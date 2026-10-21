# review.md — L285 (`data/wanderer/wanderer missions.txt`, righe 169–182)

Registro delle decisioni editoriali del **lotto terminale** delle missioni Wanderer: l'**epilogo** della pianta.

## 1. Che cosa succede

Anni dopo, avvicinandosi a `<planet>`, il giocatore **ricorda** di avervi piantato il fiore dei Mereti. Fra le nuvole vede «un
minuscolo puntino blu in fondo a una valle, **esattamente dove** hai lasciato i Wanderer anni fa». Scende: la **Strong Wind** è
parcheggiata «in mezzo a un campo di fiori, i cui petali brillano di un bellissimo blu intenso».

Un drone Mereti gli vola incontro «con una voce **molto più sommessa** di quanto ti aspetti» e **ringrazia**:

> «Grazie, `<first> <last>`. Hai `[salvato, riportato in vita]` il **sitrasanir**.»

Il **traduttore** non prova nemmeno a rendere l'ultima parola: «non somiglia a nessuna parola che tu abbia sentito nella lingua
Hai o in quella dei Wanderer». Il giocatore ripete la parola come domanda, e il drone spiega che il fiore era un **simbolo** per
i loro **creatori**, che l'hanno `[abbandonato, ignorato]` per anni, e che i loro `[genitori, antenati]` li hanno aiutati a
**ricordarlo**. Il testo chiude sull'immagine: il sole sale, il campo risplende «di tonalità blu che quasi coincidono con le
vernici blu delle navi Mereti lassù nel cielo».

## 2. Il nome che non si traduce

`sitrasanir` è **il nome del fiore** e resta **invariato**. Non è una scelta di stile: **il testo stesso dice** che il
traduttore non lo rende, e che non appartiene né alla lingua Hai né a quella dei Wanderer. Tradurlo («sitra-sanir» come
«fiore-stella») avrebbe **spiegato** ciò che il testo lascia **straniero**.

Il test lo verifica **tre volte**: due minuscole (unità 5 e 8) più la domanda con l'iniziale maiuscola (unità 6), con conteggio
**case-insensitive** e controllo esplicito della forma `Sitrasanir?`.

## 3. Il cerchio: `[genitori, antenati]`

In **L282** (unità 5) il drone si era interrotto: «Questa pianta è importante per noi. È la nostra...», e poco dopo diceva
«Ci hai portato i nostri `[genitori? antenati?]`». Qui, alla riga 180, la stessa coppia torna — **con la virgola** invece del
punto interrogativo: `[parents, ancestors]`.

La resa **riprende la stessa coppia** (`[genitori, antenati]`) e il test la verifica: due lotti distinti, la stessa parola.
Il cambio di separatore (`?` → `,`) è **del sorgente** e viene conservato: nella prima scena il drone **non sa** quale delle due
parole sia giusta, nella seconda **lo sa**.

## 4. Le scelte del giocatore

| inglese | resa | forma |
|---|---|---|
| `(Take a closer look.)` | **(Guarda più da vicino.)** | parentesi tonde, **punto dentro** |
| `(Not right now.)` | **(Non ora.)** | idem |

Sono **opzioni** del motore di missione: se la parentesi o il punto si perdono, la scelta **non compare**. Non sono prosa e non
si «abbelliscono». «Non ora.» invece di «Non adesso.»: più corto, e il registro del giocatore è **asciutto** in tutta la serie.

## 5. Scelte di resa

| inglese | resa | nota |
|---|---|---|
| `a tiny blue dot in the depths of a valley` | **un minuscolo puntino blu in fondo a una valle** | |
| `exactly where you left the Wanderers years ago` | **esattamente dove hai lasciato i Wanderer anni fa** | |
| `their petals gleaming a beautiful deep blue` | **i cui petali brillano di un bellissimo blu intenso** | colore già usato in L282 |
| `far more subdued than you expect` | **molto più sommessa di quanto ti aspetti** | il drone **ringrazia**, e la voce è bassa |
| `Your translator makes no attempt at the last word` | **Il tuo traduttore non prova nemmeno a rendere l'ultima parola** | |
| `in a contemplative silence` | **in un silenzio contemplativo** | |
| `the blue paints on the Mereti ships` | **le vernici blu delle navi Mereti** | |

## 6. Struttura

| cosa | inglese | italiano |
|---|---|---|
| tab | **8** (unità 2-9) | **8**, primo carattere; la 1 no |
| virgolette | **8** | **8**, per unità |
| alternative | **6** (tutte coppie) | **6** |
| apici | **2** | **1** |
| segnaposto | **3** | **3** |
| parentesi di scelta | **2** | **2**, punto dentro |

## 7. Cosa resta aperto (dichiarato)

- **Nessuna approvazione**: 9 unità `PENDING`; **nessuna revisione umana**.
- **Il file è chiuso a 54/54** in staging: quarto file della serie `wanderer` completato? **No** — è il **primo**: `wanderer
  jobs.txt` (92/92) era un altro file.
- **Prossimo file**: `data/gegno/gegno ships.txt` — righe **53–302**, **7 unità** (tutte `DESCRIPTION`), **454 parole**, **6
  contesti** (`Shale`, `Dolomite`, `Conglomerate`, `Granofel`, `Gypsum` ×2, `Corundum`), **1 tab**, **0 virgolette**, **4
  apici**, **0 segnaposto**, **0 alternative**: il lotto più «pulito» della serie, e serve a verificare che il metodo regga anche
  dove **non** ci sono parentesi quadre.
