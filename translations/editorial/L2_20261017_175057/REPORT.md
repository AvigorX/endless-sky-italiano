# L2 — Secondo blocco editoriale

**Data:** 2026-10-17 · **Esito: blocco completo, 101/101 unità, 0 omissioni**
**Directory:** `endless-sky-l10n/staging/editorial/L2_20261017_175057/`

---

## 1. Blocco tradotto

| Voce | Valore |
|---|---|
| File | `data/map planets.txt` |
| Intervallo | righe **4308–4781** |
| Continuità | inizia subito dopo L1 (ultima riga 4295, `planet:Oblivion`) |
| Unità | **101** (`DESCRIPTION`, tutte `PENDING`) |
| Parole | **5.552** inglesi → **5.472** italiane |
| Rapporto | 0,89 – 1,27 |
| Pianeti | 44 (da **Occupas** a **Quicksilver**) |
| Tab di paragrafo | 34 |
| Virgolette | 6 |
| Token `<...>` | 0 |

Il blocco si chiude a fine pianeta: l'ultima unità è la quarta descrizione di Quicksilver. Non ho tagliato
un testo a metà e non ho saltato unità: le 101 sono consecutive nell'ordine del file.

**Perché 101 e non 120:** la densità di parole per unità qui è più alta che in L1 (55 contro 44). A parità
di range (100–200) ho scelto il limite basso per mantenere lo stesso volume di L1 e garantire una
revisione reale invece di una traduzione affrettata.

**Confronto con L1:** 0 ID in comune (verificato), nessuna unità già approvata inclusa.

---

## 2. Esempi rappresentativi

**Unità 20 — `planet:Osolaa-Val-Mavra`**

> The desolate habitation trench and ice-covered surface of the moon are testaments to Sejra's folly; of
> trying to escape something they did not understand and had no hope of stopping.

> La fossa abitativa desolata e la superficie ghiacciata della luna sono testimonianze della follia di
> Sejra: del tentativo di sfuggire a qualcosa che non comprendeva e che non aveva alcuna speranza di
> fermare.

**Unità 56 — `planet:Periaxle Circuit`**

> Having very little in the form of windows to look out into the system, and not much to gaze at the
> small, barren planet it encompasses, the station sees very few visitors...

> Con pochissime finestre per guardare fuori verso il sistema, e ben poco da ammirare nel piccolo e
> sterile pianeta che racchiude, la stazione riceve pochissimi visitatori...

**Unità 69 — `planet:Placatious`**

> ...the executive responsible for the entire scheme was forced into an early retirement, and the idea was
> quietly dropped.

> ...il dirigente responsabile dell'intera operazione fu costretto al prepensionamento, e l'idea fu
> accantonata in silenzio.

**Unità 80 — `planet:Poisonwood`**

> Its walls are covered in photographs from after the war, all taken here on Poisonwood: freed slaves
> boarding Navy ships to leave the planet that brought them so much pain; Navy officers disembarking to
> retire on the world that they liberated; friends gone away, and friends left behind.

> Le pareti sono coperte di fotografie del dopoguerra, tutte scattate qui su Poisonwood: schiavi liberati
> che salgono sulle navi della Marina per lasciare il pianeta che aveva dato loro tanto dolore; ufficiali
> della Marina che sbarcano per ritirarsi sul mondo che hanno liberato; amici partiti e amici rimasti.

**Unità 101 — `planet:Quicksilver`**

> The air is not particularly cold here, but it is very damp, and the howling weather outside seems to
> weigh on everyone's spirits.

> L'aria non è particolarmente fredda, ma è molto umida, e il vento ululante fuori sembra pesare
> sull'umore di tutti.

---

## 3. Interventi editoriali

Cinque correzioni in rilettura (dettaglio in `review.md` §3): "riestrarre" → "raccogliere ripetutamente";
"santuario naturale per specie esotiche" → "santuario per la fauna selvatica, con specie esotiche";
"campagna marketing" → "campagna pubblicitaria"; "Ospita la Betelgeuse Shipyards" → "la sede della…";
"il tempo ululante" → "il vento ululante".

Convenzioni nuove introdotte in questo blocco, coerenti col criterio di L1 (parole comuni tradotte,
nomi inventati invariati):

| Termine | Resa | Occorrenze |
|---|---|---|
| `Coalition` | Coalizione | 5 |
| `hyperdrive` | iperpropulsore | 3 |
| `the Incursion` | l'Incursione | 3 |
| `Paradise World` | Mondo Paradisiaco | 1 |
| `House Sejra` | Casata Sejra | 1 |

