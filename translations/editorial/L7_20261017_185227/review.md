# L7 — Revisione editoriale del blocco `data/map planets.txt` 733–1077

84 descrizioni, 4.452 parole inglesi → 4.385 italiane. Terzo lotto del tratto iniziale del file, nessun
ID in comune con L1–L6. Inizia con `planet:Bunthro` e si chiude a fine pianeta con `planet:Cyife`
(riga 1077); l'unità successiva (riga 1082) apre Cyreal.

---

## 1. Metodo

Stesso impianto dei lotti precedenti: contesto letto per pianeta, glossario e checkpoint consultati prima
di ogni scelta, traduzione in quattro gruppi nell'ordine del file (1–21, 22–42, 43–63, 64–84), rilettura
del solo italiano.

Le 84 unità sono state esportate da `state.db` (tutte `PENDING`, tutte `DESCRIPTION`); `raw` coincide con
la riga del sorgente per tutte e 84 (verificato in `verify.py`).

---

## 2. Convenzioni applicate

| Termine | Resa | Occorrenze EN → IT | Note |
|---|---|---:|---|
| `Remnant` | invariato | 2 → 2 | fazione, come L1–L6 |
| `the Alphas` | invariato | 1 → 1 | convenzione L3 |
| `the Waste` | "il Waste" | 1 → 1 | forma breve di `Ember Waste`, invariato |
| `the Deep` | invariato | 1 → 1 | nome di regione |
| `Dirt Belt` | invariato | 2 → 2 | — |
| `the Rim` | "il Rim" | 1 → 1 | unità 39, maiuscola = regione |
| `Paradise Worlds` | Mondi Paradisiaci | 1 → 1 | plurale di `Paradise World` (§7 checkpoint) |
| `Coalition` | Coalizione | 3 → 3 | decisione L2 |
| `Syndicate` | Sindacato | 3 → 3 | convenzione L1 |
| `Republic` | Repubblica | 1 → 1 | — |
| `Earth` | Terra | 3 → 3 | eccezione deliberata |
| `High Houses` / `New Houses` | Alte Casate / Nuove Casate | 1 / 1 | convenzione L3d |
| `Successors`, `Unfettered`, `Hai`, `Quarg`, `Heliarch`, `Arach`, `Saryd`, `Kimek`, `Gegno Scin`, `Bunrodea` | invariati | 1/1/4/3/1/1/6/3/1/2 | specie e fazioni |
| `Halite` | invariato | 1 → 1 | classe di nave Scin, trattata come nome proprio |
| `longcows` | bovini lunghi | 4 → 4 | convenzione L3d |
| `jump drives` | motori di salto | 1 → 1 | `hyperdrive` → iperpropulsore |
| `hyperdrive` / `hyperspace` | iperpropulsore / iperspazio | 1 / 4 | glossario |
| `terraforming` | terraformazione | 4 → 4 | — |
| `wormholes` | wormhole | 1 → 1 | invariato, convenzione L3 |
| `Remembrance Day`, `Alpha Wars` | invariati | 1 / 1 | convenzioni L1 |
| `landing pad` | piazzola di atterraggio | 5 → 5 | — |

Nomi di pianeti, stazioni e stelle restano invariati: Bunthro, Burthen, Byruca, Caelian, Calda, Calesi,
Pelesi, Canyon, Capitoline, Carbuncle, Cassandra, Cavaasa-Vasa-Tej, Kasii-Cavaasa, Soar, Ceaseless Toil,
Ceilia'sei, Celeatis, Celestial Third, Charon, Charybdis, Chiron, New Sydney, Chosen Nexus,
Chyyra-Raaqa-Tuur, Cipi, Zug, Clark, Clink, Cloudfire, Cold Horizon, Cool Forest, Diligent Hand,
Cornucopia, Corral of Meblumem, Covert, Crataegusa, Crossroads, Cyife, Algorel, Delve, Vail.

---

## 3. Interventi fatti in stesura e rilettura

| # | Intervento | Perché |
|---|---|---|
| 31 | `Cavasaa-Vasa-Tej` (grafia del sorgente, 1 volta) → **Cavaasa-Vasa-Tej** | refuso nel sorgente: il pianeta è `Cavaasa-…` nel nome del nodo e nell'unità 30. Segnalato, non propagato |
| 38 | `southern galactic rim` → "margine meridionale della galassia" | minuscola = descrizione geografica generica, non la regione `the Rim` |
| 39 | `worlds farther up the Rim` → "i mondi più su lungo il Rim" | qui la maiuscola indica la regione: resa con l'invariato |
| 52 | "probabilmente per ricavare materiali da usare nella costruzione" → "forse per i materiali" | rapporto 1,35: periodo troppo dilatato rispetto all'originale (ora 1,15) |
| 57 | `startup-world attitude` → "mentalità da mondo agli inizi" | evita l'anglicismo "startup" |
| 79 | `linear shear cloud lines` → "linee nuvolose di taglio disposte in modo lineare" | termine meteorologico reso per esteso |
| 27 | `In the late 2300s` → "Alla fine del XXIV secolo" | in inglese "the 2300s" con *late* indica l'epoca, non il decennio; il gioco data gli eventi per anno |
| 5 | "The locals - exceptionally strong and short -" → incisi con virgole | em dash vietato (§3 regola 6) |
| 14 | `a pleasant place to unwind` → "un luogo piacevole dove rilassarsi" | evita il calco "un posto dove staccare" |
| 75 | `primal forests` → "foreste primigenie" | resa corrente in italiano |
| 40 | `scrupulosity` → "scrupolosità" | — |
| 45 | `de-facto leader` → "di fatto il punto di riferimento" | evita il latinismo anglicizzato |

---

## 4. Incoerenze e decisioni aperte (non bloccanti)

1. **`Halite` invariato** (1): è una classe di nave Scin. Se in altri file compare come nome comune
   ("alite"), va uniformato.
2. **`Bunrodean`** (2): invariato al singolare e al plurale ("i Bunrodean"), come da §7 punto 5 ancora
   aperto; qui non ci sono occorrenze al plurale morfologico che obblighino a scegliere.
3. **`Cavasaa-Vasa-Tej`** (1): refuso del sorgente, corretto. Se il refuso compare in altri file, la
   correzione va replicata coerentemente.
4. **`Paradise Worlds` → Mondi Paradisiaci** (1): coerente con la voce "Mondo Paradisiaco", ancora da
   ratificare (§7 punto 3).
5. Restano aperte: `Successors`, `Antecessors`, `caveau`, `ringroide`, `Starlit University`, `Costruttori`,
   `Key Stones`, `skyhook`, `il Rim` / `the Deep`.

---

## 5. Esito dei controlli

```
unità 84 · mancanti 0 · estranei 0 · vuote 0 · duplicati IT 0 · duplicati EN 0
parole 4452 -> 4385 · ratio 0.88-1.24
tab 32 (tutti gli iniziali conservati) · virgolette 0 · token <...> 0
riga grezza identica al file: 84/84 · english/kind/path/state identici al DB: 84/84
tipografia: 0 accenti sostitutivi, 0 ellissi, 0 caporali, 0 em dash, 0 apostrofi curvi
parole inglesi residue: nessuna · anglicismi evitabili: nessuno
problemi 0
```

Nessun errore rilevato dai controlli al primo passaggio; un intervento volontario sull'unità 52
(rapporto 1,35, entro soglia ma troppo dilatato) l'ha portato a 1,15.

**Non verificato:** rendering in gioco (nessun avvio, come da mandato).
