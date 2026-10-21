# L38 — revisione editoriale

Lotto `L38_20261018_123202` · `data/human/free worlds 3 reconciliation.txt` · righe 31–2729 ·
596 unità · 21.021 parole EN → 20.228 IT · `check.py` `FAIL totale: 0` · `verify.py` 29 controlli,
exit 0.

Questo documento registra **le decisioni**, non i numeri: i numeri stanno in `REPORT.md` e sono
rigenerabili con i due comandi di verifica.

---

## 1. Che cosa copre il lotto

L'atto della ricostruzione: dalla scelta di salvare il disertore del Sindacato al trattato di pace, fino
allo scioglimento del Consiglio. In ordine: l'incontro con Raven e la spiegazione degli «empati»; Ijs al
Conservatorio e le impronte isotopiche su Mutiny; l'udienza in Parlamento che si trasforma in un processo
a Sawyer; il Deep e la proposta di «azione di polizia» di Edrick Flint; Stormhold e le informazioni
comprate; la difesa di Farpoint; l'ambasciata; la cattura di Alexander Soylent su Nimbus e la fuga sotto
il fuoco nucleare; il Parlamento che chiede al giocatore di rischiare; il Sindacato che si scopre vittima
dei Pug; i Quarg che spiegano la guerra-gioco; la flotta congiunta, Maker, Delta Capricorni, il riflettore
di gravitoni, Altair, la battaglia finale e — dopo la partenza dei Pug — il conto con gli Alphas e
l'Oracolo, il dispositivo di occultamento, Buccaneer Bay, la menzione del Parlamento.

## 2. Ricognizione (misurata sul `source.json`, non dedotta)

```
MISSION_TEXT 425 · VALUE 42 · DESCRIPTION 42 · LOGBOOK 41 · DIALOG 35 · UI_LABEL 2 · CONVERSATION 9
contesti 51 · tab 361 · virgolette 1004 · token 119
unità con numero dispari di virgolette: 2 (45, 546)
unità con quadre: 1 (426, una coppia)
righe `log`: 41 → 41 unità LOGBOOK (1:1), nessuna a tre argomenti, nessuna categoria
prima unità alla riga 31 (non 16)
```

Tre fatti che hanno richiesto preparazione e **non** si potevano copiare da L37:

- **`UI_LABEL` torna a 2** (in L37 era 0), e sono due `label` di salto in un dialogo a scelte: `NT`
  non è vuoto. Copiare la lista vuota di L37 avrebbe lasciato in inglese due label e rotto due `goto`.
- **`CONVERSATION` 9**: primo file della serie con un blocco di conversazione vero e proprio. Il tipo è
  solo un'etichetta dell'inventario, ma il blocco (403–411) va tradotto come un dialogo continuo, con i
  turni che si rispondono: il `verify.py` lo asserisce.
- **Il file inizia a riga 31**: la coppia `(first, last)` andava misurata. Il `verify.py` asserisce
  `(31, 2729)`, non `(16, ...)`.

## 3. Metodo

1. `export_section.py` su righe 31–2729 → 596 unità, 51 contesti.
2. Ricognizione dei tipi, del `raw` delle due `UI_LABEL`, delle righe `log`, delle quadre, delle
   virgolette dispari.
3. `check.py` derivato da L37 con `NT = {139, 308}`.
4. Traduzione in 14 parti a fine contesto, ognuna chiusa con `check.py --range` verde.
5. `check.py` completo e `verify.py` indipendente con asserzione su `CONVERSATION` e sulle quadre.

Le parti: 1–58, 59–100, 101–140, 141–169, 170–201, 202–234, 235–285, 286–342, 343–384, 385–419,
420–457, 458–518, 519–558, 559–596.

## 4. Le voci di questo file

**Raven.** È il personaggio nuovo che porta il registro più controllato del lotto: frasi brevi, nessuna
spiegazione non richiesta, e una cortesia che non ammorbidisce («Non ringraziarmi. Sto solo badando a me
stessa.»). Quando spiega cosa sono gli «empati» lo fa in un italiano tecnico e piano, senza misticismo:
«Il termine ufficiale per noi è 'empati'.» — e ammette di non sapere come funzioni.

**Alondo.** Torna diplomatico e diventa il contrappeso morale: è lui a imporre la condizione a Korban
(«Ci darete subito uno dei vostri motori di salto»), ed è lui a fermare il giocatore quando la rabbia
rischia di far saltare l'accordo («Basta così. Le riparazioni le sistemeremo dopo.»).

**Freya.** Nel lotto precedente era la tecnica entusiasta; qui è la scienziata che ammette di procedere
alla cieca («Sto andando in gran parte alla cieca», «Non sono sicura di niente»). Il registro regge perché
l'ammissione non è modestia ma metodo: dice anche che «a volte l'intuito ci porta terribilmente fuori
strada».

**Alastair Korban.** Il dirigente che ha deciso di dimettersi: parla per frasi lunghe, con subordinate
difensive, e passa dall'arroganza alla confessione senza transizione. La resa italiana conserva la
cacofonia dei suoi «abbiamo preso una decisione sbagliata dopo l'altra»: è un uomo che si sta
giustificando, non un pentito esemplare.

**Edrick Flint.** Il governatore che parla per categorie giuridiche («tecnicamente legale»), con un
understatement che diventa comico quando Ijs lo smonta.

**Ijs Springborn.** Il professore: entusiasta, imbarazzato, e l'unico che nel lotto parla di «eroe» al
plurale («lei è il mio eroe»). Il registro resta quello di L34, con più stanchezza.

## 5. Il tema: la guerra come scelta economica

