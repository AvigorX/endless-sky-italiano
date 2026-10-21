# L9 — Revisione editoriale del blocco `data/map planets.txt` 1395–1820

82 descrizioni, 4.523 parole inglesi → 4.460 italiane. Quinto lotto del tratto iniziale del file, nessun
ID in comune con L1–L8. Inizia con `planet:Dwelling of Speloog` e si chiude a fine pianeta con
`planet:Farwater` (riga 1820); l'unità successiva (riga 1826) apre Featherweight.

---

## 1. Metodo

Stesso impianto dei lotti precedenti: contesto letto per pianeta, glossario e checkpoint consultati prima
di ogni scelta, traduzione in quattro gruppi nell'ordine del file (1–21, 22–42, 43–62, 63–82), rilettura
del solo italiano.

Le 82 unità sono state esportate da `state.db` (tutte `PENDING`, tutte `DESCRIPTION`); `raw` coincide con
la riga del sorgente per tutte e 82 (verificato in `verify.py`).

---

## 2. Convenzioni applicate

| Termine | Resa | Occorrenze EN → IT | Note |
|---|---|---:|---|
| `Gegno` | invariato | 14 → 13 | l'unità 15 usa al terzo posto "quelli più vicini alla tua statura" invece di ripetere il nome (anafora) |
| `Scin` / `Vi` | invariati | 5 / 1 | sottospecie `Gegno Scin`, `Gegno Vi` |
| `Arachi`, `Heliarch`, `Quarg`, `Remnant`, `Aberrant`, `Saryd`, `Kimek`, `Hai`, `Unfettered` | invariati | 2/4/3/1/1/5/1/3/1 | specie e fazioni |
| `Korath`, `Kor Mereti`, `Kor Sestor` | invariati | 6 / 2 / 1 | — |
| `Bunrodea` / `Bunrodean` | invariati | 5 → 5 | §7 punto 5 ancora aperto |
| `Consonance` | **invariato** (provvisorio) | 1 → 1 | coerente con L2 unità 36; vedi §4 punto 1 |
| `Coalition` | Coalizione | 4 → 4 | decisione L2 |
| `Republic` | Repubblica | 2 → 2 | `Republic Navy` → Marina della Repubblica |
| `Earth` | Terra | 5 → 5 | eccezione deliberata |
| `the Core` | "il Nucleo" | 1 → 1 | maiuscola = regione; `core systems` in L7 era "sistemi centrali" |
| `Bunrodean Hegemony` | Egemonia Bunrodean | 1 → 1 | `Hegemony` è nome comune politico: tradotto |
| `the Queen` / `royal palace` / `royal guards` | la Regina / palazzo reale / guardie reali | — | — |
| `ringworlds` | mondi ad anello | 1 → 1 | convenzione L3d |
| `the Incursion` | l'Incursione | 1 → 1 | convenzione L2 |
| `Empire`-type nomi di istituzioni | **invariati**: `Royal University of Dogen`, `Military Academy of Fuhtiiski` | 1+1 | come `Starlit University` (§7 ancora aperto) |
| `Tarazed Corporation`, `Peripheria`, `Navigeo`, `Ochrescoop`, `Greymoon`, `Aventine`, `Araio`, `Wah Ki`, `Sef`, `Anax`, `Eragaru Le`, `Mnai`, `Kasii-Cavaasa` | invariati | — | nomi propri |

`terraformazione`: 4 occorrenze, sempre invariata come termine. `iperspazio`/`iperpropulsore` secondo
glossario. `ascensore spaziale`, `habitat cilindrici`, `materiali fissili`, `cavi orbitali` resi come
termini tecnici correnti.

---

## 3. Interventi fatti in stesura e rilettura

| # | Intervento | Perché |
|---|---|---|
| 58 | sorgente `Kasii-Cavasaa` → **Kasii-Cavaasa** | terzo refuso del sorgente: il pianeta è `Cavaasa-Vasa-Tej` e in L7 la stella era già `Kasii-Cavaasa`. Normalizzato, non propagato |
| 4 / 5 | due varianti quasi identiche della descrizione della Terra | differenze conservate ("gran parte della sua superficie" / "la sua superficie"; "mentre altri" / "mentre altri" in posizione diversa): erano distinte in originale |
| 15 | terzo `Gegno` reso con "quelli più vicini alla tua statura" | evita tre ripetizioni dello stesso nome in un periodo |
| 18 | `island vessels` → "porti-isola" | il testo parla di porti, non di navi |
| 32 | `abundance of volatiles` → "abbondanza di sostanze volatili" | resa tecnica corretta, non "volatili" |
| 33 | `upmass` → "carico in uscita" | evita l'anglicismo gergale |
| 39 | nomi delle accademie lasciati in inglese | coerente con `Starlit University` invariato |
| 41 | `applied energistics` → "energistica applicata" | — |
| 61 | `vomits vast slabs` → "vomita vasti lastroni" | immagine cruda conservata |
| 71 | `"the last candle-flame"` → "l'ultima fiammella di candela" | virgolette conservate attorno alla glossa |
| 76 | `Maginot Line` → "Linea Maginot" | nome storico reale |
| 80 | `run-down pubs` → "pub malandati" | — |

---

## 4. Incoerenze e decisioni aperte (non bloccanti)

1. **`Consonance`: scelta provvisoria.** L'unità 41 richiede il nome della compagine che gestisce la
   ricerca. Ho mantenuto **"Consonance" invariato**, come in L2 unità 36, e non "Consonanza". Resta
   l'incoerenza già annotata con L2 unità 59 ("Assemblea delle Entità Consonanti"): la ratifica di §7
   punto 2 vale per tutto il corpus e non è stata anticipata qui.
2. **`Bunrodean Hegemony` → Egemonia Bunrodean** (1): primo uso del nome dello Stato. Se in altri file
   compare come "Egemonia Bunrodea" va uniformato.
3. **`the Core` → "il Nucleo"** (1): primo uso della regione con la maiuscola. Alternativa: "il Centro".
4. **`Kasii-Cavasaa`** (1): refuso normalizzato in `Kasii-Cavaasa`. Terzo refuso del sorgente incontrato
   (dopo `Cavasaa-Vasa-Tej` in L7 e `Unlikely` in L8).
5. **Nomi di accademie invariati** (2): coerente con `Starlit University`, ma se si decide di tradurre i
   nomi delle istituzioni la modifica riguarda almeno tre lotti.
6. Restano aperte: `Successors`, `Antecessors`, `caveau`, `ringroide`, `Starlit University`, `Costruttori`,
   `Key Stones`, `skyhook`, `il Rim`, `Halite`, `Bulk Freighter`, `Twilight Guard`.

---

## 5. Esito dei controlli

```
unità 82 · mancanti 0 · estranei 0 · vuote 0 · duplicati IT 0 · duplicati EN 0
parole 4523 -> 4460 · ratio 0.86-1.29
tab 23 (tutti gli iniziali conservati) · virgolette 6 (unità 23 e 71) · token <...> 0
riga grezza identica al file: 82/82 · english/kind/path/state identici al DB: 82/82
tipografia: 0 accenti sostitutivi, 0 ellissi, 0 caporali, 0 em dash, 0 apostrofi curvi
parole inglesi residue: nessuna · anglicismi evitabili: nessuno
problemi 0
```

Nessun errore rilevato dai controlli al primo passaggio. Le unità 4 e 5 hanno inglese quasi identico ma
non sono duplicati: la traduzione conserva la differenza, e il controllo duplicati resta a 0.

**Non verificato:** rendering in gioco (nessun avvio, come da mandato).
