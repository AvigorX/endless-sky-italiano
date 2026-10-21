# REVIEW — L73 · `data/successors/successor 2 ghosts aqrabe.txt`

## 1. Coerenza con la linea Successors (L68–L72)

- **Casa X**, **Casate**, **Predecessori**, **erede**, **sfera di dati**, **dispositivo di traduzione**,
  **piazzola**, **datapad**: tutte forme già fissate; nessun termine reinventato.
- **Il registro cerimonioso** resta quello di Myurej («cortesemente», «se tu lo desideri»), ma qui è più
  **giocoso**: Sola scherza («Amateur secrecy shall get thee nowhere»), Tiliia è pratica.
- **Casa Aqrabe** era già citata in L70 («ricordando l'esperienza con Casa Aqrabe») e in L45: il nome resta
  invariato, e questo file ne è il seguito.
- **I «santi»** sono una trovata nuova del file: arti recisi che parlano in frammenti. La traduzione non li
  addomestica.

## 2. Nodi traduttivi aperti (dichiarati)

- **`saints`** (15, 20): «santi» fra virgolette. La parola è usata con ironia dalla Casa; se un lotto futuro
  la trattasse come titolo ufficiale, la resa andrebbe rivista (maiuscola, nessuna virgoletta).
- **`weft-weaving armor`** (44) e **`multimodal armor`** (51): due rese diverse per la stessa tecnologia.
  Non è incoerenza: l'inglese usa due espressioni, e allinearle renderebbe due unità identiche.
- **`Aqrabe I- Sola`**: il prefisso `I-` resta; non è spiegato nel testo e non va interpretato.
- **`keystone`** → «pietra chiave»: se in futuro il gioco usasse `Keystone` come nome di un'organizzazione
  (in staging esiste `Keystone Research` **non tradotto**), la resa dell'oggetto resterebbe distinta.
- **`Seiitejen`** (49): nome di nave, invariato.

## 3. `CONVERSATION`: testo, non etichetta

Le sei unità (31–36) sono il **corpo** del blocco `conversation`, con backtick nel `raw` e senza delimitatore
nell'`english`. Sono tradotte come prosa. Il `verify.py` asserisce **due** cose: il **conteggio** (6) e che
nessuna resti identica all'inglese. Se un inventario futuro cambiasse (un'etichetta di `goto` che entra nel
lotto), il controllo diventerebbe rosso — che è quello che si vuole.

## 4. `LOGBOOK` misto

- **30** e **51**: testi, forma **diretta**, tradotti.
- **43**: **categoria** (`People`) da un `log "People" "Tiliia" "…"`, lasciata **identica** e messa in `NT`.

Il `check.py` verifica che l'unica riga a tre argomenti sia proprio quella della categoria: se il file
cambiasse forma, il controllo lo direbbe.

## 5. Duplicati, virgolette, tab

- **0 gruppi di duplicati inglesi**; nessuna resa italiana ripetuta fra inglesi diversi.
- **90 virgolette** su 51 unità, **0 dispari**: dialogo fitto (reliquiario, Tiliia, Sola).
- **42 tab** su **38 unità** con tab iniziale: 4 unità ne hanno due (le voci dei «santi» indentate).
- **0 quadre**, **0 backtick** nel tradotto.

## 6. Cosa NON è stato fatto

- **Nessuna scrittura su `state.db`**: le 51 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: nessun test a schermo del reliquiario, dei «santi» o della scorta.
- **Nessuna verifica del registro**: le tre voci (Sola, Tiliia, i santi) sono valutate come testo.
- **La categoria `People`** resta in inglese per scelta, non per dimenticanza.

## 7. Rischi residui

- **`0,72` è il rapporto minimo del lotto**: vicino al gate ma dentro; nessuna battuta riscritta.
- **Il `verify.py` cita 0 prima e 129 dopo**: sono i conteggi veri del file oggi. Se un lotto futuro
  coprisse le righe 23–158, diventerebbe rosso — è voluto.
- **`saints` fra virgolette** dipende dalla punteggiatura: un refuso che togliesse le virgolette passerebbe i
  controlli di parità (due virgolette in meno) solo se il conteggio per unità non tornasse — e tornerebbe,
  perché il testo ne ha due coppie. Va verificato a lettura.

## 8. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 3 parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì — entrambi gli script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (35 controlli), `verify.py` exit 0 (47 controlli), sha256 `1cd04c9a55a1312c` |
