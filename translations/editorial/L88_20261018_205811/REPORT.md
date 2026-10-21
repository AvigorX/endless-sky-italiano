# REPORT — L88 · `data/successors/successor outfits.txt`

## 1. Contenuto

Dieci `DESCRIPTION` in sette contesti, tutte sui propulsori dei Successori: `Aqra` (spinta e retro), `Chyyra`
(spinta, manovra, retro, «anche le navi grandi e apparentemente pesanti diventano più agili quando sono
minacciate»), `Veusa` (i più grandi, per navi da guerra e mercantili, con il consumo rapido degli scudi e il
riferimento ai **Successori invertebrati**).

## 2. Scelte

| nodo | scelta | perché |
|---|---|---|
| `reverse thruster` (×3) | **propulsore di retro** | una sola resa per tre occorrenze identiche |
| `steering engines/units` | **propulsori / unità di manovra** | coerente con L87 |
| `pulsed inductive thrusters` | **propulsori induttivi pulsati** | `pulsed` distingue la serie `Veusa` |
| `ion thrusters` | **propulsori ionici** | termine corrente |
| `lumbering` | **pesanti** | già reso così in L84 (navi «più pesanti») |
| `invertebrate Successors` | **Successori invertebrati** | dato biologico dichiarato nel testo |
| `g-force stress` | **sollecitazioni da forza g** | non «stress», che in italiano è psicologico |

## 3. Difficoltà

1. **Duplicato inglese su tre unità** (2, 6, 10): non è un errore del sorgente, è lo stesso avviso ripetuto per
   ogni propulsore di retro. Reso **identico** e asserito; `check.py` elenca il gruppo, `verify.py` pretende
   l'identità.
2. **Tre tab** (2, 6, 10) coincidono con le tre unità duplicate.
3. **Zero virgolette**: dichiarato come assenza, non come conteggio implicito.
4. **Directory sbagliata di nuovo**: avevo scritto parte e script in una cartella con timestamp diverso
   dall'export; spostati nella directory reale, la vuota rimossa.

## 4. Numeri osservati

```
unita' 10/10 · tab 3 (2,6,10) · virgolette 0 · token 0
rapporto 0.91 - 1.19 · parole EN 329 -> IT 343 · righe 429/560
duplicato legittimo 2/6/10 identico
FAIL totale: 0 (24 controlli) · verify exit 0 (24 controlli)
sha256[:16] 40dafd350a29f440
```

## 5. Stato del progetto

```
TOTALE staging: 24861 unita · 791992 EN · 750949 IT
successor outfits.txt: 44/56 (78,6%) · 1922 EN -> 1976 IT · 3 lotti
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | parte, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (24 controlli) **e** `verify.py` exit **0** (24 controlli) |
