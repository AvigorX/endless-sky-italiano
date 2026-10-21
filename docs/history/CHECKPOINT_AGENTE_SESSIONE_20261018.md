> **Sostituito** da `RIPRESA_L154_20261019.md` per la ripresa a freddo; questo file resta come storia.

# CHECKPOINT_AGENTE_SESSIONE_20261018.md — ripresa a freddo per L154

**Documento autosufficiente.** Chi apre la sessione successiva senza memoria del passato parte da qui e
nient'altro: contesto, regole, stato misurato, prossimo lotto, metodo, comandi, trappole, glossario, limiti
dichiarati.

**Generato** il 2026-10-19 dopo il **batch L150–L153**, che ha portato `data/coalition/coalition jobs.txt` a
156/197. Il progetto ha **cinquanta file completi** e **27.802 unità** in staging.
**Regola suprema**: se un numero qui non torna con il workspace, **vince il workspace**; il documento si
**rigenera dai dati**, non si aggiusta a mano.

---

## 1. Il progetto in cinque righe

Traduzione **italiana** di *Endless Sky* (testi in file di testo sotto `data/`). Si lavora per **lotti**: ogni
lotto copre un intervallo di righe di un file, si traduce in `staging/editorial/L<n>_<data>_<ora>/` e si
verifica con **due script indipendenti a exit code** (`check.py`, `verify.py`). Tutto resta `PENDING`: **lo
staging non è approvazione**. Non si scrive mai su `state.db`, non si carica nulla nel gioco, il repository
originale non si tocca.

```
~/PROGETTI/G-DEV/GAME-SOURCE-LAB/endless-sky-l10n/
├── endless-sky/                    # repo originale, HEAD b4aa3bac3, MAI modificato
├── data/                           # sorgente delle unità
├── tools/l10n.py                   # PROTETTO
├── state.db                        # PROTETTO, sola lettura (contiene anche i testi APPROVED)
├── glossary.csv                    # PROTETTO
├── staging/editorial/
│   ├── tools/{state,export_section,next_section,check_handoff}.py · protected.sha256
│   ├── inventory_fields.csv        # PROTETTO
│   └── L*_<data>_<ora>/            # 158 cartelle, 157 con translation.json
└── HANDOFF_L*.md · CHECKPOINT_*.md
```

### File protetti — hash attesi

| file | sha256[:16] |
|---|---|
| `state.db` | `9125282973ddc8b9` |
| `glossary.csv` | `94e785f68be271d8` |
| `staging/inventory_fields.csv` | `c9d8bc651cd70c56` |
| `tools/l10n.py` | `743c6a3f8c217f35` |

Se uno cambia, **fermarsi**: `state.py` stampa la sezione `INTEGRITA'`.

## 2. Regole inviolabili

1. **Nessuna approvazione, nessun caricamento nel gioco.** Solo staging.
2. **Un'unità `APPROVED` non si riscrive**: si riproduce **alla lettera** dal campo `italian` di `state.db`.
3. **Misurare gli stati prima di tradurre** e **asserirlo** nel costruttore.
4. **Misurare la forma dei contesti**: uno per unità (L111, L112, L114); meno delle unità (L113 87/96, L115
   72/104, L116 80/133); missioni (L117 31/98, L118 33/104, L119 20/77); eventi (L120 3 contesti con uno da 37,
   L121 12, L122 18); **navi: un contesto per nave** (L123: 33 contesti per 54 unità, 18 da una sola).
5. **Quando il sorgente ripete, la resa ripete** e la ripetizione si dichiara (L122: 36 testi per 42 unità).
6. **File protetti**: i difetti si documentano, non si riparano.
7. **Numeri misurati, mai dedotti**: tipi, contesti, tab, virgolette, token, quadre si rimisurano sul `source.json`.
8. **Parti senza tab iniziali**; il `\t` lo antepone il costruttore, e il controllo conta le **unità** che
   iniziano con tab (L120: 41 su 52; L121: 28 su 56; L122: 21 su 42; L123: 14 su 54).
9. **`UI_LABEL`, `VALUE` e chiavi `Preferences` non si traducono**; **le virgolette di dialogo sì**, per unità.
10. **Un elenco vuoto è un'asserzione**: `VALUE`/token assenti (`== {}`), quadre assenti (`not [...]`).
11. **Un registro solo**: «tu» per il giocatore; la cortesia «lei» si corregge nel testo.
12. **Ogni sostituzione nei documenti va asserita** come occorrenza unica.
13. **EOL preservati**: i tre `CHECKPOINT_*.md` sono `CRLF`, gli `HANDOFF_*.md` sono `LF`.
14. **Gate di lunghezza 0,55-1,90**: si riscrive la resa, non si allarga il gate.
15. **Un documento superato si marca `OBSOLETO`**.

## 3. Stato misurato (19 ottobre 2026, dopo L122)

