# REPORT — L170 · `paradise world jobs.txt` (quarto lotto)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| pensionati | 1-7 | 526-574 | `"pensionati"` ricercati, multa modesta, fonte anonima del pagamento |
| ritiro | 8-10 | 578-599 | `"Ritiro nella Natura"`, guide comiche, il sospetto del reality show |
| cantieri | 11-18 | 603-668 | quattro consegne, due a Gemini Shipyards |
| Martini | 19-20 | 690-691 | la famiglia evacuata dopo il bombardamento nucleare |

## 2. Scelte

| nodo | IT | unità |
|---|---|---|
| `no-questions-asked transport` | **trasporto ... senza domande** | 2, 6 |
| `self-proclaimed retirees` | **pensionati autoproclamati** | 4, 7 |
| `if raucous` | **anche se chiassosi** | 4, 7 |
| `a small fine` | **una multa modesta** | 3 |
| `pseudo-celebrities` | **pseudo-celebrità** | 9 |
| `safely fleeced of their money` | **alleggerite dei loro soldi senza correre rischi** | 10 |
| `constituent of the Republic Navy Yard` | **costola del Republic Navy Yard** | 12, 14 |
| `respected` → `well-respected` | **ben considerato** | 16 |

## 3. Difficoltà

1. **12 virgolette** (record della campagna), in 5 unità: si verificano **per unità**, non sul totale.
2. **Sei testi ripetuti** in contesti diversi: `Wealthy retirees to <planet>` (1/5), la `DESCRIPTION` (2/6), la
   `DESCRIPTION` dei cantieri (12/14), e **quattro** `Shipment to <planet>` (11/13/15/17). Un controllo pretende che la
   resa sia **una sola** per ciascun gruppo.
3. **Il refuso `anyonymous` in idx 7**: fedeltà al sorgente **senza propagarlo** — la resa italiana resta quella di idx 4.
4. **`<martini house>`**: segnaposto composto, una volta, nell'ultima unità. Verificato intero.
5. **Nomi propri inglesi**: `Gemini Shipyards`, `Lovelace Labs`, `Polymath Nanoinstruments`, `Republic Navy Yard`.
6. **Confine misurato**: riga 719 = **`VALUE`** (quarta volta su quattro quando misurato).
7. **Gate**: 0,95–1,16, media **1,00** — il più compatto della campagna.

## 4. Numeri osservati

```
unita' 20 · 8 VALUE · 8 DESCRIPTION · 3 DIALOG · 1 MISSION_TEXT · tutte PENDING
token 39 su 7 simboli · <martini house> 1 · 0 tab · 12 virgolette
14 testi distinti · 8 contesti · righe 526/691
parole 496 -> 516 (1.040) · rapporto 0.95 - 1.16, media 1.00
FAIL totale: 0 (27 controlli) · verify exit 0 (23 controlli) · sha256[:16] 900e58542d06ef12
```

## 5. Stato del progetto (dopo L170)

```
TOTALE staging: 28085 unità · 884607 EN · 841372 IT
paradise world jobs.txt: 89/131 (67,9%) · 4 lotti
residuo traducibile (formula state.py): 3845
endless-sky HEAD b4aa3bac3, 0 modifiche
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (27 controlli), `verify.py` exit **0** (23 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 20 unità `PENDING`.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Quarto lotto del file**: contratto successivo in `HANDOFF_L171_20261019.md`.
