# REPORT — L189 · `gegno outfits.txt`

## 1. Contenuto

Il lotto delle **armi da abbordaggio** e delle **licenze**: quattro armi corpo a corpo e poi sei permessi che salgono di rango, scritti in seconda persona («Sei stato accettato…»).

| blocco | unità | righe | contenuto |
|---|---|---|---|
| armi da abbordaggio | 1-5 | 1034-1077 | `Savagery Pike`, `Irate Carronade`, `Plasmasickle`, `Plasma Grenades` |
| licenze Gegno | 6-7 | 1088-1095 | civile e trivellatore |
| licenze Vi | 8-10 | 1102-1116 | `Lord`, `Centurion`, `Evocati` |
| licenze Scin | 11-12 | 1123-1130 | `Hoplologist`, `Architect` |

## 2. Scelte

| nodo | IT | unità |
|---|---|---|
| ceremonial spear-like weapon | **arma cerimoniale simile a una lancia** | 1 |
| haphazardly shoving them into small makeshift barricades | **infilarli alla bell'e meglio in piccole barricate improvvisate** | 2 |
| will likely become a new paint layer on the nearby walls | **probabilmente diventerà un nuovo strato di vernice sulle pareti vicine** | 2 |
| less of a hazard than unpredictable fragmentation grenades | **meno pericolose delle imprevedibili granate a frammentazione** | 5 |
| a titular Gegno citizen | **cittadino Gegno titolare** | 6 |
| invaluable asset for their ambitions | **risorsa inestimabile per le loro ambizioni** | 8 |
| a successful user of judgment | **abile utilizzatore del giudizio** | 9 |

## 3. Difficoltà

1. **Le sei licenze sono un unico registro**: seconda persona, participio passato, ricompensa. Il controllo pretende le marche della seconda persona in **tutte** e sette le frasi che le contengono.
2. **`Plasma Grenades` è l'unico `VALUE`** (idx 4) e resta inglese; in prosa la sostanza è «plasma», non «granata al plasma» come nome.
3. **11 apici italiani** contro **6** inglesi: le elisioni italiane (`all'estremità`, `l'accesso`, `un'arma`) non hanno nulla a che vedere con i possessivi inglesi.

## 4. Numeri osservati

```
unita' 12 · 11 DESCRIPTION · 1 VALUE · tutte PENDING
token 0 · 0 tab · 0 virgolette · 6 apici EN · 11 apici IT
12 testi distinti · 11 contesti · righe 1034/1130
parole 443 -> 472 · rapporto 0.97 - 1.18, media 1.07
FAIL totale: 0 (23 controlli) · verify exit 0 (21 controlli) · sha256[:16] ad29d24c33d43d52
```

## 5. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (23 controlli), `verify.py` exit **0** (21 controlli) |

## 6. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 12 unità `PENDING`.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**, **nessuna revisione umana**.
