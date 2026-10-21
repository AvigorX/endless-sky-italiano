# L39 — revisione editoriale

Lotto `L39_20261018_124057` · `data/human/free worlds 4 epilogue.txt` · righe 22–341 · 114 unità ·
3.487 parole EN → 3.209 IT · `check.py` `FAIL totale: 0` · `verify.py` 29 controlli, exit 0.

Questo documento registra **le decisioni**, non i numeri: i numeri stanno in `REPORT.md` e sono
rigenerabili con i due comandi di verifica.

---

## 1. Che cosa copre il lotto

L'epilogo della campagna delle Free Worlds: quattro visite facoltative, una per personaggio, più la prova
di un'arma. In ordine: Ijs e Katya al Conservatorio (con la cena e la scoperta della parentela),
Alondo su Bourne (il corpo diplomatico), Freya sul mondo dei Pug (l'ipotesi del giocattolo didattico e la
rivelazione dei bisnonni), Danforth su Farpoint (gli Oathkeepers che crescono, l'intelligence che resta
sul Sindacato), e infine Barmy Edward alla Kraz Cybernetics (il Ripetitore al plasma e una serata al bar).

È il **primo file della serie in cui non c'è niente da decidere**: nessuna battaglia, nessun bivio con
conseguenze. Il registro è perciò quello del congedo, e la traduzione lo ha trattato come tale.

## 2. Ricognizione (misurata sul `source.json`, non dedotta)

```
MISSION_TEXT 77 · CONVERSATION 34 · VALUE 1 · DESCRIPTION 1 · LOGBOOK 1 · UI_LABEL 0
contesti 6 · tab 105 · virgolette 258 · token 16
unità con numero dispari di virgolette: 0
unità con quadre: 0
righe `log`: 1 → 1 unità LOGBOOK
prima unità alla riga 22 (non 16)
```

Due fatti che hanno richiesto preparazione:

- **34 `CONVERSATION` su 114 unità** (30%): il secondo atto del file è un colloquio continuo con Barmy
  Edward. Va letto tutto prima di scrivere, perché le battute si rispondono e i pronomi si riferiscono al
  turno precedente.
- **`UI_LABEL` = 0**: `NT` vuoto, e il `verify.py` asserisce che il file non abbia nessuna `UI_LABEL`.
  Copiare `{139, 308}` da L38 avrebbe messo in `NT` due unità che qui sono testo normale, lasciandole in
  inglese.

## 3. Metodo

1. `export_section.py` su righe 22–341 → 114 unità, 6 contesti.
2. Ricognizione dei tipi, delle righe `log`, delle quadre, delle virgolette dispari.
3. `check.py` derivato da L38 con `NT = set()`.
4. Traduzione in 2 parti a fine contesto (1–63, 64–114), ognuna chiusa con `check.py --range` verde.
5. `check.py` completo e `verify.py` indipendente con asserzione su `CONVERSATION` e sulle quadre.

## 4. Le voci di questo file

