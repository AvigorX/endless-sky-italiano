# REVIEW — L71 · `data/successors/successor 2 ghosts myurej.txt`

## 1. Coerenza con L68–L70

- **Casa Myurej**, **le Casate**, **Predecessori**, **Quarg**, **sfera di dati**, **dispositivo di
  traduzione**, **spazioporto**, **Casate del Popolo**: tutte forme già fissate.
- **Ijaset** è un personaggio nuovo e parla in modo diverso dagli altri Myurej: è cortese, curioso, e
  ammette di non avere nulla contro il giocatore. Non usa il disprezzo cerimonioso della voce dietro lo
  schermo; la traduzione lo distingue (frasi piane, nessuna minaccia, «Che piacere incontrarti»).
- **`ninnoli`** torna qui (unità 26) per gli oggetti della cripta: è la parola con cui la Casa sminuisce
  ciò che vale, già usata in L70.

## 2. Nodi traduttivi aperti (dichiarati)

- **`vault` → «cripta»**: nessun precedente in staging. Se un lotto futuro usasse `vault` per una cassaforte
  di navi o un ambiente tecnico, la resa andrebbe distinta; oggi il testo parla di una camera sotterranea
  con scatole di legno, e «cripta» regge.
- **`wormhole`** resta in inglese. È una scelta, non una dimenticanza: cambiarla richiederebbe un
  allineamento su tutti i lotti che la usano.
- **Ijaset senza genere**: la scelta è dichiarata nel `REPORT.md`. Se un lotto futuro dovesse riferirsi a
  Ijaset con un pronome o un aggettivo concordato, la frase va riscritta, non il personaggio.
- **`the Old`** non compare qui; la resa di L70 («i Vecchi») resta valida solo per quel contesto.

## 3. L'unico `LOGBOOK` del file resta in L68

In questo lotto non ci sono diari: `LOGBOOK 0`, asserito anche sul `raw`. L'unica voce di diario del file
resta quella di L68 (unità 23, categoria `People`) e il testo perso di quella voce resta la settima
occorrenza della lacuna dell'estrattore.

## 4. Duplicati, virgolette, tab

- **0 gruppi di duplicati inglesi** (controllo negativo dichiarato): nessuna resa italiana ripetuta fra
  unità con inglese diverso.
- **72 virgolette** su 42 unità, **0 dispari**: è il lotto più dialogato del file finora (due terzi delle
  unità sono battute o scelte).
- **38 tab su 38 unità**; 4 unità senza tab (nome, descrizione, due testi non indentati).
- **0 quadre**, **0 backtick**.

## 5. Cosa NON è stato fatto

- **Nessuna scrittura su `state.db`**: le 42 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: nessun test a schermo della cripta, dell'apertura dell'incasso o del
  bombardamento.
- **Nessuna verifica del registro**: la voce di Ijaset è valutata come testo, non misurata.
- **`vault` → «cripta»** non è confrontato con un uso futuro del termine nel gioco.

## 6. Rischi residui

- **`0,59` è vicino al gate**: una riscrittura futura della battuta più corta («Tutto qui?») potrebbe
  scendere sotto 0,55. Il gate non si allarga (decisione 211).
- **Il `verify.py` cita 119 prima e 50 dopo**: sono i conteggi veri del file oggi. Se un lotto futuro
  coprisse le righe 311–401, il controllo diventerebbe rosso — è voluto.
- **Ijaset senza genere** dipende dalla formulazione: un refuso futuro che introduca «lui» o «lei»
  passerebbe tutti i controlli automatici. Va verificato a lettura.

## 7. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 2 parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì — entrambi gli script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (33 controlli), `verify.py` exit 0 (45 controlli), sha256 `9bdce0c7e02de186` |
