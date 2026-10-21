# ENDLESS SKY IT — ALLINEAMENTO FINALE (21 ottobre 2026)

Build di lavoro: `../endless-sky-it-v2/` · repo gioco `../endless-sky` @ `b4aa3bac3` (0 righe di diff)
`state.db` **non scritto** (`9125282973ddc8b9`, mtime 17/10 16:33) · file protetti **7/7** integri

---

## 1. Regola applicata

| Contenuto | Lingua | Unità | Stato |
|---|---|---|---|
| Storia, dialoghi, missioni, eventi | italiano | 26.043 / 26.886 | conservato |
| Pianeti e sistemi | italiano | 1.548 / 1.549 | conservato |
| **Descrizioni delle navi** | italiano | **501 / 501** | **conservato** |
| **Interfaccia dati** (`_ui/*`: menu, etichette, tooltip, messaggi) | inglese | **1.087 / 1.087** | **ripristinato** |
| **Componenti e outfit** (nomi + descrizioni tecniche) | inglese | **1.127 / 1.127** (996 descrizioni) | **ripristinato** |
| News ed eventi | italiano | 113 tradotte su 685 | **in corso** |

## 2. Ripristini effettuati (mirati per unità, non per file)

- **2.074 unità** riportate all'inglese in **98 lotti** (1.075 interfaccia + 999 outfit), su **114 file `parts/`**.
- **393 stringhe C++** (491 occorrenze, 68 file) invertite: verifica completa → *italiano residuo 0, inglese presente 393/393*.
- L'italiano rimosso è archiviato in `review/reverted_ui_it.jsonl` (2.074 record: id, lotto, inglese, italiano tolto): reversibile in blocco.
- Motivo del ripristino: era la UI tradotta a sfondare i riquadri a larghezza fissa; con l'inglese si torna al layout di riferimento.
- Ripristino solo delle unità interessate: **0 descrizioni di navi toccate** (controllo automatico in `review/make_r10_revert.py`).

## 3. News in tempo reale

**Causa misurata della lacuna**: l'estrattore ufficiale scarta le righe formate da una sola stringa, cioè le alternative dei blocchi `word` — che sono il corpo delle notizie e degli hail.

Testo reale nei 5 file news indicati: **685 unità / 8.163 parole**.
Intervento minimo: `review/extract_news_units.py` estrae quelle righe in **lotti `N*`** di staging (id `N|file|word|riga|0`), senza toccare `tools/l10n.py`, `l10n_inventory.py` né `state.db`. I due glob di `apply_translations.py` e `verify_integration.py` accettano ora anche `N*`.

| File | Unità | Tradotte | Note |
|---|---|---|---|
| `korath news.txt` | 44 | **44** | completo, 39 distinte + 5 nomi propri |
| `successor news.txt` | 119 | **69** | tradotte le unità autosufficienti |
| `remnant news.txt` | 161 | 0 | **frammenti** (2,2 parole/unità): tradurli 1:1 produce italiano sgrammaticato |
| `hai news.txt` | 246 | 0 | 4.146 parole, da fare |
| `wanderer news.txt` | 115 | 0 | 1.771 parole, da fare |
| **totale** | **685** | **113 (16%)** | |

**Frammenti**: i blocchi `40-77` e `13-25` di `successor news.txt` sono pezzi da concatenare (`"Interested in " + ", noble captain?"`). Restano in inglese per scelta: la traduzione richiede di ripianificare la composizione, non una sostituzione riga per riga.

**Hail (testo che scorre in basso)**: stessa lacuna, volume molto maggiore — `human/hails.txt` **5.478 righe / 20.333 parole**, `korath hails.txt` 803 / 2.754, `successor hails.txt` 648 / 2.431. Non estratti, non tradotti: **restano in inglese**.

## 4. Gate

98 lotti riequilibrati rieseguiti: **93 verdi, 5 rossi**.

I 5 rossi (`L111` tooltips, `L327`/`L328`/`L329` help, `L398` interfaces) falliscono **per conflitto con i dati protetti**, non per difetto di traduzione:

```
check  | stato: PENDING originale, o APPROVED trascritta identica al DB | FAIL
verify | unità APPROVED trascritte identiche al DB (244)                 | FAIL
```

`state.db` contiene **364 unità APPROVED con testo italiano** (244 `interfaces.txt`, 68 `help.txt`, 52 `tooltips.txt`); il gate impone che il testo approvato vinca, il mandato impone l'inglese. **Non ho toccato il DB.**

Modifica minima necessaria (da autorizzare): riportare a `PENDING` le unità dei tre file `_ui/`
`UPDATE units SET state='PENDING' WHERE path IN ('data/_ui/interfaces.txt','data/_ui/help.txt','data/_ui/tooltips.txt') AND state='APPROVED';`
Dopo di che i 5 lotti tornano verdi senza altre modifiche.

## 5. Build

| Controllo | Esito |
|---|---|
| `apply_translations --dest src` | 33.037 unità · **28.912 applicate** · 4.123 identiche · 0 errori reali (2 segnalazioni = unità già applicate nella stessa passata, in `_deprecated/`) |
| `verify_integration --dest src` | 28.912 righe cambiate · **FAIL 0 · ESITO OK** |
| `--parse-assets` | **exit 0** — "Parse completed with no error(s)" |
| eseguibile | `af600bd8f1246e3d6e3050a3` · 6.047.003 byte |
| copia `build-cmake` → `build` | **sha identici** (lezione del `cp` fallito per file bloccato: ora `taskkill` prima e confronto dopo) |
| UTF-8 / glifi | invariati: `GLYPHS 224`, `char32_t`, shader `/224.f`, atlanti 6272×32 |

## 6. Non verificato

- **UI a schermo**: la finestra del gioco viene catturata completamente nera; la finestra di Hermes si cattura correttamente, quindi l'ambiente funziona ed è la superficie OpenGL a non essere acquisibile. Avvio tuttavia confermato: processo vivo con 3,3 GB di asset caricati, `errors.txt` con il solo avviso audio, parsing pulito. Prova sostitutiva sui sorgenti: 393/393 stringhe UI in inglese, 0 residui italiani.
- Nessuna sessione di gioco giocata: le news korath/successor sono verificate nei dati e nel parsing, non a video.

## 7. UI esclusa

Nessuna nuova stringa di interfaccia è stata tradotta in questa fase: le 393 già tradotte sono state **riportate indietro**. Il ripristino delle traduzioni italiane della UI resta un'operazione non avviata, da pianificare dopo una build verificata a schermo.
