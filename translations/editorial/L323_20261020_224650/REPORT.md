# REPORT — L323 (`data/rulei/rulei.txt`, righe 38–157) — **LOTTO TERMINALE**

**Esito: lotto CHIUSO, file CHIUSO a 41/41.** `check.py` esce 0 con **22 controlli**; `verify.py` esce 0 con **19 controlli**.
`state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 41 (38 `MISSION_TEXT` + 3 `LOGBOOK`) | 41 |
| parole | 919 | **871** (0,948) |
| tab | **32** | **32** |
| virgolette | **34** (16 unità) | **34** |
| segnaposto / alternative | 0 / 0 | **0 / 0** |
| apici | **12** (7 unità) | 19 |

Rapporto per unità **0,71 – 1,83**:

| riga | inglese → italiano | rapporto |
|---|---|---|
| 49 | `"Show yourself!"` → «"Mostrati!"» | **0,71** (due parole contro due, ma più corte) |
| 154 | `"Beware..."` → «"State in guardia..."» | **1,83** (l'inglese è una parola sola, l'italiano tre) |

Gli estremi sono **battute di due parole**: il rapporto non misura nulla, e il gate serve solo a intercettare **troncamenti**, non a
giudicare lo stile.

## 2. Invariante di FILE

```
FILE   41/41 (100%) · zero unità prima della 38 · zero dopo la 157
RIGHE  41 distinte · prima 38 · ultima 157 · un solo lotto
TIPI   38 MISSION_TEXT + 3 LOGBOOK
```

`data/rulei/rulei.txt` è il **trentasettesimo** file chiuso nel progetto (**96** su 167).

## 3. Il primo `LOGBOOK`, misurato invece che presunto

Il contratto diceva: «`LOGBOOK` = prosa di diario in **prima persona**». La misura dice:

| riga | inizio | persona reale |
|---|---|---|
| 38 | «I Rulei **erano** probabilmente una civiltà antica…» | **terza** (voce dell'equipaggio) |
| 116 | «**Scoperta** una regione di vuoto…» | **prima implicita** |
| 151 | «I Rulei **sembrano** riconoscere il vuoto…» | **terza** |

Il controllo è stato riscritto su ciò che è **vero e falsificabile**: i `LOGBOOK` **non contengono «tu»**, e la **116** ha la prima
persona implicita («Scoperta»). Un controllo su «noi/io» avrebbe dato **FAIL su un testo corretto**, come è successo al primo giro.

## 4. Il testo che scivola

Le righe 95–99 sono **una frase in cinque righe**, con l'indentazione che cresce:

```
95   ←11 tab→  Basta a far impazzire qualsiasi essere vivente.
98   ←21 tab→  la tua
99   ←23 tab→  mente nel pianeta qui sotto.
```

È il momento in cui la mente del giocatore viene **trascinata** nel pianeta, e il gioco lo mostra **muovendo il testo**. I tre numeri
(11 / 21 / 23) sono verificati **esatti e in entrambe le lingue**: se l'italiano avesse perso un tab, la frase avrebbe smesso di
scivolare — un danno visivo invisibile a ogni controllo sul contenuto.

## 5. La storia in cinque contesti

| contesto | unità | che cosa |
|---|---|---|
| `First Contact: Rulei` | 24 | il **contatto**: il vuoto, i sussurri, le domande del giocatore, le risposte — «**Umano**», «**Precursori**», «**Una Fine**» |
| `Rulei Planet` | 8 | il **pianeta**: il peso sulla mente, il testo che scivola, «meglio non restare troppo a lungo» |
| `You Are (Not) Alone: L-118` | 2 | **logbook** + arrivo: la regione di vuoto a est del nucleo |
| `You Are (Not) Alone: L-6181` | 1 | **una creatura** che gli scanner classificano come «collezione di materia» |
| `Umbral Reach` | 6 | il **nome** della regione e l'**avvertimento**: «State in guardia... Umbral Reach...» |

La scala è **del sorgente**: dal **contatto** al **pianeta** al **vuoto** al **nome** del vuoto. La resa non aggiunge nulla —
soprattutto non spiega che cos'è l'`Umbral Reach`, perché il testo **non lo spiega**.

## 6. Sei rossi al primo giro: quattro erano errori di **metodo**

| # | errore mio | correzione |
|---|---|---|
| 1 | virgolette e apici indicizzati per **indice** invece che per **riga** | riallineati con una **query**, non a mano |
| 2 | «13 battute fra virgolette» | sono **14** |
| 3 | «`Umbral Reach` 3 volte» | sono **2** per lingua: il test ora confronta **le due lingue** |
| 4 | «i `LOGBOOK` sono tutti in prima persona» | falso: solo la 116; controllo riscritto |
| 5 | soglia seconda persona a **15** | misurate **14**; soglia a **12** |

Il filo comune: avevo scritto il test **dal contratto** invece che **dalla misura**. Le asserzioni che restano sono tutte
**falsificabili** e **misurate**.

## 7. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 41 unità `PENDING`; il file è **finito in staging**, non approvato.
- **Nessun testo visto nel gioco**: l'indentazione a scala è verificata **nei dati**; che il motore la renda come «discesa» dipende dal
  font e dal layout, non dal testo.
- **`Umbral Reach` resta invariato**: è un **nome proprio di regione**, e la resa non lo traduce (né lo spiega).
