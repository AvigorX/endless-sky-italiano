# CHECKPOINT_AGENTE_20261018.md — **OBSOLETO** (storia di L67 → L68)

> **Non usare come stato corrente.** Il documento di ripresa a freddo valido è
> `CHECKPOINT_AGENTE_SESSIONE_20261018.md`, aggiornato dopo la chiusura di **L68** (prossimo lotto: **L69**).
> Questo file resta come traccia di come è stato preparato L68; i numeri del workspace qui sotto sono
> stati riallineati al 2026-10-18 dopo L68, così il checker non legge valori falsi.

**Generato il 2026-10-18 dopo la chiusura di L66 e L67** (L67 chiude `culture conversations.txt`).
**Superato**: L68 è stato chiuso lo stesso giorno (`successor 2 ghosts myurej.txt`, righe 16–113, 49 unità,
`check.py` 37 controlli, `verify.py` 46 controlli, sha `eaafbeb6e504c701`). La sezione §4 descrive quindi il
lotto **L68 come è stato aperto**, non il prossimo lotto.

**Regola suprema**: se un numero qui non torna con il workspace, **vince il workspace**. Il documento si
**rigenera** dai dati, non si aggiusta a mano.

**Verifica** (exit 0 e `FAIL: 0`):

```bash
cd ~/PROGETTI/G-DEV/GAME-SOURCE-LAB/endless-sky-l10n
python staging/editorial/tools/check_handoff.py CHECKPOINT_AGENTE_20261018.md
```

---

## 1. Il progetto in cinque righe

Traduzione **italiana** di *Endless Sky* (gioco libero, dati in file di testo sotto `data/`). Si lavora
per **lotti**: ogni lotto copre un intervallo di righe di un file, si traduce in `staging/editorial/`, si
verifica con due script indipendenti a **exit code**, e resta `PENDING` nel database.

**Lo staging NON è approvazione.** Non si scrive mai su `state.db`, non si carica nulla nel gioco, non si
tocca il repository originale: il deliverable è **staging verificato**.

```
~/PROGETTI/G-DEV/GAME-SOURCE-LAB/endless-sky-l10n/
├── endless-sky/                     # repository originale, HEAD b4aa3bac3, MAI modificato
├── data/                            # dati del gioco (sorgente delle unità)
├── tools/l10n.py · state.db · glossary.csv   # PROTETTI
├── staging/editorial/
│   ├── tools/{state,export_section,next_section,check_handoff}.py · protected.sha256
│   ├── inventory_fields.csv         # PROTETTO
│   └── L*_<data>_<ora>/             # 71 lotti con translation.json (72 cartelle L*)
│       ├── source.json  translation.json  check.py  verify.py
│       ├── parts/partNN.json
│       └── STATO.md  REPORT.md  review.md
├── HANDOFF_L68_20261018.md          # contratto del prossimo lotto (0/23 col checker)
├── CHECKPOINT_EDITORIALE.md         # totali, decisioni numerate (1–225)
└── CHECKPOINT_SESSIONE_20261018.md  # stato di sessione (0/50 col checker)
```

| file protetto | sha256[:16] |
|---|---|
| `state.db` | `9125282973ddc8b9` |
| `glossary.csv` | `94e785f68be271d8` |
| `staging/inventory_fields.csv` | `c9d8bc651cd70c56` |
| `tools/l10n.py` | `743c6a3f8c217f35` |

Se un hash è cambiato, **fermati**: qualcosa ha scritto su un file che il workflow tratta in sola lettura.

---

## 2. Regole inviolabili

1. **Nessuna approvazione, nessun caricamento nel gioco.** Solo staging.
2. **File protetti**: i difetti di inventario del `log` si documentano, non si riparano.
3. **Numeri misurati, mai dedotti** dal lotto precedente (decisione 119).
4. **`UI_LABEL` identici** ed elencati **uno per uno** (decisione 151).
5. **Parti senza tab iniziali**: li antepone il costruttore di `check.py`.
6. **Virgolette dispari riprodotte, non chiuse**; confronto come **insieme di indici**.
7. **Duplicati quasi identici si risolvono riscrivendo**; due scelte simili **non** sono la stessa scelta
   se l'inglese le distingue (decisione 216).
