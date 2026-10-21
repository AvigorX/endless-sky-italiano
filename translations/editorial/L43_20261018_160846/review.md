# L43 — revisione editoriale

Lotto `L43_20261018_160846` · `data/remnant/remnant 2 side missions.txt` · righe 17–775 · 299 unità ·
10.539 parole EN → 9.870 IT · `check.py` `FAIL totale: 0` · `verify.py` 33 controlli, exit 0.

Questo documento registra **le decisioni**, non i numeri: i numeri stanno in `REPORT.md` e sono
rigenerabili con i due comandi di verifica.

---

## 1. Che cosa copre il lotto

Le trame secondarie dei Remnant, undici episodi autonomi:

1. **Visit to Paradise** — Taely porta il giocatore su Vail, pianeta-vacanza per l'hoverboard, e poi su
   Caelian a vedere uno spazioporto storico (cammelli, carri, mulini a vento, muri contro la fauna).
2. **Celebration** — la Celebrazione del Ricordo: danza, tamburi, canti, e le domande del giocatore su
   chi guida la cerimonia e perché qualcuno piange.
3. **Teciimach Deployment** — la nuova versione dei siluri EMP, la **Tana** e i **Maudrakoi**.
4-6. **Shattered Light 2–6** — la nave-città fantasma dell'Esodo: scansione, recupero, rientro nella
   Trama Primaria, spiegazione della **Trama** e degli **androidi NDR-114**.
7. **Scent of Rain** — la nuova nave Korath che porta tre caccia, e la metafora di Chilia sul primo
   odore di pioggia.
8. **Will Not Someone Please Think Of The Children** — il Dathnak A'awoj con i civili a bordo.

## 2. Ricognizione (misurata sul `source.json`)

```
MISSION_TEXT 235 · UI_LABEL 36 · VALUE 10 · DESCRIPTION 10 · DIALOG 8 · LOGBOOK 0 · CONVERSATION 0
contesti 11 · tab 208 · virgolette 445 · token 47 (9 famiglie) · quadre 0
unità con virgolette dispari: 11 (133, 188, 190, 225, 227, 229, 245, 247, 280, 285, 286)
9 gruppi di inglese identico (22 unità su 299)
```

Le differenze da L42 che contano: **36 label con indici nuovi** (un in più, ma nessuno in comune),
**nessun `LOGBOOK`** (quindi nessuna lacuna di inventario), **densità di token bassa** (47 su 299 contro
174 su 572) e **due missioni che si chiudono con lo stesso testo** (`Shattered Light` compare come titolo
di due lotti interni, 202 e 233).

## 3. Metodo

1. `export_section.py` su righe 17–775 → 299 unità, 11 contesti.
2. Ricognizione dei tipi, delle 36 label (`raw`), delle virgolette dispari, dei duplicati, dei token.
3. `check.py` derivato da L42: `NT` rimisurato, docstring riscritta, costruttore dei tab riusato.
4. Traduzione in 8 parti a fine contesto (41 · 30 · 38 · 39 · 36 · 45 · 29 · 41), ognuna chiusa con
   `check.py --range`; controllo completo dopo la terza, la sesta e l'ottava.
5. `check.py` completo (verde al primo colpo) e `verify.py` indipendente.

## 4. La voce

La voce dei Remnant è quella di L21/L24/L42: cortesia formale, «Ben incontrato», «Che le Braci…»,
«Embers light your path» → «Che le Braci illuminino il tuo cammino». In questo lotto si aggiungono due
registri nuovi, e sono distinti di proposito:

- **Taely da turista** (Visit to Paradise): entusiasta e leggera, con battute tecniche («Tantissimi
  produttori diversi hanno partecipato alla costruzione di questo veicolo»). Il suo stupore per Vail è
  autentico, e la traduzione non lo raffredda.
- **Chilia da profeta** (Scent of Rain): la metafora del temporale in arrivo regge solo se resta
  concreta: «sai nelle ossa che sta arrivando una tempesta», «questo è il primo odore di pioggia».
  Ho tenuto «odore di pioggia» anche nel titolo della missione (`Scent of Rain` → **Odore di pioggia**
  non è un titolo: il titolo resta `Scent of Rain`, che è un nome di missione e non si traduce).

Chiarimento necessario: **i titoli delle missioni** (`Scent of Rain 1`, `Shattered Light 4`, …) non
compaiono nelle unità tradotte: sono contesti, non testo. Nei `VALUE` tradotti ci sono invece i titoli
**visibili** (`Hoverboarding with Taely`, `Brilliant Energy`, `Sympathy For The Korath`, …).

## 5. Le scelte terminologiche

