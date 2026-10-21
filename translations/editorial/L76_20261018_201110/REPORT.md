# REPORT — L76 · `data/successors/successor 2 ghosts aqrabe.txt` (chiude il file)

## 1. Cosa contiene il lotto

**Il giardino saccheggiato** (unità 1–11). Con `<capacity>` libera, il Vujlet torna al giardino di metallo
stellare. Lo scafo resta incandescente per minuti; nella baia di carico, i fili metallici sono avvolti su
bobine enormi. Una bobina è **vuota**: qualcuno è già passato. Tiliia teme che sia «l'aggressore di
Kaatrij» — o, se la fortuna assiste, i **Quarg** in ispezione solitaria. In ogni caso: tornare subito a
Aqrabe con la notizia.

**La nave drone** (12–13). Al decollo gli allarmi di prossimità suonano: un'altra nave decolla con le armi
puntate. Distrutta, trasmette dati che «non possono essere decifrati per ora».

**Il ritorno e la resa dei conti** (14–30). Lo scarico a `<planet>` avviene sotto lo sguardo
dell'osservatore di Kaatrij; Tiliia si rilassa recitando parole «dal suono aspro e apparentemente
intraducibili». Poi spiega: era un **drone**, un guardiano automatico dei primi tempi del giardino. Ma un
cimelio di quell'età non si abbandona: **qualcosa non torna**. Segue il pagamento `<payment>` e, nel ramo
finale, le **scuse di Tiliia** per la mancanza di rispetto avuta prima della partenza: «ascoltiamo solo noi
stessi e i fantasmi degli altri».

## 2. Scelte editoriali

| nodo | scelta | perché |
|---|---|---|
| `drone ship` / `automated guardian` | **nave drone** / **guardiano automatico** | termini tecnici, non descrittivi |
| `loading bay` / `spools` | **baia di carico** / **bobine** | «rocchetti» sarebbe tessile, qui è metallo avvolto |
| `bounty` | **bottino** | è il carico recuperato, non una taglia |
| `heirlooms` | **cimeli** | oggetti di un'epoca passata |
| `the ghosts of others` | **i fantasmi degli altri** | è il titolo della linea (`Ghosts`) |
| `thine account flusher` | **il tuo conto più pieno** | arcaico reso in italiano corrente |
| `not confronted` | **identica** | `label` di salto, in `NT` |
| `'Tis impossible to know` | **È impossibile saperlo** | «tu» formale, nessun arcaismo |
| `Quarg` | invariato | nome proprio |

## 3. Difficoltà incontrate

1. **Coppia quasi identica 23/25**: la 23 chiude la virgoletta, la 25 no (`"What about this ship? Do I get
   to keep it?`). Le rese differiscono **solo** per la virgoletta finale, e il controllo lo pretende
   esattamente così: se avessi «migliorato» la 25 chiudendola, il `verify.py` sarebbe diventato rosso.
2. **Due `DIALOG` con forme diverse nel `raw`** (backtick in 12, virgolette in 13): entrambi testi, entrambi
   tradotti; il controllo asserisce anche **quale** delle due forme usa ciascuno.
3. **`LOGBOOK` 1 di forma diretta** e **`UI_LABEL` 1** nello stesso lotto: due controlli positivi.
4. **Un solo contesto** (`Aqrabe 7`) su 30 unità: nessun taglio interno, il lotto è un blocco unico.
5. **Il file si chiude**: l'invariante diventa «di file» — `0 dopo`, `max(line)`, 180/180, e la copertura
   dell'intero file verificata leggendo **tutti** i `translation.json` dei lotti.

## 4. Numeri osservati (output letto)

```
unita' tradotte nell'intervallo   30/30
copertura del lotto               30/30
tab IT 21 / EN 21
virgolette IT 43 / EN 43
virgolette dispari: (25) in inglese e in italiano
token IT 6 / EN 6   (5 famiglie)
rapporto IT/EN 0.75 - 1.26
parole EN 822 -> IT 788
prima/ultima riga del segmento: 404/478
CHIUDE il file: 0 unita dopo la riga 478 · 180 unita · max(line) 478
copertura del file intero: 180/180
FAIL totale: 0                     (35 controlli)
verify.py exit 0                   (49 controlli)
sha256[:16] translation.json      44a954ecdc2aac76
```

## 5. Stato del progetto dopo il lotto

```
TOTALE staging: 24594 unita · 785171 EN · 744192 IT
APPROVED 364 · PENDING 32560 · totale 32924
lotti con translation.json: 80
file completi: trentatré
```

`successor 2 ghosts aqrabe.txt`: **180/180 (100%)**, 5.147 EN → 4.942 IT, quattro lotti (L73–L76),
**nessuna unità approvata**.

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 2 parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`/`REPORT.md`/`review.md` |
| ESEGUITO | sì | `check.py` e `verify.py` lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` → `FAIL totale: 0` (35 controlli) **e** `verify.py` → `FAIL: 0`, exit **0** (49 controlli, invariante di file) |
