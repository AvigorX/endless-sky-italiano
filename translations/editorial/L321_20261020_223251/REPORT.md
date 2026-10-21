# REPORT — L321 (`data/wanderer/wanderer outfits.txt`, righe 463–659) — **LOTTO TERMINALE**

**Esito: lotto CHIUSO, file CHIUSO a 31/31.** `check.py` esce 0 con **21 controlli**; `verify.py` esce 0 con **19 controlli**.
`state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 13 (`DESCRIPTION`) | 13 |
| parole | 514 | **547** (1,064) |
| tab | **0** | **0** |
| virgolette | **0** | **0** |
| segnaposto / alternative | 0 / 0 | **0 / 0** |
| apici | **3** (2 unità) | 5 |

Rapporto per unità **0,95 – 1,27**. Il minimo è la riga 638 («È il più grande sistema di timone che i Wanderer vendano», 0,95): una
frase **corta** che in italiano resta corta. Il massimo è la 477 (1,266), dove `ancillary cooling is unnecessary` diventa «il
raffreddamento ausiliario è inutile» e l'articolo pesa.

## 2. Invariante di FILE

```
FILE        31/31 (100%) · somma lotti 18 (L320) + 13 (L321) = 31
RIGHE       31 distinte · prima 40 · ultima 659 · zero dopo
```

`data/wanderer/wanderer outfits.txt` è il **trentacinquesimo** file chiuso nel progetto (**94** su 167).

## 3. Il lotto spiega **una sola meccanica** in otto modi

I Wanderer hanno risolto un problema — **il calore** — con **tre verbi** diversi, e ogni scheda ne illumina un lato:

| verbo inglese | resa | che cosa aggiunge |
|---|---|---|
| `radiating excess heat` | **irradiando** | il calore esce **come radiazione** |
| `transferring … into the exhaust plasma` | **trasferendo … al plasma di scarico** | il calore **finisce nello scarico**, cioè è **espulso con la spinta** |
| `vent extra heat` | **espellere il calore in eccesso** | il calore è **buttato fuori** attivamente |

Se avessi reso tutti e tre con «dissipare», le otto schede avrebbero detto **la stessa cosa otto volte** e il giocatore non avrebbe
capito **perché** conviene un motore grande (raffredda **anche mentre spinge**) rispetto a un timone (raffredda **anche da fermo**).

E c'è la progressione implicita, che il testo dà e la resa conserva:

```
Type 1  «il più piccolo motore»      → raffredda perché irradia
Type 4  «il più grande»              → raffredda «anche mentre è in funzione»
Type 2 Steering  «anche quando non è in uso»
```

## 4. I numeri sono nomi

`Type 1..4 Radiant Thruster` e `Type 1..4 Radiant Steering` restano **identici all'inglese**. Il test verifica i **quattro contesti
esatti** di ciascuna scala: non «piccolo/medio/grande/massimo». Motivo pratico: sono le **etichette dell'emporio**, e un giocatore che
cerca «Type 3 Radiant Steering» deve trovarlo.

## 5. Le licenze: tre oggetti, tre diritti, una storia

| riga | oggetto | diritto | tono |
|---|---|---|---|
| 645 | **piatto** con semi di `Sentinel Skirtgrass` (con **limite generazionale**) | **equipaggiamenti** | **speranza**: i semi spariscono da soli per non invadere la flora locale |
| 652 | **ramo** del `Noble Watchwood` in **ambra** | **navi non militari** | **orgoglio**: l'albero è fragile, e la sua maturità è «segno di un ecosistema risanato» |
| 659 | lo **stesso ramo**, **rinsecchito**, in **bronzo** | **navi da guerra** | **lutto**: «quando la pace fallisce, anche loro devono prepararsi a combattere» |

Il terzo è il **rovescio** del secondo: lo stesso albero, non più vivo. La resa tiene la **parentela** («il loro emblema più caro») e
non la spiega, perché il testo non la spiega — la **mostra**.

## 6. Verifica

```
check.py   21 controlli · FAIL totale: 0 · exit 0
verify.py  19 controlli · FAIL: 0 · exit 0
FILE       31/31 (100%) · trentacinquesimo file completo
```

**Nessun rosso**: primo giro verde, con le asserzioni **vuote dichiarate** (0 tab, 0 virgolette, 0 segnaposto, 0 alternative): un file
che finisce **senza** nota dei rifornimenti è un fatto, e va scritto, non omesso.

## 7. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 13 unità `PENDING`; il file è **finito in staging**, non approvato.
- **Nessun testo visto nel gioco**: le tre licenze e i loro **diritti** sono verificati **nei dati**; che il gioco li conceda davvero
  dipende dal codice, non dal testo.
- **La botanica è quella del sorgente**: `Sentinel Skirtgrass` e `Noble Watchwood` restano **invariati**; nessuna verifica che siano
  specie plausibili.
