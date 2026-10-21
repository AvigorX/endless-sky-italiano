# L45 — stato di avanzamento (CHIUSO 2026-10-18)

Lotto `L45_20261018_163313` · `data/successors/successor 2 ghosts.txt` · righe 37–2167 ·
**680/680 unità**. Venticinquesimo file completo dello staging. Tutti i numeri sono misurati, non stimati.

## Fatto

- `source.json`: 680 unità, 36 contesti (`Successors: Ghosts Prelude Wedding` … `Successors: Ghosts
  Reincarnation`), kind 559 `MISSION_TEXT` / 26 `UI_LABEL` / **23 `LOGBOOK`** / 21 `DESCRIPTION` /
  20 `VALUE` / **16 `CONVERSATION`** / 15 `DIALOG`. Nessun `TEXT`.
- `check.py` derivato da L44 con **`NT` = 34** (26 `UI_LABEL` + 8 riferimenti di dato), **`LOGBOOK`
  positivo su 19 testi**, **`CONVERSATION` dedicato su 16 nodi**, controllo **quadre su 11 unità**,
  costruttore dei tab riusato tal quale.
- 14 parti, tutte a fine contesto: 45 · 55 · 50 · 50 · 50 · 50 · 50 · 50 · 50 · 50 · 50 · 50 · 50 · 30.
- `translation.json`: 680 unità, 18.302 EN → 17.736 IT (0,969), rapporto per unità 0,59–1,79,
  sha256[:16] `480ff95bd7e2d97b`.
- `verify.py`: **39 controlli**, `FAIL: 0`, exit 0. Copertura **680/680**, coppia di righe **(37, 2167)**,
  `NT` 34 elencati uno per uno, `CONVERSATION` 16 con il solo 137 identico per necessità, 19 righe `log`
  di testo + 4 categorie identificate, insieme delle 15 virgolette dispari, 11 unità con quadre.
- `review.md`, `REPORT.md`, questo `STATO.md`.

## Regole applicate

- **26 `UI_LABEL`, indici rimisurati** (12, 51, 56, 99, 186, 206, 208, 218, 221, 349, 434, 473, 533,
  536, 574, 578, 616, 627, 632, 636, 639, 641, 643, 654, 656, 658).
- **`NT` non è solo `UI_LABEL`**: 8 riferimenti di dato restano identici — 4 categorie di diario
  (`People` ×3, `Factions`) e 4 nomi di governo (`House Kaatrij` ×3, `High Houses (Unknown)`).
- **`LOGBOOK` 23 = 19 testi + 4 categorie**. Le 4 categorie sono `log "Categoria" "Nome" "testo"` con il
  testo fra **virgolette** invece che fra backtick: `tools/l10n.py` estrae come unità la sola categoria.
  Lacuna di inventario del tool protetto, **documentata** in `review.md` §2, non riparata.
- **`CONVERSATION` 16** (135–138, 256–267): prima volta nella serie. Nodi con il testo fra backtick,
  tab interni conservati; il solo nodo **137** `(No.)` → `(No.)` resta identico per necessità
  (`CONV_SAME`), dichiarato nel `check.py`.
- **Tab 526**: nessuna traduzione scritta con `\t`; il costruttore li aggiunge e la parità è verificata
  per unità (526 unità su 680 iniziano con tab).
- **15 virgolette dispari** (15, 95, 159, 163, 479, 524, 525, 611, 612, 651, 652, 657, 666, 667, 669):
  battute aperte nel sorgente, riprodotte aperte; confronto come insieme di idx.
- **Quadre**: 11 unità con i marcatori `[...]` dei frammenti redatti. Il controllo è **per unità**
  (conteggio di `[` e `]` invariato), non un'asserzione di assenza come in L44. Due unità (657, 669)
  avevano **una quadra in più** in prima stesura: corrette sul numero misurato, non a occhio.
- **Lessico nuovo registrato**: Casate (Chydiyi, Myurej, Seineq, Kaatrij, Sioeora, Aqrabe), Saajret,
  Sijra, Rijatet, Kampa, Resja, Tiliia, Khiajsore, Riijaaora · `mantello` (*cloak*, tecnologia di
  occultamento) e `occultato/occultarsi` · `il Tangled Shroud` invariato (28 occorrenze nel corpus) ·
  `Nastri di Iret` · `cunicolo` (*wormhole*) · `nave da guerra di famiglia` (*heirloom warship*) ·
  `chiavi di volta` (*keystones*) · `Casate Alte` (*High Houses*) · `Cavaliere-Vassallo` ·
  `metallo stellare` (*stellar metal*).

## Verifica

```
python staging/editorial/L45_20261018_163313/check.py    → FAIL totale: 0 (25 controlli)
python staging/editorial/L45_20261018_163313/verify.py   → exit 0, 39 controlli, FAIL: 0
```

## Non fatto (dichiarato)

- **Nessuna approvazione nel database**: le 680 unità sono `PENDING`.
- **Nessun caricamento nel gioco**: la traduzione non è mai stata letta da Endless Sky né vista a
  schermo. In particolare non è verificato il percorso Ghosts (36 contesti, molti `goto`), né la resa dei
  16 nodi di conversazione, né che la licenza Kaatrij e il brevetto di Cavaliere-Vassallo compaiano con i
  nomi tradotti.
- **Nessun test di gameplay** della linea Successors.
