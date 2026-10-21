# STATO — L282 (`data/wanderer/wanderer missions.txt`, righe 16–41)

**Stato: CHIUSO.** Primo lotto del file: la missione **«Mereti: The Plant 1»**, con **9 alternative fra parentesi quadre**. Il
file è aperto a **13/54 (24,1%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L282_20261020_181705/` |
| file | `data/wanderer/wanderer missions.txt` (54 unità · 1.727 parole · righe 16–182 · 1 `UI_LABEL`) |
| righe | 16–41 |
| unità | **13** — 11 `MISSION_TEXT` + 1 `DESCRIPTION` + 1 `VALUE` |
| parole | **449 EN → 420 IT** (0,94) |
| rapporto | **0,74 – 1,24** |
| contesti | **1** — `mission:Wanderers: Mereti: The Plant 1` |
| tab | **9** (unità 4–12) |
| virgolette | **16**, per unità |
| **alternative `[...]`** | **9**, ognuna con **2 opzioni** |
| segnaposto | **4** — `<planet>` 3 · `<destination>` 1 |
| apici | **4 EN** / **5 IT** |
| `check.py` | **24 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **22 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 0 prima (il lotto **apre** il file) · 13 qui · **41 dopo** la 41 |
| `sha256[:16]` | **`0e77aed1e368033c`** |

## Comandi

```bash
python staging/editorial/L282_20261020_181705/check.py     # FAIL totale: 0 (24 controlli)
python staging/editorial/L282_20261020_181705/verify.py    # FAIL: 0 (22 controlli, 13/54)
```

## Le nove alternative: la parte delicata

Il testo contiene **scelte a runtime** fra parentesi quadre — il gioco ne sceglie una a ogni esecuzione. Tradurle come prosa
avrebbe rotto la logica; copiarle avrebbe lasciato inglese nel testo. La resa **conserva la struttura** e traduce le opzioni:

| inglese | resa |
|---|---|
| `[defend, protect]` | **`[difenderci, proteggerci]`** |
| `[parents? ancestors?]` | **`[genitori? antenati?]`** (separatore `?`, come il sorgente) |
| `[teachers, mentors]` | **`[insegnanti, mentori]`** |
| `[native, local]` | **`[nativa, originaria]`** |
| `[grow, tend]` | **`[coltiviamo, curiamo]`** |
| `[differences, complications]` | **`[differenze, complicazioni]`** |
| `[best, most likely]` | **`[migliore, più probabile]`** |
| `[approach, solution]` | **`[piano, approccio]`** |
| `[house, cultivate]` | **`[ospitare, coltivare]`** |

Il `check.py` verifica **tre cose per ogni alternativa**: il numero (9 in entrambe le lingue), la **posizione** (unità 5, 8, 11),
e il **numero di opzioni** — due ciascuna, comprese quelle separate da `?` invece che da virgola.

## La scena

I Mereti hanno **ampliato le serre**; una pianta dai **petali blu intenso** e dalle **foglie verde acqua** non cresce. Un drone,
«molto più piano dell'ultima volta», chiede aiuto ricordando al giocatore ciò che ha fatto per loro. Due Wanderer propongono di
portarla su `<planet>`: «Ci saranno differenze, ma è il migliore approccio nel breve periodo», però «vogliamo comunque lasciare
questi mondi agli **Slegati**».

## Limiti dichiarati

Nessuna approvazione (13 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Restano **41 unità**.
