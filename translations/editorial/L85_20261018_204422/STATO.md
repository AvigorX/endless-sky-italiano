# STATO — L85 · `data/successors/predecessors.txt` — **ULTIMO LOTTO, CHIUDE IL FILE**

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L85_20261018_204422` |
| Righe / unità | **648–782** (finestra 621–800) / **7** |
| Tipi | **7 `DESCRIPTION`** — nessun tipo di dato |
| Contesti | **7**, uno per unità (`"Tijra" Heirloom Lance` … `Stolen Cloak (Deactivated)`) |
| Parole | 250 EN → 258 IT (1,032); per unità 1,07–1,15 |
| Tab · virgolette | **0** · **4** (0 dispari) |
| Token · duplicati | **0 = 0** · **0** |
| sha256 | `3fad23a16aeaa834…` |
| `check.py` | **21 controlli**, `FAIL totale: 0` |
| `verify.py` | **29 controlli**, exit **0** |

## Invariante di FILE

| Voce | Valore |
|---|---|
| Unità prima della riga 648 | **52** (L81–L84) |
| Unità dopo la riga 782 | **0** |
| File | **59 unità**, `max(line) = 782` |
| Copertura | **59/59 (100%)** — 59 id distinti, 59 righe |
| Lotti | **5** — L81 (22), L82 (15), L83 (11), L84 (4), L85 (7) |
| Parole del file | **898 EN → 927 IT** |

`predecessors.txt` è il **trentacinquesimo file completo**, **non approvato**: 59 unità `PENDING`.

## Contenuto e decisioni

Sette schede di equipaggiamento dei Predecessori: il **cannone a bobina** più grande («una frazione
considerevole della velocità della luce», capace di distruggere «una piccola città o, in alternativa, una
grande nave da guerra»); il **reattore** dei Myiara, «una macchina aggraziata ed elegante, facile da
scambiare per una scultura»; la **batteria** che immagazzina energia nei «vuoti quasi innumerevoli di una
schiuma di metallo stellare»; il **raffreddamento**, che le attrezzature moderne non rendono più necessario; il
**generatore di scudi** «lucido fino a brillare per oltre mille anni»; il **congegno** di cui Resja parla come
di un vuoto che «si allarga a ogni battito di ciglia»; il **dispositivo di occultamento rubato a Casa Kaatrij**,
«temporaneamente disattivato da un congegno rilevatore».

Scelte: «coilgun» → **cannone a bobina** (come L82/L84); `cortex` resta `cortex`; `House Kaatrij` → **Casa
Kaatrij**; `Myiara` invariato. Le due grafie `Valkkyiara-Khorasaqran`/`-Khorasaqra` restano come nel sorgente.

## Verifica

```bash
cd staging/editorial/L85_20261018_204422
python check.py   # FAIL totale: 0
python verify.py  # exit 0 (invariante di file)
```
