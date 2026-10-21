# L37 — revisione editoriale

Lotto `L37_20261018_122434` · `data/human/free worlds 3 checkmate.txt` · righe 16–2463 · 482 unità ·
16.244 parole EN → 15.239 IT · `check.py` `FAIL totale: 0` · `verify.py` 28 controlli, exit 0.

Questo documento registra **le decisioni**, non i numeri: i numeri stanno in `REPORT.md` e sono
rigenerabili con i due comandi di verifica.

---

## 1. Che cosa copre il lotto

Terzo degli atti centrali delle Free Worlds, e come i file di L32–L36 **finisce con il lotto**: riga 16
prima unità, riga 2463 ultima. La copertura 482/482 è quindi un invariante legittimo.

In ordine: la ricognizione e l'attacco a Kaus Borealis, con il ritorno di Tomek reintegrato e la
rivelazione che il Branco di Lupi usa testate nucleari comprate con l'uranio di Greenrock; Cebalrai e la
sua cattura; il convoglio di uranio e il convoglio di testate; il secondo tentativo diplomatico sulla
Terra, che finisce con un processo per tradimento e una minaccia di bombardamento orbitale con barre di
tungsteno; la difesa di Tundra e la decisione dell'opzione «scacco matto»; Menkent e Vega; l'arrivo dei
Pug, il taglio dei collegamenti iperspaziali e l'invasione; Shiver e il mondo natale dei Pug; la fuga
col motore di salto, la cattura di Freya, l'alleanza con la Marina e i Quarg; la liberazione dei sistemi
e la scoperta che le città Pug erano scenografie costruite per gli umani; il trattato di pace e lo
scioglimento del Consiglio.

## 2. Ricognizione (misurata sul `source.json`, non dedotta)

```
MISSION_TEXT 356 · VALUE 36 · DESCRIPTION 36 · LOGBOOK 27 · DIALOG 27 · UI_LABEL 0
contesti 37 · tab 305 · virgolette 900 · token 121
unità con numero dispari di virgolette: 0
unità con quadre: 1 (143, riga 980: una coppia che racchiude l'intera riga)
righe `log`: 27 → 27 unità LOGBOOK (1:1), nessuna a tre argomenti, nessuna categoria
```

Due fatti che hanno richiesto preparazione e **non** si potevano copiare da L36:

- **`UI_LABEL` torna a 0** (in L36 erano 3, in L35 una più una categoria): `NT` vuoto. Copiare
  `{407, 501, 503}` avrebbe messo in `NT` tre unità che in questo file sono testo normale, lasciandole
  in inglese.
- **Le quadre**: l'unità 143 è un avviso al giocatore racchiuso fra `[` e `]`. In L33 le quadre erano il
  dispositivo `[a, b]` con gruppi di alternative; qui è una cornice. Il controllo va quindi sul **numero
  di coppie per unità**, non sulle alternative — e l'asserzione «0 unità con quadre» sarebbe stata
  semplicemente falsa.

## 3. Metodo

1. `export_section.py` su righe 16–2463 → 482 unità, 37 contesti.
2. Ricognizione dei tipi, delle righe `log`, delle quadre, delle virgolette dispari.
3. `check.py` derivato da L36 con `NT = set()`, e **nuovo controllo `quadre [ ] per unita`**.
4. Traduzione in 11 parti a fine contesto, ognuna chiusa con `check.py --range` verde.
5. `check.py` completo e `verify.py` indipendente con due asserzioni sulle quadre.

Le parti: 1–49, 50–109, 110–147, 148–210, 211–269, 270–325, 326–361, 362–392, 393–422, 423–459, 460–482.

## 4. Le voci di questo file

**Tomek Voigt.** Torna reintegrato, e il registro è quello di L35 senza l'ira: parla da militare che ha
avuto ragione e non lo ricorda a ogni frase. Il suo tratto qui è la **reticenza**: ammette che la
situazione delle testate non gli piace («Il che, per inciso, continua a non piacermi») e si ferma lì,
senza moraleggiare. L'unica volta che alza la voce è per chiudere una discussione («Ci hanno lasciato
qualche altra scelta?»).

**Katya Reynolds.** Il suo registro è il più duro del lotto, e non per volume: parla per domande secche
(«Quindi ora usate le testate nucleari? Di chi è stata questa dannata idea?»). La traduzione ha tenuto
«dannata» perché è l'unico imprecazione del personaggio in 482 unità e caratterizza più di una frase
intera.