```
  data/_ui/tooltips.txt                        667/  667 unità (100.0%) ·  12084 EN ->  12495 IT · 6 lotti
  data/avgi/avgi 0 first contact.txt           406/  406 unità (100.0%) ·  12251 EN ->  11483 IT · 3 lotti
  data/avgi/avgi outfits.txt                    63/   63 unità (100.0%) ·   3126 EN ->   3328 IT · 6 lotti
  data/avgi/avgi ships.txt                     102/  102 unità (100.0%) ·   2528 EN ->   2669 IT · 6 lotti
  data/avgi/avgi side missions.txt             436/  436 unità (100.0%) ·  13233 EN ->  12621 IT · 2 lotti
  data/bunrodea/bunrodea missions.txt           77/   77 unità (100.0%) ·   2316 EN ->   2155 IT · 5 lotti
  data/coalition/coalition culture conversations.txt   157/  157 unità (100.0%) ·   9964 EN ->   9138 IT · 5 lotti
  data/coalition/coalition jobs.txt            197/  197 unità (100.0%) ·   3258 EN ->   3272 IT · 8 lotti
  data/coalition/coalition missions.txt       1580/ 1580 unità (100.0%) ·  48224 EN ->  46002 IT · 2 lotti
  data/coalition/heliarch intro.txt            663/  663 unità (100.0%) ·  21729 EN ->  20845 IT · 1 lotti
  data/coalition/lunarium intro.txt            730/  730 unità (100.0%) ·  29208 EN ->  28079 IT · 1 lotti
  data/gegno/gegno I corroboration.txt         298/  298 unità (100.0%) ·  10645 EN ->   9652 IT · 2 lotti
  data/gegno/gegno intro missions.txt          276/  276 unità (100.0%) ·  11323 EN ->  10179 IT · 3 lotti
  data/gegno/gegno outfits.txt                  60/   60 unità (100.0%) ·   2342 EN ->   2497 IT · 6 lotti
  data/hai/hai culture conversations.txt       147/  147 unità (100.0%) ·   5003 EN ->   4781 IT · 4 lotti
  data/hai/hai missions.txt                    823/  823 unità (100.0%) ·  23926 EN ->  22373 IT · 1 lotti
  data/hai/unfettered 0 prologue.txt           147/  147 unità (100.0%) ·   4057 EN ->   3667 IT · 7 lotti
  data/hai/unfettered side missions.txt        159/  159 unità (100.0%) ·   4418 EN ->   3994 IT · 3 lotti
  data/human/boarding missions.txt             240/  240 unità (100.0%) ·   4571 EN ->   4480 IT · 3 lotti
  data/human/campaign events.txt               150/  150 unità (100.0%) ·   6961 EN ->   6788 IT · 3 lotti
  data/human/culture conversations.txt         374/  374 unità (100.0%) ·  11269 EN ->  10858 IT · 10 lotti
  data/human/deep missions.txt                1355/ 1355 unità (100.0%) ·  38724 EN ->  36319 IT · 1 lotti
  data/human/free worlds 0 prologue.txt        703/  703 unità (100.0%) ·  18612 EN ->  17855 IT · 1 lotti
  data/human/free worlds 1 start.txt           663/  663 unità (100.0%) ·  21140 EN ->  20273 IT · 1 lotti
  data/human/free worlds 2 middle.txt          552/  552 unità (100.0%) ·  16290 EN ->  15323 IT · 1 lotti
  data/human/free worlds 3 checkmate.txt       482/  482 unità (100.0%) ·  16244 EN ->  15239 IT · 1 lotti
  data/human/free worlds 3 reconciliation.txt   596/  596 unità (100.0%) ·  21021 EN ->  20228 IT · 1 lotti
  data/human/free worlds 4 epilogue.txt        114/  114 unità (100.0%) ·   3487 EN ->   3209 IT · 1 lotti
  data/human/free worlds side plots.txt        211/  211 unità (100.0%) ·   5683 EN ->   5339 IT · 1 lotti
  data/human/free worlds war jobs.txt           72/   72 unità (100.0%) ·   1124 EN ->   1140 IT · 1 lotti
  data/human/human missions.txt               4253/ 4253 unità (100.0%) · 104495 EN ->  98511 IT · 6 lotti
  data/human/intro missions.txt                637/  637 unità (100.0%) ·  19451 EN ->  17681 IT · 1 lotti
  data/human/jobs.txt                          390/  390 unità (100.0%) ·   5823 EN ->   5969 IT · 1 lotti
  data/human/outfits.txt                        63/   63 unità (100.0%) ·   2373 EN ->   2381 IT · 5 lotti
  data/human/paradise world jobs.txt           131/  131 unità (100.0%) ·   2918 EN ->   3044 IT · 7 lotti
  data/human/pirate jobs.txt                   279/  279 unità (100.0%) ·   4780 EN ->   4735 IT · 3 lotti
  data/human/ships.txt                         103/  103 unità (100.0%) ·   5083 EN ->   5286 IT · 3 lotti
  data/human/weapons.txt                        90/   90 unità (100.0%) ·   3241 EN ->   3355 IT · 6 lotti
  data/incipias/incipias first contact.txt     161/  161 unità (100.0%) ·   4662 EN ->   4282 IT · 3 lotti
  data/kahet/kahet missions.txt               1738/ 1738 unità (100.0%) ·  66316 EN ->  60554 IT · 2 lotti
  data/korath/korath missions.txt              158/  158 unità (100.0%) ·   5268 EN ->   5103 IT · 5 lotti
  data/map planets.txt                        1544/ 1544 unità (100.0%) ·  83687 EN ->  83453 IT · 18 lotti
  data/quarg/quarg missions.txt                178/  178 unità (100.0%) ·   5417 EN ->   5184 IT · 4 lotti
  data/remnant/remnant 1 introduction.txt     1250/ 1250 unità (100.0%) ·  41087 EN ->  38140 IT · 1 lotti
  data/remnant/remnant 2 cognizance.txt        572/  572 unità (100.0%) ·  22761 EN ->  21522 IT · 1 lotti
  data/remnant/remnant 2 side missions.txt     299/  299 unità (100.0%) ·  10539 EN ->   9870 IT · 1 lotti
  data/sheragi/archaeology missions.txt        625/  625 unità (100.0%) ·  18966 EN ->  17522 IT · 1 lotti
  data/starts.txt                              113/  113 unità (100.0%) ·   4236 EN ->   4094 IT · 5 lotti
  data/successors/predecessors.txt              59/   59 unità (100.0%) ·    898 EN ->    927 IT · 5 lotti
  data/successors/successor 1 prologue.txt     345/  345 unità (100.0%) ·  11308 EN ->  11005 IT · 2 lotti
  data/successors/successor 2 ghosts aqrabe.txt   180/  180 unità (100.0%) ·   5147 EN ->   4942 IT · 4 lotti
  data/successors/successor 2 ghosts myurej.txt   211/  211 unità (100.0%) ·   6612 EN ->   6329 IT · 5 lotti
  data/successors/successor 2 ghosts.txt       680/  680 unità (100.0%) ·  18302 EN ->  17736 IT · 1 lotti
  data/successors/successor culture conversations.txt   114/  114 unità (100.0%) ·   4063 EN ->   3873 IT · 3 lotti
  data/successors/successor outfits.txt         56/   56 unità (100.0%) ·   2269 EN ->   2364 IT · 4 lotti
  data/successors/successor side missions.txt   164/  164 unità (100.0%) ·   4001 EN ->   3854 IT · 4 lotti
  data/wanderer/wanderers middle.txt           731/  731 unità (100.0%) ·  22378 EN ->  21188 IT · 1 lotti
  data/wanderer/wanderers start.txt            805/  805 unità (100.0%) ·  24166 EN ->  22753 IT · 1 lotti
  TOTALE staging: 28429 unità · 895008 EN · 851938 IT
```

