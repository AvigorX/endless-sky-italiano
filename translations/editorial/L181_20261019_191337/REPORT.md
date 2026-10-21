# REPORT — L181 · `human outfits.txt` (secondo lotto)

## 1. Contenuto

Nove schede: due disturbatori radar, tre ramscoop (dal passato dell'esplorazione al `Catalytic Ramscoop` del Deep), tre
iperguide (la scatola misteriosa, i dodici che la capiscono, lo `Scram Drive`) e il `Jump Drive` che chiude il lotto.

## 2. Scelte

| nodo | IT | unità |
|---|---|---|
| `radar jammer` | **disturbatore radar** | 1, 2 |
| `target locks` | **aggancio del bersaglio** | 1 |
| `heat signature` | **firma termica** | 2 |
| `solar wind` | **vento solare** | 3, 4 |
| `a dozen systems` | **una mezza dozzina di sistemi** | 3 |
| `the Free Worlds war` | **la guerra dei Free Worlds** | 5 |
| `engineers in the Deep` | **ingegneri del Deep** | 5 |
| `inscrutable thoughts` | **imperscrutabili pensieri** | 6 |
| `like a wasp stinging an oak leaf` | **come una vespa che punge una foglia di quercia** | 6 |
| `containment field` | **campo di contenimento** | 9 |
| `reverse engineer them` | **ricostruirli a ritroso** | 9 |

## 3. Difficoltà

1. **Nomi tecnici invariati**: `Sidewinders`, `ramscoop`, `scram drive`, `jump drive`, e i nomi propri `Free Worlds` e
   `Deep`. Solo `hyperdrive` diventa **iperguida** — è un nome comune, già reso così nei lotti precedenti.
2. **La metafora della vespa**: l'unico punto del file dove la voce si fa letteraria. Tradotta come metafora, non come
   spiegazione tecnica.
3. **Un errore in corsa (mio)**: il `check.py` pretendeva `hyperdrive` in **idx 6**, dove la parola **non compare** — il
   testo dice «questa misteriosa scatola». L'asserzione era sbagliata; spostata su idx 7 (dove la parola c'è) e
   completata con la verifica che idx 6 non la nomini **né in inglese né in italiano**.
4. **`ZERO VALUE`** in tutto il lotto: asserzione scritta, non omessa.
5. **2 tab** (idx 4 e 7) che in L180 non c'erano: verificati in inglese e in italiano, uno solo per unità.
6. **Gate**: 1,02–1,16, media 1,09. Le parole **calano** di 1 (477 → 476).

## 4. Numeri osservati

```
unita' 9 · 9 DESCRIPTION · 0 VALUE · tutte PENDING
token 0 · 2 tab (4, 7) · 0 virgolette · 1 apice inglese (idx 2)
9 testi distinti · 7 contesti (2 + 2 + cinque con 1) · righe 158/233
parole 477 -> 476 (0.998) · rapporto 1.02 - 1.16, media 1.09
FAIL totale: 0 (25 controlli) · verify exit 0 (19 controlli) · sha256[:16] 4a13b745b4c7e37b
```

## 5. Stato del progetto (dopo L181)

```
TOTALE staging: 28250 unità · 888921 EN · 845859 IT
human outfits.txt: 21/63 (33,3%) · 2 lotti
residuo traducibile (formula state.py): 3680
residuo misurato: 4349 unità / 88183 parole su 111 file
endless-sky HEAD b4aa3bac3, 0 modifiche
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (25 controlli), `verify.py` exit **0** (19 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 9 unità `PENDING`.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Secondo lotto del file**: contratto successivo in `HANDOFF_L182_20261019.md`.
