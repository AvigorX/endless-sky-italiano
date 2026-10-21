# CHECKPOINT SESSIONE — Endless Sky IT · 2026-10-18 (aggiornato a L153 chiuso)

**Questo è il documento da leggere per primo in una sessione nuova.** Contiene tutto ciò che serve per
riprendere senza la cronologia della chat: dove siamo, cosa è chiuso, come si lavora, quali trappole sono
già state pagate, e qual è il prossimo comando da lanciare.

Sostituisce la versione precedente dello stesso nome (ferma a L32) e **integra**
`HANDOFF_L154_20261019.md`, che resta il contratto formale verificato da `check_handoff.py`. Se un numero
di questo documento non torna con il workspace, **vince il workspace**: il documento va rigenerato, non
aggiustato a mano.

Verifica di questo file:

```bash
cd ~/PROGETTI/G-DEV/GAME-SOURCE-LAB/endless-sky-l10n
python staging/editorial/tools/check_handoff.py CHECKPOINT_SESSIONE_20261018.md   # atteso: exit 0, FAIL: 0
```

---

## 0. In una riga

Stiamo traducendo in italiano, a mano e a lotti, i testi di **Endless Sky** dentro `staging/editorial/`.
Nessuna approvazione nel database, nessun caricamento nel gioco: solo staging verificato con exit code.
**Batch L150–L153**: quattro lotti in `data/coalition/coalition jobs.txt`, **72 unità**, **1.645 parole** inglesi.
L150 (turisti, 14 unità) distingue `bring them to` da `bring them **home** to`; L151 (37 unità, ma **14 testi**) usa una
**mappa per stringa inglese** perché le 8 copie di Cargo/Bulk restino una resa sola; L152 (21 unità) porta il cambio di
carattere — `MISSION_TEXT` e `LOGBOOK` — e **l'inversione dell'Arach** («Enormemente prezioso è…»); L153 (20 unità)
raddoppia l'inversione con il Saryd e distingue `on site` da `on the site` («sul posto» / «sul luogo»). Il file è al
**79,2%** (156/197): restano **41 unità**, e **L154 chiude il file**.

## 1. Ambiente e percorsi

| voce | valore |
|---|---|
| Workspace | `C:/Users/Dave/PROGETTI/G-DEV/GAME-SOURCE-LAB/endless-sky-l10n` (`~` in bash = `C:/Users/Dave`) |
| Repo del gioco (sola lettura) | `../endless-sky`, HEAD `b4aa3bac3`, `git status` vuoto |
| Shell | bash MSYS su Windows; i path nativi vanno passati come `C:/...`, non `/c/...` |
| Python | `python` (3.14.7) disponibile come comando; `python3` no |
| Database | `state.db` (SQLite), **sempre** aperto `mode=ro` |
| Staging | `staging/editorial/L*_<YYYYmmdd>_<HHMMSS>/` |
| Tool | `staging/editorial/tools/{state.py, export_section.py, next_section.py, check_handoff.py, protected.sha256}` |
| Scratch | `C:/Users/Dave/AppData/Local/hermes/profiles/game/cache/scratch/` (contiene `build_part.py`, `recon_lot.py`, `l33/partNN.json`) |

Il workspace **non è un repository git**: la persistenza è affidata ai documenti (questo, `CHECKPOINT_EDITORIALE.md`,
gli handoff) e ai file su disco. Non c'è `git revert`: un lotto sbagliato si ricostruisce dalle parti.

### File che non si toccano (hash registrati: se cambiano, fermarsi)

| file | sha256[:16] |
|---|---|
| `state.db` | `9125282973ddc8b9` |
| `glossary.csv` | `94e785f68be271d8` |
| `staging/inventory_fields.csv` | `c9d8bc651cd70c56` |
| `tools/l10n.py` | `743c6a3f8c217f35` |

---

## 2. Stato misurato del workspace (19 ottobre 2026)

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
  TOTALE staging: 31341 unità · 961693 EN · 918875 IT
```

- **336 directory** con `translation.json`; **334** di esse hanno `verify.py` (`L19_20261017_201342/` resta un
export scartato). **`L1` e `L2` (17 ottobre) non hanno
  `verify.py`**: precedono la regola dei due script e non si riscrivono.
- Database: **APPROVED 364 · PENDING 32560** su 32.924 unità; ultimo evento `2026-10-17T14:33:18Z`.
- Unità `PENDING` di tipo `UI_LABEL` (non traducibili): 630, delle quali **15** non ancora in staging
  (misurato: `58` nella stesura precedente era arretrato).
- residuo traducibile: 589 (formula di `state.py`); valore **misurato**: **1.336 unità / 17.799 parole** su
  **101 file** (unità `PENDING` non `UI_LABEL` assenti da ogni `translation.json`).
- `data/human/human missions.txt` è completo (4.253/4.253): **2141 unità / 51158 parole** dopo la riga 6428, già tradotte.
- **Sessantaquattro file interamente tradotti** su 167 percorsi (65 contando `deep jobs.txt`, che ha
  l'ultima unità `UI_LABEL` non traducibile: 186 su 187); i chiusi di recente sono `data/hai/hai jobs.txt`
  (**175/175**, L196–L200), **`data/hai/hai outfits.txt` (65/65, L201–L205)** e **`data/coalition/coalition news.txt`
  (112/112, L206–L211)**.
  **`successor ships.txt` è chiuso 146/146** (L218–L222). **`remnant outfits.txt` è chiuso 57/57** (L223–L227).
  **`data/korath/korath outfits.txt` è CHIUSO 92/92** (L228–L232): tab 0 (L228) → 3 (L229) → 7 (L230) → 0 (L231) →
  **4** (L232). In L231 due nuovi nomi di scena (**Quarg**, **Efreti**); in L232 il primo lotto di sola prosa
  (**0 identiche / 10 tradotte**). **`data/avgi/avgi news.txt` è CHIUSO a 115/115** (L233–L238, sei lotti): notizie con citazione intera, un lotto di
  sola composizione (6 prefissi × 7 messaggi), la lacuna dichiarata dei 13 blocchi `word`, un refuso del sorgente
  (`Frustation.`) tradotto nel senso e non replicato, e l'**etichetta di modalità** nelle sue tre posizioni: in testa,
  in coda (L236) e a metà frase (L238).

## 3. Lotti chiusi e ultimi numeri

| lotto | file | righe | unità | EN → IT | verify |
|---|---|---|---|---:|---|
| L27 | `kahet missions.txt` | 39–3048 | 917 | 35.520 → 32.640 | 25 controlli |
| L28 | `kahet missions.txt` | 3051–5297 | 821 | 30.796 → 27.914 | 24 controlli |
| L29 | `hai missions.txt` | 23–2696 | 823 | 23.926 → 22.373 | 25 controlli |
| L30 | `lunarium intro.txt` | 21–2111 | 730 | 29.208 → 28.079 | 25 controlli |
| L31 | `heliarch intro.txt` | 16–2140 | 663 | 21.729 → 20.845 | 25 controlli |
| L32 | `wanderers start.txt` | 23–3092 | 805 | 24.166 → 22.753 | 26 controlli |
| L33 | `wanderers middle.txt` | 22–3601 | 731 | 22.378 → 21.188 | 27 controlli |
| L34 | `free worlds 0 prologue.txt` | 16–2502 | 703 | 18.612 → 17.855 | 27 controlli |
| L35 | `free worlds 1 start.txt` | 16–2343 | 663 | 21.140 → 20.273 | 27 controlli |
| L36 | `free worlds 2 middle.txt` | 16–2336 | 552 | 16.290 → 15.323 | 27 controlli |
| L37 | `free worlds 3 checkmate.txt` | 16–2463 | 482 | 16.244 → 15.239 | 28 controlli |
| L38 | `free worlds 3 reconciliation.txt` | 31–2729 | 596 | 21.021 → 20.228 | 29 controlli |
| L39 | `free worlds 4 epilogue.txt` | 22–341 | 114 | 3.487 → 3.209 | 29 controlli |
| L40 | `free worlds side plots.txt` | 18–888 | 211 | 5.683 → 5.339 | 29 controlli |
| L41 | `free worlds war jobs.txt` | 16–927 | 72 | 1.124 → 1.140 | 30 controlli |
| L42 | `remnant 2 cognizance.txt` | 16–1747 | 572 | 22.761 → 21.522 | 33 controlli |
| L43 | `remnant 2 side missions.txt` | 17–775 | 299 | 10.539 → 9.870 | 33 controlli |
| L44 | `archaeology missions.txt` | 16–1718 | 625 | 18.966 → 17.522 | 37 controlli |
| L45 | `successor 2 ghosts.txt` | 37–2167 | 680 | 18.302 → 17.736 | 39 controlli |
| L46 | `successor 1 prologue.txt` | 24–664 | 221 | 7.180 → 6.973 | 37 controlli |
| L47 | `successor 1 prologue.txt` | 680–1024 | 124 | 4.128 → 4.032 | 38 controlli |
| L48 | `avgi side missions.txt` | 26–499 | 180 | 5.627 → 5.297 | 40 controlli |
| L49 | `avgi side missions.txt` | 524–1117 | 256 | 7.606 → 7.324 | 38 controlli |
| L50 | `avgi 0 first contact.txt` | 22–402 | 119 | 4.399 → 4.139 | 47 controlli |
| L51 | `avgi 0 first contact.txt` | 413–869 | 152 | 4.314 → 3.971 | 45 controlli |
| L52 | `avgi 0 first contact.txt` | 873–1120 | 135 | 3.538 → 3.373 | 44 controlli |
| L53 | `gegno intro missions.txt` | 17–230 | 89 | 4.287 → 3.896 | 41 controlli |
| L54 | `gegno intro missions.txt` | 280–676 | 159 | 5.975 → 5.274 | 41 controlli |
| L55 | `gegno intro missions.txt` | 677–954 | 28 | 1.061 → 1.009 | 40 controlli |
| L56 | `gegno I corroboration.txt` | 29–904 | 171 | 5.671 → 5.138 | 40 controlli |
| L57 | `gegno I corroboration.txt` | 943–1287 | 127 | 4.974 → 4.514 | 41 controlli |
| L58 | `culture conversations.txt` | 25–209 | 43 | 1.610 → 1.532 | 35 controlli |
| L59 | `culture conversations.txt` | 225–423 | 42 | 1.475 → 1.402 | 35 controlli |
| L60 | `culture conversations.txt` | 437–495 | 31 | 661 → 626 | 36 controlli |
| L61 | `culture conversations.txt` | 511–552 | 26 | 394 → 355 | 35 controlli |
| L62 | `culture conversations.txt` | 566–611 | 30 | 674 → 681 | 36 controlli |
| L63 | `culture conversations.txt` | 624–711 | 37 | 1.087 → 1.025 | 36 controlli |
| L64 | `culture conversations.txt` | 723–810 | 42 | 1.652 → 1.598 | 36 controlli |
| L65 | `culture conversations.txt` | 819–920 | 43 | 1.666 → 1.676 | 36 controlli |
| L66 | `culture conversations.txt` | 930–1053 | 45 | 1.239 → 1.176 | 36 controlli |
| **L67** | **`culture conversations.txt`** | **1062–1122** | **35** | **811 → 787** | **38 controlli** |
| **L68** | **`successor 2 ghosts myurej.txt`** | **16–113** | **49** | **1.502 → 1.447** | **46 controlli** |
| **L69** | **`successor 2 ghosts myurej.txt`** | **118–197** | **31** | **687 → 704** | **46 controlli** |
| **L70** | **`successor 2 ghosts myurej.txt`** | **215–307** | **39** | **1.028 → 953** | **48 controlli** |
| **L71** | **`successor 2 ghosts myurej.txt`** | **311–401** | **42** | **1.632 → 1.546** | **45 controlli** |
| **L72** | **`successor 2 ghosts myurej.txt`** | **407–531** | **50** | **1.763 → 1.679** | **46 controlli** |
| **L73** | **`successor 2 ghosts aqrabe.txt`** | **23–158** | **51** | **1.330 → 1.281** | **47 controlli** |
| **L74** | **`successor 2 ghosts aqrabe.txt`** | **161–255** | **38** | **1.106 → 1.077** | **44 controlli** |
| **L75** | **`successor 2 ghosts aqrabe.txt`** | **259–400** | **61** | **1.889 → 1.796** | **47 controlli** |
| **L76** | **`successor 2 ghosts aqrabe.txt`** | **404–478** | **30** | **822 → 788** | **49 controlli** |
| **L77** | **`successor side missions.txt`** | **17–220** | **63** | **1.909 → 1.829** | **45 controlli** |
| **L78** | **`successor side missions.txt`** | **224–325** | **53** | **1.109 → 1.060** | **39 controlli** |
| **L79** | **`successor side missions.txt`** | **336–381** | **29** | **620 → 611** | **36 controlli** |
| **L80** | **`successor side missions.txt`** | **416–453** | **19** | **363 → 354** | **36 controlli** |
| **L81** | **`predecessors.txt`** | **17–196** | **22** | **106 → 106** | **34 controlli** |
| **L82** | **`predecessors.txt`** | **208–381** | **15** | **220 → 220** | **32 controlli** |
| **L83** | **`predecessors.txt`** | **446–520** | **11** | **153 → 166** | **27 controlli** |
| **L84** | **`predecessors.txt`** | **534–608** | **4** | **169 → 177** | **22 controlli** |
| **L85** | **`predecessors.txt`** | **648–782** | **7** | **250 → 258** | **29 controlli** |
| **L86** | **`successor outfits.txt`** | **19–235** | **21** | **1021 → 1042** | **24 controlli** |
| **L87** | **`successor outfits.txt`** | **251–409** | **13** | **572 → 591** | **24 controlli** |
| **L88** | **`successor outfits.txt`** | **429–560** | **10** | **329 → 343** | **24 controlli** |
| **L89** | **`successor outfits.txt`** | **574–647** | **12** | **347 → 388** | **25 controlli** |
| **L90** | **`successor culture conversations.txt`** | **23–142** | **34** | **1098 → 1014** | **26 controlli** |
| **L91** | **`successor culture conversations.txt`** | **155–229** | **34** | **1117 → 1084** | **28 controlli** |
| **L92** | **`successor culture conversations.txt`** | **230–351** | **46** | **1848 → 1775** | **29 controlli** |
| **L93** | **`coalition culture conversations.txt`** | **24–66** | **31** | **1744 → 1616** | **27 controlli** |
| **L94** | **`coalition culture conversations.txt`** | **81–133** | **36** | **2321 → 2115** | **28 controlli** |
| **L95** | **`coalition culture conversations.txt`** | **148–190** | **27** | **1382 → 1242** | **29 controlli** |
| **L96** | **`coalition culture conversations.txt`** | **192–234** | **27** | **2248 → 2023** | **29 controlli** |
| **L97** | **`coalition culture conversations.txt`** | **251–462** | **36** | **2269 → 2142** | **29 controlli** |
| **L98** | **`hai culture conversations.txt`** | **1–105** | **39** | **1262 → 1180** | **28 controlli** |
| **L99** | **`hai culture conversations.txt`** | **106–211** | **38** | **1183 → 1151** | **28 controlli** |
| **L100** | **`hai culture conversations.txt`** | **212–320** | **44** | **1587 → 1512** | **28 controlli** |
| **L101** | **`hai culture conversations.txt`** | **321–386** | **26** | **971 → 938** | **29 controlli** |
| **L102** | **`quarg missions.txt`** | **1–117** | **48** | **1675 → 1632** | **27 controlli** |
| **L103** | **`quarg missions.txt`** | **118–249** | **42** | **956 → 882** | **28 controlli** |
| **L104** | **`quarg missions.txt`** | **250–334** | **27** | **631 → 597** | **27 controlli** |
| **L105** | **`quarg missions.txt`** | **335–506** | **61** | **2155 → 2073** | **31 controlli** |
| **L106** | **`korath missions.txt`** | **1–120** | **25** | **854 → 833** | **29 controlli** |
| **L107** | **`korath missions.txt`** | **121–212** | **38** | **1742 → 1683** | **30 controlli** |
| **L108** | **`korath missions.txt`** | **216–335** | **36** | **737 → 730** | **36 controlli** |
| **L109** | **`korath missions.txt`** | **338–451** | **33** | **1205 → 1188** | **33 controlli** |
| **L110** | **`korath missions.txt`** | **474–580** | **26** | **730 → 669** | **35 controlli** |
| **L111** | **`_ui/tooltips.txt`** | **16–328** | **104** | **1810 → 1848** | **28 controlli** |
| **L112** | **`_ui/tooltips.txt`** | **331–688** | **120** | **1813 → 2044** | **33 controlli** |
| **L113** | **`_ui/tooltips.txt`** | **691–973** | **96** | **1808 → 1864** | **38 controlli** |
| **L114** | **`_ui/tooltips.txt`** | **976–1309** | **110** | **1816 → 1905** | **41 controlli** |
| **L115** | **`_ui/tooltips.txt`** | **1312–1566** | **104** | **1819 → 1839** | **47 controlli** |
| **L116** | **`_ui/tooltips.txt`** | **1569–1865** | **133** | **3018 → 2995** | **47 controlli** |
| **L117** | **`pirate jobs.txt`** | **20–1624** | **98** | **1804 → 1715** | **38 controlli** |
| **L118** | **`pirate jobs.txt`** | **1627–2955** | **104** | **1753 → 1774** | **38 controlli** |
| **L119** | **`pirate jobs.txt`** | **2958–3706** | **77** | **1223 → 1246** | **31 controlli** |
| **L120** | **`campaign events.txt`** | **28–242** | **52** | **2255 → 2193** | **29 controlli** |
| **L121** | **`campaign events.txt`** | **282–1332** | **56** | **2486 → 2404** | **29 controlli** |
| **L122** | **`campaign events.txt`** | **1338–3468** | **42** | **2220 → 2191** | **30 controlli** |
| **L123** | **`ships.txt`** | **78–2044** | **54** | **2364 → 2483** | **29 controlli** |
| **L124** | **`ships.txt`** | **2102–3422** | **29** | **1539 → 1603** | **27 controlli** |
| **L125** | **`ships.txt`** | **3491–4266** | **20** | **1180 → 1200** | **29 controlli** |
| **L126** | **`incipias first contact.txt`** | **22–218** | **55** | **1788 → 1626** | **28 controlli** |
| **L127** | **`incipias first contact.txt`** | **224–331** | **63** | **1697 → 1556** | **28 controlli** |
| **L128** | **`incipias first contact.txt`** | **343–439** | **43** | **1177 → 1100** | **33 controlli** |
| **L129** | **`boarding missions.txt`** | **15–386** | **89** | **852 → 819** | **30 controlli** |
| **L130** | **`boarding missions.txt`** | **417–686** | **75** | **2087 → 2067** | **30 controlli** |
| **L131** | **`boarding missions.txt`** | **695–959** | **76** | **1632 → 1594** | **31 controlli** |
| **L132** | **`unfettered side missions.txt`** | **17–229** | **84** | **2055 → 1850** | **32 controlli** |
| **L133** | **`unfettered side missions.txt`** | **237–477** | **67** | **2007 → 1821** | **32 controlli** |
| **L134** | **`unfettered side missions.txt`** | **494–510** | **8** | **356 → 323** | **32 controlli** |
| **L135** | **`starts.txt`** | **18–130** | **32** | **1485 → 1448** | **29 controlli** |
| **L136** | **`starts.txt`** | **135–167** | **15** | **587 → 559** | **28 controlli** |
| **L137** | **`starts.txt`** | **172–210** | **17** | **802 → 786** | **28 controlli** |
| **L138** | **`starts.txt`** | **215–358** | **47** | **1356 → 1295** | **31 controlli** |
| **L139** | **`starts.txt`** | **365–366** | **2** | **6 → 6** | **22 controlli** |
| **L140** | **`unfettered 0 prologue.txt`** | **22–81** | **25** | **405 → 375** | **25 controlli** |
| **L141** | **`unfettered 0 prologue.txt`** | **83–132** | **20** | **591 → 566** | **25 controlli** |
| **L142** | **`unfettered 0 prologue.txt`** | **139–201** | **20** | **493 → 456** | **26 controlli** |
| **L143** | **`unfettered 0 prologue.txt`** | **214–317** | **30** | **723 → 643** | **25 controlli** |
| **L144** | **`unfettered 0 prologue.txt`** | **367–420** | **20** | **486 → 406** | **25 controlli** |
| **L145** | **`unfettered 0 prologue.txt`** | **423–459** | **13** | **703 → 635** | **27 controlli** |
| **L146** | **`unfettered 0 prologue.txt`** | **460–530** | **19** | **656 → 586** | **26 controlli** |
| **L147** | **`coalition jobs.txt`** | **16–293** | **30** | **437 → 412** | **27 controlli** |
| **L148** | **`coalition jobs.txt`** | **309–435** | **16** | **205 → 207** | **25 controlli** |
| **L149** | **`coalition jobs.txt`** | **455–634** | **18** | **246 → 268** | **25 controlli** |
| **L150** | **`coalition jobs.txt`** | **639–794** | **14** | **234 → 216** | **24 controlli** |
| **L151** | **`coalition jobs.txt`** | **799–1171** | **37** | **302 → 316** | **24 controlli** |
| **L152** | **`coalition jobs.txt`** | **1191–1359** | **21** | **527 → 531** | **24 controlli** |
| **L153** | **`coalition jobs.txt`** | **1360–1469** | **20** | **582 → 601** | **25 controlli** |

L134 chiuso il 2026-10-19 — terzo e ultimo lotto di `data/hai/unfettered side missions.txt`, che **chiude il
file**: `check.py` → `FAIL totale: 0` (**27 controlli**); `verify.py` → exit 0, **32 controlli**; `sha256[:16]` =
`L134 173cf3edac2a3208`. 2 parti (4+4), **1 contesto** e **8 testi distinti**. Tipi: **8 `MISSION_TEXT`**, con **tre
asserzioni vuote** (`VALUE`, `UI_LABEL`, token). **7 unità con tab**, **13 virgolette** con **una sola nell'unità 6**.
L'**invariante di file** somma i tre lotti e dimostra **159/159**, sovrapposti 0, `max(line)` 510. La tipografia ha
bocciato il primo giro (trattino lungo in unità 6 → virgola). `Jump Drive` e `Lightning Bug` restano nomi inglesi.
Numeri di dettaglio in `staging/editorial/L134_20261019_125428/{review,REPORT,STATO}.md`.

L133 chiuso il 2026-10-19 — secondo lotto di `data/hai/unfettered side missions.txt`: `check.py` →
`FAIL totale: 0` (**31 controlli**); `verify.py` → exit 0, **32 controlli**; `sha256[:16]` =
`L133 c214c835e561be8e`. 3 parti (23+22+22), **2 contesti** (10 / 57) e **64 testi distinti**. Tipi: **50
`MISSION_TEXT`**, **9 `DIALOG`**, **2 `VALUE`**, **2 `DESCRIPTION`**, **2 `LOGBOOK`**, **2 `UI_LABEL`**. **98
virgolette** con distribuzione **18 / 44 / 1 / 3 / 1** e quattro unità dispari (47, 48, 64, 65) rese con `[1, 1, 3,
1]`; **34 unità con tab**, **8 token in 6 famiglie** con `<date>` e `<system>` per la prima volta. Un'incoerenza del
sorgente **riprodotta**: il diario parla di `food shipment`, il testo di `medical supplies`. Contenuto: la consegna con
l'Anomalocaris e i suoi tre esiti, poi **Mera** l'ingegnere, la sfida pubblica, le regole implicite del capo, i tre
forfait e il duello. Numeri di dettaglio in
`staging/editorial/L133_20261019_124700/{review,REPORT,STATO}.md`.

L132 chiuso il 2026-10-19 — primo lotto di `data/hai/unfettered side missions.txt`: `check.py` →
`FAIL totale: 0` (**30 controlli**); `verify.py` → exit 0, **32 controlli**; `sha256[:16]` =
`L132 4fcdf80f4d1d3888`. 3 parti (28x3), **2 contesti** (18 / 66) e **82 testi distinti**. Tipi: **78 `MISSION_TEXT`**,
**3 `UI_LABEL`**, **1 `DESCRIPTION`**, **1 `DIALOG`**, **1 `LOGBOOK`**, **zero `VALUE`**. **89 virgolette** in 84
unità con **tre unità a una sola** (57, 62, 73), **74 unità con tab**, **8 token in 4 famiglie**. Due scelte
dichiarate: `Hai-home` resta nome proprio; `(No.)` → `(No.)` è una resa identica elencata in `ID_OK`. Contenuto: il
giovane Hai che diserta, la scritta dentro l'involucro del tributo, poi la figura incappucciata nel cantiere, la
stazione sotterranea, la spiaggia, la nave che emerge dal mare e l'**Anomalocaris** nella grotta. Numeri di dettaglio
in `staging/editorial/L132_20261019_124026/{review,REPORT,STATO}.md`.

L131 chiuso il 2026-10-19 — terzo e ultimo lotto di `data/human/boarding missions.txt`, che **chiude il file**:
`check.py` → `FAIL totale: 0` (**28 controlli**); `verify.py` → exit 0, **31 controlli**; `sha256[:16]` =
`L131 ec991eb6a0c3f258`. 3 parti (26+25+25), **2 contesti** (1 / 75) e **52 testi distinti** su 76 unità — **24
ripetizioni**, il massimo finora. Tipi: **75 `MISSION_TEXT`**, **1 `DESCRIPTION`**, **zero `VALUE`**, **zero
`UI_LABEL`** (due asserzioni vuote scritte). **74 unità con tab**, **2 virgolette** (unità 60, `"astronavi ostili"`),
**22 token in 2 famiglie**. Le frasi di riparazione sono **costanti** nel costruttore e il controllo verifica le
occorrenze (4 + 4); una collisione di nomi (`ENG` costante contro `ENG` dizionario) è stata corretta in `ENG_REP`.
L'**invariante di file** legge i tre lotti e dimostra **240/240**, sovrapposti 0, `max(line)` 959. Contenuto: lo scafo
abbandonato, le tre riparazioni con i loro successi e disastri, le tre corse al portello, la trappola dei pirati e il
virus che svuota il conto. Numeri di dettaglio in
`staging/editorial/L131_20261019_123356/{review,REPORT,STATO}.md`.

L130 chiuso il 2026-10-19 — secondo lotto di `data/human/boarding missions.txt`: `check.py` → `FAIL totale: 0`
(**30 controlli**); `verify.py` → exit 0, **30 controlli**; `sha256[:16]` = `L130 53f6d41b0bfedb6c`. 3 parti (25x3),
**4 contesti** (1 / 1 / 6 / 67) e **74 testi distinti** su 75 unità. Tipi: **50 `MISSION_TEXT`**, **22 `UI_LABEL`**
(elencate una per una e verificate identiche), **1 `CONVERSATION`**, **1 `DESCRIPTION`**, **1 `DIALOG`**, **zero
`VALUE`** — due asserzioni vuote scritte. **45 unità con tab**, **31 virgolette** (unità 21 con **tre**), **19 token in
5 famiglie**. Contenuto: la cassa di gettoni di credito, l'autodistruzione della nave pirata, l'ammutinamento con i
superstiti, e **Tarquin** sulla nave negriera, con le quattro strade e i loro esiti. Le tre varianti d'ingresso (11, 13,
15) condividono un lungo testo reso con costanti comuni, così il confronto tra varianti resta leggibile. Numeri di
dettaglio in `staging/editorial/L130_20261019_122807/{review,REPORT,STATO}.md`.

L129 chiuso il 2026-10-19 — primo lotto di `data/human/boarding missions.txt`, che **apre il file**:
`check.py` → `FAIL totale: 0` (**30 controlli**); `verify.py` → exit 0, **30 controlli**; `sha256[:16]` =
`L129 fee796a7a3f4f2bd`. 3 parti (30+30+29), **18 contesti** e **80 testi distinti** su 89 unità. Tipi: **48
`TEXT`**, **21 `MISSION_TEXT`**, **6 `CONVERSATION`**, **6 `VALUE`**, **6 `DESCRIPTION`**, **2 `DIALOG`**. I 48 `TEXT`
sono **frammenti** di una frase che il gioco compone a caso, e il lotto introduce l'invariante degli **spazi iniziali
e finali identici** (89/89): senza, la frase perde le parole. **Quattro unità non sono testo** (2 template `${...}`, 2
nomi di frase) e restano identiche, più 2 frammenti di sola punteggiatura e 6 `VALUE`. **43 token in 7 famiglie**, **22
unità con tab**, **10 virgolette**. Due difetti del sorgente **riprodotti**: il frammento `the` senza spazio finale e la
frase sgrammaticata per costruzione. Sei frammenti riscritti per rientrare nel gate 0,55–1,90, **non allargato**.
Numeri di dettaglio in `staging/editorial/L129_20261019_121941/{review,REPORT,STATO}.md`.

L128 chiuso il 2026-10-19 — terzo e ultimo lotto di `data/incipias/incipias first contact.txt`, che **chiude il
file**: `check.py` → `FAIL totale: 0` (**30 controlli**); `verify.py` → exit 0, **33 controlli**; `sha256[:16]` =
`L128 2efab055b9515fde`. 3 parti (15+14+14), **3 contesti** (2 / 1 / 40) e **43 testi distinti**. Tipi: **33
`MISSION_TEXT`**, **4 `UI_LABEL`** (`has incipias ship`, `initial choice`, `odd question`, `end no time`,
**identiche**), **3 `LOGBOOK`**, **1 `DIALOG`**, **1 `VALUE`** (`Bring Incipias back to <planet>`, identico **token
compreso**), **1 `DESCRIPTION`**. **30 unità con tab**, **43 virgolette** di cui **tre unità con una sola** (28, 30,
36: battute non chiuse dal sorgente), **6 token** in **5 famiglie** su cinque unità. L'**invariante di file** legge i
tre lotti e dimostra **161/161**, sovrapposti 0, `max(line)` 439. Una voce di diario (unità 2) ripete quella di L127
unità 24: la resa è **riletta** dal `translation.json` precedente e confrontata. Contenuto: la discesa nel gigante
gassoso, il salvataggio dei cinque Incipias, i capi-governatori degli Hicemus e le domande sul mondo-origine.
Numeri di dettaglio in `staging/editorial/L128_20261019_074634/{review,REPORT,STATO}.md`.

L127 chiuso il 2026-10-19 — secondo lotto di `data/incipias/incipias first contact.txt`, che prende **tutto** il
contesto `Help The Stranded 1`: `check.py` → `FAIL totale: 0` (**30 controlli**); `verify.py` → exit 0, **28
controlli**; `sha256[:16]` = `L127 d811d1921f891627`. 3 parti (21+21+21), **un solo contesto** per 63 unità e **63
testi distinti** (nessuna ripetizione). Tipi: **58 `MISSION_TEXT`**, **3 `LOGBOOK`**, **1 `VALUE`** (`Seek help from
the Incipias`, **identico** al sorgente), **1 `DESCRIPTION`**. **55 unità con tab**, **98 virgolette** (nessuna unità
dispari), **2 token** (`<first>`, `<last>`) **nella sola unità 38**. Due marche di stile **verificate**: i composti con
trattino degli Incipias (`intenzione-scopo`, `stazione-capitale`, `essere-esterno`, `viaggiatore-di-mondi`,
`pianeta-d'aria`, `luoghi-sistema`) e la terza persona del Quarg («questo uno», 7 occorrenze), che convive con il
plurale dei Quarg collettivi. Contenuto: la richiesta di aiuto, il divieto di dare tecnologia, il traduttore nella
scatola d'argento, il primo messaggio, i tubi pieni di nebbia della stazione e le domande degli Incipias. **Errore di
misura corretto**: le unità dopo la riga 331 sono **43** (161 − 55 − 63), non 39 — patch a `verify.py` e ai tre
documenti a contratto. Numeri di dettaglio in `staging/editorial/L127_20261019_073900/{review,REPORT,STATO}.md`.

