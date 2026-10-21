# Endless Sky — Traduzione italiana

Localizzazione italiana di **Endless Sky 0.11.4-alpha** (commit `b4aa3bac3`) per Windows, con
build già compilata, dati inglesi originali e tutto il corpus di traduzione che serve a
mantenerla.

## Che cosa contiene

| Cartella | Contenuto |
|---|---|
| `data-it/` | Dati italiani: storia, dialoghi, missioni, pianeti, descrizioni delle navi, news tradotte. **Interfaccia ed equipaggiamenti in inglese** (scelta editoriale, vedi sotto) |
| `data-en/` | Dati inglesi originali, intatti (da `git archive` del commit di riferimento) |
| `data/` | Insieme attivo: viene reso identico a `data-it` o `data-en` dal launcher scelto |
| `build/` | `Endless Sky.exe` + 22 DLL richieste |
| `images/`, `sounds/`, `shaders/`, `credits.txt` | Risorse condivise dal motore (non tradotte) |
| `source/`, `CMakeLists.txt` | Sorgenti C++ del gioco, per ricompilare |
| `tools/` | Strumenti di manutenzione della traduzione |
| `translations/` | Corpus completo: 405 lotti di staging, `state.db`, glossario |
| `docs/` | Report di revisione, decisioni, problemi noti; `docs/history/` = cronologia dei lotti |
| `patches/`, `font/` | Correzione UTF-8 dei glifi accentati e relativo report |

## File di risorse upstream indispensabili

Sono file del commit `b4aa3bac3` che il motore legge (o che la build richiede) e che **non vanno
eliminati**: se mancano, il gioco parte ma si comporta in modo anomalo senza stampare errori evidenti.

| File | Perché serve | blob git in `b4aa3bac3` |
|---|---|---|
| `keys.txt` | binding di tastiera **predefiniti**: `Command::LoadSettings()` non ha default nel codice, li legge solo da questo file. Senza, nessun tasto risulta assegnato e `PreferencesPanel::Exit()` rifiuta di salvare («Menu keybind is not bound»): le assegnazioni sembrano non essere mantenute | `45de4921` |
| `icons/WinApp.ico` | richiesto da `source/windows/WinApp.rc` (windres) e da `CPACK_NSIS_MUI_ICON`: senza, la compilazione Windows si ferma sulla risorsa mancante | `f49c97c1` |
| `license.txt` | richiesto da `install(FILES license.txt)` e da `CPACK_RESOURCE_FILE_LICENSE` | `9cecc1d4` |
| `utils/vcpkg_bootstrap.cmake` | incluso da `CMakeLists.txt` solo con `ES_USE_VCPKG=ON`; serve per ricompilare via vcpkg | `f29d8852` |

## Avviare il gioco

Nessuna installazione: doppio clic sul launcher scelto.

| File | Lingua |
|---|---|
| **`Gioca in italiano.cmd`** | italiano (storia e contenuti narrativi) |
| **`Play in English.cmd`** | inglese (originale) |

Ogni launcher rende `data/` identica al proprio insieme con `robocopy /MIR` e avvia il gioco con
`--resources .`. La selezione avviene **prima dell'avvio**, non dentro il gioco: il motore 0.11.4
non ha un selettore di lingua per i dati.

> Il metodo nativo a plugin è stato provato e **scartato su misura**: una cartella in
> `plugins/` viene caricata sempre (anche rinominata) e produce migliaia di
> `Duplicate definition` — 4.203 righe di log, `--parse-assets` con exit 1.

## Che cosa è tradotto e che cosa no

| Contenuto | Lingua | Copertura |
|---|---|---|
| Storia, dialoghi, missioni, eventi | italiano | 26.043 / 26.886 unità |
| Pianeti e sistemi | italiano | 1.548 / 1.549 |
| Descrizioni delle navi | italiano | 322 nomi (501 unità, varianti incluse) |
| News (korath, successor) | italiano | 113 / 685 unità nei 5 file news |
| **Interfaccia, menu, Preferences, tooltip** | **inglese** | 1.087 / 1.087 |
| **Componenti, outfit, descrizioni tecniche** | **inglese** | 1.127 / 1.127 |

