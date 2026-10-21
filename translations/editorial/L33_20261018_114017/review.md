# L33 — revisione editoriale

Lotto `L33_20261018_114017` · `data/wanderer/wanderers middle.txt` · righe 22–3601 · 731 unità ·
22.378 parole EN → 21.188 IT · `check.py` `FAIL totale: 0` · `verify.py` 27 controlli, exit 0.

Questo documento registra **le decisioni**, non i numeri: i numeri stanno in `REPORT.md` e sono
rigenerabili con i due comandi di verifica.

---

## 1. Che cosa copre il lotto

`wanderers middle.txt` è il secondo dei tre file della campagna dei Wanderers, e come `wanderers start`
(L32) **finisce con il lotto**: riga 22 è la prima unità del file, riga 3601 l'ultima. La copertura
731/731 è quindi un invariante legittimo e non una coincidenza.

Il contenuto, in ordine: l'assistenza dei Pug rifiutata, il tentativo fallito di violare la rete Kor
Mereti, la "Mente" dei Wanderers introdotta nella coscienza Mereti, la scoperta che i droni Mereti sono
diventati giardinieri senzienti, la diplomazia con i Kor Efret, la guerra contro i droni Kor Sestor
fino alla base degli Alphas su Zenith, e infine i negoziati con gli esuli Korath.

