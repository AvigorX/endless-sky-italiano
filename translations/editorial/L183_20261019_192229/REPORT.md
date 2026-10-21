# REPORT — L183 · `human outfits.txt` (quarto lotto)

## 1. Contenuto

Quindici unità in tre registri: schede tecniche (alloggi di lusso, pod di carburante, placcatura anti-scansione, fucili
laser, barricata, gas nervino), **una battuta** (il `Mug`: «Puoi lanciarlo in caso di necessità, supponi») e **un
mistero** (la spada dell'`Old Man's Sword`).

## 2. Scelte

| nodo | IT | unità |
|---|---|---|
| `a certain amount of passenger discomfort` | **una certa dose di disagio per i passeggeri** | 2 |
| `better paying class of passenger` | **disposta a pagare meglio** | 2 |
| `one additional hyperspace jump` | **un salto nell'iperspazio in più** | 3 |
| `evading detection` | **sfuggire al rilevamento** | 4 |
| `sidearms` | **armi corte** | 5 |
| `defensible choke points` | **punti di strozzamento difendibili** | 7 |
| `barricade` | **barricata** | 8 |
| `banned by interstellar law` | **vietate dal diritto interstellare** | 10 |
| `marginalmente more effective` | **marginalmente più efficace** | 14 |
| `old curios and commemorative objects` | **vecchie curiosità e oggetti commemorativi** | 15 |

## 3. Difficoltà

1. **Quattro `VALUE`**, fra cui `Antigrav Glasses` **plurale** mentre il contesto è `Antigrav Glass` singolare: il nome si
   copia com'è, il contesto non si tocca. Il controllo verifica entrambi.
2. **Un errore in corsa (mio)**: l'asserzione sui contesti diceva «`Antigrav Glass` con 2 unità». Sono **3** (il nome e due
   descrizioni). La distribuzione misurata è **3 + 2 + 2 + 2 + sei con 1** = 15. Corretto con il valore del `Counter`.
3. **I tre punti del gas nervino**: il testo inglese finisce con `...`. In italiano ho tenuto i **tre punti ASCII**, non
   l'ellissi tipografica `…` — e il `check.py` lo verifica, perché è il tipo di dettaglio che una passata tipografica
   «sistemerebbe» introducendo un carattere che il resto della campagna non usa.
4. **La battuta del `Mug`**: resa in 8 parole, con il controllo che **non** superi le 10 — una battuta spiegata smette di
   essere una battuta.
5. **Nessun possessivo inglese** nel lotto: i 3 apici sono tutti elisioni (`you're`, `you've`, `don't`), e in italiano
   **nessun** apice sopravvive come possessivo.
6. **Gate**: 0,94–1,25, media 1,07. Le parole calano di 3 (474 → 471).

## 4. Numeri osservati

```
unita' 15 · 11 DESCRIPTION · 4 VALUE · tutte PENDING
token 0 · 1 tab (14) · 0 virgolette · 3 apici EN (elisione, nessun possessivo)
15 testi distinti · 10 contesti (3 + 2 + 2 + 2 + sei con 1) · righe 390/514
parole 474 -> 471 (0.994) · rapporto 0.94 - 1.25, media 1.07
FAIL totale: 0 (27 controlli) · verify exit 0 (20 controlli) · sha256[:16] c98a702886a3b041
```

## 5. Stato del progetto (dopo L183)

```
TOTALE staging: 28279 unità · 889892 EN · 846828 IT
human outfits.txt: 50/63 (79,4%) · 4 lotti — restano 13 unità
residuo traducibile (formula state.py): 3651
residuo misurato: 4320 unità / 87212 parole su 111 file
endless-sky HEAD b4aa3bac3, 0 modifiche
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (27 controlli), `verify.py` exit **0** (20 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 15 unità `PENDING`.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Quarto lotto del file**: restano **13 unità**, e **L184 chiuderà `human outfits.txt`**.
