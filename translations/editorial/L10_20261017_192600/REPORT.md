# L10 — Sesto lotto del tratto iniziale di `data/map planets.txt`

**Data:** 2026-10-17 · **Esito: lotto completo, 81/81 unità, 0 omissioni**
**Directory:** `endless-sky-l10n/staging/editorial/L10_20261017_192600/`

---

## 1. Blocco tradotto

| Voce | Valore |
|---|---|
| File | `data/map planets.txt` |
| Intervallo | righe **1826–2163** |
| Posizione | sesto tratto del settore iniziale (1826–3845) |
| Unità | **81** (`DESCRIPTION`, tutte `PENDING`) |
| Parole | **4.549** inglesi → **4.567** italiane |
| Rapporto | 0,94 – 1,24 |
| Pianeti | **30** (da **Featherweight** a **Giaru Gegno**) |
| Tab di paragrafo | 30 |
| Virgolette | 12 (6 coppie: unità 40 ×2, 41, 53, 54, 55) |
| Token `<...>` | 0 |

Confine pulito: l'ultima unità (riga 2163) chiude Giaru Gegno; la successiva (riga 2171) apre Giiq-Oj-Sol,
e tra le due righe non esistono unità.

**Dopo L10** restano **379 unità / 20.816 parole** nel tratto iniziale (righe 2171–3845).

---

## 2. Esempi rappresentativi

**Unità 9 — `planet:Feo Platform`**

> Hastily assembled from the parts of a mothballed interstellar laser driver, the Feo Platform is an
> enormous free electron laser intended to provide fire support to Avgi fleets defending the Tangled Shroud
> from Aberrant invasion.

> Montata in fretta con i pezzi di un acceleratore laser interstellare messo fuori servizio, la Piattaforma
> Feo è un enorme laser a elettroni liberi pensato per fornire fuoco di appoggio alle flotte Avgi che
> difendono il Tangled Shroud dall'invasione degli Aberrant.

**Unità 40 — `planet:Freedom`**

> A sign above the entrance to the spaceport bar reads, "Fine home-brewed whiskey! Get smashed without
> getting taxed!" Further down the street, a sign over what appears to be a real estate office reads, "Why
> not settle where The Man can't reach you?"

> Un cartello sopra l'ingresso del bar dello spazioporto dice: "Whisky fatto in casa, ottimo! Ubriacati
> senza pagare le tasse!" Più avanti nella strada, un cartello sopra quella che sembra un'agenzia
> immobiliare dice: "Perché non stabilirsi dove il Sistema non può raggiungerti?"