Il file è anche il primo del progetto in cui il giocatore **bombarda un pianeta abitato**: le unità
569–577 (descrizione di Zenith, l'esplosione, il cratere fino al mantello) sono state tradotte senza
attenuare il testo. Il sorgente dice che la crosta del pianeta si sposta e trema; l'italiano lo dice
uguale.

## 2. Ricognizione (misurata sul `source.json`, non dedotta)

```
MISSION_TEXT 494 · DESCRIPTION 68 · VALUE 61 · DIALOG 56 · LOGBOOK 41 · UI_LABEL 11 · CONVERSATION 0
contesti 75 · tab 408 · virgolette 1.002 · token 166 · unità con parentesi quadre 113
```

Due differenze rispetto a L32 che hanno richiesto lavoro di preparazione e **non** si potevano copiare:

- **`CONVERSATION` non esiste in questo file.** In L32 era 47 unità di contenitore misto (testo visibile
  + `label` di salto da mettere in `NT`). Qui il tipo è assente: nessuna label, nessun contenitore misto.
- **`UI_LABEL` esiste, 11 unità.** Sono i salti `skip unmark <stella>` per undici stelle. In L32 erano
  zero. La lista `NT` del lotto precedente (`"Bondir" Atomic Thruster`, `alt start`, `alt end`) qui
  sarebbe stata **sbagliata**: `check.py` avrebbe segnalato 11 unità non traducibili non dichiarate.

## 3. Metodo

1. `export_section.py` su righe 22–3601 → 731 unità, 75 contesti.
2. Ricognizione dei tipi e delle righe `log` **prima** di scrivere una riga di traduzione.
3. `check.py` derivato da L32 con `NT = set(range(580, 591))`, `TOKEN_EXC` vuoto, 7 famiglie di token,
   e il controllo delle parentesi quadre.
4. Traduzione in 11 parti a fine missione, ognuna chiusa con `check.py --range A B` verde.
5. `check.py` completo (duplicati, copertura, tipografia, token) e `verify.py` indipendente.

Le parti: 1–43, 44–87, 88–149, 150–219, 220–292, 293–364, 365–443, 444–515, 516–596, 597–678, 679–731.
Il confine è sempre a fine missione: una parte che si apre a metà missione costringe a tenere a mente
il contesto della parte precedente, ed è la principale fonte di incoerenza nei lotti lunghi.

## 4. Le voci di questo file

Il file ha **cinque** voci, non due. La voce dei Wanderers è quella fissata in L32 e non è stata
rinegoziata; le altre sono state ricavate dal testo.

**Wanderers (continuità da L32).** Frase piana, cortesia formale, nessun ordine marcato dei costituenti.
Tele'ek spiega e non comanda; Iriket propone e non ordina. Quando devono dare un ordine operativo lo
fanno con una domanda cortese ("vuoi accompagnarli là?"), e in italiano resta una domanda.

**Kor Efret (tradotti da Rek).** Parola guardinga, diffidente ma non ostile; parlano di onore
(unità 404: essere "carico vivo" su una nave aliena è disonorevole). Il testo arriva al giocatore
attraverso una traduzione dichiarata, e questo giustifica un registro leggermente più formale del
normale: «Non ce li daranno; devono andare a inserirli di persona.»

**Esuli Korath.** Frasi brevi, transazionali, nessuna cortesia. Non negoziano la pace: chiedono termini
commerciali. Unità 681, il commento di Rek («sembrava una recita infantile su un vertice di pace») è la
chiave di lettura dell'intero episodio e in italiano conserva la durezza.

**Pug.** Condiscendenti fino all'insulto, e il testo lo dichiara (unità 170: «il piccolo cervello
dell'umano»). Non è stato ammorbidito: è caratterizzazione, non scortesia dell'autore.

**Marina / Danforth.** Registro militare asciutto. Danforth non fa discorsi: dà coordinate e conseguenze
(unità 548: quindici secondi per essere a mille chilometri).

## 5. Le parentesi quadre: struttura, non stile

113 unità contengono `[a, b]`. Il gioco mostra **una sola alternativa per volta**: ogni alternativa deve
reggere la frase da sola, e il numero di gruppi e di alternative deve restare identico al sorgente.
Il `check.py` di questo lotto verifica esattamente questo, e in tre punti la prima resa non passava:

| unità | problema | soluzione |
|---|---|---|
| 286 | ordine dei gruppi invertito rispetto al sorgente | «la più [attraente, gradita] [linea d'azione?]» |
| 324 | un gruppo perso nella resa | `[saccheggiare, cacciare]` reintrodotto |
| 685 | un gruppo perso nella resa | `[tenteranno, porteranno a termine]` reintrodotto |

Caso particolare, unità 688: il sorgente ha **un gruppo con due alternative di lunghezza diversa**
(`[Hopefully, If this goes well]`). Reso «[Speriamo che, Se tutto va bene]», che regge in entrambe le
letture. Il caso 461 (`[month?]`, `[bedrock?]`) mostra invece il punto interrogativo *dentro* la
parentesi: è un'incertezza del personaggio, non un dubbio del traduttore, e resta dov'è.

## 6. Decisioni lessicali

| inglese | italiano | perché |
|---|---|---|
| Eye | Occhio | fissato in L32, non rinegoziato |
| Molt | Muta | fissato in L32 |
| Unfettered (Hai) | Slegati | fissato in L32 |
| Archon(s) | Archon | nome di specie, invariato |
| Keepers of the Eye | Custodi dell'Occhio | il testo (unità 160) li descrive come guardiani, non come tecnici |
| world-ship | nave-mondo | descrittivo, reso ogni volta |
| artificial mind / the Mind | mente artificiale / la Mente | maiuscola quando è il nome proprio del dispositivo |
| gestalt consciousness | coscienza gestaltica | termine tecnico ricorrente dei Wanderers |
| terraforming | terraformaggio | fissato in L32 |
| greenhouse facility | struttura delle serre | struttura, non la pianta |
| Oathkeepers, Alphas, Pug, Quarg | invariati | nomi propri di fazione/specie |
| Zenith, Farpoint, Saiph, Alnilam, Mesuket, Sestor Ikfar, Varu K'prai | invariati | toponimi |
| Heart of Gold | Heart of Gold | nome di una singola nave: tradurlo la renderebbe irriconoscibile |

Nota su `Oathkeepers`: il termine compare in contesti in cui il giocatore li ha già incontrati in
italiano nei lotti precedenti, e resta invariato per coerenza con quelli.

## 7. La lacuna `log`: qui la forma è quella di L32

Misurato sul file, non dedotto:

- **41 righe `log`** nell'intervallo 22–3601 → **41 unità `LOGBOOK`**: corrispondenza 1:1.
- L'unità prodotta è il **testo del diario** (l'argomento fra backtick), non la categoria.
- **3 righe** hanno la forma a tre argomenti `log "Categoria" "Nome" \`testo\``:

| riga | categoria | nome | unità |
|---|---|---|---|
| 338 | `People` | `Iktat Rek` | 92 |
| 549 | `Factions` | `Pug` | 169 |
| 953 | `People` | `Meto Pa'aret` | 281 |

Categoria e nome **non sono inventariati** in `state.db` e restano in inglese. È la stessa forma di
perdita documentata in L32, e l'opposto di L30 (dove la perdita era il testo). La forma cambia da file a
file: non esiste una regola unica, va misurata ogni volta.

Non è riparabile da questo lotto: `tools/l10n.py` e `state.db` sono file protetti con hash registrato.
La lacuna è documentata qui e nel checkpoint, non corretta.

## 8. Cosa è stato corretto e perché

- **33/38/194/390** hanno in inglese la stessa frase (`Sure, I would be glad to do that.`) e possono
  avere lo stesso italiano; **411/721** (`Sure, I would be glad to.`) e **593** (`Of course, I would be
  glad to.`) hanno inglesi diversi: il primo giro le aveva rese tutte uguali e il controllo dei
  duplicati — che scatta solo sul lotto **completo**, non sul `--range` — le ha segnalate.
- **331**: «È una serra.» dava rapporto 0,61, sotto il gate. Riscritta «È proprio una serra.», che è anche
  più vicina al tono del drone che annuncia la scoperta.
- **391**: «E i droni Sestor?» dava 0,44. Riscritta «E che cosa facciamo con i droni Sestor?».
- **485**: refuso «lo metallo» → «il metallo».
- **569**: una virgoletta di troppo che il sorgente non ha; rimossa (il controllo delle virgolette per
  unità l'avrebbe segnalata al lotto completo).
- **324, 685, 286**: vedi §5.
- **18, 58, 202, 540**: unità corte o quasi duplicate, riscritte.

## 9. Controlli e limiti

`check.py` (22 controlli) verifica: copertura, unità vuote, `NT` identiche, duplicati italiano spiegati
dal sorgente, tab e virgolette per unità e come totale, token `<...>`, parentesi quadre, backtick, spazi,
rapporto lunghezze, tipografia, caratteri non latini, parole inglesi residue, stato del database.

`verify.py` (27 controlli) **non riusa** la logica di `check.py`: ricostruisce tutto da `source.json`,
dal file sorgente su disco e da `state.db` in sola lettura, e verifica anche che le 11 parti su disco
ricostruiscano `translation.json`.

Limiti, dichiarati:

- **Il lotto non è nel gioco.** Nessuna approvazione nel database, nessun caricamento: 731 unità
  `PENDING`, come da mandato.
- **Nessuna verifica nell'editor.** Il testo non è stato visto renderizzato. Le virgolette doppie che il
  sorgente usa come virgolette di battuta sono state riprodotte in numero identico (1.002/1.002), ma la
  resa a schermo non è stata osservata.
- **Il rapporto 0,72–1,44 non è un giudizio di qualità.** Dice solo che nessuna unità è stata
  compressa o gonfiata fuori misura. Le scelte che lo hanno reso possibile sono in §5 e §6.
