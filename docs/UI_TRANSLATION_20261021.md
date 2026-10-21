# Traduzione UI di Endless Sky + correzione del rendering degli accenti

**Data:** 2026-10-21 · **Build:** `endless-sky-it-v2` (aggiornata) · **Sorgente:** `b4aa3bac3`, repo intatto
**`state.db` non scritto** · nessuna unità approvata · nessuna traduzione sovrascritta

---

## 1. Il difetto degli accenti: causa misurata, non ipotesi

`può` appariva come `pu `. La causa **non** è nella traduzione né nell'atlante: erano **due** difetti
indipendenti, entrambi nel percorso di rendering.

### Difetto A — l'eseguibile non aveva il patch UTF-8

`endless-sky-it/src/source/text/Font.h` (la copia che era stata compilata) conteneva:

```cpp
static const int GLYPHS = 98;
static int Glyph(char c, bool isAfterSpace) noexcept;   // un byte, non un codepoint
```

Con questa mappatura ogni carattere accentato (UTF-8, 2 byte) produce **due** celle: `ò` = `C3 B2` →
`Glyph(0xC3)` e `Glyph(0xB2)` → entrambe `min(95, byte-32)` = cella **95**, che nell'atlante da 98 celle
è il carattere 127 (DEL) → **spazio vuoto**. Da qui `pu` seguito da due celle bianche: esattamente il
sintomo riportato.

### Difetto B — il numero di celle è hardcoded nello **shader**

`shaders/font.vert`:

```glsl
texCoord = vec2((float(glyph) + corner.x) / 98.f, corner.y);
```

Con un atlante esteso a 224 celle, la coordinata UV resta divisa per 98 → ogni glifo campiona la cella
sbagliata. **Questo era il pezzo mancante**: `patches/0001-font-utf8.patch` copriva `Font.h`/`Font.cpp`
ma non lo shader, ed è il motivo per cui il patch non era mai stato portato in una build funzionante.

### Correzione minima applicata (3 pezzi, nessuno tocca le traduzioni)

| # | file | modifica |
|---|---|---|
| 1 | `src/source/text/Font.h` · `Font.cpp` | `GLYPHS 98 → 224`, `Glyph(char32_t)`, decodifica UTF-8 in `DrawAliased`/`WidthRawString` (patch già esistente, mai compilata) |
| 2 | `src/shaders/font.vert` | `98.f` → `224.f` (una riga: è un **dato**, si corregge senza ricompilare) |
| 3 | `src/images/font/ubuntu14r.png` · `ubuntu18r.png` | atlanti estesi: 2744×32 → **6272×32**, 3528×36 → **8064×36**, cella invariata (28 / 36 px) |
| 4 | `Font::Glyph()` | i caratteri di controllo tornano a renderizzare nulla (come nella build a 98 celle) invece di un `?` visibile |

### Verifica (non dichiarata: misurata)

| prova | esito |
|---|---|
| cella 210 dell'atlante = `ò` | decodificata dal PNG: **`o` con tratto d'accento sopra** (127 px di inchiostro), `è` alla cella 200 idem |
| geometria | 6272/224 = 28 px = cella dell'atlante originale (2744/98 = 28) |
| schermata reale del menu | testo **leggibile** e in italiano: “Preferenze…”, “Esci”, “Nuovo pilota”, “Nessun pilota caricato”, “tempo di gioco:” (prima: glifi casuali) |
| falsificabilità | con lo shader a `/98` e l'atlante a 224 celle la schermata era **illeggibile**: il controllo può fallire |

**Nota onesta:** la prima compilazione con il solo patch A produceva testo illeggibile. È stato il
controllo visivo a rivelare il difetto B, non un ragionamento a priori.

## 2. Cosa era già tradotto nei dati (non rifatto)

Le etichette dell'interfaccia che vivono in `data/_ui/*.txt` erano **già in italiano** prima di questa fase
(trascritte nei lotti L327–L329 e L398): 1 087 unità su 5 file, 0 residue tranne 12 token tecnici
(`_Audio`, `_+`, `_−`, `A`). In questa fase su quei file: **0 modifiche**. Non le ho riscritte.

