# L31 — revisione editoriale

`data/coalition/heliarch intro.txt`, righe 16–2140 · 663 unità · 21.729 parole inglesi.
Lotto che **chiude il file** (11º file completo dello staging). Nessuna unità è stata approvata nel
database: lo staging non è approvazione.

---

## 1. Che cosa copre il lotto

Il lotto prende il file dalla prima unità all'ultima. L'arco narrativo è l'ascesa del giocatore dentro
l'Eliarchia, dal lavoro di ricognizione per conto degli Heliarchs fino all'incorporazione formale:

| righe | contenuto |
|---|---|
| 16–158 | indagine su Kirrie (cacciatore di taglie) e sul Saryd che protegge i rifugiati |
| 159–286 | pianeta ghiacciato, deposito minerario, relitto; ricognizioni 1, 2-A, 2-B |
| 287–363 | scansione del Wardragon a Zubeneschamali; il console Aulori entra in scena |
| 364–436 | **mondo ad anello rotto** di Deneb: spedizione, base su Ruin, il frammento |
| 437–519 | il console Aulori e la politica dei consoli; trasporto di agenti e feriti |
| 520–575 | droni spia, trasporti sotto copertura, navi in fuga con armi umane |
| 576–633 | le esercitazioni della magistra Lotuora (rifornimento, inseguimento, duello) |
| 634–663 | incoronazione, cerchietto, calibrazione, accesso alle sezioni riservate |

---

## 2. Ricognizione (misurata sul `source.json`, non dedotta)

```
MISSION_TEXT 571 · VALUE 31 · DESCRIPTION 31 · DIALOG 16 · UI_LABEL 10 · LOGBOOK 4 · CONVERSATION 0
contesti 41, da `Heliarch Investigation 1` a `Heliarch License 2`
tab 509 · virgolette 878 · token 181 · virgolette dispari 0
```

- **`UI_LABEL` 10**: tutte etichette di salto (`final thanks`, `bush ending`, `bumpy road`,
  `bumpy blizzard`, `snow dig`, `keep dig`, `open crate`, `expeditions past` ×2, `knows iekie`).
  Verificate una per una sul `raw`: sono nomi di nodo, non prosa. Restano identiche e sono elencate
  in `NT` una per una, non per regola generale.
- **`LOGBOOK` 4**: quattro righe `log` a due argomenti, tutte con unità regolare nel database.
  In questo file **non** c'è la lacuna vista in L30 (`log` a tre argomenti fra virgolette, righe 21 e
  467 di `lunarium intro.txt`): qui nome e testo del diario esistono e sono tradotti.
- **`DIALOG` 16**: righe di atterraggio, comprese le tre condizioni di fallimento del duello (628–631).
- **`VALUE` 31**: titoli di missione, tradotti (sono testo mostrato).

---

## 3. Metodo

1. `export_section.py` ha esportato le righe 16–2140 in `source.json` (663 unità).
2. `check.py` è derivato da quello di L30: `NT` rimisurato (10 elementi), docstring riscritta con i
   numeri del lotto, `TOKEN_EXC` vuoto, `TITLES` esteso con i nomi incontrati (`Punishers`,
   `Finishers`, `Judicators`, `Wardragon`, `Spires`, `Deneb`, `Zubeneschamali`, `Alta Hai`, `Forpelog`,
   `Grakhord`, `Kuwaru Efreti`, `Lagrange`, `Aulori`, `Iekie`, `Into White`, `Mebla's Portion`,
   `Stronghold of Flugbu`, `Shifting Sand`, `Fourth Shadow`, `Remote Blue`).
3. Traduzione in **11 parti**, tutte chiuse a fine missione, ognuna con `check.py --range` verde:

   | parte | unità | n. | parte | unità | n. |
   |---|---|---:|---|---|---:|
   | 01 | 1–42 | 42 | 07 | 364–436 | 73 |
   | 02 | 43–101 | 59 | 08 | 437–519 | 83 |
   | 03 | 102–158 | 57 | 09 | 520–575 | 56 |
   | 04 | 159–238 | 80 | 10 | 576–633 | 58 |
   | 05 | 239–286 | 48 | 11 | 634–663 | 30 |
   | 06 | 287–363 | 77 | | | |

