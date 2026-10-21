# REPORT — L169 · `paradise world jobs.txt` (terzo lotto)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| turisti di lusso | 1-4 | 376-414 | due missioni con lo **stesso testo** in contesti diversi; i passeggeri si disperdono delusi |
| crociera di piacere | 5-8 | 419-447 | scorta al `<npc>` con `<tons>` di `<commodity>`, tappa obbligata, ritorno |
| passeggeri | 9-17 | 453-522 | liberati sulla parola (`secure ship`), debitori con «si rendano utili», pensionati con gli aneddoti |

## 2. Scelte

| nodo | IT | unità |
|---|---|---|
| `outrageously wealthy` | **sfacciatamente ricchi** | 1, 3 |
| `sporting puzzled looks` | **con l'aria perplessa** | 2, 4 |
| `pleasure cruise` | **crociera di piacere** | 5 |
| `bedecked in ... tourist attire` | **agghindati con ... abbigliamento da turista** | 6 |
| `community service sentences` | **condanne ai lavori socialmente utili** | 10 |
| `secure ship` | **nave sicura** | 10 |
| `job service provider` | **fornitore di servizi per il lavoro** | 14 |
| `travel broker` | **agente di viaggio** | 17 |

## 3. Difficoltà

1. **`<npc>`** (4): un segnaposto che il motore sostituisce con il nome di una nave. Sembra un nome proprio, non lo è:
   resta identico, e 4 controlli lo verificano (multiset, ordine per unità, presenza in idx 5/6/7/8, nessun `<npc> nomedelnpc`).
2. **Due coppie di testi identici** (1/3 e 2/4) in contesti diversi (`tourists` vs `tourist group`): la resa deve essere
   identica, e un controllo lo pretende.
3. **Apici e virgolette**: `'appropriate facilities'` (2 apici) e `"make themselves useful."` (2 virgolette).
4. **Errore in corsa (mio)**: avevo scritto un controllo che pretendeva **lo stesso numero di apici** in inglese e in
   italiano. L'inglese ne ha **3** (`They'll` + la frase fra apici), l'italiano **2**, perché la contrazione sparisce in
   «Considereranno». Il controllo era sbagliato, la resa no: riscritto pulito, e annotato che i conteggi di apici **non**
   devono coincidere fra le due lingue.
5. **Confine misurato**: riga 526 = **`VALUE`** (terza volta che un confine è un `VALUE`: L164, L167, L169).
6. **Gate**: 0,90–1,24, media 1,05 — il lotto più stretto finora.

## 4. Numeri osservati

```
unita' 17 · 3 VALUE · 6 DESCRIPTION · 8 DIALOG · tutte PENDING
token 38 su 8 simboli · <npc> 4 (segnaposto) · 0 tab · 2 virgolette · 2 apici
15 testi distinti · 6 contesti · righe 376/522
parole 493 -> 505 (1.024) · rapporto 0.90 - 1.24, media 1.05
FAIL totale: 0 (26 controlli) · verify exit 0 (22 controlli) · sha256[:16] 150e46846747c2d3
```

## 5. Stato del progetto (dopo L169)

```
TOTALE staging: 28065 unità · 884111 EN · 840856 IT
paradise world jobs.txt: 69/131 (52,7%) · 3 lotti
residuo traducibile (formula state.py): 3865
endless-sky HEAD b4aa3bac3, 0 modifiche
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (26 controlli), `verify.py` exit **0** (22 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 17 unità `PENDING`.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Terzo lotto del file**: contratto successivo in `HANDOFF_L170_20261019.md`.
