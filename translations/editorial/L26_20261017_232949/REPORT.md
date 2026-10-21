# REPORT — L26

**Lotto:** L26 (ultimo segmento di `coalition missions.txt`)
**File:** `data/coalition/coalition missions.txt`
**Intervallo:** righe **2913–3868** (unità 1–406 del lotto; unità 1175–1580 del file)
**Data di chiusura:** 2026-10-17
**Stato:** CHIUSO — `check.py` `FAIL totale: 0`, `verify.py` exit 0

## 1. Consegna

| voce | valore misurato |
|---|---|
| unità tradotte | **406** |
| di cui non traducibili (`UI_LABEL`) | **27** |
| di cui traducibili | **379** |
| parole inglesi | **10.765** |
| parole italiane | **10.151** |
| rapporto complessivo IT/EN | **0,943** |
| contesti distinti | **19** |
| parti | **5** (`part01.json` … `part05.json`) |
| riga iniziale / finale del lotto | **2913 / 3868** |
| unità del file prima / dopo il lotto | **1.174 / 0** |

Deviazione dal target di ~40.000 parole: **−73%**, dichiarata e voluta. Il lotto chiude il file:
`coalition missions.txt` passa a **1.580/1.580** unità, contando due lotti (L25 1.174 + L26 406).

## 2. Composizione per tipo

| tipo | unità |
|---|---|
| `MISSION_TEXT` | 321 |
| `UI_LABEL` (NT) | 27 |
| `CONVERSATION` (testo, tradotto) | 23 |
| `VALUE` | 13 |
| `DESCRIPTION` | 13 |
| `LOGBOOK` | 6 |
| `DIALOG` | 3 |

## 3. Misure di conformità (esecuzione completa, non per intervallo)

```
FAIL totale .............. 0
tab .................... 308 / 308
virgolette ............. 593 / 593
token <...> .............. 69 / 69
backtick .................. 0 / 0
traduzioni vuote ......... 0
duplicati non spiegati ... 0
caratteri non latini ..... nessuno
trattini lunghi/en-dash .. nessuno
rapporto lunghezze ....... 0,69 – 1,86
```

## 4. Duplicati e virgolette

- **7 gruppi** di inglese identico, **15 unità**: risposte alternative con lo stesso esito, `(Say nothing.)`,
  `Visit Anna` in due missioni, `(Accompagna Anna…)`.
- **9 unità con virgolette dispari** nel sorgente, riprodotte esattamente: 116, 118, 172, 186, 346, 401
  con 3 virgolette; 252, 309, 311 con 1.
- Il caso **309 / 313** (stesso testo, 1 vs 2 virgolette) è la prova che la virgoletta del sorgente è
  informazione, non rumore: normalizzarla produce due FAIL insieme.

## 5. Verifica indipendente

`verify.py` (**28 controlli**, exit **0**) rilegge file sorgente, `state.db` e parti su disco senza
riusare la logica di `check.py`:

- riga grezza identica al file;
- `english`/`kind`/`path` identici al database, stato `PENDING`, **nessuna** `APPROVED`;
- id univoci, ordine uguale al sorgente, stesse unità nei due JSON;
- collocazione: 406 unità, righe 2913–3868, **1.174** unità prima, **0** dopo, ultima riga del file 3868;
- **copertura del file 1.580/1.580** da **due** lotti, con zero unità sovrapposte;
- 27 NT identiche al sorgente; **23 `CONVERSATION` tradotte** e **nessuna** in `NT`;
- parità esatta dei token; tab, virgolette, backtick uguali al sorgente;
- italiano mai vuoto, nessun carattere non latino, nessun trattino lungo;
- rapporto definito per tutte le unità;
- le 5 parti ricostruiscono `translation.json`.

**sha256[:16] di `translation.json`:** `889ca7d8935e9ac0`

## 6. Stato del progetto dopo L26

| voce | valore |
|---|---|
| unità in staging | **11.009** (30 directory con `translation.json`) |
| parole EN → IT in staging | **341.491 → 326.075** |
| unità `PENDING` nel DB | **32.560** |
| unità `APPROVED` nel DB | **364** (nessuna di questo lotto) |
| unità non traducibili nel DB | **630** |
| residuo traducibile | **20.921** |
| file completi in staging | **sette** (`map planets`, `human missions`, `intro missions`, `jobs`, `deep missions`, `remnant 1 introduction`, `coalition missions`) |

## 7. Che cosa questo report non dimostra

- **Non** dimostra che la traduzione sia corretta: dimostra che è completa, coerente e conforme ai
  controlli definiti.
- **Non** c'è rendering nel gioco: nessuna stringa è stata vista a schermo.
- **Non** c'è approvazione nel database: lo staging non è approvazione.
- **Non** c'è revisione umana terza.

## 8. Prossimo passo

L27: `data/kahet/kahet missions.txt`, righe **39–3048** — **917 unità / 35.520 parole / 49 contesti**
(−11,2% sul target), confine misurato con `next_section.py`: dopo la riga 3048 resta il contesto
`Ka'het: Patir Mystery 20`, che apre il segmento successivo (821 unità / 30.796 parole).
