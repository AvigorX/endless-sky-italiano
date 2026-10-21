# Fase post-traduzione — revisione globale, accenti, verifica pre-build

**Data:** 2026-10-21 · **Ambito:** `endless-sky-l10n` (workspace) · **Repo gioco:** `b4aa3bac3`, pulito
**Stato:** revisione eseguita e misurata. **Build non avviata** (non autorizzata in questa fase). **UI non tradotta.**

Tutti i numeri qui sotto sono rimisurati in questa sessione. Gli strumenti e i log sono in `review/`.

---

## 1. Baseline misurata (prima di ogni modifica)

| Voce | Valore |
|---|---|
| Unità in staging | 32 924 · 167 file · 403 lotti (402 con `translation.json`, 1 archivio storico) |
| Parole | 979 975 EN → 936 995 IT |
| `state.db` | 32 560 `PENDING` + 364 `APPROVED` = 32 924 · 0 unità fuori dallo staging |
| Inventario audit | 41 972 righe = 9 048 `NOT_LOCALIZABLE` + 32 924 `MISSING` · **0 `UNRESOLVED`** |
| File protetti | 7/7 integri (`sha256sum -c` con CRLF normalizzato) |
| Repo gioco | `git status --porcelain` = 0 righe, HEAD `b4aa3bac3` |
| Issue aperte nel DB | 88, tutte `warning`/`info`: 72 `NON_ASCII` (nota atlante font), 16 `GLOSSARY` (falsi positivi dello stem) |

Snapshot con sha256 di ogni artefatto: `review/baseline_prima_della_revisione.json`.

## 2. Difetto di integrità trovato e riparato (prima della revisione)

`parts/*.json` e `translation.json` erano **disallineati in 66 lotti**:
- **4 347 unità** in cui `translation.json` aveva i tab di paragrafo iniziali che il gate pretende identici
  all'inglese, mentre `parts/` li aveva persi;
- **9 unità** (bersagli `label` di conversazione, testo = inglese per necessità) presenti in
  `translation.json` e **assenti** da `parts/`.

Se si fosse eseguito `check`, `translation.json` sarebbe stato rigenerato da `parts` **perdendo i tab** e
fallendo il gate su 66 lotti. Riparazione in direzione `translation.json` → `parts` (l'artefatto verificato,
con gli sha del ledger), con backup, log per unità (`review/integrity_repair.jsonl`) e verifica che il
testo consegnato non cambiasse: **0 divergenze** fra corpus pre-riparazione e stato attuale.

## 3. Revisione linguistica: batch e modifiche

| batch | criterio | unità | lotti |
|---|---|---:|---:|
| R01 | nomi di missione lasciati in inglese (letti a mano, 24) | 24 | 11 |
| R02 | nomi di incarico in inglese la cui famiglia è già tradotta altrove: **157 stringhe distinte** | 412 | 52 |
| R03 | glossario: `disable` → **neutralizzare** (la stessa meccanica aveva 3 nomi) | 34 | 9 |
| R04 | glossario: `job board` → **bacheca degli incarichi** (3 varianti in uso) | 35 | 18 |
| **totale applicato** | | **491** (78 lotti, 118 file `parts`) | |

Ogni correzione è una riga di `review/applied.jsonl` con `id`, testo vecchio, testo nuovo, motivo e batch.
La reversione è una lettura di quel file. Pre-flight per ogni scrittura: tab, virgolette, segnaposto,
rapporto di lunghezza, caratteri tipografici, doppio spazio — gli stessi vincoli del gate.

Esempio della classe più numerosa (R02): `Supplies to <planet>` → `Provviste per <planet>`,
`Defend <planet>` → `Difendi <planet>` (allineato alla resa già in uso), `Wanted individual to <planet>` →
`Ricercato per <planet>`, `Twilight Guard Officers to <planet>` → `Ufficiali della Guardia del Crepuscolo per <planet>`.

