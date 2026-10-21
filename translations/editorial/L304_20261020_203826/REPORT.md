# REPORT — L304 (`data/quarg/quarg outfits.txt`, righe 37–137)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **21 controlli**; `verify.py` esce 0 con **22 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 11 (tutte `DESCRIPTION`) | 11 |
| parole | 466 | **473** (1,02) |
| tab | **5** | **5** |
| virgolette / segnaposto / alternative | 0 / 0 / 0 | **0 / 0 / 0** |
| apici | 1 | 11 |
| contesti | **6** (5 doppi + 1 prima metà) | invariati |

Rapporto per unità **0,99 – 1,16**.

## 2. Il ritornello: quattro identiche, una variante

| riga | soggetto inglese | resa |
|---|---|---|
| **38** | `**These engines** also have… Ships **equipped with them**` | «**Questi motori** hanno anche… Le navi che **ne sono dotate**» |
| **55** | `**They** also have… Ships **with these engines**` | «**Hanno** anche… Le navi **con questi motori**» |
| **78, 96, 120** | identiche alla 55 | identiche alla 55 |

La riga 38 è **la prima scritta**, quando il paragrafo parlava ancora del *modulo* («questi motori»); le altre quattro sono la
forma **rifattorizzata** sul soggetto implicito. È una **variante del sorgente**, non una svista dell'estrattore.

Il `check.py` verifica:
- che le **quattro** siano identiche **con `set()`**, in inglese e in italiano;
- che la **38** sia **diversa** e contenga «Questi motori» / «ne sono dotate»;
- che «Questi motori» **non** compaia nelle altre.

Uniformare tutto avrebbe cancellato una differenza reale; verificarle tutte con `set()` avrebbe fatto fallire un testo corretto.

## 3. Il confine taglia una coppia

La **137** (`Large Graviton Steering`) è la **prima** unità di una coppia; la **138**, fuori segmento, è la **seconda**. Il test
verifica **tre** cose: che la 137 non inizi con la tab, che il contesto sia lo stesso, e che la prima unità dopo il confine sia la
138 **dello stesso contesto**. Il taglio è **dichiarato nel contratto**, non un effetto collaterale.

## 4. Terminologia

Il corpus ha già «sistemi di governo» per `steering systems` (58 occorrenze), quindi:

- `steering engines` → **motori di governo**;
- `steering thrusters` → **propulsori di governo**.

La scelta mantiene il legame **nautico** con «governo» invece di introdurre «sterzata», che sarebbe più meccanico e meno coerente
con le schede di nave già tradotte.

## 5. Verifica

```
check.py   21 controlli · FAIL totale: 0 · exit 0
verify.py  22 controlli · FAIL: 0 · exit 0
segmento   0 prima · 11 qui · 20 dopo la 137 · file 11/31 (35,5%)
```

**Primo giro verde**: il contratto aveva individuato la variante della 38 e il confine sulla 137.

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 11 unità `PENDING`; **nessuna revisione umana**.
- **Nessun testo visto nel gioco**.
- **Il file resta aperto**: 11/31; restano **20 unità**.