- lotti con `translation.json` in staging: **199 directory** su 200 (la cartella `L19_20261017_201342/` è un
  artefatto storico senza `translation.json`: non conta);
- `verify.py` presenti: **197**, tutti verdi;
- database: **APPROVED 364 · PENDING 32560** · totale 32924, ultimo evento `2026-10-17T14:33:18Z`;
- unità `PENDING` di tipo `UI_LABEL` (label, non traducibili): 630 — **15** delle quali non ancora in staging;
- unità `PENDING` non ancora in staging in totale: **4.131**;
- unità realmente traducibili ancora da fare: **4.170** su **108 file** · parole inglesi: **82.096**;
- residuo traducibile: 3501 (formula di `state.py`; lo scarto con il misurato nasce dalle 630 label contate anche se
  già in staging e dalle 52 unità `APPROVED` contate come `PENDING`);
- `human missions.txt` completo in staging: **2141 unità / 51158 parole** dopo la riga 6428;
- **cinquantadue file completi**; cinquantadue file con almeno un lotto (misurato: ogni file aperto è stato chiuso);
- `endless-sky` HEAD **b4aa3bac3**, 0 modifiche.

Avanzamento: **28.429 / 32.924 unità (86,3%)** · **895.008 / 979.975 parole (91,3%)**.

### Lotti recenti · `sha256[:16]`

| lotto | file | righe | unità | EN → IT | controlli |
|---|---|---|---|---|---|
| L117 | `pirate jobs.txt` | 20–1624 | 98 | 1804 → 1715 | 29 / 38 |
| L118 | `pirate jobs.txt` | 1627–2955 | 104 | 1753 → 1774 | 28 / 38 |
| L119 | `pirate jobs.txt` | 2958–3706 | 77 | 1223 → 1246 | 31 / 31 |
| L120 | `campaign events.txt` | 28–242 | 52 | 2255 → 2193 | 32 / 29 |
| L121 | `campaign events.txt` | 282–1332 | 56 | 2486 → 2404 | 32 / 29 |
| **L122** | **`campaign events.txt`** | **1338–3468** | **42** | **2220 → 2191** | **32 / 30** |
| **L123** | **`ships.txt`** | **78–2044** | **54** | **2364 → 2483** | **29 / 29** |
| **L124** | **`ships.txt`** | **2102–3422** | **29** | **1539 → 1603** | **28 / 27** |
| **L125** | **`ships.txt`** | **3491–4266** | **20** | **1180 → 1200** | **28 / 29** |
| **L126** | **`incipias first contact.txt`** | **22–218** | **55** | **1788 → 1626** | **31 / 28** |
| **L127** | **`incipias first contact.txt`** | **224–331** | **63** | **1697 → 1556** | **30 / 28** |
| **L128** | **`incipias first contact.txt`** | **343–439** | **43** | **1177 → 1100** | **30 / 33** |
| **L129** | **`boarding missions.txt`** | **15–386** | **89** | **852 → 819** | **30 / 30** |
| **L130** | **`boarding missions.txt`** | **417–686** | **75** | **2087 → 2067** | **30 / 30** |
| **L131** | **`boarding missions.txt`** | **695–959** | **76** | **1632 → 1594** | **28 / 31** |
| **L132** | **`unfettered side missions.txt`** | **17–229** | **84** | **2055 → 1850** | **30 / 32** |
| **L133** | **`unfettered side missions.txt`** | **237–477** | **67** | **2007 → 1821** | **31 / 32** |
| **L134** | **`unfettered side missions.txt`** | **494–510** | **8** | **356 → 323** | **27 / 32** |
| **L135** | **`starts.txt`** | **18–130** | **32** | **1485 → 1448** | **29 / 29** |
| **L136** | **`starts.txt`** | **135–167** | **15** | **587 → 559** | **28 / 28** |
| **L137** | **`starts.txt`** | **172–210** | **17** | **802 → 786** | **29 / 28** |
| **L138** | **`starts.txt`** | **215–358** | **47** | **1356 → 1295** | **32 / 31** |
| **L139** | **`starts.txt`** | **365–366** | **2** | **6 → 6** | **21 / 22** |
| **L140** | **`unfettered 0 prologue.txt`** | **22–81** | **25** | **405 → 375** | **31 / 25** |
| **L141** | **`unfettered 0 prologue.txt`** | **83–132** | **20** | **591 → 566** | **30 / 25** |
| **L142** | **`unfettered 0 prologue.txt`** | **139–201** | **20** | **493 → 456** | **29 / 26** |
| **L143** | **`unfettered 0 prologue.txt`** | **214–317** | **30** | **723 → 643** | **30 / 25** |
| **L144** | **`unfettered 0 prologue.txt`** | **367–420** | **20** | **486 → 406** | **31 / 25** |
| **L145** | **`unfettered 0 prologue.txt`** | **423–459** | **13** | **703 → 635** | **32 / 27** |
| **L146** | **`unfettered 0 prologue.txt`** | **460–530** | **19** | **656 → 586** | **31 / 26** |
| **L147** | **`coalition jobs.txt`** | **16–293** | **30** | **437 → 412** | **28 / 27** |
| **L148** | **`coalition jobs.txt`** | **309–435** | **16** | **205 → 207** | **27 / 25** |
| **L149** | **`coalition jobs.txt`** | **455–634** | **18** | **246 → 268** | **31 / 25** |
| **L150** | **`coalition jobs.txt`** | **639–794** | **14** | **234 → 216** | **27 / 24** |
| **L151** | **`coalition jobs.txt`** | **799–1171** | **37** | **302 → 316** | **27 / 24** |
| **L152** | **`coalition jobs.txt`** | **1191–1359** | **21** | **527 → 531** | **25 / 24** |
| **L153** | **`coalition jobs.txt`** | **1360–1469** | **20** | **582 → 601** | **27 / 25** |

Hash: `L150 160a1592a36efff5` · `L151 8faf5d133a5b433c` · `L152 580b5869e9f95bed` ·
`L153 7b5d3d976e20fb6c` (batch).

### File completi (44)

