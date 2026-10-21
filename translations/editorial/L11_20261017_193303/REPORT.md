# L11 — Settimo lotto del tratto iniziale di `data/map planets.txt`

**Data:** 2026-10-17 · **Esito: lotto completo, 80/80 unità, 0 omissioni**
**Directory:** `endless-sky-l10n/staging/editorial/L11_20261017_193303/`

---

## 1. Blocco tradotto

| Voce | Valore |
|---|---|
| File | `data/map planets.txt` |
| Intervallo | righe **2171–2551** |
| Posizione | settimo tratto del settore iniziale (2171–3845) |
| Unità | **80** (`DESCRIPTION`, tutte `PENDING`) |
| Parole | **4.597** inglesi → **4.629** italiane |
| Rapporto | 0,90 – 1,22 |
| Pianeti | **29** (da **Giiq-Oj-Sol** a **Hermes**) |
| Tab di paragrafo | 24 |
| Virgolette | 20 (10 coppie) |
| Token `<...>` | 0 |

Confine pulito: l'ultima unità (riga 2551) chiude Hermes; tra la 2551 e la 2555 non esistono unità e la
2555 apre Hespair.

**Dopo L11** restano **299 unità / 16.219 parole** nel tratto iniziale (righe 2555–3845).

---

## 2. Esempi rappresentativi

**Unità 1 — `planet:Giiq-Oj-Sol`**

> The specific atmosphere of this planet combined with its volcanic activity have combined to make the
> perfect conditions for the geological production of strands of natural glass, which are thrown into the
> atmosphere by volcanoes and then carried by high winds all over the planet.

> L'atmosfera particolare di questo pianeta, unita alla sua attività vulcanica, ha creato le condizioni
> perfette per la produzione geologica di filamenti di vetro naturale, che i vulcani lanciano nell'atmosfera
> e che i venti forti poi trasportano su tutto il pianeta.

**Unità 14 — `planet:Glory`**

> Elsewhere in the galaxy, people speak dismissively of the "boughten sunshine" that rich terraformed worlds
> can afford. On Glory, even many of the lakes and hills are artificial, crafted to garden-like perfection.

> Altrove nella galassia la gente parla con sufficienza del "sole comprato" che i mondi terraformati ricchi
> possono permettersi. Su Glory perfino molti dei laghi e delle colline sono artificiali, modellati fino a
> una perfezione da giardino.

**Unità 24 — `planet:Grakhord`**

> Here, you feel like a young child lost among a crowd of tall, indifferent adults. The average adult Quarg
> is over three meters tall, and although they move slowly and gracefully, on their long legs they easily
> speed by you.

> Qui ti senti come un bambino perso tra una folla di adulti alti e indifferenti. Il Quarg adulto medio
> supera i tre metri di altezza e, benché si muovano piano e con grazia, sulle loro lunghe gambe ti superano
> facilmente.

**Unità 43 — `planet:Guardian Array Sapphire`**

> More commonly referred to as "Checkpoint of Ablodab," this enormous station was built shortly after the
> end of the Coalition's war against the Quarg, meant to serve as a regional dry dock and supply base that
> damaged combat ships could return to after some time at the front lines.

> Più comunemente chiamata "Checkpoint of Ablodab", questa enorme stazione fu costruita poco dopo la fine
> della guerra della Coalizione contro i Quarg, pensata come bacino di carenaggio e base di rifornimento
> regionale a cui le navi da combattimento danneggiate potessero tornare dopo un po' di tempo in prima linea.

**Unità 66 — `planet:Heartland`**

> There are tractors with rubber wheels, spiked wheels, and tracks; with plows, combines, balers, and chaser
> bins; tractors barely big enough to sit on and tractors the size of a small freighter. It's somewhat
> overwhelming.

> Ci sono trattori con ruote di gomma, ruote a spuntoni e cingoli; con aratri, mietitrebbie, imballatrici e
> rimorchi di raccolta; trattori appena grandi abbastanza per sedercisi e trattori delle dimensioni di un
> piccolo mercantile. È un po' travolgente.

**Unità 80 — `planet:Hermes`**

> Industrial strength ultraviolet lasers are mounted on turrets throughout the atrium, and fire
> automatically at entering and departing ships to sterilize them.

> Laser ultravioletti di potenza industriale sono montati su torrette lungo tutto l'atrio e sparano
> automaticamente contro le navi in arrivo e in partenza per sterilizzarle.

---

## 3. Interventi editoriali

Tredici interventi in stesura e rilettura (dettaglio in `review.md` §3). **Nessun errore imposto dai
controlli**: il lotto passa con `FAIL totale: 0` al primo tentativo.

