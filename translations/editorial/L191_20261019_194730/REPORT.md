# REPORT — L191 · `bunrodea missions.txt`

## 1. Contenuto

L'esordio della missione: l'invito, l'incontro notturno sulla pista di <origin>, le tre battute di dialogo e il dispositivo che proietta una mappa stellare.

| blocco | unità | righe | contenuto |
|---|---|---|---|
| invito e arrivo | 1-2 | 16-17 | il `VALUE` «An Intriguing Invitation» e l'invito nel sistema indicato |
| l'incontro notturno | 3-4 | 38-39 | due mantidi armati, uno con modifiche cibernetiche |
| le tre battute | 5-7 | 41-43 | pace, incomprensione, resa |
| il dispositivo | 8-12 | 44-52 | la mappa olografica e le due varianti (raccogliere o schivare) |

## 2. Difficoltà

1. **1 segnaposto `<origin>`** da conservare alla lettera (idx 3), in inglese e in italiano.
2. **6 virgolette di dialogo** (idx 5, 6, 7) e **9 tab**: le virgolette sono diritte, mai caporali.
3. **Le due varianti 11 e 12** condividono la seconda metà (mappa, sistema evidenziato, partenza) e la resa deve coincidere: il controllo confronta le due stringhe.
4. Un'asserzione sbagliata (mia): il controllo pretendeva `(Schivi` mentre l'imperativo corretto è **Schiva**.

## 3. Numeri osservati

```
unita' 12 · {'VALUE': 1, 'DESCRIPTION': 1, 'MISSION_TEXT': 10} · tutte PENDING
9 tab · 6 virgolette · 13 apici EN · 6 apici IT
12 testi distinti · 1 contesto · righe 16/52
parole 466 -> 434
FAIL totale: 0 (25 controlli) · verify exit 0 (21 controlli) · sha256[:16] a1c782a568e872ed
```

## 4. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (25 controlli), `verify.py` exit **0** (21 controlli) |

## 5. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 12 unità `PENDING`.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**, **nessuna revisione umana**.