4. I tab iniziali non sono digitati: un costruttore li aggiunge dal sorgente (`'\t' * tab_EN`).
   Risultato: 509 IT = 509 EN.
5. Dopo ogni parte anche il controllo **completo**, perché la deduplica italiana è sul lotto e non
   sull'intervallo.

---

## 4. Voce della Coalizione

Convenzione già fissata in L24–L26 e L30 e mantenuta qui: **Kimek, Saryd e Arach parlano con l'ordine
dei costituenti marcato** (soggetto esplicito, verbo in coda, participio in testa), mentre la
narrazione resta in italiano normale. Il contrasto è deliberato: si riconosce chi parla dal ritmo
della frase.

Esempi dal lotto (unità 305, 394, 451, 647, 661):

- `"Thank you again, we must, for your latest service. Much more detailed than what we had, your
  scans are."` → «Ringraziarti ancora, noi dobbiamo, per il tuo ultimo servizio. Molto più dettagliate
  di quelle che avevamo, le tue scansioni sono.»
- `"Skeptical of what you told us, we all were, Captain"` → «Scettici su ciò che ci hai detto, tutti
  noi eravamo, Capitano»
- `"Not a single dent, they left. Not one."` → «Non una sola ammaccatura, hanno lasciato. Nemmeno una.»
- `"Truly special, this ceremony is"` → «Davvero speciale, questa cerimonia è»
- `"As of a lower rank you are, permit you access to everything and everywhere, your circlet will
  not."` → «Dato che di rango inferiore tu sei, permetterti l'accesso a tutto e ovunque, il tuo
  cerchietto non lo farà.»

La stessa voce si applica ai Quarg quando parlano (unità 291–302): il Quarg che attende fuori dalla
nave usa lo stesso ordine marcato, e la narrazione intorno resta piana.

---

## 5. Decisioni lessicali

| inglese | italiano | motivo |
|---|---|---|
| `Heliarch` / `Heliarchy` | Heliarch / Eliarchia | continuità con L24–L26 e L30 |
| `console` / `consuls` | console / consoli | carica; invariata al singolare e al plurale |
| `Arbiter` | arbitro | grado (`Arbiter Sedlitaris` → «arbitro Sedlitaris») |
| `Magister` | magistra | grado femminile (`Magister Lotuora`) |
| `circlet` | cerchietto | oggetto centrale dell'incorporazione |
| `Punishers`, `Finishers`, `Judicators`, `Hunters`, `Wardragon`, `Spires` | invariati | classi di nave: nomi propri di modello |
| `Refueling/Pursuit/Combat Drill` | prova di rifornimento / inseguimento / combattimento | `Drill` è un'esercitazione; «prova» tiene il titolo corto |
| `Finisher Pods` | pod Finisher | equipaggiamento, nome della ditta invariato |
| `plasma turrets` / `torpedo launchers` | torrette al plasma / lanciatori di siluri | attrezzature umane viste dal lato della Coalizione |
| `spy drone` | drone spia | da `repair drone` + modulo di scansione |
| `ring` / `ringworld` | anello / mondo ad anello | glossario della Coalizione |
| `jump drive` | motore di salto | precedente di L24 |

Nomi propri, pianeti, sistemi, anelli e persone restano in inglese: `Anello dell'Amicizia` e
`Anello del Potere` sono i due anelli dove si svolge l'arco (nome tradotto perché descrittivo),
mentre `Fourth Shadow`, `Remote Blue`, `Ashy Reach`, `Deneb`, `Zug`, `Ruin`, `Zubeneschamali`,
`Aulori`, `Iekie`, `Plortub`, `Lotuora`, `Sedlitaris`, `Kirrie`, `Tugroob` restano invariati.

