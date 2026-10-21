# REPORT — L187 · `gegno outfits.txt`

## 1. Contenuto

Il lotto più **corto** della serie per numero di unità (7) ma con 453 parole: quattro schede su sette superano le 60 parole.

| blocco | unità | righe | contenuto |
|---|---|---|---|
| cannoni Vi | 1-6 | 459-728 | `Irate` → `Choleric` → `Ballistic`, ognuno con la sua torretta |
| batteria Scin | 7 | 728 | la `Astuit Battery`, «simile agli Energy Blasters umani» |

## 2. Scelte

| nodo | IT | unità |
|---|---|---|
| rudimentary cannon technology | **tecnologia di cannoni rudimentale** | 1 |
| condensed scrap metal | **rottami metallici compressi** | 1 |
| doubling its rate of fire in a single mount | **raddoppiando la cadenza di tiro in un solo supporto** | 2 |
| barely enough to output any sort of meaningful damage | **basta a malapena a produrre un danno significativo** | 1 |
| a deadly wall of fire | **una letale muraglia di fuoco** | 5 |
| self-sustaining base with its own vent ports | **base enorme e autosufficiente, con i propri sfiati** | 6 |

## 3. Difficoltà

1. **L'incoerenza del sorgente si conserva**: il contesto è `outfit:Astuit Battery` ma il testo parla di **`Astuit Blasters`** (quattro su una torretta). Non è un refuso del lotto: è il dato, e il controllo lo pretende.
2. **7 unità, 7 contesti**: una scheda per arma, nessuna ripetizione da verificare.
3. **Zero `VALUE`** (asserzione scritta) e **4 apici** tutti possessivi.

## 4. Numeri osservati

```
unita' 7 · 7 DESCRIPTION · tutte PENDING
token 0 · 0 tab · 0 virgolette · 4 apici EN · 3 apici IT
7 testi distinti · 7 contesti · righe 459/728
parole 453 -> 469 · rapporto 1.02 - 1.17, media 1.1
FAIL totale: 0 (23 controlli) · verify exit 0 (21 controlli) · sha256[:16] 6b36e485ac98788b
```

## 5. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (23 controlli), `verify.py` exit **0** (21 controlli) |

## 6. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 7 unità `PENDING`.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**, **nessuna revisione umana**.
