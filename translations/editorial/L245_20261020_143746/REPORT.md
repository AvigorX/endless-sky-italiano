# REPORT — L245 (`data/hai/hai ships.txt`, righe 901–1516)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **32 controlli** (`FAIL totale: 0`); `verify.py` esce 0 con **26 controlli**
(invariante di segmento: 74 prima, 46 qui, 37 dopo). `state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su
`state.db`: le 46 unità restano `PENDING`.

## 1. Cosa contiene il lotto

| contesto | unità | contenuto |
|---|---|---|
| `Pond Strider` | 8 `TEXT` | la coda della scheda lasciata aperta da L244 (righe 901–953) |
| `Sea Scorpion` | 12 `TEXT` + 1 `DESCRIPTION` | piattaforma mobile per lanciare i Tracker; gli Slegati la producono in serie |
| `Scarab` | 2 `TEXT` + 1 `DESCRIPTION` | la cugina laboriosa della Lightning Bug |
| `Shield Beetle` | 18 `TEXT` + 1 `DESCRIPTION` | l'unica nave da guerra pesante degli Hai |
| `Emperor Beetle` | 2 `DESCRIPTION` | un Titan corazzato: ammiraglia e nave trofeo; il secondo paragrafo è **rientrato col tab** |

## 2. Misure

```
unità             46            (41 TEXT + 5 DESCRIPTION · NESSUN VALUE)
parole            442 EN -> 441 IT       rapporto 0,98 - 1,10 (media 1,00)
contesti          5             (8 + 13 + 3 + 20 + 2 = 46)
tab               1             all'inizio dell'unità 46, in inglese e in italiano
virgolette        82            = 2 × 41 nomi, nessuna nella prosa
apici             0 EN / 2 IT   (unità 27 e 45: elisioni)
segnaposto        0             asserzione negativa scritta
gruppi duplicati  6             di nomi ripetuti, una resa ciascuno
```

## 3. Le tre cose che il lotto ha di proprio

1. **Non c'è nessun `VALUE`.** Il file ne ha due e il secondo (`Geocoris`) è passato in L244. Il controllo non si limita
   a far tornare i conteggi: pretende che nel `Counter` dei tipi la chiave `VALUE` **non esista**. Un export sbagliato di
   una riga la farebbe ricomparire e il test diventa rosso.
2. **Il tab è su una `DESCRIPTION`, non su una nota.** È il secondo paragrafo della scheda dell'Emperor Beetle, che il
   gioco mostra rientrato. Verificato come **primo carattere in entrambe le lingue** e con un controllo di contenuto
   («baie di carico» + punto finale), così una traduzione che lo perde non passa.
3. **I plurali inglesi dei nomi non si copiano.** L'inglese dice `Shield Beetles` e `Trackers`; l'italiano «gli Shield
   Beetle» e «i Tracker». Il controllo asserisce **entrambe le direzioni**: le forme plurali **esistono in inglese** e
   **non esistono in italiano** — altrimenti «non c'è `Shield Beetles`» passerebbe anche se l'inglese non lo dicesse mai.

## 4. Copertura del file

```
L243   29 unità   righe  15 -  332
L244   45 unità   righe 362 -  885
L245   46 unità   righe 901 - 1516
---------------------------------
120 unità su 157 (76,4%)

residuo 37 unità, righe 1517 - 1860   → lotto TERMINALE (L246)
```

## 5. Controlli che hanno morso

Un rosso, **nell'asserzione**: la `verify.py` dichiarava **13** «unità-nome» nelle schede, misurate **10** (il mio elenco
includeva `Titan` e `Titan Beetle`, che si sovrappongono, e `Titan` non era nella tupla). Sostituito il totale con un
**conteggio per nome** (`{'Sea Scorpion': 1, …, 'Shield Beetle': 3, …}`, 11 unità-nome), che è più stretto: un nome
aggiunto al sorgente sposta il numero e il controllo se ne accorge.

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: le 46 unità sono `PENDING`.
- **Nessuna scheda vista nel gioco**: il tab è verificato **sul carattere**, non a schermo.
- **Nessuna revisione umana**.
- **Il file non è completo**: 120/157 (76,4%); le **37** unità che restano sono un lotto terminale.
