# REPORT — L159 · `weapons.txt` (siluri, Typhoon e razzi pesanti)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| siluri | 1-10 | 1263-1390 | `Javelin Turret`, `VALUE` `Torpedoes`, munizione, rack, lanciatore, pod |
| Typhoon | 11-18 | 1414-1521 | `VALUE` `Typhoon Torpedoes`, munizione, tubo, lanciatore, pod |
| razzi pesanti | 19-22 | 1552-1601 | munizione, rack, `Heavy Rocket Launcher` |

## 2. Scelte

| nodo | IT | unità |
|---|---|---|
| `Torpedoes` · `Typhoon Torpedoes` | **identici** (2 `VALUE`) | 3, 11 |
| `torpedoes` (prosa) | **siluri** | 4, 6, 8, 9 |
| `capital ships` | **navi capitali** | 6, 14 |
| `proximity trigger` | **detonatore di prossimità** | 21 |
| `blast radius` | **raggio d'esplosione** | 21 |
| `Heavy Rockets are…` | **I Heavy Rocket sono…** | 19, 21 |

## 3. Difficoltà

1. **Sei copie** della riga munizioni nello stesso lotto, più il riuso da L157/L158: un solo controllo per tutte e tre le cose.
2. **idx 8 è un prefisso di idx 6**, non una stringa uguale: si verifica come sotto-stringa (`startswith`), mai come uguaglianza.
3. **Errore in corsa**: avevo asserito 15 testi inglesi distinti; il dato dice **16** (22 − 6 copie + 1 − 1 duplicato). Corretto a 16 in `check.py` e `verify.py` dopo averlo misurato.

## 4. Numeri osservati

```
unita' 22 · 20 DESCRIPTION · 2 VALUE · tutte PENDING
token 0 (asserzione vuota) · 8 tab · 0 virgolette
16 testi distinti · 12 contesti · tab 8 · virgolette 0
parole 576 -> 593 (1.030) · rapporto 0.96 - 1.27
righe 1263/1601
FAIL totale: 0 (25 controlli) · verify exit 0 (20 controlli) · sha256[:16] 9e0b0c5d6a3f6cd3
```

## 5. Stato del progetto (dopo L159)

```
TOTALE staging: 27920 unità · 878997 EN · 835443 IT
residuo traducibile (formula state.py): 4010
file completi: 51
endless-sky HEAD b4aa3bac3, 0 modifiche
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (25 controlli), `verify.py` exit **0** (20 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 22 unità `PENDING`.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Lotto del batch L154–L160**: contratto = piano del batch, nessun `HANDOFF_L159` separato.
