# REPORT — L236 (`data/avgi/avgi news.txt`, righe 301–344)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **36 controlli** (`FAIL totale: 0`); `verify.py` esce 0 con **21
controlli** (invariante di segmento: 57 prima, 23 qui, 35 dopo). `state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna
scrittura su `state.db`: le 23 unità restano `PENDING`.

## 1. Cosa contiene il lotto

| contesto | righe | unità | contenuto |
|---|---|---|---|
| `news:avgi student happy` | 301–313 | 13 | sei lauree magistrali (fisica, economia, ingegneria, nanotecnologia, genetica, aerodinamica), l'ingresso nell'accademia, i fondi arrivati con gli umani, la fine degli esami intermedi, i compiti mangiati dall'Aberrant, il confronto con Aviskir e Livloua |
| `news:avgi student frustrated` | 335–344 | 10 | scienze politiche contro le materie «pratiche», linguistica dirottata a ingegneria, arte derisa, sociologia «inutile alla Guerra», la ricerca di un lavoro, l'ultimo esame, e le tre battute ripetute dal primo contesto |

## 2. Misure

```
unità             23            (tutte NEWS)
parole            348 EN -> 320 IT
rapporto          0,88 - 1,58 (media 1,04)   gate 0,55-1,90
contesti          2             (student happy 13, student frustrated 10)
tab               0             asserzione negativa scritta
virgolette        46            esattamente 2 per unità
apici             18 EN / 14 IT (contrazioni e virgolette semplici in entrambe le lingue)
segnaposto        0             asserzione negativa scritta
identiche         0             23 tradotte
etichette         19 in testa + 4 senza + 2 in coda
```

## 3. Le relazioni del lotto, verificate come relazioni

| relazione | forma | controllo |
|---|---|---|
| **tre coppie di inglese identico** | 10/20, 12/22, 13/23 | stessa resa dentro la coppia, confronto di stringa |
| **una coppia quasi identica** | 11/21 | stesso testo **tranne** l'etichetta in coda (`divertimento.` / `scoramento.`): il controllo toglie l'ultima parola e confronta |
| **sei varianti di una formula** | 301–306 | `re.sub` sulle sei discipline → **una sola** stringa risultante |
| **quattro unità senza etichetta** | 10, 11, 20, 21 | lista delle etichette con `None` in quelle posizioni, confrontata **con** i `None` |
| **il dispositivo della domanda Avgi** | 10, 20 | «, domanda?» 2 volte, come «, question?» 2 volte |

## 4. Copertura del file

```
L233   22 unità   righe  32 -  91
L234   20 unità   righe 115 - 180
L235   15 unità   righe 197 - 280
L236   23 unità   righe 301 - 344
residuo 35 unità  righe 369 - 507
------------------------------------
22 + 20 + 15 + 23 + 35 = 115 = unità del file (min 32, max 507)
```

Copertura **80/115 (69,6%)**. Confine misurato: **riga 369**, `news:avgi physicist`.

## 5. Controlli che hanno morso

Un solo rosso, al primo giro, **nel `verify.py` e non nella traduzione**: avevo scritto una catena
`IT == EN == [lista italiana]`, che non può reggere perché le etichette inglesi sono inglesi. Corretto in due confronti
separati (lista italiana contro la lista italiana, lista inglese contro la lista inglese). Il `check.py` era già verde.

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: le 23 unità sono `PENDING`.
- **Nessuna notizia vista nel gioco**.
- **Nessuna revisione umana**.
- **Il file non è completo**: 80/115 (69,6%).
