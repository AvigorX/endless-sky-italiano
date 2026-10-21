# STATO — L135 · `data/starts.txt` (file nuovo: gli inizi di partita)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L135_20261019_131024` |
| Righe / unità | **18–130** / **32** — su 113 unità del file (**28,3%**) |
| Tipi | **18 `CONVERSATION`** · **8 `LOGBOOK`** · **4 `DESCRIPTION`** · **2 `VALUE`** |
| `UI_LABEL` · token | **0** · **0** — **due asserzioni vuote scritte** |
| Stati | **32 `PENDING`** — misurato e **asserito** |
| Contesti | **4 completi** — `start:default` 3, `conversation:default intro` 13, `start:deep` 3, `conversation:deep intro` 13 |
| Testi distinti | **27** su 32 — **5 frasi ripetute** fra i due inizi (21–25 = 5–9) |
| Parole | **1.485 EN → 1.448 IT** (0,975); per unità 0,94–1,28, media 1,05 |
| Tab · virgolette | **14 unità** · **14** (nessuna unità dispari) |
| sha256 | `f897bd0f3d943382…` |
| `check.py` | **29 controlli**, `FAIL totale: 0` |
| `verify.py` | **29 controlli**, exit **0** — invariante di **segmento** |

## Un tipo di file mai visto

`starts.txt` sono **gli inizi di partita**: la scelta iniziale del giocatore.

| `kind` | che cos'è | resa |
|---|---|---|
| `VALUE` | **il nome dell'inizio** (`Endless Sky`, `Deep Desire`) | **identico al sorgente** |
| `DESCRIPTION` | il testo della scelta nel menu | tradotto |
| `CONVERSATION` | la scena iniziale (banca, treno, ufficio) | tradotto |
| `LOGBOOK` | le voci di diario | tradotto |

`VALUE` non è più «nome di missione»: è **nome di modalità di gioco**. Resta inglese per la stessa ragione, ed è la
prima volta che il progetto incontra questa forma.

## Zero token, in tutto il file

```python
assert collections.Counter(t for u in SRC for t in TAGS.findall(u['english'])) == {}
```

Non è «nessun token in questa finestra»: il file **non ne contiene nessuno**, su 113 unità. Il controllo è `== {}`,
più forte di una lista vuota, e vale per tutti i lotti futuri di `starts.txt`.

## Cinque frasi ripetute, cinque rese identiche

`start:default` e `start:deep` condividono lo stesso blocco di storia (Repubblica, Parlamento, Sindacato, ambiente,
pirati). Le unità **21–25** ripetono **5–9**, e la resa è la **stessa** — verificata per confronto diretto, non a
occhio:

```python
ck('5 frasi ripetute con resa identica (21-25 = 5-9)',
   all(by[a]['italian'] == by[b]['italian'] for a, b in ((21, 5), (22, 6), (23, 7), (24, 8), (25, 9))))
```

## Le scelte di lingua

| termine | resa | perché |
|---|---|---|
| `Deep` | **Deep** | nome di regione: 266 occorrenze già così in staging |
| `Dirt Belt` | **Dirt Belt** | nome di regione: 27 occorrenze già così |
| `Syndicate` | **Sindacato** | 338 occorrenze |
| `Paradise Worlds` | **Mondi del Paradiso** | forma dominante |
| `Navy` · `Republic` | **Marina** · **Repubblica** | 642 e 380 occorrenze |
| `480,000 credits` · `0.4%` | **480.000 crediti** · **0,4%** | convenzione italiana, come nei lotti precedenti |
| `Peace. Prosperity. Progress.` | **Pace. Prosperità. Progresso.** | motto già tradotto così altrove |

Nessun numero cambia **valore**: cambia solo il separatore (`,` → `.`, `.` → `,`). Il controllo vieta esplicitamente
che resti una forma inglese (`480,000`, `0.4%`, `2,503`, …).

## Verifica

```bash
cd staging/editorial/L135_20261019_131024
python mkparts.py   # 32 unità · 27 distinti · 4 contesti completi · 14 tab · 14 virgolette
python check.py     # FAIL totale: 0 (29 controlli)
python verify.py    # exit 0 (29 controlli, invariante di segmento)
```

**Non verificato**: nessuna partita avviata con questi inizi. La verifica è testuale e a exit code.