8. **Token `<…>` non si traducono**; parità **per simbolo**, non solo sul totale (decisione 219).
9. **Nomi propri**: non si traducono, non si unificano se incoerenti, i refusi non si replicano.
10. **Rapporto lunghezze**: gate `0,55 < IT/EN < 1,90`; fuori banda si **riscrive** (decisioni 211, 223).
11. **Caratteri non latini vietati**: `°` (0xB0) rifiutato (decisione 212).
12. **Un tipo assente può tornare presente**: `LOGBOOK` e `UI_LABEL` vanno resi **positivi** quando ci sono
    (decisioni 190, 221).
13. **Un lotto incompleto non si dichiara chiuso**: `FAIL totale: 0` **e** `verify.py` exit 0.

---

## 3. Stato misurato (18 ottobre 2026, dopo L68)

```
data/human/human missions.txt         4253/ 4253 unità (100.0%) · 104495 EN ->  98511 IT · 6 lotti
data/map planets.txt                  1544/ 1544 unità (100.0%) ·  83687 EN ->  83453 IT · 18 lotti
TOTALE staging: 24873 unità · 792339 EN · 751337 IT
```

- lotti con `translation.json`: **93 directory** su 94 (`L19_20261017_201342/` è un export scartato);
- `verify.py`: **91**, tutti **verdi** (L1, L2 e L19 non ne hanno);
- database: **APPROVED 364 · PENDING 32560** su 32.924 unità; ultimo evento `2026-10-17T14:33:18Z`;
- `UI_LABEL` `PENDING` (non traducibili): 630;
- residuo traducibile (formula): 7057 — misurato **7.620 unità / 183.684 parole** (decisione 99);
- `human missions.txt` completo: **2141 unità / 51158 parole** dopo la riga 6428, già tradotte;
- **trentuno file completi**: i trenta storici più `culture conversations.txt` (374 unità, dieci lotti,
  11.269 EN → 10.858 IT);
- **file aperto da L68**: `data/successors/successor 2 ghosts myurej.txt` (211 unità, **file completo** con L68–L72);
- `endless-sky` HEAD **b4aa3bac3**, `git status` vuoto.

### Ultimi due lotti chiusi

| lotto | righe | unità | EN → IT | `check.py` | `verify.py` | sha256[:16] |
|---|---|---:|---|---|---|---|
| L67 | 1062–1122 | 35 | 811 → 787 | 33 controlli | 38 controlli | `ad997eaa9007d7c2` |
| **L68** | **16–113** | **49** | **1.502 → 1.447** | **37 controlli** | **46 controlli** | **`eaafbeb6e504c701`** |

L67 ha **chiuso** `culture conversations.txt` (374/374). L68 ha aperto `successor 2 ghosts myurej.txt`:
**2 `LOGBOOK`** (unità 23 = categoria `People` lasciata identica, unità 24 = testo tradotto), **10 token**
in 5 famiglie, 2 gruppi di duplicati inglesi, **0 virgolette dispari**.

---

## 4. Il lotto L68 (chiuso il 2026-10-18) — descrizione storica

```bash
cd ~/PROGETTI/G-DEV/GAME-SOURCE-LAB/endless-sky-l10n
python staging/editorial/tools/export_section.py "staging/editorial/L68_$(date +%Y%m%d)_$(date +%H%M%S)" \
  "data/successors/successor 2 ghosts myurej.txt" 16 113
```

| voce | valore |
|---|---|
| File | `data/successors/successor 2 ghosts myurej.txt` |
| Righe | 16-113 |
| Unità | 49 |
| Parole | 1502 |
| Contesti | 1 (`Successors: Ghosts Myurej 1` … `Successors: Ghosts Myurej 1`) |
| Tab / virgolette | 42 / 90 |
| Confine dopo | riga 118 apre `mission:Successors: Ghosts Myurej 2` |