## 3. Testo UI nel codice C++ — tradotto ora

| passo | numero |
|---|---:|
| letterali stringa nel C++ (esclusi i test) | 9 626 |
| candidati “testo di visualizzazione” | 514 (+102 etichette brevi recuperate) |
| stringhe distinte dopo deduplica | 485 |
| diagnostica di parser/validazione (esclusa: non è UI di gioco) | 52 |
| **testo rivolto al giocatore** | **433** |
| nomi di azione in `keys.txt` (**esclusi**: sono le chiavi dei comandi) | 34 |
| perimetro traducibile | **399** |
| **tradotte e applicate** | **393** (491 occorrenze, **68 file**) |
| lasciate identiche per scelta | 6 (`Drone`, `Endless Sky`, `Endless Sky ver.`, `New Boston`, `Sprite \"`, `Windows NT`) |

Esempi: “Crew Salaries” → *Stipendi dell'equipaggio* · “You could not pay all your crew salaries.” →
*Non hai potuto pagare tutti gli stipendi dell'equipaggio.* · “Borrow how many credits?” → *Quanti crediti
vuoi prendere in prestito?* · “Can be jettisoned while installed.” → *Può essere espulso mentre è
installato.* · “You have been killed. Your ship is lost.” → *Sei stato ucciso. La tua nave è perduta.*

**Territorio escluso per non rompere il gioco** (verificato su file reali, non per prudenza generica):

| classe | unità | prova |
|---|---:|---|
| nomi di azione dei comandi | 34 | compaiono verbatim in `userdata/keys.txt` (bind dei tasti): tradurli azzererebbe i comandi salvati |
| chiavi di preferenza | 113 | compaiono in `userdata/preferences.txt`; il codice le usa anche come etichetta (`AUTO_AIM_SETTING = "Automatic aiming"`): serve separare chiave e testo, è un refactor, non una traduzione |
| chiavi di mappa/`Preferences::`/`Get`/`Set` | 146 + 404 + 89 | uso come identificatore nel codice |
| identificatori, nomi di oggetto, chiavi di dato | ~8 400 | non sono testo |
| nessuno dei 393 tradotti compare in 362 KB di salvataggi reali | 0 | controllo sui file `.sav` del profilo |

## 4. Unit`a rimaste in inglese (contabilizzate, non ignorate)

| insieme | stato | nota |
|---|---|---|
| etichette in `data/_ui/*.txt` | **tradotte** | 1 087 unità |
| testo C++ per il giocatore | **393/399 tradotte** | 6 lasciate per scelta; 34+113 non traducibili senza rompere bind/preferenze |
| `credits.txt` (radice del repo, mostrato nel menu principale) | **non tradotto — lacuna nuova** | **550 righe**; l'estrattore percorre solo `data/`, quindi il file non ha unità |
| news e hail (6 file) | **non tradotto — lacuna già nota** | 2 065 righe / 29 128 parole, vedi `review/PROPOSTA_ESTRATTORE.md` |
| messaggi di diagnostica del parser | non tradotti per scelta | compaiono solo con dati errati |

`credits.txt` è la prima cosa che il giocatore legge nel menu: è il candidato naturale per il prossimo lotto,
con lo stesso criterio delle news (unità nuove solo dopo l'autorizzazione a toccare l'estrattore, per non
inventare identificativi).

## 5. File modificati

| percorso | contenuto |
|---|---|
| `endless-sky-it-v2/src/source/**/*.cpp` · `*.h` | 68 file, 491 occorrenze sostituite (backup in `review/backups/*_cpp`) |
| `endless-sky-it-v2/src/source/text/Font.h` · `Font.cpp` | patch UTF-8 + gestione caratteri di controllo |
| `endless-sky-it-v2/src/shaders/font.vert` | `/ 98.f` → `/ 224.f` |
| `endless-sky-it-v2/src/images/font/*.png` | atlanti estesi (224 celle) |
| `endless-sky-it-v2/build/Endless Sky.exe` | ricompilato da `b4aa3bac3` con MinGW 16.1 (`exit 0`) |
| `endless-sky-l10n/review/**` | strumenti, elenchi, log, questo documento |
| **non toccati** | `../endless-sky` (0 righe di diff), `state.db` (sha e mtime invariati), `endless-sky-it` (build del 20 ottobre), file protetti 7/7 |

