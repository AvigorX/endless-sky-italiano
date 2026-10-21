# review.md — L277 (`data/korath/korath ships.txt`, righe 2010–2363)

Registro delle decisioni editoriali dell'**ultimo lotto** delle navi Korath: le sette `Model` dei Kor Mereti, cioè la storia di
un drone che diventa un'arma.

## 1. Un testo in sette tappe

La serie numerata (8, 16, 32, 64, 128, 256, 512) non è un catalogo: è un **ciclo di vita**. Ogni scheda presuppone le
precedenti, e la resa ha dovuto tenere i **nessi** invece di tradurre sette paragrafi isolati.

| tappa | inglese | resa |
|---|---|---|
| minerario | `primary role … is asteroid mining` | **il ruolo principale … è l'estrazione mineraria sugli asteroidi** |
| riadattato | `lasers can also be employed as offensive weapons` | **i loro laser possono anche essere usati come armi offensive** |
| modulare | `constructed in a modular fashion, which allows them to grow` | **costruiti in modo modulare, il che permette loro di crescere** |
| vivo | `built their drones to mimic life: capable of growth and development` | **costruirono i loro droni imitando la vita: capaci di crescere e svilupparsi** |
| riconfigurabile | `convert the drones from one configuration to another` | **convertire i droni da una configurazione all'altra** |
| fregata | `serves … in much the same way as a human Frigate` | **serve … più o meno come una fregata umana** |
| scissione | `they split down the middle` | **si dividono a metà** |
| arma | `a weapon that outlives its creators` | **un'arma che sopravvive ai suoi creatori** |
| anello | `a perfect ring, with … turrets firing in every direction` | **un anello perfetto, con … torrette che sparano in ogni direzione** |

## 2. Il detto dei Quarg

> «Fra i Quarg si dice che ogni specie che insista nello studiare la guerra finirà per costruire un'arma che sopravvive ai
> suoi creatori. Per i Korath, i loro droni da guerra ci sono andati molto vicini.»

L'ordine delle due frasi è quello del sorgente, e conta: prima la **massima generale**, poi l'applicazione ai Korath. Invertirle
avrebbe trasformato un proverbio in una battuta sui Korath. `very nearly done so` → «**ci sono andati molto vicini**» conserva
l'ambiguità (non è ancora successo, ma quasi).

## 3. Lessico

| inglese | resa | nota |
|---|---|---|
| `drone` | **drone** / **droni** | è anche parola italiana: non si traduce |
| `Frigate` | **fregata** | categoria navale umana |
| `firepower` | **potenza di fuoco** | |
| `shields` / `turrets` | **scudi** / **torrette** | |
| `automated factories` | **fabbriche automatiche** | |
| `life cycles` | **ciclo vitale** | |
| `Kor Mereti` | **Kor Mereti** | invariato |

## 4. I nomi numerati

`Model 8` … `Model 512` restano **invariati**, e il numero non si «italianizza» né si scrive a parole: è il nome della nave
nel gioco, e il `check.py` verifica che nessuna resa contenga la parola `Model`.

## 5. Struttura

| cosa | inglese | italiano |
|---|---|---|
| tab | **0** | **0** |
| virgolette | **0** | **0** |
| apici | **0** | **4** (`l'estrazione`, `all'altra`, `un'arma`, `dell'evoluzione`) |
| segnaposto | **0** | **0** |

È il lotto più «pulito» del file: nessun tab, nessuna virgoletta, nessun apice inglese, nessun segnaposto.

## 6. Chiusura del file

`data/korath/korath ships.txt` è **50/50** in staging: cinque lotti (L273 8, L274 9, L275 14, L276 12, L277 7), righe 95–2363,
tutte `PENDING`.

Cosa **non** significa: non è approvato, non è stato visto nel gioco, non è stato revisionato da una persona. Significa che in
staging **non manca nessuna unità** del file — e `verify.py` lo dimostra sommando i cinque lotti, contando le righe distinte e
verificando che dopo la 2363 non ci sia nulla.
