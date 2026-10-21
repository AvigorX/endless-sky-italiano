# REPORT — L190 · `gegno outfits.txt`

## 1. Contenuto

Un lotto di **una sola riga**, la licenza `Scin Adjutant License`, che chiude il file. Nasce perché L189 si è fermato a 1130: il residuo era di 23 parole, e un lotto di una unità è comunque un lotto con due script a exit code.

| blocco | unità | righe | contenuto |
|---|---|---|---|
| licenza Scin | 1 | 1137 | l'accesso alla «tecnologia più elementare» degli Scin |

## 2. Scelte

| nodo | IT | unità |
|---|---|---|
| Productive acts perpetrated by you | **Gli atti produttivi che hai compiuto** | 1 |
| raised the interests of the Gegno Scin | **hanno suscitato l'interesse dei Gegno Scin** | 1 |
| their most basic technology | **la loro tecnologia più elementare** | 1 |

## 3. Difficoltà

1. **Una sola unità non giustifica un controllo più debole**: 16 controlli nel `check.py`, 18 nel `verify.py`, compreso l'**invariante di FILE** sulle sei finestre L185…L190 (60/60 unità su 60 righe distinte).
2. **0 apici inglesi, 1 italiano** (`l'interesse`): anche su una riga la differenza fra le lingue va misurata, non assunta — l'asserzione «zero apici in entrambe» è stata bocciata e corretta.
3. Il `verify.py` ha richiesto tre correzioni di forma (parentesi sbilanciata, `v['italian']` su una lista di sole unità inglesi): gli errori erano negli script, non nella resa.

## 4. Numeri osservati

```
unita' 1 · 1 DESCRIPTION · tutte PENDING
token 0 · 0 tab · 0 virgolette · 0 apici EN · 1 apici IT
1 testi distinti · 1 contesti · righe 1137
parole 23 -> 22 · rapporto 1.02 - 1.02, media 1.02
FAIL totale: 0 (16 controlli) · verify exit 0 (18 controlli) · sha256[:16] 13766cd38ed4be40
```

## 5. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (16 controlli), `verify.py` exit **0** (18 controlli) |

## 6. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 1 unità `PENDING`.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**, **nessuna revisione umana**.
