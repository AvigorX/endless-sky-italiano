# REPORT — L294 (`data/human/marauders.txt`, righe 62–484)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **19 controlli**; `verify.py` esce 0 con **21 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 12 (tutte `DESCRIPTION`) | 12 |
| parole | 493 | **549** (1,11) |
| tab / virgolette / segnaposto / alternative | 0 / 0 / 0 / 0 | **0 / 0 / 0 / 0** |
| apici | 5 | 7 |

Rapporto per unità **1,08 – 1,29**: tutte sopra 1, come le schede tecniche di L286–L289.

## 2. La struttura a serie

Il file organizza **lo stesso modello in tre allestimenti**: il test verifica **tre unità per contesto** e le righe esatte, e in
più controlla che le varianti **si distinguano per contenuto**:

```python
'combattimento' in by[1] and 'missile' in by[2] and "sistemi d'arma" in by[3]      # Arrow
'ancora più veloce' in by[5] and 'letale' in by[6]                                  # Bounder
```

Senza questo, tre descrizioni quasi identiche sarebbero passate (stessa lunghezza, stesso lessico tecnico).

## 3. Il registro, misurato invece che presunto

Le schede sono **tecniche** ma **quattro** parlano al lettore. Il test usa una **lista esatta** di righe ammesse:

```
[1, 8, 9, 10]  ← «possiate trovare», «il tuo sogno», «tu possa immaginare», «sospetti»
```

È **l'opposto** della regola applicata a `gegno ships.txt` (L286–L289), dove il «tu» era vietato. Significa che il registro va
deciso **per file**, non per progetto.

## 4. Terminologia: il corpus vince sul gusto

`gun port` si potrebbe rendere «feritoia per cannoni», più naturale in italiano. Il corpus ha però **11 occorrenze** di «**porto
per cannoni**»: la coerenza con ciò che il giocatore ha già letto vale più dell'eleganza locale. Il test **rifiuta** «feritoia»
nella resa.

Stessa logica per `hull plating` → «corazzatura» e `interceptor` → «intercettore» (58 occorrenze).

## 5. I nomi che restano

`Arrow` · `Bounder` · `Falcon` · `Firebird` · `Megaparsec` · `Tarazed` · `Betelgeuse` · `Lionheart` · `Headhunter` · `Flivver`.

Il test verifica anche l'**assenza** di traduzioni tentatrici («Freccia», «Falcone», «Uccello di fuoco»): un nome di modello
tradotto romperebbe il riferimento alle navi base, che nel gioco hanno lo stesso nome.

## 6. Verifica

```
check.py   19 controlli · FAIL totale: 0 · exit 0
verify.py  21 controlli · FAIL: 0 · exit 0
segmento   0 prima (apre il file) · 12 qui · 17 dopo la 484 · 4 serie da 3
```

**Un rosso al primo giro** (controllo mio): cercavo «velocità» nella seconda variante del `Bounder`, che dice «ancora più
**veloce**» — la parola esatta non c'era. Corretto il termine cercato, non la resa.

## 7. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 12 unità `PENDING`.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Il file resta aperto**: 12/29; restano **17 unità**, tutte `DESCRIPTION` (`Leviathan`, `Manta`, `Quicksilver`…).
