# FASE E — Audit del percorso di localizzazione e piano d'integrazione

Sola ricognizione: **nessun file modificato, nessuna build, nessun test, nessun pacchetto**. Evidenze dai
file letti in `endless-sky-mingw` (copia di lavoro) e in `endless-sky-l10n` (workspace).

---

## 1. Stato verificato

| Elemento | Stato | Evidenza |
|---|---|---|
| `endless-sky` (originale) | `b4aa3bac3`, 0 modifiche | `git status` vuoto |
| `endless-sky-mingw` | `b4aa3bac3` + **4 file modificati** | `M images/font/ubuntu1{4,8}r.png`, `M source/text/Font.cpp`, `M source/text/Font.h` |
| Build | verde (incrementale), 37/37 | `build_font.log` → `build_exit=0` |
| Test | 46/46, exit 0 | `test_font.log` |
| Atlanti | 224 celle, 28 px / 36 px per cella | `ubuntu14r.png` 6272×32, `ubuntu18r.png` 8064×36 |
| Accenti nell'atlante | 12/12 glifi con inchiostro | controllo indice `ord-32` ↔ cella |
| Rendering a schermo | **non verificato** | nessuna cattura, nessun OCR |
| Selettore lingua | **non esiste** | vedi §2 |

## 2. Percorso della traduzione: dalla sorgente al gioco

**Non esiste alcun percorso.** Verificato:

| Domanda | Risposta | Evidenza |
|---|---|---|
| C'è un sistema i18n? | **No** | grep `l10n|translation|locale` su `source/`: solo un commento in `ZipFile.h` |
| C'è una selezione lingua? | **No** | `Preferences`/`PreferencesPanel`: nessuna occorrenza |
| Come si caricano i testi? | `UniverseObjects::Load` → `Files::RecursiveList(source/"data")` → `LoadFile` per ogni `.txt` | `UniverseObjects.cpp:40-80` |
| Quali radici esistono? | `Files::Resources()`, `Files::Data()` | `Files.h:34,38` |
| Come si identifica una stringa? | **Non si identifica**: il testo è il contenuto dell'oggetto; non ci sono chiavi | `DataFile`, per-classe `Load` |
| UTF-8 nei dati? | i file sono ASCII; il renderer ora decodifica UTF-8 (patch applicata) | `Font.cpp` patchato |
| Serve C++ o bastano i dati? | **Serve C++** per un selettore; i soli dati possono sostituire, non selezionare | vedi §5 |

Conseguenza: le traduzioni oggi esistono solo come **file di dati modificati** in
`endless-sky-l10n/output/l10n-it/data/_ui/` (`interfaces.txt`, `tooltips.txt`, `help.txt`). Il gioco non
li carica da lì: la directory non è una radice nota.

## 3. Le 352 unità: schema e significato

Schema effettivo (`state.db`, letto in sola lettura):

| Tabella | Righe | Contenuto |
|---|---:|---|
| `units` | 32.924 | id stabile, path, riga, kind, context, english, hash, italian, state, batch_id |
| `batches` | 5 | B001 244 · B002 40 · B003 40 · B004 25 · B005 3 |
| `issues` | 77 | esiti dei validatori per batch (warning/info) |
| `events`, `runs` | — | log di pipeline e benchmark |

Stati presenti: **`APPROVED` 352**, **`PENDING` 32.572**. Nessun `NEEDS_REVIEW`.

Cosa sono realmente le 352: **etichette UI, tooltip e 68 righe di guida** — non missioni, non descrizioni
di pianeti, non dialoghi. Copertura **1,07% delle unità** e **0,36% delle parole**: la partita resterebbe
in gran parte in inglese.

Esportazione esistente: `tools/apply_patch.py` legge `batches/*/output.json`, sostituisce **un solo token
per riga** nel file originale, verifica struttura e scrive in `output/l10n-it/<path>`. È un export
corretto ma **non integrato** con il gioco.

## 4. Gap bloccanti (in ordine di priorità)

| # | Gap | Effetto | Classe |
|---|---|---|---|
| G1 | Nessuna radice di caricamento per le traduzioni | i 3 file tradotti non vengono letti | **S** (verificabile leggendo il loader) |
| G2 | Nessun selettore lingua né persistenza | non si può passare IT/EN | **S** + **B** |
| G3 | Semantica di sovrascrittura disomogenea per classe | un overlay può duplicare o azzerare oggetti | **S** (per-classe) |
| G4 | Copertura 1,07% | gioco misto, non "in italiano" | **S** (stato db) |
| G5 | Rendering accenti non osservato | non sappiamo se si vedono | **R** |
| G6 | Packaging: `install(DIRECTORY data)` copia i dati così come sono | un pacchetto può contenere traduzioni mai caricate | **S** |