Il lotto chiude il cerchio aperto in L36 con il disertore: la guerra è cominciata perché un modello
predittivo diceva che una recessione sarebbe stata peggiore. La traduzione ha tenuto il lessico
economico senza addolcirlo — «i nostri affari prosperavano come mai prima», «la fine dei giorni d'oro
della Repubblica», «un investimento poco saggio» (Freya, L36) — perché è il registro con cui il
Sindacato parla di sé anche quando confessa.

L'Oracolo è reso come nome proprio invariato, con l'articolo: «l'Oracolo». La frase che chiude il
ragionamento di Korban («se la vostra flotta prova a eliminare gli Alphas, risponderanno con le
testate») resta una minaccia contrattuale, non un avvertimento morale.

## 6. Decisioni lessicali

| inglese | italiano | perché |
|---|---|---|
| empath | empate / empati | termine ufficiale del corpo; reso con il calco trasparente e spiegato nel testo |
| Navy Intelligence | Intelligence della Marina | nome dell'organismo, invariato nella parte inglese come «Intelligence» |
| Department of Intelligence | Dipartimento dell'Intelligence | idem |
| Oracle | l'Oracolo | nome proprio del sistema, con articolo |
| cloaking device | dispositivo di occultamento | equipaggiamento; titolo 527 lasciato per esteso (vedi §8) |
| scram drive | motore scram | equipaggiamento, come in L37 |
| Quicksilver, Protector, Argosy, Aerie, Star Queen | invariati | modelli di nave |
| Deep | il Deep | nome della regione, invariato |
| Core | il Nucleo | regione galattica; tradotto perché è un nome comune geografico |
| the Net | la Rete | rete di comunicazioni; tradotto, è un sostantivo comune |
| Buccaneer Bay, Stormhold, Nimbus, Maker, Altair, Valhalla, Farpoint, Hephaestus, Geminus, Foundry | invariati | pianeti e sistemi |
| Mr. Eyes | Mr. Eyes | nome proprio, come già in L34 |
| police action | azione di polizia | istituto giuridico, reso alla lettera |

**I numeri**: «a million-credit chip» → «una scheda da un milione di crediti»; «five million credits» →
«cinque milioni di crediti»; «seventeen thousand credits a day» → «diciassettemila crediti al giorno»;
«three hundred and forty-seven people» → «trecentoquarantasette persone».

## 7. La lacuna `log`: qui non perde niente

Misurato: **41 righe `log` → 41 unità `LOGBOOK`** (1:1), **nessuna** a tre argomenti, **nessuna**
categoria emersa. Come in L36 e L37, l'inventario è completo rispetto al file; la lacuna resta in
`tools/l10n.py` (protetto) e qui non c'era nulla da documentare come perdita.

## 8. Cosa è stato corretto e perché

- **32**: «ha ricevuto durante l'orario di ricevimento?» era sgrammaticato; riscritto «è in orario di
  ricevimento adesso?».
- **89**: «Su cui la gente non è d'accordo è come rispondere» → «Quello su cui la gente non è d'accordo è
  come rispondere».
- **146**: avevo reso «every bit as inefficient» con «efficiente» — **errore di senso** che rovesciava la
  battuta di Alondo; corretto in «una burocrazia inefficiente esattamente quanto quella contro cui ci
  siamo ribellati».
- **401**: «ma sono contento che questa volta sarà con te» → «ma sei contento che questa volta sia con te»
  (persona sbagliata).
- **527** `Cloaking Device` → «Dispositivo di occultamento» esce dalla banda comoda (1,80) ma resta
  **dentro il gate** (0,55–1,90). Lasciato per esteso: abbreviarlo in «Occultamento» scenderebbe sotto
  0,70 e perderebbe la natura di equipaggiamento.
- **403–411**: il blocco `CONVERSATION` è stato tradotto come dialogo continuo, mantenendo il turno di
  Freya che prende le difese dell'ingegnere («Dagli tregua, <first>. Sta solo pensando da ingegnere»).
- **183/185/187** (L37) e **183/185/187** di questo lotto: le tre varianti identiche della spia nucleare
  sono state lasciate identiche, come nell'inglese.
- **Le due battute aperte** (45, 546) sono state riprodotte, non chiuse.

## 9. Controlli e limiti

`check.py` (22 controlli) verifica: copertura, unità vuote, `NT` identiche, duplicati italiano spiegati
dal sorgente, tab e virgolette per unità e come totale, quadre per unità, token `<...>`, backtick, spazi,
rapporto lunghezze, tipografia, caratteri non latini, parole inglesi residue, stato del database.

`verify.py` (29 controlli) **non riusa** la logica di `check.py`: ricostruisce tutto da `source.json`, dal
file sorgente e da `state.db` in sola lettura, e in più asserisce (a) che le `UI_LABEL` siano 139 e 308,
(b) che le `CONVERSATION` siano 9 e tutte tradotte, (c) che l'unica unità con quadre sia la 426 con una
coppia conservata, (d) che le virgolette dispari siano esattamente quelle del sorgente, (e) che le 14
parti ricostruiscano `translation.json`, (f) la copertura totale 596/596 del file da un solo lotto e la
coppia di righe (31, 2729).

Limiti, dichiarati:

- **Il lotto non è nel gioco.** Nessuna approvazione nel database, nessun caricamento: 596 unità
  `PENDING`.
- **Nessuna verifica nell'editor.** In particolare non è verificato come venga reso a schermo il blocco
  `CONVERSATION` 403–411, che nel gioco ha un'interfaccia propria, né il testo lungo dell'unità 426 fra
  le quadre.
- **Il rapporto 0,74–1,80 non è un giudizio di qualità.**