L126 chiuso il 2026-10-19 — primo lotto di `data/incipias/incipias first contact.txt`, che **apre il file più
pesante che resta**: `check.py` → `FAIL totale: 0` (**31 controlli**); `verify.py` → exit 0, **28 controlli**;
`sha256[:16]` = `L126 c928bf1d8815cac5`. 3 parti (19+19+17), **6 contesti** (23 / 13 / 13 / 2 / 2 / 2) e **52 testi
distinti** per 55 unità (3 coppie ripetute). Tipi: **48 `MISSION_TEXT`**, **4 `UI_LABEL`** (`ut divitas`, `spec
inci`, `both planets`, `new species`, **identiche** al sorgente ed escluse da «tutte tradotte»), **3 `LOGBOOK`**.
**37 unità con tab**, **65 virgolette** (unità 23 con **tre**, una in più nel sorgente), **zero token** asserito. Due
registri **verificati** nel controllo: il Guardiano alto e arcaico («pura follia», «qui giacciono», «viaggiatore») e i
Quarg cerimoniali («peregrinare», «vagabondaggi», «autorizzato»). Contenuto: l'avvertimento del Guardiano e i «fiori
non nati», la presenza nei sistemi Dom'us e Hui'uc, il primo contatto a suon di fruscio, la visita ai Quarg e il
relitto con i cinque polpi-medusa. Numeri di dettaglio in
`staging/editorial/L126_20261019_073300/{review,REPORT,STATO}.md`.

L125 chiuso il 2026-10-19 — terzo e ultimo segmento di `data/human/ships.txt`, che **chiude il file**: `check.py` →
`FAIL totale: 0` (**28 controlli**); `verify.py` → exit 0, **29 controlli**, invariante **di file** (**103/103**
righe coperte, `sovrapposti = 0`, `max(line) = 4266`); `sha256[:16]` = `L125 e2309e1d7fee3d39`. 2 parti (10+10),
**15 contesti** (10×1, 5×2) e **20 testi distinti**; **1 nota** (droni) ripresa da L123/L124 e confrontata. Tipi:
**20 `DESCRIPTION`**, **nessun `VALUE`**; **5 unità con tab**, **14 virgolette** (6 + 2 + 6 nelle unità 1, 6, 7),
**zero token** e **zero quadre**, asseriti. Contenuto: le portatrici civili Roost e Skein, le navi da guerra Saber,
Splinter, Vanguard e Valkyrie, le piccole Scoutship, Shuttle, Sparrow, Wasp e Scrapper, il CT-50 Star Barge, la
Sunder, il Surveillance Drone e la Star Queen. Numeri di dettaglio in
`staging/editorial/L125_20261019_072624/{review,REPORT,STATO}.md`.

L124 chiuso il 2026-10-19 — secondo segmento di `data/human/ships.txt`: `check.py` → `FAIL totale: 0` (**28
controlli**); `verify.py` → exit 0, **27 controlli**; `sha256[:16]` = `L124 5b6c5456b299d979`. 2 parti (15+14),
**24 contesti** (19×1, 5×2) e **29 testi distinti** per 29 unità. Tipi: **28 `DESCRIPTION`**, **1 `VALUE`**
(`Modified Argosies`, plurale, identico al sorgente). **3 unità con tab** (9, 12, 17), **14 virgolette** (unità 8, 9,
10, 20, 23, 26), **zero token** e **zero quadre** asseriti. Le due note tecniche (caccia e droni) sono **le stesse
di L123** e la resa è confrontata. Contenuto: Gunboat, Lance, Monitor e Rainmaker per la Marina; Hauler, Hauler II,
Hauler III, Mule e Nest per il carico; Mining Drone; Jackal, Mammoth, Modified Argosy e Nighthawk per pirati e
contrabbandieri; Hawk, Headhunter, Heavy Shuttle, Hogshead, Leviathan, Manta, Osprey, Protector, Quicksilver e Raven
per i civili. Numeri di dettaglio in `staging/editorial/L124_20261019_071927/{review,REPORT,STATO}.md`.

L123 chiuso il 2026-10-19 — primo lotto di `data/human/ships.txt`, che **apre il file più pesante che resta**:
`check.py` → `FAIL totale: 0` (**29 controlli**); `verify.py` → exit 0, **29 controlli**; `sha256[:16]` =
`L123 dce934d804256232`. 3 parti (18×3), **33 contesti** (18×1, 11×2, 3×3, 1×5) e **48 testi distinti** per 54
unità. Tipi: **48 `DESCRIPTION`**, **6 `VALUE`** — `Argosies`, `Auxiliaries` ×3, `Finches`, `Furies`, **identici**
al sorgente perché sono nomi di nave al plurale (decisione 259). **14 unità con tab**, **16 virgolette** (unità 13,
21, 27, 36, 42), **zero token** e **zero quadre**, asseriti. Contenuto: portatrici e capitali (Aerie, Bactrian,
Carrier, Dreadnought), caccia e droni (Barb, Boxwing, Combat Drone, Dagger, Dropship, Finch), navi da carico (Bulk
Freighter, Container Transport, Class C «Freighter»), navi della Marina (Auxiliary, Bastion, Corvette, Cruiser,
Enforcer, Frigate), civili e pirati (Argosy, Arrow, Blackbird, Courier, Cutthroat, Falcon, Flivver, Fury). Numeri
di dettaglio in `staging/editorial/L123_20261019_071206/{review,REPORT,STATO}.md`.

L122 chiuso il 2026-10-19 — terzo e ultimo segmento di `campaign events.txt`, che **chiude il file**: `check.py`
→ `FAIL totale: 0` (**32 controlli**); `verify.py` → exit 0, **30 controlli**, invariante **di file** (**150/150**
righe coperte, `sovrapposti = 0`); `sha256[:16]` = `L122 3ff793b7a7ed6422`. 3 parti (14×3), **18 contesti** (8×2,
4×1, 4×4, 2×3) e **36 testi distinti** per 42 unità, di cui **3 già resi in L120/L121** (5 unità condivise, rese
identiche verificate). Tipi: **41 `DESCRIPTION`**, **1 `MISSION_TEXT`**; **21 unità con tab**, **8 virgolette**
(unità 19, 21, 32), **zero token** e **zero quadre**, entrambi **asseriti**. Contenuto: il memoriale di Deep nei
tre stadi, New Iceland e la base abbandonata, la colonia penale di Clink, Poisonwood e la taverna «The Parting
Glass», Bloodsea in tre versioni, Albatross, Covert e il cartello minerario, Geminus ricostruita, Martini e il
vecchio spazioporto in rovina. Numeri di dettaglio in
`staging/editorial/L122_20261019_070623/{review,REPORT,STATO}.md`.

L121 chiuso il 2026-10-19 — secondo segmento di `campaign events.txt`: `check.py` → `FAIL totale: 0` (**32
controlli**); `verify.py` → exit 0, **29 controlli**; `sha256[:16]` = `L121 292f0d3b327b16f9`. 3 parti
(19+19+18), **12 contesti** (15 / 10 / 5 / 4×3 / 3×2 / 2×4) e **52 testi distinti** per 56 unità, con **4 coppie**
ripetute. Tipi: **41 `DESCRIPTION`**, **14 `MISSION_TEXT`**, **1 `UI_LABEL`** (`new stock`, **identica** al
sorgente e verificata in un controllo suo). **28 unità con tab**, **46 virgolette** (le unità 22 e 24 ne hanno una
sola, come il sorgente), **1 token** (`<origin>`). Contenuto: schieramento della Marina su Ingot, New Wales e New
Austria, l'emporio Central Outfitters con la merce di Kraz e Delta V, Zug e «L'Ampliamento», Kornephoros e Clink,
Farpoint e gli Oathkeepers, il Conservatorio dei Mondi Liberi, Thule, e Greenrock in tre versioni (occupata,
abbandonata, recuperata) con «Mike's Mustelids». Numeri di dettaglio in
`staging/editorial/L121_20261019_065925/{review,REPORT,STATO}.md`.

L120 chiuso il 2026-10-19 — primo lotto di `campaign events.txt`, che **apre il file più pesante che resta**:
`check.py` → `FAIL totale: 0` (**32 controlli**); `verify.py` → exit 0, **29 controlli**; `sha256[:16]` =
`L120 a4f3e6160ea73524`. 3 parti (18+18+16), **3 contesti** (6 / 9 / **37** unità) e **45 testi distinti** per 52
unità, con **7 coppie** che ripetono l'inglese (le risposte del giocatore e un paragrafo di cronaca). Tipi: **41
`MISSION_TEXT`**, **9 `DESCRIPTION`**, **2 `LOGBOOK`**, **zero `VALUE`** — il controllo dei nomi di missione è
un'asserzione vuota, dichiarata. **41 unità su 52 iniziano con tab** (qui il tab è la norma), **58 virgolette** di
dialogo tradotte, **5 token** (`<ship>` 4, `<planet>` 1). Contenuto: Giorno del Ricordo e gli Alphas, l'Arsenale di
Geminus e la Borsa su Martini, Bourne e i Mondi Liberi, l'ultimatum, l'ufficiale che caccia il giocatore, la scena
di Martini e l'arresto con la licenza revocata. Numeri di dettaglio in
`staging/editorial/L120_20261019_065236/{review,REPORT,STATO}.md`.

L119 chiuso il 2026-10-19 — terzo e ultimo lotto di `pirate jobs.txt`, che **chiude il file**: `check.py` →
`FAIL totale: 0` (**31 controlli**); `verify.py` → exit 0, **31 controlli**, invariante **di file**
(**279/279** righe coperte, `sovrapposti = 0`); `sha256[:16]` = `L119 51189eab238776c8`. 4 parti
(20+20+20+17), **20 contesti** (19 da quattro unità, **uno da una sola**: `outfit:Secret Cargo`) e **47 testi
distinti** per 77 unità: **4 nomi identici** (`Merchants near <system>`, `Defend <planet>`, `Convoy near
<system>`, `Assassinate a political target`) e **43 testi prosaici**, di cui **2 già resi in L118**. Tipi: **32
`DIALOG`**, **17 `DESCRIPTION`**, **16 `VALUE`**, **12 `CONVERSATION`** — quest'ultimo nuovo per la campagna
recente: tre scene con **9 unità che iniziano con tab** e **6 virgolette** nelle battute d'apertura. **106 token**
in sei famiglie (`<planet>` 28, `<payment>` 23, `<destination>` 19, `<system>` 14, `<npc>` 12, `<day>` 10).
Contenuto: razzie ai mercantili del Sud, tre difese pirata (Marina, Sindacato, milizia) con scena di scelta, furti
di carico segreto in tre regioni, sei assassinii politici. Numeri di dettaglio in
`staging/editorial/L119_20261019_064438/{review,REPORT,STATO}.md`.

L118 chiuso il 2026-10-19 — secondo lotto di `pirate jobs.txt`: `check.py` → `FAIL totale: 0` (**28 controlli**);
`verify.py` → exit 0, **38 controlli**; `sha256[:16]` = `L118 31bb9438bee96230`. 4 parti (26 × 4), **33 contesti**
(19 con quattro unità, 14 con due) e **39 testi distinti** per 104 unità: **11 nomi identici** e **28 testi
prosaici**, di cui **3 già resi in L117** e ripresi dal suo `translation.json` (8 unità condivise, tutte
identiche). Tipi: **36 `DIALOG`**, **33 `VALUE`**, **33 `DESCRIPTION`**, **2 `MISSION_TEXT`**; **192 token** in
**nove** famiglie (`<planet>` 53, `<payment>` 52, `<destination>` 33, `<system>` 33, `<day>` 17, `<npc>` 9,
`<date>` 9, `<bunks>` 5, `<cargo>` 2); **zero virgolette**, asserito. Contenuto: criminale galattico Core e Sud,
trasporto di schiavi (cinque missioni), mercenari e scorte in tre regioni, eliminazione di Marina, Sindacato e
milizia, eliminazione di bande rivali e predoni, razzie ai mercantili. Numeri di dettaglio in
`staging/editorial/L118_20261019_063903/{review,REPORT,STATO}.md`.

L117 chiuso il 2026-10-19 — primo lotto di `pirate jobs.txt`: `check.py` → `FAIL totale: 0` (**29 controlli**);
`verify.py` → exit 0, **38 controlli**; `sha256[:16]` = `L117 6ed8bb0de3875183`. 3 parti (33+33+32), **31
contesti** (26 da tre unità, 5 da quattro) e **26 testi distinti** per 98 unità: la ripetizione è del sorgente e la
resa ripete, assegnata per firma dell'inglese. **31 `VALUE`** identici (nomi di missione), **31 `DESCRIPTION`**,
**31 `MISSION_TEXT`**, **5 `DIALOG`**; **108 token** in sei famiglie (`<payment>` 36, `<planet>` 31, `<cargo>` 31,
`<destination>` 31, `<passengers>` 4, `<bunks>` 3), **2 virgolette** (unità 81), zero tab, zero quadre. Contenuto:
contrabbando di carico, trasporto di droga, grosse partite, contrabbando e droga «stealth» in tre regioni,
ricercato singolo e ricercati multipli (tre fallimenti diversi) e criminale galattico. Numeri di dettaglio in
`staging/editorial/L117_20261019_063154/{review,REPORT,STATO}.md`.

L116 chiuso il 2026-10-19 — **chiude `_ui/tooltips.txt`**: `check.py` → `FAIL totale: 0` (**38 controlli**);
`verify.py` → exit 0, **47 controlli** con invariante **di file** (667/667 unità coperte, `sovrapposti = 0`);
`sha256[:16]` = `L116 9a630cfede888bed`. 4 parti (34+33+33+33), **80 contesti** per **133 unità** (62 singole, 1
coppia, 4 terne, 8 quaterne, 5 gruppi da cinque), **144 virgolette** in 66 unità, **1 token** `<shift>`, zero tab,
zero quadre, **zero ripetizioni**. Le citazioni sono chiavi e valori di `Preferences` e nomi di gamerule
(`"ship cap,"`, `"off"`, `"Restricted save loading"`) e restano in inglese; le unità 122–124 hanno la **virgola
dentro le virgolette**, riprodotta dal sorgente. Contenuto: sovrapposizioni di stato e HUD, radar e mini-mappa,
mira e fuoco automatici, scelte automatiche (asteroidi, abbordaggio, munizioni, detrito), caccia e flotta,
interfaccia (zoom, font, notifiche, registro, tema), regole di gioco (svalutazione, navi personaggio, distanze,
limiti di flotta, morte permanente, salvataggi) e pannello di abbordaggio. Numeri di dettaglio in
`staging/editorial/L116_20261019_062253/{review,REPORT,STATO}.md`.

L115 chiuso il 2026-10-19: `check.py` → `FAIL totale: 0` (**38 controlli**); `verify.py` → exit 0, **47
controlli**; `sha256[:16]` = `L115 1c8c5a0ff94ca5b2`. 3 parti (35+35+34), **72 contesti** per **104 unità**
(56 singole, 7 coppie, 5 terne, 2 quaterne, una da cinque e una da sei), **82 virgolette** in 38 unità (una con
otto), **8 token** `<shift>`, zero tab, zero quadre, **una ripetizione** identica (89/92). Le citazioni sono
**chiavi e valori di `Preferences`** (`"Escorts expend ammo"`, `"text alignment"`, `"fancy"`, `"off"`) e restano
in inglese; unica eccezione dichiarata `"surge"` → `"picco"`, etichetta già resa da L113. Contenuto: avvisi del
cantiere (batterie, spinta e virata limitate, energia solare, carburante, iperguida, baie, energia per sparare,
equipaggiamento atroce), comandi di volo, selezione e interazione, armi e torrette, pannelli di sistema, ordini
di flotta, zoom e testo, schermo e prestazioni, sfondo e parallasse, contorni delle navi, filtro delle texture e
sovrapposizioni di stato. Numeri di dettaglio in `staging/editorial/L115_20261019_061333/{review,REPORT,STATO}.md`.

L114 chiuso il 2026-10-19: `check.py` → `FAIL totale: 0` (**36 controlli**); `verify.py` → exit 0, **41
controlli**; `sha256[:16]` = `L114 83513c92ec109aa8`. 3 parti (37 × 3), **110 contesti** per **110 unità** (uno
per unità), **12 virgolette** in cinque unità, zero tab, zero token, zero quadre. **Quattro coppie di ripetizioni
legittime** rese identiche — `scrambling` 17/64, `slowing` 18/65, `disruption` 19/66, `firing scramble` 36/83 —
perché l'inglese è identico e cambia solo il contesto (`/ second` contro `/ shot`): qui il criterio «zero
ripetizioni» di L111–L113 è rovesciato. Contenuto: la serie completa dei danni delle armi (scudi, scafo,
estraibili, carburante, calore, energia, ionizzazione, disturbo, interferenza sui motori, disruzione, scarica,
corrosione, perdita di carburante, ustione), le stesse voci in percentuale, le voci allo sparo, la cadenza e le
torrette, l'inseguimento (ottico, infrarossi, radar), la precisione e l'area, e i dieci avvisi del cantiere
(cuccette, surriscaldamento, energia, carburante, propulsori, governo, nave fredda, solo postbruciatore, solo
spinta inversa). Numeri di dettaglio in `staging/editorial/L114_20261019_060200/{review,REPORT,STATO}.md`.

L113 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**30 controlli**); `verify.py` → exit 0, **38
controlli**; `sha256[:16]` = `L113 dc0775e3161aa2b4`. 3 parti (32 × 3), **87 contesti** per **96 unità** con
**nove contesti doppi**, **22 virgolette** (L112 ne aveva zero), zero tab, zero token, zero quadre, zero
ripetizioni. Contenuto: scanner (strategico, tattico, mobilità ×3, equipaggio, energia, carburante, manovra,
telemetro, termico, armi), alloggiamenti per cannoni e torrette, scansione del carico (visibilità e occultamento),
i pannelli **emporio** e **cantiere** con sei coppie azione + scorciatoia, i consumi (inattiva, in movimento,
spinta, spinta inversa, postbruciatore, virata, sparo, scudi e scafo, riparazione, ricarica, variazione netta,
capacità, picco) e le sei categorie del pannello armi. Refuso del sorgente normalizzato nell'unità 4 («before it as
slowed»). Numeri di dettaglio in `staging/editorial/L113_20261018_231320/{review,REPORT,STATO}.md`.

L112 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**29 controlli**); `verify.py` → exit 0, **33
controlli**; `sha256[:16]` = `L112 3ff21c44bf59b9fc`. 4 parti (30 × 4), **120 contesti**, **120 `TUTORIAL_TIP`**
tutte `PENDING` (misurato prima di scrivere). Zero tab, **zero virgolette** (in L111 erano 14), zero token, zero
quadre, zero ripetizioni. **Otto varianti identiche nello stampo** per l'autoriparazione (13–20) e **otto** per la
spinta inversa (88–95): il `check.py` verifica la formula comune, la distinzione reciproca e i nove tipi di danno
(ionizzazione, disturbo, disruzione, interferenza sui motori, scarica, corrosione, perdita di carburante, ustione,
perforazione). Numeri di dettaglio in `staging/editorial/L112_20261018_230735/{review,REPORT,STATO}.md`.

L111 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**31 controlli**); `verify.py` → exit 0, **28
controlli**; `sha256[:16]` = `L111 dee204e785c7d01b`. 4 parti (26 × 4), **104 contesti**. **104 `TUTORIAL_TIP`**,
di cui **52 `APPROVED`** riprodotte **alla lettera** dal campo `italian` di `state.db` (1–52) e **52 `PENDING`**
tradotte (53–104) col registro del blocco approvato: **«tu»**, **«danni da …»** al plurale (**«resistiti»**),
**«ammiraglia»**, **«ustione»** (non «bruciatura»), «spazio carico»/«spazio motori». Zero tab, zero token, zero
quadre, zero ripetizioni, **14 virgolette**, **104 contesti distinti**. Il gate di lunghezza e la tipografia si
applicano **solo alle PENDING**: le approvate non si toccano. Numeri di dettaglio in
`staging/editorial/L111_20261018_230007/{review,REPORT,STATO}.md`.