**Dichiarazioni `id_ok.json`**: 1 388 unità restano identiche all'inglese per necessità e sono ora dichiarate
in 169 lotti (meccanismo previsto dal gate): 674 identificatori di flusso (`label`/`log`/`scene`/`gun`),
704 nomi propri o di equipaggiamento con prefisso alieno, 10 dichiarati singolarmente con motivo
(`review/idok_declared.jsonl`). Prima: 198 lotti con 1 810 unità identiche **non** dichiarate → il gate
falliva. Dopo: 0.

**Cosa non è stato toccato**: 0 unità `APPROVED` (le 364 del DB sono identiche), 0 unità `UI_LABEL`
nuove tradotte, 0 stringhe `_ui/*` modificate.

## 4. Audit degli accenti

| classe | unità | esito |
|---|---:|---|
| `e'` / `E'` al posto di `è` | **0** | nessuna occorrenza: verificato anche con ricerca diretta del token |
| apostrofo al posto dell'accento (`perche'`, `piu'`, `citta'`…) | **0** | — |
| accento sbagliato o superfluo (`perchè`, `nè`, `sè`, `pò`) | **0** | — |
| accento decomposto (NFD) o mojibake | **0** | tutte le forme sono NFC |
| parola accentata scritta senza accento | 3 candidati | **tutti falsi positivi verificati nel contesto** |

I 3 candidati: `Sara` (nome proprio di una senatrice, ×2) e `piu piu` (onomatopea di `pew pew`). Nessuna
correzione applicata — sarebbero stati errori.

Copertura dell'audit, per non dichiarare più di quanto misurato: **1 061 forme accentate distinte**,
33 444 occorrenze, elencate in `review/vocab_alpha.txt`; **89 collisioni di lemma** in
`review/incoerenze.txt`, tutte omografe legittime (`unità`/`unita` participio, `meta` sostantivo,
`dà`/`da`, `sé`/`se`). Le forme ambigue per natura (`e`, `la`, `li`, `si`, `ne`, `da`) sono 55 000+
occorrenze: sono state verificate con il rilevatore di copula (`che e`, `non e`, `e stato`…) → **0** casi
sospetti reali, e con la lettura di campioni deterministici sulle frasi narrative.

## 5. Lacuna dell'estrattore sulle news — stato reale

**Non è «solo il carattere `.`», ed è più ampia del dichiarato.** Le unità prodotte sono il carattere `"`
(virgolette), e il testo delle notizie non è mai stato estratto.

| | righe | parole |
|---|---:|---:|
| `message > word` (corpo delle notizie, visibile) | 1 577 | 27 974 |
| `name > word` (nome di chi parla, visibile) | 344 | 633 |
| `phrase > word` (parole composte, in parte tecniche) | 144 | 521 |
| riferimenti a `phrase` (da **non** toccare) | 34 | 79 |
| **testo effettivamente mancante** | **2 065** | **29 128** |

Su 979 975 parole dell'inventario: **2,97%**. Interessa 6 file, `human/news.txt` compreso.

**Causa dimostrata** (due difetti, entrambi necessari): manca il caso «riga = una sola stringa, senza
chiave» (il corpo delle news è scritto così) e il ramo `if bt:` scarta il resto della riga quando c'è un
backtick. **Intervento minimo proposto** in `review/PROPOSTA_ESTRATTORE.md`, con il diff esatto e la
condizione che esclude automaticamente i 34 riferimenti.

**Non applicato**: `l10n_inventory.py` genera l'inventario da cui `tools/l10n.py init` ricostruisce
`state.db`, che è protetto; il mandato vieta di scrivere nel DB e impone di fermarsi prima di modificare
l'estrattore. **Rischio**: le notizie restano in inglese nel gioco; la build non si blocca; il denominatore
di copertura però non contiene quelle righe, quindi «copertura 100% per ID» **non** significa copertura del testo.

