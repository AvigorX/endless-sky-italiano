# L3c — Revisione editoriale del blocco `data/map planets.txt` 5465–5829

84 descrizioni, 4.597 parole inglesi → 4.563 italiane. Continua la sezione 2 di L3 senza
sovrapposizioni (0 ID in comune con L1, L2, L3 e L3b). Il blocco inizia con `planet:Silwan` e si chiude
con l'ultima descrizione di `planet:Swiftsong`; l'unità successiva del file (riga 5836, `planet:Taylor`)
è fuori intervallo.

---

## 1. Metodo

Impianto identico alle sezioni precedenti: contesto letto per pianeta, glossario e checkpoint consultati
prima di ogni scelta, traduzione in quattro gruppi nell'ordine del file (1–21, 22–42, 43–63, 64–84),
rilettura del solo italiano.

Le 84 unità sono state esportate da `state.db` (tutte `PENDING`, tutte `DESCRIPTION`); `raw` coincide con
la riga del sorgente per tutte e 84 (verificato in `verify.py`).

---

## 2. Convenzioni applicate

| Termine | Resa | Occorrenze EN → IT | Note |
|---|---|---:|---|
| `Antecessors` | invariato | 1 → 1 | specie antica, **prima occorrenza nel corpus** |
| `Old Houses` | Vecchie Casate | 1 → 1 | simmetrico a `New Houses` → Nuove Casate |
| `High Houses` | Alte Casate | 1 → 1 | nome di consesso nobiliare |
| `House Sioeora` / `House Bebliss` | Casata Sioeora / Casata Bebliss | 1 / 2 | convenzione L1 |
| `Coalition` | Coalizione | 6 → 6 | decisione di L2 |
| `Lunarium` | invariato | 1 → 1 | ordine/organizzazione |
| `Twilight` | invariato | 1 → 1 | nome di regione |
| `Megasa`, `Erabu`, `Ki Patek Ka` | invariati | 2 / 3 / 1 | nomi di regione e pianeta |
| `Kor Sestor`, `Kor Mereti` | invariati | 2 / 1 | fazioni Korath |
| `spaceport` | spazioporto | 31 → 32 | glossario; un caso con ripetizione nel periodo |
| `landing pad` | piazzola di atterraggio | 9 → 9 | convenzione L1/L2 |
| `Earth` | Terra | 2 → 1 | eccezione deliberata; l'altro caso reso con "terrestri" |
| `Remembrance Day` | invariato | 2 → 2 | convenzione L1 |
| `void sprites` | spiriti del vuoto | 2 → 2 | nome descrittivo di creatura |
| `hunger towers` | torri alimentari | 1 → 1 | resa funzionale, non letterale |
| `Lofstrom launch loop` | anello di lancio Lofstrom | 1 → 1 | toponimo tecnologico, nome proprio invariato |
| `Delta V Corporation`, `Megaparsec, Inc.`, `Imo Blep`, `Betelgeuse`, `Grendel Station` | invariati | — | aziende e stazioni |

---

## 3. Interventi fatti in stesura e rilettura

| # | Prima | Dopo | Perché |
|---|---|---|---|
| 5 | "l'unico segno che su questo pianeta si celebra il Remembrance Day" | "si celebri" | concordanza al congiuntivo dopo "l'unico segno che" |
| 38 | "a soli pochi cento metri" | "a poche centinaia di metri" | errore di accordo |
| 43 | "la maggior parte sono finanziati" | "la maggior parte è finanziata" | soggetto singolare collettivo |
| 50 | "lampade solari che danno un senso di calore" | invariato dopo verifica | *sun-lamps* già reso in L3 sez. 1 |
| 53 | "vendono nulla tranne poche cose Kimek" | "vendono ben poche cose Kimek" | l'inglese è ellittico (*nothing but few*) |
| 58 | "quasi bloccate in posizione" | "quasi bloccate" | ridondanza |
| 67 | "una grande città di circa trentamila abitanti" | "una cittadina di circa trentamila abitanti" | *large town*, non *city* |
| 68 | "La Rocca di Flugbu" | "Stronghold of Flugbu" | nome di pianeta: invariato per regola |

---

## 4. Incoerenze e decisioni aperte (non bloccanti)

1. **`Antecessors` invariato** (1): prima occorrenza nel corpus. È una specie antica distinta dai
   `Predecessors` → Predecessori, e la scelta invariata crea la stessa asimmetria già segnalata per
   `Successors`. Da ratificare insieme.
2. **`Old Houses` → Vecchie Casate / `High Houses` → Alte Casate**: coerenza con Nuove Casate, ma sono
   nomi di consessi politici e andrebbero ratificati insieme a `New Houses`.
3. **`void sprites` → spiriti del vuoto** (2): nome descrittivo di creatura. Alternativa: l'invariato
   "void sprite".
4. **`hunger towers` → torri alimentari** (1): resa funzionale; l'alternativa letterale ("torri della
   fame") è ambigua in italiano.
5. Restano aperte dalle sezioni precedenti: `Successors`, `il Rim`, `caveau`, `wormhole`, `ringroide`,
   `Starlit University`.

---

## 5. Esito dei controlli

```
unità 84 · mancanti 0 · estranei 0 · vuote 0 · duplicati IT 0 · duplicati EN 0
parole 4597 -> 4563 · ratio 0.88-1.20
tab 26 (tutti gli iniziali conservati) · virgolette 12 · token <...> 0
riga grezza identica al file: 84/84 · english/kind/path/state identici al DB: 84/84
tipografia: 0 accenti sostitutivi, 0 ellissi, 0 caporali, 0 em dash, 0 apostrofi curvi
parole inglesi residue: nessuna · anglicismi evitabili: nessuno
problemi 0
```

**Non verificato:** rendering in gioco (nessun avvio, come da mandato).
