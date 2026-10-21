# STATO — L259 (`data/human/post-war reactions.txt`, righe 222–250)

**Stato: CHIUSO.** Quarto lotto del file: **15 unità**, `MISSION_TEXT`, **un solo contesto**
(`mission:War Reactions: Syndicate Orphan`). Il file è aperto a **80/87 (92,0%)**: resta **una finestra**, L260, che sarà
**terminale**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L259_20261020_160343/` |
| file | `data/human/post-war reactions.txt` (87 unità · 1.925 parole · righe 40–264) |
| righe | 222–250 |
| unità | **15** |
| parole | **426 EN → 441 IT** |
| rapporto | **0,93 – 1,53** |
| contesti | **1** — `War Reactions: Syndicate Orphan` |
| tab | **15** in inglese, **15** in italiano, su **tutte** le unità, primo carattere |
| virgolette | **45** in inglese, **45** in italiano, mappa **per unità identica** (e la **2 ne ha 5**) |
| apici | **19 EN** su 10 unità / **17 IT** su 8 unità |
| segnaposto | **4** — `<first>` 2, `<last>` 2, solo nelle unità **4** e **7**, ordine identico |
| tipi | **15 `MISSION_TEXT`** |
| `check.py` | **23 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **23 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 65 prima · 15 qui · **7 dopo** la 250 · nessun cambio di missione |
| `sha256[:16]` | **`b4019aeff69585da`** |

## Comandi

```bash
python staging/editorial/L259_20261020_160343/check.py     # FAIL totale: 0 (23 controlli)
python staging/editorial/L259_20261020_160343/verify.py    # FAIL: 0 (23 controlli, 80/87)
```

## Le due forme delicate

1. **La 2 ha CINQUE virgolette**: l'ultima citazione (`"Solo i più svegli di noi possono farlo…`) si apre e **non si
   chiude** nel sorgente. Terzo caso del file dopo L257 u12 e L258 u5: si **riproduce**, non si «aggiusta».
2. **Le unità 7 e 8 sono quasi identiche**: cambia solo una battuta — `Sei il capitano <first> <last>!` contro `Hai guidato
   tu l'attacco!` — e il resto è identico, fino a `Ti tende la mano e tu la stringi.` Il test verifica **la differenza** e
   **l'identità della coda**, così non si possono «unificare» per distrazione.

## Limiti dichiarati

Nessuna approvazione (15 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Restano **7 unità**
(righe 253–264) per **L260**, che chiuderà il file a **87/87** — quattordicesimo file completo della campagna.
