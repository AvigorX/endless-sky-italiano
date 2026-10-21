# REPORT.md — L24 · `data/remnant/remnant 1 introduction.txt`

**Data di chiusura:** 2026-10-17 · **Esito:** `check.py` `FAIL totale: 0` · `verify.py` exit 0
**File:** `data/remnant/remnant 1 introduction.txt`, righe **23–3923** (file completo, 3.901 righe)
**Unità:** **1.250 / 1.250** (43 non traducibili dichiarate in `NT`)

## 1. Volume

| voce | valore |
|---|---:|
| unità del lotto | 1.250 |
| unità traducibili | 1.207 |
| parole inglesi | 41.087 |
| parole italiane | 38.140 |
| rapporto complessivo IT/EN | 0,928 |
| rapporto per unità (min–max) | 0,57 – 1,86 |
| contesti di missione | 68 |
| parti | 14 (`part01`…`part14`, 90 unità ciascuna tranne l'ultima da 80) |
| tabulazioni (IT/EN) | 931 / 931 |
| virgolette (IT/EN) | 2.111 / 2.111 |
| token `<…>` (IT/EN) | 255 / 255 |
| backtick | 0 / 0 |
| duplicati inglesi nel sorgente | 78 gruppi / 195 unità |
| unità con virgolette dispari nel sorgente | 41 (riprodotte, non normalizzate) |

## 2. Esito dei controlli

`check.py` (lotto completo, 22 righe di controllo): **`FAIL totale: 0`**.
Copertura 1250/1250, nessuna traduzione vuota, `NT` identiche, nessun duplicato italiano non
spiegato dal sorgente, tab/virgolette/backtick in parità per unità, token in parità, spazi ai bordi
come il sorgente, rapporto entro 0,55–1,90, tipografia pulita (nessun accento sostitutivo, nessun
trattino lungo, nessun apostrofo curvo), nessun carattere non latino, nessuna parola inglese residua,
database a `APPROVED 364 · PENDING 32560` con tutte le unità del lotto `PENDING` e nessuna `APPROVED`.

`verify.py` (indipendente da `check.py`, **24 controlli**): **exit 0**. Verifica in particolare: riga
grezza identica al file su tutte le 1.250 unità; `english`/`kind`/`path` identici al database;
file completo (23–3923, zero unità prima e dopo); copertura dello staging 1250/1250 da **un solo**
lotto (nessuna sovrapposizione); `NT` identiche; token in parità esatta; assenza di trattini lunghi;
ricostruzione di `translation.json` dalle 14 parti su disco.

`translation.json` sha256[:16] **92e4737d1b55d9dc** — hash **dopo l'ultima esecuzione di
`check.py`**; le parti sono la fonte, l'hash si muove se si rilancia `check.py`.

## 3. Integrità

| elemento | stato |
|---|---|
| repository `endless-sky` | HEAD `b4aa3bac3`, `git status` pulito, nessuna scrittura |
| `state.db` | hash `9125282973ddc8b9` invariato, sola lettura |
| `glossary.csv`, `inventory_fields.csv`, `tools/l10n.py` | hash invariati (`ESITO: OK`) |
| `output/l10n-it/**` (3 file UI) | hash invariati |
| patch K4 o altre patch | nessuna applicata |
| build, test di gioco, packaging | non eseguiti |
| rendering nel gioco | **non verificato**: il workflow non esegue il gioco |

## 4. Bilancio del lotto

- **Target editoriale** ~40.000 parole sorgente per lotto. Il file vale **41.087 parole**: è stato
  preso **intero**, deviazione **+2,7%**, dichiarata qui e non compensata con altri file. È la scelta
  che evita un taglio arbitrario dentro una sequenza di missioni (kahet vale 66.316 parole, coalition
  48.224: entrambi avrebbero richiesto un confine inventato).
- Il lotto è stato completato in **due sessioni**: parti 01–03 (unità 1–270) prima, parti 04–14
  (unità 271–1.250) in questa sessione, con `check.py --range` verde dopo **ogni** parte e
  `check.py` completo rieseguito a ogni parte per intercettare i duplicati fra parti.
- **Dodici difetti corretti** durante il lotto (elenco completo in `review.md` §5): un tab perduto
  (489), tre conteggi di virgolette non allineati al sorgente (618, 911), sei collisioni di duplicato
  italiano con inglese diverso (108, 655, 883, 1132, 1240), una parola inglese residua da apostrofo
  troncato (`Be'` → `Beh`, unità 657) e due riscritture per rapporto di lunghezza.
- **Un limite del sorgente documentato, non aggirato**: `<compared>` (unità 373) è una sostituzione
  definita nei dati del gioco, con varianti in inglese fuori dal nostro controllo.
- Staging complessivo dopo la chiusura: **9.429 unità · 293.267 EN → 280.073 IT**; residuo
  traducibile **22.501 unità**. Con L24 sono **28** i lotti con `translation.json` in staging
  (la 29ª cartella `L19_20261017_201342/` è l'export scartato documentato in `NOTE.md`).

## 5. Cosa resta non verificato

Il rendering delle accentate dipende dall'atlante bitmap del font e non è stato osservato; nessuna
unità è stata approvata nel database (lo staging non è approvazione); non esiste ancora una
revisione umana terza. Questi tre punti valgono per l'intera campagna, non solo per L24.

## 6. Prossimo passo

Nuovo lotto **L25** su `data/coalition/coalition missions.txt`, misurato con `next_section.py`:
righe **16–2907**, **1.174 unità**, **37.459 parole**, **65 contesti** (da `First Contact` a
`Expeditions Past 10`), deviazione **−6,4%** sul target. Il confine cade fra due contesti, dopo
`Long Lost Property 1` — nessun taglio dentro un testo. Il resto del file (406 unità) resta per un
lotto successivo. Dettagli e punto di ripresa in `HANDOFF_L25_20261017.md` e in
`CHECKPOINT_EDITORIALE.md` §8.
