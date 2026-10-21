# L4 — Ultimo lotto di `data/map planets.txt`

**Data:** 2026-10-17 · **Esito: lotto completo, 83/83 unità, 0 omissioni · FILE `map planets.txt` CHIUSO**
**Directory:** `endless-sky-l10n/staging/editorial/L4_20261017_182100/`

---

## 1. Blocco tradotto

| Voce | Valore |
|---|---|
| File | `data/map planets.txt` |
| Intervallo | righe **6383–6802** (ultima unità del file) |
| Continuità | inizia dopo L3d (ultima riga 6371, `planet:Varu K'est`) |
| Unità | **83** (`DESCRIPTION`, tutte `PENDING`) |
| Parole | **4.734** inglesi → **4.752** italiane |
| Rapporto | 0,93 – 1,28 |
| Pianeti | **39** (da **Varu K'prai** a **Zydee**) |
| Tab di paragrafo | 23 |
| Virgolette | 8 (unità 61, 81, 82) |
| Token `<...>` | 0 |

Il lotto assorbe anche la coda di 4 unità (6783–6802) che il checkpoint indicava separatamente: così la
parte di `map planets.txt` **dalla riga 3851 alla fine** è tradotta per intero, senza frammenti residui
dopo la riga 6802 (`verify.py`: 0 unità non tradotte oltre 6802).

**Correzione rispetto a una prima stesura di questo report:** il file **non** è completo. Delle 1544 unità
`PENDING` di `map planets.txt`, **673 sono tradotte** (righe 3851–6802) e **871 non sono mai state
affrontate** (righe 17–3845, 48.092 parole): sono anteriori al punto in cui L1 è cominciato e nessun lotto
le ha finora incluse. Restano il lavoro principale sul file.

**Confronto con i lotti precedenti:** 0 ID in comune con L1–L3d; 0 duplicati interni di inglese e di
italiano; nessuna unità già approvata.

---

## 2. Esempi rappresentativi

**Unità 5 — `planet:Varu Tek'kai`**

> Here, factories have been built to process the most dangerous and destructive of industrial chemicals.
> If disaster strikes one of the factories, the only result will be the contamination of a world that is
> already dead and lifeless - far better, in the judgment of the Wanderers, than allowing such risky
> industries to operate on a living world.

> Qui sono state costruite fabbriche per lavorare le sostanze chimiche industriali più pericolose e
> distruttive. Se un disastro colpisse una delle fabbriche, l'unico risultato sarebbe la contaminazione di
> un mondo già morto e senza vita: secondo il giudizio dei Wanderers, molto meglio che lasciare industrie
> così rischiose operare su un mondo vivo.

**Unità 16 — `planet:Viminal`**

> The continued Remnant presence here is due to the planet's Key Stones, which enable ships to travel
> through certain wormholes in the Ember Waste, and which the Remnant have not found on any other planet.

> La presenza continua dei Remnant qui è dovuta alle Pietre Chiave del pianeta, che permettono alle navi di
> attraversare certi wormhole nell'Ember Waste e che i Remnant non hanno trovato su nessun altro pianeta.

**Unità 38 — `planet:Warm Wind`**

> In place of trees, the village is full of trellised arches and spires; vines grow on the trellises, and
> moss grows on the vines, watered by the fog that sweeps up every evening from the rainforest below.

> Al posto degli alberi il villaggio è pieno di archi e guglie a pergolato; sulle pergole crescono viti,
> sulle viti cresce il muschio, innaffiato dalla nebbia che ogni sera sale dalla foresta pluviale
> sottostante.

**Unità 59 — `planet:Wyvern Station`**

> Wyvern Station was once one of the end destinations for the merchant caravans traveling along the Rim,
> back in the days before the Republic existed when most systems were not policed and the only way to
> avoid being plundered by pirates was for ships to travel in large convoys.

> La Stazione Wyvern era un tempo una delle destinazioni finali delle carovane mercantili che percorrevano
> il Rim, nei giorni in cui la Repubblica non esisteva ancora e la maggior parte dei sistemi non era
> sorvegliata, e l'unico modo per evitare di essere saccheggiati dai pirati era viaggiare in grandi
> convogli.

**Unità 77 — `planet:Zenith`**

> Because the land is owned by no government and anyone can build a dwelling without permission or
> paperwork as long as they are willing to fight off any other claimants, the total population of Zenith
> is unknown.

> Poiché la terra non appartiene a nessun governo e chiunque può costruire un'abitazione senza permessi né
> scartoffie, purché sia disposto a respingere qualsiasi altro aspirante, la popolazione totale di Zenith
> è sconosciuta.

**Unità 83 — `planet:Zydee`** (ultima del file)

> Although this moon initially seems barren and lifeless, there is evidence that the nearby Gegno Scin have
> recently attempted to set up an outpost here. Several partially-constructed buildings and landing zones
> are scattered about the surface, but none of them show any signs of activity, likely due to recent
> warfare with the Gegno Vi.

> Benché a prima vista questa luna sembri sterile e senza vita, ci sono prove che i vicini Gegno Scin
> abbiano recentemente tentato di impiantarvi un avamposto. Diversi edifici parzialmente costruiti e zone
> di atterraggio sono sparsi sulla superficie, ma nessuno mostra segni di attività, probabilmente a causa
> della recente guerra con i Gegno Vi.

---

## 3. Interventi editoriali

Sette interventi in stesura e rilettura (dettaglio in `review.md` §3): trattino lungo sostituito dai due
punti (unità 5); "bedrock" → "basamento roccioso"; "design più moderno" → "linea più moderna"; refuso
`Veiyue` del sorgente uniformato a `Veiuye` (nome del nodo); `Hot Jupiter` → "Giove caldo"; boilerplate
della stazione in disarmo allineato all'unità 21 di L3.

Convenzioni nuove introdotte in questo blocco:

| Termine | Resa | Occorrenze |
|---|---|---|
| `Key Stones` | Pietre Chiave | 1 |
| `defense prefects` | prefetti della difesa | 1 |
| `the Unfettered Hai` | gli Hai Unfettered | 1 |
| `gas dwarf` / `Hot Jupiter` | nano gassoso / Giove caldo | 1 / 2 |
| `House Seineq`, `Houses Aqrabe and Kaatrij` | Casata Seineq, Casate Aqrabe e Kaatrij | 2 |

Invariati: `Wanderers`, `Remnant`, `Aberrant`, `Tangled Shroud`, `Ember Waste`, `wormhole`,
`Alpha Wars`, `Gegno Scin`, `Gegno Vi`, `Tarazed Corporation`, `Southbound Shipyards`, `Ceaseless Toil`,
`Pherkad`, `Solace`, `Vinci`, `Wayfarer`, `Zydee`.

---

## 4. Decisioni ancora aperte

1. **`Key Stones` → Pietre Chiave** (1): se il nome dell'equipaggiamento viene localizzato altrove, deve
   coincidere; altrimenti resta "Key Stone".
2. **`Wanderers` invariato**: confermato da L3d.
3. Restano aperte: `Successors`, `Antecessors`, `caveau`, `ringroide`, `Starlit University`, `longcows`,
   `il Rim` / `the Deep`.

Nessuna è stata scritta nel glossario.

---

## 5. Controlli

| Controllo | Esito |
|---|---|
| Indici: 83 attesi, 83 presenti, 0 mancanti, 0 estranei | OK |
| ID univoci, allineati a `source.json` | OK |
| `raw` identica alla riga del file (83/83) | OK |
| `english`/`kind`/`path`/`state` identici al DB (83/83) | OK |
| Unità residue dopo la riga 6802 | **0** |
| Unità non tradotte nel file fuori dall'intervallo 3851–6802 | 871 (righe 17–3845, misurate) |
| Traduzioni vuote / duplicati EN e IT | 0 |
| Tab: totale invariato (23) e tab iniziale conservato unità per unità | OK |
| Virgolette: stesso conteggio per unità (8) | OK |
| Token `<...>`: multinsiemi identici (0) | OK |
| Spazi doppi / ai bordi / newline interne | OK |
| Rapporto di lunghezza 0,93–1,28 | OK |
| Tipografia: accenti sostitutivi, ellissi, caporali, em dash, apostrofi curvi | 0 |
| Parole inglesi residue / anglicismi evitabili | 0 / 0 |
| Coerenza inter-lotto su inglese ripetuto | stesso italiano per L4/21 = L3/21 |

`check.py`: `FAIL totale: 0` al primo passaggio.

---

## 6. Integrità

| Voce | Atteso | Osservato | Esito |
|---|---|---|---|
| `endless-sky` HEAD / modifiche | `b4aa3bac3` / 0 | identico / 0 | OK |
| `state.db` | 364 / 32.560, nessuna scrittura | `9125282973ddc8b9`, ultimo evento `14:33:18Z` | OK |
| Batch B001–B006 · glossario · inventario · `tools/l10n.py` | invariati | hash invariati | OK |
| Output approvati (3) | hash del checkpoint | invariati | OK |
| L1 · L2 · L3 · L3b · L3c · L3d | intatti | hash invariati | OK |
| Build / test / packaging | non eseguiti | non eseguiti | OK |

---

## 7. Artefatti

```
endless-sky-l10n/staging/editorial/L4_20261017_182100/
├── source.json       83 unità (idx, id, riga, contesto, inglese, delimitatore, tab, riga grezza, hash)
├── translation.json  83 unità (idx, id, riga, contesto, inglese, italiano, ratio)
├── review.md         convenzioni, 7 interventi, incoerenze aperte
├── REPORT.md         questo report
├── parts/            part01 (1–21), part02 (22–42), part03 (43–63), part04 (64–83)
└── check.py, verify.py
```

---

## 8. Cosa non è stato fatto

- Nessuna applicazione al gioco, nessun batch, nessuna build, nessun packaging.
- Nessuna modifica a `state.db`, glossario, inventario, output approvati, sorgenti o dati.
- **Rendering non verificato** (nessun avvio del gioco, come da mandato).
- Le 83 unità sono **tradotte in staging e restano `PENDING`**.

**Totale editoriale complessivo: 673 unità · 35.595 parole inglesi → 35.388 italiane**
(L1 120 + L2 101 + lotto L3 369 + L4 83).
