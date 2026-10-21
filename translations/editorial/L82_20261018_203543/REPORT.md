# REPORT — L82 · `data/successors/predecessors.txt`

## 1. Cosa contiene il lotto

Quattro blocchi di un file che descrive navi e armi dei Predecessori:

- **Hasur, Vowsworn** (1–2): l'avvertimento dei **costrutti** della «sciocca Myiara» — «eternamente morenti
  ma mai morti, consumati da una rabbia programmata» — che chiude con una promessa: «Ti uccideranno. Lo
  faranno in fretta.»
- **Queru, Luminous Gazes** (3, 12): la nave e la sua scheda — «il più ispirato dei tre», che sventrava a
  distanza; Resja lo odiavano, ma il loro destino era già segnato.
- **"Iasa," Lethal Word** (4–13): l'arma, otto voci di equipaggiamento e la scheda — il **cannone a bobina**
  di una nave drone, «un'arma temibile e affamata», efficiente dopo **millecinquecento anni**.
- **"Kis," Lethal Wishes** (14–15): l'arma e la scheda — una «bestia fredda e famelica» che squarcia le
  difese da vicino e, da lontano, perde penetrazione ma resta rispettabile.

## 2. Scelte editoriali

| nodo | scelta | perché |
|---|---|---|
| `Querun, Luminous Gazes`, `"Kis," Lethal Wishes`, 8 nomi di equipaggiamento | **identici** | dati definiti altrove (decisione 259) |
| `coilgun` (in prosa) | **cannone a bobina** | qui è descrizione, non nome d'oggetto |
| `immured deep within those hostile, rotting abscesses of the stars` | «murati in fondo a quegli ascessi ostili e putrescenti delle stelle» | l'immagine medica è dell'autore |
| `their so-false flesh` | «la loro carne così falsa» | l'enfasi è nel `so-` |
| `eviscerating at a distance` | «sventrava a distanza» | verbo crudo, non «annientava» |
| `a fearsome, hungry weapon` | «un'arma temibile e affamata» | due aggettivi, tenuti separati |
| `fifteen hundred years of waiting` | «millecinquecento anni di attesa» | numero in lettere |
| `encouraging enemies to retreat` | «incoraggiando i nemici a ritirarsi» | letterale: è una nota di bilanciamento |

## 3. Difficoltà incontrate

1. **Un trattino lungo inglese** (`Resja hated it - but by then`): l'em dash è vietato, e la resa usa una
   virgola — il senso concessivo resta.
2. **`-` in unità 12 e `:` in unità 1**: punteggiatura diversa, resa diversa (virgola e due punti), non
   appiattita.
3. **1 tab** (unità 2): il primo del file; le parti non ne hanno, e il costruttore lo aggiunge.
4. **Nessun duplicato**: i nomi ripetuti in L81 qui non tornano, e il controllo negativo lo dichiara.
5. **Un errore mio nel `check.py`**: la riga dei token passava `tok` come terzo elemento (il booleano), e
   stampava `FAIL True` su un conteggio corretto — corretto in `str(tok), tok == 0`.

## 4. Numeri osservati (output letto)

```
unita' 15/15 · copertura 15/15
tab IT 1 / EN 1 · virgolette IT 8 / EN 8 · dispari 0
token 0 = 0 · duplicati 0 gruppi
rapporto IT/EN 0.97 - 1.10
parole EN 220 -> IT 220
prima/ultima riga: 208/381
FAIL totale: 0    (26 controlli)
verify.py exit 0  (32 controlli)
sha256[:16] 3a179de373b2fe67
```

## 5. Stato del progetto dopo il lotto

```
TOTALE staging: 24795 unita · 789498 EN · 748372 IT
predecessors.txt: 37/59 (62,7%) · 326 EN -> 326 IT · 2 lotti
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 1 parte, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (26 controlli) **e** `verify.py` exit **0** (32 controlli) |
