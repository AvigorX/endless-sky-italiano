# L30 — revisione di chiusura

Lotto `L30_20261018_105244` · `data/coalition/lunarium intro.txt` · righe 21–2111 · 730 unità ·
aperto e chiuso il 2026-10-18.

Tutti i numeri di questo documento sono misurati con `check.py`, `verify.py`, `state.py` e i file su
disco. Nessun valore è dedotto dal lotto precedente.

## 1. Collocazione nel file

`lunarium intro.txt` conta 730 unità nel database, dalla riga 21 alla 2111. L30 le copre tutte: è
l'unico lotto di questo file, quindi la copertura totale 730/730 è un invariante asserito e non una
stima. Prima della riga 21 e dopo la 2111 non esiste alcuna unità (`where line < 21` → 0,
`where line > 2111` → 0, `max(line)` → 2111).

Decimo file completo dello staging.

## 2. Le tredici parti

| parte | unità | righe | EN → IT | ratio | min–max |
|---|---|---|---|---|---|
| 01 | 1–57 (57) | 21–188 | 1.832 → 1.760 | 0,961 | 0,73–1,66 |
| 02 | 58–104 (47) | 199–317 | 2.164 → 2.093 | 0,967 | 0,71–1,35 |
| 03 | 105–158 (54) | 323–480 | 1.957 → 1.920 | 0,981 | 0,76–1,62 |
| 04 | 159–239 (81) | 487–671 | 2.503 → 2.392 | 0,956 | 0,74–1,30 |
| 05 | 240–310 (71) | 681–838 | 2.809 → 2.656 | 0,946 | 0,80–1,22 |
| 06 | 311–342 (32) | 843–928 | 1.371 → 1.316 | 0,960 | 0,74–1,19 |
| 07 | 343–402 (60) | 935–1105 | 2.335 → 2.267 | 0,971 | 0,81–1,39 |
| 08 | 403–479 (77) | 1112–1321 | 2.692 → 2.526 | 0,938 | 0,73–1,38 |
| 09 | 480–527 (48) | 1328–1459 | 1.902 → 1.766 | 0,928 | 0,70–1,42 |
| 10 | 528–574 (47) | 1464–1591 | 2.453 → 2.371 | 0,967 | 0,86–1,43 |
| 11 | 575–641 (67) | 1598–1873 | 3.261 → 3.239 | 0,993 | 0,71–1,62 |
| 12 | 642–700 (59) | 1876–2014 | 2.649 → 2.532 | 0,956 | 0,73–1,30 |
| 13 | 701–730 (30) | 2016–2111 | 1.280 → 1.241 | 0,970 | 0,91–1,27 |

Il confine di ogni parte cade a fine missione. Le righe sono quelle della prima e dell'ultima unità
della parte, lette da `source.json`, non calcolate.

## 3. Tabella dei controlli (`check.py`, lotto completo)

| Controllo | Esito | OK |
|---|---|---|
| unità richieste in questo controllo | 730 | OK |
| unità tradotte nell'intervallo | 730/730 | OK |
| copertura del lotto | 730/730 | OK |
| traduzioni vuote | 0 | OK |
| non traducibili lasciate identiche (9 attese) | ok | OK |
| duplicati italiano non spiegati dal sorgente | ok | OK |
| tab per unità | ok | OK |
| tab iniziale conservato | ok | OK |
| virgolette per unità | ok | OK |
| token `<...>` (eccezioni pronomi ammesse: 0) | ok | OK |
| eccezioni token coerenti | ok | OK |
| backtick per unità | ok | OK |
| spazio iniziale/finale come il sorgente | ok | OK |
| spazi doppi/ai bordi non voluti | ok | OK |
| rapporto lunghezza | 0,70 – 1,66 | OK |
| tipografia (accenti/apostrofi/dash) | ok | OK |
| caratteri non latini | ok | OK |
| parole inglesi residue (istituzioni/navi escluse) | nessuna | OK |
| state.db APPROVED/PENDING | 364/32560 | OK |
| ultimo aggiornamento APPROVED | 2026-10-17T14:33:18Z | OK |
| unità del lotto fuori da PENDING | 0 | OK |

Totale del lotto: **FAIL totale: 0**. Parole EN 29.208 → IT 28.079. Tab IT 550 / EN 550.
Virgolette IT 1.449 / EN 1.449. Token IT 334 / EN 334. Parti caricate: 13. Duplicati inglese:
32 gruppi (70 unità). Unità mancanti: 0.

## 4. Controlli indipendenti (`verify.py`)

`verify.py` non riusa la logica di `check.py`: rilegge la riga grezza dal file del gioco, confronta
ogni unità con `state.db`, ricostruisce `translation.json` dalle parti e conta i caratteri sul testo.
**25 controlli, `FAIL: 0`, exit 0.** Copertura 730/730 asserita, un solo lotto sul file.

