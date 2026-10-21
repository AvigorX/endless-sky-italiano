# REPORT — L322 (`data/human/frontier jobs.txt`, righe 16–318) — **LOTTO TERMINALE**

**Esito: lotto CHIUSO, file CHIUSO a 45/45.** `check.py` esce 0 con **24 controlli**; `verify.py` esce 0 con **21 controlli**.
`state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 45 | 45 |
| parole | 1.014 | **999** (0,985) |
| tab | **19** | **19** |
| virgolette | **4** | **4** |
| segnaposto | **10 tipi** | **10 tipi** identici |
| alternative | 0 | **0** |
| apici | **18** (12 unità) | 13 |

Rapporto per unità **0,63 – 1,58**. I due estremi sono **scelte del giocatore** di lunghezza diversa:

| riga | inglese | italiano | rapporto |
|---|---|---|---|
| 269 | `(Say nothing and continue playing.)` | «(Non dire nulla e continua a giocare.)» | **0,63** |
| 250 | `(Join their game.)` | «(Unisciti alla loro partita.)» | **1,58** |

Su frasi di 20–30 caratteri il rapporto **non misura la qualità**: misura solo quanto l'italiano deve aggiungere o togliere per essere
idiomatico.

## 2. Invariante di FILE

```
FILE   45/45 (100%) · zero unità prima della 16 · zero dopo la 318
RIGHE  45 distinte · prima 16 · ultima 318 · un solo lotto
TIPI   7 VALUE + 6 UI_LABEL + 8 DESCRIPTION + 4 DIALOG + 20 MISSION_TEXT
```

`data/human/frontier jobs.txt` è il **trentaseiesimo** file chiuso nel progetto (**95** su 167).

## 3. La trappola che il contratto aveva dichiarato — e che era vera

Le sei `UI_LABEL` **sembrano prosa**:

```
good luck   bad luck   shoot and die   shoot and run   grab and die   grab and run
```

Sono **etichette di salto** (`label` / `goto`) della conversazione `Small Pirate gambling`: il codice le usa come **bersagli**, il
giocatore **non le vede**. Tradurle avrebbe **rotto tutti i salti** — e nessun controllo sul numero di parole o sul rapporto
l'avrebbe rilevato.

Il test le **elenca** e le pretende **identiche**. Non è una precauzione teorica: in questo file sei salti su sei sarebbero diventati
irraggiungibili.

## 4. I controlli sono **per gruppo**, mai in somma

Il contratto lo imponeva e il test lo fa:

| gruppo | che cosa si verifica |
|---|---|
| **copiati** (13) | `italian == english` **per tipo** (7 `VALUE`, 6 `UI_LABEL`) |
| **tradotti** (32) | `italian != english` **per tipo** (8 `DESCRIPTION`, 4 `DIALOG`, 20 `MISSION_TEXT`) |

Un controllo «13 + 32 = 45 unità, tutte presenti» avrebbe **passato** un lotto in cui le `UI_LABEL` erano tradotte e i `VALUE` no.

## 5. Il casinò: quattro finali, due coppie

```
(shoot first!)  →  296 «il tuo corpo straziato cade a terra»     /  302-303 «spari, ne abbatti due e fuggi»
(grab the pot)  →  311 «il pirata ti finisce con un altro colpo»  /  317-318 «arraffi la posta e fuggi»
```

I due finali «fuga» hanno **la stessa prima frase**:

> «Corri verso la baia degli hangar e decolli in fretta. Conti rapidamente il bottino e vedi che sei più ricco di quasi 25.000
> crediti!»

e **diversa la seconda**: nel primo i **due pirati rimasti** ti urlano insulti via radio, nel secondo le **autorità del porto** ti
avvisano che due sono stati fermati. Il test verifica **entrambe** le cose: l'**identità** dell'esordio e la **differenza** del resto.
Due finali identici sarebbero un errore; due finali completamente diversi avrebbero perso la **simmetria** del sorgente.

## 6. `<npc>` è femminile

`forgot to escort the <npc>` → «hai dimenticato di scortare **la** `<npc>`». La regola era già stata fissata (una `<npc>` è una
**nave**), e il test la verifica alla lettera: «la `<npc>`».

## 7. Verifica

```
check.py   24 controlli · FAIL totale: 0 · exit 0
verify.py  21 controlli · FAIL: 0 · exit 0
FILE       45/45 (100%) · trentaseiesimo file completo
```

**Nessun rosso**: primo giro verde. Il file era il primo a **cinque tipi**, e la scomposizione in gruppi ha reso inutile qualunque
correzione: ogni tipo ha il suo controllo, e nessuno può «coprire» un altro.

## 8. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 45 unità `PENDING`; il file è **finito in staging**, non approvato.
- **Nessun testo visto nel gioco**: che le sei `UI_LABEL` siano davvero `goto` è **dedotto dal tipo** (`UI_LABEL`) e dalla forma
  (`good luck`, `shoot and die`), non letto nel codice di Endless Sky in questa sessione.
- **I valori di gioco** (25.000 crediti, 15.000, 10.000) sono **testo**, non verificati contro il bilanciamento del gioco.