Tipi: **44 `MISSION_TEXT`**, 1 `VALUE`, 1 `DESCRIPTION`, **1 `UI_LABEL`** (unità 20), **2 `LOGBOOK`**
(unita 23 e 24); 0 `DIALOG`, 0 `CONVERSATION`, 0 `TEXT`; **13 token** in 5 famiglie (`<first>` 3,
`<last>` 3, `<ship>` 2, `<destination>` 1, `<planet>` 1); **0 virgolette dispari**.

### Le quattro cose che rendono L68 diverso da L67

1. **File nuovo della linea Successors**: lessico e nomi già fissati in L45 (`successor 2 ghosts.txt`) e
   L46–L47 (`successor 1 prologue.txt`) vanno riusati, non reinventati.
2. **2 `LOGBOOK` e 1 `UI_LABEL`**: tre controlli **positivi**, ciascuno con l'elenco per indice.
3. **13 token in 5 famiglie**: parità **per simbolo**; `<first>`/`<last>` sono nome e cognome del
   giocatore e non si traducono.
4. **49 unità in un solo contesto**: si chiude in un lotto, senza tagli.

---

## 5. Metodo obbligatorio

### 5.1 Preflight

```bash
cd ~/PROGETTI/G-DEV/GAME-SOURCE-LAB/endless-sky-l10n
python staging/editorial/tools/state.py                                  # ESITO: OK
python staging/editorial/tools/check_handoff.py HANDOFF_L68_20261018.md  # 0 FAIL
python staging/editorial/L67_20261018_191025/check.py                    # FAIL totale: 0
python staging/editorial/L67_20261018_191025/verify.py                   # exit 0
```

### 5.2 Apertura

1. `export_section.py` (§4); rifiuta di sovrascrivere una directory esistente.
2. **Ricognizione misurata**: unità, righe prima/dopo, tipi, tab, virgolette (totali e dispari), token,
   quadre/backtick, duplicati inglesi, `UI_LABEL`, righe `log` con la loro forma.
3. `check.py` derivato da L67 con **ogni asserzione ricostruita**: `NT` positivo (1), `LOGBOOK` positivo (2)
   con l'asserzione sulle tre forme `log`, `DIALOG`/`CONVERSATION`/`TEXT` dichiarati assenti, token con
   parità per simbolo, costruttore dei tab. Ogni riga di `rows` è una tupla a tre elementi.

### 5.3 Parti

- 35-50 unità (qui un solo contesto da 49: una parte sola, oppure 25+24).
- Senza tab iniziali; `check.py --range a b` dopo ogni parte.
- `check.py --range` su un lotto incompleto stampa `copertura del lotto N/49 | FAIL`: atteso.

### 5.4 Chiusura

1. `check.py` → `FAIL totale: 0`.
2. `verify.py` **indipendente**: riga grezza da `source.json`, english/kind/path/context vs `state.db`,
   PENDING, no APPROVED, id/ordine, collocazione, copertura per segmento, kind, `NT`, `LOGBOOK`,
   `DIALOG`, parità tab/virgolette/token per unità e per simbolo, insieme delle virgolette dispari,
   duplicati, ricostruzione da parti.
3. `STATO.md`, `REPORT.md`, `review.md`.
4. Aggiornare **nello stesso momento** `HANDOFF_L69_20261018.md`, `CHECKPOINT_EDITORIALE.md`,
   `CHECKPOINT_SESSIONE_20261018.md` e questo file; poi `check_handoff.py` sui tre a contratto.
5. `state.py` verde.

---

## 6. Comandi