`campaign events.txt` **150/150** (L120–L122) è l'ultimo chiuso: **6961 EN → 6788 IT** in tre lotti. Prima
`pirate jobs.txt` 279/279, `_ui/tooltips.txt` 667/667, `korath missions.txt` 158/158, e altri quaranta.
`starts.txt` è **chiuso** (113/113, 4236 EN → 4094 IT, cinque lotti); il file aperto è
`data/coalition/coalition jobs.txt` è aperto (**156/197, 79,2%**); `unfettered 0 prologue.txt` è **chiuso**
(147/147, cinque contesti).

## 4. Ultimi lotti chiusi

| lotto | file | righe | unità | EN → IT | check / verify | sha256[:16] |
|---|---|---|---|---|---|---|
| L189 | `gegno outfits.txt` | 1034–1130 | 12 | 443 → 472 | 23 / 21 | `ad29d24c33d43d52` |
| L190 | `gegno outfits.txt` | 1137 | 1 | 23 → 22 | 16 / 18 | `13766cd38ed4be40` |
| L191 | `bunrodea missions.txt` | 16–52 | 12 | 466 → 434 | 25 / 21 | `a1c782a568e872ed` |
| L192 | `bunrodea missions.txt` | 64–91 | 12 | 465 → 418 | 24 / 21 | `6a45d9d51cb156e7` |
| L193 | `bunrodea missions.txt` | 92–150 | 30 | 500 → 463 | 23 / 21 | `0ba103f679e3b8cc` |
| L194 | `bunrodea missions.txt` | 152–203 | 18 | 488 → 479 | 21 / 21 | `5b5071523577ff54` |
| L195 | `bunrodea missions.txt` | 207–219 | 5 | 397 → 361 | 20 / 17 | `a75a3d4708ee72a5` |

`gegno outfits.txt` **CHIUSO** (60/60); `bunrodea missions.txt` **CHIUSO** (77/77); file completi: **57**.

## 5. Prossimo lotto — L196 (apre `hai jobs.txt`)

```bash
python staging/editorial/tools/export_section.py "staging/editorial/L196_$(date +%Y%m%d)_$(date +%H%M%S)"   "data/hai/hai jobs.txt" 15 489
```

| voce | valore |
|---|---|
| File | `data/hai/hai jobs.txt` (175 unità · 2.302 parole · 71 `VALUE` + 75 `DESCRIPTION` + 6 `TEXT` + 23 `DIALOG`) |
| Righe | 15–489 |
| Unità | **39** |
| Parole | **499** |
| Contesti | **20** — da `Human Vacation [1]` a `Delivery to Human Space [2]` |
| Tab / virgolette | **0** / **6** |
| Tipi | **17 `VALUE`** · **16 `DESCRIPTION`** · **6 `TEXT`** |
| Token | **0** |
| Confine dopo | riga **492** apre `mission:Delivery to Human Space [2]` (una `DESCRIPTION`) |

Nuovo file, **20 contesti** in 39 unità: si torna al registro da **listino di lavori**. **17 `VALUE`** e **6 `TEXT`** da
copiare alla lettera, parentesi quadre comprese. Il file si chiuderà in **5 finestre** (L196…L200). Contratto verificato:
`HANDOFF_L196_20261019.md` (`FAIL: 0 / 21`).

## 6. Metodo per lotto (7 passi)

1. **Preflight**: `state.py` → `ESITO: OK`.
2. **Export**: `export_section.py <dir> <file> <riga_da> <riga_a>` (directory **prima** del percorso).
3. **Stati e forma**: contare `APPROVED`/`PENDING`, il `Counter(kind)`, i contesti e i gruppi; **asserirli**.
4. **Traduzione** in `parts/partNN.json` (niente tab), con asserzioni su virgolette, token, quadre, ripetizioni.
5. **`check.py`**: costruisce `translation.json`, verifica tipi, tab, virgolette, contesti, token, gate, tipografia.
6. **`verify.py`** indipendente: invariante di **segmento** (o di **file** se il lotto chiude il file), ricalcolando
   dal DB.
7. **Documenti** e checkpoint nello stesso turno; poi la batteria finale (`check_handoff.py` ×3, `state.py`, tutti i
   `verify.py`, `git status`).

### Comandi

```bash
python staging/editorial/tools/state.py
python staging/editorial/L123_*/check.py
python staging/editorial/L123_*/verify.py; echo "exit=$?"
python staging/editorial/tools/check_handoff.py HANDOFF_L123_20261019.md
python staging/editorial/tools/check_handoff.py CHECKPOINT_SESSIONE_20261018.md
python staging/editorial/tools/check_handoff.py CHECKPOINT_AGENTE_SESSIONE_20261018.md
ls -d staging/editorial/L*/translation.json | wc -l      # 126 oggi, 127 dopo L123
for f in staging/editorial/L*/verify.py; do python "$f" >/dev/null 2>&1 || echo "ROSSO $f"; done
```

## 7. Trappole misurate (non reimpararle)

1. **La forma dei contesti cambia da file a file**: uno per unità (L111, L112, L114); meno delle unità (L113, L115,
   L116); missioni (L117–L119); eventi (L120–L122); **navi: un contesto per nave** (L123, 33 per 54).
2. **La forma dei `kind` cambia dentro lo stesso file**: `campaign events` ha avuto 41 `MISSION_TEXT` + 2
   `LOGBOOK` (L120), poi 41 `DESCRIPTION` + 1 `UI_LABEL` (L121), poi 41 `DESCRIPTION` + 1 `MISSION_TEXT` (L122).
   `ships.txt` è 96 `DESCRIPTION` + 7 `VALUE`.
3. **I `VALUE` di un file di navi sono nomi propri al plurale** (`Argosies`, `Auxiliaries`, `Finches`, `Furies`):
   identici al sorgente, elencati nel `check.py`.
4. **Zero token è un'asserzione** (`== {}`), non un silenzio.
5. **I nomi propri inglesi dentro una frase italiana fanno fallire la scansione dei residui** (`The Parting
   Glass`): si neutralizzano **prima**, non si allenta il controllo.
6. **Le virgolette possono essere sbilanciate** (L121, unità 22 e 24): si riproduce e si verifica **quali** unità.
7. **Una `UI_LABEL` rompe due controlli se non è dichiarata** (L121): esclusa e verificata identica a parte.
8. **Le firme delle rese devono essere uniche**: `insist`, `militia`, `rogue planets down south`, `closest thing
   that the pirates` hanno tutti abortito il costruttore.