L110 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**28 controlli**); `verify.py` → exit 0, **35
controlli**; `sha256[:16]` = `L110 741adbe5e3ce5afc`. 2 parti (13, 13), **3 contesti**. **21 `MISSION_TEXT` + 2
`VALUE` + 2 `DESCRIPTION` + 1 `DIALOG`**. Il criterio delle ripetizioni è **rovesciato**: 1/4 sono lo stesso
`VALUE` (`Salvage the <EDC-ship>`) e 2/5 la stessa `DESCRIPTION`, **rese identiche** — il gioco mostra lo stesso
nome per la stessa missione. Tab **17**, virgolette **8**, **19 token** in sette famiglie, zero quadre. La dedica
(unita 25) contiene `<first>` e `<last>` **insieme** e nomina la `<EDC-ship>` due volte. `verify.py` con
**invariante di file**: cinque lotti, **158 `id` distinti**, copertura completa. Numeri di dettaglio in
`staging/editorial/L110_20261018_225501/{review,REPORT,STATO}.md`.

L109 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**30 controlli**); `verify.py` → exit 0, **33
controlli**; `sha256[:16]` = `L109 6e60f04cc8291cb4`. 2 parti (17, 16), **4 contesti**. **27 `MISSION_TEXT` + 3
`VALUE` + 3 `DESCRIPTION`**: i `VALUE` (`Recover the fallen crew of the <EDC-ship>`, `Recover the fallen of
<EDC-ship>`, `<EDC-ship> salvage team`) restano **identici**, le `DESCRIPTION` sono tradotte. Tab **20**,
virgolette **14** (tutte binate), **23 token** in sette famiglie, **`<origin>` ×2** — che è la **partenza**, non
l'arrivo, e va confrontato **per unità** con `<destination>` — `<EDC-ship>` 11, zero quadre. Due coppie di unità
identiche per costruzione (1/4 `VALUE`, 2/5 `DESCRIPTION` identiche nel sorgente) e tre quasi-duplicati (18/19,
20/21/22, 24/25) da tenere distinti. Numeri di dettaglio in
`staging/editorial/L109_20261018_224951/{review,REPORT,STATO}.md`.

L108 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**33 controlli**); `verify.py` → exit 0, **36
controlli**; `sha256[:16]` = `L108 c429ddeb0b22241c`. 2 parti (18, 18), **4 contesti**. **14 `TEXT` + 15
`MISSION_TEXT` + 3 `VALUE` + 3 `DESCRIPTION` + 1 `DIALOG`**: i `VALUE` (`Package to <planet>`, `Distress call from
the <EDC-ship>`, `Return the <EDC-ship> survivors`) restano **identici**. Tab **12** (unità 21–28, 33–36),
virgolette **18** tutte binate, **23 token** (`<EDC-ship>` 8), **zero quadre**, **zero ripetizioni**. Il nodo sono
i **frammenti composti**: vincoli per casella (maiuscola/minuscola, infinito in testa, `a ` e punto finale nella
destinazione) e **24 combinazioni** ricalcolate nel `verify.py`. Numeri di dettaglio in
`staging/editorial/L108_20261018_224456/{review,REPORT,STATO}.md`.

L107 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**27 controlli**); `verify.py` → exit 0, **30
controlli**; `sha256[:16]` = `L107 0c901ea4867f63e3`. 2 parti (19, 19), **3 contesti**. **34 `MISSION_TEXT` +
2 `VALUE` + 2 `DESCRIPTION`**: i `VALUE` (`Korath to <planet>`, `Livestock to <planet>`) restano **identici**, le
`DESCRIPTION` sono tradotte. Tab **29**, virgolette **20** tutte binate (**zero citazioni aperte**), **21 token**
(`<planet>` 12, `<bunks>` 3, `<payment>` 2, `<destination>` 2, `<cargo>` 1, `<tons>` 1), **zero quadre**, **zero
ripetizioni**. Unica identica non-`VALUE`: l'unità 10 `(No.)`. Il nodo è l'**unità 16**, il **Quarg che parla
male**, reso con parole inventate ma trasparenti. Numeri di dettaglio in
`staging/editorial/L107_20261018_223650/{review,REPORT,STATO}.md`.

L106 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**31 controlli**); `verify.py` → exit 0, **29
controlli**; `sha256[:16]` = `L106 10952e0d80f509b5`. 2 parti (13, 12), **6 contesti**. **22 `MISSION_TEXT` +
1 `LOGBOOK` + 1 `VALUE` + 1 `DESCRIPTION`**: il `VALUE` (`Supplies to <planet>`) resta **identico** — è il nome
della missione, con un token dentro — mentre `LOGBOOK` e `DESCRIPTION` sono **tradotti**. Tab **17**, virgolette
**45** con **una citazione aperta** (unità 16), **13 token** in sei famiglie, **16 coppie di quadre** nelle unità
11, 16, 17, 20, 25 (la voce dei Wanderer: due alternative tradotte, struttura intatta, compreso il caso
`[perire? spegnersi?]` con i punti interrogativi **dentro** le quadre) e due ripetizioni (2/3/4, 15/19). Numeri di
dettaglio in `staging/editorial/L106_20261018_223227/{review,REPORT,STATO}.md`.

L105 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**29 controlli**); `verify.py` → exit 0, **31
controlli** (invariante di file); `sha256[:16]` = `L105 4ae2c9e490a62867`. 4 parti (15, 15, 15, 16), **un solo
contesto**. **56 `MISSION_TEXT` + 4 `UI_LABEL` + 1 `LOGBOOK`**: le etichette di salto (`heliarch 2`,
`heliarch ask`, `lunarium 2`, `lunarium ask`) restano **identiche**, il `LOGBOOK` (unità 58, la scheda di Gohl) è
**tradotto per intero**. Tab **54**, virgolette **99** con **una citazione aperta** (unità 26), **7 token** in
cinque famiglie (due nuovi: `<start planet>` e `<start system>`), 5 ripetizioni (una tripla). **Chiude il file**:
117 unità prima, **0 dopo**, 178/178, quattro lotti. La voce di Gohl — il Quarg anziano con la cicatrice — parla
al «tu» con frasi interrotte, e la resa conserva le pause. Numeri di dettaglio in
`staging/editorial/L105_20261018_222718/{review,REPORT,STATO}.md`.

L104 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**27 controlli**); `verify.py` → exit 0, **27
controlli**; `sha256[:16]` = `L104 1186c7b9ae462081`. 2 parti (14, 13), **2 contesti**. **27 `MISSION_TEXT`**,
tab **24**, virgolette **37** con **cinque citazioni aperte** (5, 19, 22, 23, 24; la 5 ne ha tre e nessuna
chiude), **0 token**, **0 quadre**, nessuna ripetizione. **Un'unità identica al sorgente per coincidenza
linguistica**: `(No.)` = `(No.)`, asserita come eccezione nominata e non come permesso generico. 90 unità prima,
61 dopo. Numeri di dettaglio in `staging/editorial/L104_20261018_222145/{review,REPORT,STATO}.md`.

L103 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**28 controlli**); `verify.py` → exit 0, **28
controlli**; `sha256[:16]` = `L103 2e3f270bdda5ce6a`. 2 parti (21, 21), **3 contesti**. **28 `MISSION_TEXT` +
8 `DIALOG` + 3 `DESCRIPTION` + 3 `VALUE`**: i `VALUE` — nomi di missione e di carico — restano **identici**
all'inglese e sono asseriti come uguaglianza per indice; `DESCRIPTION` e `DIALOG` sono tradotti per intero. Tab
**25**, virgolette **43** con **una citazione aperta** (unità 30), **19 token** in sei famiglie (`<cargo>`,
`<payment>`, `<stopovers>`, `<destination>`, `<waypoints>`, `<system>`), 5 ripetizioni (8/12, 10/13, 21/39,
22/40, 36/41). 48 unità prima, 88 dopo. Numeri di dettaglio in
`staging/editorial/L103_20261018_221731/{review,REPORT,STATO}.md`.

L102 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**29 controlli**); `verify.py` → exit 0, **27
controlli**; `sha256[:16]` = `L102 d1e12262951885ee`. 3 parti (22, 15, 11), **2 contesti**. **46 `MISSION_TEXT`
+ 2 `LOGBOOK`** — il primo `LOGBOOK` della campagna, tradotto per intero e verificato come prosa — tab **44**,
virgolette **98**, **2 token** nella stessa unità (42: `<first>` e `<last>`), **0 quadre**, 3 ripetizioni
(17/20, 35/40, 37/38). 0 unità prima, 130 dopo. Due voci Quarg distinte: il primo dá del «tu» e si riferisce a sé
come «questo uno»; quello di Kuwaru Efreti parla in inglese arcaico, reso con ordine marcato italiano e «voi».
Numeri di dettaglio in `staging/editorial/L102_20261018_221223/{review,REPORT,STATO}.md`.

L101 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**26 controlli**); `verify.py` → exit 0, **29
controlli** (invariante di file); `sha256[:16]` = `L101 b32aaa185052d185`. 2 parti (13, 13), **2 contesti**.
**26 `MISSION_TEXT`, 0 `UI_LABEL`**, tab **24**, virgolette **34** (8 nell'unità 25), **0 token**, **1 coppia di
quadre** (unità 13: `[a sedere, a riposare]`), nessuna ripetizione. **Chiude il file**: 121 unità prima, **0
dopo**, 147/147, quattro lotti (39 + 38 + 44 + 26). Due trattini lunghi sono stati sostituiti perché la
tipografia del progetto li vieta; le quadre erano state perse nella prima stesura e l'asserzione del costruttore
ha fermato la build. Numeri di dettaglio in `staging/editorial/L101_20261018_220744/{review,REPORT,STATO}.md`.

L100 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**30 controlli**); `verify.py` → exit 0, **28
controlli**; `sha256[:16]` = `L100 8fb5defc43780334`. 3 parti (16, 15, 13), **2 contesti**. **41 `MISSION_TEXT`
+ 3 `UI_LABEL`** (`field trip`, `pleasant lunch`, `finishing chat`, identiche), tab **39**, virgolette **40** con
**quattro citazioni aperte e non chiuse** (23, 24, 39, 41), **1 token** (`<last>`), **0 quadre**, **nessuna
ripetizione**. 77 unità prima, 26 dopo. Due asserzioni della prima stesura erano sbagliate («una virgoletta
ciascuna», «la citazione si chiude nell'unità successiva»): la 39 ne ha tre, la 25 e la 40 quattro, la 43 non
apre nulla — riscritte sul conteggio misurato. Numeri di dettaglio in
`staging/editorial/L100_20261018_220239/{review,REPORT,STATO}.md`.

L99 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**30 controlli**); `verify.py` → exit 0, **28
controlli**; `sha256[:16]` = `L99 545c18fca521b07f`. 3 parti (13, 14, 11), **4 contesti**. **38 `MISSION_TEXT`,
0 `UI_LABEL`**, tab **34**, virgolette **23** — di cui **una sola** nell'unità 32 (citazione aperta e non chiusa,
voluta) — **0 token**, **0 quadre**, **7 gruppi di ripetizioni** (119/142/165, 121/144/167, 123/146/169,
124/147/170, 126/149, 128/151/174, 191/196). 39 unità prima, 70 dopo. Il contratto diceva «77 unità prima»: era
il totale cumulativo, corretto a **39** dopo la misura del `verify.py`. Numeri di dettaglio in
`staging/editorial/L99_20261018_215807/{review,REPORT,STATO}.md`.

L98 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**29 controlli**); `verify.py` → exit 0, **28
controlli**; `sha256[:16]` = `L98 8df01d63f077d9a2`. 2 parti (20, 19), **3 contesti**. **39 `MISSION_TEXT`,
0 `UI_LABEL`**, tab **36**, virgolette **58**, **1 token** (`<destination>`), **6 quadre** (3 coppie, la voce del
dispositivo di traduzione nell'unità 30). Ripetizioni 20/37, 27/31, 29/39; **28 e 32 differiscono per una
virgola**. Primo lotto del file: 0 unità prima, 108 dopo. Numeri di dettaglio in
`staging/editorial/L98_20261018_215350/{review,REPORT,STATO}.md`.

L97 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**30 controlli**); `verify.py` → exit 0, **29
controlli**; `sha256[:16]` = `L97 cc6086592132277e`. 3 parti (12, 12, 12), **7 contesti**. **36 `MISSION_TEXT`,
0 `UI_LABEL`**, tab **29**, virgolette **24**, **14 token** (`<origin>` ×8, `<ship>` ×5, `<last>` ×1), una
**ripetizione tripla** (7/9/11) e due varianti che differiscono per la virgola (`"collaborazione,"` /
`"collaborazione",`). **Chiude il file**: 121 unità prima, **0 dopo**, 157/157, cinque lotti. Numeri di
dettaglio in `staging/editorial/L97_20261018_214757/{review,REPORT,STATO}.md`.

L96 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**28 controlli**); `verify.py` → exit 0, **29
controlli**; `sha256[:16]` = `L96 0c863a3843dd5f4e`. 3 parti (8, 9, 5) + **5 `UI_LABEL` scritte dal sorgente**
(`defend ww`, `attack w`, `attack wr`, `attack r`, `attack rr`, identiche), **1 contesto** (`Kimek`, chiuso),
**22 `MISSION_TEXT`**. Tab **22**, virgolette **26** (12 nell'unità 6), token **0** (asserzione), ripetizioni
**12/19** e **14/21** rese identiche. Il banchetto dei Kimek e la poltiglia «brodosa e parzialmente digerita».
Numeri di dettaglio in `staging/editorial/L96_20261018_214303/{review,REPORT,STATO}.md`.

L95 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**28 controlli**); `verify.py` → exit 0, **29
controlli**; `sha256[:16]` = `L95 58cfe11da4d60c5c`. 3 parti (9, 8, 7) + **3 `UI_LABEL` scritte dal sorgente**
(`defend r`, `defend rw`, `defend w`, identiche), **1 contesto** (`Kimek`), **24 `MISSION_TEXT`**. Tab **23**,
virgolette **38**, token **0** (asserzione), ripetizione **20/27** resa identica. La rievocazione dell'**Assedio
di Primavera**: il menestrello, il vento che gli coprì il finale, i secchi di liquido scivoloso. Numeri di
dettaglio in `staging/editorial/L95_20261018_213812/{review,REPORT,STATO}.md`.

L94 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**29 controlli**); `verify.py` → exit 0, **28
controlli**; `sha256[:16]` = `L94 2413e9527696c61a`. 3 parti (12, 12, 12), **1 contesto** (`Coalition Folklore:
Arach`). **36 `MISSION_TEXT`, 0 `UI_LABEL`**, tab **35**, virgolette **64** (6 nelle unità 1 e 7), token **0**
(asserzione), **due gruppi di ripetizioni**: 16/22 `(Resta per il prossimo spettacolo.)` e 17/23/29
`(Vai via.)`, rese identiche. Le tre opere (`Toccato dalla Luna`, `Bebliss Balbettante`, `Fino alla Morte`) e la
quarta rappresentazione non annunciata. Numeri di dettaglio in
`staging/editorial/L94_20261018_213255/{review,REPORT,STATO}.md`.

L93 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**28 controlli**); `verify.py` → exit 0, **27
controlli**; `sha256[:16]` = `L93 f11dbf2fa0744173`. 3 parti (10, 10, 11), **1 contesto** (`Coalition Folklore:
Saryd`). **31 `MISSION_TEXT`, 0 `UI_LABEL`** nella finestra, tab **30**, virgolette **22** (4 nell'unità 5),
token **0** (asserzione), **ripetizione tripla 15/20/25** resa identica (la descrizione del palco nei tre
sentieri). **La voce dei Saryd resta invertita** in 2, 5, 10, 31: è caratterizzazione, non refuso. Numeri di
dettaglio in `staging/editorial/L93_20261018_212733/{review,REPORT,STATO}.md`.

L92 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**28 controlli**); `verify.py` → exit 0, **29
controlli**; `sha256[:16]` = `L92 ac367d9586bdaad5`. 3 parti (17, 17, 12), **5 contesti**. **46 `MISSION_TEXT`,
0 `UI_LABEL`** (premessa asserita), tab **42** (senza tab 21, 37, 44, 46), virgolette **48 = 48** con **una sola
nelle unità 13 e 21** (citazioni lasciate aperte dal testo, riprodotte), token **1** `<ship>` (41), ripetizione
**17/20** resa identica. **Chiude il file**: 68 unità prima, **0 dopo**, 114/114, `max(line) = 351`. Numeri di
dettaglio in `staging/editorial/L92_20261018_212146/{review,REPORT,STATO}.md`.

L91 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**28 controlli**); `verify.py` → exit 0, **28
controlli**; `sha256[:16]` = `L91 9a8dcdeaee3a69af`. 2 parti (17, 16) + il solo `UI_LABEL` scritto dal
sorgente, **2 contesti** (`Graffiti`, `Stage Play`). **33 `MISSION_TEXT` + 1 `UI_LABEL`** (`myiara system`,
identica), tab **30** (tutte tranne 1, 28, 29, 30), virgolette **60 = 60** (4 nelle unità 19, 27, 31, 34),
token **5 = 5** (4 `<ship>` + 1 `<origin>`), **tre coppie di inglese identico** (8/12, 9/13, 10/14) rese
identiche. 34 unità prima, **46 dopo**. Numeri di dettaglio in
`staging/editorial/L91_20261018_211306/{review,REPORT,STATO}.md`.

L90 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**27 controlli**); `verify.py` → exit 0, **26
controlli**; `sha256[:16]` = `L90 45fd22aca9b71868`. 2 parti, **6 contesti**. **34 `MISSION_TEXT`**, tab
**28**, virgolette **2** (unità 23), token **3** `<ship>` (1, 10, 18), **una coppia di inglese identico**
(3/13) resa `(Prendilo.)`/`(Prendila.)` per il genere dell'oggetto e una resa identica (26/31). **Primo lotto
del file**: finestra ridotta dichiarata (34 unità su 76 previste). Numeri di dettaglio in
`staging/editorial/L90_20261018_210455/{review,REPORT,STATO}.md`.

L89 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**23 controlli**); `verify.py` → exit 0, **25
controlli**; `sha256[:16]` = `L89 c49081b925bee187`. 1 parte (12 unità), **6 contesti**. **12 `DESCRIPTION`,
nessun dato**, tab **6** (2, 4, 6, 8, 11, 12), virgolette **0**, **0 token**, **duplicato legittimo 1/3/5/7**.
**Chiude il file**: 0 unità dopo, 56/56, `max(line) = 647`.

L88 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**24 controlli**); `verify.py` → exit 0, **24
controlli**; `sha256[:16]` = `L88 40dafd350a29f440`. 1 parte (10 unità), **7 contesti**. **10 `DESCRIPTION`,
nessun dato**, tab **3** (2, 6, 10), virgolette **0**, **0 token**, **duplicato legittimo 2/6/10** reso
identico. 34 unità prima, **12 dopo**.

L87 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**24 controlli**); `verify.py` → exit 0, **24
controlli**; `sha256[:16]` = `L87 667d024aa8548de4`. 1 parte (13 unità), **9 contesti**. **12 `DESCRIPTION`
tradotte** + **1 `VALUE` identico** (`"Niis" Inductive Engines`), tab **3** (2, 7, 9), virgolette **2 = 2**,
0 dispari, **0 token**, 0 duplicati. 21 unità prima, **22 dopo**.

L86 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**26 controlli**); `verify.py` → exit 0, **24
controlli**; `sha256[:16]` = `L86 c3947926c8e088f1`. 1 parte (21 unità), **15 contesti**. **4 `VALUE`
identiche** (plurali dei cortex) + **17 `DESCRIPTION`** tradotte, tab **1**, virgolette **8 = 8**, 0 dispari,
**0 token**, 0 duplicati. Primo lotto del file: **0 prima**, 35 dopo.

L85 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**21 controlli**); `verify.py` → exit 0, **29
controlli**; `sha256[:16]` = `L85 3fad23a16aeaa834`. 1 parte (7 unità), 7 contesti. **7 `DESCRIPTION`, nessun
dato**, tab **0**, virgolette **4 = 4**, 0 dispari, **0 token**, 0 duplicati. **Chiude il file**: 0 unità dopo,
59/59, `max(line) = 782`.

L84 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**24 controlli**); `verify.py` → exit 0, **22
controlli**; `sha256[:16]` = `L84 4107161eef110612`. 1 parte (4 unità), 2 contesti. **1 `TEXT` dato** +
**3 `DESCRIPTION`** tradotte, tab **1**, virgolette **2 = 2**, 0 dispari, **0 token**, 0 duplicati. 48 unità
prima, **7 dopo**.

L83 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**22 controlli**); `verify.py` → exit 0, **27
controlli**; `sha256[:16]` = `L83 5c427d01bb9c39a0`. 1 parte (11 unità), **4 contesti** (`outfit:` e
`ship:`). **8 unità di dato identiche**, **3 `DESCRIPTION` tradotte** (Torji, Crimson Halo, Visions of Rime),
tab **0**, virgolette **12 = 12**, 0 dispari, **0 token**, 0 duplicati. 37 unità prima, **11 dopo**.

L82 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**26 controlli**); `verify.py` → exit 0, **32
controlli**; `sha256[:16]` = `L82 3a179de373b2fe67`. 1 parte (15 unità), **4 contesti** (`ship:` e
`outfit:`). **10 unità di dato identiche** (2 `VALUE` + 8 `TEXT`), **5 `DESCRIPTION` tradotte** (i costrutti
di Myiara, Queru, Iasa, Kis), **1 tab**, virgolette **8 = 8**, 0 dispari, **0 token**, 0 duplicati. 22 unità
prima, **22 dopo**.

L81 chiuso il 2026-10-18 (primo lotto su `predecessors.txt`, descrizioni di navi): `check.py` → `FAIL
totale: 0` (**30 controlli**); `verify.py` → exit 0, **34 controlli**; `sha256[:16]` = `L81 26f957d5edbd1958`.
1 parte (22 unità), due contesti `ship:`. Tab **0**, virgolette **12 = 12**, **0 dispari**, **0 token**,
**5 gruppi di duplicati** (nomi ripetuti su due navi). **17 unità di dato identiche** (nomi di nave e di
equipaggiamento, decisione 259), **5 di prosa tradotte e rimate** (la poesia di Resja). 0 unità prima,
**37 dopo**. Due miei controlli erano sbagliati (rima sulle parole intere, condizione/dettaglio invertiti) e
li ho corretti prima di chiudere.

L80 chiuso il 2026-10-18 e **chiude `successor side missions.txt`**: `check.py` → `FAIL totale: 0`
(**32 controlli**); `verify.py` → exit 0, **36 controlli** con invariante **di file**; `sha256[:16]` =
`L80 0cc5130f4bba902e`. 1 parte (19 unità), un contesto (`Unified Defense`). Tab **11 = 11**, virgolette
**20 = 20**, **0 dispari**, **0 token**, **`NT` 4** (2, 9, 15, 17), **3 gruppi di duplicati** (5/11, 6/12,
7/13), **6 assenze di tipo**. Il file chiude a **164/164**, `max(line) = 453`, **0 dopo**, 4.001 EN → 3.854 IT
in quattro lotti.

L79 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**32 controlli**); `verify.py` → exit 0,
**36 controlli**; `sha256[:16]` = `L79 54af11093d844256`. 2 parti (15 · 14), un contesto intero
(`People's Houses: First Contact`, 29 unità), **tutte `MISSION_TEXT`**. Tab **28 = 28**, virgolette
**33 = 33** con **3 dispari (10, 22, 27)**, **0 token** (`0 = 0` asserito), **3 gruppi di duplicati**
(22/27, 23/28, 18/24/29), **7 assenze di tipo** dichiarate. 116 unità prima, **19 dopo**.

L78 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**31 controlli**); `verify.py` → exit 0,
**39 controlli**; `sha256[:16]` = `L78 a0ebf1dce186051d`. 3 parti (18 · 18 · 17), un contesto intero
(`Stargazing 1`, 53 unità). Tab **46 = 46**, virgolette **86 = 86** e **0 dispari**, **13 token** in 7
famiglie (`<home system>` nuovo), **`NT` 2** (47 `fah soom`, 50 `novel name`), **0 `LOGBOOK`/`DIALOG`**, **5
gruppi di duplicati** (13/20, 15/22, 16/23, 39/41, 45/49) resi identici di proposito. 63 unità prima,
**48 dopo**.

L77 chiuso il 2026-10-18 (primo lotto su `successor side missions.txt`): `check.py` → `FAIL totale: 0`
(**32 controlli**); `verify.py` → exit 0, **45 controlli**; `sha256[:16]` = `L77 5e8d1c0e38c05612`. 4 parti
(16 · 16 · 16 · 15), due contesti interi (`Predecessor Research 1` 37, `Biology Research 1` 26). Tab **53 = 53**
su 53 unità, virgolette **68 = 68**, **2 dispari (56, 57)** che aprono e non chiudono, **13 token** in 6
famiglie (`<planet stopovers>` con spazio), **`NT` 1** (12 `has deferred`), **0 `LOGBOOK`/`DIALOG`**, **3
gruppi di duplicati** (7/42, 9/43, 28/55) e la coppia **22/50** che doveva restare distinta — il primo giro
era rosso lì. Apre il file: 0 unità prima, **101 dopo**, file di 164, `max(line) = 453`.

L76 chiuso il 2026-10-18 e **chiude `successor 2 ghosts aqrabe.txt`**: `check.py` → `FAIL totale: 0`
(**35 controlli**); `verify.py` → exit 0, **49 controlli** con invariante **di file**; `sha256[:16]` =
`L76 44a954ecdc2aac76`. 2 parti (15 · 15), un solo contesto (`Aqrabe 7`). Tab **21 = 21**, virgolette
**43 = 43**, **1 dispari (25)**, **6 token** in 5 famiglie, **`NT` 1** (unità 28 `not confronted`),
**`LOGBOOK` 1** (14, diretta), **`DIALOG` 2** (12 backtick, 13 virgolette), **`UI_LABEL` 1**, **0
duplicati esatti** e la coppia **23/25** che differisce solo per la virgoletta finale. Il file chiude a
**180/180**, `max(line) = 478`, **0 unità dopo**, 5.147 EN → 4.942 IT in quattro lotti.

