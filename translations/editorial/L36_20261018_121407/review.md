# L36 — revisione editoriale

Lotto `L36_20261018_121407` · `data/human/free worlds 2 middle.txt` · righe 16–2336 · 552 unità ·
16.290 parole EN → 15.323 IT · `check.py` `FAIL totale: 0` · `verify.py` 27 controlli, exit 0.

Questo documento registra **le decisioni**, non i numeri: i numeri stanno in `REPORT.md` e sono
rigenerabili con i due comandi di verifica.

---

## 1. Che cosa copre il lotto

Secondo dei tre atti centrali delle Free Worlds, e come i file di L32–L35 **finisce con il lotto**: riga
16 prima unità, riga 2336 ultima. La copertura 552/552 è quindi un invariante legittimo.

In ordine: la diplomazia sulla Terra che fallisce; la ricognizione dei sistemi del sud e il furto del
fascio di elettroni; la scorta dei primi tre Dreadnought da Zug e la battaglia di Rastaban; il bivio sui
prigionieri della Marina e lo scambio con Katya; la sorveglianza da smantellare su Hope, Clark, New
Holland e New Tibet; Poisonwood e gli Alphas, con gli Oathkeepers che combattono al fianco delle Free
Worlds; Bloodsea, diplomatica o invasa; Albatross e l'omicidio mirato di Ryk Bartlett; l'occupazione di
Zeta Aquilae; l'invasione della Marina a Rastaban e Delta Sagittarii che spezza la flotta in due; il
disertore del Sindacato, Raven e il ritorno di Katya.

È il lotto in cui **il giocatore entra nel Consiglio** (unità 221, dopo la sospensione di L35) e in cui
le decisioni cominciano a essere sue: tre voti decisivi in 552 unità (prigionieri, Bloodsea, disertore).
La traduzione non ha ammorbidito nessuno dei tre.

## 2. Ricognizione (misurata sul `source.json`, non dedotta)

```
MISSION_TEXT 396 · VALUE 46 · DESCRIPTION 45 · DIALOG 39 · LOGBOOK 23 · UI_LABEL 3
contesti 52 · tab 341 (nessuna unità ne ha più di uno iniziale) · virgolette 919 · token 139
unità con parentesi quadre [a, b]: 0
unità con numero dispari di virgolette: 3 (76, 77, 355)
righe `log`: 23 → 23 unità LOGBOOK (1:1), nessuna a tre argomenti, nessuna categoria
```

Due fatti che hanno richiesto preparazione e **non** si potevano copiare da L35:

- **`UI_LABEL` passa da 1 a 3**, e tutte e tre sono `label` di salto in un dialogo a scelte (unità 407,
  501, 503). In L35 una era una label e una una categoria di diario: `NT = {513, 547}`. Copiare quella
  lista avrebbe fatto tradurre tre label e rotto tre `goto`.
- **`VALUE` sale a 46** (in L35 erano 32) e sono per lo più titoli di missione di due o tre parole: è il
  tipo che produce più spesso sforamenti del rapporto (è successo a 123, 138 e 247).

## 3. Metodo

1. `export_section.py` su righe 16–2336 → 552 unità, 52 contesti.
2. Ricognizione dei tipi, del `raw` delle tre `UI_LABEL`, delle righe `log`, delle virgolette dispari.
3. `check.py` derivato da L35 con `NT = {407, 501, 503}`, `TOKEN_EXC` vuoto, nessun controllo parentesi
   quadre (0 unità: asserito nel `verify.py`).
4. Traduzione in 11 parti a fine contesto, ognuna chiusa con `check.py --range` verde.
5. `check.py` completo (duplicati, copertura, tipografia, token) e `verify.py` indipendente.

Le parti: 1–71, 72–122, 123–163, 164–207, 208–257, 258–318, 319–386, 387–440, 441–471, 472–538, 539–552.

## 4. Le voci di questo file

Gli stessi personaggi di L34–L35, con un'aggiunta che cambia il tono del lotto: **il giocatore siede nel
Consiglio**. Da unità 221 in poi Alondo e Freya non gli danno più ordini, gli chiedono un voto.

