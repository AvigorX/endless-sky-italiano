# CHECKPOINT — Endless Sky IT (build + localizzazione)

**Data:** 2026-10-17 · **Per:** sessione successiva · **Stato:** build verde, localizzazione non ancora caricabile.

Leggi questo file per intero prima di agire. Ogni numero qui è misurato; dove non lo è, è scritto.

---

## 1. Dove sono le cose

| Percorso | Ruolo | Stato |
|---|---|---|
| `GAME-SOURCE-LAB\endless-sky` | repository **originale** | `b4aa3bac3`, **0 modifiche** — mai toccare |
| `GAME-SOURCE-LAB\endless-sky-mingw` | copia di lavoro (MinGW) | `b4aa3bac3` + **4 file modificati** (patch UTF-8) |
| `GAME-SOURCE-LAB\endless-sky-build` | copia MSVC abbandonata | contiene 3 patch di portabilità MSVC, non serve più |
| `GAME-SOURCE-LAB\endless-sky-mingw-vcpkg-ci` | vcpkg isolato a `89dc8be6` | **inutilizzabile** con questo progetto (vedi §6) |
| `C:\vcpkg` | vcpkg condiviso `a5f736224e` | intatto, non usato dalla build |
| `GAME-SOURCE-LAB\endless-sky-l10n` | workspace localizzazione | `state.db`, pipeline, staging, pacchetto |

## 2. Build — VERIFICATA

| Prova | Valore |
|---|---|
| Configure | `build/ci`, exit 0, deps vcpkg “completed successfully in 11 min” |
| Build | `build_exit=0`, 264/264, `build/ci/Endless Sky.exe` 6.171.821 B |
| Test | `ctest --preset mingw-ci` → **46/46**, `test_exit=0`, 405–430 s |
| Toolchain | MinGW `x86_64-w64-mingw32-g++` (MSYS2), Ninja, triplet `win64-release`, `ES_USE_SYSTEM_LIBRARIES=OFF` |

**Comando di build (funzionante):**
```bash
cd endless-sky-mingw
export CI=true VCPKG_ROOT=C:/Users/Dave/PROGETTI/G-DEV/GAME-SOURCE-LAB/endless-sky-mingw-vcpkg-ci
export PATH=/c/msys64/mingw64/bin:$PATH
"C:/msys64/mingw64/bin/cmake.exe" --build --preset mingw-ci
"C:/msys64/mingw64/bin/ctest.exe" --preset mingw-ci
```

## 3. Font UTF-8 — applicato e compilato, **rendering non osservato**

Modifiche in `endless-sky-mingw` (le uniche 4):
```
M images/font/ubuntu14r.png   (b5da523c… → fcc9ebd9…, 20.991 B)
M images/font/ubuntu18r.png   (aafa812a… → 9b77faf7…, 27.259 B)
M source/text/Font.cpp        (GLYPHS 224, Glyph(char32_t), UTF-8 in Draw/Width)
M source/text/Font.h
```
Atlanti: 224 celle, 28 px / 36 px per cella, 12 glifi critici con inchiostro verificato
(`à:192, è:200, é:201, ì:204, ò:210, ù:217`, maiuscole 160–185). Build e test verdi **con** patch.

**Non verificato:** il rendering a schermo. Manca uno screenshot; nessun OCR disponibile. Non dichiararlo.

## 4. Localizzazione — 364 unità approvate

| Metrica | Valore |
|---|---:|
| Unità localizzabili | 32.924 |
| **APPROVED** | **364** (1,106%) |
| PENDING | 32.560 |
| Batch | B001 244 · B002 40 · B003 40 · B004 25 · B005 3 · B006 12 |
| SAFE pendenti | 3.493 (484 tooltip, 972 pianeti, 143 missioni umane, …) |
| CONSTRAINED pendenti | ~29.067 |
| Escluse (identificatori) | 9.048 |

Output approvati (hash da non cambiare senza motivo):
`interfaces.txt` `5912ad739fe79fd4` · `tooltips.txt` `2cf104fee408313c` · `help.txt` `1e0108530781320a`.

**Benchmark Fase K2:** 30 unità tooltip tradotte dal modello di sessione, **0 errori QA**, 15 warning
`NON_ASCII`, verdetto **GO CON RISERVE** (placeholder mai esercitati).
Report: `endless-sky-l10n\staging\benchmarks\hermes_deepseek_20261017_164125\REPORT.md`.

## 5. Gap che bloccano il "gioco in italiano"