## 6. Gate: eseguiti ed esiti

Gate riusato: `staging/editorial/tools/batch_lot.py check` + `verify` (nessun framework nuovo), orchestrato
da `review/gate.py` sui 403 lotti.

```
lotti eseguiti        402 (1 saltato: archivio storico senza parts/)
verdi                 395
falliti                 6
fail per difetto di traduzione   0
```

I 6 fallimenti, analizzati uno per uno, sono **difetti del controllo**, non della traduzione:

| lotto | controllo | causa misurata |
|---|---|---|
| `L19_20261017_201414`, `L22`, `L42`, `L198` | segnaposto «identici» | confronto **come lista**: l'italiano riordina i segnaposto (`<destination>` prima di `<date>`). Multinsieme identico: 0 segnaposto persi, 0 aggiunti |
| `L21b` | segnaposto «identici» | 6 segnaposto pronominali (`<they>`, `<their>`, `<they're>`, `<they are>`, `<they've>`) omessi: in italiano il soggetto e il possessivo (“sua flotta”) sono impliciti — resa corretta |
| `L16` | `verify`: «righe distinte» | la riga 555 contiene **3 unità** (nome, plurale, descrizione): il controllo presume una unità per riga |

Nessun tentativo di “aggiustare” la traduzione per far passare il gate. `L62` era fallito in una prima
esecuzione parallela (scrittura concorrente di `translation.json`), al secondo passaggio è verde.

**Log superato da non leggere come stato attuale.** `review/gate_riparati.log` contiene `lotti: 66 ·
falliti: 45`: è la corsa partita **prima** delle dichiarazioni `id_ok.json` ed è stata completata solo alla
fine della sessione. Rieseguita quella stessa lista di 66 lotti nello stato finale:

```
66 lotti → 65 verdi, 1 fallito (L42, riordino dei segnaposto: difetto del controllo già documentato)
```

Il totale globale non cambia (395 verdi / 6 falliti / 1 saltato), perché `L42` era già contato fra i 6.


**Nota di trasparenza.** Il `check` riscrive `translation.json` da `parts/` anche quando fallisce. Sul lotto
archivio `L19_20261017_201342` (1 636 unità, **senza `parts/`**, formato vecchio con ID non mappabili) il
file è stato azzerato. Impatto sul pipeline: **nullo** — quei 1 636 ID non erano mappabili e le stesse
righe sono ricoperte dai lotti successivi (0 ID orfani, 0 unità senza resa). L'artefatto storico non è
recuperabile e non è stato ricostruito per non fabbricare dati. `review/gate.py` ora **salta** i lotti senza
`parts/` e lo dichiara.

## 7. File modificati e integrità

| | |
|---|---|
| modificati | `staging/editorial/L*/parts/*.json` (118 file, 78 lotti), `id_ok.json` (169 lotti), `review/` (nuovo) |
| **non** modificati | `state.db` (sha e mtime invariati: 2026-10-17 16:33:18), `glossary.csv`, `staging/inventory_fields.csv`, `tools/l10n.py`, `output/l10n-it/data/_ui/*.txt` → **7/7 protetti integri** |
| unità `APPROVED` alterate | **0** |
| repo `../endless-sky` | non scritto, non committato, non ripulito · 0 righe di diff · HEAD `b4aa3bac3` |
| copertura | 32 924 unità uniche · **0 senza resa** · 0 ID presenti solo nel DB o solo nello staging · corpus ≡ `translation.json` (0 divergenze) |

Verifica di integrazione pre-build, la più vicina alla build vera senza scrivere nulla:

```
python staging/editorial/tools/apply_translations.py --l10n . --dest ../endless-sky --dry-run
→ 32 924 unità su 167 file · applicate 30 882 · saltate (identiche) 2 042 · errori 0 · exit 0
```

Ogni unità da sostituire compare **esattamente una volta** nella propria riga di sorgente: nessuna
sostituzione ambigua, nessuna riga persa.