Invariati: `Remembrance Day` (1), `Syndicate` → Sindacato (2, come L1), `Dissonance`, `Consonance`,
`Bunrodean`, `Arach`, `Avgi`, `Hai`, `Pug`, `Remnant`, `Ka'het`, `Incipias`, `Scin`, nomi di aziende e
locali (`Betelgeuse Shipyards`, `Lovelace Labs`, `Yoot Ki…`, `The Parting Glass`).

---

## 4. Decisioni ancora aperte

1. **`Coalition` → Coalizione**: nuova decisione di universo, da ratificare (non c'era in L1).
2. **`Assembly of Consonant Polities`** reso "Assemblea delle Entità Consonanti" mentre `Consonance` resta
   in inglese: è l'incoerenza più visibile del blocco. Serve una scelta (tradurre anche Consonance in
   "Consonanza", oppure "Entità della Consonance").
3. **`Paradise World` → Mondo Paradisiaco**: allineare se l'etichetta compare nella UI.
4. **`hyperdrive` → iperpropulsore**: verificare l'eventuale nome dell'equipaggiamento.
5. **`Bunrodean` al plurale invariato**: se si preferisce "Bunrodeani", decidere una volta e applicare.
6. Restano aperte da L1: `New Houses` → Nuove Casate (0 occorrenze qui), `Remembrance Day` invariato,
   `Syndicate` → Sindacato, `square dances`/`line dances` (0 occorrenze qui).

Nessuna di queste è stata scritta nel glossario.

---

## 5. Controlli

| Controllo | Esito |
|---|---|
| Indici: 101 attesi, 101 presenti, 0 mancanti, 0 estranei | ✅ |
| ID univoci, allineati a `source.json` | ✅ |
| Traduzioni vuote | 0 |
| Duplicati di traduzione | 0 |
| Tab: numero invariato (34) e tab iniziale conservato | ✅ |
| Virgolette: stesso conteggio per unità (6 unità) | ✅ |
| Token `<...>`: multinsiemi identici (0) | ✅ |
| Spazi doppi / ai bordi | ✅ |
| Rapporto di lunghezza 0,89–1,27 | ✅ |
| Parole inglesi residue | 1: "The Parting Glass" (nome proprio, atteso) |

---

## 6. Integrità

| Voce | Atteso | Osservato | Esito |
|---|---|---|---|
| `endless-sky` HEAD / modifiche | `b4aa3bac3` / 0 | identico / 0 righe | ✅ |
| `endless-sky-mingw` | 4 file `M` | 4 file `M` | ✅ |
| `state.db` | 364 / 32.560, nessuna scrittura | `9125282973ddc8b9`, ultimo evento `14:33:18Z` | ✅ |
| Batch | B001–B006 | B001–B006 | ✅ |
| `glossary.csv` | invariato | `94e785f68be271d8` | ✅ |
| `inventory_fields.csv` | invariato | `c9d8bc651cd70c56` | ✅ |
| `tools/l10n.py` | invariato (patch K4 non applicata) | `743c6a3f8c217f35` | ✅ |
| Output approvati | 3 hash del checkpoint | `5912ad73…` · `2cf104fe…` · `1e010853…` | ✅ |
| **L1** | intatto | `translation.json` `05cf183e1046f855`, `source.json` `84cc3540d874a6cd` | ✅ |
| Build / test / packaging | non eseguiti | non eseguiti | ✅ |

---

## 7. Artefatti

```
endless-sky-l10n/staging/editorial/L2_20261017_175057/
├── source.json       101 unità: id, riga, contesto, inglese, delimitatore, riga grezza
├── translation.json  101 unità: id, riga, inglese, italiano, ratio
├── review.md         convenzioni, correzioni, incoerenze aperte
├── REPORT.md         questo report
└── parts/            part01..04.json (traduzioni per gruppo)
```

Nessuno script nuovo: esportazione e controlli sono stati eseguiti con comandi una tantum; sorgente e
traduzione restano ricostruibili da `source.json` (contiene la riga grezza) e da `parts/`.

---

## 8. Cosa non è stato fatto

- Nessuna applicazione al gioco, nessun batch, nessuna build, nessun packaging.
- Nessuna modifica a `state.db`, glossario, inventario, output approvati, sorgenti o dati.
- **Rendering non verificato** (nessun avvio del gioco, come da mandato).

Totale editoriale L1 + L2: **221 unità**, **10.782 parole** inglesi → **10.639** italiane.
