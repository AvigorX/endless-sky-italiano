# BUILD RECON — Endless Sky 0.11.3 (commit `b4aa3ba`)

Ricognizione **documentale e diagnostica**, nessuna build eseguita, nessun file di sorgente modificato,
nessuna dipendenza installata o aggiornata. Ogni affermazione cita il file o il log da cui deriva.

---

## 1. Documenti e file letti

| Percorso | Cosa contiene | Rilevanza |
|---|---|---|
| `docs/readme-developer.md` (righe 21-46) | istruzioni Windows e Windows (MinGW) | toolchain raccomandata |
| `.github/workflows/ci.yml` (righe 133-179) | job `build_windows` | toolchain **effettivamente usata dalla CI** |
| `CMakePresets.json` | preset `base`, `ci`, `release`, `mingw*` | configurazioni supportate |
| `CMakeLists.txt` (righe 1-15, 78-140) | opzioni e dipendenze | semantica delle opzioni |
| `vcpkg.json` | manifest e feature | grafo dipendenze |
| `C:\vcpkg\versions\baseline.json` | baseline della registry locale | stato del registry |
| `endless-sky-mingw/configure_vcpkg2.log` | errore vcpkg | causa del fallimento |
| `endless-sky-mingw/build/vcpkg-manifest-install.log` | log dettagliato vcpkg | oggetto Git mancante |

---

## 2. Toolchain raccomandata dai documenti

`docs/readme-developer.md:23-33` — **Windows (MSVC)**: Visual Studio 2022 (o Build Tools) con i componenti
*Desktop Development with C++*, **C++ Clang Compiler for Windows**, *C++ CMake tools for Windows*.

`docs/readme-developer.md:35-45` — **Windows (MinGW)**: distribuzione **Winlibs** (GCC ≥ 14.2, x86_64,
threads posix, eccezioni seh, runtime **UCRT**); MSYS2 è ammessa esplicitamente: «It is possible to use
other MinGW distributions too (like Msys2 for example), but you'll need to make sure to install CMake
(3.21 or later) and Ninja».

## 3. Toolchain effettivamente usata dalla CI per questa revisione

`.github/workflows/ci.yml`:

- job `build_windows`, `runs-on: windows-2025` (riga 137);
- `lukka/run-vcpkg@v11` con **`vcpkgGitCommitId: '89dc8be6dbcf18482a5a1bf86a2f4615c939b0fb'`** (riga 170);
- comandi: `cmake --preset mingw-ci` · `cmake --build build --preset mingw-ci` · `ctest --preset mingw-ci`
  (righe 173-175).

Preset `mingw-ci` (da `CMakePresets.json`): eredita `ci` (Ninja, `Release`, `ES_USE_VCPKG=ON`,
`ES_USE_SYSTEM_LIBRARIES=OFF`, `CMAKE_COMPILE_WARNING_AS_ERROR=ON`, `CMAKE_POLICY_VERSION_MINIMUM=3.5`)
e aggiunge:

```
CMAKE_CXX_COMPILER      = x86_64-w64-mingw32-g++
CMAKE_RC_COMPILER       = windres
VCPKG_HOST_TRIPLET      = win64-release
VCPKG_TARGET_TRIPLET    = win64-release
```

Preset `mingw` (sviluppo, non CI) usa invece `x64-mingw-dynamic`.

**Conclusione:** la CI Windows di questa revisione è **MinGW + vcpkg a commit fissato + triplet
`win64-release`**, non MSVC.

---

## 4. Opzioni CMake: semantica reale

| Opzione | Definizione | Conseguenza |
|---|---|---|
| `ES_USE_VCPKG` | `option(... OFF)` alla riga 5, `option(... ON)` alla riga 7 (rami di piattaforma) | il default dipende dal ramo; la CI la forza a `ON` |
| `ES_USE_SYSTEM_LIBRARIES` | `cmake_dependent_option(... ON "APPLE OR ES_STEAM" OFF)` (riga 12) | **è ON solo su macOS o build Steam**; altrove è OFF e le librerie arrivano da vcpkg |
| `BUILD_TESTING` | `option(... ON)` (riga 15) | i test sono attivi per default |

**Discrepanza grave nei miei tentativi:** ho forzato `ES_USE_SYSTEM_LIBRARIES=ON` su Windows. È una
combinazione che il progetto **non usa** su questa piattaforma: da lì la cascata di dipendenze mancanti
(`libavif`, `GLEW`, `FLAC`, blocco audio, `minizip`, …), ognuna delle quali esiste nel grafo vcpkg ma non
nel set di sistema che stavo costruendo a mano.

---

## 5. Grafo delle dipendenze (da `CMakeLists.txt` + `vcpkg.json`)

**CMake, librerie richieste** (`CMakeLists.txt:78-140`):

| Dipendenza | Come viene cercata | Note |
|---|---|---|
| SDL2 / SDL3 | `find_package(SDL2 CONFIG)` o `SDL3` con `ES_USE_SDL3` | default SDL2 |
| PNG, JPEG | `find_package(... REQUIRED)` | — |
| libavif | `find_package(libavif REQUIRED)` | mancava nel mio set |
| GLEW | `find_package(GLEW REQUIRED)` se `NOT APPLE` | mancava |
| OpenAL | `find_package(OpenAL CONFIG QUIET)` altrimenti `find_library(openal)` | — |
| libmad | `find_path(mad.h)` + `find_library(mad)` | nessun supporto CMake nativo |
| FLAC | `find_package(FLAC CONFIG)` (con `PkgConfig` di riserva) | mancava |
| ZLIB, minizip | `find_package(ZLIB REQUIRED)`, `unofficial-minizip`/`pkg-config minizip` | mancava minizip |
| Threads | `find_package(Threads REQUIRED)` | — |
| catch2 | solo con `BUILD_TESTING` | — |