| Nome | Trattamento |
|---|---|
| `Academy of Planetary Sciences` | invariato |
| `Syndicated Systems`, `Syndicated Shipyards` | invariati (ragioni sociali) |
| `House Chamgar` | Casata Chamgar (2) |
| `Paradise Planet` | Pianeta Paradisiaco (1) |
| `Hei Low Io ... foundation`, `Far Loo Bah ... corporation` | nome proprio invariato + descrizione tradotta |
| `"Checkpoint of Ablodab"` | invariato, virgolette conservate |

Rese notevoli: `strands of natural glass` → "filamenti di vetro naturale"; `offgassing waves` →
"onde che rilasciano gas"; `marsupials` → "marsupiali"; `receptionist` → "receptionist"; `vending
machines` → "distributori automatici"; `aged care facilities` → "struttura per anziani"; `bacterial
sludge` → "fango batterico"; `chaser bins` → "rimorchi di raccolta"; `monorail trams` → "tram monorotaia";
`cantilevered platforms` → "piattaforme a sbalzo"; `horse-drawn buggies` → "carrozze trainati da cavalli";
`rivet guns` → "rivettatrici".

---

## 4. Decisioni ancora aperte

1. **Istituzioni lasciate in inglese**: `Academy of Planetary Sciences` si aggiunge a `Starlit University`,
   `Royal University of Dogen`, `Military Academy of Fuhtiiski`. Da ratificare in blocco.
2. **`Syndicated Systems` / `Syndicated Shipyards`** invariati: se si traduce "Sindacato", cambiano due lotti.
3. **`"boughten sunshine"` → "sole comprato"**: calco trasparente, non equivalente regionale.
4. **`terrestrial` → "sulla Terra"** (1): esplicitazione del riferimento.
5. Restano aperte: `Successors`, `Antecessors`, `Consonance`, `Consigli Confederati` (L10) vs `Confederated
   Councils` invariato (L6), `caveau`, `ringroide`, `Halite`, `Bulk Freighter`, `Costruttori`,
   `Key Stones`, `skyhook`, `il Rim`, `il Nucleo`, `Twilight Guard`, `Egemonia Bunrodean`.

---

## 5. Controlli

| Controllo | Esito |
|---|---|
| Indici: 80 attesi, 80 presenti, 0 mancanti, 0 estranei | OK |
| ID univoci, allineati a `source.json` | OK |
| `raw` identica alla riga del file (80/80) | OK |
| `english`/`kind`/`path`/`state` identici al DB (80/80) | OK |
| Traduzioni vuote / duplicati EN e IT | 0 |
| Tab: totale invariato (24) e tab iniziale conservato unità per unità | OK |
| Virgolette: stesso conteggio per unità (20) | OK |
| Token `<...>`: multinsiemi identici (0) | OK |
| Spazi doppi / ai bordi / newline interne | OK |
| Rapporto di lunghezza 0,90–1,22 | OK |
| Tipografia: accenti sostitutivi, ellissi tipografiche, caporali, em dash, apostrofi curvi | 0 |
| Parole inglesi residue / anglicismi evitabili | 0 / 0 |

`check.py`: `FAIL totale: 0` al primo passaggio.

---

## 6. Integrità

| Voce | Atteso | Osservato | Esito |
|---|---|---|---|
| `endless-sky` HEAD / modifiche | `b4aa3bac3` / 0 | identico / 0 | OK |
| `state.db` | 364 / 32.560, nessuna scrittura | `9125282973ddc8b9`, ultimo evento `14:33:18Z` | OK |
| Batch · glossario · inventario · `tools/l10n.py` · output approvati | invariati | hash invariati | OK |
| L1–L10 | intatti | hash invariati | OK |
| Build / test / packaging | non eseguiti | non eseguiti | OK |

---

## 7. Artefatti

```
endless-sky-l10n/staging/editorial/L11_20261017_193303/
├── source.json       80 unità (idx, id, riga, contesto, inglese, delimitatore, tab, riga grezza, hash)
├── translation.json  80 unità (idx, id, riga, contesto, inglese, italiano, ratio)
├── review.md         convenzioni, 13 interventi, incoerenze aperte
├── REPORT.md         questo report
├── parts/            part01 (1–20), part02 (21–40), part03 (41–60), part04 (61–80)
└── check.py, verify.py
```

---

## 8. Cosa non è stato fatto

- Nessuna applicazione al gioco, nessun batch, nessuna build, nessun packaging.
- Nessuna modifica a `state.db`, glossario, inventario, output approvati, sorgenti o dati.
- **Rendering non verificato** (nessun avvio del gioco, come da mandato).
- Le 80 unità sono **tradotte in staging e restano `PENDING`**.

**Totale editoriale complessivo: 1.245 unità · 67.468 parole inglesi → 67.057 italiane.**