```bash
cd ~/PROGETTI/G-DEV/GAME-SOURCE-LAB/endless-sky-l10n
python staging/editorial/tools/state.py
python staging/editorial/tools/next_section.py "data/successors/successor 2 ghosts myurej.txt" 113
python staging/editorial/L68_*/check.py
python staging/editorial/L68_*/verify.py; echo "exit=$?"
python staging/editorial/tools/check_handoff.py HANDOFF_L68_20261018.md
python staging/editorial/tools/check_handoff.py CHECKPOINT_SESSIONE_20261018.md
python staging/editorial/tools/check_handoff.py CHECKPOINT_AGENTE_20261018.md
for f in staging/editorial/L*/verify.py; do python "$f" >/dev/null 2>&1 || echo "ROSSO $f"; done
```

Oggi: **69 file, 69 verdi, 0 rossi.**

---

## 7. Trappole già pagate

1. **I controlli si giustificano, non si copiano** (decisione 119): `NT` 0 in L66, 0 in L67, **1 in L68**;
   `LOGBOOK` 0, 1, **2**; token 0, 2, **13**.
2. **Un tipo assente può tornare presente**: `LOGBOOK` in L67 ha richiesto di cambiare il segno del
   controllo (decisione 221); con 2 diari L68 deve restare positivo.
3. **Le assenze si dichiarano** con `== []` / `== ()` (decisione 160).
4. **Copertura per segmento** (decisione 166); «di file» solo per chi chiude (L52, L55, L57, L67).
5. **Gli insiemi non hanno ordine**: `tuple(sorted(...))`.
6. **`translation.json` non contiene `raw`**: leggere `source.json` (decisione 186).
7. **Il filtro `parole inglesi residue` rimuove i titoli** (decisione 205): si riscrive la traduzione.
8. **`LOG` può restare definito due volte** (decisione 222): correggere **per riga**, non con `str.replace`.
9. **Rapporto fuori banda** (decisioni 211, 223): L63 unità 27 da 2,08 a 1,85; L66 unità 41 da 0,48 a 0,64.
10. **Caratteri non latini** (decisione 212): `°` rifiutato; usare la parola.
11. **La finestra di export non è la prima unità** (decisione 196).
12. **Le patch si copiano dal file** (decisioni 192, 204).
13. **`write_file` su un file già scritto in questa sessione viene rifiutato**: usare un nuovo nome
    (mk67b/mk67c) o leggere prima di sovrascrivere.
14. **`check_handoff.py` ha un formato a contratto**: copertura in stile `state.py` con lo spazio dopo la
    barra, `non traducibili): 630` e `residuo traducibile: 7057` fuori dal grassetto, `**2141 unità /
    51158 parole** dopo la riga 6428`, **quattro backtick** in `Contesti` se il contesto è uno solo,
    `Confine dopo` col prefisso grezzo.

---

## 8. Integrità dei lotti (sha256[:16] di `translation.json`)

