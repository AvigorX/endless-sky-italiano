> **SUPERATO il 2026-10-19** da `RIPRESA_L197_20261019.md` (punto d'ingresso a freddo, verificato `FAIL: 0 / 22`)
> e da `HANDOFF_L197_20261019.md` (contratto del prossimo lotto, `FAIL: 0 / 22`).
>
> Questo file fotografa il workspace **prima** di L196 e **non va rigenerato a mano**: i suoi numeri
> (28429 unità · 895008 EN · 851938 IT · 199 directory · residuo 3501 · L196 «da aprire») sono quelli del
> 19 ottobre **prima** dell'apertura del lotto. Dopo la chiusura di L196 `check_handoff.py` su questo file
> restituisce **4 FAIL su 21, per costruzione**, non per errore.
>
> Corretto durante L196: la riga `Token` del §3 diceva **0**; misurati **72 segnaposto** su 32 unità.

# AGENTE_PROSSIMA_SESSIONE_20261019.md — checkpoint a freddo per l'agente

**Cos'è.** Il documento unico da consegnare a un agente che apre la campagna da zero: stato misurato, prossimo lotto,
comandi esatti, trappole note, regole e roadmap. **Non è un riassunto**: si verifica da solo e contiene i numeri con cui
si controlla.

```bash
cd ~/PROGETTI/G-DEV/GAME-SOURCE-LAB/endless-sky-l10n
python staging/editorial/tools/check_handoff.py AGENTE_PROSSIMA_SESSIONE_20261019.md   # atteso: FAIL: 0 / 21
```

**Generato** il 2026-10-19 dopo la chiusura di **L195** (e del file `bunrodea missions.txt`). **Sostituisce**
`RIPRESA_L196_20261019.md` come punto d'ingresso per una sessione nuova.

---

## 1. Stato misurato del workspace

```
  data/human/human missions.txt               4253/ 4253 unità (100.0%) · 104495 EN ->  98511 IT · 6 lotti
  data/map planets.txt                        1544/ 1544 unità (100.0%) ·  83687 EN ->  83453 IT · 18 lotti
  TOTALE staging: 28429 unità · 895008 EN · 851938 IT
```

- **199 directory** con `translation.json` (200 cartelle `L*`; `L19_20261017_201342/` è un export scartato senza
  `translation.json` e non conta); **197** hanno `verify.py`, tutte verdi;
- database: **APPROVED 364 · PENDING 32560** · totale 32924, ultimo evento `2026-10-17T14:33:18Z`;
- unità `PENDING` di tipo `UI_LABEL` (label, non traducibili): 630;
- residuo traducibile: 3501 (formula di `state.py`);
- unità realmente traducibili ancora da fare: **4.170 su 108 file** · parole inglesi: **82.096**;
- `human missions.txt` completo in staging: **2141 unità / 51158 parole** dopo la riga 6428;
- **file completi in staging: 57** su 167 percorsi;
- avanzamento: **28429/32924 unità (86,3%)** · **895008/979975 parole (91,3%)**;
- `endless-sky` HEAD **b4aa3bac3**, `git status --porcelain` vuoto.

### File protetti (non si toccano)

| file protetto | sha256[:16] atteso |
|---|---|
| `state.db` | `9125282973ddc8b9` |
| `glossary.csv` | `94e785f68be271d8` |
| `staging/inventory_fields.csv` | `c9d8bc651cd70c56` |
| `tools/l10n.py` | `743c6a3f8c217f35` |

### File chiusi in questa campagna

`human missions.txt` · `map planets.txt` · `coalition jobs.txt` 197/197 · `weapons.txt` 90/90 · `avgi outfits.txt` 63/63
· `paradise world jobs.txt` 131/131 · `avgi ships.txt` 102/102 · `human outfits.txt` 63/63 · `gegno outfits.txt` 60/60 ·
**`bunrodea missions.txt` 77/77**.

## 2. Ultimi lotti chiusi (L190–L195)

| lotto | file | righe | unità | EN → IT | check / verify | sha256[:16] |
|---|---|---|---|---|---|---|
| L190 | `gegno outfits.txt` | 1137 | 1 | 23 → 22 | 16 / 18 | `13766cd38ed4be40` |
| L191 | `bunrodea missions.txt` | 16–52 | 12 | 466 → 434 | 25 / 21 | `a1c782a568e872ed` |
| L192 | `bunrodea missions.txt` | 64–91 | 12 | 465 → 418 | 24 / 21 | `6a45d9d51cb156e7` |
| L193 | `bunrodea missions.txt` | 92–150 | 30 | 500 → 463 | 23 / 21 | `0ba103f679e3b8cc` |
| L194 | `bunrodea missions.txt` | 152–203 | 18 | 488 → 479 | 21 / 21 | `5b5071523577ff54` |
| L195 | `bunrodea missions.txt` | 207–219 | 5 | 397 → 361 | 20 / 17 | `a75a3d4708ee72a5` |

## 3. Prossimo lotto — L196 (apre `hai jobs.txt`)

```bash
python staging/editorial/tools/export_section.py "staging/editorial/L196_$(date +%Y%m%d)_$(date +%H%M%S)" \
  "data/hai/hai jobs.txt" 15 489
```

| voce | valore |
|---|---|
| File | `data/hai/hai jobs.txt` (175 unità · 2.302 parole · 71 `VALUE` + 75 `DESCRIPTION` + 6 `TEXT` + 23 `DIALOG`) |
| Righe | 15–489 |
| Unità | **39** |
| Parole | **499** |
| Contesti | **20** — da `Human Vacation [1]` a `Delivery to Human Space [2]` |
| Tab / virgolette | **0** / **6** |
| Tipi | **17 `VALUE`** · **16 `DESCRIPTION`** · **6 `TEXT`** |
| Token | **72 segnaposto** su 32 unità — 19 `<planet>` · 18 `<payment>` · 11 `<destination>` · 9 `<bunks>` · 6 `<tons>` · 5 `<date>` · 2 `<cargo>` · 1 `<passengers>` · 1 `<origin>` |
| Confine dopo | riga **492** apre `mission:Delivery to Human Space [2]` — una `DESCRIPTION` |

Il file `hai jobs.txt` si chiude in **5 finestre**, già calcolate sul database (non a memoria):

| lotto | righe | unità | parole |
|---|---|---|---|
| L196 | 15–489 | 39 | 499 |
| L197 | 492–967 | 36 | 488 |
| L198 | 988–1565 | 51 | 472 |
| L199 | 1579–1750 | 26 | 489 |
| L200 | 1753–2067 | 23 | 354 |

## 4. Metodo (sette passi, invariato)

1. **Preflight**: `python staging/editorial/tools/state.py` → deve dire `ESITO: OK` e `INTEGRITA'` pulita.
2. **Export**: `export_section.py <directory> <percorso> <riga_da> <riga_a>` — **la directory viene prima del percorso**.
3. **Lettura e conteggio**: `Counter(kind)`, contesti, tab, virgolette, apici, token, `min/max(line)`; **ogni numero va
   misurato sul `source.json` o sul database**, mai dedotto.
4. **Traduzione** in `parts/part01.json`; `VALUE`/`TEXT` copiati alla lettera; tab iniziali conservati.
5. **`check.py`**: asserzioni sul lotto (tipi, tab, virgolette, apici con la **causa**, nomi invariati, registro, gate
   0,55–1,90, `PENDING`). Le asserzioni «vuote» (0 token, 0 tab) si scrivono comunque.
6. **`verify.py`**: riga grezza identica al sorgente, identità col DB, unità prima/dopo, **confine misurato**, e — quando il
   lotto chiude il file — l'**invariante di FILE** (somma delle finestre = unità del file, righe distinte).
7. **Documenti**: `STATO.md`, `REPORT.md`, `review.md` generati dai numeri misurati; poi il contratto del lotto successivo
   (`HANDOFF_L<n+1>`), i due checkpoint, la `RIPRESA_L<n+1>`, la batteria e `git status`.

**Scrittura degli script**: si scrivono nello scratch, si copiano nella cartella del lotto con `cp`, si verifica con
`ls -la` e poi si eseguono (trappola 46: `write_file` può rispondere «ok» senza creare il file).

### Comandi di verifica, con esito atteso

```bash
python staging/editorial/L<n>_<data>/check.py    # "FAIL totale: 0", exit 0
python staging/editorial/L<n>_<data>/verify.py   # "FAIL: 0", exit 0
python staging/editorial/tools/state.py          # "ESITO: OK", 8/8 INTEGRITA' OK
python staging/editorial/tools/check_handoff.py HANDOFF_L<n+1>_<data>.md   # "FAIL: 0 / 21", exit 0
for f in staging/editorial/L*/verify.py; do python "$f" >/dev/null || echo "ROSSO $f"; done   # batteria
git -C ../endless-sky status --porcelain         # 0 righe
```

## 5. Trappole note (verificate, non ipotesi)

| n. | trappola | come si evita |
|---|---|---|
| 44 | la sezione «prossimo lotto» di `CHECKPOINT_SESSIONE` deve essere `## 4.`, e i marcatori di `span()` sono di **sezione**, non di titolo | `grep -n "^## "` dopo ogni patch |
| 45 | nelle tabelle «prossimo lotto» la cella **`File` è obbligatoria**; il formato contesti è `**N** — da \`X\` a \`Y\`` | scrivere sempre `File` e i due contesti |
| 46 | `write_file` può rispondere «ok» senza creare il file | scratch → `cp` → `ls -la` |
| 47 | **la cella `Contesti` non vuole il prefisso `mission:`** (il checker confronta il contesto **nudo**), e ogni backtick in più sposta il parsing dell'ultimo contesto | esattamente 4 backtick, nessun altro nella cella |
| 48 | nel «Confine dopo» invece il **contesto grezzo** serve intero (`mission:X`), e per il lotto terminale la formula è `**fine file**` | copiare dal DB, non dal titolo |
| 49 | `next_section.py` può dare **falsi negativi** («il file finisce prima di raggiungere N parole» con migliaia di parole residue) | calcolare la finestra sul database e verificarla con una query |
| 50 | il generatore dei `verify.py` deve usare `chr(9)` per i tab: `'\t'` dentro un template raw diventa `'\\t'` | usare `chr(9)` e `chr(39)` |
| 51 | le asserzioni su `a in b == c` in Python non significano quel che sembrano (catena di confronti) | parentesi esplicite |
| 52 | gli apici **non** hanno lo stesso numero fra inglese e italiano: i possessivi inglesi diventano «di + articolo» | legare ogni apice alla sua causa e misurare i due conteggi |

## 6. Regole non negoziabili

- **Nessuna approvazione**: le unità restano `PENDING`. Scrivere nel `state.db` non è compito del lotto.
- **Nessuna riscrittura totale**: diff piccoli; un file generato non si aggiusta a mano, si rigenera dai dati.
- **Nessun numero inventato**: ogni cifra nei documenti viene da `state.py`, dal database o dall'output di uno script.
- **Nessun file protetto toccato** (tabella al §1), **nessun commit** nel repository `endless-sky`.
- **Fedeltà al sorgente**: le incoerenze del gioco (per esempio `Astuit Battery` nel contesto e `Astuit Blasters` nel
  testo) si conservano e si verificano, non si correggono.
- **Se un controllo fallisce, l'errore è nella traduzione o nell'asserzione**: si guarda il dato prima di «semplificare»
  il controllo.

## 7. Roadmap del residuo

**Scala misurata**: 4.170 unità / 82.096 parole su 108 file; a ~460 parole per lotto sono **circa 178 lotti**.

I primi file del ranking residuo (criterio: primo file **senza unità che siano solo punteggiatura**):

| file | unità | parole | note |
|---|---|---|---|
| `data/hai/hai jobs.txt` | 175 | 2302 | **in corso**, L196–L200 |
| `data/hai/hai outfits.txt` | 65 | 2289 | 56 `DESCRIPTION` + 9 `VALUE` |
| `data/successors/successor ships.txt` | 146 | 2288 | 100 `TEXT` (nomi da copiare) |
| `data/remnant/remnant outfits.txt` | 57 | 2217 | 55 `DESCRIPTION` |
| `data/korath/korath outfits.txt` | 92 | 2204 | 63 `DESCRIPTION` + 29 `VALUE` |
| `data/korath/korath ships.txt` | 50 | 2049 | |
| `data/gegno/gegno ships.txt` | 37 | 2036 | |
| `data/human/syndicate jobs.txt` | 94 | 1927 | |
| `data/human/post-war reactions.txt` | 87 | 1925 | 87 `MISSION_TEXT` |
| `data/human/engines.txt` | 61 | 1882 | |

**Esclusi dal percorso finché non si decide come trattarli** (contengono unità che sono **solo punteggiatura**, da
verificare una per una prima di tradurle): `data/coalition/coalition news.txt` (2 sospette), `data/human/deep jobs.txt`
(3 sospette), `data/avgi/avgi news.txt` (2 sospette).

## 8. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 28.429 unità in staging, tutte `PENDING` nel database.
- **Nessun caricamento nel gioco** e **nessun test di gameplay**: la verifica è testuale, a exit code.
- **Nessuna revisione umana** e **nessun testo visto dentro Endless Sky**.
- **Il residuo non è finito**: 4.170 unità su 108 file restano da tradurre; questo documento dice da dove ripartire, non
  che la campagna sia completa.