9. **I numeri in prosa non li controlla nessuno**: «N dopo la riga X» va misurato e corretto in tutti i documenti.
10. **La cella `Contesti` vuole il nome senza prefisso**, `Confine dopo` col prefisso; la riga `**N unità / M
    parole** dopo la riga X` deve esserci.
11. **`check_handoff.py` legge la PRIMA cella con quel nome**: nel documento di ripresa le tabelle del lotto chiuso
    e del prossimo convivono, quindi le chiavi del primo vanno qualificate (`Parole (L122)`).
12. **Un registro solo**: «tu»; la cortesia «lei» si corregge nel testo.
13. **Il gate respinge i testi corti**: minimo osservato 0,69 (L120), 0,86 (L122).
14. **La write-guard rifiuta la sovrascrittura** di un file letto in modo paginato: file nuovo o `patch`.
15. **A chiusura di un file cambiano i documenti in più punti**: copertura, file completi, lotti del file, forma del
    `verify.py` successivo.
16. **`cargo` è un prestito italiano**: «modulo cargo», «cassa cargo» non sono residui inglesi.
17. **`startswith` su unità con tab fallisce anche con pochi tab**: basta un'unità su cinque (la nota sui caccia di
    L123). Ogni asserzione di contenuto usa `.strip().startswith(...)`.
18. **Un file di navi non ripete come un file di lavori**: 48 testi distinti su 54 unità, e le uniche ripetizioni
    sono la stessa nota tecnica (5 volte) e il plurale del nome (`Auxiliaries`, 3 volte).
19. **Un segmento può non avere ripetizioni**: in L124 29 testi per 29 unità. Il gruppo di confronto, quando
    esiste, è quello con il lotto precedente (le due note tecniche di L123).
20. **Un solo `VALUE` va elencato, non escluso**: `VAL == [18]` con il testo atteso.
21. **La cella `Contesti` toglie solo il prefisso prima del primo `:`**: `mission:Incipias: Warning of the
    Guardian` si scrive **`Incipias: Warning of the Guardian`**. Il checker usa `split(':', 1)[1]`.
22. **Un file senza `VALUE` non toglie le asserzioni**: zero `VALUE`, zero token e zero quadre vanno scritti come
    `not [...]` / `== {}`, altrimenti un errore passa inosservato proprio dove non c'è niente da confrontare.
23. **Un lotto con un solo contesto**: la cella `Contesti` vuole primo e ultimo fra backtick e il checker esige
    almeno quattro backtick, quindi si scrive `da X a X`.
24. **Due testi di cui uno è prefisso dell'altro** (le voci di diario 18 e 22 di L126) fanno scattare due firme: si
    risolvono con una mappa `EXACT` per testo completo, dichiarata.
25. **Due registri nello stesso file** vanno verificati con parole-spia proprie (Guardiano arcaico, Quarg
    cerimoniale), altrimenti un appiattimento futuro passa inosservato.
26. **Un controllo di cortesia con `\b(Le|Lei|Suo…)`** boccia «Le tue intenzioni» e «Le stelle»: l'articolo `Le`
    non è il pronome. Si cercano `Lei/lei` e i possessivi maiuscoli **in mezzo alla frase**, e il `voi` plurale
    («Vi saluto», gli Incipias sono una folla) non è cortesia.
27. **La coda di un file si dichiara `fine file`** nella cella `Confine dopo`: il checker verifica che dopo la riga
    finale non ci siano unità.
28. **Un file chiuso si conta dalla somma dei lotti** (55 + 63 + 43 = 161): `sovrapposti = 0` senza il conteggio
    non dimostra niente, e una riga scoperta deve far scattare «file coperto 161/161».
29. **Una ripetizione fra lotti** si **rilegge** dal `translation.json` precedente e si confronta, invece di
    ricopiarla a memoria.
30. **`\blei\b` non è cortesia**: «su di lei» parla della nave. La cortesia si cerca con la maiuscola.
31. **`residuo traducibile` compare due volte nell'handoff** (stato e trappole): vanno aggiornate entrambe.
32. **I frammenti di frase hanno lo spazio finale dentro il testo**: conservarlo unità per unità, o la frase
    composta perde le parole.
33. **Con frammenti brevi le firme sono ambigue** (`to ` dentro `in order to `): la resa si indicizza per indice e la
    coerenza si controlla a posteriori con «stesso inglese ⇒ stessa resa».
34. **Le unità che non sono testo** in un file di frasi: template `${...}` delle `conversation` e nomi di frase citati
    da `phrase`. Elencarli e verificarli identici, altrimenti il gioco si rompe.
35. **Due frammenti di sola punteggiatura** identici per necessità vanno dichiarati, o «tutte tradotte» li boccia.
36. **Un lotto può non avere `VALUE` né `UI_LABEL`**: la cella si scrive `0 = 0` e la lista si verifica `== []`,
    altrimenti il «tutto verde» non ha controllato niente.
37. **Le varianti della stessa scena** condividono lunghi testi: le parti comuni si rendono con **costanti** e restano
    identiche parola per parola, altrimenti il confronto tra varianti diventa impossibile.
38. **`residuo traducibile` non si calcola a memoria**: nel passaggio L129→L130 il valore atteso era **4779**, non
    4801 — e il `check_handoff.py` lo ha bocciato.
39. **Una costante può oscurare un dizionario** (`ENG` stringa sopra `ENG` dizionario): l'asserzione sulle chiavi
    fallisce con «unità» che sono i caratteri della stringa. Rinominare la costante.
40. **Un file chiuso si conta dalla somma dei lotti** (89 + 75 + 76 = 240): un totale che non torna è una riga
    scoperta o un lotto duplicato.
41. **Le virgolette possono essere decine** (89 in 84 unità): si contano per unità e si riproducono doppie.
42. **I nomi di luogo restano nomi**: `Hai-home` non si traduce, e il controllo **vieta** la forma tradotta.
43. **Una resa identica legittima va dichiarata**: `(No.)` → `(No.)` in `ID_OK` con un controllo suo.
44. **Le virgolette si distribuiscono**: 43 senza, 33 con 2, 5 con 4, 3 con 1. Il totale da solo non rivela una
    battuta chiusa per sbaglio.
45. **Le misure si prendono dal DB prima di scriverle**: in L132 un numero stimato (`4608`) è stato bocciato dal
    `check_handoff.py` che ne ha misurato **4619**.
