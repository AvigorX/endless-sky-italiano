# REPORT — L302 (`data/remnant/remnant ships.txt`, righe 807–1291)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **24 controlli**; `verify.py` esce 0 con **24 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 12 (**11 `DESCRIPTION` + 1 `VALUE`**) | 12 |
| parole | 486 | **509** (1,05) |
| tab | **6** | **6** |
| virgolette / segnaposto / alternative | 0 / 0 / 0 | **0 / 0 / 0** |
| apici | 6 | 15 |
| contesti | **6** | invariati |

Rapporto per unità **1,00 – 1,13**: il **primo lotto del file** in cui l'italiano è **sempre più lungo** dell'inglese, perché le
descrizioni sono dense di **termini tecnici composti**.

## 2. La famiglia `cloaking technology`: quattro frasi, una sola resa

| riga | nave | lotto |
|---|---|---|
| 549 | `Gull` | **L301** |
| 982 | `Merganser` | L302 |
| 1202 | `Penguin` | L302 |
| 1291 | `Peregrine` | L302 |

Il `check.py` **riapre il `translation.json` di L301**, sostituisce il nome della nave con `X` in entrambe le versioni e
confronta le stringhe risultanti. Non è un controllo di presenza: è un controllo di **uguaglianza strutturale**. Se la
`Peregrine` avesse ricevuto una resa «migliore» («lo scafo integra la tecnologia…»), il test avrebbe fallito.

## 3. La continuità di `Heron` fra due lotti

La stessa nave è descritta in **806** (L301) e **807** (L302). Il contesto è **uno**, il taglio è **uno**, e il test lo verifica
su entrambi i lati: la **807** inizia con la tab, la **806** no. È l'unico caso finora di contesto **diviso su due lotti** — perché
la finestra di L301 era già satura.

## 4. Struttura

```
 807  DESCRIPTION  Heron      (tab)   2ª unità del contesto
 812  VALUE        Ibis       -> copiato («Ibises»)
 892  DESCRIPTION  Ibis                ┐
 893  DESCRIPTION  Ibis      (tab)     ┘
 981  DESCRIPTION  Merganser           ┐
 982  DESCRIPTION  Merganser (tab)     ┘ + formula occultamento
1072  DESCRIPTION  Pelican            (singola)
1201  DESCRIPTION  Penguin            ┐
1202  DESCRIPTION  Penguin   (tab)     ┘ + formula occultamento
1289  DESCRIPTION  Peregrine          ┐
1290  DESCRIPTION  Peregrine (tab)     ├ terzina
1291  DESCRIPTION  Peregrine (tab)     ┘ + formula occultamento
```

## 5. Verifica

```
check.py   24 controlli · FAIL totale: 0 · exit 0
verify.py  24 controlli · FAIL: 0 · exit 0
segmento   12 prima · 12 qui · 14 dopo la 1291 · file 24/38 (63,2%)
```

**Primo giro verde**: il contratto aveva individuato la famiglia dell'occultamento, la continuità `Heron` e la terzina.

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 12 unità `PENDING`; **nessuna revisione umana**.
- **Nessun testo visto nel gioco**.
- **`Ember Waste` resta invariato** nonostante l'anomalia (69 «Distesa di Braci» vs 16 inglese): serve **autorizzazione
  esplicita** per cambiare, e il lotto non l'ha.
- **Il file resta aperto**: 24/38; restano **14 unità**.
