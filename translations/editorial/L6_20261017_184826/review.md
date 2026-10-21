# L6 — Revisione editoriale del blocco `data/map planets.txt` 357–728

84 descrizioni, 4.586 parole inglesi → 4.564 italiane. Secondo lotto del tratto iniziale del file,
0 ID in comune con L1–L5. Inizia con `planet:Asgard` e si chiude a fine pianeta con
`planet:Builder Settlement` (riga 728); l'unità successiva (riga 733) appartiene a Bunthro.

---

## 1. Metodo

Impianto identico ai lotti precedenti: contesto letto per pianeta, glossario e checkpoint consultati
prima di ogni scelta, traduzione in quattro gruppi nell'ordine del file (1–21, 22–42, 43–63, 64–84),
rilettura del solo italiano.

Le 84 unità sono state esportate da `state.db` (tutte `PENDING`, tutte `DESCRIPTION`); `raw` coincide con
la riga del sorgente per tutte e 84 (verificato in `verify.py`).

---

## 2. Convenzioni applicate

| Termine | Resa | Occorrenze EN → IT | Note |
|---|---|---:|---|
| `the Deep` | invariato | 4 → 4 | nome di regione; la quinta occorrenza inglese è l'avverbio *deep* ("deep in the jungles"), non il toponimo |
| `Paradise Worlds` | Mondi Paradisiaci | 1 → 1 | plurale di `Paradise World` → Mondo Paradisiaco (decisione da ratificare) |
| `Parliament` | Parlamento | 1 → 1 | — |
| `Confederated Councils` | **invariato** | 1 → 1 | nome di fazione/Stato |
| `the Builders` | Costruttori | 1 → 1 | epiteto di specie, non nome proprio: da ratificare (vedi §4) |
| `Ka'sei` | invariato | 1 → 1 | specie |
| `Avgi`, `Remnant`, `Quarg`, `Arach`, `Saryd`, `Kimek`, `Bunrodean`, `Gegno`, `Scin`, `Aberrant`, `Heliarch` | invariati | 6/5/1/9/5/3/1/2/2/2/2 | specie e fazioni |
| `Coalition` | Coalizione | 4 → 4 | decisione L2 |
| `Syndicate` | Sindacato | 1 → 1 | convenzione L1 |
| `Republic` | Repubblica | 2 → 2 | — |
| `Ember Waste`, `Tangled Shroud` | invariati | 1 / 1 | nomi di regione |
| `the Incursion` | l'Incursione | 1 → 1 | convenzione L2 |
| `Remembrance Day`, `Alpha Wars` | invariati | 2 / 1 | convenzioni L1 |
| `Earth` | Terra | 5 → 5 | eccezione deliberata |
| `Hot Jupiters` | "gioviani caldi" | 1 → 1 | termine astronomico italiano, virgolette conservate |
| `skyhook` | invariato | 1 → 1 | come in L5 |
| `spaceport` | spazioporto | 25 → 23 | unità 10 "spaceport settlement" → "insediamento portuale"; unità 30 con pronome |
| `landing pad` | piazzola di atterraggio | 2 → 3 | unità 42: "piazzole di atterraggio" + "un metro di piazzola" |

Nomi astronomici reali adattati come in L3: `Enceladus` → Encelado, `Mercury` → Mercurio,
`Neptune` → Nettuno. `Sol` resta invariato (nome del sistema).

---

## 3. Interventi fatti in stesura e rilettura

| # | Prima | Dopo | Perché |
|---|---|---|---|
| 4 | "apparentemente incurante della tua presenza; le uniche persone che incrociano il tuo sguardo sono i tuoi simili" | "quasi non esistessi; solo i tuoi simili, visitatori con gli occhi sgranati, incrociano il tuo sguardo" | rapporto 1,42: la frase breve non reggeva l'espansione |
| 7 | "Per il resto un mondo roccioso qualunque" | invariato dopo verifica | *otherwise mundane* reso senza calchi |
| 10 | "le torri formano un paesaggio" | "i torrioni formano un paesaggio" | evita la ripetizione di "torri" nello stesso periodo |
| 37 | "una gruppo di cadetti" | "un gruppo di cadetti" | errore di accordo |
| 48 | "trasmette in loop" | "trasmette in ciclo" | anglicismo |
| 52 | "il gergo locale incorpora minacce" | invariato | resa letterale ma naturale |
| 68 | "un solo piccolo fornitore" | invariato dopo verifica | *outfitter* → fornitore, glossario |
| 84 | "dai Builders" | "dai Costruttori" | vedi §4: epiteto tradotto, non nome proprio |

---

## 4. Incoerenze e decisioni aperte (non bloccanti)

1. **`the Builders` → Costruttori** (1): è l'unico caso in cui ho tradotto un epiteto di specie invece di
   lasciarlo invariato. Se si preferisce l'invariato "Builders", va cambiato qui e in ogni occorrenza
   futura (i droni `Ka'sei` restano invariati).
2. **`Paradise Worlds` → Mondi Paradisiaci** (1): coerenza con `Paradise World` → Mondo Paradisiaco, ma la
   voce è ancora "da ratificare" nel checkpoint §7.
3. **`Confederated Councils` invariato** (1): nome di Stato; se in altri file compare come "Consigli
   Confederati", va uniformato.
4. **`skyhook` invariato** (1): confermata la scelta di L5.
5. Restano aperte: `Successors`, `Antecessors`, `caveau`, `ringroide`, `Starlit University`, `longcows`,
   `Key Stones` → Pietre Chiave, `il Rim` / `the Deep`.

---

## 5. Esito dei controlli

```
unità 84 · mancanti 0 · estranei 0 · vuote 0 · duplicati IT 0 · duplicati EN 0
parole 4586 -> 4564 · ratio 0.85-1.27
tab 30 (tutti gli iniziali conservati) · virgolette 10 · token <...> 0
riga grezza identica al file: 84/84 · english/kind/path/state identici al DB: 84/84
tipografia: 0 accenti sostitutivi, 0 ellissi, 0 caporali, 0 em dash, 0 apostrofi curvi
parole inglesi residue: nessuna · anglicismi evitabili: nessuno
problemi 0
```

Un errore trovato dal controllo: unità 4, rapporto 1,42 (soglia 1,40), corretto a 1,03.

**Non verificato:** rendering in gioco (nessun avvio, come da mandato).
