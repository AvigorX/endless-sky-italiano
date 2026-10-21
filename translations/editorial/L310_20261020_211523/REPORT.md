# REPORT — L310 (`data/korath/korath culture conversations.txt`, righe 26–75) — **LOTTO TERMINALE**

**Esito: lotto CHIUSO, file CHIUSO a 27/27.** `check.py` esce 0 con **23 controlli**; `verify.py` esce 0 con **23 controlli**.
`state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 27 (24 `MISSION_TEXT` + 3 `UI_LABEL`) | 27 |
| parole | 1.295 | **1.187** (0,92) |
| tab | **23** | **23** |
| virgolette | **14** | **14** |
| segnaposto | **3** | **3** |
| alternative | 0 | **0** |
| apici | 10 | 12 |

Rapporto per unità **0,82 – 1,48**: le due battute brevi fra virgolette («Che cosa sarebbe tutto questo, esattamente?»,
«(Gesticola verso il santuario…)») crescono **in percentuale** perché una frase nominale italiana richiede più parole di
un'interrogativa inglese di quattro parole.

## 2. Invariante di FILE

```
FILE         27/27 (100%) · 27 righe distinte · prima 26 · ultima 75
PRIMA/DOPO   zero unità prima della 26 · zero dopo la 75
LOTTI        uno solo: il file intero
```

`data/korath/korath culture conversations.txt` è il **trentesimo** file chiuso nel progetto (**89** su 167).

## 3. Che cos'è la scena

Una **preghiera** in un santuario di casse, in uno spazioporto Korath. Il gioco mostra al giocatore:

- i **bambini** che disegnano un **pianeta** sul muro;
- le **lastre incise** che, viste da certi angoli, formano **mappe stellari**;
- una **candela sola** su una piuma, una conchiglia e un fiore, e **nessun vento** su `<origin>`;
- la **giovane Korath** che disegna **braccia a spirale** (la galassia) e un punto protetto da una **barriera** (`Far'en Lai`);
- **quattro modi** di partecipare: tre offerte in crediti e **una fotografia di casa**.

## 4. Le scelte e la scala

| riga | scelta | resa |
|---|---|---|
| 43 | `(Offer 100 credits.)` | `(Offri 100 crediti.)` |
| 47 | `(Offer 10,000 credits.)` | `(Offri 10.000 crediti.)` |
| 51 | `(Offer 10,000,000 credits.)` | `(Offri 10.000.000 crediti.)` |
| 55 | `(Offer a picture of my home planet.)` | `(Offri una fotografia del mio pianeta natale.)` |
| 56 | `"I'm sorry, but I have nothing to offer. Goodbye."` | «Mi dispiace, ma non ho nulla da offrire. Addio.» |

**Le parentesi sono del sorgente** e restano: sono le **scelte del giocatore**, non prosa. I numeri passano alla **separazione
italiana** (`.`) come in tutto il progetto.

## 5. Il gesto che cambia di valore

Le risposte alle tre offerte **non sono uguali**:

| riga | reazione |
|---|---|
| 63 (100 crediti) | «annuire con approvazione», «soddisfatta della tua comprensione» |
| 68 (10.000) | lei e altri **si inchinano leggermente** |
| 73 (10.000.000) | i chip **cadono rumorosamente**, ma i Korath sono **sconvolti**, non infastiditi: «sembra raggiante» |

La resa conserva la **gradazione**: comprensione → rispetto → **shock reverenziale**.

## 6. Verifica

```
check.py   23 controlli · FAIL totale: 0 · exit 0
verify.py  23 controlli · FAIL: 0 · exit 0
FILE       27/27 (100%) · trentesimo file completo
```

**Due rossi al primo giro**, tutti **miei**:
1. pretendevo la seconda persona in **≥15** unità misurandola **solo sui pronomi**: l'italiano la esprime spesso **solo nel
   verbo** («noti», «vedi», «cominci»), quindi ne trovavo 10. Sostituito con: pronomi in ≥10 unità **e** presenza esplicita di
   «ti serve», «noti», «Ti ricordi» nelle tre unità chiave;
2. le quattro offerte iniziano con la **tab**: `startswith('(')` falliva. Corretto con `lstrip(TAB)`.

## 7. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 27 unità `PENDING`; il file è **finito in staging**, non approvato.
- **Nessun testo visto nel gioco**: la resa del **santuario** e delle **scelte** è verificata **nei dati**, non a schermo.
- **Il file è completo al 100%** solo in staging.
