# REVIEW — L68 · `data/successors/successor 2 ghosts myurej.txt`

Revisione del primo lotto sul file, dopo la chiusura dei controlli.

## 1. Coerenza con L45–L47 (linea Successors)

- **`Casa X`**: la forma dominante in staging è `Casa Kaatrij` (51), `Casa Sioeora` (8+17+10), `Casa
  Myurej` (4). Questo lotto usa `Casa Myurej` / `Casa Sioeora` e `Casate` al plurale. Restano in L45 due
  `Casata Myurej`: **non** vengono riscritte (un lotto chiuso non si riallinea), ma la forma nuova è quella
  da seguire.
- **Registro arcaico**: L45–L47 rendono `thou/thee/thy` con «tu» moderno e sintassi formale; qui la stessa
  scelta. La voce cerimoniosa si riconosce da «desidera avvalersi dei tuoi servigi», «non trattabili»,
  «sarai ricompensato», non da pronomi antichi.
- **`Successori`** (mai `Successors` nel testo italiano), **`Casate del Popolo`**, **`sfera di dati`**,
  **`dispositivo di traduzione`**: tutte forme già in staging, riusate e non reinventate.
- **Nomi propri invariati**: `Myurej`, `Chydiyi`, `Kaatrij`, `Sioeora`, `Riiria`, `Riijaaora`,
  `Kasii-Tuur-Saqru`, `Vade-Osolaa-Kaska`, `Kvelqden`, `Myaede`. `Riijaaora` è la stessa persona di L45
  (erede di Casa Sioeora): nome identico, quindi il riferimento resta riconoscibile.

## 2. Il `log` a tre argomenti: categoria al posto del testo

L'unità 23 (riga 67) è `log "People" "Riiria" "One of the most influential members …"`. L'estrattore
protetto ha inventariato **`People`**, cioè la **categoria**, e il testo descrittivo di Riiria **non è in
inventario**. È la settima occorrenza della lacuna già documentata (L45 195/305/357/418, L46 62, L47 54) e
la prima con questa forma esatta (tre argomenti *tutti* fra virgolette).

Conseguenze, tutte asserite:

- `LOG = {23, 24}`, `LOG_CAT = {23}`, `LOG_TEXT = {24}`. La categoria è in `NT` e il controllo pretende che
  sia **identica**; il testo (24) è tradotto e il controllo pretende che **non** sia identico all'inglese.
- Il `check.py` asserisce **quattro** forme di `log` e che esse esauriscano `LOG`: `1 tre argomenti fra
  virgolette, 0 tre con backtick, 0 backtick, 1 diretta`.
- **Il testo perso non è recuperabile in questo lotto**: ricostruirlo significherebbe scrivere una unità che
  il database non ha, cioè introdurre una traduzione senza unità di riferimento. Va segnalato a chi
  possiede `tools/l10n.py` (protetto), non corretto qui.

## 3. Nodi traduttivi aperti (dichiarati)

- **`the Old`** (34) → «i Vecchi»: indica le Casate antiche. Se in un lotto futuro il gioco usasse «Antichi»
  per una fazione, la scelta va rivista **prima** di riusarla.
- **`cant of an arm`** (34) → «il cenno di un braccio»: è la resa più plausibile di un'espressione che nel
  testo è già ellittica. Se un lotto successivo chiarisce il gesto, si allinea.
- **`Kvelqden` corazzati** (29): la razza non compare altrove nello staging (`0` occorrenze): nome
  invariato per default, non c'è un precedente da rispettare.
- **`Myaede`** (33): animale/struttura sconosciuta, invariato. «sventrato» rende `gutted` e regge
  l'immagine della bottega ricavata dalla carcassa.
- **`Vade-Osolaa-Kaska`** (46): toponimo inventato, invariato, con la stessa punteggiatura dei toponimi
  Successors già in staging (`Kasii-Cavasaa-Oa`, `Kasi-Osolaa-Sossa`).
- **`'Tis` / `thou'rt` / `shouldst`**: nessun arcaismo italiano. È una scelta, non una dimenticanza.

## 4. Duplicati e virgolette

- **2 gruppi di duplicati inglesi**: 15/21 (`"All right, I'll do it."`) e 16/22 (`"Sorry, but I don't want
  any part of this."`). Sono le stesse due battute di scelta ripetute nel ramo «perché io?» e nel ramo
  «quanto paghi?». L'inglese è **identico**, quindi la resa italiana identica è corretta; e il controllo
  «nessuna resa ripetuta fra inglesi diversi» resta verde.
- **90 virgolette** su 49 unità, **0 dispari** nel sorgente e **0** in italiano: parità per unità.
- **0 quadre**, **0 backtick**: assenze dichiarate, non omesse.

## 5. Cosa NON è stato fatto

- **Nessuna scrittura su `state.db`**: le 49 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: nessun test a schermo della scena, del paravento o della trasmissione.
- **Nessun recupero del testo perso** dell'unità 23 (lacuna dell'estrattore protetto).
- **Nessun allineamento retroattivo** delle due `Casata Myurej` in L45.
- **Nessuna misura del registro**: la voce cerimoniosa/popolare/sarcastica è verificata solo come testo.

## 6. Rischi residui

- **L'invariante è di segmento**: se un lotto futuro ripartisse dalla riga 113, l'unità di riga 113
  risulterebbe in **due** lotti (L68 e il nuovo) senza che nessuno script se ne accorga — il `verify.py`
  di L68 controlla il proprio segmento, non le sovrapposizioni. Per L69 ho misurato la finestra **114–197**
  proprio per evitarlo: `next_section.py` propone 113 e va corretto a mano.
- **`162 unità / max line 531`** sono cablati nel `verify.py`: se il file crescesse, diventerebbe rosso.
  È il comportamento voluto (il lotto descrive un segmento di un file che prosegue), ma chi riprende deve
  sapere che il rosso può venire dal file, non dalla traduzione.
- **Il `check.py` rigenera `translation.json` a ogni esecuzione**: l'hash citato (`eaafbeb6e504c701`) è
  quello **dopo l'ultima esecuzione** di `check.py`, e le parti restano la fonte.

## 7. Correzione a un documento chiuso

`staging/editorial/L67_20261018_191025/STATO.md` chiudeva con «**13 token** in 5 famiglie» riferito a
**questo** lotto: la somma della sua stessa tabella è 10 e il sorgente ne conta 10. Corretto nella riga
finale di quel documento (numero, non riscrittura), perché una sessione a freddo lo avrebbe ereditato.
Nessun altro documento chiuso è stato toccato.

## 8. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 2 parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì — entrambi gli script lanciati, output letto per intero |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (37 controlli), `verify.py` exit 0 (46 controlli), sha256 `eaafbeb6e504c701` |
