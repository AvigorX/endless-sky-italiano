# review.md — L279 (`data/human/kestrel.txt`, righe 56–164)

Registro delle decisioni editoriali del **secondo lotto** del file della Kestrel: il colloquio tecnico e la **sceneggiata del
nome**.

## 1. Tre registri in un solo lotto

| atto | unità | registro |
|---|---|---|
| le istruzioni | 1-3 | **tecnico-contrattuale**: dove, cosa, cosa perdi |
| il ritorno | 4-16 | **colloquiale-professionale**: complimenti, autocritica, quattro domande |
| il nome | 17-33 | **comico**: una trattativa che non è una trattativa |

La resa non ha uniformato i tre: le istruzioni sono asciutte («disabilitala senza distruggerla»), il ritorno ha il tono
compiaciuto di chi ha costruito la nave, il finale è una gag costruita sulla **ripetizione**.

## 2. Scelte

| inglese | resa |
|---|---|
| `We do most of our starship testing in the <waypoints> system` | **Facciamo la maggior parte dei collaudi delle nostre astronavi nel sistema <waypoints>** |
| `The test ship is unmistakable` | **La nave da collaudo è inconfondibile** |
| `disable it without destroying it` | **disabilitala senza distruggerla** |
| `you will forfeit your payment` | **perderai il pagamento** |
| `Atinoda meets up with you soon after you land` | **Atinoda ti raggiunge poco dopo che sei atterrato** |
| `I see that you survived` | **Vedo che sei sopravvissuto** |
| `I'm afraid I made short work of it` | **temo che l'abbia liquidata in fretta** |
| `we have the opportunity to make a few tweaks` | **abbiamo l'occasione di fare qualche ritocco** |
| `before we start mass-producing this ship` | **prima di iniziare a produrre questa nave in serie** |
| `you are the infamous <first> <last>, after all` | **dopotutto sei il famigerato <first> <last>** |
| `any single warship will be little threat to you` | **una singola nave da guerra sia una minaccia minima per te** |
| `we'll focus on strengthening the hull and the shield matrix` | **ci concentreremo sul rafforzare lo scafo e la matrice degli scudi** |
| `we'll see if we can incorporate more fighter bays into the hull` | **vedremo se possiamo integrare più baie di caccia nello scafo** |
| `he jerks as if he's just been electrocuted` | **sussulta come se fosse appena stato folgorato** |
| `That's the name we'll go with` | **È il nome che sceglieremo** |
| `we will take your recommendations into account` | **terremo conto dei tuoi consigli** |
| `wishes you the best of luck in your future endeavors` | **ti augura buona fortuna per le tue future imprese** |

## 3. La gag della ripetizione

Le quattro battute del giocatore che propone `Kestrel` sono **identiche**: `"La Kestrel."` — quattro volte. Non è pigrizia
traduttiva: è **la struttura della scena**, in cui Atinoda cambia motivazione a ogni rifiuto (gli animali, gli uccelli, il
troppo) e il giocatore **non cambia risposta**. Variare le battute per «eleganza» avrebbe distrutto la comicità.

Per lo stesso motivo sono conservate le ripetizioni «gemelle» di Atinoda (unità 7 e 8 ripetono la stessa proposta di ritocco
in due contesti diversi) e la forma `-` del sorgente nell'elenco delle navi uccello (unità 27): «il Falcon, l'Osprey, il
Hawk», con i **trattini semplici**, non i trattini lunghi.

## 4. Il nome maschile o femminile

I nomi proposti sono sostantivi italiani di genere diverso: `Wraith` e `Reaper` (maschili: «il»), `Dire Wolf` (maschile),
`Grey Goose` e `Kestrel` (femminili, perché sono **navi** e la parola «nave» è femminile). Il risultato è coerente: «**La**
Kestrel», «**Il** Wraith», e nell'epilogo «**la** Kestrel sarà in vendita».

## 5. `'Kestrel'` fra apici semplici

Unità 33: `When you say the word 'Kestrel'`. L'inglese usa **apici semplici** per la parola citata dentro il discorso, e la
resa li conserva. È il motivo per cui gli apici italiani di quell'unità sono **due** e non zero, e il `check.py` lo verifica
esplicitamente.

## 6. Struttura

| cosa | inglese | italiano |
|---|---|---|
| tab | **32** (tutte tranne la 4) | **32**, primo carattere |
| virgolette | **94** | **94**, per unità, dritte |
| apici | **16** | **10** |
| segnaposto | **3** | **3**, stesse famiglie |

## 7. Cosa resta aperto (dichiarato)

- **Nessuna approvazione**: 33 unità `PENDING`.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Il file è a 49/51**: restano il **messaggio di disponibilità** (`Kestrel Available`) e la **`DESCRIPTION` della nave**;
  L280 chiude `kestrel.txt`.
