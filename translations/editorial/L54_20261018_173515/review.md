# L54 — revisione editoriale

`data/gegno/gegno intro missions.txt` · righe 280–676 · 159 unità · chiuso il 2026-10-18.
Questo file registra le **decisioni di traduzione** e i **limiti osservati**, non le lodi.

## 1. La voce dei Quarg: sintassi invertita, lessico celebrativo

Tutti i Quarg del gioco parlano in modo formale, ma **questo** Quarg parla in un modo che nessun altro
usa: mette il predicato prima del soggetto, accumula aggettivi encomiastici e chiama il giocatore
«brave traverser». È una scelta del testo, e la traduzione la riproduce invece di normalizzarla:

| inglese | resa |
|---|---|
| `This must be for you an exhilarating day, young traverser.` | **Questa deve essere per te una giornata esaltante, giovane viaggiatore.** |
| `Not significantly often it is that the mighty Gegno interact with daring outsiders.` | **Non è con frequenza significativa che i possenti Gegno interagiscono con audaci estranei.** |
| `You have astonishingly achieved a wondrous feat, brave traverser` | **Hai compiuto in modo sorprendente un'impresa meravigliosa, coraggioso viaggiatore** |
| `the imperious Gegno` | **gli imperiosi Gegno** |
| `a juvenile race, they are` | **una razza giovane, sono** |
| `the robust Gegno` | **i robusti Gegno** |

Le inversioni sono deliberatamente **leggere** in italiano: troppo marcate avrebbero fatto sembrare il
Quarg comico, mentre il testo lo fa sembrare **straniero e solenne** insieme. La differenza con gli altri
Quarg (ostili, secchi: «Non troverai un aiuto simile in noi») resta netta, ed è la ragione per cui il
narratore nota che «il ritmo vivace del parlato non è quello che ti aspetteresti da un Quarg».

Nota: il narratore dice anche che il giocatore si chiede se gli aggettivi nascano da **lacune della
traduzione**. Ho tradotto quella frase mantenendo il dubbio, senza spiegarlo (unità 30).

## 2. I Gegno: due rami, due estetiche

Il testo costruisce l'opposizione Vi/Scin su **come sono fatti**, non su cosa dicono:

| | Vi (L53) | Scin (L54) |
|---|---|---|
| corpo | massiccio, cornuto, peloso, curvo | esile, osseo, tre piccole corna, quasi senza peli |
| armatura | metallo pesante | piastre segmentate «a squame», oppure veste arancione |
| armi | lancia | dispositivo di disegno, poi **lama a forma di falce** |
| rapporto | scontro, sfida | osservazione, misurazione, minaccia trattenuta |

La traduzione tiene le due estetiche separate con lo stesso lessico tecnico per entrambe: `segmented
armor with many layers of plates` → **«armatura segmentata a molti strati di piastre»**,
`sickle-like blade weapons` → **«armi a lama a forma di falce»**. La falce non è una spada: il testo lo
dice esplicitamente («è a forma di falce e non di spada»), e quella differenza è ciò che rende credibile
la minaccia finale.

## 3. Il parlato Scin: «Dueyu», «Vie», «Sinn»

Gli Scin non hanno un traduttore: **disegnano** e pronunciano poche parole. Il testo distingue due
momenti, e la traduzione li riproduce alla lettera:

- **prima visita**: `"Dueyu Scin"`, `"Dueyu human..?"`, `"Dueyu Vi?"`, e poi `"Vi"` e `"Scin"` indicando
  le macchie di colore (unità 98–105);
- **seconda visita, dentro la nave**: le stesse parole ma **pronunciate diversamente** — `"Vie"`,
  `"Sinn"` (unità 148), con il verbo `enunciates` al posto di `says`.

Quella differenza è nel sorgente e **non è un refuso**: nella seconda scena il narratore è più vicino e
sente meglio la pronuncia. Ho tenuto `Vie` e `Sinn` distinti da `Vi` e `Scin`, e `Dueyu` invariato in
entrambe le scene.

`Huema` (unità 17) è il tentativo dei Quarg di dire «umano»: resta invariato, fra virgolette, perché il
giocatore deve capire che è una **parola straniera**, non un errore.

## 4. La virgoletta dispari dell'unità 59

Unità 59: il Quarg apre un discorso, lo chiude, ne apre un altro e **non lo chiude**. Nel sorgente ci sono
**tre** virgolette. La traduzione ne ha tre, con la terza che resta aperta:

```
"Certo, le coincidenze strane accadono in modo curioso. ... sottile stranezza." Il Quarg accenna a
un'espressione cupa. "A volte una può essere grande e potente, ... I Gegno l'hanno imparato un gran
numero di volte.
```

Chiudere quella virgoletta sarebbe un **miglioramento del testo inglese**, che non spetta al traduttore:
il difetto resta, ed è registrato qui perché un revisore lo troverà. `verify.py` confronta l'**insieme
degli idx** con virgolette dispari (deve essere `{59}`), non un conteggio.

## 5. Decisioni puntuali

1. **`traverser`** → **viaggiatore**, non «attraversatore»: è un titolo onorifico del Quarg, e in
   italiano «viaggiatore» regge sia l'enfasi sia la cortesia.
2. **`instigator`** → **sobillatore** (unità 8): il Quarg accusa il giocatore di fomentare, non di
   combattere.
3. **`warmongers`** → **guerrafondai** (unità 8); `aggressor` → **aggressore** (unità 2).
4. **`brutes`** → **bruti** (unità 34–35, e in L53): è la parola del Quarg sui Vi, e va tenuta dura.
5. **`progressers of research and technology`** → **cultori della ricerca e della tecnologia** (unità 10):
   «progressisti» avrebbe aggiunto una connotazione politica che il testo non ha.
6. **`Hauler`, `Behemoth`** invariati (unità 83, 127): classi di nave, come `Firebird` in L53.
7. **`freighter`** → **mercantile**; `shuttlecraft`/`shuttle` → **shuttle** (unità 67, 78).
8. **`environment suit`** → **tuta ambientale**, `pistol` → **pistola** (e `sidearm` resta «arma da
   fianco» in L53: qui il testo dice `pistol`, e la differenza è tenuta).
9. **`sickle`** → **falce**: non « Falce» con la maiuscola, è un oggetto.
10. **`Dueyu`** e i nomi propri **non si traducono**: sono già stranieri per il giocatore umano.

## 6. Cosa il lotto **non** dimostra

- Non dimostra che le sei missioni siano giocabili: i `goto` e le condizioni sui 19 `label` non sono stati
  percorsi.
- Non dimostra la resa **a schermo** dei tre rami dell'incontro (disegni, capo inclinato, lama alla gola),
  che sono quasi tutto il lotto.
- Non dimostra la coerenza con `gegno I corroboration.txt`, non ancora toccato.
- Il rapporto lunghezze (0,73–1,58) è dentro il gate ma **non è un giudizio di qualità**: il minimo
  (unità 68–70, opzioni di due parole) è fisiologico.
