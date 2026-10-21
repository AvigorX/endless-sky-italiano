# STATO — L316 (`data/coalition/coalition ships.txt`, righe 59–969)

**Stato: CHIUSO.** Primo lotto del file: **10 unità su 27** (**37,0%**). `check.py` esce 0 con **23 controlli**; `verify.py` esce 0
con **20 controlli**. `state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

| voce | valore |
|---|---|
| directory | `staging/editorial/L316_20261020_220013/` |
| file | `data/coalition/coalition ships.txt` (27 unità · 1.105 parole · 27 `DESCRIPTION`) |
| righe | 59–969 |
| unità | **10** — tutte `DESCRIPTION` |
| contesti | **9** — 5 navi **Arach** + 4 **Heliarch** (il `Judicator` è doppio) |
| parole | **473 EN → 496 IT** (1,049) |
| rapporto | **0,94 – 1,22** |
| tab | **1** — riga **969**, primo carattere |
| virgolette | **0** |
| segnaposto / alternative | **0 / 0** |
| apici | **2 EN / 9 IT** |
| `check.py` | **23 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **20 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: **0 prima** (il lotto apre il file) · 10 qui · **17 dopo** (la prossima alla 1141) |
| copertura | **10/27 (37,0%)** — **stampata, non asserita** |
| `sha256[:16]` | **`223f6b9e162366d6`** |

## Comandi

```bash
python staging/editorial/L316_20261020_220013/check.py     # FAIL totale: 0 (23 controlli)
python staging/editorial/L316_20261020_220013/verify.py    # FAIL: 0 (20 controlli, 10/27)
```

## Le nove navi

| riga | contesto | che cosa racconta |
|---|---|---|
| 59 | `Arach Courier` | il **cargo piccolo** dei giovani Arachi; chi nasce in una **Casata** si fa comprare una nave più grande |
| 125 | `Arach Freighter` | scafi **leggendari**: un cargo non più spaziale diventa **casa** su un pianeta e dura **secoli** |
| 200 | `Arach Hulk` | «la **funzionalità efficiente** è la più alta forma di bellezza»: **brutto ma utilitario**, con **pod laterali staccabili** |
| 275 | `Arach Spindle` | **parla del Hulk** (vedi sotto) e spiega perché una flotta porta uno Spindle |
| 383 | `Arach Transport` | il **progetto più antico**: dalla cacciata dei Quarg e dai **mondi ad anello** all'obsolescenza militare |
| 461 | `Heliarch Breacher` | poco resistente ma **veloce in avanti**: ideale per il **volo radente** |
| 588 | `Heliarch Hunter` | oggi **pattugliatore**, un tempo cacciatore di **dissidenti** |
| 779 | `Heliarch Interdictor` | **raggi attrattori e repulsori** che impediscono l'**aggancio iperspaziale** |
| 968–969 | `Heliarch Judicator` | **due unità**: la storia dei caccia Heliarch e la scheda tecnica (**sei baie di caccia**, cuccette, **nave logistica**) |

## Le tre trappole del contratto, verificate

1. **la riga 275 è `Arach Spindle` ma descrive il `Hulk`** — il test verifica la **relazione fra contesti**: `at[275]` parla del
   `Hulk` e `at[200]` è il `Hulk`;
2. **il `Judicator` ha due unità** (968 + 969) e **entrambe stanno dentro** il lotto: nessuna nave spezzata fra due lotti;
3. **una sola tab**, riga **969**, come **primo carattere**.

## Cosa il test pretende

| oggetto | verifica |
|---|---|
| contesti | 9 su 10 unità; `Judicator` = 2, tutti gli altri 1 |
| nomi | `Arach …`, `Breacher`, `Hunter`, `Interdictor`, `Judicator` **invariati** dove compaiono |
| `Coalition` | → **«Coalizione»** (corpus: **291** occorrenze contro 3) |
| tecnica | pod laterali, volo radente, raggi attrattori/repulsori, aggancio iperspaziale, sei baie di caccia, cuccette |
| vuote | 0 virgolette, 0 segnaposto, 0 alternative |
| apici | **2** in inglese, righe **461** e **968** |

## Limiti dichiarati

Nessuna approvazione (10 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. **Il file non è finito**: restano
**17 unità / 632 parole** (righe 1141–2195), che lo chiudono in **L317**.
