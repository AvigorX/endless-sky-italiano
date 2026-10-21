# REPORT — L319 (`data/korath/korath weapons.txt`, righe 615–1222) — **LOTTO TERMINALE**

**Esito: lotto CHIUSO, file CHIUSO a 39/39.** `check.py` esce 0 con **24 controlli**; `verify.py` esce 0 con **22 controlli**.
`state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 22 (20 `DESCRIPTION` + 2 `VALUE`) | 22 |
| parole | 612 | **643** (1,051) |
| tab | **5** | **5** |
| virgolette | **0** | **0** |
| segnaposto / alternative | 0 / 0 | **0 / 0** |
| apici | **4** (3 unità) | 11 |

Rapporto per unità **0,93 – 1,27**. Il massimo è la nota dei rifornimenti (1,274): una frase corta inglese che in italiano chiede
l'articolo e il verbo («Le munizioni per quest'arma possono essere rifornite…»); il minimo è la scheda del `Firelight Missile` (0,926),
dove l'inglese usa **tre participi** (`must be kept minimally active … to ensure it is ready`) che l'italiano risolve con un infinito
solo.

## 2. Invariante di FILE

```
FILE        39/39 (100%) · somma lotti 17 (L318) + 22 (L319) = 39
RIGHE       39 distinte · prima 53 · ultima 1222 · zero dopo
TIPI        37 DESCRIPTION + 2 VALUE
```

`data/korath/korath weapons.txt` è il **trentaquattresimo** file chiuso nel progetto (**93** su 167).

## 3. Un lotto di «come funziona»

Le schede di questo lotto spiegano **meccanismi**, non tattiche:

| arma | il meccanismo |
|---|---|
| `Cluster Mine Layer` | la mina fa **meno danni** se la colpisci **prima** che si dispieghi |
| `Shield Disruptor` | permette di danneggiare lo scafo **anche con gli scudi attivi**, ma da solo fa poco |
| `Husk-Slice` | inefficace sugli scudi, **taglia la corazzatura come carta** |
| `Langrage Hyper-Heaver` | converte **rottami** in un campo di detriti; a distanza ravvicinata **respinge**, poi il campo **collassa** in una nube letale |
| `Firelight` | il reattore resta **attivo al minimo** e produce «un filo di energia» |
| `Microbot Grinder` | **bocche**, **artigli**, **sciame omicida**: scompone in molecole |
| `Firestorm Battery` | il reattore **senza involucro né sicurezze**: esplosione che **respinge e fonde** gli scafi |

Il filo è **l'economia del rischio**: ogni arma Korath **paga** qualcosa (danni ridotti, inefficienza, calore, instabilità) per
ottenere un effetto che le altre non hanno. La resa conserva ogni **«ma»**: «Da sole, però, fanno pochissimi danni», «Sebbene meno
raffinato…», «Benché terribilmente inefficiente…».

## 4. Le due generazioni

```
Firestorm (vecchia)  →  nessuna schermatura, nessuna sicurazza, esplosione enorme
Firelight (nuova)    →  reattore miniaturizzato, pronto al lancio, missili per navi piccole
```

Il testo dice **esplicitamente** che il `Firelight` **deriva** dal `Firestorm` (1049) e che il `Firestorm` è «**meno raffinato** della
più recente versione Firelight» (1221). Il test verifica **entrambe** le citazioni incrociate: è il modo per non confondere le due
famiglie in una traduzione che, per il resto, è fatta di nomi **invariati**.

## 5. La nota dei rifornimenti, tre volte in un lotto

| riga | contesto |
|---|---|
| 659 | `Cluster Mine Layer` |
| 1051 | `Firelight Missile Bank` (seconda tab dello stesso contesto) |
| 1222 | `Firestorm Battery` (ultima riga del file) |

Resa **identica** a L318, che era la **di maggioranza** del corpus. `verify.py` non si fida di questa dichiarazione: **cerca** la
stringa italiana in tutti gli altri lotti (misurate **≥16** occorrenze). Zero occorrenze avrebbe significato «resa inventata qui».

## 6. Verifica

```
check.py   24 controlli · FAIL totale: 0 · exit 0
verify.py  22 controlli · FAIL: 0 · exit 0
FILE       39/39 (100%) · trentaquattresimo file completo
```

**Un rosso al primo giro**, mio, e **lo stesso errore di L311**: la catena di uguaglianza univa **italiano e inglese**
(`it659 == it1051 == it1222 == en659`). Spezzata in **due** asserzioni. È la seconda volta in venti lotti: la regola è nella skill,
ma il gesto va **ricordato al momento di scrivere la riga**, non solo letto.

## 7. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 22 unità `PENDING`; il file è **finito in staging**, non approvato.
- **Nessun testo visto nel gioco**: i meccanismi (danni ridotti, scudi attivi, fusione degli scafi) sono verificati **nei dati**.
- **`langrage` resta `langrage`**: è un prestito marinaresco inglese (ghiaia usata come mitraglia) e nel testo è già **nome proprio**
  dell'arma; tradurlo con «ghiaino» avrebbe introdotto un termine che il giocatore non collega all'arma.