**vcpkg, feature del manifest:** `system-libs` (glew, libavif, libpng, libjpeg-turbo, libmad, libflac,
minizip, openal-soft), `sdl2`, `sdl3`, `test-libs` (catch2), `steam-libs`. Override: `openal-soft 1.23.1#2`.

---

## 6. Causa dimostrata del fallimento vcpkg

Dal log `build/vcpkg-manifest-install.log`:

```
error: git --git-dir "C:\vcpkg\.git" -c core.autocrlf=false read-tree -- b7a86219797184383b76c0efa3eeb54aaee060bd
       failed with exit code 128
fatal: failed to unpack tree object b7a86219797184383b76c0efa3eeb54aaee060bd
```

Verifiche eseguite:

| Verifica | Comando | Esito |
|---|---|---|
| L'oggetto esiste nel repo locale? | `git -C C:/vcpkg cat-file -t b7a8621…` | **`fatal: could not get object info`** → non esiste |
| È un commit valido del repo? | `git merge-base --is-ancestor b7a8621… HEAD` | **`fatal: Not a valid commit name`** |
| HEAD della registry locale | `git -C C:/vcpkg rev-parse --short HEAD` | **`a5f736224e`** |
| Il commit fissato dalla CI esiste? | `git -C C:/vcpkg cat-file -t 89dc8be6…` | **`commit`** → presente |
| Clone parziale? | `git config remote.origin.partialclonefilter/promisor` | **nessun valore** (coerente con `fsck` pulito) |

**Causa dimostrata:** il repository vcpkg locale è integro ma **non è il commit che la CI usa**
(`a5f736224e` vs `89dc8be6…`). Il manifest di Endless Sky **non dichiara un `builtin-baseline`**, quindi la
risoluzione dei port dipende dallo stato della registry del tool; lo stato presente cita un albero
(`b7a8621…`) che in questa copia non esiste, e `read-tree` fallisce prima di installare qualsiasi port.
Non è corruzione (fsck passa) né shallow (nessun filtro): è **disallineamento tra registry e baseline
attesa**.

---

## 7. Confronto: istruzioni documentate vs tentativi effettuati

| Aspetto | Documenti / CI | Tentato | Esito |
|---|---|---|---|
| Compilatore | MSVC+Clang (docs) / **MinGW** (CI) | MSVC | errori `C2059`, `C2248`, `C2666` |
| Librerie | vcpkg (`ES_USE_VCPKG=ON`) | `ES_USE_SYSTEM_LIBRARIES=ON` | 5 dipendenze mancanti a cascata |
| vcpkg | commit fissato `89dc8be6…` | clone locale `a5f736224e` non fissato | `read-tree` fallisce |
| Triplet | `win64-release` (CI) / `x64-mingw-dynamic` (dev) | `x64-mingw-dynamic` | mai arrivato a installare |
| CMake | CMake di MSYS2 o VS | prima `C:\Program Files\CMake`, poi MSYS2 | PATH non tradotto al primo giro |
| Preset | `mingw-ci`, `mingw`, `release` | invocazioni manuali con `-D` | deviazione dalle convenzioni |

Ogni riga è un mio scostamento documentato, non un difetto del repository.

---

## 8. Piano di recupero (unico, in ordine)

1. **Allineare vcpkg al commit della CI** (senza toccare Endless Sky):
   `git -C C:/vcpkg checkout 89dc8be6dbcf18482a5a1bf86a2f4615c939b0fb`
   e `C:/vcpkg/bootstrap-vcpkg.bat -disableMetrics` se il tool va rigenerato.
2. **Definire la baseline nel manifest della copia di lavoro** (solo `endless-sky-mingw/vcpkg.json`):
   `"builtin-baseline": "89dc8be6dbcf18482a5a1bf86a2f4615c939b0fb"`.
3. **Usare il preset della CI** invece di `-D` manuali:
   `"C:/msys64/mingw64/bin/cmake.exe" --preset mingw-ci` (con `VCPKG_ROOT=C:/vcpkg`),
   verificando che `x86_64-w64-mingw32-g++` e `windres` siano in `C:/msys64/mingw64/bin`.
4. Build: `cmake --build build --preset mingw-ci`; test: `ctest --preset mingw-ci`.
5. Solo a baseline verde: patch UTF-8 + atlanti `*_it.png`, ricompilare, test ASCII/accenti/multibyte;
   poi selettore lingua; infine runtime e pacchetto.

**Rischio residuo dichiarato:** il passo 1 riscarica la storia della registry (rete, minuti); il passo 3
può richiedere `ccache` (impostato da `ci`) — se assente, va rimosso `CMAKE_CXX_COMPILER_LAUNCHER` o
installato `mingw-w64-x86_64-ccache`.

**Nessuna di queste azioni è stata eseguita in questa fase.**