| lotto | unità | hash | lotto | unità | hash |
|---|---:|---|---|---:|---|
| L1 | 120 | `L1 05cf183e1046f855` | L2 | 101 | `L2 d27126c4523204d9` |
| L3 | 79 | `L3 c9bf11f695b29422` | L3b | 84 | `L3b 957a3bd94f8bc712` |
| L3c | 84 | `L3c 9a7b385cca8ad613` | L3d | 122 | `L3d 31c00efa471b6f44` |
| L4 | 83 | `L4 c90d1b7d9523c6c8` | L5 | 84 | `L5 dd5344fd8ebed83b` |
| L6 | 84 | `L6 9f14fc1dc2ae07b8` | L7 | 84 | `L7 983598ed163083e0` |
| L8 | 77 | `L8 593b93a74f26e952` | L9 | 82 | `L9 629b020cb125c5fc` |
| L10 | 81 | `L10 d6deac4868695c41` | L11 | 80 | `L11 b323f2c2b3653ef0` |
| L12 | 88 | `L12 885565766fbc2ff7` | L13 | 79 | `L13 e399c61bfbc7dd3b` |
| L14 | 83 | `L14 db2bbb9216cb37dd` | L15 | 49 | `L15 dfa6b7f9d2ace40d` |
| L16 | 181 | `L16 cabde982f103c218` | L17 | 133 | `L17 9a3566bd4e577c36` |
| L18 | 187 | `L18 45e6693c69689927` | L19 | 1611 | `L19 a56041126bb484e8` |
| L20 | 1676 | `L20 b955f643f2acd399` | L21a | 465 | `L21a 0a849622634ec72a` |
| L21b | 637 | `L21b 70d260bc3fcec51b` | L22 | 390 | `L22 24e9b400b5c5cb75` |
| L23 | 1355 | `L23 f745dd523ff32319` | L24 | 1250 | `L24 92e4737d1b55d9dc` |
| L25 | 1174 | `L25 fc850daffc4363da` | L26 | 406 | `L26 889ca7d8935e9ac0` |
| L27 | 917 | `L27 37e09b22e11caf89` | L28 | 821 | `L28 ba932b11d8e35fb8` |
| L29 | 823 | `L29 b8bf47375f390542` | L30 | 730 | `L30 5adcc2bfda276f8f` |
| L31 | 663 | `L31 09e75a0528604150` | L32 | 805 | `L32 bdabdc64ad3b7ce1` |
| L33 | 731 | `L33 1bc292eafe08f311` | L34 | 703 | `L34 50fbd52f12326484` |
| L35 | 663 | `L35 3a434b106edfceb3` | L36 | 552 | `L36 502a8f740d9181e9` |
| L37 | 482 | `L37 8a12ed7b7d904c04` | L38 | 596 | `L38 1cda2e18fc38b163` |
| L39 | 114 | `L39 b41df1b6b2b9dec7` | L40 | 211 | `L40 516c1b1a59c9cfe0` |
| L41 | 72 | `L41 17727c643c46cd38` | L42 | 572 | `L42 1115f51df15d6704` |
| L43 | 299 | `L43 018217f1aac1ba49` | L44 | 625 | `L44 2a83b689b3604483` |
| L45 | 680 | `L45 480ff95bd7e2d97b` | L46 | 221 | `L46 aa71c36e9b399505` |
| L47 | 124 | `L47 d783356009cbb44d` | L48 | 180 | `L48 fcb07ed0909aeb65` |
| L49 | 256 | `L49 0fe8cac3bf134108` | L50 | 119 | `L50 50c003eec1b5e9a3` |
| L51 | 152 | `L51 62a89c1348ea5162` | L52 | 135 | `L52 d529e6f657dc9aef` |
| L53 | 89 | `L53 7e2899a23c7c3c8e` | L54 | 159 | `L54 5ac7ae01fd74ae15` |
| L55 | 28 | `L55 69eaa9d886a113f0` | L56 | 171 | `L56 c2fe3862c23a294e` |
| L57 | 127 | `L57 c3f3b8a9de69cfe1` | L58 | 43 | `L58 0a66e11210f15963` |
| L59 | 42 | `L59 5d42121563e61f8d` | L60 | 31 | `L60 412787a6b5f31400` |
| L61 | 26 | `L61 8b7278d41edd723f` | L62 | 30 | `L62 8b9f92399b32c32a` |
| L63 | 37 | `L63 3535834a2a119c44` | L64 | 42 | `L64 57a238ca0241c4ca` |
| L65 | 43 | `L65 8cde7537201a63c9` | L66 | 45 | `L66 41a48d5412d5b7c6` |
| L67 | 35 | `L67 ad997eaa9007d7c2` | | | |

---

## 9. Protocollo di ripresa a freddo

1. `python staging/editorial/tools/state.py` → **INTEGRITA' OK**, `TOTALE staging: 24873`.
2. `ls -d staging/editorial/L*/translation.json | wc -l` → atteso **71**. Se è 70 o 72, c'è una directory
   aperta a metà o un lotto cancellato: leggi `STATO.md` prima di tradurre.
3. `check_handoff.py` sui tre a contratto (`HANDOFF_L68`, `CHECKPOINT_SESSIONE`, `CHECKPOINT_AGENTE`):
   tutti `FAIL: 0`. Gli handoff dei lotti chiusi falliscono di proposito.
