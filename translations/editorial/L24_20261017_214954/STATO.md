# L24 — stato di avanzamento (CHIUSO il 2026-10-17)

`data/remnant/remnant 1 introduction.txt`, righe 23–3923, **1.250 unità**, 41.087 parole, 68 contesti.
File **intero** (deviazione +2,7% sul target di 40.000 parole, dichiarata in `REPORT.md` alla chiusura).

## Fatto

| parte | unità | righe | esito |
|---|---|---|---|
| part01 | 1–90 | 23–294 | `check.py --range 1 90` verde |
| part02 | 91–180 | 295–629 | `check.py --range 91 180` verde |
| part03 | 181–270 | 631–898 | `check.py --range 181 270` verde |
| part04 | 271–360 | 899–1183 | `check.py --range 271 360` verde |
| part05 | 361–450 | 1185–1440 | `check.py --range 361 450` verde |
| part06 | 451–540 | 1458–1700 | `check.py --range 451 540` verde |
| part07 | 541–630 | 1703–2109 | `check.py --range 541 630` verde |
| part08 | 631–720 | 2114–2452 | `check.py --range 631 720` verde |
| part09 | 721–810 | 2453–2729 | `check.py --range 721 810` verde |
| part10 | 811–900 | 2730–3007 | `check.py --range 811 900` verde |
| part11 | 901–990 | 3019–3355 | `check.py --range 901 990` verde |
| part12 | 991–1080 | 3357–3566 | `check.py --range 991 1080` verde |
| part13 | 1081–1170 | 3567–3773 | `check.py --range 1081 1170` verde |
| part14 | 1171–1250 | 3775–3923 | `check.py --range 1171 1250` verde · **lotto completo** |

**1.250 / 1.250 unità · 41.087 EN → 38.140 IT (100%)**

```bash
python staging/editorial/L24_20261017_214954/check.py   # atteso: i 2 FAIL di copertura (1170/1250)
```

Misure dell'esecuzione completa su unità 1–1170 (lette, non dedotte): tab **867/867**, virgolette
**1955/1955**, token **238/238**, rapporto 0,57–1,82, nessuna parola inglese residua, nessun duplicato
italiano non giustificato dal sorgente.

## Ripresa

**Unità 1171**, riga **3775**, contesto `mission:Remnant: Expanded Horizons Storms 1` (le tempeste
della Distesa). Ultima unità del file: **1250**, riga **3923**.

Resta **1 parte**: **80 unità**, righe **3775–3923**, **2.750 parole**.

```bash
python "C:/Users/Dave/AppData/Local/hermes/profiles/game/cache/scratch/dump_section.py" \
  staging/editorial/L24_20261017_214954 1171 1250
python staging/editorial/L24_20261017_214954/check.py --range 1171 1250
```

## Ricognizione del file (fatta prima di tradurre)

| tipo | unità | trattamento |
|---|---:|---|
| `MISSION_TEXT` | 1.008 | tradotte |
| `VALUE` | 52 | nomi di missione (`name "…"`) — tradotti |
| `DESCRIPTION` | 52 | istruzioni con `<destination>`, `<waypoints>`, `<payment>` — tradotte |
| `CONVERSATION` | 44 | **nessuna** `label` dentro: verificato sul `raw`, 0 occorrenze |
| `UI_LABEL` | 43 | tutte righe `label "…"` con un `goto`: **restano identiche** (`NT`) |
| `DIALOG` | 28 | avvisi di sistema — tradotti |
| `LOGBOOK` | 22 | diario del giocatore — tradotto in prima persona |
| `TEXT` | 1 | unità 786: prosa vera (promemoria), si traduce |

`NT` = le 43 `UI_LABEL` elencate in `check.py`. `TOKEN_EXC` vuoto: nel sorgente non ci sono
pronomi-token (`<they>`, `<their>`…).

## Regole specifiche di questo file

1. **Virgolette esterne: sì** nel campo `english` (come `human missions.txt` e `deep missions.txt`);
   le interne si scrivono `\"`.
2. **`TAB`**: molte unità iniziano con `\t`, una (`1105`-style) può averne più d'uno — qui nessuna.
   Il conteggio va confrontato con il sorgente, non dedotto.
3. **Citazioni dal conteggio dispari già incontrate**: `23`, `68`, `72`, `74`, `78`, `79`, `120`.
   Si riproducono con lo **stesso numero** di `"`; il numero atteso è `english.count('"')`.