## 6. Controlli eseguiti (tutti con exit code)

| controllo | esito |
|---|---|
| compilazione MinGW (`cmake --build`) | **exit 0** (3 build: font, +UI, +fix controllo) |
| `--parse-assets` sui dati tradotti | **exit 0** · *Analisi completata con no error(s).* |
| coerenza dati ↔ lotti (`apply_translations.py --dry-run`) | **exit 0** · 0 errori |
| verifica indipendente (`verify_integration.py --dest`) | **exit 0** · FAIL 0 |
| gate per lotto (403 lotti) | 395 verdi · 6 per difetto del controllo · 1 saltato (archivio) |
| avvio reale + cattura schermo | processo attivo, finestra creata; lettura indipendente dell'immagine: pulsanti **Preferenze… / Esci / Gestisci piloti… / Nuovo pilota**, pannello **pilota: Nessun pilota caricato · nave · pianeta · sistema · crediti · data · tempo di gioco**, testo nitido, **nessun `?` residuo** nei crediti |
| integrità file protetti | 7/7 |

## 7. Problemi reali trovati (e cosa dicono del metodo)

1. **Shader con 98 hardcoded** (§1): invisibile a ogni controllo statico, visibile solo guardando lo schermo.
2. **`Glyph` che rendeva visibili i caratteri di controllo**: il mio patch mappava `\r` su `?`, quindi le
   righe di `credits.txt` (CRLF) mostravano un `?` in coda. Corretto: controllo → nessun glifo.
3. **`credits.txt` fuori dall'estrazione** (§4): nuova lacuna, stessa famiglia di quella delle news.
4. **`cp` dell'eseguibile fallito** (`Device or resource busy`) in una delle build in background: Windows
   blocca il file se il gioco è in esecuzione. Rimediato uccidendo il processo e ricopiando; la procedura
   ora include il `taskkill` prima del `cp` e il confronto degli `sha256`. Le tre build riportano comunque
   `exit=0`: il difetto era nella *copia*, non nella compilazione.
5. **Nessuna stringa tradotta è una chiave**: verificato su `preferences.txt`, `keys.txt`, salvataggi e
   contesti `Preferences::/Get/Set/map<>` prima di scrivere una sola riga. Le 34 azioni e le 113 preferenze
   sono state **escluse**, non tradotte “a sentimento”.

## 8. Come aggiornare la build (riproducibile)

```bash
cd ~/PROGETTI/G-DEV/GAME-SOURCE-LAB/endless-sky-l10n
python review/apply_cpp_ui.py                 # 393 stringhe nei sorgenti della copia
cd ../endless-sky-it-v2
export PATH="/c/msys64/mingw64/bin:$PATH"; export PKG_CONFIG_PATH="C:/msys64/mingw64/lib/pkgconfig"
/c/msys64/mingw64/bin/cmake.exe --build build-cmake -j4
# Windows blocca l'exe in esecuzione: il cp fallisce con "Device or resource busy".
MSYS2_ARG_CONV_EXCL="*" taskkill /IM "Endless Sky.exe" /F 2>/dev/null
cp "build-cmake/Endless Sky.exe" "build/Endless Sky.exe"
sha256sum "build-cmake/Endless Sky.exe" "build/Endless Sky.exe"   # devono coincidere
./"build/Endless Sky.exe" --resources src --config userdata --parse-assets
```

`review/export_ui_batches.py`, `review/classify_cpp_ui.py`, `review/final_ui_scope.py`,
`review/apply_cpp_ui.py` sono gli strumenti usati: quattro passi, nessun framework nuovo.
