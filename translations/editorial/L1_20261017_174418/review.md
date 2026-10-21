# L1 — Revisione editoriale del blocco `data/map planets.txt` 3851–4295

120 descrizioni di pianeti, 5.230 parole inglesi → 5.167 italiane.
Riferimenti: `source.json` (originale + riga di file), `translation.json` (traduzione + `ratio`).

---

## 1. Metodo

1. Letto il testo con il contesto (le descrizioni sono sequenze per pianeta: `description` + paragrafi
   successivi con tab).
2. Consultato `glossary.csv` (81 voci) prima di ogni scelta di lessico tecnico.
3. Tradotto per gruppi di 30, tenendo il contesto dei pianeti già resi.
4. Rilettura del solo italiano come testo autonomo: 11 correzioni (elenco in §4).
5. Controllo di completezza e token con `assemble_and_check.py` (temporaneo, non fa parte della pipeline).

---

## 2. Come sono stati risolti i nomi propri

| Originale | Resa | Motivo |
|---|---|---|
| Neriene, New Argentina, New Austria, New Boston, New Britain, New China, New Finding, New Greenland, New Holland, New Iceland, New India, New Kansas, New Portland, New Sahara, New Switzerland, New Tibet, New Tortuga, New Wales, New Washington, Newhome, Nifel, Nilokep, Nimbus, Nisos Cylinder, Noluc, Norn, O-Vasa-Oa, Oasis, Oberon Station, Oblivion | invariati | nomi di pianeti: il glossario vieta di tradurli |
| Mars, Earth | **Marte, Terra** | non sono nomi inventati dal gioco ma corpi reali, che l'italiano rende così da sempre |
| Dragon, Hai, Avgi, Aberrant, Successors, Syndicate | **Hai, Avgi, Aberrant, Successors invariati; Syndicate → Sindacato** | fazioni/specie: i primi sono nomi propri; `Syndicate` è una parola comune e in italiano "Sindacato" rende il cartello economico |
| New Houses | **Nuove Casate** | nome collettivo descrittivo ("le famiglie nobili") — da ratificare, vedi §5 |
| The Grange | invariato | insegna di un locale: è un nome proprio, e nel testo è tra virgolette |
| Remembrance Day | invariato | nome di una ricorrenza del gioco, citata molte volte in tutto il corpus |
| Alpha Wars, Turf Wars | invariati | nomi di guerre/periodi storici |
| Dirt Belt, Deep | invariati | nomi di regioni |
| Cilindro di O'Neil | adattato | concetto reale (O'Neill cylinder), reso con l'articolo italiano |
| Bulk Freighters | **mercantili pesanti** | classe descrittiva, non nome proprio (style guide §2) |
| Rigellian Plague | **Peste Rigelliana** | nome di malattia, aggettivo italianizzato |
| wormhole | invariato | termine tecnico corrente in italiano; il glossario non lo copre |

---

## 3. Terminologia tecnica (glossario)

Applicate senza deroghe: `ship` → nave, `planet` → pianeta, `system` → sistema, `spaceport` →
spazioporto, `outfitter` → fornitore, `shipyard` → cantiere, `cargo` → carico (e "stiva" per lo spazio),
`fuel` → carburante, `hull` → scafo, `jump` → salto, `hyperspace` → iperspazio, `landing` → atterraggio.

Nessuna voce nuova è stata aggiunta al glossario.

---

## 4. Correzioni fatte in rilettura

| # | Prima | Dopo | Perché |
|---|---|---|---|
| 13 | "colture da fibra" | "piante da fibra" | "coltura" in italiano è l'attività, non la pianta |
| 16 | "negli anni da quando sono state colate" | "a distanza di anni dalla colata" | calco e sintassi goffa |
| 23 | "è un messaggio chiaro ai visitatori" | "vuole essere una dimostrazione inequivocabile" | il testo dice *is meant as*, cioè l'intenzione |
| 26 | "abbastanza povero che" | "così povero che" | calco di *poor enough that* |
| 29 | "sta come un'isola" | "si erge come un'isola" | "stare come" non è idiomatico |
| 37 | "devi riconoscere a malincuore il rispetto dovuto" | "non puoi fare a meno di provare, a malincuore, un certo rispetto" | più naturale e più vicino a *grudging respect* |
| 55 | "visitatori che girano" | "che si aggirano" | registro |
| 59 | "Una stravaganza così bizzarra sembra particolarmente strana" | "Un capriccio del genere sembra particolarmente strano" | ripetizione |
| 72 | "città tentacolari" | "città sconfinate" | calco di *sprawling* |
| 86 | "relitto di un periodo" | "residuo di un'epoca" | "relitto" suggerisce un oggetto |
| 106 | "le hanno abitate" | "le hanno colonizzate" | il testo dice *colonized* |

---

## 5. Decisioni che richiedono ratifica umana

1. **`Syndicate` → "Sindacato"**: nessuna occorrenza approvata in precedenza, quindi non c'è conflitto;
   ma è una scelta di universo e va confermata una volta per tutte.
2. **`New Houses` → "Nuove Casate"**: se altrove il gioco lo tratta come nome proprio di fazione,
   conviene tornare all'inglese. Da verificare sui testi dei Successors.
3. **`Remembrance Day` invariato**: se il progetto decide di tradurre i nomi delle ricorrenze, va
   cambiato in tutto il corpus (molte occorrenze), non solo qui.
4. **`Bulk Freighters` → "mercantili pesanti"**: verificare che la schermata di acquisto navi usi la
   stessa resa per la classe.

---

## 6. Ambiguità e limiti

- **Nessuna occorrenza di `discharge`, `disruption`, `scrambling`** in questo blocco (verificato):
  le decisioni terminologiche di K4 restano aperte e non sono state toccate.
- **`square dances` / `line dances`** (unità 5) rese "quadriglie e danze in fila": il riferimento
  culturale è americano e non ha un equivalente perfetto; è la resa meno straniante.
- **`the Deep`** lasciato in inglese: se in futuro si traduce il nome della regione, va fatto ovunque.
- I nomi dei pianeti restano inglesi per scelta: il giocatore vedrà "New Argentina" in un testo italiano.
  È coerente con il glossario, ma è un effetto da mettere in conto.

---

## 7. Esito dei controlli

`check_results.json`:

```
unità 120 · parole 5230 -> 5167 · ratio 0.87-1.24
ids_complete True · tabs True · quotes True · tokens True · no_empty True
problemi 0
```

Due segnalazioni di "parola inglese residua" (unità 5 e 6) sono i nomi propri **"The Grange"**: attese,
non errori.

**Non verificato:** il rendering in gioco (nessun avvio, come da mandato).
