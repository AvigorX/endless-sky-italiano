# Aggiornamento della build esistente con le traduzioni correnti

**Data:** 2026-10-21 · **Sorgente:** `endless-sky` @ `b4aa3bac3` (repo intatto, 0 righe di diff)
**Build esistente:** `GAME-SOURCE-LAB/endless-sky-it` (20 ottobre 2026) — **non modificata**
**Nuova build:** `GAME-SOURCE-LAB/endless-sky-it-v2` — separata, autosufficiente, verificata
**`state.db` non scritto**, nessuna unità approvata, UI non tradotta in questa fase.

---

## 1. Come è stata costruita la versione precedente

Fonte: `endless-sky-it/BUILD.md` (scritto il 20 ottobre), **verificato contro gli artefatti presenti**:

| Passo documentato | Riscontro sull'artefatto |
|---|---|
| `git -C ../endless-sky archive HEAD \| tar -x -C src` | `src/` senza `.git`, 204 file `data/*.txt`, `src/CMakeLists.txt` identico a HEAD tranne l'aggiunta dichiarata |
| `apply_translations.py --l10n ../endless-sky-l10n --dest src` | 65 file tradotti, **27 869 righe** cambiate rispetto a `git show HEAD:` (misurate oggi) |
| `verify_integration.py` | coerente: 27 870 unità su 27 869 righe (una riga ha 2 unità) |
| CMake + **MinGW/MSYS2**, `ES_USE_VCPKG=OFF`, `ES_USE_SYSTEM_LIBRARIES=ON`, `BUILD_TESTING=OFF` | `src/../build/CMakeCache.txt` conferma: `CMAKE_CXX_COMPILER=C:/msys64/mingw64/bin/g++.exe`, `CMAKE_PREFIX_PATH=C:/msys64/mingw64`, `CMAKE_GENERATOR=Ninja`, `BUILD_TESTING=OFF` |
| Correzione di portabilità `-DNOGDI=` su 5 sorgenti | presente solo nella copia, `src/source/CMakeLists.txt` |
| `bundle_dlls.py` | **22 DLL** accanto all'exe (il documento ne dichiarava 19) |
| Avvio con `--resources src --config userdata` | `Gioca Endless Sky IT.cmd`, `userdata/errors.txt` con il solo warning audio |

**Architettura rilevante:** i dati **non** sono compilati dentro l'eseguibile. L'exe riceve
`--resources src`; tradurre significa rigenerare `src/data/`, non ricompilare. L'exe della build del
20 ottobre (`sha256 764e7663…`) corrisponde allo stesso `HEAD` di oggi (`b4aa3bac3`).

## 2. Quali traduzioni entrano effettivamente

Misura (`review/compare_builds.py`, 204 file di dati, confronto con i blob di `HEAD`):

| | build 2026-10-20 | build 2026-10-21 | delta |
|---|---:|---:|---:|
| file di dati tradotti | 65 | **159** | +94 |
| righe tradotte | 27 869 | **30 879** | **+3 010** |
| unità applicate | 27 870 | **30 880** | +3 010 |
| unità saltate (identiche: nomi propri) | 1 382 | 2 044 | +662 |

Differenza fra le due build: **121 file, 3 067 righe**, così ripartite:

| componente | righe | file | nota |
|---|---:|---:|---|
| prosa (missioni, dialoghi, descrizioni, news già estratte) | 2 659 | 117 | lotti L333–L398 completati dopo il 20 ottobre + correzioni R01–R04 |
| `_ui/` | 408 | 4 | `interfaces.txt` 232, `help.txt` 113, `messages.txt` 53, `flight checks.txt` 10 — sono le **364 unità `APPROVED` già trascritte** nei lotti L327–L329 e L398 **prima** di questa fase |

Nessuna traduzione UI nuova è stata scritta in questa fase (0 correzioni su unità `interface:`/`tip:`/`help:`).
Se si vuole che la nuova build si comporti come quella del 20 ottobre anche nell'interfaccia, basta
escludere i 4 file `_ui/` dal passo 2 del piano (§6): è una scelta, non un difetto.

## 3. L'integrazione avviene senza scrivere in `state.db` — dimostrato

`apply_translations.py` legge i `translation.json` dei lotti e scrive **solo** nella copia indicata con
`--dest`. Non tocca il database, non approva unità, non modifica il repository.

```
python staging/editorial/tools/apply_translations.py --l10n . --dest ../endless-sky-it-v2/src
→ 32 924 unità su 167 file · applicate 30 880 · saltate (identiche) 2 044 · errori 0 · exit 0
```