46. **Un'incoerenza del sorgente si riproduce e si verifica due volte**: diario «cibo», testo «forniture mediche».
47. **Quattro virgolette dispari possono avere conteggi diversi** (1, 1, 3, 1): si confronta la sequenza.
48. **Un lotto di 8 unità non si verifica con un `check.py` da 67**: i numeri attesi si misurano sull'export.
49. **Le sezioni dei checkpoint si sostituiscono per span di heading** (`## 4.` → `## 6.`), non con regex
    `.*?(?=\n## 5\. )`: quella forma dipende da uno spazio finale e fallisce in silenzio.
51. **Tre asserzioni vuote insieme** (`VALUE`, `UI_LABEL`, token): scriverle è l'unico modo per distinguere «niente
    da controllare» da «controllo mancato».
52. **Il trattino lungo non passa la tipografia**: si riscrive la frase con una virgola, non si allarga il controllo.
53. **La cella `Contesti` vuole la forma «bare»**: il checker toglie il prefisso prima del **primo** due punti, quindi
    `conversation:deep intro` → `deep intro`; il nome intero si aggiunge fra parentesi.
54. **Un `VALUE` può essere il nome di una modalità di gioco** (`starts.txt`: `Endless Sky`, `Deep Desire`): resta
    identico, e la tassonomia dei file di missioni non vale qui.
55. **Un blocco può triplicarsi se il testo nuovo contiene quello vecchio**: la guardia «salta se `a` non c'è» non
    scatta. Si genera con una `marker` sul testo nuovo e si deduplica per blocco.
56. **La convenzione numerica si cambia solo dove è lecito**: `480.000`/`0,4%` sì, e un controllo vieta le forme
    inglesi (`480,000`, `0.4%`) perché un separatore sbagliato è un errore silenzioso.
57. **`distinti` dentro il lotto ≠ `nuovi` rispetto ai lotti**: servono due misure, la seconda contro i
    `translation.json` precedenti; la resa delle condivise si **rilegge**, non si ricopia.
58. **Due `VALUE` identici sono due inizi**: `Hai Origins` alle righe 215 e 227, lista esatta di due coppie.
59. **La cortesia di un personaggio non è quella della narrazione**: si conta (≤1), non si vieta.
60. **Due inizi con lo stesso nome vogliono due controlli**: la lista di coppie dice «sono due», un secondo
    controllo dice «dicono cose diverse sullo sblocco».
61. **Le battute aperte si lasciano aperte**: la resa non deve **finire** con una virgoletta; chiuderla è
    un'invenzione e il controllo la intercetta.
62. **Un nome identico si dichiara**: lista `ID_OK` con controllo proprio, non esclusione dai controlli.
63. **Tab e backtick possono stare nel `raw` e non nel testo**: «0 tab» è la risposta giusta, e va asserita.
64. **Confrontare percorsi con separatori misti non trova niente**: normalizzare con `os.path.abspath`.
65. **Un testo ripetuto in due rami della missione è un vincolo**: stesse parole, o il giocatore legge due
    storie diverse per la stessa scelta.
66. **Un motto ripetuto è una costante**: verificata con `count` sull'intero lotto, non a occhio.
67. **Una sgrammaticatura del sorgente resta**: ripulirla è una scelta dell'autore, non del traduttore.
68. **Una voce identica si rilegge, una variante si riscrive**: due casi diversi, due trattamenti.
69. **Una `VALUE` a metà lotto**: dentro il lotto è l'unità 1, nel file è la riga 139.
70. **Un «N dopo» si calcola per sottrazione** (totale − prima − finestra): in L142 era 81 invece di 82.
71. **`(No.)` identico e `(Yes.)` tradotto**: due scelte vicine, due trattamenti; un controllo unico sbaglia.
72. **Due missioni corte possono stare in un lotto**: ognuna si chiude, e il `verify.py` lo verifica due volte.
73. **Un token si verifica per simbolo e per unità**: due segnaposto in due unità diverse danno un totale pari anche
    se scambiati di posto.
74. **Un token-suffisso si incolla al nome** (`Hai<hood>` → «Slegato`<hood>`»), un token a inizio frase regge la
    maiuscola che segue.
75. **Un segnaposto che contiene una frase si confronta esatto**: `<The engineer>` con `.lower()` sarebbe un altro
    simbolo.
76. **Le virgolette aperte dal sorgente non si chiudono**: disparità riprodotta, nessuna virgoletta finale
    aggiunta, segno finale uguale all'inglese.
77. **Un lotto che chiude il file scrive `Confine dopo` = «fine file»**: il checker ha un ramo terminale apposta.
78. **Un token con parentesi si confronta intero**: `<as before (run)>` non si spezza.
79. **Un file può avere inventario vuoto di testo**: `news.txt` ha 164 unità su 202 che sono il delimitatore
    `` `"` `` e 1.356 righe di frase assenti dal DB. Prima di aprire un lotto si verifica che le unità siano testo.
80. **La parità dei token si fa in tre modi**: multiset, ordine per unità, conteggi nominati per i simboli corti.
81. **Un `ck(..., True)` non è un controllo**: se non può fallire, va rimosso.
82. **Il controllo dei residui inglesi esclude i `VALUE`**: sono inglesi per contratto.
83. **Due simboli con lo stesso conteggio rendono il multiset cieco**: serve l'ordine per unità.
84. **Le coppie `VALUE`+`DESCRIPTION` si tengono intere**: si allunga la finestra di una unità invece di tagliare.
85. **«Quasi la stessa frase» non è la stessa frase**: `on <planet>` contro `on the <planet>` — resa diversa, e il
    riuso si nega con un'asserzione sulla chiave inglese.
86. **In batch si traduce per stringa, non per unità**: mappa `(kind, english) -> italiano`; le copie non divergono.
87. **Un lotto troppo grande si taglia al confine che non spezzi una coppia** `VALUE`+`DESCRIPTION`.
88. **Una finestra che finisce a un numero tondo taglia i contesti**: le righe 172–194 sono solo lo `start`, la scena
    inizia alla 195; il taglio si prende alla fine del contesto.
89. **Un handoff superato si marca `OBSOLETO`**; oggi: `HANDOFF_L98`…`L150` (L151–L153 non emessi: batch).