1. **Non esiste loader per le traduzioni.** `UniverseObjects::Load` legge solo `<resources>/data`;
   nessun i18n, nessun `Preferences` di lingua. I 3 file tradotti in `output/l10n-it/` **non vengono letti**.
2. **Nessun selettore lingua** (serve `Preferences::GetLanguage/SetLanguage` + radice
   `Resources()/l10n/<lang>` accodata in `GameData::BeginLoad`).
3. **Semantica di sovrascrittura da decidere per classe** prima di accodare una radice:
   `Planet` ha `shouldOverwrite` (sicuro), `Interface` no (rischio duplicati UI).
4. **Copertura 1,1%**: anche finito il loader, il gioco sarebbe bilingue.
5. **Accenti non osservati a schermo.**

## 6. Trappole già pagate (non ripeterle)

- **`cmd //c` da MSYS non esegue i batch**: exit 0 falso, nessun effetto. Verificare sempre l'effetto
  (es. `CMakeCache.txt`), non l'exit code.
- **Preset `mingw-ci` “disabled”**: `ci` ha `condition: $env{CI}=="true"`. Serve `CI=true`.
- **vcpkg**: il progetto usa `vcpkg-configuration.json` → baseline **`a3476c776e`** e overlay locali.
  La copia isolata a `89dc8be6` **non** contiene `catch2 3.10.0` → non usarla.
  `CMakeLists.txt:32-38` **ignora `VCPKG_ROOT`** e forza `${sourceDir}/vcpkg`.
- **`ccache` è obbligatorio**: preset `ci` imposta `CMAKE_CXX_COMPILER_LAUNCHER=ccache`; senza, la build
  muore con `CreateProcess failed`. Installato `mingw-w64-x86_64-ccache 4.13.6`.
- **`-B` funziona con `--preset`** (serve per non toccare `build/ci`).
- **Symlink `compile_commands.json`** fallisce senza Developer Mode: errore non fatale.
- **Pipeline l10n**: le cifre finali sono un frame solo se precedute da un marker (`^3`, `+0`);
  `dialog phrase "X"` è un riferimento, non testo; `dynamic button`/`wrapped string` sono binding.
- **`apply_patch.py`** preserva i fine riga (CRLF) e verifica un solo token cambiato per riga.

## 7. Prossimi passi, in ordine (con criteri di accettazione)

1. **Loader + selettore (S+B)** — `Preferences::{Get,Set}Language`, voce nel pannello, radice
   `Resources()/l10n/<lang>` in `GameData::BeginLoad` **solo se la dir esiste**.
   *Accettazione:* avvio con `it` → etichette italiane; con dir rinominata → inglese senza errori fatali.
2. **Verifica accenti (R)** — screenshot leggibile di `à è é ì ò ù`; senza immagine, resta “non verificato”.
3. **Lotto misto 30 unità con ≥10 placeholder** (mission/help) → QA deterministico a zero errori.
4. **Solo dopo**: lotti da 150 (candidati pronti in `staging/candidates_B007.json`, 2.375 parole).
5. **Packaging (B)** — `install(DIRECTORY data ...)`; non generare ZIP finché il loader non carica davvero.

## 8. Comandi di ripresa

```bash
cd endless-sky-l10n
python tools/l10n.py status                 # stati per batch
python tools/l10n.py build --batch B007 --name "Tooltips SAFE (bulk)" \
  --where "path='data/_ui/tooltips.txt' AND state='PENDING'" --limit 30
python tools/l10n.py export B007            # batches/B007/input.json
#   tradurre → batches/B007/output.json  ([{"id","it"}])
python tools/l10n.py import B007            # valida e approva solo con 0 errori
python tools/apply_patch.py B006 B007       # cumulativo, token-exact
python tools/validate_pipeline.py           # exit 0/1
```

**Alternativa automatica:** `python tools/worker.py --engine api --batch B007 --where "..." --limit 150`
funziona **solo** se `DEEPSEEK_API_KEY` è esportata nel processo. Oggi: unset, nessun endpoint locale.
Non chiedere la chiave in chat e non stamparla.

## 9. Invarianti da non violare

- `endless-sky` resta `b4aa3bac3` e pulito.
- `state.db` non si scrive a mano; si passa sempre da `l10n.py`.
- Le 364 approvate e i 3 file di output non si sovrascrivono.
- Nessun `git reset/clean`, nessun checkout distruttivo.
- Patch, atlanti e modifiche vivono **solo** in `endless-sky-mingw`.
