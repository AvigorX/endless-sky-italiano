# REPORT — L256 (`data/human/post-war reactions.txt`, righe 40–74)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **23 controlli**; `verify.py` esce 0 con **21 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure del lotto

| voce | inglese | italiano |
|---|---|---|
| unità | 22 | 22 |
| parole | 433 | **422** (rapporto 0,97) |
| tab | 21 | 21 · **stesse unità** (2–22) |
| virgolette | 34 | 34 · **per unità identiche** |
| apici | 19 su 10 unità | 9 su 7 unità |
| segnaposto | 0 | 0 |

Rapporto per unità: **0,83 – 1,32** (gate 0,55–1,90). Tre rese sono state **accorciate** dopo la prima misura, perché il
rapporto usciva alto senza guadagno di senso:

| unità | prima | poi | rapporto |
|---|---|---|---|
| 8 | «Ah, i Pug erano reali eccome. Ne ho incontrati alcuni e ho combattuto contro di loro.» | «Ah, i Pug erano veri eccome. Ne ho incontrati e ci ho combattuto.» | 1,44 → **1,11** |
| 14 | «Come i terroristi che ci fanno saltare in aria con un'atomica» | «Come i terroristi con la bomba» | 1,84 → **1,22** |
| 18 | «Tutto quello che possiamo fare è andare avanti con la nostra vita, no?» | «Possiamo solo andare avanti con la nostra vita, no?» | 1,49 → **1,10** |

## 2. Il dialogo e i suoi segni

Le 21 battute rientrate conservano il **tab come primo carattere**; la sola unità non rientrata è la **1**, la descrizione
d'ambiente. Le 34 virgolette sono **due per battuta citata** in 17 unità: il `check.py` confronta la **mappa** unità →
conteggio, non il totale, perché un totale identico nasconderebbe una virgoletta spostata da una battuta all'altra.

Gli apici inglesi sono **19** (`you're`, `It's`, `they're`, `everyone's`, `won't`, `'Pug'`, `Navy's`, `don't`, `that's`…),
gli italiani **9**: l'italiano perde i possessivi inglesi e i futuri contratti, e guadagna elisioni proprie (`l'evento`,
`l'ammiraglio`, `dell'invasione`). La differenza è **elencata per unità** in entrambi gli script.

## 3. Il refuso voluto

| riga | inglese | italiano |
|---|---|---|
| 73 | `"Who are you, Admiral Danforts?"` | «"E tu chi saresti, ammiraglio Danforts?"» |
| 74 | `"Danforth. Admiral Danforth. Did the Navy fire you or are you here on holiday?"` | «"Danforth. Ammiraglio Danforth. La Marina ti ha licenziato o sei qui in vacanza?"» |

Il refuso **resta**: è la gag. Il `check.py` verifica che `Danforts` sia presente nella 21 e **assente** nella 22, che lì ci
sia `Danforth`.

## 4. Lessico

| inglese | resa | nota |
|---|---|---|
| `the Navy` | **la Marina** | nome comune di istituzione: si traduce |
| `Syndicate` | **il Sindacato** | come in tutti i lotti precedenti |
| `the Pug` | **i Pug** | nome proprio, invariato |
| `Admiral Danforth` | **l'ammiraglio Danforth** | grado tradotto, nome invariato |
| `Councilor Maduena Kabiru` / `Bounty's Councilor` | **il consigliere di Bounty, Maduena Kabiru** | |
| `Parliament` | **il Parlamento** | |
| `the uncanny valley` | **la valle perturbante** | termine italiano corrente |
| `talking heads` | **teste parlanti** | |
| `conspiracy theorists` | **complottisti** | |
| `bozo` | **pagliaccio** | |
| `terrorists nuking us` | **i terroristi con la bomba** | reso breve: il senso è il nucleare, la battuta è secca |
| `belly laughs` | **ridono di gusto** | con i baffi che «ondeggiano nella brezza del loro stesso respiro» |

## 5. Verifica

```
check.py   23 controlli · FAIL totale: 0 · exit 0
verify.py  21 controlli · FAIL: 0 · exit 0
segmento   0 prima · 22 qui · 65 dopo la 74 · confine riga 76 (stesso contesto) · copertura 22/87
```

L'unico difetto trovato è stato nel **`verify.py` stesso**, al primo salvataggio: una riga corrotta
(`... for x in [0]'.split(' for ')[0] if False)`) lasciava l'espressione senza `else` e il file **non compilava**. Sostituita
con la query semplice; al secondo giro, verde. **Un file che non compila non è un test fallito: è un test che non esiste** —
ed è la ragione per cui `--check-only`/lint va guardato prima di interpretare il silenzio come successo.

## 4. Correzione retroattiva (dopo L257)

Il `verify.py` di questo lotto asseriva due cose **dipendenti dal futuro**: «questo è il **solo** lotto del file» e «copertura
del file 22/87». Quando L257 ha aggiunto il secondo lotto del file, la batteria ha dato **rosso L256** con

```
SEGMENTO: questo e il solo lotto del file … FAIL ([('L256…', 22), ('L257…', 23)], 45)
copertura del file: 22/87 … FAIL 45/87
```

Riscritte sull'**invariante di segmento**: le righe del lotto sono **esattamente** quelle 40–74 e nessun'altra, e la
copertura del **segmento** è 22/22 (il totale del file è **stampato**, non asserito). Dopo la correzione: `FAIL: 0`.
È la **quarta** recidiva della stessa trappola (L46→L47, L233/L234, L235): un controllo che elenca i lotti esistenti
**non è** un invariante, perché descrive il passato del file, non il contratto del lotto.

## 5. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 22 unità `PENDING`.
- **Nessun testo visto nel gioco**.
- **Nessuna revisione umana**.
- **Il file resta aperto**: 22/87; il resto è nei lotti successivi.