L75 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**37 controlli**); `verify.py` → exit 0,
**47 controlli**; `sha256[:16]` = `L75 83744e86d2da8682`. 4 parti (15 · 15 · 15 · 16). Tab **51 = 51** su 51
unità, virgolette **130 = 130**, **dispari: insieme (5, 6, 7, 8)** — due battute di K- I- Saajret spezzate a
metà, la virgoletta chiude nelle unità 6 e 8 —, **8 token** in 7 famiglie, **`NT` 1** e **`LOGBOOK` 1**
(unità 27: categoria `People`, testo **non** nel lotto), **`DIALOG` 1** (unità 15, testo), **`UI_LABEL` 0**,
**1 gruppo di duplicati** (6 e 8, stessa firma). Due contesti interi (`Aqrabe 5` 53, `Aqrabe 6` 8):
89 unità prima, **30 dopo**. Un controllo mio era troppo largo («la virgoletta chiude solo in 6 e 8»
guardava tutte le unità che finiscono con `"`): ristretto alle quattro dispari.

L74 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**34 controlli**); `verify.py` → exit 0,
**44 controlli**; `sha256[:16]` = `L74 3928a76816c49f89`. 3 parti (13 · 12 · 13). Tab **28 = 28** su 28
unità con tab iniziale, virgolette **68 = 68**, **0 dispari**, **10 token** in 4 famiglie (`<ship>` 6),
**`NT` 1** (unità 19: `label "no shields"`), **`LOGBOOK` 1** (unità 21, forma diretta), **`VALUE` 2** e
**`DESCRIPTION` 2** (unità 1, 2, 24, 25), **`DIALOG`/`CONVERSATION`/`TEXT` assenti** (in L73 erano 1 e 6),
**1 gruppo di duplicati** (`(Retreat.)` unità 12 e 16, resa identica voluta). Due contesti interi
(`Aqrabe 3`, `Aqrabe 4`), 51 unità prima, **91 dopo**. Il `verify.py` era rosso su «94 dopo»: il numero
giusto è 91 (180 − 51 − 38).

L73 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**35 controlli**); `verify.py` → exit 0,
**47 controlli**; `sha256[:16]` = `L73 1cd04c9a55a1312c`. 3 parti (17 · 18 · 16). Tab **42 = 42** su 38
unità con tab iniziale, virgolette **90 = 90**, **0 dispari**, **9 token** in 6 famiglie, **`NT` 1**
(unita 43: categoria di diario `People`, identica), **`LOGBOOK` 3** (testi 30 e 51 + categoria 43),
**`CONVERSATION` 6** (31–36: **testo** del blocco, tradotto), **`DIALOG` 1** (50, testo), 0 duplicati.
**Primo lotto sul file**: 0 unità prima della 23, **129 dopo** la 158, file di 180, `max(line) = 478`.
Numeri in `staging/editorial/L73_20261018_195325/{review,REPORT,STATO}.md`.

L72 chiuso il 2026-10-18 e **chiude il file**: `check.py` → `FAIL totale: 0` (**35 controlli**);
`verify.py` → exit 0, **46 controlli**; `sha256[:16]` = `L72 bd09dd6de0b9ff04`. 3 parti (17 · 19 · 14).
Tab **36 = 36**, virgolette **96 = 96**, **0 dispari**, **18 token** in 8 famiglie (`<tons>` e `<payment>`
nuovi), **`NT` vuoto**, **`LOGBOOK` 2** (5, 30) e **`DIALOG` 2** (3, 4: **testo**, non etichette), 0
duplicati. **Chiude il file**: **211/211**, `max(line) = 531`, **0 dopo**, cinque lotti (L68–L72),
6.612 EN → 6.329 IT: **trentaduesimo file completo**. Deviato dal piano di `HANDOFF_L72` (che prevedeva
402–464): il lotto copre tre contesti e chiude il file, per non lasciare un ultimo lotto da 30 unità senza
struttura. Numeri in `staging/editorial/L72_20261018_194753/{review,REPORT,STATO}.md`.

L71 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**33 controlli**); `verify.py` → exit 0,
**45 controlli**; `sha256[:16]` = `L71 9bdce0c7e02de186`; `STATO.md` in stato CHIUSO. 2 parti (21 · 21).
Tab **38 = 38** su 38 unità, virgolette **72 = 72**, **0 dispari**, **9 token** in 4 famiglie (`<last>` e
`<planet>` nuove per il file), **`NT` vuoto** e **`LOGBOOK` 0** (assenze dichiarate anche sul `raw`), 0
duplicati. **Segmento**: **119 unità prima** della 311 (L68–L70), **50 dopo** la 401, file di 211,
`max(line) = 531`. Personaggio nuovo (Ijaset) reso **senza genere**: l'inglese usa `they`, l'italiano evita
i participi concordati. `vault` → **cripta** (resa nuova, dichiarata). Numeri di dettaglio in
`staging/editorial/L71_20261018_194315/{review,REPORT,STATO}.md`.

L70 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**38 controlli**); `verify.py` → exit 0,
**48 controlli**; `sha256[:16]` = `L70 a767223f993886ef`; `STATO.md` in stato CHIUSO. 2 parti (20 · 19).
Tab **28 = 28** su 28 unità, virgolette **64 = 64**, **0 dispari**, **5 token** in 4 famiglie con parità
**per simbolo**, **`NT` 3** (unità 30 label di salto; unità **7 e 10** `government \`People's Houses
(Hostile)\``: riferimenti di dato, non prosa), **`LOGBOOK` 3** (8, 35, 37) tutte forma **diretta** e
tradotte, di cui due **alternative** (accettato 35 / rifiutato 37) volutamente distinte, `DIALOG`/
`CONVERSATION`/`TEXT` **0**, **1 gruppo** di duplicati (7/10, il riferimento di governo). **Segmento
interno**: **80 unità prima** della 215 (L68+L69), **92 dopo** la 307, file di 211, `max(line) = 531`.
Numeri di dettaglio in `staging/editorial/L70_20261018_193755/{review,REPORT,STATO}.md`.