45. **La tabella «prossimo lotto» deve contenere la cella `File`.** Senza quella cella `check_handoff.py` ricade su
   `human missions.txt` e verifica **un altro file**: il sintomo e' un FAIL su `contesti` e `confine dopo` con
   contesti che non esistono nel lotto (successo con L173: `mission:Hallucination`, riga 1415, 5 FAIL su tre
   documenti). La cella `Contesti` va inoltre nella forma `**N** — da `mission:X` a `mission:Y``: la forma
   abbreviata `[0..2]` non viene letta. Verifica: `python staging/editorial/tools/check_handoff.py <documento>`.
   La cella `Contesti` va scritta **senza** il prefisso del contesto (`Koryfi`, non `ship:Koryfi`): il checker
   toglie il prefisso dal lato database e **non** dal documento, quindi la forma con prefisso fallisce pur
   essendo identica a occhio (visto in L174).

## 8. Glossario attivo (scelte già applicate)

| EN | IT | nota |
|---|---|---|
| **Endless Sky · Deep Desire · Birthday Surprise · Escaping Squalor · Hai Origins** | nomi degli inizi (`VALUE`): identici | L135–L138 |
| **Benga Atomic Thruster · Biroo Atomic Steering** | nomi di equipaggiamento fra virgolette: identici | L139 |
| **Hai · Slegati · scimmia** | `Hai` invariato; `Unfettered` → Slegati nei testi; `monkey` → scimmia | L140–L141 |
| **jump drive · wormhole · popoli-drago** | `jump drive` → motore di salto; `wormhole` invariato; `dragonfolk` → popoli-drago | L141 |
| **hyperdrive · (No.) · (Yes.)** | `hyperdrive` → iperpropulsore; `(No.)` identico; `(Yes.)` → «(Sì.)» | L142–L143 |
| **scavengers · carrion-feeders · by right** | **sciacalli** · **divoratori di carogne** · **di diritto** | L143 |
| **outfitter · <hood> · <learned>** | **fornitore**; `<hood>` incollato; `<learned>` a inizio frase | L144 |
| **<The engineer> · virgolette aperte** | token esatto (case-sensitive); le dispari restano aperte | L145 |
| **UI_LABEL · token con parentesi** | label identiche al sorgente; `<as before (run)>` intero | L146 |
| **news.txt** | **fuori bersaglio**: 164/202 unità sono `` `"` `` | L146 |
| **15 VALUE inglesi (jobs)** | nomi di lavoro: identici, token compreso | L147 |
| **parità token** | multiset + ordine per unità + conteggi nominati | L147 |
| **`<destination>` vs `<planet>`** | dest. di missione vs mondo di consegna; assenze incrociate | L148 |
| **frase «quasi uguale»** | `on <planet>` ≠ `on the <planet>`: resa nuova, riuso negato | L149 |
| **inversione Arach/Saryd** | si conserva: è la voce della specie | L152–L153 |
| **`on site` / `on the site`** | «sul posto» / «sul luogo», rese diverse | L153 |
| **resa per stringa** | mappa (kind, english) → italiano nei lotti ripetitivi | L151 |
| **Tripulse Shredder · Blaster · Ion Cannon** | nomi inglesi, mai tradotti | L145 |
| **Deep · Dirt Belt** | nomi di regione: restano inglesi (266 e 27 occorrenze) | L88–L135 |
| **Jump Drive · Lightning Bug · Anomalocaris** | nomi di moduli e modelli: restano inglesi | L131–L134 |
| **Veri Hai · scimmia · cessate il fuoco** | `True Hai · monkey · ceasefire` | L133 |
| **fuori uso · spoglie · tangente** | `disabled · spoils · bribe` | L133 |
| **figura incappucciata · relitto del passato · pilota automatico** | `hooded figure · relic of the past · autopilot` | L132 |
| **Hai-home · Anomalocaris · Korath** | invariati (nomi propri) | L132 |
| **scafo · alimentazione · valvola secondaria · refrigerante** | `hull · power · secondary valve · coolant` | L131 |
| **sovratensione · cacciatori di relitti · eroe d'azione** | `powersurge · derelict hunters · action hero` | L131 |
| **spilorcio · zotici · lezione imparata** | `cheapskate · bumpkins · paying for a lesson learned` | L130 |
| **nave negriera · paratia · arma da fianco** | `slave ship · bulkhead · sidearm` | L130 |
| **sapendo che · hai cambiato rotta · hai rischiato la vita** | `Knowing that · you altered course · you risked your life` | L129 |
| **per · al fine di · così che potessi** | `to · in order to · so that you could` | L129 |
| **ti dà · ti offre · ti ricompensa con** | `gives you · offers you · rewards you with` | L129 |
| **giorno-momento · protettore-di-vite · calamità-meteo** | `day-moment · life-protector · weather-calamity` | L128 |
| **capi-governatori · domande-quesiti · ponte-stellare** | `leader-governers · question-queries · star-bridge` | L128 |
| **questo uno** | `this one` (terza persona del Quarg) | L102, L127 |
| **viaggiatore-di-mondi · intenzione-scopo · stazione-capitale** | `world-traveler · intention-goal · capital-station` | L127 |
| **essere-esterno · pianeta-d'aria · luoghi-sistema** | `outer-being · air-planet · system-places` | L127 |
| **fiori non nati · viaggiatore · guardiano di questo spazio** | `unborn flowers · traveler · guardian of this space` | L126 |
| **vagabondaggi · peregrinare · intervallo minimo** | `wanderings · perambulate · trifling interval` | L126 |
| **gradienti di colore · richiesta di collegamento** | `color gradients · hail request` | L126 |
| **container portacaccia · pod** | `fighter-carrying containers · pod` | L125 |
| **transatlantico di lusso · vibrazioni soniche** | `luxury liner · sonic vibrations` | L125 |
| **Cintura Principale del Sol · Nucleo** | `Sol Main Belt · Core` | L125 |
| **bracci di attracco per caccia · piattaforma sensoristica mobile** | `fighter docking arms · mobile sensor platform` | L124 |
| **lanciamissili · lanciatori di missili · generatore di scudi** | `missile boat · missile launchers · shield generator` | L124 |
| **rapporto durabilità-costo · propulsori inversi** | `durability to cost ratio · reverse thrusters` | L124 |
| **piattaforma sensoristica mobile** | `mobile sensor platform` | L124 |
| **baia di caccia · baia per droni** | `fighter bay · drone bay` | L123 |
| **portatrice · portatrice leggera** | `carrier · light carrier` | L123 |
| **nave da guerra · nave capitale** | `warship · capital ship` | L123 |
| **matrice di scudi · alloggiamento per torretta · portello del cannone** | `shield matrix · turret mount · gun port` | L123 |
| **nave-città · carovana di merci · cuccette** | `city-ship · freight caravan · bunks` | L123 |
| **Interference Plating · Q-ship · Proton Gun** | invariati (equipaggiamenti) | L123 |
| **Memoriale di Guerra dei Mondi Liberi** | `Free Worlds War Memorial` | L122 |
| **nomi dei caduti · pareti di granito** | `names of the fallen · granite walls` | L122 |
| **maschere antipolvere · particolato** | `dust masks · particulate matter` | L122 |
| **colonia penale** | `prison colony` | L122 |
| **guazzabuglio di piccole strutture metalliche** | `hodgepodge…` | L122 |
| **alghe rodofite** | `rhodophyte algae` | L122 |
| **scudi deflettori · area ristorazione · carrelli elettrici** | `deflector shields · food court · electric carts` | L122 |
| **polpetta** · **organizzazioni che vendevano protezione** | `meat patty` · `protection rackets` | L122 |
| **The Parting Glass** | invariato | L122, taverna |
| **Bordo Meridionale** | `Southern Rim` | L121–L122 |
| **emporio · new stock** | `outfitter` · `UI_LABEL` invariata | L121 |
| **Vecchio Porto / Il Porto / Porto Nuovo / L'Ampliamento** | `Old Port / The Port / New Port / The Expansion` | L121 |
| **Oathkeepers della Marina · Conservatorio dei Mondi Liberi** | `Navy Oathkeepers · Free Worlds Conservatory` | L121 |
| **Smuggler's Den · la stazione Grendel** | idem | L121 |
| **Mike's Mustelids · donnole · furetti · ghiottoni** | idem | L121 |
| **il Giorno del Ricordo** | `Remembrance Day` | L120 |
| **gli Alphas** | `the Alphas` | specie, invariata |
| **i Mondi Liberi** | `the Free Worlds` | L120 |
| **Arsenale della Marina della Repubblica** | `Republic Navy Yard` | L120 |
| **la Borsa Galattica** | `Galactic Stock Exchange` | L120 |
| **squadrone di navi portatrici** | `Carrier squadron` | L120 |
| **ufficiale di collegamento · ospedale da campo · brandine** | `liaison officer · field hospital · cots` | L120 |
| **Paradisiani · bacheche dei lavori** | `Paradisians · job boards` | L120 |
| **anarchia · signore della guerra** | `anarchy · warlord` | L118–L119 |
| **Marina · Sindacato · milizia · predoni** | `Navy · Syndicate · militia · Marauders` | L118 |
| **compenso · una parte del bottino** | `bounty payment · cut of the loot` | L118 |
| **entro `<date>` · entro `<day>`** | `by <date> · by <day>` | senza articolo |
| **baie · navi portatrici · navi trasportate** | `bays · carriers · carried ships` | L115 |
| **flotta · scorte · ammiraglia** | `fleet · escorts · flagship` | L115 |
| **sovrapposizioni di stato · angoli morti** | `status overlays · blindspots` | L115–L116 |
| **regola di gioco · nave personaggio · morte permanente** | `gamerule · person ship · permadeath` | L116 |
| **robustezza dello scafo · messa fuori uso · riparazioni** | `hull strength · disabled · repairs` | L111–L112 |
| **emporio · cantiere · deposito planetario** | `outfitter · shipyard · planetary storage` | L113 |
| **iperguida · motore di salto · ramscoop** | `hyperdrive · jump drive · ramscoop` | L112, invariato |
| **detrito · bottino** | `flotsam · plunder` | L111–L112 |
| **registro dei tooltip** | **«tu»** | fissato dalle 52 unità approvate |
| **chiavi e valori di `Preferences`** | invariati, fra virgolette | L115–L116 |
| Quarg · Drak · Korath · Hai · Pug · Wanderer | invariati | specie |
| spaceport / landing pad / port authority | **spazioporto / piazzola di atterraggio / autorità portuale** | L91 |