## 8. Blocchi che impediscono la build

1. **Lacuna dell'estrattore** (§5): 2 065 righe di testo non sono nell'inventario. Serve un'autorizzazione
   per modificare l'estrattore e rigenerare `state.db`; in alternativa va dichiarata nella copertura.
2. **Il DB non contiene le traduzioni.** 32 560 unità sono `PENDING` nel DB e vivono solo in staging:
   `tools/package.py` calcola la copertura e il pacchetto dalle unità `APPROVED`, quindi confezionerebbe
   **364 unità**. La build «ufficiale» richiede la scrittura su `state.db`, **vietata in questa fase**.
3. **Compilazione del gioco**: `BUILD_RECON.md` §6-7 documenta il disallineamento della registry `vcpkg`
   (commit fissato dalla CI assente nel clone locale) e gli errori MSVC. Il patch font
   (`patches/0001-font-utf8.patch`) **non è mai stato compilato**. Nessun tentativo è stato fatto in questa
   fase: non era nel perimetro.

## 9. Stato di preparazione della build

| condizione | stato |
|---|---|
| revisione linguistica | eseguita (491 correzioni, 4 batch) |
| audit degli accenti | eseguito (0 errori reali su 33 444 occorrenze) |
| integrità `parts/` ↔ `translation.json` | riparata, 0 divergenze |
| copertura per ID | 32 924/32 924 |
| integrazione sulle righe di sorgente | `apply_translations --dry-run` exit 0, 0 errori |
| file protetti | 7/7 integri |
| gate per lotto | 395/402 verdi + 6 fallimenti da difetto del controllo (documentati) |
| lacuna estrattore | **aperta**, documentata con causa e proposta |
| DB allineato allo staging | **no** (fuori perimetro per mandato) |
| procedura di build individuata | `apply_translations.py --dest <copia>` → patch font + atlante → compilazione |

**Conclusione: il workspace è pronto per una build di verifica, ma la build non può essere prodotta in
questa fase** perché richiede la scrittura su `state.db` (vietata) e la compilazione con la toolchain non
ancora allineata. Nessuna build è stata eseguita: non viene dichiarato alcun esito di build.

## 10. UI

**Non avviata.** Nessuna `UI_LABEL` tradotta in questa fase, nessuna etichetta/pulsante/menu/tooltip
aggiunto, `_ui/help.txt`, `_ui/interfaces.txt` e `_ui/tooltips.txt` intatti (sha verificato). La revisione
delle traduzioni UI già presenti non ha prodotto modifiche: 0 correzioni su unità `interface:`/`tip:`/`help:`.

## 11. Strumenti prodotti (`review/`)

| file | cosa fa |
|---|---|
| `snapshot.py` | baseline con sha256 di tutti gli artefatti |
| `check_protected.py` | verifica dei file protetti (CRLF-safe) |
| `build_corpus.py` | corpus unico (id, EN, IT, lotto) da 403 lotti |
| `detect_accents.py`, `vocab_accents.py` | candidati accenti + inventario delle forme |
| `probe_incoerenze.py`, `probe_d1.py`, `classify_d1.py` | incoerenze ortografiche, residui inglesi |
| `detect_defects.py` | difetti concreti (omissioni, numeri, copia-incolla, segnaposto) |
| `probe_extractor_gap.py`, `probe_gap_blocks.py` | quantificazione della lacuna dell'estrattore |
| `repair_parts.py` | riparazione `parts/` con backup e log |
| `apply_fixes.py` | applica i batch con pre-flight identico al gate, backup e log |
| `declare_idok.py` | dichiarazione delle unità identiche per necessità |
| `gate.py` | orchestrazione del gate esistente + coerenza `parts`→`translation.json` |
| `sample.py`, `ctx.py`, `distinct.py` | strumenti di lettura e classificazione |
