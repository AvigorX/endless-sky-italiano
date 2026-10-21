# L3 — Terzo blocco editoriale (prima sezione)

**Data:** 2026-10-17 · **Esito: sezione completa, 79/79 unità, 0 omissioni**
**Directory:** `endless-sky-l10n/staging/editorial/L3_20261017_180114/`

---

## 1. Blocco tradotto

| Voce | Valore |
|---|---|
| File | `data/map planets.txt` |
| Intervallo | righe **4790–5121** |
| Continuità | inizia subito dopo L2 (ultima riga 4781, `planet:Quicksilver`) |
| Unità | **79** (`DESCRIPTION`, tutte `PENDING`) |
| Parole | **4.509** inglesi → **4.506** italiane |
| Rapporto | 0,88 – 1,30 |
| Pianeti | **31** (da **Quirinal** a **Sardva**) |
| Tab di paragrafo | 24 |
| Virgolette | 14 (unità 12, 15, 38, 39, 45) |
| Token `<...>` | 0 |

Il blocco si chiude a fine pianeta: l'ultima unità è il testo `spaceport` di Sardva (riga 5121),
l'ultima riga tradotta dell'intervallo. Non ho tagliato un testo a metà e non ho saltato unità:
le 79 sono consecutive nell'ordine del file.