Verifica indipendente, non auto-referenziale (confronto con `git show HEAD:`, riga per riga):

```
python staging/editorial/tools/verify_integration.py --dest ../endless-sky-it-v2/src
→ file confrontati 167 · righe cambiate 30 879 (attese 30 879) · FAIL 0 · exit 0
```

`state.db` non è stato scritto: sha `9125282973ddc8b9…` e mtime `2026-10-17 16:33:18` invariati.
`package.py` **non è stato usato**: confezionerebbe le sole 364 unità `APPROVED`.

## 4. Regressione trovata dal parse e corretta (da leggere)

La prima applicazione sulle nuove traduzioni **ha prodotto dati non caricabili**:

```
W | outfit "Motori atomici "Baellie"" is referred to, but not fully defined.
Parse completed with at least one error(s).   exit=1
```

Causa: nel batch R02 la mappa era per *stringa inglese*, quindi ha tradotto anche i **riferimenti** a un
identificativo di equipaggiamento in `data/hai/hai ships.txt` (righe 362 e 378), mentre la **dichiarazione**
`outfit `"Baellie" Atomic Engines`` è rimasta in inglese. Il gate per-lotto non poteva vederlo: virgolette,
segnaposto e rapporto erano identici. Lo ha visto solo `--parse-assets`.

Correzione: ripristinate all'inglese le 2 unità-riferimento, dichiarate in `id_ok.json`, lotto `L244`
riverificato verde (`check` 0, `verify` 0), dati riapplicati da estrazione pulita.

Controllo esteso a **tutte** le 491 correzioni della revisione, contro gli 8 015 nomi di oggetto
dell'inventario: solo 5 toccavano un testo che è anche nome di oggetto — 2 erano riferimenti (ripristinati),
3 erano `plural` di visualizzazione (legittimi: `Ausiliarie`, `Motori atomici "Baellie"`, `Motori ionici X1050`).

**Questo è il motivo per cui un parse va sempre eseguito dopo un'applicazione**: la verifica strutturale
per lotto non sostituisce il caricamento reale dei dati.

## 5. Stato della lacuna delle news

Confermata e contabilizzata (misura indipendente, `review/gap_extractor_by_block.txt`):

| | righe | parole |
|---|---:|---:|
| corpo delle notizie (`message > word`) | 1 577 | 27 974 |
| nomi di chi parla (`name > word`) | 344 | 633 |
| parole composte (`phrase > word`, in parte tecniche) | 144 | 521 |
| riferimenti a `phrase` (esclusi) | 34 | 79 |
| **testo mancante** | **2 065** | **29 128** |

= **2,97%** delle 979 975 parole dell'inventario, su 6 file. **Prova nel dato costruito:** in
`endless-sky-it-v2/src/data/hai/hai news.txt` i corpi delle notizie sono ancora in inglese, perché quelle
righe non esistono come unità.