**Freya Winters.** Resta la tecnica che fa i conti, ma qui ha due registri nuovi: l'entusiasmo
dell'ingegnere quando la produzione dei Dreadnought parte («I cantieri Southbound stanno sfornando
Dreadnought adesso!») e la freddezza contabile quando deve opporsi al giocatore («barattare un alleato
certo per una magra possibilità di pace è un investimento poco saggio», unità 486). Il secondo è il
registro che conta: Freya non dice «è sbagliato», dice «è un cattivo investimento».

**Alondo Gruyere.** Il diplomatico che sa di essere stato messo da parte: su Albatross non può andare
perché è gay (unità 401), e il testo lo dice senza giri di parole. La traduzione ha tenuto la frase
secca — «Alondo è gay» — perché il valore della scena sta nella franchezza, e l'ha resa in un italiano
piano, senza eufemismi e senza aggiunte.

**JJ.** Torna a essere la coscienza del gruppo: rifiuta di degnare di risposta la domanda del giocatore
sul rischio di morire tutti («Se moriamo, le Free Worlds vivranno lo stesso», unità 470) e si oppone
all'invasione di Bloodsea («Stai cominciando a somigliare parecchio a Tomek», unità 380).

**Tomek.** Assente come personaggio, presente come misura: due volte il testo lo cita come termine di
paragone per una decisione sbagliata (355, 377, 380). In italiano il nome resta nudo, senza epiteti.

