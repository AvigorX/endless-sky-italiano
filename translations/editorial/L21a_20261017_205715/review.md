# L21a — revisione editoriale

Ultimo segmento di `data/human/human missions.txt`: righe **10812–11777**, **465 unità**,
**11.046 parole inglesi → 10.356 italiane**, 16 contesti (missioni `Ice Queen` 1–8 e
`A Dead Man's Path` 1–2, più le due conversazioni `Ice Queen` / `Ice Queen End`).

Con questo segmento il file **è coperto al 100%**: 4.253 unità su 4.253 (L16+L17+L18+L19+L20+L21a).

## 1. Confini

- Inizio **10812**, `mission:Stone to Ice Queen`. L'unità precedente è la 10806, ultima di
  `mission:Stone to Hope` (chiusa in L20).
- Fine **11777**, ultima unità del file (`mission:A Dead Man's Path 2`). Dopo non c'è nulla:
  verificato con `select count(*) ... where line > 11777` = 0.
- Nessuna missione spezzata: il segmento copre missioni intere dall'inizio alla fine del file.

## 2. Tipi e classificazione (novità rispetto a L19/L20)

| tipo | n | trattamento |
|---|---:|---|
| `MISSION_TEXT` | 346 | prosa missione, tradotta |
| `CONVERSATION` | 80 | **testo di conversazione** (`text` backtick-delimitato): tradotto |
| `UI_LABEL` | 12 | `label` di missione: **invariate** |
| `VALUE` | 10 | nome missione, tradotto |
| `DESCRIPTION` | 10 | descrizione missione, tradotta |
| `DIALOG` | 5 | messaggio di dialogo, tradotto |
| `LOGBOOK` | 2 | voce di diario, tradotta |

**Il caso nuovo:** 7 delle 80 unità `CONVERSATION` non sono testo ma `label "..."` dentro un
blocco `conversation` (delimitatore `"` invece di backtick): 14, 20, 28, 35, 63, 69, 82.
Sono bersagli di `goto` dentro la conversazione e restano **identiche** al sorgente. Il
classificatore del database le assegna a `CONVERSATION` perché costruisce l'id dal testo:
non è un errore del database, ma un caso da gestire nel checker. Per questo `NT` contiene
**19 unità** (12 `UI_LABEL` + 7 `label` di conversazione) e `verify.py` le ricontrolla una
per una leggendo il `delimiter` da `source.json`.

## 3. Decisioni terminologiche

| EN | IT | nota |
|---|---|---|
| House Drifa / Drifa Manor | Casa Drifa / Drifa Manor | «casa» nobiliare resa con la maiuscola, come in italiano storico |
| Family-Cairn | Family-Cairn | invariato, coerente con L20 (`Stone to Hope`) |
| Blood of Surtr | Sangue di Surtr | artefatto: si traduce il nome comune, si mantiene il teonimo |
| Scales of Ran / Tear of Skade | Squame di Ran / Lacrima di Skade | idem |
| God-Stone | Pietra-Divina | con trattino, per distinguerla da «pietra» comune |
| Academy of Planetary Sciences | invariato | come L19; «l'Accademia» quando il testo dice `the Academy` |
| Second Degree Terraformer | Terraformatore di Secondo Grado | |
| Marauder (nave) | Marauder | classe di nave invariata, come in L20 |
| Valhalla, Nifel, Alfheim, Skadenga, Ranfolk, Ondurdis, Hrithfjall, Windblain | invariati | nomi propri e culturali |
| Eustace Goodfellow, Ildico Drifa/Drifa, Deoric, Hogne, Randalin, Sophie, Liam, Helm, Tosti, Ian McGiven, Grenwich Millstone, Albert Foster | invariati | nomi propri |
| «Murderous Heiress» | «Ereditiera Assassina» | epiteto di cronaca nera: tradotto, è un soprannome parlato |
| New Toulouse, New Pyrenees, New China, New Sydney, Clark, Chiron, Prime, Haven | invariati | toponimi |
| Betelgeuse (cantiere) / Behemoth | invariati | nome del costruttore e classe nave |

Registro: l'Ondurdis parla un inglese spezzato (verbi all'infinito, articoli mancanti); in
italiano è reso con lo stesso deficit («Dicono loro cultura e mondo stanno morendo»), senza
trasformarlo in dialetto regionale. I pirati di Haven usano un italiano basso («li ammazziamo
subito», «che ne dici»), Ildico un italiano freddo e formalissimo anche nelle minacce.

## 4. Casi editoriali

- **Testamento del padre** (444–447): tre unità con tre tab iniziali, scritte come epigrafe.
  Ho mantenuto i tab e il registro solenne, senza spezzare le frasi lunghe.
- **Frase in lingua inventata** (425): `Edr- i fen` resta identica — è una parola d'ordine
  fantasy, non inglese; tradurla distruggerebbe il riferimento ai romanzi del padre.
- **Lettere firmate** (169–171, 242–244): l'inglese apre la citazione e la chiude solo alla
  firma, su unità diverse. L'italiano riproduce i conteggi dispari (169 e 242 hanno una sola
  virgoletta, 171 e 244 solo quella di chiusura).
- **Bambina di due anni** (294–306): Randalin non parla; il testo dice «babbles something
  incoherent» → «farfuglia qualcosa di incomprensibile», senza inventare parole.
- **Violenza** (59–62, 197–200, 220–221): morte del giocatore, parricidio, arresto. Nessuna
  edulcorazione, nessun dettaglio aggiunto che l'originale non contenga.
- **Riferimento incrociato a L20** (5–34, 349–365): la missione `Stone to Hope` torna come
  `Stone to Hope: Thanks`. Ho riusato la stessa terminologia di L20 (`Family-Cairn`,
  `Snaiwaz`, Tosti, Helm) per non creare due versioni dello stesso oggetto narrativo.

## 5. Correzioni effettuate

- Unità **51, 54, 97, 231, 279, 396, 449**: citazioni allineate al conteggio del sorgente
  (dispari) invece di essere chiuse d'ufficio.
- Unità **226**: `oranate` (refuso inglese) → «ornata». Non è una correzione di controllo ma
  una scelta di resa: il refuso dell'originale non si propagava.



Elenco aggiornato delle unità con virgolette allineate al conteggio dispari del sorgente:
**51, 54, 97, 212, 231, 278, 279, 331, 396, 449**, più **364** lasciata aperta come nel testo.

## 6. Controlli

`check.py`: **FAIL totale 0** (465/465, tab 417/417, virgolette 548/548, token 64/64,
duplicati inglesi 13 gruppi/26 unità, nessun inglese residuo, nessun carattere non latino).

`verify.py`: **22 controlli, 0 FAIL, exit 0** — riga grezza, DB, `PENDING`, ordine, intervallo,
fine file, unità precedente, copertura 4.253/4.253, nessuna sovrapposizione fra lotti,
19 non traducibili identiche, token/tab/virgolette, vuoti, caratteri, rapporti, ricostruzione
delle parti.

Rapporto IT/EN: min 0,69 · max 1,71.

## 7. Cosa non è stato fatto

Nessuna scrittura in `state.db` o negli output approvati; nessuna patch K4; nessuna build o
applicazione al gioco; **rendering non verificato** (fuori dal perimetro).
