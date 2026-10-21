# REPORT — L71 · `data/successors/successor 2 ghosts myurej.txt`

## 1. Cosa contiene il lotto

**L'attesa allo spazioporto** (unità 3–15). In una zona bassa e colonnata, con vasche circolari in cui i
Successori si immergono per qualche minuto, il giocatore incontra **Ijaset**, inviato di Casa Myurej,
affiancato da due soldati. Ijaset è più cortese degli altri Myurej, e lo dice: «Non ho certo nulla contro
di te». Spiega che cosa fa la Casa oltre il wormhole: **sonde** accelerate da un cannone a bobina planetario,
perché anni fa le stelle vicine erano più collegate e si potevano mandare navi intere. Poi rivela la
missione: una **cripta nascosta** su `<planet>`, con dentro una collezione di gioielli. «Le cose più piccole
preannunciano i viaggi più grandiosi.»

**La città bombardata** (unità 16–22). Il quartiere orientale è raso al suolo, con travi contorte e piazze in
frantumi: qualcuno ha già colpito quel mondo. Ijaset guida il gruppo in una piazza identica a quella dello
spazioporto ma asciutta, trova la colonna giusta con tre braccia e apre un tunnel che scende per chilometri.

**La cripta** (unità 23–32). Una sala sferica gigantesca, con migliaia di **incassi circolari** sulle pareti
e un fascio di luce che scende dall'alto. Ijaset apre un incasso con una **sfera di dati dorata**: i filamenti
si distendono in una rete frattale, la superficie si liquefa e dietro c'è una sala di scatole di legno. Prende
pochi oggetti, la maggior parte non più grandi di una mano: «se è rimasto per mille anni, ne sopporterà altri
mille».

**L'attacco** (unità 33–42). Mentre risalgono, il dispositivo di traduzione capta un suono e perde il
controllo: Ijaset parla e le parole non arrivano, poi tornano («...le tue orecchie? ... Dobbiamo andarcene»).
La cripta trema, un proiettile ad altissima velocità colpisce un edificio, l'aria puzza di ozono. Due vie
d'uscita: correre alla nave o chiamarla via radio. In entrambi i rami il fuoco orbitale continua, gli scudi
reggono, le colonne crollano.

## 2. Scelte editoriali

| nodo | scelta | perché |
|---|---|---|
| `vault` | **cripta** | luogo sotterraneo, ricorrente («la cripta nascosta», «la sala della cripta»); nessun precedente in staging, scelta dichiarata |
| `wormhole` | **invariato** | in staging è sempre in inglese; tradurlo creerebbe una seconda nomenclatura |
| `Ijaset` (they) | **nessun participio concordato** | «La posizione e la chiave… sono state impresse in me», «Ijaset si irrigidisce»: l'italiano non deve scegliere un genere che l'inglese non dà |
| `fashioned with` | «sono state impresse in me» | rende l'idea di essere stato *progettato* per la missione senza inventare una biografia |
| `probes` / `planetary coilgun` | **sonde** / **cannone a bobina planetario** | lessico tecnico già in staging per `coilgun` (resta in inglese nel nome dell'arma, ma qui è descrizione) |
| `insets` | **incassi** | cavità circolari nelle pareti; «nicchie» è già usato per altro |
| `highborn` / `despoilers` | **nobili** / **saccheggiatori** | parole comuni, nessun neologismo |
| `gilded data-sphere` | **sfera di dati dorata** | forma già fissata per `data-sphere` |
| `repulsors` | **repulsori** | già in staging |
| `shards of which tear through a swath of columns` | «le schegge squarciano una fascia di colonne» | mantiene l'immagine fisica, senza spiegarla |
| `Trova la cripta nascosta` | titolo con verbo | forma dei nomi di missione già fissata in L68–L70 |

## 3. Difficoltà incontrate

1. **Un personaggio senza genere** (Ijaset): l'inglese usa `they` per tutti i Successori, ma l'italiano deve
   concordare gli aggettivi. Ho riscritto le frasi per evitare il problema (participi al passivo
   impersonale, riflessivi), e l'ho dichiarato qui perché è una scelta invisibile nel testo ma non nel
   metodo.
2. **42 unità in un solo contesto**, il lotto più grande del file: due parti da 21, nessun taglio a metà
   scena. Il confine successivo (riga 401, fine `Myurej 5`) è netto.
3. **Il rapporto minimo** (0,59) è vicino al gate (0,55) ma dentro: la battuta più corta è «Tutto qui?»
   (11 caratteri contro 10). Non è stato necessario riscrivere nulla, e la soglia non è stata toccata.
4. **La descrizione della sala** (unità 23) è lunga e piena di subordinate: il rischio è perdere il ritmo
   della discesa. Ho spezzato in frasi brevi come l'originale, senza aggiungere aggettivi.
5. **Nessun `LOGBOOK`**: il `check.py` dichiara l'assenza **e** verifica che nel `raw` non ci sia nessuna
   riga `log` — la premessa, non solo l'insieme vuoto (decisione 231).

## 4. Numeri osservati (output letto)

```
unita' tradotte nell'intervallo   42/42
copertura del lotto               42/42
tab IT 38 / EN 38
virgolette IT 72 / EN 72
token IT 9 / EN 9
rapporto IT/EN 0.59 - 1.33
parole EN 1632 -> IT 1546
prima/ultima riga del segmento: 311/401
duplicati inglese: 0 gruppi
FAIL totale: 0                     (33 controlli)
verify.py exit 0                   (45 controlli)
sha256[:16] translation.json      9bdce0c7e02de186
```

## 5. Stato del progetto dopo il lotto

```
TOTALE staging: 24364 unita · 778261 EN · 737571 IT
APPROVED 364 · PENDING 32560 · totale 32924
lotti con translation.json: 75
```

`successor 2 ghosts myurej.txt` è coperto **161/211 unità (76,3%)**: restano **50 unità** dopo la riga 401.

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 2 parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`/`REPORT.md`/`review.md` |
| ESEGUITO | sì | `check.py` e `verify.py` lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` → `FAIL totale: 0` (33 controlli) **e** `verify.py` → `FAIL: 0`, exit **0** (45 controlli) |