**Ijs Springborn.** Il professore che finalmente può scherzare: «Ops, ora l'hai fatto, è caduta la quarta
parete.» Il suo registro è quello di sempre (entusiasta, un po' imbranato), ma alleggerito: non spiega
niente, non insegna niente, e quando può fa una battuta.

**Katya Reynolds.** La più cambiata: nella guerra era la voce più dura del lotto L37, qui dice che
«dopo tanto tempo da sola e in prigione» le fa bene potersi rilassare. La traduzione ha tenuto il
contrasto senza commentarlo: la frase è breve e non si giustifica.

**Alondo Gruyere.** Il burocrate felice: parla della burocrazia come di un lavoro utile e ammette che
«per un po' sembrava che non riuscivamo a combinare niente». Il registro è quello di sempre, con una
punta di autoironia che prima non aveva.

**Freya Winters.** La scienziata che non ha smesso: il suo monologo (unità 38–39) è il cuore del file, e
la traduzione ha reso l'immagine chiave — «un giocattolo didattico», «come un genitore distratto che
lascia ai figli un set di chimica superavanzato» — senza spiegarla di più. Anche la rivelazione della
parentela è resa con la stessa secchezza: «Credo che siamo parenti. Cugini di secondo grado.»

**Danforth.** Il militare che non si arrende: «Non andrò mai in pensione dalla Marina. Conto di essere
ancora in servizio il giorno in cui morirò.» Il secondo registro è quello dell'intelligence, che parla
sottovoce e cambia argomento.

**Barmy Edward.** Il comico tecnico: parla per entusiasmi, si strofina le mani, e la sua idea di festa è
«un baretto grazioso». Il registro è lo stesso di L36 («cannoncini mollaccioni»), senza volgarità nuove.

## 5. Le due rotture della quarta parete

Il file contiene due battute metaletterarie, entrambe nel primo dialogo:

- **unità 9**: «Voglio esplorare il resto della galassia, ma a quanto pare quella parte del gioco non è
  ancora stata implementata del tutto.»
- **unità 12**: «Ops, ora l'hai fatto, è caduta la quarta parete.»

Sono **battute del gioco, non note dell'autore**: la traduzione le ha rese come tali, senza virgolette
di scusa e senza spiegarle. La seconda dipende dalla prima, e in italiano funziona perché «cadere la
quarta parete» è un'espressione già in uso.

L'unità 13 completa il gesto: Katya invita il giocatore a contribuire alle storie del gioco perché «è un
gioco open source, e si basa su gente come te per prendere vita». Reso alla lettera.

## 6. Decisioni lessicali

| inglese | italiano | perché |
|---|---|---|
| second cousin | cugino di secondo grado | grado di parentela preciso: «cugino» da solo cambierebbe il rapporto |
| visiting professor | professore a contratto | ruolo accademico, reso con il termine italiano corrente |
| Plasma Repeater | Ripetitore al plasma | nome dell'arma nuova, distinto dal «cannone al plasma» |
| Plasma Cannon | cannone al plasma | equipaggiamento già in uso nei lotti precedenti |
| Kraz Cybernetics | Kraz Cybernetics | nome di azienda, invariato |
| Conservatory | Conservatorio | istituzione, come in L35 |
| the fourth wall | la quarta parete | espressione già in uso in italiano |
| educational toy / chemistry set | giocattolo didattico / set di chimica | immagini del testo, rese alla lettera |
| homely little bar | baretto grazioso | «homely» qui vale accogliente, non brutto |
| New Boston | New Boston | pianeta, invariato |
| Farpoint, Bourne, Skymoot, Valhalla | invariati | pianeti |

**I numeri**: nessun importo in questo file; i token sono `<first>`, `<last>`, `<origin>`, `<planet>`,
`<npc>`.

## 7. La lacuna `log`: qui non perde niente

Misurato: **1 riga `log` → 1 unità `LOGBOOK`** (1:1), nessuna forma a tre argomenti, nessuna categoria
emersa. L'inventario è completo rispetto al file; la lacuna generale resta in `tools/l10n.py` (protetto).

## 8. Cosa è stato corretto e perché

Il lotto non ha avuto FAIL: nessuna unità fuori dal gate, nessun duplicato non spiegato, nessuna parola
inglese residua. Le correzioni sono state di rifinitura, fatte prima del controllo:

- **9, 12, 13**: le tre battute metaletterarie, riscritte per non sembrare note dell'autore.
- **47–62**: tutta la sequenza Lavinia/Marcus è stata riscritta per tenere la progressione
  (nome vago → ricordo → bisnonni → cugini di secondo grado) e per non anticipare la rivelazione.
- **52**: il periodo lungo del sorgente («spremendoti le meningi...») è stato tenuto lungo: è il momento
  in cui il giocatore capisce, e accorciarlo toglierebbe la suspense.
- **79**: «mettila fuori uso (ma non abbordarla né distruggerla!)» — le due negazioni sono enfatiche nel
  sorgente e restano enfatiche.
- **107 vs 113**: due varianti dello stesso passaggio (Barmy racconta la sua infanzia in modo generico o
  la colloca su New Boston). Tenute distinte, come nell'inglese.

## 9. Controlli e limiti

`check.py` (22 controlli): copertura, unità vuote, `NT` identiche, duplicati italiano spiegati dal
sorgente, tab e virgolette per unità e come totale, quadre per unità, token `<...>`, backtick, spazi,
rapporto lunghezze, tipografia, caratteri non latini, parole inglesi residue, stato del database.

`verify.py` (29 controlli) **non riusa** la logica di `check.py`: ricostruisce tutto da `source.json`, dal
file sorgente e da `state.db` in sola lettura, e in più asserisce (a) che le `UI_LABEL` siano zero,
(b) che le `CONVERSATION` siano 34 e tutte tradotte, (c) che non ci siano quadre in nessuna delle due
lingue, (d) che le virgolette dispari siano esattamente quelle del sorgente (nessuna), (e) che le 2 parti
ricostruiscano `translation.json`, (f) la copertura totale 114/114 e la coppia di righe (22, 341).

Limiti, dichiarati:

- **Il lotto non è nel gioco.** Nessuna approvazione nel database, nessun caricamento: 114 unità
  `PENDING`.
- **Nessuna verifica nell'editor.** In particolare non è verificato come venga reso a schermo il blocco
  `CONVERSATION` 81–114, che nel gioco ha un'interfaccia propria.
- **Il rapporto 0,72–1,50 non è un giudizio di qualità.**