**Confronto con L1/L2:** 0 ID in comune (verificato sull'ID completo); nessuna unità già approvata
inclusa; tutte le 79 sono `PENDING` nel database, sia prima sia dopo il lavoro.

**Perché 79 unità e tre gruppi:** la sezione era già delimitata dal checkpoint (§8). L'ho tradotta
in tre gruppi nell'ordine del sorgente (25 / 25 / 29 unità), riversati in `parts/part01..03.json`.

---

## 2. Esempi rappresentativi

**Unità 1 — `planet:Quirinal`**

> While otherwise resembling a fairly typical moon, Quirinal is notable for the lava rifts that seem
> to be an inexplicably constant feature on its surface. For lack of a better description, it looks
> like the moon was struck a glancing blow by some sort of massive force, and the resulting chasm
> has been oozing lava ever since.

> Per il resto Quirinal somiglia a una luna piuttosto comune, ma è nota per le fratture laviche che
> sembrano una presenza inspiegabilmente costante sulla sua superficie. In mancanza di una
> descrizione migliore, sembra che la luna abbia ricevuto un colpo di striscio da una qualche forza
> immane, e la voragine che ne è risultata da allora continua a vomitare lava.

**Unità 10 — `planet:Raaqa-Uur-Kaav`**

> The one-time ancestral home of House Kaatrij is one of the few worlds of the Predecessors that
> remains relatively habitable.

> La dimora avita della Casata Kaatrij è uno dei pochi mondi dei Predecessori che resti relativamente
> abitabile.

**Unità 32 — `planet:Remote Blue`**

> Several of the local restaurants outright refuse to serve any species but the Kimek, claiming that
> their patrons would lose their appetites if forced to witness the disgusting eating habits of other
> species.

> Diversi ristoranti locali rifiutano senza mezzi termini di servire specie diverse dai Kimek,
> sostenendo che i loro clienti perderebbero l'appetito se costretti ad assistere alle disgustose
> abitudini alimentari delle altre specie.

**Unità 38 — `planet:Ring of Friendship`**

> This is the crown jewel of the Heliarchs, a ringworld that was completed by the Quarg before the
> Coalition formed and drove them away.

> Questo è il gioiello più prezioso degli Heliarch: un mondo ad anello completato dai Quarg prima che
> la Coalizione si formasse e li scacciasse.

**Unità 71 — `planet:Sandsnap`**

> A tourist FAQ in the docking area cheerily informs visitors that after the opening of the wormhole
> in Waypoint, Sandsnap was briefly considered as a destination for humans looking to settle in Hai
> space.

> Un documento di domande frequenti per i turisti nell'area di attracco informa allegramente i
> visitatori che, dopo l'apertura del wormhole a Waypoint, Sandsnap fu brevemente considerata una
> destinazione per gli umani che volevano stabilirsi nello spazio degli Hai.

**Unità 79 — `planet:Sardva`**

> You eventually find a vault that is willing to let you land so that you may refuel, but they don't
> seem too happy about your presence, and seem like they're only refueling you so that you stop
> asking every vault you come across.

> Alla fine trovi un caveau disposto a lasciarti atterrare per fare rifornimento, ma non sembrano
> affatto contenti della tua presenza, e danno l'impressione di rifornirti solo per farti smettere di
> chiedere a ogni caveau che incontri.

---

## 3. Interventi editoriali

**Venti correzioni in rilettura** (tabella completa in `review.md` §3): eliminazione degli anglicismi
residui (*standby*, *design*, *marketing*, *shipping*, *clamps*, *reverse engineer*), dei calchi
("sostiene una popolazione" → "ospita", "riprodurre a ritroso" → "ricostruire", "oggetto di un
notevole esame" → "osservato con grande attenzione") e di due ridondanze ("antica dimora ancestrale"
→ "dimora avita"; "le più grandi fra le Casate" → "le maggiori Casate").

Convenzioni nuove introdotte in questo blocco, coerenti col criterio di L1/L2 (parole comuni tradotte,
nomi inventati invariati):

| Termine | Resa | Occorrenze |
|---|---|---|
| `House Kaatrij`, `House Debdo`, `Arach houses` | Casata Kaatrij, Casata Debdo, Casate Arach | 9 |
| `New Houses` | Nuove Casate | 1 |
| `Coalition` | Coalizione | 8 |
| `ringworld` | mondo ad anello | 9 |
| `vault` | caveau | 6 |
| `wormhole` | wormhole (invariato) | 1 |
| `the Rim` | il Rim (in "nel Rim") | 1 |

Invariati: `Successors`, `Dirt Belt`, `Southern Rim`, `Deep`, `Unfettered`, `Remembrance Day`,
`Alpha Wars`, `Heliarch`, `Quarg`, `Kimek`, `Saryd`, `Arachi`, `Incipias`, `Bunrodea(n)`, `Korath`,
`Avgi`, `Hai`, `Kraz Cybernetics`, `Rowark's Roost`, `Rowark Balois`, `Waypoint`, `Mellow`, `Anax`,
`Aviskir`.

---

## 4. Decisioni ancora aperte

1. **`Successors` invariato** (8) contro `Predecessors` → Predecessori (2): asimmetria accettata dal
   checkpoint, ma è la scelta più visibile del blocco. "Successori" richiederebbe una ratifica e
   un'applicazione a tutto il corpus.
2. **`Coalition` → Coalizione** (8): decisione di L2, ancora da ratificare.
3. **`New Houses` → Nuove Casate** (1): decisione di L1, ancora da ratificare.
4. **`il Rim`** (1): forma breve di `Southern Rim` mantenuta invariata; alternativa "il Margine".
5. **`caveau`** (6): prestito invalso; alternativa "camera blindata".
6. **`wormhole`** (1): invariato come termine tecnico; nel testo narrativo l'alternativa è "varco".
7. **Unità 21 e 70** hanno lo stesso inglese (stazione in disarmo). Le traduzioni differiscono per
   varianti lessicali, così il lotto non contiene duplicati identici; se si vuole la memoria di
   traduzione rigida, l'unità 70 va riallineata alla 21.
8. Da L1/L2, **0 occorrenze qui**: `Consonance`, `Paradise World`, `hyperdrive` come nome di
   equipaggiamento, `Bunrodean` al plurale, `square dances`/`line dances`.

Nessuna di queste è stata scritta nel glossario.

---

## 5. Controlli

| Controllo | Esito |
|---|---|
| Indici: 79 attesi, 79 presenti, 0 mancanti, 0 estranei | OK |
| ID univoci, allineati a `source.json` | OK |
| `raw` identica alla riga del file (79/79) | OK |
| `english`/`kind`/`path`/`state` identici al DB (79/79) | OK |
| Traduzioni vuote | 0 |
| Duplicati di traduzione | 0 |
| Tab: totale invariato (24) e tab iniziale conservato unità per unità | OK |
| Virgolette: stesso conteggio per unità (14) | OK |
| Token `<...>`: multinsiemi identici (0) | OK |
| Spazi doppi / ai bordi / newline interne | OK |
| Rapporto di lunghezza 0,88–1,30 | OK |
| Tipografia: accenti sostitutivi, ellissi, caporali, em dash, apostrofi curvi | 0 |
| Parole inglesi residue | 0 |
| Anglicismi evitabili (`standby`, `design`, `marketing`, `shipping`, …) | 0 |

I controlli sono in `check.py` (esito stampato: `FAIL totale: 0`) e `verify.py`; entrambi operano in
sola lettura su `state.db` e sul sorgente.

---

## 6. Integrità

| Voce | Atteso | Osservato | Esito |
|---|---|---|---|
| `endless-sky` HEAD / modifiche | `b4aa3bac3` / 0 | `b4aa3bac3fcfa43d6…` / 0 righe | OK |
| `state.db` | 364 / 32.560, nessuna scrittura | `9125282973ddc8b9`, ultimo evento `14:33:18Z` | OK |
| Batch | B001–B006 | B001–B006 | OK |
| `glossary.csv` | invariato | `94e785f68be271d8` | OK |
| `staging/inventory_fields.csv` | invariato | `c9d8bc651cd70c56` | OK |
| `tools/l10n.py` | invariato (patch K4 non applicata) | `743c6a3f8c217f35` | OK |
| Output approvati | 3 hash del checkpoint | `5912ad739fe79fd4` · `2cf104fee408313c` · `1e0108530781320a` | OK |
| **L1** | intatto | `translation.json` `05cf183e1046f855`, `source.json` `84cc3540d874a6cd` | OK |
| **L2** | intatto | `translation.json` `d27126c4523204d9`, `source.json` `0b13e9e7f74b0503` | OK |
| Build / test / packaging | non eseguiti | non eseguiti | OK |

---

## 7. Artefatti

```
endless-sky-l10n/staging/editorial/L3_20261017_180114/
├── source.json       79 unità: idx, id, riga, contesto, inglese, delimitatore, tab iniziale, riga grezza, hash
├── translation.json  79 unità: idx, id, riga, contesto, inglese, italiano, ratio
├── review.md         convenzioni, 20 correzioni, incoerenze aperte
├── REPORT.md         questo report
└── parts/            part01.json (1–25), part02.json (26–50), part03.json (51–79)
                      + check.py, verify.py, counts.py, apply_fix.py (controlli, sola lettura sui dati)
```

Nessuno script nuovo nel toolbox del progetto: i quattro file `.py` sono controlli una tantum del
lotto, eseguiti da questa directory. Sorgente e traduzione restano ricostruibili da `source.json`
(contiene la riga grezza) e da `parts/`.

---

## 8. Cosa non è stato fatto

- Nessuna applicazione al gioco, nessun batch, nessuna build, nessun test di gioco, nessun packaging.
- Nessuna modifica a `state.db`, glossario, inventario, output approvati, sorgenti o dati.
- **Rendering non verificato** (nessun avvio del gioco, come da mandato).
- Le 79 unità sono **tradotte in staging e restano `PENDING`** nel database: non sono approvate,
  non sono importate, non sono conteggiate fra le 364 unità `APPROVED`.

Totale editoriale L1 + L2 + L3: **300 unità**, **15.291 parole** inglesi → **15.145** italiane.