## 5. Piano d'integrazione minimo

Due opzioni; **consiglio la A**, perché è l'unica che soddisfa "italiano selezionabile".

### A. Selettore + radice di traduzione (raccomandata)

| File | Modifica | Scopo | Dipendenza |
|---|---|---|---|
| `source/Preferences.h/.cpp` | `std::string GetLanguage()` / `SetLanguage()` su `Preferences::Get`, default `"en"` | persistere la scelta | — |
| `source/GameData.cpp` (`BeginLoad`, ~154-173) | se `language != "en"` e `Files::Resources()/l10n/<lang>` esiste, **accodare** quella radice a `sources` | caricare dopo l'inglese, così l'overlay vince | G1 |
| `source/UniverseObjects.cpp` | nessuna modifica: `Files::RecursiveList(source/"data")` percorre già ogni radice | — | — |
| `source/PreferencesPanel.cpp` | voce lingua nella sezione Interface | selezione utente | A1 |
| `data` overlay | `l10n/it/data/_ui/*.txt` | contenuto tradotto | export esistente |

Nota critica: accodare la radice **dopo** l'inglese sfrutta l'ordine di caricamento; per le classi con
`shouldOverwrite` (es. `Planet.cpp:69`) la ridescrizione parziale è sicura, per altre (es. `Interface`)
va verificato che la seconda definizione sostituisca e non accodi duplicati. **Questo va deciso per
classe prima di scrivere il loader**, ed è il vero rischio tecnico della fase.

### B. Nessun selettore: due pacchetti

Sostituire i 3 file in `data/_ui/` nel pacchetto italiano. Costo quasi zero (nessuna build), ma niente
scelta lingua, niente fallback inglese, e il pacchetto diventa "IT-only". Accettabile solo come demo.

## 6. Piano di verifica

| Fase | Controllo | Classe | Criterio |
|---|---|---|---|
| 1 | `Preferences` legge/scrive la lingua su file | **S** | chiave presente nel file di preferenze |
| 2 | Radice `l10n/it` inclusa in `sources` quando la lingua è `it` | **S** (log) | riga di log con la radice |
| 3 | Overlay caricato senza duplicati | **R** | nessun warning "duplicate" e UI con etichette italiane |
| 4 | Fallback: lingua `it` con directory assente | **R** | avvio in inglese, nessun errore fatale |
| 5 | Accenti a schermo | **R** | screenshot leggibile di `à è é ì ò ù` |
| 6 | Regressione | **T** | `ctest --preset mingw-ci` 46/46 |

## 7. Rischi e rollback

- **Originale**: mai toccato (`b4aa3bac3`, 0 sporchi). Qualsiasi esperimento resta in `endless-sky-mingw`.
- **Rollback codice**: `git -C endless-sky-mingw checkout -- source/ images/font/` riporta alla baseline;
  i 4 file attuali sono l'unica modifica e sono rintracciabili da `git status`.
- **Traduzioni**: `state.db` non va scritto; le 352 approvate sono in `units` + `translation_memory.jsonl`.
  Backup consigliato prima della fase successiva: copia di `state.db` e di `batches/`.
- **Pacchetto**: `dist/endless-sky-it-0.1.0.zip` non va rigenerato finché il loader non carica davvero i dati.

## 8. Prossima tranche (non avviata)

**Tranche unica, prima della prossima build:**

1. **S** — decidere, classe per classe, se la ridescrizione dell'overlay sostituisce o duplica
   (`Planet`, `Interface`, `Outfit`, `Ship`, `Mission`); scrivere l'esito in una tabella nel workspace.
2. **S** — implementare in `endless-sky-mingw`: `Preferences::GetLanguage/SetLanguage`, la voce nel
   pannello, l'accodamento condizionale della radice in `GameData::BeginLoad`.
3. **S** — creare `l10n/it/data/_ui/` nella copia con i 3 file già esportati (nessuna ritraduzione).
4. **B** — una sola build: `cmake --build --preset mingw-ci`.
5. **R** — avvio con `language=it` e `l10n/it` presente → verificare etichette; poi con directory
   rinominata → verificare fallback; infine screenshot degli accenti.
6. **T** — `ctest --preset mingw-ci`.

Solo dopo il punto 5 si può parlare di "italiano selezionabile"; solo dopo il 6 di "pacchetto
distribuibile". E resterebbe vero che la copertura è dell'1,07%: il gioco sarebbe **mixed-language**, non
una localizzazione completa.