`review/PROPOSTA_ESTRATTORE.md` resta **non applicata**: richiede di modificare `l10n_inventory.py` e
rigenerare `state.db`. Serve autorizzazione esplicita e un piano di backup (`state.db` copiato e
`sha256` registrato prima, ripristino = ricopia del file; il resto dello staging non dipende dall'inventario).

## 6. Blocchi di compilazione

**Nessun blocco per aggiornare i dati**: non serve compilare (§7).
Se si volesse ricompilare l'eseguibile:

| prerequisito | stato misurato |
|---|---|
| `g++` MinGW | **presente**: `C:/msys64/mingw64/bin/g++.exe` (16.1.0) — non nel PATH, va dato per percorso |
| cmake / ninja | presenti (`/c/Program Files/CMake/bin`, winget ninja; anche in `C:/msys64/mingw64/bin`) |
| header/librerie richiesti | **9/9 presenti** in `C:/msys64/mingw64/include`: SDL2, png, jpeg, avif, glew, openal, mad, FLAC, minizip |
| `vcpkg` | **non necessario**: la ricetta funzionante usa `ES_USE_VCPKG=OFF` + librerie di sistema MSYS2. Il `read-tree` fallito descritto in `BUILD_RECON.md` §6 riguarda solo il percorso vcpkg, che questa build non usa |
| correzione `-DNOGDI=` | necessaria (5 sorgenti), già applicata nella copia della build precedente |

Comando documentato, **non eseguito in questa fase**:

```bash
cmake -G Ninja -S src -B build -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_CXX_COMPILER=C:/msys64/mingw64/bin/g++.exe \
  -DCMAKE_PREFIX_PATH=C:/msys64/mingw64 \
  -DES_USE_VCPKG=OFF -DES_USE_SYSTEM_LIBRARIES=ON -DBUILD_TESTING=OFF \
  -DCMAKE_POLICY_VERSION_MINIMUM=3.5
cmake --build build -j4
```

## 7. Piano minimo per aggiornare la build esistente

La nuova directory **è già pronta e verificata**; questi sono i passi che l'hanno prodotta, riproducibili:

```bash
cd ~/PROGETTI/G-DEV/GAME-SOURCE-LAB
mkdir -p endless-sky-it-v2/src
git -C endless-sky archive HEAD | tar -x -C endless-sky-it-v2/src      # 1. estrazione pulita (b4aa3bac3)

cd endless-sky-l10n
python staging/editorial/tools/apply_translations.py --l10n . --dest ../endless-sky-it-v2/src   # 2. applica
python staging/editorial/tools/verify_integration.py --dest ../endless-sky-it-v2/src            # 3. verifica

cd ../endless-sky-it-v2
mkdir -p build userdata
cp ../endless-sky-it/build/"Endless Sky.exe" build/ && cp ../endless-sky-it/build/*.dll build/   # 4. riuso exe+DLL
../endless-sky-it/build/"Endless Sky.exe" --resources src --config userdata --parse-assets       # 5. parse
```

Il passo 4 **non è una scorciatoia**: l'exe è lo stesso sorgente (`b4aa3bac3`, `sha256 764e7663…` identico) e
i dati sono esterni. Ricompilare produrrebbe lo stesso binario.

## 8. Verifiche eseguite sulla nuova build (tutte con exit code)

| prova | comando | esito |
|---|---|---|
| applicazione | `apply_translations.py --dest ../endless-sky-it-v2/src` | **exit 0** · 30 880 applicate · 2 044 identiche · 0 errori |
| verifica indipendente | `verify_integration.py --dest …` | **exit 0** · 30 879 righe = 30 879 attese · FAIL 0 |
| parse dati **nuovi** | `--parse-assets --resources src` | **exit 0** · *Parse completed with no error(s)* |
| parse dati **inglesi** (baseline) | `--parse-assets --resources ../endless-sky` | **exit 0** · *no error(s)* |
| falsificabilità | la stessa invocazione sui dati con il riferimento rotto | **exit 1** · *at least one error(s)* → il controllo può fallire |
| avvio reale | `--resources src --config userdata` | processo attivo (`Endless Sky.exe`, pid 148512, 1,5 GB, sessione Console), finestra creata; `userdata/errors.txt` con il **solo** warning audio |

Nota per chi riproduce: `--config <dir>` **non crea** la directory. Se non esiste, il gioco esce con
`exit=3` e `Unable to create config directory!` prima di leggere i dati — non è un errore di dati.
Le prove qui sopra usano directory già create (`userdata/`, `userdata_en/`).

**Non verificato (dichiarato):** nessuna partita giocata, nessuna missione letta a schermo, nessuno screenshot
analizzato; l'audio non si inizializza in questa sessione (come nella build del 20 ottobre). La nuova build
riproduce le condizioni della precedente, con 3 010 righe di traduzione in più.

## 9. Cosa non è stato fatto

- `state.db` non scritto, nessuna unità approvata, `package.py` non eseguito.
- `endless-sky-it` (build del 20 ottobre) **non toccata**: nessun file sovrascritto o cancellato.
- Repository `endless-sky` non modificato, nessun commit, HEAD `b4aa3bac3` preservato.
- Estrattore delle news non modificato; `state.db` non rigenerato.
- UI non tradotta: 0 correzioni su unità UI in questa fase.
- Compilazione non eseguita (non necessaria per aggiornare i dati).

## 10. Artefatti

| percorso | contenuto |
|---|---|
| `endless-sky-it-v2/src/` | dati tradotti, 411 MB, 204 file `data/*.txt` |
| `endless-sky-it-v2/build/` | `Endless Sky.exe` + 22 DLL (39 MB), copiati dalla build precedente |
| `endless-sky-it-v2/Gioca Endless Sky IT v2.cmd` | avvio con profilo separato `userdata/` |
| `endless-sky-it-v2/parse_it.log`, `parse_en.log`, `gui_test.log`, `userdata/errors.txt` | log delle prove |
| `review/compare_builds.py` | confronto misurato repo ↔ vecchia ↔ nuova build |
| `review/fixes_R05_revert.jsonl` | le 2 unità-riferimento ripristinate, con motivo |
