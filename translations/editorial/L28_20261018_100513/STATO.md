# L28 — stato di avanzamento (CHIUSO 2026-10-18)

`data/kahet/kahet missions.txt`, righe **3051–5297** (fine file), **821 unità**,
**30.796 parole EN → 27.914 IT**, **47 contesti**, **10 parti**.

| Esito | Valore |
|---|---|
| `check.py` completo | **`FAIL totale: 0`** (821/821) |
| `verify.py` | **24 controlli, `FAIL: 0`, exit 0** |
| `state.py` | **`ESITO: OK`** |
| `translation.json` sha256[:16] | `ba932b11d8e35fb8` |
| Copertura del file | **1.738 / 1.738 (100%)** con L27 |
| Approvazione DB | **nessuna** (821 `PENDING`) |

---

## Fatto

| parte | unità | righe | EN | IT | IT/EN | esito |
|---|---|---|---|---|---|---|
| part01 | 1–85 | 3051–3300 | 3.229 | 2.894 | 0,896 | verde |
| part02 | 86–170 | 3301–3503 | 3.858 | 3.435 | 0,890 | verde |
| part03 | 171–255 | 3504–3730 | 3.970 | 3.530 | 0,889 | verde dopo fix 176/177 (inglese e refuso) |
| part04 | 256–340 | 3731–3954 | 3.246 | 2.937 | 0,905 | verde |
| part05 | 341–425 | 3960–4169 | 3.155 | 2.870 | 0,910 | verde |
| part06 | 426–510 | 4170–4371 | 2.740 | 2.484 | 0,907 | FAIL reale 456 (registro) e 484 (refuso) → riscritte |
| part07 | 511–595 | 4372–4678 | 2.514 | 2.315 | 0,921 | FAIL reale 546 (rapporto 0,44) → riscritta |
| part08 | 596–680 | 4679–4863 | 3.163 | 2.867 | 0,906 | verde |
| part09 | 681–765 | 4864–5117 | 2.898 | 2.685 | 0,927 | verde |
| part10 | 766–821 | 5118–5297 | 2.023 | 1.897 | 0,938 | verde |
| **totale** | **821** | **3051–5297** | **30.796** | **27.914** | **0,906** | **`FAIL totale: 0`** |

**821 / 821 unità.**

---

## Regole applicate

- **`NT` = 4 unità**, tutte `UI_LABEL`: 198 (`blown up`), 800 (`ka'het killed for the cloud probe`),
  804 (`ka'het killed early`), 818 (`burnt electronics`).
- **Nessuna `CONVERSATION`** in questo segmento.
- **`TOKEN_EXC` vuoto**: famiglie presenti `<system>`, `<destination>`, `<date>`, `<first>`, `<planet>`,
  `<npc>`, `<origin>`, `<tons>`, `<ship>`, `<payment>`, `<waypoints>`, `<bunks>`, `<stopovers>`,
  `<home planet>`.
- **651 unità con tab iniziale su 821**: confronto per unità.
- **29 gruppi di duplicati inglesi / 67 unità**.
- **1.199 virgolette**: 51 unità con conteggio dispari, riprodotte.

---

## Glossario del lotto

Navi invariati: `Swan`, `Petrel`, `Tern`, `Peregrine`, `Smew`, `Merganser`, `Albatross`, `Ibis`,
`Calm Sea Afire`, `Snipes`. Tecnologia: `nave viva`, `ramscoop`, `motore Scram`, `adatta all'atmosfera`,
`Cannone/Torretta Inibitrice`, `satellite zombi`. Da L24: `Cimitero`, `Distesa di Braci`, `Costruttori`,
`camera di equilibrio`, `Devastatore`, `Pietra Chiave`, `spettro del vuoto`, `motore di salto`.
Invariati: `Ka'het`, `Ka'sei`, `Fetri'sei`, `Ka'mar`, `Faes'mar`, `Alix`, `Pathera`, `Balnii`,
`Antamesa`, `Baliesa`, `Meligara`, `Seraglio`, `Kumkapi`, `Viminal`, `Ssil Vida`.

---

## Limiti dichiarati

- **51 unità con virgolette non bilanciate** (sorgente): riprodotte, non normalizzate.
- **Nessuna approvazione nel DB** e **nessun caricamento nel gioco**: verifica strutturale, non visiva.
- Il lotto è **−23,0%** dal target di 40.000 parole: è l'intero residuo del file, scelto per chiuderlo.

---

## Prossimo passo

**L29** = `data/hai/hai missions.txt`, righe **23–2696**, **823 unità**, 23.926 parole, 54 contesti.
Ripresa: unità **1**, riga **23**, contesto `mission:First Contact: Hai`. L29 chiude il file.
