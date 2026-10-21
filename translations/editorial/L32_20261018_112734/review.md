# L32 — revisione editoriale

`data/wanderer/wanderers start.txt`, righe 23–3092 · 805 unità · 24.166 parole inglesi.
Lotto che **chiude il file** (12º file completo dello staging). Nessuna unità è stata approvata nel
database: lo staging non è approvazione.

---

## 1. Che cosa copre il lotto

Dodicesimo file chiuso e primo della fazione **Wanderers**: il primo contatto, la loro cosmologia e la
guerra contro gli Hai Slegati.

| unità | contenuto |
|---|---|
| 1–100 | primo contatto con la specie avicola, l'interprete Hai, Sayari, la macchina parlante di Eruk |
| 101–165 | Iktat Rek, l'**Occhio** e la **Muta**, il sospetto sui Pug, il primo trasporto |
| 166–231 | difesa dall'incursione, il **tributo** agli Slegati, il cessate il fuoco |
| 232–370 | vendita del motore di salto, cubi di sorveglianza, gli **Alphas**, il Carrier della Marina |
| 371–483 | Avalon, Danforth, l'assalto alla base, l'arresto, Elias Hanover |
| 484–612 | invasione, evacuazione, consiglio di guerra, i Pug che rifiutano, mediazione con gli Hai |
| 613–736 | il Solifuge, Osen, la Muta che avanza, la madre di Rek |
| 737–805 | i tre viaggi a Sko'karak, il fenomeno, la quarantena, l'arrivo dei **Custodi** |

---

## 2. Ricognizione (misurata sul `source.json`, non dedotta)

```
MISSION_TEXT 561 · DESCRIPTION 58 · VALUE 53 · CONVERSATION 47 · DIALOG 45 · LOGBOOK 40 · TEXT 1
UI_LABEL 0
contesti 69, da `Wanderers: Pre-Colony` a `wanderers: sestor planets unrestricted`
tab 512 · virgolette 1.305 · token 173 · virgolette dispari 1 unità (161)
parentesi quadre 112 unità
```

- **`UI_LABEL` 0**: qui le etichette di salto non sono `UI_LABEL` ma `CONVERSATION` (sotto), quindi la
  lista di L31 non si poteva copiare.
- **`CONVERSATION` 47**: contenitore misto (decisioni 77 e 100). 45 sono **testo visibile** del blocco
  `conversation` (tradotto come prosa); 2 sono `label` di salto — 646 `alt start` e 671 `alt end` —
  che restano identiche.
- **`TEXT` 1** (unità 346): `"Bondir" Atomic Thruster`, un **riferimento a un outfit** dentro la lista
  `outfits` della Carrier (riga 1231), fra backtick nel sorgente perché contiene virgolette. Non è
  prosa: sta in `NT`.
- **`LOGBOOK` 40**: qui la lacuna dell'inventario ha la forma opposta a L30 (vedi §7).
- **Virgolette dispari: solo l'unità 161**, che apre la citazione e la lascia aperta (continua nella
  162). Riprodotta.

---

## 3. Metodo

1. `export_section.py` ha esportato le righe 23–3092 in `source.json` (805 unità).
2. `check.py` derivato da L31: `NT` rimisurato (3 elementi), docstring riscritta, `TITLES` esteso ai
   nomi dei Wanderers e degli Alphas, **controllo nuovo per le parentesi quadre**.
3. Traduzione in **13 parti**, tutte chiuse a fine missione, ognuna con `check.py --range` verde:

   | parte | unità | n. | parte | unità | n. |
   |---|---|---:|---|---|---:|
   | 01 | 1–45 | 45 | 08 | 423–483 | 61 |
   | 02 | 46–100 | 55 | 09 | 484–555 | 72 |
   | 03 | 101–165 | 65 | 10 | 556–612 | 57 |
   | 04 | 166–231 | 66 | 11 | 613–675 | 63 |
   | 05 | 232–290 | 59 | 12 | 676–736 | 61 |
   | 06 | 291–370 | 80 | 13 | 737–805 | 69 |
   | 07 | 371–422 | 52 | | | |

4. Tab iniziali derivati dal sorgente (512 IT = 512 EN); virgolette per unità confrontate una a una
   (1.305 = 1.305).
5. Dopo ogni parte anche il **controllo completo**, che è l'unico a vedere i duplicati fra parti.

---

## 4. La voce dei Wanderers

Nessun lessico ereditato dalla Coalizione: qui la voce si ricava dal testo e ha tre registri distinti,
tutti deliberati.

**a) I Wanderers parlano in modo piano e cortese**, non con l'ordine marcato dei Kimek/Saryd/Arach:

- `"It is very [rare, exceptional] in our history that we have to [deal with, cope with] other
  species"` → «È molto [raro, eccezionale] nella nostra storia dover [trattare con, convivere con]
  altre specie»
- `"This we guessed when they first raided us"` → «Lo abbiamo intuito quando ci hanno fatto la prima
  incursione»

**b) Il dispositivo di traduzione di Eruk parla come una macchina**: periodi interi, nessun
troncamento, e nella scena del Pug (335–341) la voce è **monotona e senza punteggiatura**, perché è
così che il testo la descrive. Esempio (337):

> `"Humans are not our responsibility why have you come to our planet."` → «Gli umani non sono nostra
> responsabilità perché sei venuto sul nostro pianeta.»

La mancanza di punteggiatura è un effetto voluto, non una svista: il testo dice che la scatola parla
«senza pause fra le frasi».

