# L15 — Lotto finale di `data/map planets.txt` — **FILE COMPLETO**

**Data:** 2026-10-17 · **Esito: lotto completo, 49/49 unità, 0 omissioni · `map planets.txt` al 100% in staging**
**Directory:** `endless-sky-l10n/staging/editorial/L15_20261017_194639/`

---

## 1. Blocco tradotto

| Voce | Valore |
|---|---|
| File | `data/map planets.txt` |
| Intervallo | righe **3614–3845** (ultima unità del tratto iniziale) |
| Unità | **49** (`PENDING`) |
| Parole | **2.693** inglesi → **2.756** italiane |
| Rapporto | 0,93 – 1,23 |
| Pianeti | **19** (da **Midway Emerald** a **Nepheritis**) |
| Tab di paragrafo | 15 |
| Virgolette | 0 |
| Token `<...>` | 0 |

Il lotto è più corto degli altri perché la sezione si esaurisce: dopo la riga 3845 il file riprende a 3851
con `planet:Neriene`, già tradotto da L1–L4.

---

## 2. Copertura del file — misurata

```
unita: 49 righe 3614 - 3845
unita successiva nel file: (3851, 'planet:Neriene')
map planets.txt: 1544 unita totali nel DB
unita in staging (tutti i lotti): 1544
copertura di map planets.txt: 1544 / 1544
stato: COMPLETA
```

**`map planets.txt` è interamente tradotto in staging**: 1.544 unità su 1.544, da L1–L4 (righe 3851–6802)
e L5–L15 (righe 17–3845). **Nessuna unità è stata importata nel database**: tutte restano `PENDING`.

---

## 3. Esempi rappresentativi

**Unità 16 — `planet:Mordente-Bridi`**

> A testament to the ingenuity of the engineering corps of the now defunct Confederated Councils of the
> Outer Rim, the massive Mordente-Bridi Station is one of the largest in human space.

> Testimonianza dell'ingegno del corpo di ingegneri dei Consigli Confederati del Bordo Esterno, ormai
> defunti, la massiccia Stazione Mordente-Bridi è una delle più grandi dello spazio umano.

**Unità 32 — `planet:Mutiny`**

> No longer prisoners, the inhabitants who remain do so because they prefer a simple life beyond the reach
> of any government, on a planet that will never be stolen from them because it carries nothing of value.

> Non più prigionieri, gli abitanti rimasti restano perché preferiscono una vita semplice fuori dalla portata
> di qualsiasi governo, su un pianeta che non sarà mai sottratto loro perché non contiene nulla di valore.

**Unità 37 — `planet:Mystery`**

> Saryd homes on other worlds often have night lighting cycles designed to mimic the moons of their
> homeworld.

> Le case dei Saryd su altri mondi hanno spesso cicli di illuminazione notturna progettati per imitare le
> lune del loro mondo natale.

**Unità 42 — `planet:Nasqueron`**

> Beneath Nasqueron's cloudy surface is a complex and thriving ecosystem of gas-dwelling organisms, from the
> massive void sprites all the way down to bacteria that inhabit tiny water droplets suspended in the air.

> Sotto la superficie nuvolosa di Nasqueron c'è un ecosistema complesso e fiorente di organismi che vivono nel
> gas, dai giganteschi spiriti del vuoto fino ai batteri che abitano le minuscole goccioline d'acqua sospese
> nell'aria.

**Unità 48 — `planet:Nepheritis`**

> An unusually large ice giant, Nepheritis is well-known among the denizens of the Paradise Planets for its
> prodigious rains of large diamonds.

> Gigante di ghiaccio insolitamente grande, Nepheritis è ben nota tra gli abitanti dei Pianeti Paradisiaci
> per le sue prodigiose piogge di diamanti di grosse dimensioni.

---

## 4. Interventi editoriali

Undici interventi in stesura e rilettura (dettaglio in `review.md` §3).

| Termine | Resa | Occorrenze |
|---|---|---|
| `Confederated Councils of the Outer Rim` | Consigli Confederati del Bordo Esterno | 1 (quarta occorrenza) |
| `the Assembly` | l'Assemblea | 1 |
| `void sprites` | spiriti del vuoto | 2 |
| `Pulse Laser` | Laser a impulsi | 2 |
| `Twilight Guard` | invariato | 2 |
| `rocket fuel` | carburante per razzi | 1 |

Un errore mio corretto in rilettura, prima dei controlli: unità 3, "sfuggire alla squallore affollato" →
"sfuggire al degrado affollato" (accordo e registro).

**Un duplicato dal sorgente**: le unità 22 e 24 hanno l'inglese identico (lavori di ampliamento dello
spazioporto di Mosaa-Oa-Vyret). Le due rese italiane differiscono, restando fedeli; documentato e
reversibile.

---

## 5. Controlli

| Controllo | Esito |
|---|---|
| Indici: 49 attesi, 49 presenti, 0 mancanti, 0 estranei | OK |
| ID univoci, allineati a `source.json` | OK |
| `raw` identica alla riga del file (49/49) | OK |
| `english`/`kind`/`path` identici al DB (49/49) · `state = PENDING` (49/49) | OK |
| Traduzioni vuote / duplicati IT | 0 / 0 |
| Duplicati EN | **1** (unità 22/24 — ripetizione nel sorgente, documentata) |
| Tab: totale invariato (15) e tab iniziale conservato unità per unità | OK |
| Virgolette: stesso conteggio per unità (0) | OK |
| Token `<...>`: multinsiemi identici (0) | OK |
| Spazi doppi / ai bordi / newline interne | OK |
| Rapporto di lunghezza 0,93–1,23 | OK |
| Tipografia: accenti sostitutivi, ellissi tipografiche, caporali, em dash, apostrofi curvi | 0 |
| Parole inglesi residue / anglicismi evitabili | 0 / 0 |

`check.py`: `FAIL totale: 0` al primo passaggio. `verify.py` riscritto per il caso "fine file".

---

## 6. Integrità

| Voce | Atteso | Osservato | Esito |
|---|---|---|---|
| `endless-sky` HEAD / modifiche | `b4aa3bac3` / 0 | identico / 0 | OK |
| `state.db` | 364 / 32.560, nessuna scrittura | `9125282973ddc8b9`, ultimo evento `14:33:18Z` | OK |
| Batch · glossario · inventario · `tools/l10n.py` · output approvati | invariati | hash invariati | OK |
| L1–L14 | intatti | hash invariati | OK |
| Build / test / packaging | non eseguiti | non eseguiti | OK |

---

## 7. Artefatti

```
endless-sky-l10n/staging/editorial/L15_20261017_194639/
├── source.json       49 unità (idx, id, riga, contesto, inglese, delimitatore, tab, riga grezza, hash)
├── translation.json  49 unità (idx, id, riga, contesto, inglese, italiano, ratio)
├── review.md         convenzioni, 11 interventi, duplicato documentato
├── REPORT.md         questo report
├── parts/            part01 (1–13), part02 (14–26), part03 (27–38), part04 (39–49)
└── check.py, verify.py
```

---

## 8. Cosa non è stato fatto

- Nessuna applicazione al gioco, nessun batch, nessuna build, nessun packaging.
- Nessuna modifica a `state.db`, glossario, inventario, output approvati, sorgenti o dati.
- **Rendering non verificato** (nessun avvio del gioco, come da mandato).
- Le 49 unità sono **tradotte in staging e restano `PENDING`**.

**Totale editoriale complessivo: 1.544 unità · 83.687 parole inglesi → 83.453 italiane.**
