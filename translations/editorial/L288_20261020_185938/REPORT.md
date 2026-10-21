# REPORT — L288 (`data/gegno/gegno ships.txt`, righe 725–1192)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **24 controlli**; `verify.py` esce 0 con **22 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 9 (8 `DESCRIPTION` + 1 `VALUE`) | 9 |
| parole | 469 | **525** (1,12) |
| tab | 1 | 1 (unità 7) |
| virgolette | 0 | **0** |
| segnaposto / alternative | 0 / 0 | **0 / 0** |
| apici | 9 | 9 |

Rapporto per unità **1,00 – 1,18**: tutte sopra 1, come nelle schede tecniche di L286–L287.

## 2. La trappola annunciata: tre tipi nello stesso contesto

Il contratto avvertiva che `ship:Gneiss` ha **tre** unità. Il test le separa così:

```python
collections.Counter(u['kind'] for u in cov) == {'DESCRIPTION': 8, 'VALUE': 1}
[by[i]['italian'] == by[i]['english'] for i in VALUE]     # identità
[by[i]['italian'] != by[i]['english'] for i in DESCRIPTION]  # differenza
```

e aggiunge un controllo esplicito che **tutte e tre** condividano `ship:Gneiss` — così un errore di contesto (una `DESCRIPTION`
trattata come `VALUE`) fallirebbe **due** controlli invece di passare inosservato.

## 3. Il confine non è la fine della scheda

`Halite` (riga 1192) è **la prima metà** della scheda: le righe 1193–1194 sono ancora `ship:Halite` e andranno in L289. Il
`verify.py` lo verifica esplicitamente:

```python
db.execute('select context from units where path=? and line>1192 order by line limit 1') == ('ship:Halite',)
```

Senza questo controllo, un lotto che avesse «chiuso» il `Halite` con la riga 1192 avrebbe lasciato una descrizione **spezzata fra
due lotti** senza accorgersene.

## 4. Terminologia

| inglese | resa |
|---|---|
| `prototype Vi interceptor design` | **progetto di intercettore Vi allo stato di prototipo** |
| `armed to the teeth with cannons` | **armata fino ai denti di cannoni** |
| `unloading volleys of shells` | **scaricando salve di proiettili** |
| `keep a bead on other ships its size` | **tenere facilmente la mira su navi della sua dimensione** |
| `workhorse of the military` | **bestia da soma dell'esercito** |
| `lined with many mounting points` | **rivestita di numerosi punti di attacco** |
| `three huge mounts dedicated to holding enormous Ballistic Cannons` | **tre enormi supporti dedicati a ospitare giganteschi Ballistic Cannons** |
| `take a hefty beating` | **incassare colpi pesanti** |
| `threatening broadsides` | **minacciose bordate** |
| `fend off larger ships long enough for reinforcements` | **respingere navi più grandi abbastanza a lungo perché arrivino i rinforzi** |
| `fighter-based craft` | **velivolo da combattimento** |

## 5. Verifica

```
check.py   24 controlli · FAIL totale: 0 · exit 0
verify.py  22 controlli · FAIL: 0 · exit 0
segmento   16 prima · 9 qui · 12 dopo la 1192 · 7 contesti
```

**Un rosso al primo giro** (controllo mio): dichiaravo `Hornfel` **3** volte nella resa, misurate **4** (le due frasi iniziali,
«varianti degli Hornfel», «l'Hornfel è una delle navi più diffuse»). Corretto il numero nel controllo.

Una correzione **di resa** prima del test: la prima versione diceva «è un **cavallo di battaglia** dei Gegno Vi» per
`is a Gegno Vi staple`, ripetendo l'idea di «stile» già presente nella frase. Sostituito con «**è un tratto tipico** dei Gegno
Vi»: stesso significato, nessuna ripetizione.

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 9 unità `PENDING`.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Il file resta aperto**: 25/37; restano **12 unità**, tutte `DESCRIPTION`, con **quattro** coppie consecutive e **otto**
  contesti — sarà il lotto **terminale** del file.
