# L11 — Revisione editoriale del blocco `data/map planets.txt` 2171–2551

80 descrizioni, 4.597 parole inglesi → 4.629 italiane. Settimo lotto del tratto iniziale del file, nessun
ID in comune con L1–L10. Inizia con `planet:Giiq-Oj-Sol` e si chiude a fine pianeta con `planet:Hermes`
(riga 2551); tra la riga 2551 e la 2555 non esistono unità, e la 2555 apre Hespair.

---

## 1. Metodo

Stesso impianto dei lotti precedenti: contesto letto per pianeta, glossario e checkpoint consultati prima
di ogni scelta, traduzione in quattro gruppi nell'ordine del file (1–20, 21–40, 41–60, 61–80), rilettura
del solo italiano.

Le 80 unità sono state esportate da `state.db` (tutte `PENDING`, tutte `DESCRIPTION`); `raw` coincide con
la riga del sorgente per tutte e 80 (verificato in `verify.py`).

---

## 2. Convenzioni applicate

| Termine | Resa | Occorrenze EN → IT | Note |
|---|---|---:|---|
| `Hai` | invariato | 19 → 19 | la ventesima occorrenza del conteggio è il verbo italiano *hai* (unità 28) |
| `Quarg` / `Saryd` / `Kimek` / `Gegno` / `Scin` / `Vi` / `Korath` | invariati | 7/4/1/3/4/1/3 | specie |
| `Heliarch(s)` | invariato | 2 → 2 | — |
| `Coalition` | Coalizione | 5 → 5 | — |
| `Syndicate` / `Syndicated Systems` / `Syndicated Shipyards` | Sindacato / **invariato** / **invariato** | 5 → 5 | le due ragioni sociali restano invariate, come in L10 |
| `Republic` | Repubblica | 1 → 1 | — |
| `House Chamgar` | Casata Chamgar | 2 → 2 | `house X` → Casata X (`House Chamgar` ×2) |
| `Paradise Planet` | Pianeta Paradisiaco | 1 → 1 | — |
| `Alpha Wars`, `the Deep`, `wormhole`, `Bulk Freighter` | invariati | 1 / 1 / 1 / 1 | convenzioni consolidate |
| `dry dock` | bacino di carenaggio | 1 → 1 | — |
| `outfits` | equipaggiamenti | 4 → 5 | l'italiano richiede l'articolo in un caso in più |
| `terraforming` / `terraformed` | terraformazione / terraformato | 5 → 3 + 2 | 3 sostantivi, 2 participi: la regex conta solo il sostantivo |
| `Terrestrial` | "sulla Terra" | — | unità 20: `terrestrial aged care facilities` → "struttura per anziani sulla Terra" (esplicitazione) |

Nomi propri invariati: Giiq-Oj-Sol, Giiq-Sou-Kella, Giverstone, Glaze, Gliese, Glittering Ice, Glory,
Goldcrawl, Graede, Grakhord, Greenbloom, Greenrock, Greenview, Greenwater, Gresku Fodar, Greymoon,
Guardian Array Sapphire, Gue Faur, Hai-home, Haimat, Hammer of Debrugt, Harmony, Haven, Haze, Heartland,
Heartvalley, Heavenly Halls, Helheim, Hephaestus, Hermes.

Istituzioni e ragioni sociali:

| Nome | Trattamento |
|---|---|
| `Academy of Planetary Sciences` | **invariato** (come `Starlit University`) |
| `Hei Low Io species preservation foundation` | nome proprio invariato + "fondazione per la conservazione delle specie" |
| `Far Loo Bah fuel collection corporation` | nome proprio invariato + "società di raccolta di carburante" |
| `Syndicated Systems`, `Syndicated Shipyards` | **invariati** (ragioni sociali) |
| `"Checkpoint of Ablodab"` | **invariato** (soprannome tra virgolette) |

---

## 3. Interventi fatti in stesura e rilettura

| # | Intervento | Perché |
|---|---|---|
| 1 | `stepping outside of one's ship ... a very bad idea` → "rende pessima l'idea di uscire dalla nave" | più naturale del calco "un'idea molto cattiva" |
| 7 | `"canyon people"` → "gente dei canyon", virgolette conservate | — |
| 10 | `a shine of magenta emanates` → "emana un bagliore magenta" | soggetto invertito, l'italiano non regge il calco |
| 14 | `"boughten sunshine"` → "sole comprato" | resa dell'arcaismo inglese con un calco trasparente, virgolette conservate |
| 24 | `you feel like a young child lost among a crowd` → "ti senti come un bambino perso tra una folla" | — |
| 30 | `infographic proclaims` → "un pannello informativo proclama" | — |
| 32 | `mezzanine` → "soppalco" | termine architettonico corrente |
| 42 | `store frontage` → "vetrine" | — |
| 46 | `turnover capabilities` → "capacità di smaltimento" | senso: capacità di smaltire i turni di riparazione |
| 62 | `monorail trams` → "tram monorotaia" | — |
| 66 | `chaser bins` → "rimorchi di raccolta" | termine agricolo: rimorchi che affiancano la mietitrebbia |
| 73 | `hermetically sealed parks` → "parchi sigillati ermeticamente" | — |
| 80 | `sterilize them` → "sterilizzarle" | — |

Nessun errore imposto dai controlli: `check.py` passa con `FAIL totale: 0` al primo tentativo.

---

## 4. Incoerenze e decisioni aperte (non bloccanti)

1. **`Academy of Planetary Sciences` invariato** (1): coerente con `Starlit University`, ma la lista di
   istituzioni lasciate in inglese si allunga (`Starlit University`, `Royal University of Dogen`,
   `Military Academy of Fuhtiiski`, questa). Conviene ratificare una volta per tutte.
2. **`Syndicated Systems` / `Syndicated Shipyards`** invariati (1 + 1): ragioni sociali. Se si traduce
   "Sindacato", cambiano L10 e L11.
3. **`"boughten sunshine"` → "sole comprato"**: l'inglese usa un arcaismo dialettale; l'italiano lo rende
   con un calco trasparente, non con un equivalente regionale.
4. **`terrestrial` → "sulla Terra"** (unità 20): esplicitazione del riferimento; l'originale è più vago
   ("strutture per anziani terrestri").
5. Restano aperte: `Successors`, `Antecessors`, `Consonance`, `Consigli Confederati` vs L6, `caveau`,
   `ringroide`, `Halite`, `Bulk Freighter`, `Costruttori`, `Key Stones`, `skyhook`, `il Rim`, `il Nucleo`,
   `Twilight Guard`, `Egemonia Bunrodean`.

---

## 5. Esito dei controlli

```
unità 80 · mancanti 0 · estranei 0 · vuote 0 · duplicati IT 0 · duplicati EN 0
parole 4597 -> 4629 · ratio 0.90-1.22
tab 24 (tutti gli iniziali conservati) · virgolette 20 (10 coppie) · token <...> 0
riga grezza identica al file: 80/80 · english/kind/path/state identici al DB: 80/80
tipografia: 0 accenti sostitutivi, 0 ellissi tipografiche, 0 caporali, 0 em dash, 0 apostrofi curvi
parole inglesi residue: nessuna · anglicismi evitabili: nessuno
problemi 0
```

Le coppie di unità 2/3 (stesso pianeta, stesso incipit) e 33/34 (stesso pianeta) hanno inglese diverso e
traduzioni distinte: il controllo duplicati resta a 0.

**Non verificato:** rendering in gioco (nessun avvio, come da mandato).