I nomi di nave, arma ed equipaggiamento **restano in inglese** (decisione 259); **i nomi di missione e di carico**
restano in inglese (decisione L103): nei file di lavori sono i `VALUE`. Il giocatore è «voi» nella narrazione e
nei dialoghi, **«tu» nei tooltip**.

## 9. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione e nessun caricamento**: 27.802 unità in staging, tutte `PENDING`.
- **Nessun test di gameplay**: la verifica è testuale, a exit code. **Nessuna nave, evento o missione è stata vista
  nel gioco.**
- **`campaign events.txt` è chiuso in staging, non nel gioco**: 150 unità tradotte, zero caricate.
- **`unfettered 0 prologue.txt` è chiuso in staging (147/147), zero nel gioco**: nessuna unità caricata, nessuna
  missione giocata.
- **`Bordo Meridionale`** è una scelta di glossario (L121), non una verifica.
- **Otto righe di diario** senza testo italiano (L45 195/305/357/418, L46 62, L47 54, L68 23, L75 27).
- **La campagna è all'84,4%**: 116 file con unità residue, 4.797 unità / 101.660 parole.
- **Nessuna revisione umana**: nessun lotto è stato approvato da una persona.

## 10. Mappa dei documenti

| documento | stato | a cosa serve |
|---|---|---|
| questo file | **valido** | ripresa a freddo, numeri correnti |
| `CHECKPOINT_SESSIONE_20261018.md` | **valido** | storia dei lotti, metodo, trappole, glossario (CRLF) |
| `CHECKPOINT_EDITORIALE.md` | **valido** | decisioni editoriali e tabella dei lotti (CRLF, **non** in formato handoff) |
| `HANDOFF_L154_20261019.md` | **valido** | contratto del prossimo lotto, verificato da `check_handoff.py` |
| `HANDOFF_L150_20261019.md` | **OBSOLETO** | contratto del lotto chiuso |
| `HANDOFF_L151`…`L153` | **non emessi** | batch: contratto = piano del batch |
| `HANDOFF_L149`…`L98` | **OBSOLETO** | idem |
| `CHECKPOINT_AGENTE_20261018.md` | **OBSOLETO** | versione ferma a L68 |
