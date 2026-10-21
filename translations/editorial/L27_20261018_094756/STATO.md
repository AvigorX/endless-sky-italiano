# L27 — stato di avanzamento (CHIUSO 2026-10-18)

`data/kahet/kahet missions.txt`, righe **39–3048**, **917 unità**, **35.520 parole EN → 32.640 IT**,
**49 contesti**, **11 parti**. Deviazione dal target: **−11,2%**, dichiarata (`HANDOFF_L27` §3).

| Esito | Valore |
|---|---|
| `check.py` completo | **`FAIL totale: 0`** (917/917) |
| `verify.py` | **25 controlli, `FAIL: 0`, exit 0** |
| `state.py` | **`ESITO: OK`** |
| `translation.json` sha256[:16] | `37e09b22e11caf89` |
| Approvazione DB | **nessuna** (917 `PENDING`) |

---

## Fatto

| parte | unità | righe | EN | IT | IT/EN | esito |
|---|---|---|---|---|---|---|
| part01 | 1–85 | 39–295 | 2.862 | 2.750 | 0,961 | verde |
| part02 | 86–170 | 296–511 | 3.071 | 2.898 | 0,944 | verde dopo fix virgolette 122/155/159 |
| part03 | 171–255 | 513–958 | 2.735 | 2.533 | 0,926 | verde dopo fix virgolette 172/246 |
| part04 | 256–340 | 960–1167 | 3.035 | 2.720 | 0,896 | verde dopo normalizzazione virgolette |
| part05 | 341–425 | 1169–1427 | 3.680 | 3.335 | 0,906 | FAIL reale 347 (tab in eccesso) → rimosso |
| part06 | 426–510 | 1428–1624 | 3.931 | 3.602 | 0,916 | FAIL reale 509 (rapporto 2,00) → riscritta |
| part07 | 511–595 | 1629–1950 | 3.084 | 2.790 | 0,905 | FAIL reale 528 (rapporto 0,47) → riscritta |
| part08 | 596–680 | 1953–2136 | 3.654 | 3.326 | 0,910 | verde |
| part09 | 681–765 | 2138–2534 | 3.206 | 2.928 | 0,913 | FAIL reale 722 (rapporto 0,47) → riscritta |
| part10 | 766–850 | 2535–2798 | 3.648 | 3.349 | 0,918 | FAIL reale 807 (duplicato di 157) → riscritta |
| part11 | 851–917 | 2799–3048 | 2.614 | 2.409 | 0,921 | FAIL reale 913 (rapporto 0,44) → riscritta |
| **totale** | **917** | **39–3048** | **35.520** | **32.640** | **0,919** | **`FAIL totale: 0`** |

**917 / 917 unità.**

---

## Regole applicate in questo lotto

- **`NT` = 20 unità**, tutte `UI_LABEL`: 4, 103, 197, 199, 201, 204, 206, 209, 211, 214, 216, 219,
  221, 223, 225, 227, 281, 404, 411, 536.
- **`CONVERSATION` (30 unità) = testo visibile** dentro un blocco `conversation` (backtick nel `raw`,
  già rimosso in `english`): tradotto come prosa, **non** in `NT`.
- **`TOKEN_EXC` vuoto**: nessun pronome-token. Famiglie: `<origin>`, `<first>`, `<destination>`,
  `<planet>`, `<system>`, `<payment>`, `<waypoints>`, `<ship>`, `<capacity>`, `<commodity>`, `<cargo>`,
  `<flagship>`, `<bunks>`, `<tons>`.
- **718 unità con tab iniziale su 917**: confronto **per unità** (le `VALUE`, `DESCRIPTION`, `DIALOG`,
  `UI_LABEL` e il primo `MISSION_TEXT` di ogni missione non lo hanno).
- **34 gruppi di duplicati inglesi / 81 unità**: italiano identico ammesso solo dentro un gruppo.
- **1.210 virgolette**: 70 unità con conteggio dispari, riprodotte esattamente.

---

## La voce dei Ka'het (misurata, non assunta)

I Ka'het **non** sono membri della Coalizione: la voce rovesciata di L25/L26 (complemento → soggetto →
verbo in fondo) **non** è stata applicata. Nel sorgente i Remnant (Dusk, Taely, Chilia) parlano in
italiano normale con registro tecnico-scientifico; nel testo il segnale del loro modo di parlare è il
verbo `sign`, reso con **accennare** (o **canta** quando è `chant`).

---

## Glossario del lotto

`Cimitero` · `Distesa di Braci` · `Costruttori` · `Remnant` · `Prisma di Brace` · `cunicolo di
Ossipago` · `Insediamento dei Costruttori` · `camera di equilibrio` · `lumaca` · `Devastatore` ·
`Annichilatrice` · `Dispositivo EMP` · `Ripristinatore di Scudi` · `Accumulatore di Riserva` ·
`Laboratorio di Ricerca` · `Pietra Chiave Quantistica` · `Fucile del Vuoto` · `motore di salto` ·
`iperguida` · `iperspazio`.
Invariati: `Ka'het`, `Ka'sei`, `Fetri'sei`, `Fetri'seia`, `Maeri'het`, `Telis'het`, `Vareti'het`,
`Aberrant`, `Starling`, `Ibis`, `Ssil Vida`, `Patir`, `Lathia`, `Chanai`, `Postverta`, `Aventine`,
`Caelian`, `Viminal`, `Dusk`, `Taely`, `Chilia`.

---

## Limiti dichiarati

- **Unità 188**: il sorgente è troncato (`on anoth.`); l'italiano riproduce il troncamento
  (`su un altr.`). Non è un errore introdotto dalla traduzione.
- **70 unità con virgolette non bilanciate** (sorgente): riprodotte; non normalizzate.
- **Nessuna approvazione nel DB** e **nessun caricamento nel gioco**: verifica strutturale, non visiva.

---

## Prossimo passo

**L28** = `data/kahet/kahet missions.txt`, righe **3051–5297**, **821 unità**, 30.796 parole.
Ripresa: unità **918**, riga **3051**, contesto `mission:Ka'het: Patir Mystery 20`.
L28 chiude il file: il suo `verify.py` **può** asserire la copertura totale 1.738/1.738.
