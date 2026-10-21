# REPORT.md — L23 · `data/human/deep missions.txt`

**Data di chiusura:** 2026-10-17 · **Esito:** `check.py` `FAIL totale: 0` · `verify.py` exit 0
**File:** `data/human/deep missions.txt`, righe **16–4293** (file completo, 4.278 righe)
**Unità:** **1.355 / 1.355** (30 non traducibili dichiarate in `NT`)

## 1. Volume

| voce | valore |
|---|---:|
| unità del lotto | 1.355 |
| unità traducibili | 1.325 |
| parole inglesi | 38.724 |
| parole italiane | 36.319 |
| rapporto complessivo IT/EN | 0,938 |
| rapporto per unità (min–max) | 0,58 – 1,65 |
| contesti di missione | 83 |
| parti | 15 (`part01`…`part15`, 90 unità ciascuna tranne l'ultima da 95) |
| tabulazioni (IT/EN) | 1.064 / 1.064 |
| virgolette (IT/EN) | 1.816 / 1.816 |
| token `<…>` (IT/EN) | 280 / 280 |
| backtick | 0 / 0 |
| duplicati inglesi nel sorgente | 58 gruppi / 127 unità |

## 2. Esito dei controlli

`check.py` (lotto completo, 22 righe di controllo): **`FAIL totale: 0`**.
Copertura dell'intervallo e del lotto verdi, nessuna traduzione vuota, `NT` identiche, nessun
duplicato italiano non spiegato dal sorgente, tab/virgolette/backtick in parità per unità, token in
parità, spazi ai bordi come il sorgente, rapporto entro 0,55–1,90, tipografia pulita (nessun accento
sostitutivo, nessun trattino lungo, nessun apostrofo curvo), nessun carattere non latino, nessuna
parola inglese residua, database a `APPROVED 364 · PENDING 32560` con tutte le unità del lotto
`PENDING` e nessuna `APPROVED`.

`verify.py` (indipendente da `check.py`, 22 controlli): **exit 0**. Verifica in particolare: riga
grezza identica al file su tutte le 1.355 unità; `english`/`kind`/`path` identici al database;
file completo (16–4293, zero unità prima e dopo); copertura dello staging 1355/1355 da **un solo**
lotto (nessuna sovrapposizione); `NT` identiche; token in parità esatta; ricostruzione di
`translation.json` dalle 15 parti su disco.

`translation.json` sha256[:16] **f745dd523ff32319** — hash **dopo l'ultima esecuzione di
`check.py`**; le parti sono la fonte, l'hash si muove se si rilancia `check.py`.

## 3. Integrità

| elemento | stato |
|---|---|
| repository `endless-sky` | HEAD `b4aa3bac3`, `git status` pulito, nessuna scrittura |
| `state.db` | hash `9125282973ddc8b9` invariato, sola lettura |
| `glossary.csv`, `inventory_fields.csv`, `tools/l10n.py` | hash invariati (`ESITO: OK`) |
| `output/l10n-it/**` (3 file UI) | hash invariati |
| patch K4 o altre patch | nessuna applicata |
| build, test di gioco, packaging | non eseguiti (divieto §9) |
| rendering nel gioco | **non verificato**: il workflow non esegue il gioco |

## 4. Bilancio del lotto

- **Target editoriale** ~40.000 parole sorgente per lotto. Il file vale **38.724 parole**: è stato
  preso **intero**, deviazione **−3,2%**, dichiarata qui e non compensata con altri file.
- Il lotto è stato completato in **due sessioni**: parti 01–08 (unità 1–720) prima, parti 09–15
  (unità 721–1355) in questa sessione, con `check.py --range` verde dopo **ogni** parte.
- Tre difetti del sorgente riprodotti o normalizzati e annotati (`776`, `1023`, `1151`); nessuna
  correzione al repository del gioco, che resta intatto.
- Staging complessivo dopo la chiusura: **8.179 unità · 252.180 EN → 241.933 IT**; residuo
  traducibile **23.751 unità**. Con L23 sono **cinque** i file completi in staging:
  `data/map planets.txt`, `data/human/human missions.txt`, `data/human/intro missions.txt`,
  `data/human/jobs.txt`, `data/human/deep missions.txt`.

## 5. Cosa resta non verificato

Il rendering delle accentate dipende dall'atlante bitmap del font e non è stato osservato; nessuna
unità è stata approvata nel database (lo staging non è approvazione); non esiste ancora una
revisione umana terza. Questi tre punti valgono per l'intera campagna, non solo per L23.

## 6. Prossimo passo

Nuovo lotto **L24** su `data/kahet/kahet missions.txt` (1.714 unità, 66.258 parole), da tagliare a un
confine reale di missione perché supera il target di ~40.000 parole: segmento proposto con
`next_section.py`, deviazione dichiarata. Alternativa più vicina al target:
`data/coalition/coalition missions.txt` (1.537 unità, 48.124 parole).
Misurare con `next_section.py` e `export_section.py`, non scegliere a naso. Dettagli e punto di
ripresa in `HANDOFF_L24_20261017.md` e in `CHECKPOINT_EDITORIALE.md` §8.
