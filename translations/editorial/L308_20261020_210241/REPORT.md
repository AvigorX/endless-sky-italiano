# REPORT — L308 (`data/avgi/avgi weapons.txt`, righe 264–703)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **26 controlli**; `verify.py` esce 0 con **25 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | **21** (13 `DESCRIPTION` + 5 `TEXT` + 3 `VALUE`) | 21 |
| parole | 489 | **537** (1,10) |
| tab | **7** | **7** |
| virgolette | **10** | **10** |
| segnaposto / alternative | 0 / 0 | **0 / 0** |
| apici | 3 | 9 |
| contesti | **6** | invariati |

Rapporto per unità **0,97 – 1,29**.

## 2. Il primo lotto a tre tipi

| tipo | righe | trattamento | verifica |
|---|---|---|---|
| `DESCRIPTION` | 264, 265, 531, 570, 613, 614, 615, 657, 658, 659, 701, 702, 703 | **tradotto** | `italian != english` per tutte e 13 |
| `TEXT` | 515, 551, 592, 636, 680 | **copiato** | `italian == english` per tutte e 5 |
| `VALUE` | 574, 618, 662 | **copiato** | `italian == english` per tutti e 3 |

I `TEXT` sono **nomi di munizione fra virgolette**: `"Ophrys" Nuclear Torpedo`, `"Orchid" Nuclear Missile`, `"Nettle" KKV`. La
verifica è **doppia**: copiati **e** con **due virgolette ciascuno** (5 × 2 = 10).

## 3. La nota munizioni arriva a **cinque** occorrenze

| lotto | righe |
|---|---|
| L307 | 69, 108 |
| **L308** | **615, 659, 703** |

Il `check.py` riapre il `translation.json` di L307 e confronta **tutte** con la costante `NOTA`. Cinque armi diverse, **una sola
frase**: è il tipo di coerenza che nessun revisore umano manterrebbe per 46 unità.

## 4. Il paragrafo VLS: tre colonne, una frase

Le righe 614, 658 e 702 dicono **la stessa cosa**: i sistemi VLS sono «insieme lanciatori e caricatori», quindi **non c'è un
deposito separato**. Il test verifica con `set()` che le tre stringhe italiane siano **una sola**.

## 5. La sorellanza 265 ↔ 203

| riga | lotto | potenza |
|---|---|---|
| **203** | L307 | «potenza sufficiente ad alimentare **tre Green Laser**» |
| **265** | L308 | «potenza sufficiente ad alimentare **un solo Blue Laser**» |

Il test confronta le due frasi **sostituendo** la parte variabile (`tre Green Laser` → `X`, `un solo Blue Laser` → `X`): se la
struttura fosse divergita, sarebbe un difetto invisibile a occhio.

## 6. Verifica

```
check.py   26 controlli · FAIL totale: 0 · exit 0
verify.py  25 controlli · FAIL: 0 · exit 0
segmento   12 prima · 21 qui · 13 dopo la 703 · file 33/46 (71,7%)
```

**Tre rossi al primo giro**, tutti **miei**:
1. indici delle tre colonne VLS sbagliati (`[10, 14, 19]` invece di `[10, 15, 20]`) — i contesti VLS hanno **cinque** unità
   (VALUE + TEXT + tre `DESCRIPTION`), non tre;
2. distribuzione dei contesti scritta `[2,2,5,5,5,2]` invece di `[2,2,2,5,5,5]`;
3. la terzina VLS confrontata su **tutte** le unità del contesto: corretto filtrando `kind == 'DESCRIPTION'`.

## 7. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 21 unità `PENDING`; **nessuna revisione umana**.
- **Nessun testo visto nel gioco**: le `TEXT` (nomi di munizione) sono verificate **nei dati**, non nel pannello.
- **Il file resta aperto**: 33/46; restano **13 unità** (il lotto **terminale**).