| inglese | italiano | nota |
|---|---|---|
| the Warren | **la Tana** | termine interno dei Remnant per la rete di caverne; maiuscola perché è un nome proprio di luogo |
| Primary Weft / Secondary Weft | **Trama Primaria** / **Trama Secondaria** | il testo spiega l'immagine tessile; `weft` è la trama |
| Warp | **Ordito** | è la proposta di rinominare la Trama Primaria: `warp` e `weft` sono ordito e trama, e la resa deve mostrare l'analogia |
| weft field | **campo di trama** | |
| Zitchal Maudrakoi, Maudrakoi | invariati | nome di specie/civiltà |
| Shattered Light | invariato | nome di nave |
| NDR-114 Androids | **Androidi NDR-114** | modello invariato, sostantivo tradotto |
| EMP Torpedo | **siluro EMP** | `EMP` resta acronimo |
| hoverboard / hoverboarding / hovercar / hovercart | **hoverboard / hoverboard / hovercar / hovercart** | il gioco usa il termine inglese anche in italiano corrente; i composti restano |
| Point Defense Turrets | **torrette di difesa puntuale** | da L42 |
| Dathnak A'awoj, Palavret, 'olofez, Ra'puk At 333 | invariati | nomi di nave Korath |
| Far Monad, Coluber, Caeculus, Kor Zena'i, Vaticanus, Terminus | invariati | toponimi |
| crater Tycho, Luna | **cratere Tycho, Luna** | `Tycho` resta, `Luna` è già italiano |

## 6. Numeri tecnici: si riproducono, non si normalizzano

Due unità contengono cifre formattate dal motore:

- `11D.E78 metri al secondo` e `1.1DE79` (unità 37 e 41): il formato `D.E` è quello del sorgente e
  **non va toccato**;
- `299.792.458 m/s`, `2.99792458x10^8`, `1.1DE784Ax10^7` (unità 45): qui ho convertito solo il
  separatore delle migliaia alla convenzione italiana (`299,792,458` → `299.792.458`), lasciando
  intatti coefficiente, base ed esponente.

Nessun altro numero del lotto è stato riscritto.

## 7. Lacuna di inventario

**Nessuna.** Il file non ha righe `log` (0 `LOGBOOK`), quindi non esiste il caso che in L30/L33/L34/L35/L42
ha lasciato in inglese categorie o nomi. Il `verify.py` lo asserisce come assenza (`log == []`), e
asserisce allo stesso modo l'assenza di `CONVERSATION`.

## 8. Cosa è stato corretto e perché

Il `check.py` completo è passato **al primo colpo**: nessuna delle 299 unità è stata riscritta per il
gate. Le uniche correzioni sono avvenute durante la scrittura, e sono di contenuto:

- **Unità 3**: la prima stesura conteneva solo la battuta e perdeva la narrazione che la precede
  («You are just settling down at a table…»). Se ne è accorto il `check.py --range`, che ha segnalato un
  rapporto di 0,33: la riga è stata riscritta per intero. È il tipo di errore che i controlli di
  lunghezza prendono e la rilettura no.
- **Unità 133, 188, 190, 225, 227, 229, 280, 285, 286**: battute aperte nel sorgente. Sono state
  riprodotte aperte, e il `verify.py` confronta l'insieme degli indici, non il totale.

## 9. Controlli e limiti

`check.py` (21 controlli): copertura, unità vuote, `NT` (36), duplicati italiano spiegati dal sorgente,
tab per unità e come totale, tab iniziale, virgolette per unità e come totale, quadre, token, backtick,
spazi, rapporto, tipografia, caratteri non latini, parole residue, stato del database.

`verify.py` (33 controlli) ricostruisce tutto da `source.json`, dal file sorgente e da `state.db` in sola
lettura. In più asserisce: le 36 `UI_LABEL` identiche **come elenco**, l'**assenza** di `LOGBOOK` e
`CONVERSATION`, l'assenza di quadre, l'insieme delle 11 virgolette dispari, la parità di tab e virgolette
per unità, la copertura 299/299 e la coppia di righe (17, 775).

Limiti, dichiarati:

- **Il lotto non è nel gioco.** Nessuna approvazione nel database, nessun caricamento: 299 unità `PENDING`.
- **Nessuna verifica a schermo.** Non ho visto la Celebrazione del Ricordo, né il recupero della
  Shattered Light, né il Dathnak A'awoj: i 36 salti `goto` sono intatti per costruzione (le label sono
  byte-identiche), ma il percorso non è stato giocato.
- **Il rapporto 0,65–1,40 non è un giudizio di qualità.**
- **`hoverboard` resta inglese**: è una scelta, non una svista. In italiano corrente il termine è usato
  così, e i composti (`hovercar`, `hovercart`) restano coerenti.
