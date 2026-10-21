# REPORT — L234 (`data/avgi/avgi news.txt`, righe 115–180)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **33 controlli** (`FAIL totale: 0`); `verify.py` esce 0 con **21
controlli** (invariante di segmento: 22 prima, 20 qui, 73 dopo). `state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna
scrittura su `state.db`: le 20 unità restano `PENDING`.

## 1. Cosa contiene il lotto

| contesto | righe | unità | chi parla |
|---|---|---|---|
| `news:avgi merchant` | 115–124 | 10 | mercanti: prezzo del carburante, tasse e porti compiacenti, sfida, dubbio sulle nuove tasse, ironia sui pirati, rotta commerciale nuova, orgoglio per la compagnia di navigazione, l'Impresa e l'Incursione, tristezza per i convogli persi |
| `news:avgi politician` | 150–155 | 6 | politici: impopolarità di tasse e quote, le mille entità politiche di prima dell'Incursione, derisione verso chi «costruirebbe più navi», umorismo sul consenso, riserva sull'austerità, rassicurazione sui debiti |
| `news:avgi military` | 177–180 | 4 | militari: notizie di Aberrant nello Shroud (domanda Avgi), riflessione sul futuro della specie, determinazione della Guardia, orgoglio di chi era paggetto su una nave corriere |

## 2. Misure

```
unità             20            (tutte NEWS)
parole            439 EN -> 433 IT
rapporto          0,90 - 1,28 (media 1,11)   gate 0,55-1,90
contesti          3             (merchant 10, politician 6, military 4)
tab               0             asserzione negativa scritta
virgolette        40            esattamente 2 per unità
apici             6 EN / 12 IT  EN (5,6,9,10,11,16) · IT (5,6,9,11x2,12x2,13,15,18,19,20)
segnaposto        0             asserzione negativa scritta
identiche         0             20 tradotte
etichette         19 su 20      la 177 non ne ha: è una domanda Avgi
```

## 3. Copertura del file

```
L233   22 unità   righe  32 -  91
L234   20 unità   righe 115 - 180
residuo 73 unità  righe 197 - 507
------------------------------------
22 + 20 + 73 = 115 = unità del file (min 32, max 507)
```

Confine misurato: **riga 197**, `news:avgi safety advisory`. Fra la 180 e la 197 il file non ha unità.

## 4. Controlli che hanno morso

Nessun rosso al primo giro. Le due cose verificate **prima** di scrivere:

- **la lista delle etichette ha un `None`**: un controllo che ne pretendesse venti sarebbe stato rosso su un lotto
  corretto, e la forma scritta (`IT_LAB == [... None ...]`) lo rende impossibile da sbagliare in silenzio;
- **gli apici si invertono rispetto a L233**: 6 contro 12, con le unità elencate — un totale uguale avrebbe potuto
  nascondere uno scambio.

## 5. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: le 20 unità sono `PENDING`.
- **Nessuna notizia vista nel gioco**.
- **Nessuna revisione umana**.
- **Il file non è completo**: 42/115 (36,5%) dopo questo lotto.
