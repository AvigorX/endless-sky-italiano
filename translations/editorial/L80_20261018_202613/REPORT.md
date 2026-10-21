# REPORT — L80 · `data/successors/successor side missions.txt` (chiude il file)

## 1. Cosa contiene il lotto

**Il bando** (1–7). Dopo l'atterraggio l'equipaggio dello spazioporto **non rifornisce né ripara** la nave, e
un **folto contingente di ufficiali militari** si raduna intorno alla piazzola con le armi puntate, mentre
gli **intercettori** si librano sopra: costretto a decollare. Una trasmissione annuncia la decisione: «Le
tue recenti azioni contro il nostro popolo rendono molto chiaro che è stato imprudente permetterti l'accesso
al nostro spazio. Le Casate hanno decretato in consiglio che sei un nemico».

**Le tre risposte** (8–18). «È stato un incidente», «Chiedo scusa, non lo farò più», «Se lo meritavano» — e
per ognuna la reazione cutanea del Successore: **arancione fiammeggiante** («qualsiasi creatura incline a
simili 'incidenti' non ha posto fra i nostri mondi»), **rosso scuro** («le nostre flotte se ne assicureranno»),
**nero irto** (nessuna parola, solo la chiusura).

**La conseguenza** (19). Il permesso di atterraggio viene revocato; le armi puntate; la nave deve decollare.

## 2. Scelte editoriali

| nodo | scelta | perché |
|---|---|---|
| `populated language` / `uninhabited language` | **identiche** | `label` di salto: una per pianeta abitato, una per disabitato |
| `never again` / `deserved it` | **identiche** | idem |
| `the Houses have decreed in council` | **le Casate hanno decretato in consiglio** | `Houses` senza aggettivo: le Casate in generale |
| `hereforth` | **da ora in poi** | arcaico reso in italiano corrente |
| `interceptors` / `contingent` | **intercettori** / **contingente** | termini militari correnti |
| `bristling black` | **nero irto** | la pelle si irrigidisce |
| `prone to such 'accidents'` | **incline a simili 'incidenti'** | virgolette semplici mantenute |

## 3. Difficoltà incontrate

1. **Quattro `UI_LABEL` in 19 unità**: quattro label da elencare una per una, verificate identiche. È il
   massimo finora in un lotto, e ognuna è un bersaglio di salto distinto.
2. **Tre gruppi di duplicati** (5/11, 6/12, 7/13): le tre risposte ripetute nei due rami. Resa identica.
3. **Due assenze da asserire** (token 0, virgolette dispari 0): non basta non controllarle.
4. **Il file si chiude**: l'invariante diventa «di file» — `0 dopo`, `max(line)`, 164 unità, e la copertura
   dell'intero file letta da **tutti** i `translation.json` (164 id distinti su 164 righe).

## 4. Numeri osservati (output letto)

```
unita' 19/19 · copertura 19/19
tab IT 11 / EN 11 · virgolette IT 20 / EN 20 · dispari 0
token IT 0 / EN 0
rapporto IT/EN 0.93 - 1.14
parole EN 363 -> IT 354
prima/ultima riga del segmento: 416/453
CHIUDE il file: 0 unita dopo la riga 453 · 164 unita · max(line) 453
copertura del file intero: 164/164
duplicati inglese: 3 gruppi (6 unita)
FAIL totale: 0    (32 controlli)
verify.py exit 0  (36 controlli)
sha256[:16] 0cc5130f4bba902e
```

## 5. Stato del progetto dopo il lotto

```
TOTALE staging: 24758 unita · 789172 EN · 748046 IT
successor side missions.txt: 164/164 (100%) · 4001 EN -> 3854 IT · 4 lotti
file completi: trentaquattro
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 1 parte, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (32 controlli) **e** `verify.py` exit **0** (36 controlli), **file 164/164** |
