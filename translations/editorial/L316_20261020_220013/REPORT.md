# REPORT — L316 (`data/coalition/coalition ships.txt`, righe 59–969)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **23 controlli**; `verify.py` esce 0 con **20 controlli**. Il file è a **10/27
(37,0%)**. `state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 10 (`DESCRIPTION`) | 10 |
| parole | 473 | **496** (1,049) |
| tab | **1** | **1** |
| virgolette | 0 | 0 |
| segnaposto / alternative | 0 / 0 | **0 / 0** |
| apici | **2** | 9 |

Rapporto per unità **0,94 – 1,22**: lotto regolare; il minimo (riga 275) è la scheda dello `Spindle`, dove l'italiano **recupera**
spazio con «una volta tolti i pod laterali» invece di `with its side pods removed`.

## 2. Invariante di segmento (il file non è finito)

```
PRIMA     zero unità prima della 59: il lotto APRE il file
QUI       10 unità, righe distinte 59–969
DOPO      17 unità / 632 parole (la prossima alla 1141)
COPERTURA 10/27 (37,0%) — STAMPATA, non asserita
```

## 3. Due civiltà, due estetiche

Il lotto si divide esattamente a metà e le due metà **si specchiano**:

| | **Arach** | **Heliarch** |
|---|---|---|
| valori | **funzionalità efficiente come bellezza** («brutto ma utilitario») | **potenza e resistenza** (il caccia prima impossibile, ora sperimentale) |
| materiali | scafi che durano **secoli**, pod intercambiabili, case ricavate dai cargo | **matrice di scudi**, integrità dello scafo, raggi trattori |
| tono | **commerciale**, familiare, con le **Casate** e i patroni | **militare**, con i **dissidenti** e l'ira degli Heliarch |
| nave-bandiera | il `Transport`, «superato rispetto alle più recenti navi militari Heliarch» | il `Judicator`, appena costruito |

Il **`Transport`** è il ponte fra le due: è la nave con cui gli Arach **rovesciarono i Quarg** e conquistarono i **mondi ad anello**,
e la sua scheda dice che oggi è **superata** — la stessa frase che apre l'obsolescenza Arach di fronte alla tecnologia Heliarch.

## 4. La riga 275: una scheda che parla di un'altra nave

```
200  ship:Arach Hulk      → descrive il Hulk
275  ship:Arach Spindle   → «The Arach Hulk is an ungainly…» e poi spiega lo Spindle
```

Il test **non** pretende che il nome del contesto compaia nel testo: verifica la **relazione fra i due contesti** (`at[275]` cita il
`Hulk`, `at[200]` **è** il `Hulk`). È il tipo di errore che un controllo ingenuo («il nome del contesto è nel testo») avrebbe
segnalato come **falso positivo** su una traduzione corretta.

## 5. Il `Coalition` → «Coalizione»

Misura sul corpus: **291** unità rendono `Coalition` con «Coalizione», **3** lo lasciano in inglese. La resa segue la maggioranza e
il test **verifica l'assenza** di `Coalition` nel testo italiano della riga 383. I nomi delle **navi** invece restano invariati.

## 6. Verifica

```
check.py   23 controlli · FAIL totale: 0 · exit 0
verify.py  20 controlli · FAIL: 0 · exit 0
copertura  10/27 (37,0%) — stampata, non asserita
```

**Nessun rosso**: primo giro verde, con le tre trappole del contratto (contesto 275, `Judicator` doppio, tab unica) **previste prima**
di scrivere.

## 7. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 10 unità `PENDING`; il lotto è **in staging**.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **I numeri di targa** (scudi, resistenza, stiva) **non** sono nel testo: le schede sono **descrittive**, e il test verifica solo le
  parole.
- **Il file non è finito**: 10/27; restano **17 unità / 632 parole**.