---

## 6. Correzioni fatte durante il lavoro

Nessuna soglia è stata toccata: si è riscritto il testo.

| unità | problema | intervento |
|---|---|---|
| 88 | resa piatta e ripetitiva di `Check the warehouse with the leaky roof` | «Controlla il magazzino dal tetto gocciolante.» |
| 111 | `Of course. Where are we headed?` reso troppo breve per il rapporto | «Certo che vengo. Dove dobbiamo andare?» |
| 167 | virgolette doppie interne al discorso diretto alteravano la parità per unità | citazione interna in apici singoli: `'tutto quello che possono fare'` |
| 134 / 153 | due inglesi quasi identici (`clearer` / `more clearly`): la prima resa italiana era identica per entrambi | differenziate: «vedere meglio il fondo» / «vedere il fondo con più chiarezza» |
| 270 / 303 | `Scanning Preparations` e `Preparations for Scanning` resi con la stessa frase: duplicato italiano non giustificato dal sorgente | 303 → «Preparare la scansione» |
| 450 | `Is this that expensive?` fuori dalla banda comoda (0,69) | «Vuoi dire che costa così tanto?» |
| 576, 595, 607, 611, 617 | titoli fuori dal gate: «Esercitazione di rifornimento» 1,93 · «Esercitazione di inseguimento» 2,23 ×3 · «Esercitazione di combattimento» 2,50 | «Prova di rifornimento» 1,40 · «Prova di inseguimento» 1,62 · «Scontro di prova» 1,33 |

Le tre unità identiche 595/607/611 hanno lo stesso inglese (`Pursuit Drill`) e quindi la stessa
traduzione: è un duplicato **giustificato dal sorgente**, come i due `expeditions past` in `NT`.

---

## 7. Controlli

`check.py` (sul lotto completo):

```
unita' richieste 663 · tradotte 663/663 · copertura 663/663
traduzioni vuote 0 · NT identiche (10 attese) · duplicati non giustificati 0
tab 509/509 · virgolette 878/878 · backtick 0/0 · token 181/181
tipografia ok · caratteri non latini ok · parole inglesi residue nessuna
state.db APPROVED/PENDING 364/32560 · unita' del lotto fuori da PENDING 0
FAIL totale: 0
```

`verify.py` (25 controlli indipendenti, exit 0): riga grezza identica al file sorgente; `english/kind/
path` identici al database e stato `PENDING`; nessuna unità `APPROVED`; id univoci; ordine identico al
sorgente; collocazione 663 unità, righe 16–2140, zero unità prima o dopo; copertura totale 663/663 da
un solo lotto; distribuzione dei kind come misurata; `NT` identiche; zero `CONVERSATION`; parità
esatta dei token; tab/virgolette/backtick uguali al sorgente; nessun italiano vuoto; nessun carattere
non latino; nessun trattino lungo; rapporto definito (0,73–1,68); le 11 parti su disco ricostruiscono
`translation.json`.

---

## 8. Limiti dichiarati

- **Nessun rendering nel gioco.** Le 663 unità non sono mai state caricate da Endless Sky. Le unità più
  lunghe (il discorso di Aulori sull'anello, unità 451, e il resoconto dell'incoronazione, unità 645–646)
  superano le 1.300 battute: **non è verificato** che stiano nelle schermate di dialogo del gioco.
- **Nessuna approvazione.** `APPROVED 364 · PENDING 32.560` al 2026-10-17T14:33:18Z, invariato.
- **Glossario non riconciliato.** I termini di questa tabella valgono per i file della Coalizione
  affrontati (L24–L26, L30, L31). `coalition jobs.txt`, `coalition news.txt`, `coalition outfits.txt`,
  `coalition ships.txt` e `coalition weapons.txt` restano da tradurre e possono richiedere aggiunte.
- **Lacuna di L30 non toccata**: riguarda `lunarium intro.txt`, non questo file.