L69 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**35 controlli**); `verify.py` → exit 0,
**46 controlli**; `sha256[:16]` = `L69 7ab0a2bee4dc90a6`; `STATO.md` in stato CHIUSO. 2 parti (16 · 15).
Tab **27 = 27** su 21 unità con tab iniziale, virgolette **4 = 4**, **0 dispari**, **10 token** in
4 famiglie con parità **per simbolo** (`<origin>` per la prima volta nel file), **`NT` vuoto** e
**`LOGBOOK` 0** (assenze dichiarate, con l'asserzione che nel `raw` non esista nessuna riga `log`),
`DIALOG`/`CONVERSATION`/`TEXT` **0**, **1 gruppo** di duplicati inglesi (28/30, `Track down Riiria`) con
resa identica, **`VALUE`/`DESCRIPTION` 4 + 4** con controllo positivo. **Segmento interno**: **49 unità
prima** della 118 (L68), **131 dopo** la 197, file di 211 unità, `max(line) = 531`. Un refuso del sorgente
(«Not longer after», unità 12) reso senza replicarlo. Numeri di dettaglio in
`staging/editorial/L69_20261018_193239/{review,REPORT,STATO}.md`.

L68 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (**37 controlli**); `verify.py` → exit 0,
**46 controlli**; `sha256[:16]` = `L68 eaafbeb6e504c701`; `STATO.md` in stato CHIUSO. 2 parti (25 · 24).
Tab **42 = 42**, virgolette **90 = 90**, **0 dispari**, **10 token** in 5 famiglie con parità **per
simbolo**, **`NT` 2** (unità 20 `follow up`, label di salto; unità 23 categoria di diario `People`),
**`LOGBOOK` 2** (unità 23 = **categoria** estratta da `log "People" "Riiria" "…"`, unità 24 = testo),
`DIALOG`/`CONVERSATION`/`TEXT` **0** (assenze dichiarate), **2 gruppi** di duplicati inglesi (15/21,
16/22) con resa identica. **Segmento interno**: 0 unità prima della 16, **162 dopo** la 113, file di
**211 unità**, `max(line) = 531`. Primo lotto sul file; il testo della voce di diario di Riiria resta
**fuori inventario** (settima occorrenza della lacuna dell'estrattore, dopo L45 195/305/357/418, L46 62,
L47 54). Qui è stato corretto il «13 token» che l'handoff L68 dichiarava: la sua stessa tabella e il
`source.json` danno **10**. Numeri di dettaglio in
`staging/editorial/L68_20261018_191943/{review,REPORT,STATO}.md`.

L67 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (33 controlli); `verify.py` → exit 0,
**38 controlli**; `sha256[:16]` = `L67 ad997eaa9007d7c2`; `STATO.md` in stato CHIUSO. 2 parti (17 · 18).
Tab **32 = 32**, virgolette **68 = 68**, **0 dispari**, **2 token** `<ship>` con parità per simbolo,
**1 `LOGBOOK`** (unità 1, forma **backtick**: controllo reso **positivo**, decisione 221), **`NT` vuoto**,
`DIALOG`/`CONVERSATION`/`TEXT` **0**, **0 gruppi** di duplicati. **Chiude il file**: 339 unità prima,
**0 dopo** la 1122, copertura **374/374**, `max(line) = 1122`. Con L66 (**45 unità**, 1.239 EN → 1.176 IT,
2 dispari riprodotte su 10/34, 33 controlli, 36 controlli di verify, sha `L66 41a48d5412d5b7c6`) il file
`culture conversations.txt` è **completo**: dieci lotti, 374 unità, 11.269 EN → 10.858 IT,
**trentunesimo file completo**. Numeri di dettaglio in `staging/editorial/L66_20261018_190909/` e
`staging/editorial/L67_20261018_191025/{review,REPORT,STATO}.md`.

L65 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (33 controlli); `verify.py` → exit 0,
**36 controlli**; `sha256[:16]` = `L65 8cde7537201a63c9`; `STATO.md` in stato CHIUSO. 2 parti (21 · 22).
Tab **45 = 45**, virgolette **22 = 22**, **0 dispari**, **2 token** (`<origin>`, `<ship>`) con parità **per
simbolo**, **`NT` 4** (10, 12, 14, 16), `DIALOG`/`LOGBOOK`/`CONVERSATION`/`TEXT` **0** (assenze dichiarate),
**1 gruppo** di duplicati (26/30). Un titolo con `°` è stato riscritto «trecentesimo anniversario» perché
il simbolo è vietato (decisione 212). **Segmento interno**: 251 unità prima, **80 dopo** la 920.
Con L64 (**42 unità**, 1.652 EN → 1.598 IT, `NT` 4 su 15/18/22/24, 3 dispari riprodotte, 33 controlli,
36 controlli di verify, sha `L64 57a238ca0241c4ca`) il file `culture conversations.txt` è a
**294/374 (78,6%)**. Numeri di dettaglio in `staging/editorial/L64_20261018_181613/` e
`staging/editorial/L65_20261018_181730/{review,REPORT,STATO}.md`.

L63 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (33 controlli); `verify.py` → exit 0,
**36 controlli**; `sha256[:16]` = `L63 3535834a2a119c44`; `STATO.md` in stato CHIUSO. 2 parti (10 · 27).
Tab **35 = 35**, virgolette **51 = 51** con **3 dispari** (unità **18, 29, 31**) **riprodotte**, **0 token**,
**`NT` 1** (unità 30, `way in`), `DIALOG`/`LOGBOOK`/`CONVERSATION`/`TEXT` **0** (assenze dichiarate),
**0 gruppi** di duplicati. Un rapporto fuori banda (unità 27, 2,08) è stato corretto **riscrivendo la
battuta** (ora 1,85), non allargando il gate. **Segmento interno**: 172 unità prima, **165 dopo** la 711.
Con L62 (**30 unità**, 674 EN → 681 IT, `NT` 3 su 4/15/26, 0 duplicati, 33 controlli, 36 controlli di
verify, sha `L62 8b9f92399b32c32a`) il file `culture conversations.txt` è a **209/374 (55,9%)**.
Numeri di dettaglio in `staging/editorial/L62_20261018_181058/` e
`staging/editorial/L63_20261018_181154/{review,REPORT,STATO}.md`.

L61 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (33 controlli); `verify.py` → exit 0,
**35 controlli**; `sha256[:16]` = `L61 8b7278d41edd723f`; `STATO.md` in stato CHIUSO. 2 parti (12 · 14).
Tab **25 = 25**, virgolette **38 = 38**, **1 token** (`<origin>`, unità 11), **`NT` vuoto**,
`DIALOG`/`LOGBOOK`/`CONVERSATION`/`TEXT` **0** (assenze dichiarate), **2 gruppi** di duplicati inglesi
(18/24, 20/26) con resa identica. **Segmento interno**: 116 unità prima, **232 dopo** la 552, file di 374.
Con L60 (**31 unità**, 661 EN → 626 IT, `NT` 2 su 6 e 20, 0 duplicati, 33 controlli, 36 controlli di
verify, sha `L60 412787a6b5f31400`) il file `culture conversations.txt` è a **142/374 (38,0%)**.
Numeri di dettaglio in `staging/editorial/L60_20261018_180524/` e
`staging/editorial/L61_20261018_180703/{review,REPORT,STATO}.md`.

L59 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (33 controlli); `verify.py` → exit 0,
**35 controlli**; `sha256[:16]` = `L59 5d42121563e61f8d`; `STATO.md` in stato CHIUSO. 4 parti (11 · 12 ·
18 · 1). Tab **32 = 32**, virgolette **34 = 34**, **0 token**, **`NT` vuoto**, `DIALOG`/`LOGBOOK`/
`CONVERSATION`/`TEXT` **0** (assenze dichiarate), **0 gruppi** di duplicati inglesi (primo caso della
serie: controllo **negativo** asserito). **Segmento interno**: 43 unità prima, **289 dopo** la 423,
file di 374. Con L58 (**43 unità**, 1.610 EN → 1.532 IT, 3 gruppi di duplicati, 33 controlli,
sha `L58 0a66e11210f15963`) il file `culture conversations.txt` è a **85/374 (22,7%)**.
Numeri di dettaglio in `staging/editorial/L58_20261018_175847/` e
`staging/editorial/L59_20261018_180020/{review,REPORT,STATO}.md`.

L57 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (33 controlli); `verify.py` → exit 0,
**41 controlli**; `sha256[:16]` = `L57 c3f3b8a9de69cfe1`; `STATO.md` in stato CHIUSO. 4 parti
(23 · 47 · 34 · 23). Tab **94 = 94**, virgolette **60 = 60**, token **13 = 13** in **6 famiglie**
(`<destination>` 4, `<ship>` 3, `<first>` 2, `<last>` 2, `<origin>` 1, `<payment>` 1), **`NT` 17**,
**`DIALOG` 3** (22, 23, 125; 22 e 23 identiche), `LOGBOOK`/`CONVERSATION`/`TEXT` **0** (assenze
dichiarate), **4 gruppi** di duplicati (8 unità). **Chiude il file**: 298/298 con L56 (171).
Il primo `verify.py` era rosso su `(905, 1287)` perché la finestra di export non coincide con la prima
unità (**943**): corretto il numero, non il controllo.
Con L56 (**171 unità**, 5.671 EN → 5.138 IT, `NT` 28, `DIALOG` 3, 12 token in 5 famiglie, 33 controlli,
sha `L56 c2fe3862c23a294e`) `gegno I corroboration.txt` è a **298/298**: trentesimo file completo.
Numeri di dettaglio in `staging/editorial/L56_20261018_174346/` e
`staging/editorial/L57_20261018_174721/{review,REPORT,STATO}.md`.

L55 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (33 controlli); `verify.py` → exit 0,
**40 controlli**; `sha256[:16]` = `L55 69eaa9d886a113f0`; `STATO.md` in stato CHIUSO. 1 parte (28 unità).
Tab **14 = 14**, virgolette **34 = 34**, **0 token**, **`NT` 4**, **`CONVERSATION` 1** (unità 28,
controllo positivo), `LOGBOOK`/`DIALOG`/`TEXT` **0** (assenze dichiarate), **1 gruppo di duplicati**
(`"I do not care."`, unità 10 e 19). **Chiude il file**: 276/276 con L53 (89) e L54 (159).
Con L54 (**159 unità**, 5.975 EN → 5.274 IT, `NT` 19, `LOGBOOK` 3, **20 gruppi** di duplicati, 33
controlli, sha `L54 5ac7ae01fd74ae15`) la linea `gegno intro missions.txt` è a **276/276**:
ventinovesimo file completo. Numeri di dettaglio in `staging/editorial/L54_20261018_173515/` e
`staging/editorial/L55_20261018_173904/{review,REPORT,STATO}.md`.

L53 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (33 controlli); `verify.py` → exit 0,
**41 controlli**; `sha256[:16]` = `L53 7e2899a23c7c3c8e`; `STATO.md` in stato CHIUSO. 3 parti
(30 · 30 · 29). Tab **75 = 75**, virgolette **6 = 6** (3 coppie, il minimo della serie), token **27 = 27**
in **5 famiglie** con maiuscole significative (`<Alien>`, `<alien>`, `<aliens>`, `<designated system>`,
`<origin>`), **`LOGBOOK` 0** e **`DIALOG` 0** (assenze dichiarate), **`NT` 5**, 8 gruppi di duplicati
inglesi con resa identica. Apre la **linea Gegno** e lascia il file a **89/276 (32,2%)**.
Con L52 (**135 unità**, 3.538 EN → 3.373 IT, `NT` 1, `LOGBOOK` 17, `DIALOG` 3, 31 controlli,
sha `L52 d529e6f657dc9aef`) il file `avgi 0 first contact.txt` è a **406/406**: ventottesimo file
completo. Numeri di dettaglio in `staging/editorial/L52_20261018_172541/` e
`staging/editorial/L53_20261018_172908/{review,REPORT,STATO}.md`.

L51 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (31 controlli); `verify.py` → exit 0,
**45 controlli**; `sha256[:16]` = `L51 62a89c1348ea5162`; `STATO.md` in stato CHIUSO. 5 parti
(43 · 32 · 29 · 39 · 9). Tab **113 = 113**, virgolette **252 = 252**, token **32 = 32** (7 famiglie),
**0 quadre**, **0 virgolette dispari**, **`NT` vuoto** (0 `UI_LABEL`: primo caso della serie),
**`LOGBOOK` 10** (6 a tre argomenti + 4 fra backtick), **`DIALOG` 6**. Con L50 (**119 unità**,
4.399 EN → 4.139 IT, `NT` 3, `LOGBOOK` 7, `DIALOG` 2, `TEXT` 1, 29 controlli, sha
`L50 50c003eec1b5e9a3`) il file `avgi 0 first contact.txt` è a **271/406 (66,7%)**: **non** completo,
restano 135 unità (L52). Numeri di dettaglio in `staging/editorial/L50_20261018_171330/` e
`staging/editorial/L51_20261018_171829/{review,REPORT,STATO}.md`.

L49 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (28 controlli); `verify.py` → exit 0,
**38 controlli**; `sha256[:16]` = `L49 0fe8cac3bf134108`; `STATO.md` in stato CHIUSO. 7 parti
(35 · 32 · 43 · 37 · 44 · 39 · 26). Tab **235 = 235**, virgolette **471 = 471**, token **13 = 13**
(6 famiglie), **0 unità con quadre**, **7 virgolette dispari** (22, 91, 101, 108, 109, 186, 218),
`NT` = **3 `UI_LABEL`**, **`LOGBOOK` 5** tutte di testo. Con L48 (**180 unità**, 5.627 EN → 5.297 IT,
`NT` 14, `LOGBOOK` 14, 30 controlli, sha `L48 fcb07ed0909aeb65`) il file `avgi side missions.txt` è a
**436/436**: ventisettesimo file completo. Numeri di dettaglio in
`staging/editorial/L48_20261018_170232/` e `staging/editorial/L49_20261018_170618/{review,REPORT,STATO}.md`.

L47 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (26 controlli); `verify.py` → exit 0,
**38 controlli**; `sha256[:16]` di `translation.json` = `L47 d783356009cbb44d`; `STATO.md` in stato
CHIUSO. 3 parti (45 · 40 · 39). Tab **102 caratteri su 100 unità**, virgolette **124 = 124**,
token **24 = 24** (9 famiglie), **1 unità con quadre** (21), **2 virgolette dispari** (46, 63),
`NT` = **9** (8 `UI_LABEL` + 1 categoria di diario), **`LOGBOOK` 4** (3 testi + 1 categoria).
Con L46 (**221 unità**, 7.180 EN → 6.973 IT, `NT` 18, `LOGBOOK` 9, 37 controlli, sha
`L46 aa71c36e9b399505`) il file `successor 1 prologue.txt` è a **345/345**: ventiseiesimo file completo.
Numeri di dettaglio in `staging/editorial/L46_20261018_164912/` e
`staging/editorial/L47_20261018_165449/{review,REPORT,STATO}.md`.

L45 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (25 controlli); `verify.py` → exit 0,
**39 controlli**; `sha256[:16]` di `translation.json` = `L45 480ff95bd7e2d97b`; documento del lotto
`STATO.md` in stato CHIUSO. 14 parti a fine contesto (45 · 55 · 50 ×11 · 30). Tab **526 = 526**, virgolette
**1107 = 1107**, token **102 = 102** (14 famiglie), **11 unità con quadre** `[...]` (frammenti redatti,
conteggio per unità), **15 virgolette dispari** conservate, `NT` = **34** (26 `UI_LABEL` + 8 riferimenti
di dato), **`LOGBOOK` 23** (19 di testo + 4 categorie estratte come unità, lacuna documentata),
**`CONVERSATION` 16** (nodi 135–138 e 256–267; il solo 137 identico per necessità). Numeri di dettaglio in
`staging/editorial/L45_20261018_163313/{review,REPORT,STATO}.md`.

L44 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (25 controlli); `verify.py` → exit 0,
**37 controlli**; `sha256[:16]` di `translation.json` = `L44 2a83b689b3604483`; documento del lotto
`STATO.md` in stato CHIUSO. 13 parti a fine contesto (50 ×12 · 25). Tab **483 = 483**, virgolette
**921 = 921**, token **73 = 73** (8 famiglie), **0 unità con quadre**, **17 virgolette dispari**
conservate, `NT` = **10 `UI_LABEL`**, **12 `LOGBOOK`** (5 a tre argomenti: categoria e nome in inglese,
lacuna documentata). Numeri di dettaglio in `staging/editorial/L44_20261018_162104/{review,REPORT,STATO}.md`.

L43 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (21 controlli); `verify.py` → exit 0,
**33 controlli**; `sha256[:16]` di `translation.json` = `L43 018217f1aac1ba49`; documento del lotto
`STATO.md` in stato CHIUSO. 8 parti a fine contesto (41 · 30 · 38 · 39 · 36 · 45 · 29 · 41). Tab
**208 = 208**, virgolette **445 = 445**, token **47 = 47** (9 famiglie), **0 unità con quadre**,
**11 virgolette dispari** conservate (133, 188, 190, 225, 227, 229, 245, 247, 280, 285, 286), `NT` =
**36 `UI_LABEL`** (label di salto, elencate una per una, due ripetute), **0 `LOGBOOK`** (asserzione di
assenza: il file non ha righe `log`). Numeri di dettaglio in
`staging/editorial/L43_20261018_160846/{review,REPORT,STATO}.md`.

L42 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (21 controlli); `verify.py` → exit 0,
**33 controlli**; `sha256[:16]` di `translation.json` = `L42 1115f51df15d6704`; documento del lotto
`STATO.md` in stato CHIUSO. 14 parti a fine contesto (58 · 39 · 49 · 41 · 38 · 52 · 46 · 37 · 39 · 35 ·
22 · 50 · 40 · 26). Tab **342 = 342**, virgolette **909 = 909**, token **174 = 174** (16 famiglie),
**0 unità con quadre**, **11 virgolette dispari** conservate (32, 48, 50, 201, 240, 241, 245, 246, 342,
485, 558), `NT` = **35 `UI_LABEL`** (label di salto, elencate una per una), **2 `LOGBOOK`** (di cui una
con la lacuna di categoria della riga 388). Numeri di dettaglio in
`staging/editorial/L42_20261018_155050/{review,REPORT,STATO}.md`.

L41 chiuso il 2026-10-18: `check.py` → `FAIL totale: 0` (22 controlli) al primo colpo; `verify.py` →
exit 0, **30 controlli**; `sha256[:16]` di `translation.json` = `L41 17727c643c46cd38`; documento del
lotto `STATO.md` in stato CHIUSO. 2 parti (40, 32), a fine contesto. Tab **0 = 0**, virgolette **0 = 0**,
token 172 = 172, **0 unità con quadre**, **0 virgolette dispari**, `NT` = **vuoto** (0 `UI_LABEL`),
**6 unità `TEXT`** (testi di `phrase`) tradotte, **0 `LOGBOOK`** (il file non ha righe `log`). È il lotto
più piccolo della serie e il più denso di token. Numeri di dettaglio in
`staging/editorial/L41_20261018_153942/{review,REPORT,STATO}.md`.

Riferimento dei due lotti precedenti: `L42 1115f51df15d6704` (572 unità, 14 parti) e `L41 17727c643c46cd38` (72 unità, 2 parti).

---

L135 chiuso il 2026-10-19 — **primo lotto di `data/starts.txt`**, un tipo di file nuovo: sono **gli inizi di
partita**. Righe **18–130**, **32 unità**, **1.485 parole**, **4 contesti completi**, `check.py` → `FAIL totale: 0`
(**29 controlli**), `verify.py` → exit 0 (**29 controlli**), `sha256[:16]` = `L135 f897bd0f3d943382`. 4 parti
(8+8+9+7). Tipi: **18 `CONVERSATION`**, **8 `LOGBOOK`**, **4 `DESCRIPTION`**, **2 `VALUE`** (`Endless Sky`, `Deep
Desire`) che sono **nomi di inizi** e restano identici. **Zero token in tutto il file**, **14 unità con tab**, **14
virgolette** senza unità dispari, **27 testi distinti** su 32 (unità 21–25 = 5–9, cinque frasi condivise fra i due
inizi, rese con costanti e confrontate). I numeri seguono la convenzione italiana (`480.000`, `0,4%`, `2.503`,
`433.567`), con un controllo che **vieta** le forme inglesi. `Deep` e `Dirt Belt` restano nomi propri inglesi.
Numeri di dettaglio in `staging/editorial/L135_20261019_131024/{review,REPORT,STATO}.md`.

L136 chiuso il 2026-10-19 — **secondo inizio di `data/starts.txt`** (`Birthday Surprise`): righe
**135–167**, **15 unità**, **587 parole**, **2 contesti completi**, `check.py` → `FAIL totale: 0` (**28 controlli**),
`verify.py` → exit 0 (**28 controlli**), `sha256[:16]` = `L136 adbc2022515e8753`. 3 parti (5+5+5). Tipi: **8
`CONVERSATION`**, **4 `LOGBOOK`**, **2 `DESCRIPTION`**, **1 `VALUE`**. **14 virgolette** (6:2, 10:4, 11:2, 12:4,
13:2), **6 unità con tab**, **zero token**. Le unità **5–9 sono le stesse di L135**: rilette dal suo `translation.json`
dopo aver verificato l'inglese, e confrontate — non ricopiate. L'handoff di L136 dichiarava «nessuna delle cinque
condivise ricade qui»: **era falso**, e il `verify.py` lo misura. La battuta dell'unità 12 è **troncata dal sorgente**
(`before-"`) e la resa riproduce il taglio. `child` → «figlio» (maschile generico, dichiarato). Numeri in convenzione
italiana (`500.000`). Numeri di dettaglio in `staging/editorial/L136_20261019_133830/{review,REPORT,STATO}.md`.

L137 chiuso il 2026-10-19 — **terzo inizio di `data/starts.txt`** (`Escaping Squalor`): righe **172–210**, **17
unità**, **802 parole**, **2 contesti completi**, `check.py` → `FAIL totale: 0` (**29 controlli**), `verify.py` → exit 0
(**28 controlli**), `sha256[:16]` = `L137 24133aaf9c9f177d`. 3 parti (6+6+5). Tipi: **10 `CONVERSATION`**, **4
`LOGBOOK`**, **2 `DESCRIPTION`**, **1 `VALUE`**. **12 virgolette** (6:2, 11:2, 13:2, **14:4**, 17:2), **8 unità con
tab**, **zero token**, **cinque unità rilette da L135**. Cinque cifre in convenzione italiana (600.000, 0,5%, 3.580,
706.571, 480.000) con un controllo che **vieta** le forme inglesi. La cortesia del cassiere («Come possiamo
aiutarla?») resta **dentro la battuta**: la narrazione continua a dare del «tu», e un controllo tollera al massimo una
forma di cortesia. `Syndicated Systems` resta nome di prodotto. Numeri di dettaglio in
`staging/editorial/L137_20261019_140902/{review,REPORT,STATO}.md`.

L138 chiuso il 2026-10-19 — **quarto inizio di `data/starts.txt`**, gli **Hai**: righe **215–358**, **47 unità**,
**1356 parole**, **2 contesti completi**, `check.py` → `FAIL totale: 0` (**32 controlli**), `verify.py` → exit 0 (**31
controlli**), `sha256[:16]` = `L138 ab536b2d9a5a2c29`. 5 parti (10+10+10+10+7). Tipi: **32 `CONVERSATION`**, **7
`LOGBOOK`**, **6 `DESCRIPTION`**, **2 `VALUE`**. **Due inizi con lo stesso nome** (`Hai Origins`, unità 1 e 5): uno
bloccato («Questo inizio è bloccato»), uno sbloccabile, e un controllo verifica che i due testi **non coincidano**.
**32 unità con tab** su 47, **56 virgolette** con **quattro dispari** (26, 36, 37, 38) lasciate aperte come nel
sorgente, **zero token**, **cinque unità rilette da L135**. Quattro cifre in convenzione italiana (1,431 milioni, 0,3%,
4.836, 1,132 milioni). `Pristine Jewel`, `Grasshopper`, `Aphid`, `Sheragi`, `Drak` restano nomi. Numeri di dettaglio in
`staging/editorial/L138_20261019_142846/{review,REPORT,STATO}.md`.

L139 chiuso il 2026-10-19 — **coda di `data/starts.txt`**, che **chiude il file a 113/113**: righe **365–366**, **2
unità**, **6 parole**, **1 contesto** (`ship:Grasshopper`), `check.py` → `FAIL totale: 0` (**21 controlli**), `verify.py`
→ exit 0 (**22 controlli**), `sha256[:16]` = `L139 1ceb216ebf1e03c6`. Le due unità sono **nomi di equipaggiamento** —
`"Benga" Atomic Thruster`, `"Biroo" Atomic Steering` — lasciati **identici** con lista `ID_OK` e controllo dedicato:
un nome identico si **dichiara**, non si esclude dai controlli. **Zero tab** (tab e backtick stanno nel `raw`, fuori dal
campo `english`), **4 virgolette** che sono parte dei nomi, **tre asserzioni vuote** (`VALUE`, `UI_LABEL`, token).
L'**invariante di file** somma i cinque lotti: **32 + 15 + 17 + 47 + 2 = 113**, sovrapposti 0, `max(line)` 366.
`starts.txt` è il **quarantanovesimo file completo** (4.236 EN → 4.094 IT). Numeri di dettaglio in
`staging/editorial/L139_20261019_144407/{review,REPORT,STATO}.md`.

L140 chiuso il 2026-10-19 — **primo lotto di `data/hai/unfettered 0 prologue.txt`**, il primo contatto con gli
**Slegati**: righe **22–81**, **25 unità**, **405 parole**, **1 contesto**, `check.py` → `FAIL totale: 0` (**31
controlli**), `verify.py` → exit 0 (**25 controlli**), `sha256[:16]` = `L140 ed2e17388b122b8f`. 3 parti (9+8+8).
Tipi: **25 `MISSION_TEXT`**. **23 unità con tab** (senza tab: 1 e 8), **50 virgolette** con sei unità da quattro,
**zero token**, **21 testi distinti** su 25. Il **motto degli Slegati** compare **cinque volte identico** ed è una
costante sola, verificata per occorrenza. Quattro coppie ripetute (le due scelte, la domanda sui «veri Hai», la battuta
sull'estinzione) hanno **la stessa resa** nei due rami: le scelte del giocatore non possono produrre testi diversi.
`monkey` → «scimmia», e la sgrammaticatura del sorgente («Although despite») resta («Sebbene, nonostante»). Numeri di
dettaglio in `staging/editorial/L140_20261019_145902/{review,REPORT,STATO}.md`.

L141 chiuso il 2026-10-19 — **seconda parte della prima missione** di `unfettered 0 prologue.txt`: righe **83–132**,
**20 unità**, **591 parole**, **1 contesto che si chiude** (`First Contact: Unfettered` 45/45), `check.py` → `FAIL
totale: 0` (**30 controlli**), `verify.py` → exit 0 (**25 controlli**), `sha256[:16]` = `L141 2abdd856e427930b`. 3 parti
(7+7+6). Tipi: **18 `MISSION_TEXT`**, **2 `LOGBOOK`**. **18 unità con tab** (le due voci di diario no), **58
virgolette** con nove unità da quattro, **zero token**, **20 testi distinti**. La **voce di diario identica a L138**
(unita 19) è riletta e confrontata; la **variante** (unità 20) è resa di nuovo, non copiata. La frase sugli «antenati
ottusi» compare in due unità con la stessa resa. La voce telegrafica degli Slegati resta spezzata: «Una volta, centomila
anni ormai passati», «Scimmia sciocca». `jump drive` → **motore di salto** (eccezione di glossario). Numeri di dettaglio
in `staging/editorial/L141_20261019_151233/{review,REPORT,STATO}.md`.

L142 chiuso il 2026-10-19 — **terza parte** di `unfettered 0 prologue.txt`, che chiude `Unfettered Jump Drive 1`:
righe **139–201**, **20 unità**, **493 parole**, `check.py` → `FAIL totale: 0` (**29 controlli**), `verify.py` → exit 0
(**26 controlli**), `sha256[:16]` = `L142 1e2c9c50567e62e1`. 3 parti (7+7+6). Tipi: **18 `MISSION_TEXT`**, **1
`VALUE`**, **1 `DESCRIPTION`**. **17 unità con tab** (senza: `VALUE`, `DESCRIPTION`, il testo introduttivo), **38
virgolette**, **zero token**, **19 testi distinti**. Il **rifiuto** compare in due punti (unità 13 e 18) ed è una
costante; **`(No.)`** resta `(No.)` perché in italiano «No» è la stessa parola, e sta in `ID_OK` con un controllo
dedicato. `jump drive` → **motore di salto**, `hyperdrive` → **iperpropulsore**, `Anomalocaris` invariato. Un **errore
di misura** («81 dopo» invece di **82**: 147 − 45 − 20) è stato bocciato dal `verify.py` e corretto in due punti.
Numeri di dettaglio in `staging/editorial/L142_20261019_153021/{review,REPORT,STATO}.md`.

L143 chiuso il 2026-10-19 — **due missioni intere in un lotto**: `Unfettered Jump Drive 2` (12) e `Jump Drive 3`
(18), righe **214–317**, **30 unità**, **723 parole**, `check.py` → `FAIL totale: 0` (**30 controlli**), `verify.py` →
exit 0 (**25 controlli**), `sha256[:16]` = `L143 a6fdd67b2067eb90`. 4 parti (8+8+8+6). Tipi: **28 `MISSION_TEXT`**, **1
`VALUE`**, **1 `DESCRIPTION`**. **26 unità con tab**, **46 virgolette** (tre unità con quattro), **zero token**, **28
testi distinti**. Il **`VALUE` `More Jump Drives` ricompare** identico a L142 e la ricomparsa è verificata qui, non
presunta. Le due scelte: **`(No.)` identico** in `ID_OK`, **`(Yes.)` → «(Sì.)»** con la stessa resa nelle due missioni.
Entrambi i contesti si chiudono (12/12 e 18/18). Il lessico degli Slegati resta solenne e sprezzante: «divoratori di
carogne», «quei mondi sono nostri di diritto». Numeri di dettaglio in
`staging/editorial/L143_20261019_154514/{review,REPORT,STATO}.md`.

L144 chiuso il 2026-10-19 — **il commercio dei motori, primo tratto**: righe **367–420**, **20 unità**, **486
parole**, `check.py` → `FAIL totale: 0` (**31 controlli**), `verify.py` → exit 0 (**25 controlli**), `sha256[:16]` =
`L144 794b9584fd67c6a0`. 3 parti (7+7+6). Tipi: **20 `MISSION_TEXT`**, zero `VALUE`/`LOGBOOK`/`UI_LABEL` (tre
asserzioni vuote). **19 unità con tab**, **12 virgolette**, **20 testi distinti**. **Primi due token del file** in due
unità diverse: `<hood>` **incollato** a «Slegato» (in inglese è un suffisso), `<learned>` **a inizio frase** con la
maiuscola italiana che segue. `outfitter` → **fornitore** per maggioranza misurata (45 contro 2 di «equipaggiatore»).
La scena: la prova della lama, i tre rifiuti, il controllo di sicurezza, Desneeparu. Numeri di dettaglio in
`staging/editorial/L144_20261019_160233/{review,REPORT,STATO}.md`.

L145 chiuso il 2026-10-19 — **la loggia delle armi**: righe **423–459**, **13 unità**, **703 parole**,
`check.py` → `FAIL totale: 0` (**32 controlli**), `verify.py` → exit 0 (**27 controlli**), `sha256[:16]` =
`L145 56b7e47a1b3a8c72`. 3 parti (5+4+4). Tipi: **12 `MISSION_TEXT`** + **1 `LOGBOOK`** (unità 3, diario tradotto e
verificato come non identico). **12 unità con tab**, **20 virgolette** con **due dispari** — unità 12 e 13: il sorgente
apre e non chiude, la resa riproduce il difetto e un controllo pretende che l'italiano **non** finisca con una
virgoletta. **Tre token**: `<learned>` e `<last>` nell'unità 2, `<The engineer>` nell'unità 5, confrontato **esatto**
(con `.lower()` sarebbe un simbolo diverso, e il controllo vieta la variante minuscola). Nomi inglesi verificati:
`Tripulse Shredder`, `Blaster`, `Ion Cannon`, `Shield Beetle`, `Firelode`; un controllo **rifiuta** le traduzioni
inventate («Distruttore», «Cannone ionico», «Scarabeo»). Numeri di dettaglio in
`staging/editorial/L145_20261019_162015/{review,REPORT,STATO}.md`.

L146 chiuso il 2026-10-19 — **il file è chiuso**: righe **460–530**, **19 unità**, **656 parole**, `check.py` →
`FAIL totale: 0` (**31 controlli**), `verify.py` → exit 0 (**26 controlli**, invariante di **file**), `sha256[:16]` =
`L146 7aaadc8a4d2d1252`. 3 parti (6+6+7). Tipi: **17 `MISSION_TEXT`** + **2 `UI_LABEL`** identiche al sorgente
(`back to choose`, `buy tripulse`), zero `VALUE`. **17 unità con tab**, **28 virgolette e ZERO dispari**, **4 token**:
`<origin>`, `<as before (run)>`, `<as before (flee)>` (parentesi **intere**, soggetti di frase) e `<leave>`. Invariante
di file: `25+20+20+30+20+13+19 = 147` **calcolato dai `translation.json`**, `max(line) = 530`, zero sovrapposizioni.
**Cinquantesimo file completo.** `data/human/news.txt` è stato **scartato** come prossimo bersaglio: **164 unità su 202
sono il delimitatore `` `"` ``** e **1.356 righe con una frase quotata non sono inventariate** (zero nel database) — un
lotto lì sarebbe una copia di `"`. Numeri di dettaglio in
`staging/editorial/L146_20261019_164012/{review,REPORT,STATO}.md`.

L147 chiuso il 2026-10-19 — **i lavori dell'Anello**: righe **16–293**, **30 unità**, **437 parole**, `check.py` →
`FAIL totale: 0` (**28 controlli**), `verify.py` → exit 0 (**27 controlli**), `sha256[:16]` = `L147 86d0e8e3b5fccb2f`.
3 parti (10+10+10). Tipi: **13 `VALUE`** identici (nomi di lavoro), **13 `DESCRIPTION`**, **4 `TEXT`**; zero `LOGBOOK`,
zero `DIALOG`, zero `UI_LABEL`. **Zero tab, zero virgolette.** **65 token su 7 simboli** con tre controlli distinti:
multiset per simbolo, **ordine per unità**, due conteggi nominati (`<payment>` 17, `<date>` 4). **14 testi distinti**
con **4 gruppi tripli** a resa unica. Durante il lotto è stata **rimossa un'asserzione fittizia** (`ck(..., True)`):
meglio un controllo in meno che uno che passa sempre. Numeri di dettaglio in
`staging/editorial/L147_20261019_171044/{review,REPORT,STATO}.md`.

L148 chiuso il 2026-10-19 — **gli interpreti e il primo `DIALOG`**: righe **309–435**, **16 unità**, **205
parole**, `check.py` → `FAIL totale: 0` (**27 controlli**), `verify.py` → exit 0 (**25 controlli**), `sha256[:16]` =
`L148 6f4f67af7faeeb38`. 3 parti (8+5+3). Tipi: **1 `DIALOG`**, **3 `TEXT`**, **6 `VALUE`**, **6 `DESCRIPTION`**;
zero `LOGBOOK`, zero `UI_LABEL`. **Arriva `<destination>`** accanto a `<planet>`: 31 token su 4 simboli, con parità per
simbolo, **ordine per unità** e due asserzioni di **assenza incrociata**. I **6 `VALUE` sono senza «the»** e il
controllo rifiuta `the <planet>`. Zero tab, zero virgolette. Numeri di dettaglio in
`staging/editorial/L148_20261019_174022/{review,REPORT,STATO}.md`.

L149 chiuso il 2026-10-19 — **scambi interspecie e trasferimenti**: righe **455–634**, **18 unità**, **246
parole**, `check.py` → `FAIL totale: 0` (**31 controlli**), `verify.py` → exit 0 (**25 controlli**), `sha256[:16]` =
`L149 b5f2ed112da6516f`. 3 parti (7+6+5). Tipi: **8 `VALUE`**, **8 `DESCRIPTION`**, **2 `TEXT`**; zero
`LOGBOOK`/`DIALOG`/`UI_LABEL`. **36 token su 4 simboli con due coppie di conteggi uguali** (10/10 e 8/8): il multiset
da solo è cieco, conta l'**ordine per unità**. Una `DESCRIPTION` **riletta da L148**; il `TEXT` degli operai ha una
variante **senza «the»** rispetto a L147 e la resa è nuova («su» non «sul»). Sostituito un controllo fittizio (`or True`)
con un'asserzione vera sulle chiavi. Numeri di dettaglio in
`staging/editorial/L149_20261019_180512/{review,REPORT,STATO}.md`.

**Batch L150–L153 chiuso il 2026-10-19**, quattro lotti di seguito in `data/coalition/coalition jobs.txt`:

| lotto | righe | unità | EN → IT | check / verify | sha256[:16] |
|---|---|---|---|---|---|
| L150 | 639–794 | 14 | 234 → 216 | 27 / 24 | `160a1592a36efff5` |
| L151 | 799–1171 | 37 | 302 → 316 | 27 / 24 | `8faf5d133a5b433c` |
| L152 | 1191–1359 | 21 | 527 → 531 | 25 / 24 | `580b5869e9f95bed` |
| L153 | 1360–1469 | 20 | 582 → 601 | 27 / 25 | `7b5d3d976e20fb6c` |

Il filo conduttore tecnico: **la resa si lega alla stringa inglese**, non alla famiglia di missione. L151 traduce **14
testi** per 37 unità con una mappa per stringa (le 8 copie di Cargo/Bulk restano una resa sola); L149 aveva già mostrato
che `on <planet>` e `on the <planet>` sono due frasi; L152–L153 conservano **l'inversione** di Arach e Saryd, che è la
voce delle specie e non un errore da correggere. Due controlli fittizi o sbagliati sono stati corretti in corsa («corriere»
in L151, «ogni/o è impegnato» in L153). Numeri di dettaglio in
`staging/editorial/L15{0,1,2,3}_*/{review,REPORT,STATO}.md`.

L196 chiuso il 2026-10-19 — **si torna al listino: apre `hai jobs.txt`**: righe **15–489**, **39 unità**, **499
parole**, `check.py` → `FAIL totale: 0` (**26 controlli**), `verify.py` → exit 0 (**19 controlli**), `sha256[:16]` =
`L196 e69389281fc1e23f`. Una parte. Tipi: **17 `VALUE`** (identici all'inglese), **16 `DESCRIPTION`**, **6 `TEXT`**
(tradotti: sono dialoghi). **Zero tab, 6 virgolette, 1 apice inglese contro 3 italiani** (`all'anno`). **72
segnaposto su nove simboli** in 32 unità, confrontati per **multiset di unità**. Quattro famiglie di ripetizioni
verificate come relazioni (8/10/12, 19/21/23, 30/32/34, 36/38). Il file resta aperto: **136 unità dopo la 489**,
quattro finestre. Numeri di dettaglio in `staging/editorial/L196_20261019_200808/{review,REPORT,STATO}.md`.

**Due numeri del documento precedente erano sbagliati** e sono stati rigenerati dai dati: `Token` dichiarato **0**
(misurati **72**) e la regola «`VALUE` **e** `TEXT` restano inglesi» (i `TEXT` in prosa sono tradotti da L108 a
L152; restano inglesi solo i nomi sotto contesti `ship:`). `check_handoff.py` non copre i segnaposto: la parola
«token» non compare nel checker.

L197 chiuso il 2026-10-19 — **ordini, scorte e trasporti**: righe **492–967**, **36 unità**, **488 parole**, `check.py`
→ `FAIL totale: 0` (**29 controlli**), `verify.py` → exit 0 (**19 controlli**), `sha256[:16]` = `L197 0ff30f8bb315b0ad`.
Tipi: **12 `VALUE`** identici, **15 `DESCRIPTION`**, **9 `DIALOG`** (nessun `TEXT`). **Zero tab, zero virgolette, zero
apici** — tre asserzioni vuote scritte. **81 segnaposto su 11 simboli**, tre nuovi (`<stopovers>`, `<planet stopovers>`
con lo spazio, `<fare>`). Due controlli di **coerenza cross-lot**: `Bring <fare>…` e `This human wishes for <cargo>…`
dovevano usare la resa già presente in staging, e la usano. Il primo `check.py` è uscito **`FAIL 1`**: l'asserzione
sulla famiglia «ordine speciale» confrontava tutto ciò che segue `<planet>` invece della sola frase condivisa; corretta
l'asserzione, non il testo. Il file è al **75/175 (42,9%)**, 100 unità dopo la 967. Numeri di dettaglio in
`staging/editorial/L197_20261019_202004/{review,REPORT,STATO}.md`.

L198 chiuso il 2026-10-19 — **il lotto dei trasporti ordinari, il più grande**: righe **988–1565**, **51 unità**,
**472 parole**, `check.py` → `FAIL totale: 0` (**29 controlli**), `verify.py` → exit 0 (**21 controlli**),
`sha256[:16]` = `L198 7465d06d0b238ebf`. Due parti. Tipi: **22 `VALUE`** (inglesi), **24 `DESCRIPTION`**, **5
`DIALOG`**. **Zero tab, 2 virgolette** (nel `VALUE` `Hai "prison" cruise`), **1 apice EN / 3 IT**, **112 segnaposto su
7 simboli**. Due template dominano il lotto — 11 copie di `Deliver <cargo>…`, 8 di `…by <date>…` — e il `check.py` li
verifica come **famiglie** (indici attesi + una sola resa). Le due stringhe avevano **rese precedenti concorrenti**
(`a`/`su <destination>`, `pagamento`/`compenso`): scelta dichiarata (`su` + `Il pagamento è`) e verifica che la resa
scelta appartenga all'insieme dei precedenti.

**L198 ha fatto emergere un errore di L197**: `You wish the mining family…` era già reso in L22 e io ne avevo creato
una variante. L197 è stato **riallineato**, rieseguito a exit 0, e lo sha passa da `f03d5d9459bc4414` a
`0ff30f8bb315b0ad` con tutti i documenti aggiornati. Il file è al **126/175 (72,0%)**, 49 unità dopo la 1565.

L199 chiuso il 2026-10-19 — **il turismo culturale Hai**: righe **1579–1750**, **26 unità**, **489 parole**, `check.py`
→ `FAIL totale: 0` (**28 controlli**), `verify.py` → exit 0 (**21 controlli**), `sha256[:16]` =
`L199 6af91de2eec66a88`. Tipi: **9 `VALUE`** identici, **8 `DESCRIPTION`**, **9 `DIALOG`**. **Zero tab, zero
virgolette**, **2 apici EN / 0 IT** (possessivo), **42 segnaposto su 3 simboli**. Quattro famiglie di eventi in due
taglie: le coppie `[1]`/`[2]` differiscono **solo** per `grande` e le quattro coppie di `DIALOG` sono **identiche**
dentro la coppia — il `check.py` verifica le relazioni, non le unità isolate. **Il confine non chiude la missione**:
la 1750 (`VALUE`) e la 1753 (`DESCRIPTION`) sono entrambe `Superstitious Hai [1]`, e il `verify.py` lo misura. Il file
è al **152/175 (86,9%)**. Numeri di dettaglio in `staging/editorial/L199_20261019_203531/{review,REPORT,STATO}.md`.

L200 chiuso il 2026-10-19 — **il lotto terminale: `hai jobs.txt` è finito, 175/175**. Righe **1753–2067**, **23
unità**, **354 parole**, `check.py` → `FAIL totale: 0` (**25 controlli**), `verify.py` → exit 0 (**17 controlli**),
`sha256[:16]` = `L200 3ff06bf4f8b326c1`. Tipi: **11 `VALUE`** identici, **12 `DESCRIPTION`**, nessun `DIALOG`. **Zero
tab, zero virgolette, zero apici**, **57 segnaposto su 5 simboli**. Sei coppie con/senza la frase sul keystone
(`[1]…[6]` contro `[7]…[12]`), verificate togliendo la frase e confrontando; accordo «Ha/Hanno chiesto»; termine
unico «chiave di volta» (18 occorrenze, mai «pietra chiave»). L'invariante di FILE copre le **cinque finestre
L196…L200 = 175 unità su 175 righe distinte**. Numeri di dettaglio in
`staging/editorial/L200_20261019_204235/{review,REPORT,STATO}.md`.

L201 chiuso il 2026-10-19 — **apre `hai outfits.txt`: descrizioni di equipaggiamento**. Righe **27–164**, **8 unità**,
**450 parole**, `check.py` → `FAIL totale: 0` (**24 controlli**), `verify.py` → exit 0 (**15 controlli**),
`sha256[:16]` = `L201 76f769f988aefc73`. Tipi: **8 `DESCRIPTION`**, nessun `VALUE`/`DIALOG`/`TEXT`. **ZERO
segnaposto** (asserzione negativa scritta), **2 tab**, **2 virgolette**, **0 apici EN / 5 IT** (elisione). Nomi di
prodotto invariati; `Pulse Turret` e `Ion Cannon` **non compaiono nel testo** (solo nei contesti) e il `check.py` lo
dichiara. Il file è all'**8/65 (12,3%)**. Numeri di dettaglio in
`staging/editorial/L201_20261019_204959/{review,REPORT,STATO}.md`.

L202 chiuso il 2026-10-19 — **armi e munizioni Hai**: righe **205–484**, **16 unità**, **436 parole**, `check.py` →
`FAIL totale: 0` (**24 controlli**), `verify.py` → exit 0 (**17 controlli**), `sha256[:16]` = `L202 2281312fe0da11a4`.
Tipi: **13 `DESCRIPTION`** e **3 `VALUE`** (`Skipper Railgun Slug`, `Skipper Slug Rack`, `Skipper Railgun`). **Zero
segnaposto**, **4 tab**, **zero virgolette**, **2 apici EN / 10 IT** (contrazione inglese contro elisione italiana).
Unità 11 e 15 hanno la stessa stringa inglese e la stessa resa. `outfitter` reso con «negozio di equipaggiamenti»
(glossario). Il refuso del sorgente *jamming affects* resta nel gioco ed è dichiarato. Il file è al **24/65 (36,9%)**.
Numeri di dettaglio in `staging/editorial/L202_20261019_205624/{review,REPORT,STATO}.md`.

L203 chiuso il 2026-10-19 — **difese e contromisure Hai**: righe **508–600**, **9 unità**, **442 parole**, `check.py` →
`FAIL totale: 0` (**24 controlli**), `verify.py` → exit 0 (**17 controlli**), `sha256[:16]` = `L203 81a25808d92d805f`.
Tipi: **9 `DESCRIPTION`**, nessun `VALUE`. **Zero segnaposto**, **1 tab**, zero virgolette, **1 apice EN / 4 IT**.
Lotto denso di **glossario**: «generatori di scudi», «matrice dello scudo» (2 volte), «disturbatore» per jammer,
«chiave di volta» per keystone. Errore d'accordo del sorgente (*the shifts … causes*) dichiarato, non corretto. Il file
è al **33/65 (50,8%)**. Numeri di dettaglio in `staging/editorial/L203_20261019_210258/{review,REPORT,STATO}.md`.

L204 chiuso il 2026-10-19 — **alimentazione Hai**: righe **603–788**, **19 unità**, **441 parole**, `check.py` →
`FAIL totale: 0` (**22 controlli**), `verify.py` → exit 0 (**18 controlli**), `sha256[:16]` = `12342441647f81f7`.
**13 `DESCRIPTION` + 6 `VALUE`**, **6 virgolette dentro i nomi** (`"Baellie" Atomic Engines`), zero tab, 2 apici EN / 6 IT.
Errore mio corretto: «battery pack» compare **4** volte, non 5 (l'unità 10 dice *battery model*); il controllo ora lega
il conteggio italiano a quello inglese.

L205 chiuso il 2026-10-19 — **propulsori Hai, lotto terminale**: righe **805–984**, **13 unità**, **520 parole**,
`check.py` → `FAIL totale: 0` (**23**), `verify.py` → exit 0 (**16**) con **invariante di FILE**, `sha256[:16]` =
`968d32112e56b1d4`. **`hai outfits.txt` CHIUSO a 65/65** (L201–L205). 1 tab, 2 virgolette, 1 apice EN / 4 IT. Errore
mio corretto: i `...` dell'unità 10 stanno **a metà frase**, non in coda.

L206 chiuso il 2026-10-19 — **primo file di tipo `NEWS`**: `coalition news.txt`, righe **28–94**, **20 unità**, **440
parole**, `check.py` → `FAIL totale: 0` (**25**), `verify.py` → exit 0 (**17**), `sha256[:16]` = `7cff828f2fb7e44b`.
**40 virgolette** (2 per unità), 4 contesti, zero tab e zero segnaposto. **Decisione del lotto: il registro Saryd** —
inversione riprodotta nel discorso citato, italiano naturale nella narrazione; marcatore verificabile = chiusura con
verbo flesso (9 unità).

L207 chiuso il 2026-10-19 — **secondo lotto di `coalition news.txt`**: righe **95–176**, **17 unità**, **432 parole**,
`check.py` → `FAIL totale: 0` (**23**), `verify.py` → exit 0 (**17**), `sha256[:16]` = `af8d352da08f8841`. **Tutte** le
unità sono citazioni (34 virgolette); 14 su 17 chiudono con un verbo, le altre 3 chiudono in ordine normale **come nel
sorgente**. Il file è al **37/112 (33,0%)**.

L208 chiuso il 2026-10-19 — **terzo lotto di `coalition news.txt`**: righe **177–246**, **19 unità**, **436 parole**,
`check.py` → `FAIL totale: 0` (**24**), `verify.py` → exit 0 (**17**), `sha256[:16]` = `a7a74f3da74a7f29`. 38 virgolette,
5 contesti, zero tab e zero segnaposto. **17 unità chiudono con un verbo e le 2 che non lo fanno sono esattamente le due
di narrazione** (1 e 12): è il marcatore più pulito dei tre lotti della Coalizione.

L209 chiuso il 2026-10-19 — **quarto lotto di `coalition news.txt`**: righe **247–308**, **21 unità**, **432 parole**,
`check.py` → `FAIL totale: 0` (**24**), `verify.py` → exit 0 (**19**), `sha256[:16]` = `7e550942341d014e`. **Nove unità
sono tre stringhe ripetute tre volte** sotto contesti `arach/kimek/saryd civilian`: le famiglie devono coincidere fra le
due lingue e le copie essere identiche, e il controllo verifica le **partizioni**, non i totali. Errori miei corretti:
le chiavi dei contesti civilian **non** hanno il prefisso `coalition`, e la citazione inglese è `'field trip,'` con la
virgola dentro le virgolette. Il file è al **77/112 (68,8%)**.

L210 chiuso il 2026-10-19 — **quinto lotto di `coalition news.txt`**: righe **309–400**, **19 unità**, **458 parole**,
`check.py` → `FAIL totale: 0` (**23**), `verify.py` → exit 0 (**17**), `sha256[:16]` = `ee5ce8eed7ac5542`. Entra nei
**Giochi della Coalizione** (7 occorrenze, «Giochi della Coalizione») e chiude il filone di **Sedlitaris**, promossa
*arbiter*. 24 apici italiani contro 4 inglesi. Due errori miei corretti: la virgola **dentro** le virgolette
(`'field trip,'`) e `endswith` su stringhe che finiscono con `."`.

L211 chiuso il 2026-10-19 — **sesto e ultimo lotto di `coalition news.txt`**: righe **401–496**, **16 unità**, **378
parole**, `check.py` → `FAIL totale: 0` (**25**), `verify.py` → exit 0 (**19**) con **invariante di FILE**, `sha256[:16]` =
`2a3bcc367bdd3978`. **`coalition news.txt` CHIUSO a 112/112.** Il tratto del lotto è la **citazione spezzata**: le unità 6
e 11 sono una sola virgoletta ciascuna (aperta alla 458, chiusa alla 465, quattro paragrafi in mezzo senza virgolette). Il
controllo verifica la **distribuzione per unità** (`2,2,2,2,2,1,0,0,0,0,1,2,2,2,2,2`), non il totale.

L212 chiuso il 2026-10-19 — **primo lotto di `deep jobs.txt`**: righe **16–322**, **45 unità**, **442 parole**, `check.py`
→ `FAIL totale: 0` (**26**), `verify.py` → exit 0 (**19**), `sha256[:16]` = `d3561b72157dd31c`. **Forma nuova**: 28 `TEXT`
sono **frammenti di frase** che il gioco concatena, 8 `VALUE` restano inglesi, 9 `DESCRIPTION` tradotte, **31 segnaposto**
su 6 simboli confrontati **per unità**. Il marcatore della composizione è la **maiuscola iniziale** del frammento.

L213 chiuso il 2026-10-19 — **secondo lotto di `deep jobs.txt`**: righe **333–453**, **22 unità**, **436 parole**,
`check.py` → `FAIL totale: 0` (**25**), `verify.py` → exit 0 (**18**), `sha256[:16]` = `a1c19c89ae374d9f`.
**Primo lotto con `DIALOG`** (7): prosa parlata, **senza** inversione Saryd — il controllo verifica l'assenza dei
marcatori della Coalizione in quei testi. **24 segnaposto su 7 simboli**, con `<npc>` quattro volte in funzioni
sintattiche diverse (soggetto con articolo, genitivo, subordinata). Coerenza cross-lot verificata: «la struttura su
<stopovers>» (L212) e «Il pagamento è <payment>» (L198). Il file è al **67/187 (35,8%)**.

L214 chiuso il 2026-10-19 — **terzo lotto di `deep jobs.txt`**: righe **457–682**, **35 unità**, **431 parole**,
`check.py` → `FAIL totale: 0` (**26**), `verify.py` → exit 0 (**19**), `sha256[:16]` = `e2d9f07af3bd3c95`.
**15 tab** dentro 16 `MISSION_TEXT` e 1 `LOGBOOK`: sono separatori di paragrafo e il controllo li verifica **per unità**
(uno nelle 21–35, sempre iniziale). La preposizione della consegna sta **dentro le sei alternative**, non nel frammento
d'apertura, perché in italiano dipende dal genere. **Registro «tu»** anche nel dialogo formale di Wayde («Accomodati»,
mai «Si accomodi»). Confine riga **683**: il primo **`UI_LABEL`** della campagna, un tipo che non entra in staging.

L215 chiuso il 2026-10-19 — **quarto lotto di `deep jobs.txt`**: righe **684–864**, **25 unità**, **431 parole**,
`check.py` → `FAIL totale: 0` (**25**), `verify.py` → exit 0 (**19**), `sha256[:16]` = `0b4212a734b678ff`.
**La battuta**: Wayde dice *at any rate* due volte e il giocatore glielo fa notare citandolo; la resa «in ogni caso»
compare **tre volte** in entrambe le lingue e il controllo verifica le tre posizioni. **Citazione su due paragrafi**:
l'unità 1 apre e non chiude (29 virgolette con distribuzione per unità). **`<date>`** per la prima volta, senza articolo.
L'`UI_LABEL` della riga 683 resta fuori dalla finestra: le unità prima della 684 sono **103**, e l'invariante torna con
`127 + 1 + 59 = 187`.

L216 chiuso il 2026-10-19 — **quinto lotto di `deep jobs.txt`**: righe **866–929**, **30 unità**, **439 parole**,
`check.py` → `FAIL totale: 0` (**25**), `verify.py` → exit 0 (**19**), `sha256[:16]` = `193651028d79b6bd`.
Tre tipi insieme: 14 `MISSION_TEXT` (dialogo di **Julie Gillar**, 13 tab), 1 `LOGBOOK`, 15 `TEXT` in due blocchi di
frammenti. **Due segnaposto nuovi**: `<last>` (cognome) e `<passengers>` (numero). Errore mio corretto: avevo assertato
che il `LOGBOOK` fosse in terza persona, ma il sorgente dice *from you* — il diario apre descrivendo Julie e poi parla al
giocatore. Confine riga **935**, un `VALUE`, **sei righe dopo** l'ultima unità.

L217 chiuso il 2026-10-19 — **sesto e ULTIMO lotto di `deep jobs.txt`**: righe **935–1234**, **29 unità**, **375 parole**,
`check.py` → `FAIL totale: 0` (**27**), `verify.py` → exit 0 (**18**), `sha256[:16]` = `379596a8a8be9b81`. **File chiuso**:
186 righe tradotte in sei finestre (45 + 22 + 35 + 25 + 30 + 29) più l'`UI_LABEL` della riga 683 = **187/187**.
**56 segnaposto su 9 simboli**, il record della campagna, verificati **per unità e nell'ordine**. Errore mio corretto: le
famiglie di `VALUE` sono `[1,1,1,2,2,5]` («Shipment to `<planet>`» **cinque** volte), non `[1,1,1,1,2,2]`.

L218 chiuso il 2026-10-19 — **primo lotto di `successor ships.txt`** (file nuovo): righe **17–381**, **45 unità**,
**499 parole**, `check.py` → `FAIL totale: 0` (**28**), `verify.py` → exit 0 (**17**), `sha256[:16]` = `9e3e6ea15d7e3638`.
**La regola del file**: 39 unità su 45 restano **identiche all'inglese** (35 `TEXT` = nomi di equipaggiamento, 4 `VALUE` =
nomi di specie) e si traducono solo le **6 `DESCRIPTION`**. Errore mio corretto: gli apici inglesi stanno nelle unità 15,
31 e **32**, gli italiani in 15, 31 e **45** — il totale coincideva (4 e 4) ma la distribuzione no, e ora si confrontano le
coppie (unità, conteggio).

L219 chiuso il 2026-10-19 — **secondo lotto di `successor ships.txt`**: righe **386–629**, **25 unità**, **467 parole**,
`check.py` → `FAIL totale: 0` (**27**), `verify.py` → exit 0 (**16**), `sha256[:16]` = `26062019d4d6d536`.
**19 unità su 25 identiche all'inglese** (16 `TEXT` + 3 `VALUE`), 6 `DESCRIPTION` tradotte. **Tratto nuovo**: le due
schede della stessa nave condividono frasi (*This tiny shuttle is the smallest vessel…*, *neither elegant nor fast*) e le rese
devono restare identiche — verificate con `startswith` e `in`. Apici 3 EN / 10 IT in unità diverse: confronto a coppie.

L220 chiuso il 2026-10-19 — **terzo lotto di `successor ships.txt`**: righe **634–873**, **26 unità**, **440 parole**,
`check.py` → `FAIL totale: 0` (**28**), `verify.py` → exit 0 (**18**), `sha256[:16]` = `3373e098d9af319f`.
**Coppia 23/25**: stesso testo, differenza di **due virgolette** (`l'"Ojde"` / `l'Ojde`), verificata in EN e IT.
**Le 34 virgolette** = 32 delle 16 `TEXT` + **2 in una `DESCRIPTION`**: il contratto L220 lo prevedeva e la misura l'ha
confermato. **Errore mio grave**: avevo **trascritto a mano** i nomi delle `TEXT` e 11 unità su 20 erano sbagliate (nomi veri,
presi dalle unità sbagliate). Correzione **strutturale**: `parts/part01.json` ora si **genera dal sorgente** per `TEXT` e
`VALUE`, e solo le `DESCRIPTION` vengono dalle traduzioni.

L221 chiuso il 2026-10-19 — **quarto lotto di `successor ships.txt`**: righe **904–1137**, **24 unità**, **451 parole**,
`check.py` → `FAIL totale: 0` (**28**), `verify.py` → exit 0 (**18**), `sha256[:16]` = `b7a2199bbf3b9e42`.
**Tre formule condivise** fra le due schede della Stolsaqra (15/17) e con la 16: potenza di fuoco, problemi di propulsione,
modello riservato ai militari — rese una volta e verificate in tutte le unità che le portano. **3 tab, tutti in
`DESCRIPTION`** (7, 16, 24); **30 virgolette tutte nelle `TEXT`**, nessuna in prosa. `drag cannon` non è un nome nel
database: reso «cannone a trascinamento», coerente con «effetti di rallentamento» di L220.

L222 chiuso il 2026-10-19 — **quinto e ULTIMO lotto di `successor ships.txt`**: righe **1141–1338**, **26 unità**, **431
parole**, `check.py` → `FAIL totale: 0` (**29**), `verify.py` → exit 0 (**20**), `sha256[:16]` = `30ae0dcd3ae347d4`.
**FILE CHIUSO 146/146**: `45 + 25 + 26 + 24 + 26`, **senza `UI_LABEL`**. Due coerenze verificate: le schede **12/14** della
Vujlet (testo condiviso identico **e** differenza di punteggiatura conservata) e la formula della Veusade che torna da
L221. `cloak`/`cloaking`/`stealth` tenuti distinti: occultamento / ricognizione furtiva / equipaggiamento occultante.

L223 chiuso il 2026-10-19 — **primo lotto di `remnant outfits.txt`** (file nuovo): righe **48–297**, **12 unità**, **463
parole**, `check.py` → `FAIL totale: 0` (**28**), `verify.py` → exit 0 (**18**), `sha256[:16]` = `865540cb64989e26`.
**Il rovesciamento**: 11 `DESCRIPTION` + 1 `VALUE`, cioè si traduce quasi tutto (in `successor ships.txt` erano 100 `TEXT`
di nomi da copiare). **La linea del lotto**: i nomi degli equipaggiamenti restano inglesi anche nella prosa, le parole
comuni si traducono (`cannon` → «cannone/cannoni», `turret` → «torretta/torrette», `torpedo` → «siluro/siluri»).
Errore mio corretto: il controllo cercava «cannone» al singolare, il testo dice «cannoni» — ora usa una regex.

L224 chiuso il 2026-10-19 — **secondo lotto di `remnant outfits.txt`**: righe **298–565**, **13 unità**, **472 parole**,
`check.py` → `FAIL totale: 0` (**28**), `verify.py` → exit 0 (**18**), `sha256[:16]` = `bee38f3d2fc80881`.
**Primato**: **zero unità da copiare** (13 `DESCRIPTION` su 13) → confronto **0 identiche / 13 tradotte**, scritto come
asserzione. **9 tab su 13 unità**, densità più alta della campagna. **Tre unità (1, 5, 8) con la stessa riga di servizio**,
resa identica e confrontata con `==`. Gioco di parole di `Ember Tear` (*strappare* o *piangere*) reso con «micro-strappi»
e «piangere», con `'both.'` → «'entrambe le cose'» fra apici singoli. Errore mio corretto: cercavo «originariamente» dentro
il testo inglese (`originally`).

L225 chiuso il 2026-10-19 — **terzo lotto di `remnant outfits.txt`**: righe **581–674**, **11 unità**, **455 parole**,
`check.py` → `FAIL totale: 0` (**25**), `verify.py` → exit 0 (**18**), `sha256[:16]` = `66b157150c05ada7`.
**Ancora zero da copiare** (11 `DESCRIPTION`), ma **i tab scendono da 9 a 4**: la densità di L224 non si eredita. La famiglia
di `ion` resa in quattro forme con «ionica» ripetuta solo **2** volte su misura. Le «branchie» fra virgolette (unità 8).
Errore mio corretto: il controllo pretendeva «tempesta ionica» al singolare, che il testo non usa.

L226 chiuso il 2026-10-19 — **quarto lotto di `remnant outfits.txt`**: righe **675–864**, **11 unità**, **445 parole**,
`check.py` → `FAIL totale: 0` (**26**), `verify.py` → exit 0 (**19**), `sha256[:16]` = `7418d831f5d6ba86`.
**Zero virgolette**, asserite in entrambe le lingue: un controllo che tace su uno zero non distingue «non ce ne sono» da «non
le ho guardate». **3 tab** dopo 4 (L225) e 9 (L224): tre conteggi diversi in tre lotti dello stesso file. **9 contesti su 11
unità**: due sole coppie, e il controllo non ne inventa altre.

L227 chiuso il 2026-10-19 — **quinto e ULTIMO lotto di `remnant outfits.txt`**: righe **884–979**, **10 unità**, **382
parole**, `check.py` → `FAIL totale: 0` (**24**), `verify.py` → exit 0 (**20**), `sha256[:16]` = `ba3673a78c7a0d5e`.
**FILE CHIUSO 57/57**: `12 + 13 + 11 + 11 + 10`, **senza `UI_LABEL`**. **Torna un'unità da copiare** (il `VALUE` della
riga 948): dopo tre lotti a zero identiche, il confronto è **1 / 9** — dipende dalla composizione della finestra, non da una
regola sul file. **Zero virgolette** per il secondo lotto di fila, asserite. L'ultima unità è una **licenza**, non un
equipaggiamento.

L228 chiuso il 2026-10-19 — **primo lotto di `korath outfits.txt`** (file nuovo, misto): righe **16–195**, **20 unità**,
**434 parole**, `check.py` → `FAIL totale: 0` (**27**), `verify.py` → exit 0 (**20**), `sha256[:16]` = `49228f599876094f`.
**Due primati negativi asseriti**: **zero tab** (mai successo) e **zero virgolette** (terzo lotto di fila). **Primo file
misto**: 7 `VALUE` copiati e 13 `DESCRIPTION` tradotte, con il controllo che verifica **quali** unità sono identiche, non solo
quante. Caso nuovo: `Fusion Reactor` maiuscolo resta nome, `fusion reactor` minuscolo si traduce.

L229 chiuso il 2026-10-19 — **secondo lotto di `korath outfits.txt`**: righe **208–318**, **15 unità**, **431 parole**,
`check.py` → `FAIL totale: 0` (**27**), `verify.py` → exit 0 (**18**), `sha256[:16]` = `b85fa00ea11fb613`.
**Tre unità quasi identiche**: 10 e 13 identiche parola per parola, la 7 con un `may` in più (reso «può quasi fondere»).
**I tab tornano a 3** dopo lo zero di L228. Il confine **spezza una scheda** (`Afterburner (Planetary Class)`), e il
`verify.py` lo registra confrontando i contesti. Errore mio corretto: avevo dedotto «2 unità per Afterburner», il valore
misurato era **3/3/3/2**.

L230 chiuso il 2026-10-19 — **terzo lotto di `korath outfits.txt`**: righe **319–581**, **26 unità**, **430 parole**,
`check.py` → `FAIL totale: 0` (**27**), `verify.py` → exit 0 (**19**), `sha256[:16]` = `d246b4e6c38a2e78`.
**10 `VALUE`** (massimo per un lotto misto) e **7 tab**. **Due gruppi di testi ripetuti**: le unità 1 e 4 ripetono una frase
già tradotta in **L229** (primo controllo **inter-lotto**, `by[1] == prev[300]`) e le unità 11/14/17/20/23 sono **cinque
copie** con una sola resa. Errore mio corretto: `startswith` senza `.strip()` cadeva sul tab iniziale.

L231 chiuso il 2026-10-19 — **quarto lotto di `korath outfits.txt`**: righe **596–808**, **21 unità**, **455 parole**,
`check.py` → `FAIL totale: 0` (**27**), `verify.py` → exit 0 (**19**), `sha256[:16]` = `39c7cbdeb1825d8b`. **Zero tab** dopo i
7 di L230 e **zero virgolette** (sesto lotto). Due nomi di scena nuovi: **Quarg** ed **Efreti** (5 e 5 occorrenze). Due errori
miei corretti, entrambi **numeri dedotti invece che misurati**: il residuo dopo la 808 ha **0** `VALUE` (avevo scritto 2) e i
nomi di scena sono **5** ciascuno (avevo scritto 4).

L232 chiuso il 2026-10-20 — **quinto e ULTIMO lotto di `korath outfits.txt`**, che **chiude il file a 92/92**: righe
**809–908**, **10 unità**, **454 parole**, `check.py` → `FAIL totale: 0` (**31 controlli**), `verify.py` → exit 0 (**19
controlli**, invariante di FILE), `sha256[:16]` = `f0ac63cba4ffbcb3`. **Primo lotto della campagna con sole
`DESCRIPTION`**: zero `VALUE`, quindi il confronto è **0 identiche / 10 tradotte** e l'asserzione è che *nessuna* unità
resti identica. **I tab risalgono a 4** (1, 5, 7, 10) dopo lo zero di L231, quinto conteggio consecutivo diverso nel file
(0 · 3 · 7 · 0 · **4**); **le virgolette tornano a 2** dopo sei lotti a zero e stanno entrambe in una sola unità
(`"escape,"`), con la virgola **dentro** le virgolette, riprodotta. **5 apici inglesi contro 3 italiani** per ragioni
opposte (contrazione contro elisione). Una divergenza dichiarata: `jump drive` → «motore di salto» (334 occorrenze nel
corpus contro 13) invece del «jump drive» di L231 unità 19. Numeri di dettaglio in
`staging/editorial/L232_20261020_120116/{review,REPORT,STATO}.md`.

L233 chiuso il 2026-10-20 — **primo lotto di `data/avgi/avgi news.txt`**: righe **32–91**, **22 unità**, **447 parole**,
`check.py` → `FAIL totale: 0` (**33 controlli**), `verify.py` → exit 0 (**20 controlli**), `sha256[:16]` =
`14b34f5d9e29558c`. **22 `NEWS`**, zero `VALUE`, zero `UI_LABEL`, zero tab, **44 virgolette = 2 per unità**: ogni unità è
**una citazione intera**, il contrario di `coalition news.txt` dove la citazione si spezzava su più unità. **Tre
contesti** completi: `siege civilian` 11, `siege merchant` 5, `siege hatchling` 6. **12 apici inglesi contro 5
italiani** (contrazione contro elisione). Il tratto del lotto è il **registro**: 22 etichette di modalità Avgi
(`Scoramento.`, `Rifiuto.`, `Ricordo.`, `Colpa.`, `Preoccupazione.`, `Dolore.`, `Rabbia.`, `Curiosità.`,
`Soddisfazione.`, `Ottimismo.`, `Sollievo.`, `Frustrazione.`, `Placazione.`, `Esasperazione.`, `Meraviglia.`,
`Confusione.`, `Tristezza.`, `Offesa.`, `Perdita.`, `Disperazione.`), riprodotte come etichette e non liquefatte in
avverbi; `Dejection` non è «deiezione» (termine clinico) ma «Scoramento». `Aberration`/`Aberrations`/`Aberrant` resi con
un solo nome della fazione. Segmento: **22/115 (19,1%)**, 0 prima della 32, 93 dopo la 91, confine riga 115. Numeri di
dettaglio in `staging/editorial/L233_20261020_123813/{review,REPORT,STATO}.md`.

L234 chiuso il 2026-10-20 — **secondo lotto di `data/avgi/avgi news.txt`**: righe **115–180**, **20 unità**, **439
parole**, `check.py` → `FAIL totale: 0` (**33 controlli**), `verify.py` → exit 0 (**21 controlli**), `sha256[:16]` =
`a1598c95777cbd57`. Tre contesti (`merchant` 10, `politician` 6, `military` 4), citazioni **intere** (40 virgolette, 2
per unità), zero tab. **19 etichette su 20**: la **177** non ne ha ed è una **domanda Avgi** che finisce con
«, domanda?» (dispositivo di L48) — il `check.py` confronta la lista **con quel `None`**. **6 apici inglesi contro 12
italiani**, il contrario di L233 (qui l'italiano elide più di quanto l'inglese contragga). Chiusa la questione lasciata
aperta in L233: **`the Guard` → «la Guardia»** (28 occorrenze nel corpus). `polities` → «entità politiche» (10
occorrenze). Segmento 42/115 (36,5%), confine riga 197. Numeri di dettaglio in
`staging/editorial/L234_20261020_124648/{review,REPORT,STATO}.md`.

L235 chiuso il 2026-10-20 — **terzo lotto, di sola composizione**: righe **197–280**, **15 unità**, **72 parole**,
`check.py` → `FAIL totale: 0` (**32 controlli**), `verify.py` → exit 0 (**21 controlli**), `sha256[:16]` =
`d6825410bf2929d6`. **6 prefissi** (`"Cautela. ` … `"Vigilanza. `, con lo **spazio finale**) × **7 messaggi** (punto e
virgoletta **in coda**) = **42 combinazioni**, verificate una per una in inglese e in italiano; il meccanismo è stato
letto nel sorgente (`Phrase::Get()` concatena **senza separatore**). Due unità di sola punteggiatura (`"` e `.`),
identiche per necessità e dichiarate in `ID_OK`. **Lacuna dichiarata**: `avgi missing advisory` ha **13 blocchi
`word`** e il database ne conserva **solo il primo e l'ultimo** — quella notizia resterà quasi tutta in inglese, e il
`verify.py` lo dimostra con una query **e** con una lettura del file del gioco. Segmento 57/115 (49,6%), confine riga
301. Numeri di dettaglio in `staging/editorial/L235_20261020_124916/{review,REPORT,STATO}.md`.

L236 chiuso il 2026-10-20 — **quarto lotto di `data/avgi/avgi news.txt`**: righe **301–344**, **23 unità**, **348
parole**, `check.py` → `FAIL totale: 0` (**36 controlli**), `verify.py` → exit 0 (**21 controlli**), `sha256[:16]` =
`df51440678f593e2`. Due contesti (`student happy` 13, `student frustrated` 10), citazioni **intere** (46 virgolette, 2
per unità), zero tab. **Tre coppie di inglese identico** (10/20, 12/22, 13/23) con resa **identica**, verificata
confrontando le stringhe; **una coppia quasi identica** (11/21) che differisce **solo nell'etichetta in coda**
(`…, divertimento.` / `…, scoramento.`): è l'unico punto del file in cui la modalità non apre la frase. **Quattro unità
senza etichetta** (10, 11, 20, 21). Il genere dello studente non è nel testo, quindi tre frasi evitano il participio
concordato («mi ha fatto passare», «mi hanno deriso», «di aver fatto bene»). Segmento 80/115 (69,6%), confine riga 369.
Numeri di dettaglio in `staging/editorial/L236_20261020_130628/{review,REPORT,STATO}.md`.

L237 chiuso il 2026-10-20 — **quinto lotto di `data/avgi/avgi news.txt`**: righe **369–399**, **14 unità**, **356
parole**, `check.py` → `FAIL totale: 0` (**36 controlli**), `verify.py` → exit 0 (**21 controlli**), `sha256[:16]` =
`4ffa812d37566858`. Due contesti (`physicist` 8, `astronomer` 6), citazioni **intere** (28 virgolette, 2 per unità), zero
tab, zero segnaposto. **Tre cose proprie del lotto**: un **refuso del sorgente** (`Frustation.` alle righe 370 e 371),
tradotto «Frustrazione» e **non** replicato — il `check.py` cita l'etichetta inglese *come sta*; una **normalizzazione
dichiarata** (`the Twilight nebula` minuscolo in 395 → sempre `Twilight Nebula`: IT 3, EN 2); **otto apici in una sola
unità** (398: `'Nord'`, `'Ovest'`, `'senso di rotazione'`, `'verso il bordo'`), il massimo della campagna per unità.
Lessico tecnico nuovo fissato: «vortici di scia», «diamante di memoria», «nebulosa a riflessione», «nube molecolare»,
«equilibrio idrostatico», «vivaio stellare», «vie stellari», «resistenza aerodinamica». Segmento 94/115 (81,7%), confine
riga 418. Numeri di dettaglio in `staging/editorial/L237_20261020_132134/{review,REPORT,STATO}.md`.

L238 chiuso il 2026-10-20 — **sesto e ULTIMO lotto di `data/avgi/avgi news.txt`, che CHIUDE il file a 115/115**: righe
**418–507**, **21 unità**, **502 parole**, `check.py` → `FAIL totale: 0` (**37 controlli**), `verify.py` → exit 0
(**21 controlli**, invariante di **FILE**), `sha256[:16]` = `21ea58dec8dd91bb`. **Quattro mestieri** in un lotto solo
(`engineer` 7, `artist` 3, `performer` 3, `doctor` 8) e una finestra **discontinua** (425–451, 455–477, 481–499 senza
unità): non è un buco, è la struttura del file, e il `check.py` lo asserisce. **Cinque etichette nuove**: `Appreciation` →
«Apprezzamento» (3), `Fascination` → «Fascinazione» (2), `Consideration` → «Considerazione» (2), `Advisement` →
«Avviso» (1, **non** «Avvertenza» che è `Warning`), `Recollection` → «Rievocazione» (2, **non** «Ricordo» che è
`Remembrance`). **Un'etichetta a metà frase** (454: `art is a waste, emphasis.` → «… uno spreco, enfasi.»), terza
posizione possibile dopo la testa (L233–L237) e la coda (L236). `Twilight Guard` invariato (30 precedenti) con i
**membri** tradotti («le Guardie»). Invariante di FILE: `22 + 20 + 15 + 23 + 14 + 21 = 115`, riga 507 ultima, 0 dopo,
115 id distinti. **Ottavo file completo della campagna.** Due rossi al primo giro, **entrambi nelle asserzioni**: la lista
tipografica vietava `un'opera`/`un'officina` (elisioni corrette) e il controllo sui puntini leggeva `cov[15]` invece di
`cov[14]`. Numeri di dettaglio in `staging/editorial/L238_20261020_133346/{review,REPORT,STATO}.md`.

L239 chiuso il 2026-10-20 — **primo lotto di `data/avgi/avgi jobs.txt`**: righe **20–656**, **62 unità** (**31 `VALUE`** +
**31 `DESCRIPTION`**), **432 parole**, `check.py` → `FAIL totale: 0` (**30 controlli**), `verify.py` → exit 0
(**22 controlli**), `sha256[:16]` = `09003f2358701239`. **31 contesti da due unità**, **zero tab, zero virgolette, zero
apici** (tre asserzioni negative scritte), **133 segnaposto** in 6 famiglie. **Sei famiglie `DESCRIPTION`** per 31 unità
(15 · 9 · 2 · 2 · 1 · 2): una sola resa ciascuna, verificata **come famiglia**; la stringa da 15 copie riprende
**identica** la resa già presente 24 volte nel corpus, e il `check.py` la cerca nei `translation.json` precedenti. **I 31
`VALUE` restano inglesi** (linea dei due lotti di lavori più recenti, L151 e L198) mentre **sette unità di file antichi**
avevano tradotto `Rush delivery` — divergenza dichiarata. `<planet>` e `<destination>` hanno **lo stesso conteggio** (31):
il `verify.py` confronta anche **l'ordine** dei segnaposto per unità. Segmento 62/102 (60,8%), confine riga 684. Numeri di
dettaglio in `staging/editorial/L239_20261020_134411/{review,REPORT,STATO}.md`.

L240 chiuso il 2026-10-20 — **secondo e ULTIMO lotto di `data/avgi/avgi jobs.txt`, che CHIUDE il file a 102/102**: righe
**684–1156**, **40 unità** (20 `VALUE` + 20 `DESCRIPTION`), **470 parole**, `check.py` → `FAIL totale: 0` (**31
controlli**), `verify.py` → exit 0 (**25 controlli**, invariante di **FILE**), `sha256[:16]` = `50d99adb0435c12d`.
**20 contesti**, zero tab e zero virgolette, **99 segnaposto** in **7** famiglie. **Due cose nuove**: `<origin>` (6, sempre
**prima** di `<destination>`: la partenza non si inverte) e il `the` **dentro** un `VALUE` (`Construction materials to the
<planet>`), che resta identico perché è un dato. **Gli unici due apostrofi sono il possessivo `<planet>'s`** (988, 1009):
in italiano diventano **zero** («la rete locale di `<planet>`»), e la differenza è asserita. **8 famiglie `DESCRIPTION`**
(6·3·3·3·2·1·1·1) e 4 gradi dei **Twilight Guard** (membri / ufficiali / ufficiali superiori / Guardie). **Nono file
completo della campagna.** Numeri di dettaglio in `staging/editorial/L240_20261020_135130/{review,REPORT,STATO}.md`.

L241 chiuso il 2026-10-20 — **primo lotto di `data/successors/successor jobs.txt`**: righe **16–280**, **86 unità**
(**76 `TEXT`** + 5 `VALUE` + 5 `DESCRIPTION`), **428 parole**, `check.py` → `FAIL totale: 0` (**33 controlli**),
`verify.py` → exit 0 (**28 controlli**), `sha256[:16]` = `19c694523a5473df`. **Il lotto della COMPOSIZIONE**: 66 unità sono
frammenti che il gioco concatena (`Phrase::Get()`, senza separatore) e le frasi nascono solo scegliendo un'opzione per
gruppo: **1104 combinazioni** per lingua, verificate **una per una** da entrambi gli script (il `verify.py` ricostruisce i
gruppi leggendo i blocchi `phrase` del file del gioco). **Quattro frammenti hanno uno spazio in meno dell'inglese**
(43/44/65/66: `begin `/`start ` → «iniziano a»/«prendono a»), perché l'oggetto comincia con uno spazio e l'inglese produce
**due** spazi: la differenza è elencata e asserita. **L'opzione vuota** del quarto gruppo non è inventariata (3 su 4):
lacuna dichiarata. Segmento 86/124 (69,4%), confine riga 306. Numeri di dettaglio in
`staging/editorial/L241_20261020_140015/{review,REPORT,STATO}.md`.

L332 chiuso il 2026-10-20 — **FILE INTERO `data/human/south jobs.txt`** (righe **15-347**, **40 unita'**: 14 `VALUE` + 14
`DESCRIPTION` + 8 `DIALOG` + 4 `CONVERSATION`, **15 contesti**, **720 EN -> 687 IT**, 0,954; **2 tab** (133,135), **2 virgolette**,
**66 segnaposto** in 8 forme; `check.py` 16 controlli, `verify.py` 12, sha `3da37b24c5169ccc`, **FILE 40/40**). I 14 `VALUE` sono
**titoli di lavoro** e sono stati **tradotti** («Consegna a <planet>», «Spedizione a <planet>», «Trasporto passeggeri a <planet>»,
«Pirati che occupano <system>»): il corpus aveva **due politiche** (`Delivery` copiato 14 / tradotto 13; `Shipment` copiato 20 / mai
tradotto) e il file ne adotta **una sola**, con divergenza dichiarata. `Southern Rim` -> «Bordo Meridionale». **Un rosso**: `verify.py`
dichiarava «52 segnaposto» mentre la somma delle forme e' **66** — totale corretto al misurato.

## 4. Prossimo lotto — L333 (**TERMINALE**, `data/persons.txt` 186–2263)

```bash
python staging/editorial/tools/export_section.py "staging/editorial/L333_$(date +%Y%m%d_%H%M%S)" "data/persons.txt" 186 2263
```

| voce | valore |
|---|---|
| File | `data/persons.txt` (49 unità · 752 parole · righe 186–2263) |
| Righe | 186–2263 |
| Copertura | **tutto il file** |
| Unità | **49** |
| Tipi | **27 `TEXT` + 20 `DESCRIPTION` + 2 `VALUE`** |
| Parole | **752** |
| Contesti | **21** — da `Wardragon` a `Modified Hauler VI` |
| Tab / virgolette | **4** / **54** |
| Segnaposto | **0** |
| Confine dopo | **fine file** |

Controlli per tipo; virgolette **per riga**. Contratto verificato: `HANDOFF_L333_20261020.md` (`FAIL: 0 / 21`).

## 5. Ciclo di lavoro (per ogni lotto)

1. **Aprire** il lotto con `export_section.py`; il tool rifiuta di sovrascrivere una directory esistente.
2. **Ricognizione** su `source.json`: kind, contesti, token, tab, virgolette, unità con virgolette dispari,
   e `raw`/`id` delle unità sospette (riferimenti di dato, `label` di salto).
3. **Derivare `check.py`** dal lotto precedente: docstring riscritta, `NT` aggiornato, `TITLES` esteso.
4. **Parti da 30–85 unità**, allineate a fine missione. Dopo ogni parte:
   a. costruzione del file di parte con i tab iniziali derivati dal sorgente (script sotto);
   b. `check.py --range A B` → devono restare verdi tutti i controlli tranne `copertura`;
   c. dopo le parti, `check.py` completo (la deduplica italiana è sul lotto, non sull'intervallo).
5. **Chiusura**: `check.py` completo `FAIL totale: 0` → `verify.py` derivato (indipendente) → `review.md`,
   `REPORT.md`, `STATO.md` CHIUSO → `state.py` OK → `HANDOFF_L<n+1>` + `CHECKPOINT_EDITORIALE.md` + questo
   documento aggiornati **nello stesso momento**.

### Costruzione delle parti (metodo usato in L31, riusabile)

Le traduzioni si scrivono **senza tab iniziali** in un file grezzo (`{"12": "testo"}`, nella scratch); un
costruttore aggiunge `'\t' * (tab iniziali del sorgente)`, verifica il conteggio dei tab per unità, le
virgolette per unità e il rapporto di lunghezza, e scrive `parts/partNN.json`.

```python
import json
LOT = 'staging/editorial/L<NN>_<data>_<ora>'            # percorso del lotto
src = {u['idx']: u for u in json.load(open(LOT + '/source.json', encoding='utf-8'))['units']}
raw = json.load(open('partNN.json', encoding='utf-8'))   # file grezzo, senza tab
out = {}
for k, v in raw.items():
    en = src[int(k)]['english']
    assert '\t' not in v
    it = '\t' * (len(en) - len(en.lstrip('\t'))) + v
    assert it.count('\t') == en.count('\t')
    out[k] = it
json.dump(out, open(LOT + '/parts/partNN.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
```

In L32 ha prodotto 512 tab IT = 512 EN su 805 unità, senza un solo scarto: i tab non sono mai stati
digitati a mano. Restano da **leggere** due esiti del costruttore, perché il conteggio torna anche con la
virgoletta nel punto sbagliato: le **virgolette per unità** e il **rapporto** (banda comoda 0,70–1,75).
Il caso che tradisce ogni ciclo meccanico è l'unità che riceve **due** virgolette in coda, quando il
sorgente lascia aperte due citazioni annidate: lì si riscrive la frase a mano.

---

## 6. Regole non negoziabili

1. **Nessuna scrittura su `state.db`.** Aperto `mode=ro`. Lo staging non è approvazione: le unità restano
   `PENDING`.
2. **Non allentare un controllo per far passare una traduzione.** Si riscrive il testo.
3. **Si riproduce il sorgente, non lo si normalizza**: virgolette aperte (le battute continuano nell'unità
   successiva), tab iniziale, spazi ai bordi, troncamenti (`on anoth.` → `su un altr.`), refusi.
4. **Niente trattino lungo `—` né en-dash `–`**: vietati dal controllo tipografico. Parentesi o virgole.
5. **Niente caratteri non latini**: `°`, `º`, `ª`, emoji, simboli matematici, e nemmeno virgolette curve
   (`‘` `’` `“` `”`) e l'ellissi tipografica `…`. L'apostrofo è quello dritto `'`.
6. **`UI_LABEL` e riferimenti di dato non si traducono mai**: restano identici, elencati uno per uno in `NT`
   (non una regola generale "salta i non traducibili": nasconderebbe le omissioni vere).
7. **Rapporto lunghezze per unità**: il gate è `0,55 < ratio < 1,90` (in `check.py`), la banda comoda
   0,70–1,75. In L32 l'esito è stato 0,72–1,61. Le battute di due parole sforano il minimo
   (`"We do," it says.` → «"Sì, ci importa," dice.»), i titoli corti il massimo (`Combat Drill` →
   «Scontro di prova» = 1,33, non «Esercitazione di combattimento» = 2,50).
   **La soglia non si tocca**: si riscrive la frase.
8. **Numeri misurati, mai dedotti**: ogni cifra nei documenti viene da `state.py`, `check.py`, `verify.py`,
   `translation.json` o `state.db`. Anche il numero di controlli di `verify.py` si conta sull'output
   (`grep -c ' OK'`), non si copia dal lotto precedente.
9. **Nessuna riscrittura totale di un file già chiuso**; nessun refactoring non richiesto.
10. **Se un lotto non si può verificare, si dichiara**: "non verificato: richiede il gioco" è una risposta
    corretta; "funziona" senza exit code no.

---

## 7. Trappole già pagate (non riscoprirle)

1. **Battute aperte dal sorgente**: in `hai missions.txt` la citazione continua nell'unità successiva e in
   L29 il ciclo di bilanciamento ne aveva chiuse 23 per errore. Il conteggio si fa per unità: due errori
   opposti si compensano nel totale e non nel testo.
2. **`log "Categoria" "Nome" "Testo"` perde qualcosa nell'inventario, ma non sempre la stessa cosa.**
   Misurato in L30 (righe 21 e 467): una sola unità, ed era la **categoria** — il testo si perdeva.
   Misurato in L32 (unità 54, 70, 109): una sola unità, ed è il **testo** — categoria e nome si perdono.
   In entrambi i casi la lacuna non è correggibile da un lotto (`tools/l10n.py` e `state.db` sono
   Misurato in L33 (righe 338, 549, 953): come L32, si perde categoria e nome. In tutti i casi la lacuna
   non è correggibile da un lotto (`tools/l10n.py` e `state.db` sono protetti) e va dichiarata
   (decisioni 94, 103 e 106). **Leggi l'`english` di ogni `LOGBOOK`, non solo il `raw`**: in L33 erano 41.
3. **Riferimenti di dato classificati come `MISSION_TEXT`**: in L29 erano `scene`/`thumbnail`. Vanno in
   `NT`, altrimenti rompono il gioco e falliscono il controllo delle parole residue.
4. **`state.py` conta al netto delle `UI_LABEL`**, il lotto esportato no; e **la maggior parte delle 630 label
   è già in staging**, quindi la formula `PENDING − staging − label` le sottrae due volte; in più **52 unità in
   staging sono già `APPROVED`** (L111), che la formula conta come se fossero `PENDING`. Per questo stampa **4128**
   mentre il residuo misurato è **4.797 unità / 101.660 parole** su 116 file (scarto **667**, dovuto alle 630
   label contate anche se già in staging e alle 52 unità `APPROVED` contate come `PENDING`). La
   tabella dell'handoff usa il totale del file, il residuo il netto misurato (decisione 99).
5. **Duplicati italiani**: ammessi solo dentro un gruppo con lo stesso inglese. Attenzione al caso opposto,
   più insidioso: due inglesi quasi identici (`any more` / `anymore`, `help` / `assist`, L32 202/516/540)
   pretendono due italiani diversi, altrimenti il controllo li boccia — e il `--range` non lo vede.
6. **Il `--range` non vede i duplicati fra parti**: dopo ogni parte va lanciato anche il controllo completo.
7. **`CONVERSATION` è un contenitore misto**: può essere il testo visibile del blocco (da tradurre, con
   backtick riprodotto) o una `label` di salto (identica, in `NT`). Si distingue dal `raw`, non dal `kind`
   (decisioni 77 e 100). In L30/L31 il tipo non esisteva, in L32 erano 47 unità (45 + 2 label), in L33 la
   misura dice 0: **rimisura a ogni lotto**, non fidarti del lotto precedente.
8. **Le parentesi quadre `[a, b]` sono struttura, non stile** (L32 112 unità, L33 113): il gioco mostra una sola
   alternativa per volta, quindi ogni alternativa deve reggere la frase da sola e il numero di
   alternative deve restare quello del sorgente. Il `check.py` derivato deve portarsi il controllo
   «gruppi e alternative»: una parentesi chiusa male passa il controllo delle virgolette e fallisce solo
   lì (decisione 102).
9. **Righe delle parti**: si leggono da `source.json`/`state.db`, non si calcolano a mano (tre errori
   consecutivi su questo punto prima che la regola entrasse in skill).
10. **Il tempo di scrittura dei documenti è parte del lavoro**: checkpoint e handoff si aggiornano nel turno
   in cui si chiude il lotto, altrimenti al turno dopo descrivono uno stato che non esiste.
11. **`check_handoff.py` ha un formato a contratto**: copertura `4253/ 4253 unità (100.0%)` con lo spazio
    dopo la barra, `non traducibili): 630` e la riga del residuo **fuori** dal grassetto e in minuscolo, contesti
    fra backtick singoli e **senza** il prefisso `mission:`, `Confine dopo` **con** il prefisso grezzo se il
    confine non è "fine file", residuo `**N unità / M parole** dopo la riga X` con il grassetto chiuso
    subito prima di ` dopo`, e **ogni** `` `L## <16 hex>` `` citato verificato contro `translation.json`.
    Se non combacia, il checker fallisce su un documento corretto.
12. **I token tornano in un lotto di tooltip**: L111–L114 ne avevano **zero**, L115 ne ha **otto** (`<shift>`)
    e L116 **uno**. «Non ci sono token» valeva per quelle quattro finestre, non per il file: la parità si scrive
    come asserzione (`8 = 8`, `1 = 1`), e il testo si costruisce **intorno** al token.
13. **Le citazioni di un pannello di impostazioni sono chiavi, non prosa**: `"Escorts expend ammo"`,
    `"ship cap,"`, `"fancy"`, `"off"` sono identificatori usati dal codice (`Preferences::Has`) e mostrati dal
    menu. Restano in inglese e si verifica l'**identità dei testi citati per unità**, non il loro numero.
    L'unica deroga ammessa è un'etichetta già tradotta da un lotto precedente (`surge` → «picco», L113).
    Attenzione alla **punteggiatura interna**: `"ship cap,"` ha la virgola dentro le virgolette (L116 122–124) e
    spostarla fuori fa fallire il controllo su un lotto corretto.
14. **Un file che si chiude cambia la forma del `verify.py`**: da invariante di **segmento** (con un'unità
    successiva da verificare) a invariante **di file** (tutti i `translation.json` del path coprono tutte le
    unità, `sovrapposti = 0`). Tenere il vecchio invariante rende rosso un lotto corretto; il nuovo va scritto
    quando il lotto è l'ultimo, non prima.
15. **In un file di lavori i `VALUE` sono nomi di missione e restano in inglese**: elenco esplicito nel
    `check.py`, ricalcolo dal `kind` nel `verify.py`. La prima stesura di L117 li aveva tradotti e il controllo
    «i 31 `VALUE` sono identici al sorgente» l'ha bocciata — la correzione è stata togliere i nomi dalla mappa
    delle rese, non allentare il controllo.
16. **Le rese si assegnano per firma dell'inglese, e la firma deve essere unica**: in L117 `insist` combaciava
    sia con `insists that` sia con `insist that`, e il costruttore abortiva con due corrispondenze. Firme più
    lunghe (`insists that` / `insist that`) e un'asserzione `len(hits) == 1` chiudono la classe di errore.
17. **I numeri in prosa non li controlla nessuno**: l'handoff di L118 dichiarava «181 dopo la riga 2955», che è
    il residuo dopo la 1624; il vero è **77** (279 − 98 − 104). Il checker dell'handoff non guarda quella frase,
    l'ha vista il `verify.py` con un'asserzione sul conteggio. Regola: ogni «N dopo la riga X» si **misura** con
    una query, e se compare in tre documenti si corregge in tre.
18. **La coda di un file ha tipi che i segmenti precedenti non avevano**: in `pirate jobs` i primi due lotti non
    avevano nessuna `CONVERSATION`, la coda ne ha **12**. Si ricognisce leggendo il `raw`, e il controllo del
    tipo si scrive sul `Counter` misurato.
19. **Un registro incoerente si corregge nel testo, non nel controllo**: l'unità 41 di L120 era al «lei» mentre
    tutto il lotto usa il «tu»; riscritta prima della verifica, e il `check.py` ora cerca e rifiuta le forme di
    cortesia (`Pensi quello`, `la sua nave`, `la farà`, `Senta, capitano`).
20. **Un contesto può non avere il prefisso `mission:`**: in `campaign events.txt` convivono `mission:…` e
    `event:…`, quindi «tutti i contesti iniziano per `mission:`» è un atteso sbagliato — corretto con una lista
    esplicita, non allentando il controllo.
21. **Una `UI_LABEL` rompe due controlli se non è dichiarata**: «tutte tradotte» e «nessun residuo inglese» sono
    rossi su un lotto corretto. Va esclusa e verificata **identica** in un controllo suo.
22. **Le virgolette possono essere sbilanciate nel sorgente**: le unità 22 e 24 di L121 aprono una battuta e non la
    chiudono (una sola virgoletta). La resa riproduce, e il controllo verifica **quali** unità hanno una virgoletta
    sola — così una «correzione» tipografica futura fa fallire il lotto invece di passare inosservata.
23. **Zero token è un'asserzione**: nella coda di `campaign events` non ci sono token, quindi il controllo va
    scritto `Counter(...) == {}`, non omesso.
24. **I nomi propri inglesi dentro una frase italiana fanno fallire la scansione dei residui**: `The Parting Glass`
    contiene « the ». Si **neutralizzano prima** della scansione (`replace(nome, '@@')`), non si allenta il
    controllo.
25. **In un file di navi un contesto è una nave**: 33 contesti per 54 unità, 18 da una sola. Non ci sono le
    ripetizioni strutturali dei file di lavori, e i `VALUE` sono nomi propri al plurale (`Modified Argosies` in
    L124).
26. **`cargo` è un prestito italiano**: «modulo cargo», «cassa cargo» non sono residui inglesi. La lista dei
    residui va costruita con parole che in italiano non esistono, non con i prestiti entrati nell'uso.
27. **`startswith` su unità con tab fallisce anche quando i tab sono pochi**: basta un'unità su cinque. Ogni
    asserzione di contenuto usa `.strip().startswith(...)`.
28. **Un segmento può non avere ripetizioni**: in L124 29 testi per 29 unità, senza memoria interna. Il gruppo di
    confronto, quando esiste, è quello con il lotto precedente (le due note tecniche di L123).
29. **Un solo `VALUE` va elencato, non escluso**: `VAL == [18]` con il testo atteso, non «tutti i `VALUE` tranne».
30. **La cella `Contesti` toglie solo il prefisso prima del primo `:`**: un contesto `mission:Incipias: Warning of
    the Guardian` va scritto **`Incipias: Warning of the Guardian`**, non `Warning of the Guardian`. Il checker usa
    `split(':', 1)[1]`.
31. **Tre asserzioni vuote in un file di descrizioni** (zero `VALUE`, zero token, zero quadre) sono il controllo
    più facile da saltare, ed è proprio dove un errore passerebbe inosservato.
32. **Due testi di cui uno è prefisso dell'altro** (le due voci di diario di L126, 18 e 22) fanno scattare due
    firme: si risolvono con una mappa **`EXACT`** per testo completo, dichiarata, non allungando la firma.
33. **Un lotto con un solo contesto**: la cella `Contesti` dell'handoff vuole **primo e ultimo** fra backtick, e il
    checker esige almeno quattro backtick. Con un contesto solo si scrive due volte (`da X a X`).
34. **Due registri nello stesso file** (Guardiano arcaico, Quarg cerimoniale) vanno verificati con parole-spia
    proprie: «follia/giacciono/viaggiatore» e «peregrinare/vagabondaggi/autorizzato».
35. **Un controllo di cortesia scritto con `\b(Le|Lei|Suo…)`** boccia «Le tue intenzioni» e «Le stelle»: l'articolo
    `Le` non è il pronome. Si cercano `Lei/lei` e i possessivi maiuscoli **in mezzo alla frase**.
36. **Il `voi` plurale non è cortesia**: gli Incipias sono una folla e li si saluta con «Vi saluto». Vietare `voi`
    sarebbe un controllo sbagliato, non un lotto sbagliato.
37. **Conteggio degli handoff**: le unità dopo la riga 331 sono **43** (161 − 55 − 63). Un «39» scritto a mente è
    l'errore tipico: si sottrae con la misura, non a occhio.
38. **Cella `Tab / virgolette`** nell'handoff: il checker la legge come `n / m` e la confronta con le unità che
    **iniziano** con tab e con il totale delle virgolette; `Tab` da solo fa fallire «tabella completa».
39. **Cella `Confine dopo`**: per l'ultimo segmento di un file si scrive `**fine file**`, e il checker verifica che
    dopo la riga finale **non** ci siano unità.
40. **Un file chiuso si conta dalla somma dei lotti**: 55 + 63 + 43 = 161. Scrivere `sovrapposti = 0` senza contare
    non dimostra niente; il `verify.py` di L128 somma i tre `translation.json` e confronta con il database.
41. **Una ripetizione fra lotti** (la voce di diario di L128 unità 2 = L127 unità 24) si **rilegge** dal
    `translation.json` precedente e si confronta: ricopiarla a memoria è la via più corta per divergere.
42. **`\blei\b` non è cortesia**: «come se non avessero alcun effetto su di lei» parla della **nave**. La cortesia si
    scrive con la maiuscola (`Lei`, `Suo`).
43. **`residuo traducibile` compare due volte nell'handoff** (stato e trappole): vanno aggiornate **entrambe**, o il
    checker boccia la seconda.
44. **I frammenti di frase (`phrase`) hanno lo spazio finale dentro il testo**: `"Knowing that "` finisce con uno
    spazio, `"the"` no. La resa deve conservarli, e il controllo confronta gli spazi **unità per unità** — senza,
    la frase composta perde le parole.
45. **Un frammento è spesso prefisso di un altro** (`to ` dentro `in order to `, `the` dentro `the `): le firme
    testuali sono ambigue, quindi la resa si indicizza **per indice di unità** e la coerenza si verifica a posteriori
    con «stesso inglese ⇒ stessa resa».
46. **Le unità che non sono testo** in un file di frasi: i template `${...}` delle `conversation` e i **nomi di
    frase** citati da `phrase`. Tradurli romperebbe il gioco; vanno elencati e verificati identici.
47. **Due frammenti di sola punteggiatura** (`, ` e `.`) sono identici per necessità: senza dichiararli, il controllo
    «tutte tradotte» boccia un lotto corretto.
48. **Un lotto può non avere `VALUE` né `UI_LABEL`**: la cella si scrive `0 = 0` e la lista si verifica `== []`.
    Ometterla fa sembrare il controllo «tutto verde» quando non ha controllato niente.
49. **Le varianti della stessa scena** (tre ingressi, quattro esiti) condividono lunghi testi: le parti comuni si
    rendono con **costanti** (`TAIL`, `CAUTIOUS`) e restano identiche parola per parola, altrimenti il confronto tra
    varianti diventa impossibile.
50. **Un numero di `residuo traducibile` scritto a memoria è un errore**: `state.py` va interrogato, e il
    `check_handoff.py` lo riverifica — nel passaggio L129→L130 il valore atteso era **4779**, non 4801.
51. **Una costante può oscurare un dizionario**: `ENG = "(Ripara i motori.)"` sopra `ENG = {idx: english}` faceva
    fallire l'asserzione sulle chiavi con 18 «unità» che erano i caratteri della stringa. Si rinomina la costante.
52. **Le virgolette possono essere decine**: 89 in 84 unità (L132), più di una per unità. Si contano **per unità** e
    si riproducono doppie, mai caporali.
53. **Un file chiuso si verifica dalla somma dei lotti**: 89 + 75 + 76 = 240. Se il totale non torna, c'è una riga
    scoperta o un lotto duplicato.
54. **I nomi di luogo restano nomi**: `Hai-home` non diventa «casa degli Hai», e il controllo vieta la forma tradotta
    invece di limitarsi a sperare che nessuno la scriva.
55. **Una resa identica legittima va dichiarata**, non nascosta: `(No.)` → `(No.)` sta in `ID_OK` e ha un controllo
    suo; senza, «tutte tradotte» la boccerebbe.
56. **Le virgolette si distribuiscono**: 43 unità senza, 33 con 2, 5 con 4, 3 con 1. Contare il totale non basta —
    una battuta chiusa per sbaglio e una aperta a metà danno lo stesso totale.
57. **Le misure dei documenti si prendono dal DB prima di scriverle**: in L132 tre valori su quattro erano stimati e
    il `check_handoff.py` ne ha bocciato uno (`4619`, non 4608).
58. **Un'incoerenza del sorgente si riproduce e si verifica due volte**: il diario di L133 dice «cibo», il testo
    «forniture mediche». Allinearli sarebbe un'invenzione; il controllo pretende entrambe le forme.
59. **Quattro virgolette dispari possono avere conteggi diversi** (1, 1, 3, 1): la sequenza va confrontata, non solo
    il numero di unità dispari.
60. **Tre asserzioni vuote insieme** (`VALUE`, `UI_LABEL`, token) sono la forma corretta per un segmento che non ha
    niente da controllare: scriverle è l'unico modo per distinguerlo da un controllo mancato.
61. **Il trattino lungo non passa la tipografia**: in L134 il primo giro usava «—» in unità 6 e il `check.py` lo ha
    bocciato. Si riscrive la frase, non si allarga il controllo.
62. **La cella `Contesti` va nella forma «bare»**: il checker toglie il prefisso prima del **primo** due punti, quindi
    `conversation:deep intro` si scrive `deep intro`, e conviene aggiungere il nome intero fra parentesi.
63. **Un `VALUE` può essere il nome di una modalità di gioco**: in `starts.txt` sono i nomi degli inizi (`Endless Sky`,
    `Deep Desire`), e restano identici come i nomi di missione. Non forzare la tassonomia dei file di missioni.
64. **Un blocco di testo può triplicarsi se il testo nuovo contiene quello vecchio** (`a` -> `a + b`): la guardia
    «salta se `a` non c'è» non scatta, perché `a` resta dentro `b`. I checkpoint si generano con una `marker` sul
    testo nuovo, e si deduplicano per blocco, non per riga.
65. **I numeri in prosa seguono la convenzione italiana** (`480.000`, `0,4%`): un controllo pretende le forme
    italiane e un altro **vieta** le inglesi, perché cambiare separatore è lecito solo dove è lecito.
66. **`distinti` dentro il lotto non significa `nuovi` rispetto ai lotti**: L136 aveva 15 testi distinti e **5 già
    tradotti** in L135. La seconda misura si fa confrontando l'inglese con i `translation.json` precedenti, e la resa
    si **rilegge** invece di ricopiarla.
68. **Due `VALUE` identici sono due inizi, non un doppione**: `Hai Origins` compare alle righe 215 e 227, e la
    verifica è una lista esatta di due coppie, non un `len()`.
69. **La cortesia di un personaggio non è quella della narrazione**: il cassiere dà del lei, il testo dà del tu. Il
    controllo contabile tollera al massimo una forma, e va scritto per **contare**, non per vietare.
70. **Un lotto può contenere due inizi con lo stesso nome**: `Hai Origins` due volte, uno bloccato e uno
    sbloccabile. La lista esatta di coppie non basta: serve un controllo che i due testi di sblocco differiscano.
71. **Quattro battute aperte vanno lasciate aperte**: 26, 36, 37, 38 hanno una sola virgoletta, e il controllo
    verifica che la resa **non finisca** con una virgoletta — cioè che nessuno abbia «riparato» l'autore.
72. **Un nome identico si dichiara, non si esclude**: `"Benga" Atomic Thruster` sta in `ID_OK` con un controllo
    proprio; toglierlo dai controlli lo avrebbe fatto sparire anche dall'inventario delle scelte.
73. **Il tab di un `raw` può non essere nel testo**: per i nomi di equipaggiamento il `english` non ha tab né backtick,
    quindi «0 tab» è la risposta giusta e va asserita.
74. **Un confronto di percorsi con separatori misti non trova niente**: `staging/editorial` costruito con `/` non
    uguaglia `staging\editorial` di `os.path.abspath`; normalizzare con `os.path.abspath` quando si confronta.
75. **Una battuta ripetuta in due rami della stessa missione è un vincolo, non una comodità**: le due scelte e le
    due risposte devono avere **la stessa resa**, o il giocatore legge testi diversi per la stessa scelta.
76. **Un motto ripetuto è una costante sola**: cinque occorrenze in quattro costruzioni, verificate con un `count`
    sull'intero lotto, altrimenti una variante sfugge.
77. **Una sgrammaticatura del sorgente resta**: «Although despite» → «Sebbene, nonostante». Ripulirla è una scelta
    dell'autore, non del traduttore.
78. **Una voce di diario identica a un altro lotto si rilegge; una variante si riscrive**: copiare la variante
    farebbe ripetere una frase, riscrivere l'identica farebbe divergere due voci che devono coincidere.
79. **Una `VALUE` può cadere a metà lotto**: dentro il lotto è l'unità 1, nel file è la riga 139; il controllo si scrive
    sull'indice del lotto e la verifica sul file.
80. **Un «N dopo la riga X» si ottiene per sottrazione** (totale − prima − finestra), non a occhio: in L142 era
    stato scritto 81 invece di **82**, e il `verify.py` l'ha bocciato.
81. **`(No.)` e `(Yes.)` nella stessa scelta**: il primo è identico per necessità (in `ID_OK`), il secondo si traduce
    («(Sì.)») e la ripetizione deve avere la stessa resa. Un controllo unico per entrambe sarebbe sbagliato.
82. **Due missioni corte si possono unire in un lotto**, quando da sole sarebbero due giri di apertura, verifica e
    documenti per poche centinaia di parole: entrambi i contesti devono chiudersi, e il `verify.py` lo verifica due volte.
83. **Un token in una frase si verifica per simbolo e per unità**: due segnaposto in due unità diverse danno un totale
    pari anche se sono stati scambiati di posto.
84. **Un token-suffisso si incolla al nome**: `Hai<hood>` non ha spazio davanti, e la resa italiana nemmeno —
    «Slegato`<hood>`». Un token a inizio frase, invece, regge la maiuscola che segue.
85. **Un segnaposto che contiene una frase si confronta esatto**: `<The engineer>` con `.lower()` diventerebbe
    `<the engineer>` e il controllo passerebbe su un simbolo diverso.
86. **Le virgolette aperte dal sorgente non si chiudono, e il controllo lo pretende**: tre asserzioni — disparità
    riprodotta, **nessuna** virgoletta finale aggiunta, segno finale uguale all'inglese.
87. **Quando un lotto chiude il file la cella `Confine dopo` comincia con «fine file»**: il checker ha un ramo
    terminale apposta, e qualsiasi altra forma fallisce con `nxt is not None`.
88. **Un file può avere un inventario vuoto di testo**: `news.txt` ha **164 unità su 202** che sono il
    delimitatore `` `"` `` e **1.356 righe con una frase quotata assenti dal database**. Prima di aprire un lotto si
    controlla che le unità siano testo, non punteggiatura: altrimenti si «traduce» una virgoletta 164 volte.
89. **Un file con troppe unità residue non è per forza il prossimo**: il numero più alto può essere un artefatto.
90. **La parità dei token si fa in tre modi, non uno**: multiset per simbolo, **ordine per unità**, e un conteggio
    nominato per i simboli corti che si somigliano (`<payment>` 17, `<date>` 4) — 65 e 65 può nascondere uno scambio.
91. **Un `ck(..., True)` non è un controllo**: se non può fallire va rimosso, non lasciato verde.
92. **Il controllo dei residui inglesi esclude i `VALUE`**: sono inglesi per contratto, altrimenti si contraddice.
93. **Due simboli con lo stesso conteggio** (`<planet>` 10 e `<payment>` 10) rendono il multiset cieco: solo
    l'ordine per unità smaschera lo scambio.
94. **Le coppie `VALUE`+`DESCRIPTION` si tengono intere**: un taglio tondo che lascia un `VALUE` orfano alla riga 611
    si evita allungando la finestra di una unità.
95. **«Quasi la stessa frase» non è la stessa frase**: `on <planet>` e `on the <planet>` sono due stringhe, e la resa
    cambia («su» contro «sul»). Il riuso si fa **solo** con la chiave inglese identica, e negarlo è un'asserzione.
96. **In batch conviene tradurre per stringa, non per unità**: 37 unità / 14 testi (L151) si fanno con una mappa
    `(kind, english) -> italiano`, e le copie non possono divergere.
97. **Un lotto troppo grande si taglia al confine che non spezzi una coppia** `VALUE`+`DESCRIPTION`, e il contratto si
    aggiorna **prima** di dichiarare chiuso il file.
98. **Una finestra che finisce su un numero tondo può tagliare un contesto a metà**: le righe 172–194 contengono solo
    lo `start` (3 unità), il `conversation:syndicate intro` inizia alla 195. Il taglio si prende alla fine del
    contesto (214), non al primo numero plausibile.

---

44. **Il blocco «prossimo lotto» non ha lo stesso numero di sezione nei due documenti**: `## 4.` in
   `CHECKPOINT_SESSIONE` (dove segue «Lotti chiusi e ultimi numeri») e `## 5.` in `CHECKPOINT_AGENTE_SESSIONE`
   (dove segue «Ultimi lotti chiusi»). Copiare lo stesso testo in entrambi crea **due sezioni `## 5.`** in
   `CHECKPOINT_SESSIONE`: e' successo due volte (L161 e L163) e il difetto si vede solo leggendo i heading.
   Prima di salvare: `grep -n "^## " CHECKPOINT_SESSIONE_20261018.md`.
   **Variante**: quando il lotto chiude un file il testo del heading cambia («Ultimo lotto — L166» invece di
   «Prossimo lotto — L16x»), e uno `span('## 4. Ultimi lotti chiusi', '## 5. Prossimo lotto', ...)` non trova piu' il
   secondo marcatore. Si usino i marcatori di **sezione** (`## 4.` / `## 5.` / `## 6.`), non il testo del titolo.


45. **La tabella «prossimo lotto» deve contenere la cella `File`.** Senza quella cella `check_handoff.py` ricade su
   `human missions.txt` e verifica **un altro file**: il sintomo e' un FAIL su `contesti` e `confine dopo` con
   contesti che non esistono nel lotto (successo con L173: `mission:Hallucination`, riga 1415, 5 FAIL su tre
   documenti). La cella `Contesti` va inoltre nella forma `**N** — da `mission:X` a `mission:Y``: la forma
   abbreviata `[0..2]` non viene letta. Verifica: `python staging/editorial/tools/check_handoff.py <documento>`.
   La cella `Contesti` va scritta **senza** il prefisso del contesto (`Koryfi`, non `ship:Koryfi`): il checker
   toglie il prefisso dal lato database e **non** dal documento, quindi la forma con prefisso fallisce pur
   essendo identica a occhio (visto in L174).

46. **`write_file` può rispondere «ok» senza creare il file.** Successo due volte di fila con i `verify.py` di L176
   e L177: lo strumento dichiarava la scrittura, `python` rispondeva `No such file or directory`. Regola: dopo aver
   scritto uno script, **verificare con `ls -la`** prima di eseguirlo; se manca, scrivere nello scratch e `cp` nella
   cartella del lotto. Costo evitato: un `verify_exit=2` interpretato come fallimento del gioco.

## 8. Glossario operativo

**Convenzioni generali** (da `CHECKPOINT_EDITORIALE.md` §6): registro "tu" al giocatore, "voi" ai collettivi;
maiuscola solo alla prima parola nelle etichette; numeri con il punto delle migliaia; niente inglese nel
testo salvo i termini marcati invariati.

**Invariati per scelta**: nomi di pianeti, sistemi, fazioni, specie, regioni, aziende (`Hai`, `Avgi`, `Pug`,
`Remnant`, `Heliarch`, `Arach`, `Saryd`, `Kimek`, `Lunarium Redoubt`, `Quarg`, `Hai-home`, `Allhome`,
`Darkrest`, `Prime`, `Stonebreak`…) e i modelli di nave (`Star Queen`, `Bulk Freighter`, `Heavy Shuttle`,
`Bastion`, `Argosy`, `Clipper`, `Thistle`, `Spire`, `Spindle`, `Finishers`, `Punishers`, `Aphid`,
`Star Barge`, `Shield Beetle`, `Geocoris`, `Leviathan`, `Solifuge`, `Starling`, `Gull`, `Keloid`).

**Eccezioni deliberate**: `Earth` → Terra, `Mars` → Marte, `Syndicate` → Sindacato, `Coalition` → Coalizione,
`Paradise World` → Mondo Paradisiaco, `hyperdrive` → iperpropulsore, `house X` → Casa/Casata X,
`Predecessors` → Predecessori, `jump drive` → motore di salto.

**Lessico dei lotti recenti** — L32 (Wanderers): `the Eye` → **l'Occhio**; `the Molt` → **la Muta**;
`Keepers` → **Custodi**; `unfettered humans` (gli Alphas, detti così dai Pug) → **umani senza freni**,
distinto da «Slegati». L31 (Heliarchs): `console`/`consuls` → **console**/**consoli**;
`Arbiter` → **arbitro**; `Magister` → **magistra**; `circlet` → **cerchietto**; `Drill` nei titoli →
**prova**. L30 (Coalizione / Lunarium): `the Redoubt` → **il Redoubt**; `Heliarchy` → **Eliarchia**.
L29 (Hai): `Unfettered Hai` → **Hai Slegati**; `keystone` → **pietra chiave**; `drone carrier` →
**porta-droni**. L27/L28 (Ka'het, Remnant): `airlock` → **camera di equilibrio**, `Ember Waste` →
**Distesa di Braci**.

**Voce dei Wanderers (L32–L33, chiusa con L33)**: nessun ordine marcato. Frase piana e cortesia formale; i Pug
parlano di sé in terza persona; il dispositivo di traduzione dei Pug parla **senza punteggiatura** per
scelta. **Non** trasportare qui la voce della Coalizione (Kimek/Saryd/Arach), che è un'altra cosa.

---

## 9. Mappa dei documenti (cosa è autorevole)

| documento | ruolo | stato |
|---|---|---|
| `RIPRESA_L154_20261019.md` | **ripresa a freddo** in un solo file: regole, stato, contratto L154, batteria | attivo, verificato dal checker |
| `CHECKPOINT_AGENTE_SESSIONE_20261018.md` | ripresa precedente, numeri a L153 | sostituito dalla RIPRESA |
| `CHECKPOINT_SESSIONE_20261018.md` (questo) | storia dei lotti, metodo, trappole, glossario | attivo |
| `CHECKPOINT_EDITORIALE.md` | fonte di verità del progetto (totali, decisioni 1–150) | aggiornato a L143 chiuso |
| `HANDOFF_L154_20261019.md` | contratto formale del prossimo lotto, verificato da checker | attivo |
| `HANDOFF_L150_20261019.md` | contratto del lotto chiuso | **OBSOLETO** |
| `HANDOFF_L151`…`L153` | **non emessi**: batch, contratto = piano del batch | — |
| `HANDOFF_L98…L149_*.md` | storico | consultazione |
| `staging/editorial/L15{0,1,2,3}_*/{STATO,REPORT,review}.md` | chiusura dei quattro lotti del batch | CHIUSI |
| `SESSION_CHECKPOINT.md` | fermo al 17 ottobre (L19) | **obsoleto**, non usare |

---

## 10. Comandi di verifica (nell'ordine, prima di lavorare)

```bash
cd ~/PROGETTI/G-DEV/GAME-SOURCE-LAB/endless-sky-l10n

python staging/editorial/tools/state.py                                    # exit 0, ESITO: OK
python staging/editorial/tools/check_handoff.py HANDOFF_L333_20261020.md    # exit 0, FAIL: 0/21
python staging/editorial/L205_20261019_211129/check.py                      # FAIL totale: 0 (23 controlli)
python staging/editorial/L205_20261019_211129/verify.py                     # exit 0, 16 controlli (FILE CHIUSO)
python staging/editorial/L332_20261021_120811/check.py                      # FAIL totale: 0 (16 controlli)
python staging/editorial/L332_20261021_120811/verify.py                     # exit 0, 12 controlli (FILE 40/40)
```

Tutti e quattro sono verdi al momento in cui questo documento è stato scritto (misurato, non stimato).
Il batch L154–L160 è chiuso e **L161–L162** lo seguono: quarantadue lotti, **627 unità**, tutti con `FAIL totale: 0` e
`verify.py` exit 0; due file sono a **197/197** (`coalition jobs.txt`) e **90/90** (`weapons.txt`), e `avgi outfits.txt`
sono **chiusi**: `avgi outfits.txt` 63/63, `paradise world jobs.txt` **131/131**, `avgi ships.txt` **102/102** e
`human outfits.txt` **63/63** e `gegno outfits.txt` **60/60** (6 lotti, L185–L190). Il
L203–L216 sono **chiusi** — quattordici lotti su tre file: `hai outfits.txt` (508–600, 603–788, 805–984), `coalition
news.txt` (28–94 … 401–496) e `deep jobs.txt` (16–322, 333–453, 457–682, 684–864, 866–929).
**Due file chiusi**: `hai outfits.txt` 65/65 (L205) e **`coalition news.txt` 112/112 (L211)**. `deep jobs.txt` è a
**157/187 + 1 `UI_LABEL` (84,0%)**: **L217 lo chiude**.
**Le lezioni di questi quattordici lotti**:
1. **Le asserzioni cadono sempre per colpa dell'asserzione, non del testo** — 16 su 16. L'ultima: avevo imposto al
   `LOGBOOK` la terza persona, ma il sorgente dice *from you*.
2. **Le strutture non si normalizzano**: citazioni spezzate o su più paragrafi, frammenti `phrase:`, tab separatori,
   `UI_LABEL` che spezza la sequenza delle finestre.
3. **I legami fra unità si traducono come sistemi**: la battuta di L215 vive solo se la stessa espressione compare nei
   tre punti collegati.
4. **I segnaposto hanno grammatica**: `<last>` (cognome, senza articolo) e `<passengers>` (numero, con articolo) non si
   trattano allo stesso modo.
Il contratto attivo è **L217**, **terminale**: righe 935–1234, **29 unità**, 375 parole, 12 contesti, **12 `VALUE` + 12
`DESCRIPTION` + 5 `DIALOG`**, **56 segnaposto su 9 simboli**. Le **3.661** unità residue stanno su 105 file.
**File completi: 65 su 167.**

---

## 11. Vincoli di mandato e stile di lavoro del committente

- Si procede **in batch**: una volta aperto un lotto si va fino alla sua chiusura, senza fermarsi a ogni
  parte a chiedere conferma.
- Il deliverable è **un artefatto verificato**, non un piano. Ogni risposta deve contenere lavoro chiuso e
  numeri misurati.
- Distinzione netta tra **misurato**, **dedotto** e **non verificato**; nessun risultato inventato.
- Diff minimi, correzioni puntuali, checkpoint di ripresa tra sessioni.
- Se un comando fallisce o un controllo è rosso, si dichiara e si corregge il **testo**, non la soglia.
- Non si installa nulla, non si cambia modello, non si toccano file di altri profili Hermes.

---

## 12. Stato delle cose non fatte (dichiarato)

- **Nessun rendering nel gioco**: le 27.802 unità di staging non sono mai state caricate da Endless Sky.
  Non è verificato che le righe lunghe stiano nelle schermate di dialogo né che le parentesi quadre
  vengano risolte a schermo.
- **Nessuna approvazione**: `APPROVED 364` è fermo al 2026-10-17, tutto il resto è `PENDING`.
- **Due voci di diario di L30 restano in inglese** (righe 21 e 467: `log "Factions" "Lunarium Redoubt"
  "…"`): fuori dall'inventario, lacuna documentata in `staging/editorial/L30_20261018_105244/review.md` §7.
  Non riparata: richiede `tools/l10n.py` e `state.db`, che sono protetti.
- **Glossario non riconciliato** fra file: i termini dei lotti recenti valgono per i file affrontati, non
  sono stati confrontati con i file ancora da tradurre.
- **Tre voci di diario di L33 restano in inglese nella categoria e nel nome** (righe 338, 549, 953):
  documentata in `staging/editorial/L33_20261018_114017/review.md` §7, non riparata.
- **Cinque schede biografiche di L34 restano in inglese nella categoria e nel nome** (righe 1622, 1623,
  2308, 2310, 2311): documentata in `staging/editorial/L34_20261018_115356/review.md` §7, non riparata.
- **La categoria di diario `People` di L35 resta in inglese** (unità 547): documentata in
  `staging/editorial/L35_20261018_120433/review.md` §7, messa in `NT`, non tradotta.
- **L36–L41 non hanno lacune `log`**: 23, 27, 41, 1, 7 e 0 righe. L41 è l'unico lotto della serie senza
  righe `log` (0 `LOGBOOK`): misura, non assenza di controllo.
- **Una lacuna `log` in L42** (riga 388, `log "People" "Gavriil" …`): categoria e nome restano in inglese,
  il testo del diario è tradotto; documentata in `staging/editorial/L42_20261018_155050/review.md` §7.
- **`remnant 2 side missions.txt` intatto**: 0 unità tradotte, 299 da fare.