`translation.json` sha256[:16] = `5adcc2bfda276f8f` (dopo l'ultima esecuzione di `check.py`, che
riscrive il file); `source.json` = `eab35484ee922877`.

## 5. Decisioni prese (contestabili)

1. **Voce della Coalizione.** I personaggi Kimek, Saryd e Arach parlano con l'ordine dei costituenti
   marcato (complemento o oggetto prima, soggetto esplicito, verbo in coda), come nei lotti L24–L26.
   La narrazione resta in italiano normale. Esempi:
   - `Interested in helping with some charity work, would you be?` → «A dare una mano con un po' di
     beneficenza, tu interessato saresti?»
   - `Grateful I am, Captain.` → «Riconoscente, io sono, Capitano.»
   - `Much better,` → «Molto meglio,»
   Il dispositivo è applicato solo alle battute di quei personaggi; Elirom (Saryd) e Pyakri (Kimek)
   lo mantengono anche nei messaggi scritti.
2. **`Factions` (idx 1 e 151) resta in inglese.** È la categoria del diario, non prosa: tradurla in
   «Fazioni» spezzerebbe il raggruppamento con gli altri file, che usano la stessa stringa e non sono
   ancora tradotti. Sta in `NT` con la motivazione scritta in `check.py`, non in una regola generale.
3. **Equipaggiamento descrittivo tradotto, nomi propri invariati.** `Heavy Anti-Missile Turrets` →
   «torrette antimissile pesanti», `Flamethrowers` → «lanciafiamme», `Jump Drive` → «motore di salto»
   (precedente di L24). Restano invariati `Bastion`, `Argosy`, `Clipper`, `Thistle`, `Finishers`,
   `Punishers`, `Spire`, `Spindle` come modelli e classi di nave.
4. **Titoli di opere teatrali tradotti.** `Twin Eclipse` → «Eclissi Gemella», `Crumbling Winter Star`
   → «Stella d'Inverno che Crolla», `The Twins' Twin Ships` → «Le navi gemelle dei gemelli»,
   `Down with the Tyrant House!` → «Abbasso la Casata Tiranna!». Sono opere inventate dentro la
   finzione, non nomi di band o di marchi: tradurle evita inglese in mezzo alla prosa e non rompe
   alcun riferimento.
5. **`Lunarium Redoubt` invariato.** È il nome della fazione di resistenza, citato anche nella
   categoria di diario non tradotta; `Redoubt` da solo non compare come parola comune.

## 6. Difetti del sorgente riprodotti, non corretti

- **Battute con citazione aperta**: l'unità 13 chiude con `I can.` senza virgoletta finale, perché la
  battuta continua nell'unità 14. Riprodotto.
- **Una sola unità con conteggio dispari** (idx 13): misurato in ricognizione prima della prima parte.
- **Refusi e costruzioni agrammaticali dell'inglese** (`to them, I lost`, `Once discovered they had`)
  sono resi in italiano corretto senza segnalarli al gioco: il repository resta intatto.

## 7. Lacuna dichiarata: due voci di diario non tradotte

Le due righe

```
log "Factions" "Lunarium Redoubt" "The Lunarium Redoubt is a resistance movement ..."
```

alle **righe 21 e 467** del file hanno prodotto **una sola unità ciascuna** (`Factions`) nel database:
il nome (`Lunarium Redoubt`) e il testo della voce di diario **non esistono in `state.db`**, quindi
non sono in questo lotto e restano in inglese nel gioco. La causa è nell'inventario (`tools/l10n.py`,
che tratta le forme `log` con delimitatori backtick ma non quella a tre argomenti fra virgolette).

`tools/l10n.py` e `state.db` sono file protetti (hash registrati): la lacuna si **documenta**, non si
ripara da questo lotto. Misura: `select count(*) from units where english like '%resistance movement%'`
→ 2 unità, entrambe in altri file. Se un lotto futuro affronta l'inventario, queste due voci vanno
aggiunte e tradotte a parte.

## 8. Limiti dichiarati

- **Nessun rendering nel gioco.** Le 730 unità non sono mai state caricate da Endless Sky; non è
  verificato che le righe lunghe stiano nelle schermate di dialogo.
- **Nessuna approvazione.** `APPROVED 364 · PENDING 32.560` invariato: lo staging non è approvazione.
- **Glossario non riconciliato** con i file ancora da tradurre: i termini di questo lotto valgono per
  `lunarium intro.txt` e per i lotti della Coalizione già chiusi.
- **Raggruppamento del diario non osservabile**: l'effetto della categoria `Factions` lasciata in
  inglese è una scelta ragionata, non una verifica a schermo.
