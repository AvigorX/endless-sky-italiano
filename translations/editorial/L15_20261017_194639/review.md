# L15 — Revisione editoriale del blocco `data/map planets.txt` 3614–3845

49 descrizioni, 2.693 parole inglesi → 2.756 italiane. **Lotto finale del file**: si chiude a riga 3845,
l'ultima unità prima del tratto 3851–6802 già tradotto da L1–L4. Con L15 `map planets.txt` raggiunge
**1.544 unità su 1.544** in staging.

---

## 1. Metodo

Stesso impianto dei lotti precedenti, su una sezione più corta del solito (49 unità invece di ~80):
contesto letto per pianeta, glossario e checkpoint consultati, traduzione in quattro gruppi (1–13, 14–26,
27–38, 39–49), rilettura del solo italiano.

Le 49 unità sono state esportate da `state.db` (tutte `PENDING`); `raw` coincide con la riga del sorgente per
tutte (verificato in `verify.py`, riscritto per il caso "fine file": la versione usata da L3 a L14 presume
una sezione successiva e qui si romperebbe).

---

## 2. Convenzioni applicate

| Termine | Resa | Occorrenze EN → IT | Note |
|---|---|---:|---|
| `Kimek` / `Arachi` / `Saryd` / `Heliarch` / `Gegno` / `Avgi` | invariati | 5/1/4/1/1/3 | — |
| `Successors` | invariato | 6 → 6 | il sorgente qui usa anche il singolare aggettivale `Successor space` |
| `Predecessors` | Predecessori | 2 → 2 | `inter-House war` → "guerra tra Casate" |
| `Syndicate` | Sindacato | 5 → 5 | — |
| `Coalition` | Coalizione | 1 → 1 | — |
| `Earth` | Terra | 1 → 1 | — |
| `CCOR` / `Confederated Councils of the Outer Rim` | **CCOR** / Consigli Confederati del Bordo Esterno | 1 / 1 | quarta occorrenza della forma sciolta (L10, L12, L14, L15) |
| `High Houses` / `New Houses` | Alte / Nuove Casate | 3 / 1 | — |
| `the Deep` | il Deep | 3 → 3 | — |
| `Paradise Planets` | Pianeti Paradisiaci | 1 → 1 | — |
| `Twilight Guard` | invariato | 2 → 2 | fazione |
| `the Assembly` | l'Assemblea | 1 → 1 | organo della Consonance: coerente con L2 ("Assemblea delle Entità Consonanti") |
| `longcows` | bovini lunghi | 2 → 2 | — |
| `void sprites` | **spiriti del vuoto** | 2 → 2 | creatura di Nasqueron: da ratificare |
| `Pulse Laser` | **Laser a impulsi** | 2 → 2 | nome di equipaggiamento: trattato come prodotto, maiuscolo |
| `rocket fuel` | carburante per razzi | 1 → 1 | — |

---

## 3. Interventi fatti in stesura e rilettura

| # | Intervento | Perché |
|---|---|---|
| 3 | "sfuggire alla **squallore affollato**" → "sfuggire al **degrado affollato**" | errore di accordo e di registro, corretto in rilettura |
| 22 / 24 | inglese **identico**, italiano differenziato | il sorgente ripete lo stesso passo sui lavori di ampliamento dello spazioporto; due rese distinte evitano il duplicato nel lotto (vedi §4.2) |
| 16 | `now defunct Confederated Councils` → "ormai defunti" | concordanza con "Consigli" |
| 20 | `Pulse Laser` → "Laser a impulsi" | nome commerciale dell'arma |
| 33 | `shanty towns` → "baraccopoli" | — |
| 34 | `the denouement of the Predecessors' last inter-House war` → "l'epilogo dell'ultima guerra tra Casate dei Predecessori" | — |
| 37 | `circadian rhythms` → "ritmi circadiani"; `two moons` → "due lune" | — |
| 38 | `cloud-to-cloud lightning discharges` → "scariche di fulmini tra nube e nube" | — |
| 41 | `coronal mass ejection` → "espulsione di massa coronale" | termine astrofisico corrente |
| 42 | `gas-dwelling organisms` → "organismi che vivono nel gas" | — |
| 47 | `perfect radial symmetry` → "perfetta simmetria radiale" | — |

---

## 4. Incoerenze e decisioni aperte (non bloccanti)

1. **`void sprites` → "spiriti del vuoto"** (2): nome di creatura. Se in altri file compare come nome
   tecnico (equipaggiamenti, missioni), va tenuto identico.
2. **Unità 22 e 24 con inglese identico**: il sorgente ripete il passo sui lavori di ampliamento. Le due rese
   italiane differiscono ("è in corso un grande progetto di ampliamento" / "proseguono da tempo grandi
   lavori"), restando fedeli. Reversibile se si preferisce la ripetizione esatta.
3. **`Pulse Laser` → "Laser a impulsi"** (2): nome di equipaggiamento reso come prodotto. Da verificare
   contro `glossary.csv` quando si tradurranno i file degli equipaggiamenti, dove il nome compare come
   chiave di gioco.
4. **`the Assembly` → l'Assemblea** (1): organo della Consonance; coerente con la resa di L2, ma la
   decisione su `Consonance` (§7 punto 19) resta aperta.
5. Restano aperte: `Successors`, `Antecessors`, `Consonance`, `Consigli Confederati` (L10–L15) vs
   `Confederated Councils` (L6), `caveau`, `ringroide`, `Halite`, `Bulk Freighter`, `Costruttori`,
   `skyhook`, `il Rim`, `il Nucleo`, `Twilight Guard`, `Egemonia Bunrodean`, `Wanderers`, istituzioni in
   inglese.

---

## 5. Esito dei controlli

```
unità 49 · mancanti 0 · estranei 0 · vuote 0 · duplicati IT 0
duplicati EN 1 (unità 22 e 24: ripetizione presente nel sorgente, documentata)
parole 2693 -> 2756 · ratio 0.93-1.23
tab 15 (tutti gli iniziali conservati) · virgolette 0 · token <...> 0
riga grezza identica al file: 49/49 · english/kind/path identici al DB: 49/49 · state PENDING 49/49
tipografia: 0 accenti sostitutivi, 0 ellissi tipografiche, 0 caporali, 0 em dash, 0 apostrofi curvi
parole inglesi residue: nessuna · anglicismi evitabili: nessuno
problemi 0
```

`verify.py` (riscritto per la fine del file) riporta:

```
unita: 49 righe 3614 - 3845
unita successiva nel file: (3851, 'planet:Neriene')
map planets.txt: 1544 unita totali nel DB
unita in staging (tutti i lotti): 1544
copertura di map planets.txt: 1544 / 1544
stato: COMPLETA
```

**Non verificato:** rendering in gioco (nessun avvio, come da mandato).
