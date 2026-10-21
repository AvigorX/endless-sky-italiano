# REPORT — L301 (`data/remnant/remnant ships.txt`, righe 17–806)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **22 controlli**; `verify.py` esce 0 con **24 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 12 (**10 `DESCRIPTION` + 2 `VALUE`**) | 12 |
| parole | 477 | **483** (1,01) |
| tab | **5** | **5** |
| virgolette | **4** | **4** |
| segnaposto / alternative | 0 / 0 | **0 / 0** |
| apici | 6 | 14 |
| contesti | **4** | invariati |

Rapporto per unità **0,91 – 1,17**.

## 2. Struttura del lotto

```
 17  VALUE        Albatrosses              -> copiato
 88  DESCRIPTION  Albatross
274  VALUE        Modified Dromedaries     -> copiato
350  DESCRIPTION  Modified Dromedary       ┐
351  DESCRIPTION  Modified Dromedary (tab) ├ terzina 1
352  DESCRIPTION  Modified Dromedary (tab) ┘
474  DESCRIPTION  Modified Dromedary       ┐ coppia (relitto): 474 = 350
475  DESCRIPTION  Modified Dromedary (tab) ┘
547  DESCRIPTION  Gull                     ┐
548  DESCRIPTION  Gull             (tab)   ├ terzina 2
549  DESCRIPTION  Gull             (tab)   ┘
806  DESCRIPTION  Heron                    (unica del lotto)
```

## 3. Il paragrafo ripetuto: nave integra e relitto

Le righe **350** e **474** sono **identiche**. Il gioco le usa per **due stati** della stessa nave: la `Modified Dromedary`
**integra** (con 351/352 che raccontano la replica commemorativa) e il **relitto** (con la 475 che descrive lo scafo distrutto).

La resa è **identica** e verificata in **entrambe le lingue**. È la **quarta** ripetizione riprodotta nel progetto
(`marauders.txt` 831/858 e 884/910, `coalition outfits.txt` 395/415, `remnant ships.txt` 350/474): il criterio è sempre lo
stesso — **si riproduce ciò che il giocatore vede**, non si uniforma.

## 4. I `VALUE` sono plurali dell'interfaccia

`Albatrosses` e `Modified Dromedaries` sono i **nomi al plurale** che il gioco mostra quando più navi di quel tipo sono
selezionate. Copiati: tradurli avrebbe rotto il legame con il nome singolare, che resta invariato nelle descrizioni.

## 5. Il confine 806/807

Il lotto finisce sulla **806**, che appartiene al contesto `Heron`; la **807** è la **seconda** unità **dello stesso contesto**.
È un taglio **dichiarato** sul numero di parole (477), non una coppia spezzata dentro il lotto. Il test verifica **tre** cose: che
806 sia nel segmento, che 807 sia la prima unità dopo, e che nel segmento ci sia **una sola** unità `Heron`.

## 6. Verifica

```
check.py   22 controlli · FAIL totale: 0 · exit 0
verify.py  24 controlli · FAIL: 0 · exit 0
segmento   0 prima · 12 qui · 26 dopo la 806 · file 12/38 (31,6%)
```

**Un rosso al primo giro** (controllo mio): il filtro della terzina `Modified Dromedary` prendeva anche il `VALUE` della riga 274
(stesso contesto), quindi la lista era `[274, 350, 351, 352]` invece di `[350, 351, 352]`. Corretto filtrando per `kind`.

## 7. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 12 unità `PENDING`; **nessuna revisione umana**.
- **Nessun testo visto nel gioco**: il taglio tab/paragrafo è verificato **nei dati**.
- **Il file resta aperto**: 12/38; restano **26 unità**.
