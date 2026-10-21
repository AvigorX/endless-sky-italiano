# REPORT — L270 (`data/human/engines.txt`, righe 488–717) — **LOTTO TERMINALE**

**Esito: lotto CHIUSO, file CHIUSO.** `check.py` esce 0 con **26 controlli**; `verify.py` esce 0 con **23 controlli**.
`state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 17 (tutte `DESCRIPTION`) | 17 |
| parole | 545 | **527** (0,97) |
| tab | 4 | 4 · primo carattere |
| virgolette | 0 | 0 |
| apici | 7 | 8 |
| segnaposto | 0 | 0 |

Rapporto per unità **0,81 – 1,24**. Il totale italiano è **più corto** dell'inglese: la serie Atomica usa formule brevi e
ripetute («Deep Sky's atomic thrusters») che in italiano diventano «i propulsori atomici della Deep Sky» senza crescere.

## 2. Il lotto

| equipaggiamento | che cosa dice |
|---|---|
| **Tyrant** steering | come il propulsore omonimo: così grande che **pochissime navi** lo usano |
| **Capybara** reverse | per le navi che non riescono a fare **virate di 180°** per fermarsi in tempo |
| **A120** thruster | il più potente che entri nella nave, se hai **denaro da buttare**; energia e raffreddamento mangiano il vantaggio |
| **A250** thruster | in produzione **da secoli**, resta di nicchia per prezzo e consumi |
| **A370** thruster | entra in una nave leggera, muove quasi tutto, a **prezzo esorbitante** |
| **A520** thruster | «sarai l'invidia di ogni pilota della galassia» |
| **A860** thruster | il più potente **venduto nello spazio umano**; serve più energia e più raffreddamento |
| **A125** steering | popolare sulle astronavi di fascia alta; un set può **costare più della nave** |
| **A255** steering | l'ultima risorsa quando la manovrabilità è esaurita |
| **A375** steering | il sogno dei **cacciatori di taglie** |
| **A525** steering | piccole navi da guerra come un caccia; sulle grandi **libera spazio** |
| **A865** steering | «il capolavoro della Deep Sky», per pochi |
| **AR120** reverse | per le **acrobazie** che quasi nessuno sa replicare |

## 3. Due note ripetute, riprese alla lettera

- **nota del plasma** (unità 1 e 3) — identica a quella di L269 (otto copie là, due qui);
- **nota del montaggio** del propulsore inverso (unità 5 e 17) — identica a quella di L268 (unità 15).

Il `check.py` non si fida della memoria: **riapre** `L269/translation.json` e `L268/translation.json` e confronta gli insiemi
delle rese per la stessa stringa inglese. Se una sola parola fosse cambiata, sarebbe rosso con conteggi identici.

## 4. L'invariante di FILE (finalmente legittima)

Nei lotti non terminali asserire la copertura totale sarebbe un'affermazione sul futuro. Qui il file **finisce**:

```
database:  61 unità, righe 27–717, ultima unità alla 717
somma dei quattro lotti (L267 + L268 + L269 + L270): 61
righe distinte: 61  ·  prima 27  ·  ultima 717  ·  dopo la 717: 0
copertura: 61/61 (100%)
```

`verify.py` verifica **tutte e cinque** le righe di questa tabella in modo indipendente da `check.py`.

## 5. Verifica

```
check.py   26 controlli · FAIL totale: 0 · exit 0
verify.py  23 controlli · FAIL: 0 · exit 0
segmento   44 prima · 17 qui · 0 dopo (fine file) · 14 contesti · 4 tab
```

Un rosso al primo giro: chiedevo che **tutti e dieci** i numeri Atomici comparissero nel **testo** italiano, ma nove stanno
solo nel **contesto** (`outfit:A370 Atomic Thruster`), che non è testo tradotto. Corretto in due asserzioni misurate: i dieci
numeri nei **contesti**, e l'unico numero che compare nel testo inglese (`A860`) anche in italiano.

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 17 unità `PENDING`; il file è **finito in staging**, non approvato.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Il file è completo al 100%** solo in staging: 61 unità su 61, tutte `PENDING`.