La separazione è deliberata: erano le stringhe di interfaccia tradotte a sfondare i riquadri a
larghezza fissa, e i nomi tecnici di componenti e outfit devono restare allineati alla
documentazione e ai riferimenti interni.

## Compilare

Servono MinGW-w64 (MSYS2), CMake e le librerie SDL2/openal/libpng/libjpeg/libavif.
Comando **verificato** (configure exit 0 → 228/228 unità → eseguibile 6.047.003 byte):

```bash
export PATH="/c/msys64/mingw64/bin:$PATH"          # serve a g++ e a ninja
export PKG_CONFIG_LIBDIR="C:/msys64/mingw64/lib/pkgconfig"   # CMake >= 3.31 usa cmake_pkg_config
cmake -G Ninja -S . -B build-cmake -DCMAKE_BUILD_TYPE=Release \
  -DES_USE_VCPKG=OFF -DES_USE_SYSTEM_LIBRARIES=ON -DBUILD_TESTING=OFF \
  -DCMAKE_MAKE_PROGRAM=C:/msys64/mingw64/bin/ninja.exe \
  -DCMAKE_C_COMPILER=C:/msys64/mingw64/bin/gcc.exe \
  -DCMAKE_CXX_COMPILER=C:/msys64/mingw64/bin/g++.exe
cmake --build build-cmake -j8
```

`PKG_CONFIG_LIBDIR` è indispensabile: `cmake_pkg_config(EXTRACT minizip)` cerca i `.pc` nativi e senza
quella variabile la configure si ferma con `Could not find pkg-config: 'minizip'`. Il messaggio
`failed to create symbolic link 'build/compile_commands.json'` (privilegio non concesso) **non è fatale**:
la configure prosegue e l'eseguibile viene prodotto.

Windows blocca un eseguibile in esecuzione: chiudere il gioco prima di sostituire
`build/Endless Sky.exe` (un `cp` senza `taskkill` fallisce con `Device or resource busy` e
lascia il vecchio binario al suo posto).

## Aggiornare la traduzione

```bash
# 1. verificare l'integrità dei file protetti
python tools/check_protected.py

# 2. applicare il corpus a un insieme di dati
python tools/apply_translations.py --l10n . --dest ../lavoro/data

# 3. verificare che ogni unità applicata sia presente (FAIL 0 = ok)
python tools/verify_integration.py --dest ../lavoro/data

# 4. controllare un lotto
python tools/batch_lot.py check translations/editorial/L398_20261021_132036
python tools/batch_lot.py verify translations/editorial/L398_20261021_132036
```

`state.db` è in **sola lettura** in questo pacchetto: contiene 364 unità `APPROVED` con testo
italiano nei tre file `_ui/`, che il gate confronta. È il conflitto documentato in
`docs/ALLINEAMENTO_20261021.md` §4 — **non va forzato**: la build usa l'inglese per scelta, il
database conserva lo stato approvato.

## Limiti noti

1. **News incomplete**: 113 unità tradotte su 685 nei cinque file news. Restano fuori i frammenti
   di composizione (`remnant`, `successor`) e i file `hai`, `wanderer`. Gli **hail** (il testo che
   scorre in basso) hanno la stessa lacuna dell'estrattore e sono molto più estesi: `human/hails.txt`
   da solo vale 5.478 righe / 20.333 parole, non estratte.
2. **Nessuna lingua selezionabile in gioco** (motore 0.11.4); la scelta è nel launcher.
3. **Verifica visiva parziale**: avvio, parsing (`exit 0`) e contenuti sono verificati; la finestra
   OpenGL di questo ambiente non è catturabile, quindi l'aspetto a schermo non è stato documentato
   con screenshot.
4. `credits.txt` (550 righe, mostrato nel menu principale) non è tradotto: l'estrattore percorre
   solo `data/`.

## Note per GitHub

L'eseguibile e `translations/state.db` sono binari: se il repository supera i limiti di dimensione
conviene Git LFS (`git lfs track "*.exe" "*.dll" "*.db"`). La build è inclusa di proposito, non va
omessa.

Codice del gioco: Endless Sky è distribuito con licenza GPL-3.0 (vedi `source/`).
