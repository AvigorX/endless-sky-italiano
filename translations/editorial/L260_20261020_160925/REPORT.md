# REPORT — L260 (`data/human/post-war reactions.txt`, righe 253–264) — LOTTO TERMINALE

**Esito: lotto CHIUSO, file COMPLETO.** `check.py` esce 0 con **23 controlli**; `verify.py` esce 0 con **21 controlli**
(invariante di **file**: 87/87). `state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

**`data/human/post-war reactions.txt` è il quattordicesimo file chiuso: 87/87 unità.**

## 1. Misure del lotto

| voce | inglese | italiano |
|---|---|---|
| unità | 7 | 7 |
| parole | 238 | **214** (0,90) |
| tab | 7 | 7 · tutte le unità |
| virgolette | 16 | 16 · per unità identiche |
| apici | 11 su 4 unità | 6 su 4 unità |
| segnaposto | 0 | 0 |

Rapporto per unità **0,91 – 1,37**: nessuna resa fuori gate.

## 2. Le virgolette, unità per unità

| unità | riga | virgolette | che cos'è |
|---|---|---|---|
| 1 | 253 | 2 | battuta di Gus |
| 2 | 256 | 2 | battuta di Gus |
| 3 | 259 | 2 | battuta di Gus |
| **4** | **261** | **0** | **narrazione**: arrivo all'officina e saluto |
| 5 | 262 | 4 | narrazione + due battute (Calvin, Gus) |
| 6 | 263 | 6 | una citazione-spezzata dal pizzicotto: `"…e spero", gli dà un pizzicotto, "che smetta…"` |
| **7** | **264** | **0** | **narrazione**: saluto finale |
| **totale** | | **16** | |

La **6** è il caso interessante: la citazione si **apre**, si interrompe con un'azione, e **riprende** — quattro segmenti di
citazione in sei virgolette. L'italiano riproduce la stessa struttura, con il pizzicotto **dentro** le virgolette.

## 3. Il lessico della scena

| inglese | resa |
|---|---|
| `choke hold` | **presa al collo** |
| `childcare district` | **distretto dell'infanzia** |
| `spaceport landing area` | **area di atterraggio dello spazioporto** |
| `scratches and bruises` | **graffi e lividi** |
| `the medic` | **il medico** |
| `he pinches him` | **gli dà un pizzicotto** |
| `the only family I have left` | **l'unica famiglia che mi resta** |
| `maintain` / `pilot their combat ships` | **manutenzione** / **pilotare le loro navi da combattimento** |
| `Honor... and service.` | **Onore... e servizio.** |
| `It isn't as profitable, but it sounds more noble.` | **Non è altrettanto redditizio, però sembra più nobile.** |
| `I dunno.` | **Boh.** |
| `let's get you to the medic` | **Dai, andiamo dal medico.** |

## 4. Verifica

```
check.py   23 controlli · FAIL totale: 0 · exit 0
verify.py  21 controlli · FAIL: 0 · exit 0
FILE       87/87 unità · 5 lotti (22 + 23 + 20 + 15 + 7) · 87 righe distinte · ultima riga 264 · 0 dopo
```

L'invariante di **file** è scritto in forma non tautologica: legge **tutti** i `translation.json` del percorso, somma i
lotti (`22 + 23 + 20 + 15 + 7`), confronta l'insieme delle righe con quello del database e solo allora stampa il totale.

## 5. Un rosso, al primo giro

Il `check.py` cercava `Gus` nell'unità **1** per verificare che i nomi propri restassero invariati — ma l'unità 1 è **Gus
che parla**, e il suo nome non vi compare; compare nella **4** (narrazione) e nella **5** (battuta di Calvin). Corretto il
riferimento (`by[5]` e `by[4]`), non l'asserzione. Verde al secondo giro.

È la differenza fra «il nome è nel lotto» e «il nome è dove credo»: il primo è un fatto misurabile, il secondo è
un'ipotesi, e il test deve verificare il fatto **nel posto giusto** o non verifica nulla.

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 7 unità `PENDING`.
- **Nessun testo visto nel gioco**.
- **Nessuna revisione umana**.
- **«Completo» significa completo in staging**, non nel gioco: 87 unità tradotte, 0 caricate.