**Freya Winters.** Due registri che si alternano: l'entusiasmo tecnico («I cantieri Southbound stanno
sfornando Dreadnought adesso!», «Ho un ciclo di retroazione positivo») e il sospetto metodico
(«Non ti sembra tutto un po' troppo... pulito?»). Il secondo è quello che porta il tema del lotto: i Pug
sembrano **lasciarsi vincere**.

**Danforth.** Il militare che vuole la pace e lo dice in una riga: «Non voglio il merito, voglio la pace».
Il resto del personaggio è coerente con L36 — onore, prigionieri, procedura — ma qui l'accento è sulla
costruzione di una narrazione condivisa («Il punto è come raccontiamo questa storia»).

**I Quarg.** Registro costruito su tre tratti: frasi brevi, terza persona per gli interlocutori («Questi
qui hanno domande?»), e una ammissione di limite metodico («è la migliore comprensione che siamo
riusciti a raggiungere della loro specie»). La spiegazione della guerra-gioco dei Pug è il cuore del
lotto e in italiano è resa senza abbreviazioni: «Se vogliono la guerra, dovete giocare al loro gioco, e
se giocate al loro gioco, potrebbero permettervi di vincere.»

**Raven.** Poche righe, tutte definitive. Compare come guardia del corpo e si scopre Interrogatrice.

## 5. Il tema: i Pug si lasciano vincere

Il lotto costruisce un sospetto in cinque passaggi misurati nel testo:

1. 351 — Freya: «Combacia tutto fin troppo bene.»
2. 372 — i Quarg: «hanno spezzato uno dei nostri anelli».
3. 377/381 — «In battaglia i Pug rispondono sempre con la forza appena sufficiente».
4. 410 — le stazioni trasmettitrici **abbandonate ma funzionanti**.
5. 437/458 — le città erano scenografie, progettate per abitanti umani.

La traduzione ha tenuto **il dubbio aperto**: nessuna riga aggiunge una spiegazione che il testo non dà,
e in particolare l'ipotesi finale (che i Pug volessero dare all'umanità un nemico comune) resta
un'ipotesi, con il «È possibile che...» del sorgente.

## 6. Decisioni lessicali

| inglese | italiano | perché |
|---|---|---|
| Pug, Quarg, Drak | invariati | specie aliene, nomi propri |
| Pug Protectorate | Protettorato Pug | istituzione descritta dal testo |
| Pugglemug | Pugglemug | nome proprio del pianeta (in inglese resta fra virgolette) |
| graviton detector / reflector | rivelatore / riflettore di gravitoni | |
| hyperspace link | collegamento iperspaziale | |
| jump drive | motore di salto | glossario |
| ringworld | mondo ad anello | descrizione, non nome proprio |
| Speaker (del Parlamento) | il Presidente | carica; «Speaker» in italiano non esiste e «portavoce» è altro |
| Questioner | Interrogatore (una degli Interrogatori) | corpo dell'Intelligence, come in L36 |
| tributation | tributazione | termine inventato dal testo, reso con un calco trasparente |
| sclera tattoo | tatuaggio sclerale | descrizione anatomica, come in L36 |
| tungsten rods | barre di tungsteno | |
| the Big Brother, Blue Yonder | la Big Brother, la Blue Yonder | nomi di nave, con articolo italiano |

**I numeri**: «seventeen thousand credits per diem» → «diciassettemila crediti al giorno»; «eight
kilometers per second» → «otto chilometri al secondo».

## 7. La lacuna `log`: qui non perde niente

Misurato: **27 righe `log` → 27 unità `LOGBOOK`** (1:1), **nessuna** a tre argomenti, **nessuna**
categoria emersa. Come in L36, l'inventario è completo rispetto al file. La lacuna resta in
`tools/l10n.py` (protetto) e qui non c'era nulla da documentare come perdita: il fatto è registrato
perché è una **misura**, non un'assenza di controllo.

## 8. Cosa è stato corretto e perché

- **140** e **179**: sotto la banda comoda (0,643 e 0,645). Riscritte in «Capito. Partiremo
  immediatamente.» e «(Resta qui e parlagli.)», allungando senza aggiungere contenuto.
- **143**: il testo fra le quadre è stato tradotto **per intero** e la coppia di quadre conservata: il
  controllo per unità ha verificato 1 `[` e 1 `]` in entrambe le lingue.
- **443**: refuso di stesura («Sparì un solo colpo»); corretto in «Spara un solo colpo».
- **273/274, 302/305, 310/311 e 351/354**: coppie di varianti dello stesso passaggio (Danforth
  riconosciuto o già incontrato; flotta superstite o no; carico già a bordo o no). Tenute distinte, come
  nell'inglese, senza unificare.
- **Nessuna battuta aperta**: il file non ha unità con numero dispari di virgolette, e il `verify.py`
  confronta insiemi vuoti invece di fidarsi del totale.

## 9. Controlli e limiti

`check.py` (22 controlli) verifica: copertura, unità vuote, `NT` identiche, duplicati italiano spiegati
dal sorgente, tab e virgolette per unità e come totale, **quadre per unità**, token `<...>`, backtick,
spazi, rapporto lunghezze, tipografia, caratteri non latini, parole inglesi residue, stato del database.

`verify.py` (28 controlli) **non riusa** la logica di `check.py`: ricostruisce tutto da `source.json`, dal
file sorgente e da `state.db` in sola lettura, e in più asserisce (a) che le `UI_LABEL` siano zero,
(b) che l'unica unità con quadre sia la 143 e che ne conservi una coppia, (c) che le virgolette dispari
siano esattamente quelle del sorgente (nessuna), (d) che le 11 parti ricostruiscano `translation.json`,
(e) la copertura totale 482/482 del file da un solo lotto.

Limiti, dichiarati:

- **Il lotto non è nel gioco.** Nessuna approvazione nel database, nessun caricamento: 482 unità
  `PENDING`.
- **Nessuna verifica nell'editor.** In particolare non è verificato come venga reso a schermo il testo
  lungo dell'unità 143 fra le quadre, né la sequenza dei Pug olografici (440–458), che ha molte unità
  brevi in successione.
- **Il rapporto 0,77–1,62 non è un giudizio di qualità.**