**Raven.** Personaggio nuovo: parla per frasi brevi e definitive, non spiega, non ripete. Il suo tratto
è il contrasto fra la cortesia formale e il contenuto («Se dice la verità, la nostra guerra con voi
finirà oggi. E comincerà un'altra guerra.»). La descrizione fisica (unità 517) è resa senza
abbellimenti: pelle scura, abiti neri, tatuaggio sclerale con nodi celtici nel bianco degli occhi.

**Nguyen.** Il buddista del Corpo Umanitario: registro colto, esitante, pieno di frasi che si
interrompono. Il suo dilemma sulle gravidanze delle schiave Alpha (unità 308) è il punto più duro del
lotto e la traduzione non lo attenua: «Dovremo chiedere loro di interrompere le gravidanze. È l'unica
decisione sicura, ma continua a non piacermi.»

## 5. I tre bivi

Il lotto contiene tre scelte che cambiano il seguito, e in tutte e tre la traduzione ha dato **lo stesso
peso alle due opzioni**: nessuna formula che faccia sembrare "giusto" un ramo.

1. **I prigionieri della Marina** (unità 125–152): restituirli sulla parola o tenerli su Clink finché
   Katya non torna. I due titoli sono stati accorciati a «Restituisci i prigionieri» e «Trattieni i
   prigionieri» perché le versioni lunghe uscivano dal rapporto (1,81 e 1,895); la simmetria dei due
   titoli è deliberata ed è ciò che rende leggibile la scelta nel diario.
2. **Bloodsea** (unità 344–386): costruire lo spazioporto o invadere. Alondo elenca le due opzioni con
   lo stesso tono, e il giocatore vota. In italiano «Opzione uno... Opzione due...» è rimasto tale,
   senza gerarchia.
3. **Il disertore del Sindacato** (unità 476–504): salvarlo o consegnarlo. È il bivio più lungo del
   lotto (29 unità) e l'unico in cui la scelta è narrata come voto del Consiglio: JJ vota per salvarlo,
   Freya per consegnarlo, e il giocatore decide. Le due `label` di salto 501 e 503 stanno qui.

## 6. Decisioni lessicali

| inglese | italiano | perché |
|---|---|---|
| Electron Beam / Electron Turret | fascio di elettroni / torretta a elettroni | arma descritta dal testo; «beam» non è un nome proprio |
| Dreadnought | Dreadnought | nome del modello, invariato come le altre navi |
| Oathkeepers | Oathkeepers | nome del reggimento, invariato (in L35 era già così) |
| Southbound Shipyards | cantieri Southbound | «Shipyards» è un sostantivo comune: tradotto, il nome proprio resta |
| Kraz Cybernetics | Kraz Cybernetics | nome di azienda, invariato |
| the Wolf Pack | il Branco di Lupi | è un gruppo di volontari che si è dato un nome descrittivo, non una fazione del gioco; tradurlo lo rende leggibile e non crea ambiguità con nessun'altra entità |
| Questioner | Interrogatore | corpo dell'Intelligence; il testo lo usa come titolo («She must be a Questioner») e la maiuscola si conserva («una degli Interrogatori») |
| Ramscoop / Catalytic Ramscoop | ramscoop / Ramscoop Catalitico | nome di equipaggiamento già in uso nei lotti precedenti |
| Battle Fleet | flotta da battaglia | |
| Bloodsea, Albatross, Rand, Oblivion, Mutiny, Wayfarer, Zeta Aquilae | invariati | pianeti e sistemi |
| the Dread (nave) | la Dread | nome proprio di nave, con articolo italiano |
| Starry Warrior (nave) | la Starry Warrior | idem |

**I numeri**: «2,100 credits» → «2.100 crediti»; «several dozen» → «diverse decine».

## 7. La lacuna `log`: qui non perde niente

Misurato, non dedotto:

- **23 righe `log`** → **23 unità `LOGBOOK`** (1:1).
- **Nessuna** riga ha la forma `log "Categoria" "Nome" `testo``.
- **Nessuna** unità prodotta è una categoria.

È il primo file della serie in cui l'inventario delle righe `log` è completo. In L33 perdeva categoria e
nome su tre righe, in L34 su cinque, in L35 su quattro (più una categoria emersa al posto del testo). La
lacuna è in `tools/l10n.py`, che è protetto: qui non c'era nulla da documentare come perdita, e il fatto
è registrato perché è una **misura**, non un'assenza di controllo.

## 8. Cosa è stato corretto e perché

- **123 e 138**: titoli usciti dalla banda comoda alta (1,81 e 1,895) con le prime versioni
  («Restituisci i prigionieri della Marina», «Trattieni i prigionieri della Marina»); accorciati a
  «Restituisci i prigionieri» e «Trattieni i prigionieri».
- **247**: titolo `Meet Convoy` a 1,909, oltre il gate; riscritto «Incontra la flotta», coerente col
  testo che parla di una flotta mercantile.
- **543**: la prima stesura aveva due virgolette dove il sorgente ne ha quattro (la battuta è spezzata
  da «he says»). Riscritta mantenendo la struttura del sorgente, ridondanza compresa.
- **326 e 355**: refusi di stesura («Mandate... vi dicono» invece della seconda persona singolare;
  «I nostri numero»); corretti.
- **97 e 98**: due varianti dello stesso discorso (Barmy Edward con armi già provate / appena finite).
  Tenute distinte, come nell'inglese.
- **64, 65, 66**: tre varianti della stessa risposta sulle armi già saccheggiate. Tenute distinte:
  «Ho già saccheggiato una di queste nuove armi» / «...nuove torrette» / «So come procurarmene una».
- **Le tre battute aperte** (76, 77, 355) sono state riprodotte, non chiuse.

## 9. Controlli e limiti

`check.py` (21 controlli) verifica: copertura, unità vuote, `NT` identiche, duplicati italiano spiegati
dal sorgente, tab e virgolette per unità e come totale, token `<...>`, backtick, spazi, rapporto
lunghezze, tipografia, caratteri non latini, parole inglesi residue, stato del database. **Non** contiene
il controllo delle parentesi quadre (0 unità nel sorgente).

`verify.py` (27 controlli) **non riusa** la logica di `check.py`: ricostruisce tutto da `source.json`, dal
file sorgente e da `state.db` in sola lettura, e in più asserisce (a) che le `UI_LABEL` siano esattamente
407, 501 e 503, (b) che non ci siano parentesi quadre, (c) che le virgolette dispari siano esattamente
quelle del sorgente, (d) che le 11 parti ricostruiscano `translation.json`, (e) la copertura totale
552/552 del file da un solo lotto.

Limiti, dichiarati:

- **Il lotto non è nel gioco.** Nessuna approvazione nel database, nessun caricamento: 552 unità
  `PENDING`.
- **Nessuna verifica nell'editor.** In particolare non è verificato come vengano impaginati i due
  monologhi lunghi (476, 480) e la scena di combattimento corpo a corpo (279–289), che ha unità molto
  lunghe.
- **Il rapporto 0,75–1,65 non è un giudizio di qualità.**