**c) I Pug parlano di sé in terza persona**: `"It appears to this one that the human is not intending
to just politely return to its vessel"` → «A questo sembra che l'umano non abbia intenzione di tornare
educatamente sulla sua nave». È un tratto della specie, non una scelta di cortesia italiana.

---

## 5. Le parentesi quadre: struttura, non stile

112 unità contengono `[parola, parola]`. Il gioco mostra **una sola alternativa** per volta: ogni
alternativa deve reggere la frase da sola, e il numero di alternative deve restare quello del
sorgente. Il `check.py` di questo lotto lo verifica per unità.

| sorgente | resa | perché |
|---|---|---|
| `It is very [rare, exceptional]` | «È molto [raro, eccezionale]» | entrambe concordano con «molto» |
| `a single Hai ship [visited, invaded] us` | «una sola nave Hai [ci ha visitato, ci ha invaso]» | il pronome resta dentro l'alternativa |
| `a [taboo? religion? mystery?] for us` | «un [tabù? religione? mistero?]» | tre alternative senza virgola: **un solo** gruppo |
| `[Sow, scatter, deploy] several of these` | «[Semina, spargi, schiera] diversi di questi» | tre imperativi, tutti validi |
| `their [being, essence]` | «il loro [essere, essenza]» | articolo fuori dalla parentesi |
| `[giants, people of renown]` | «[giganti, gente di fama]» | nome collettivo, non «persone famose» |

Due casi in cui la resa letterale non reggeva e la frase è stata riscritta **intorno** alla parentesi:
`[combattere? preoccuparci de] gli Hai` (unità 797) è diventata
`[combattere contro? preoccuparci di?] gli Hai`, e `[consomare? sostituire?] ogni cellula` (621) è
diventata «[consuma? sostituisce?] ogni cellula» per tenere il verbo finito.

---

## 6. Decisioni lessicali

| inglese | italiano | motivo |
|---|---|---|
| `the Eye` | **l'Occhio** | nome del cunicolo nella loro cultura; tradotto perché descrittivo |
| `the Molt` | **la Muta** | `molt` = muta; con la maiuscola è il nome del fenomeno |
| `Keepers` | **Custodi** | `Keepers of the Eye` → Custodi dell'Occhio |
| `Unfettered` | **Slegati** | glossario di L29, invariato |
| `unfettered humans` | **umani senza freni** | è così che i Pug chiamano gli Alphas: **non** «Slegati», che è la fazione Hai |
| `speaking machine` | macchina parlante | distinta dal `translation device` (dispositivo di traduzione) |
| `jump drive` / `hyperdrive` | motore di salto / iperpropulsore | glossario generale |
| `Carrier`, `Cruiser`, `Riptide`, `Tempest`, `Solifuge` | invariati | modelli di nave |
| `Oathkeepers` | invariato | branca della Marina, nome proprio |
| `Dirt Belt`, `Deep`, `Farpoint` | invariati | regioni e luoghi |

---

## 7. La lacuna di inventario qui ha la forma opposta a L30

In L30, `log "Factions" "Lunarium Redoubt" "<testo>"` produceva **una** unità, e quell'unità era la
**categoria**: il testo del diario si perdeva.

In questo file le righe a tre argomenti sono 12 (per esempio unità 54 `log "People" "Sayari" `…``,
70 e 109 `log "Factions" "Wanderers" `…``). Anche qui il database produce **una sola unità per riga**,
ma l'unità è il **testo del diario** (verificato: `english` di 54 comincia con «Ambassador Sayari, a
Hai, served as their envoy…»). Quindi:

- la parte **traducibile è presente e coperta**;
- categoria (`People`, `Factions`) e nome (`Sayari`) **non sono inventariati** e restano in inglese,
  ma non sono prosa visibile al giocatore nella scena;
- la lacuna va dichiarata, non riparata: `tools/l10n.py` e `state.db` sono protetti.

La lezione operativa: **la stessa forma di sorgente produce lacune diverse in file diversi**, quindi il
`raw` va letto e l'`english` verificato, non dedotto dal tipo.

---

## 8. Controlli e limiti

`check.py` (lotto completo): 805/805 unità, traduzioni vuote 0, `NT` 3 identiche, duplicati non
giustificati 0, tab 512/512, virgolette 1.305/1.305, token 173/173, parentesi quadre coerenti su 112
unità, tipografia ok, caratteri non latini ok, parole inglesi residue nessuna, `FAIL totale: 0`.

`verify.py` (26 controlli indipendenti, exit 0): riga grezza identica al sorgente; `english/kind/path`
identici al database e stato `PENDING`; nessuna `APPROVED`; id univoci; ordine identico; collocazione
805 unità righe 23–3092; zero unità prima o dopo; copertura totale 805/805 da un solo lotto; kind come
misurati; `NT` identiche; 47 `CONVERSATION` di cui 2 `label`; parità esatta dei token; parentesi quadre
identiche; tab/virgolette/backtick uguali; nessun italiano vuoto; nessun carattere non latino; nessun
trattino lungo; rapporto 0,72–1,61; le 13 parti ricostruiscono `translation.json`.

**Limiti dichiarati**

- **Nessun rendering nel gioco.** Le 805 unità non sono mai state caricate da Endless Sky. In
  particolare **non è verificato** che le parentesi quadre vengano risolte correttamente a schermo né
  che le 47 `CONVERSATION` stiano nella finestra di dialogo.
- **Nessuna approvazione.** `APPROVED 364 · PENDING 32.560`, invariato.
- **Glossario non riconciliato** con i file non ancora affrontati: `wanderers middle.txt` (L33) usa lo
  stesso lessico e va verificato sul suo `source.json`, non dato per acquisito.
