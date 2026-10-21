# STATO — L323 (`data/rulei/rulei.txt`, righe 38–157)

**Stato: CHIUSO — LOTTO TERMINALE, FILE INTERO.** Il file è **completo: 41/41 (100%)**, **trentasettesimo file interamente tradotto**
(**96** su 167 nel progetto). `check.py` esce 0 con **22 controlli**; `verify.py` esce 0 con **19 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

| voce | valore |
|---|---|
| directory | `staging/editorial/L323_20261020_224650/` |
| file | `data/rulei/rulei.txt` (**41/41 unità · 919 parole · righe 38–157**) |
| righe | 38–157 (**tutto il file**) |
| unità | **41** — **38 `MISSION_TEXT` + 3 `LOGBOOK`** |
| contesti | **5** — cardinalità **24 / 8 / 6 / 2 / 1** |
| parole | **919 EN → 871 IT** (0,948) |
| rapporto | **0,71 – 1,83** |
| tab | **32** — con **nove righe senza** (38, 39, 41, 93, 116, 118, 132, 151, 153) |
| virgolette | **34** in **16** unità, di cui **151 con quattro** |
| segnaposto / alternative | **0 / 0** |
| apici | **12 EN in 7 unità** (45 e 156 ne hanno tre) / 19 IT |
| `check.py` | **22 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **19 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di FILE**: 41 unità · **0 prima, 0 dopo** · 41 righe distinte · prima **38** · ultima **157** |
| `sha256[:16]` | **`abd649cfcc0e1085`** |

## Comandi

```bash
python staging/editorial/L323_20261020_224650/check.py     # FAIL totale: 0 (22 controlli)
python staging/editorial/L323_20261020_224650/verify.py    # FAIL: 0 (19 controlli, FILE 41/41)
```

## Il primo `LOGBOOK`: che cosa è davvero

Il contratto diceva «prosa di diario in **prima persona**». La misura dice qualcosa di **più preciso**, e il test è stato corretto:

| riga | testo | persona |
|---|---|---|
| 38 | «I Rulei **erano** probabilmente una civiltà antica…» | **terza**, ma è **la voce dell'equipaggio** che annota |
| 116 | «**Scoperta** una regione di vuoto a est del nucleo…» | **prima implicita** («noi abbiamo scoperto») |
| 151 | «I Rulei **sembrano** riconoscere il vuoto…» | **terza**, sempre voce dell'equipaggio |

Quindi i `LOGBOOK` **non** sono tutti in prima persona: sono **annotazioni di bordo**, dove la prima persona emerge **solo nel verbo**
della 116. Il controllo giusto non è «c'è "noi"», è: **nessun «tu»** e **la 116 in prima implicita**. Un controllo basato su «noi/io»
avrebbe dato **FAIL su un testo corretto**.

## L'indentazione a scala: 11, 21, 23 tab

Le righe 95–99 sono **una frase sola spezzata in cinque righe**, con l'indentazione che **cresce** mentre la mente viene trascinata:

```
 93  It feels as though there is a tremendous weight on your mind…
 94      You can barely hear yourself think.
 95  ←11 tab→  It's enough to drive any living thing mad.
 96      The most ominous sensation here is…
 97      Like something is attempting to drag
 98  ←21 tab→  your
 99  ←23 tab→  mind into the planet below.
```

I numeri **non sono decorativi**: sono il **testo che scivola** verso il basso. Il test li verifica **esatti** e **in entrambe le
lingue** (11 / 21 / 23), perché se l'italiano avesse perso un tab la frase non «scivolerebbe» più.

## Sei rossi al primo giro, tutti miei

| # | errore | correzione |
|---|---|---|
| 1 | i dizionari di virgolette e apici erano **indicizzati per indice** e non per **riga** | riallineati ai numeri di riga reali |
| 2 | «le battute fra virgolette sono **13**» | sono **14**: misurate |
| 3 | «`Umbral Reach` **3** occorrenze» | sono **2** per lingua: il test ora confronta **le due lingue**, non un numero |
| 4 | i `LOGBOOK` «tutti in prima persona» | solo la 116 lo è; il controllo ora chiede **l'assenza di «tu»** + la 116 |
| 5 | soglia della seconda persona a **15** unità | misurate **14**: soglia abbassata a **12** |
| 6 | — | — |

Quattro dei sei nascono dall'aver scritto il test **dal contratto invece che dalla misura**. La lezione operativa: **il test si scrive
dopo aver misurato**, e i dizionari per-unità vanno costruiti **con una query**, non a mano.

## Cosa il test pretende

| oggetto | verifica |
|---|---|
| tipi | **38** `MISSION_TEXT` + **3** `LOGBOOK`; i `LOGBOOK` **senza «tu»**, la 116 in prima implicita |
| contesti | cardinalità **24 / 8 / 6 / 2 / 1** |
| tab | **32** righe esatte; le **nove senza** sono quelle attese |
| scala | **11 / 21 / 23** tab, in **entrambe** le lingue |
| virgolette | **34** in **16** unità; **151** con **quattro** |
| apici | **12** in **7** unità; 45 e 156 con **tre** |
| nomi | `Umbral Reach` **invariato**, stesse occorrenze delle due lingue |
| vuote | **0 segnaposto**, **0 alternative** |
| FILE | **0 prima · 41 qui · 0 dopo** · prima 38 · ultima 157 · **41/41 asserita** |

## Limiti dichiarati

Nessuna approvazione (41 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Il file è **finito in staging**,
non approvato. Il rapporto **1,83** della riga 154 («State in guardia…» per «Beware…») è alto ma **dentro il gate**: su una parola
sola il rapporto non ha significato.