4. **Niente trattini lunghi** né apostrofi curvi (controllo tipografico).
5. **Duplicati**: 78 gruppi / 195 unità nel sorgente. Italiano identico ammesso solo dove l'inglese è
   identico; 20/47 hanno inglese **diverso** (l'uno ha in più la frase sul pasto abbondante) e
   l'italiano deve differire.
6. **Rapporto lunghezza** 0,55–1,90: le risposte cortissime vanno rese un filo più esplicite
   («You're welcome.» → «Non c'è di che.», non «Prego.»).

## Decisioni terminologiche di questo lotto

| inglese | italiano | nota |
|---|---|---|
| `Remnant` (popolo) | Remnant, «i Remnant» | invariato, con articolo italiano |
| `Ember Waste` | Distesa di Braci | decisione di progetto |
| `Key Stone` | Pietra Chiave | già in uso in L13 (`Pietre Chiave`) |
| `Quantum Key Stone` | Pietra Chiave Quantistica | |
| `Keystones` (VALUE 151) | Pietre-Chiave | variante per non collidere con `Key Stones` |
| `Alphas` / `Alpha Wars` | gli Alpha / le guerre contro gli Alpha | L3d usava «Alphas», L23 «Guerre Alfa»: qui «Alpha» invariato al singolare/plurale |
| `Prefect Chilia` | il Prefetto Chilia | carica tradotta, nome invariato |
| `Republic` | Repubblica | |
| `Korath`, `Hai`, `Palavret` | invariati | specie e classi di nave |
| `void sprites` | spettri del vuoto | creature, minuscolo |
| `Archon` / `Drak` | Archon / Drak | invariati: entità aliene |
| `Puffin` | Puffin | nome di nave, invariato |
| `Exodus` | Esodo | «al tempo dell'Esodo» |
| `IFF` | IFF | acronimo lasciato, con la spiegazione nel testo |
| `license` (dei Remnant) | licenza | carta d'identità, non «patente» |
| `prefect` | prefetto | carica di governo dei Remnant |
| `hard-shell / skin shields` | scudi a guscio duro / scudi a pelle | |
| `outfitter` | fornitore di equipaggiamento |
| `Rim` | Rim | invariato (regione), come in `TITLES` |
| `ramscoop` | ramscoop | nome dell'apparecchiatura, invariato |
| `supercapacitor` | supercondensatore | |
| `Deep Security` | Sicurezza del Deep | |
| `Ibis` | Ibis | nome di nave, invariato |
| `Heavy Laser` | Cannone Laser Pesante | |
| `Plasma Cannon` | Cannone al Plasma | |
| `Catalytic Ramscoop` | Ramscoop Catalitico | |
| `electron beam` | raggio elettronico | |
| `D94-YV Shield Generator` | Generatore di Scudi D94-YV | |
| `S-970 Regenerator` | Rigeneratore S-970 | |
| `Thrasher Cannon/Turret` | Cannone/Torretta Thrasher | invariato |
| `Starling`, `Albatross` | invariati | nomi di nave Remnant |
| `Plume` | Plume | nome proprio, come Taely/Chilia/Torza |
| `wagon`, `camel` | carro, cammello | dettaglio voluto: i Remnant usano trazione animale |
| `Archon` | Archon | invariato |
| `Slylandro`, `Nasqueron`, `Aventine`, `Viminal`, `Caelian` | invariati | pianeti, come da `TITLES` |
| `Albatross`, `Pelican` | invariati | navi di classe capitale |
| `data pad`, `data card`, `credstick` | data pad, scheda dati, credstick | |
| `outfitter` (verbo `salvage ... in the outfitter`) | fornitore di equipaggiamento | |
| `Heat Shunt` | Derivatore Termico | |
| `Systems Core` | Nucleo di Sistema | |
| `Quarg` | Quarg | invariato |
| `Wayfarer`, `Tarazed` | invariati | pianeta/sistema, da `TITLES` |
| `Dawn` | Dawn | nome proprio (ricercatrice) |
| `IFF`, `Quantum Entangled Communicator` | IFF, Comunicatore a Entanglement Quantistico | |
| `Penguin` | Penguin | nome di nave, invariato come `Puffin` |
| `'Shadow Hope'` | 'Speranza d'Ombra' | nome proprio dato da Taely, traducibile |
| `jump drive` / `hyperdrive` | motore di salto / iperguida | |
| `slime` | melma | |
| `Void Rifle` | Fucile del Vuoto | |
| `Aeolus` | Aeolus | nome proprio (fornitore/logistica) |
| `ancestral space` | spazio ancestrale | minuscolo se aggettivo, maiuscolo se «Spazio Ancestrale» come nome |
| `outfits in the current` | equipaggiamenti in corrente | metafora spiegata nel testo (unità 926) |
| `Gull` | Gull | nome di nave, invariato |
| `Hai` | Hai | invariato (specie e spazio) |
| `quantum keystone` | pietra chiave quantistica | coerente con `Key Stone → Pietra Chiave` |
| `Winds of Light` | Winds of Light | nome della nave di Aeolus, invariato |
| `symbiont` | simbionte | i Remnant ospitano organismi viventi |
| `Sagittarius A*` | Sagittarius A* | invariato |
| `3F6290`, `24D2` | invariati | cifre presenti nel sorgente, riprodotte alla lettera |
| `Seeker` | Cercatrice / Cercatore | titolo informale di rispetto per gli esploratori |
| `Research Laboratory` | Laboratorio di Ricerca | |
| `Aescolanus` | Aescolanus | invariato |
| `datapad` | datapad | grafia del sorgente (unità 1168), distinta da `data pad` | |
| `entangled particle pair` | coppia di particelle intrecciate | |
| `sign language` | lingua dei segni | il Remnant canta invece di parlare: «intona», «trilla» |

## Limite noto del sorgente (non correggibile da qui)

`<compared>` (unità **373**) non è una parola: è una **sostituzione definita nei dati del gioco**
(`remnant 1 introduction.txt` riga 966: `"<compared>" "Compared"` oppure `"The complex looks pristine
by <region> standards, but when compared"`). Il testo sostituito è **inglese** e vive nel file del
gioco, che questo workflow non può modificare: l'italiano tiene il segnaposto all'inizio della frase
(`<compared>: rispetto all'architettura…`) e la resa resta imperfetta nella seconda variante.
Da segnalare in `review.md` alla chiusura, non da «aggiustare» traducendo il token.

## Chiusura (esito misurato)

- `check.py` completo: **`FAIL totale: 0`** · copertura 1250/1250 · tab **931/931** · virgolette
  **2111/2111** · token **255/255** · backtick 0/0 · rapporto 0,57–1,86.
- `verify.py` indipendente: **24 controlli, exit 0**.
- `translation.json` sha256[:16] **92e4737d1b55d9dc**.
- `review.md` e `REPORT.md` scritti; `STATE` del database invariato (`APPROVED 364 · PENDING 32560`).
- Non verificato: rendering nel gioco, approvazione nel DB, revisione umana terza.