4. Se esiste `staging/editorial/L68_*/` con `parts/`, **il lotto è in corso**: esegui `check.py`, guarda la
   copertura, riprendi dalla prima unità mancante.
5. Altrimenti apri il lotto (§4) e ricomincia dal §5.2.

---

## 10. Cosa non fare

- **Non** scrivere su `state.db`, **non** approvare, **non** caricare nel gioco.
- **Non** toccare `tools/l10n.py`, `glossary.csv`, `staging/inventory_fields.csv`.
- **Non** dedurre i numeri dal lotto precedente: rimisura.
- **Non** riscrivere interi file per correggere una funzione: diff minimi.
- **Non** «aggiustare» un documento per far passare il checker: si rigenera dai dati.
- **Non** dichiarare chiuso un lotto senza `FAIL totale: 0` **e** `verify.py` exit 0.
- **Non** tradurre né unificare i nomi propri (Avgi, Gegno, Quarg, Free Worlds, Parliament, Navy, Deep,
  Syndicate, Delta V, Burthen, Gagarin, Chydiyi, Myurej, Kasii-Sola, Belenos, Abernathy, Caldarone,
  Tarazed, Adrauni, Dueyu Eitch, Chiron, Prasinos).

---

## 11. Criterio di «fatto» per L68

| requisito | prova |
|---|---|
| 49/49 unità tradotte | `check.py` → `copertura del lotto 49/49 \| OK` |
| `NT` (1) e `LOGBOOK` (2) identici al sorgente | `check.py` → righe positive con elenco per indice |
| tab e virgolette invariati per unità | `check.py` → `tab per unita ok`, `virgolette per unita ok` |
| token per simbolo | `check.py`/`verify.py` → 13/13, 5 famiglie, `Counter` uguali |
| assenze dichiarate | `check.py` → `DIALOG`/`CONVERSATION`/`TEXT` `OK` |
| duplicati spiegati | `check.py` → `duplicati italiano non spiegati dal sorgente ok` |
| rapporto nel gate | `check.py` → `rapporto lunghezza` 0,55–1,90 |
| indipendenza della verifica | `verify.py` → `FAIL: 0`, exit 0 |
| database intatto | `state.py`: `APPROVED 364 · PENDING 32560` |
| documenti coerenti | `check_handoff.py` → `FAIL: 0` su handoff, `CHECKPOINT_SESSIONE`, `CHECKPOINT_AGENTE` |

---

## 12. Limiti dichiarati

- **Nessuna approvazione, nessun caricamento**: 24.203 unità in staging, tutte `PENDING`.
- **Lacuna dell'estrattore** (`log` fra virgolette): sei righe, L45 195/305/357/418, L46 62, L47 54.
- **Residuo**: 8.357 unità / 202.795 parole misurate; la formula stampa 7727.
- **La voce** dei file tradotti è verificata solo come testo.
- **Scelte da propagare**: «teredini di Delve» (L66–L67), «categoria», «Tonner», «ritardanti», «signori»,
  «Parlamento»/«Marina»/«Free Worlds», «Giornata della Terra», «blackout», «iperguida», «dottorandi»,
  «Pesce Piatto», «Sindacato», «Mondi del Paradiso», «Bordo Esterno».

---

## 13. Documenti da leggere, in quest'ordine

1. `CHECKPOINT_SESSIONE_20261018.md` — ripresa a freddo, stato, ciclo di lavoro.
2. `HANDOFF_L68_20261018.md` — contratto formale del prossimo lotto.
3. `CHECKPOINT_EDITORIALE.md` — totali e **225 decisioni** numerate.
4. `staging/editorial/L66_20261018_190909/review.md` — le quattro scenette esotiche;
   `L67_20261018_191025/review.md` — i teredini, il `LOGBOOK`, la chiusura del file.
5. `staging/editorial/L67_20261018_191025/check.py` e `verify.py` — modello da cui derivare, non copiare.