**Unità 47 — `planet:Gagarin`** *(l'unità corretta dal controllo)*

> Gagarin is the most populous planet in what used to be the Confederated Councils of the Outer Rim, and it
> was one of the first colonies established in this region.

> Gagarin è il pianeta più popoloso di quello che un tempo erano i Consigli Confederati del Bordo Esterno
> (CCOR), e fu una delle prime colonie fondate in questa regione.

**Unità 53 — `planet:Garden Empyreal`**

> Arrays of gigantic metal pyramids lay at every angle, each nearly a dozen times larger than the average
> space station. Spread out over the planet's upper atmosphere, these so-called "hubs" are connected by
> long, inextensible, and extremely sturdy wires, ensuring no part of the structure is destabilized.

> Schiere di gigantesche piramidi metalliche giacciono a ogni angolazione, ciascuna quasi una dozzina di
> volte più grande della stazione spaziale media. Distribuite sull'atmosfera superiore del pianeta, questi
> cosiddetti "hub" sono collegati da funi lunghe, inestensibili ed estremamente robuste, che assicurano che
> nessuna parte della struttura si destabilizzi.

**Unità 62 — `planet:Gemstone`**

> Mining a tectonically active world is an insane project. Earthquakes cause frequent cave-ins, but the
> potential for riches draws miners here despite high mortality rates.

> Estrarre in un mondo tettonicamente attivo è un progetto da pazzi. I terremoti causano frequenti crolli,
> ma il potenziale di ricchezza attira qui i minatori nonostante l'alto tasso di mortalità.

**Unità 81 — `planet:Giaru Gegno`**

> There are probably many hundreds of billions of Quarg on this ring, and yet it still manages to feel
> spacious and lightly populated.

> Su questo anello ci sono probabilmente molte centinaia di miliardi di Quarg, e tuttavia riesce ancora a
> sembrare spazioso e scarsamente popolato.

---

## 3. Il controllo ha trovato un errore

**Unità 47: parola inglese residua `the`.** Il nome dello Stato
`the Confederated Councils of the Outer Rim` era rimasto invariato, ma in italiano lasciava in evidenza
l'articolo inglese. Sciolto in **Consigli Confederati del Bordo Esterno (CCOR)**, con l'acronimo
invariato nelle tre occorrenze in cui ricorre (unità 47, 48, 49).

Conseguenza da ratificare: **in L6 la forma breve `Confederated Councils` era stata lasciata invariata**.
La correzione retroattiva di L6 non è stata fatta (il mandato vieta di riscrivere il corpus chiuso);
le due scelte convivono e sono annotate in `review.md` §5 punto 1 e nel checkpoint.

Corretto il FAIL, `check.py` passa a `FAIL totale: 0` senza altre modifiche.

---

## 4. Interventi editoriali

Dieci interventi in stesura e rilettura (dettaglio in `review.md` §4), oltre alla correzione imposta dal
controllo.

| Termine | Resa | Occorrenze |
|---|---|---|
| `Confederated Councils of the Outer Rim` | Consigli Confederati del Bordo Esterno (CCOR) | 1 (nome sciolto) |
| `CCOR` (acronimo) | invariato | 3 |
| `Syndicated Shipyards` | invariato | 1 |
| `Paradise Planets` | Pianeti Paradisiaci | 1 |
| `Aberrations` | "Aberrant" (invariato) | 1 |
| `Antecessors` | invariato | 2 |
| `ringworld(s)` | mondo/mondi ad anello | 4 |
| `The Man` | "il Sistema" | 1 |

Rese notevoli: `mothballed` → "messo fuori servizio"; `free electron laser` → "laser a elettroni liberi";
`dry docks` → "bacini di carenaggio"; `extremophiles` → "estremofili"; `invertebrate multicellular
creatures` → "invertebrati pluricellulari"; `terrace gardens` → "giardini a terrazze"; `hand-glazed
pottery` → "ceramiche smaltate a mano"; `helical pattern` → "motivo elicoidale"; `slum world` →
"mondo-baraccopoli"; `mess hall` → "mensa"; `paid on commission` → "pagata a cottimo"; `guard rails` →
"guardrail"; `hydrological cycle` → "ciclo idrologico"; `dormant state` → "stato di quiescenza";
`axial tilt` → "inclinazione assiale".

---

## 5. Decisioni ancora aperte

1. **`Consigli Confederati` vs L6 invariato**: allineare L6 o accettare la differenza.
2. **`Syndicated Shipyards` invariato** (1): ragione sociale.
3. **`Aberrations` → "Aberrant"** (1): alternativa "Aberrazioni" per gli individui.
4. **`Paradise Planets` → Pianeti Paradisiaci** (1): in attesa di ratifica (§7 punto 3).
5. Restano aperte: `Successors`, `Antecessors`, `Consonance`, `caveau`, `ringroide`, `Starlit University`,
   `Costruttori`, `Key Stones`, `skyhook`, `il Rim`, `il Nucleo`, `Halite`, `Bulk Freighter`,
   `Twilight Guard`, `Egemonia Bunrodean`.

---

## 6. Controlli

| Controllo | Esito |
|---|---|
| Indici: 81 attesi, 81 presenti, 0 mancanti, 0 estranei | OK |
| ID univoci, allineati a `source.json` | OK |
| `raw` identica alla riga del file (81/81) | OK |
| `english`/`kind`/`path`/`state` identici al DB (81/81) | OK |
| Traduzioni vuote / duplicati EN e IT | 0 |
| Tab: totale invariato (30) e tab iniziale conservato unità per unità | OK |
| Virgolette: stesso conteggio per unità (12) | OK |
| Token `<...>`: multinsiemi identici (0) | OK |
| Spazi doppi / ai bordi / newline interne | OK |
| Rapporto di lunghezza 0,94–1,24 | OK |
| Tipografia: accenti sostitutivi, ellissi tipografiche, caporali, em dash, apostrofi curvi | 0 |
| Parole inglesi residue / anglicismi evitabili | **1 → 0** / 0 |

`check.py`: `FAIL totale: 1` al primo passaggio (unità 47, `the`), **`FAIL totale: 0`** dopo la correzione.

---

## 7. Integrità

| Voce | Atteso | Osservato | Esito |
|---|---|---|---|
| `endless-sky` HEAD / modifiche | `b4aa3bac3` / 0 | identico / 0 | OK |
| `state.db` | 364 / 32.560, nessuna scrittura | `9125282973ddc8b9`, ultimo evento `14:33:18Z` | OK |
| Batch · glossario · inventario · `tools/l10n.py` · output approvati | invariati | hash invariati | OK |
| L1–L9 | intatti | hash invariati | OK |
| Build / test / packaging | non eseguiti | non eseguiti | OK |

---

## 8. Artefatti

```
endless-sky-l10n/staging/editorial/L10_20261017_192600/
├── source.json       81 unità (idx, id, riga, contesto, inglese, delimitatore, tab, riga grezza, hash)
├── translation.json  81 unità (idx, id, riga, contesto, inglese, italiano, ratio)
├── review.md         convenzioni, 10 interventi, il FAIL e la sua correzione, incoerenze aperte
├── REPORT.md         questo report
├── parts/            part01 (1–21), part02 (22–41), part03 (42–61), part04 (62–81)
└── check.py, verify.py
```

---

## 9. Cosa non è stato fatto

- Nessuna applicazione al gioco, nessun batch, nessuna build, nessun packaging.
- Nessuna modifica a `state.db`, glossario, inventario, output approvati, sorgenti o dati.
- **Rendering non verificato** (nessun avvio del gioco, come da mandato).
- Le 81 unità sono **tradotte in staging e restano `PENDING`**.

**Totale editoriale complessivo: 1.165 unità · 62.871 parole inglesi → 62.428 italiane.**
