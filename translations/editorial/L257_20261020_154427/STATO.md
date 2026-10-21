# STATO — L257 (`data/human/post-war reactions.txt`, righe 76–151)

**Stato: CHIUSO.** Secondo lotto del file: **23 unità** di dialogo, `MISSION_TEXT`, e **due contesti** — chiude
`Asteroid Miners` e apre `Navy and Free Worlds Captains`. Il file è aperto a **45/87 (51,7%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L257_20261020_154427/` |
| file | `data/human/post-war reactions.txt` (87 unità · 1.925 parole · righe 40–264) |
| righe | 76–151 |
| unità | **23** |
| parole | **406 EN → 408 IT** |
| rapporto | **0,82 – 1,30** |
| contesti | **2** — `War Reactions: Asteroid Miners` (**9**) → `War Reactions: Navy and Free Worlds Captains` (**14**) |
| tab | **22** in inglese, **22** in italiano, sulle **stesse** unità; la **10** è l'unica senza |
| virgolette | **45** in inglese, **45** in italiano, mappa **per unità identica** (e la **12 ne ha 3**, non 4) |
| apici | **17 EN** su 12 unità / **5 IT** su 4 unità (10, 12, 22, 23) |
| segnaposto | **5** — `<first>` 1, `<last>` 3, `<ship>` 1, **ordine identico per unità** |
| tipi | **23 `MISSION_TEXT`** |
| `check.py` | **22 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **23 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 22 prima · 23 qui · **42 dopo** la 151 · cambio missione alla riga **110** |
| `sha256[:16]` | **`bce2d751217d9e1c`** |

## Comandi

```bash
python staging/editorial/L257_20261020_154427/check.py     # FAIL totale: 0 (22 controlli)
python staging/editorial/L257_20261020_154427/verify.py    # FAIL: 0 (23 controlli, 45/87)
```

## La citazione non chiusa

L'unità **12** (riga 112) ha **tre** virgolette, non quattro:

```
"Captain Fiona, F.S. Baobab," says the other. "We both saw you in battle against the Pug. You're the war's most accomplished captain!
```

La citazione lunga **si apre e non si chiude** nel sorgente. La resa la riproduce **com'è** (tre virgolette, e la frase
finisce con `!`), e i due script lo verificano in entrambe le lingue: chiuderla sarebbe un «miglioramento» che altera il
testo del gioco.

## Il cambio di missione

Le unità 1–9 chiudono la missione dei **gemelli minatori**; la **10** è una descrizione d'ambiente in un bar
(«Ti stai rilassando in un bar mentre la tua nave fa rifornimento…») e apre la missione delle **due capitane sorelle**, una
della **Marina** e una dei **Free Worlds**. Il `check.py` verifica la sequenza esatta dei contesti, non solo la loro presenza.

## Limiti dichiarati

Nessuna approvazione (23 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Il file è a **45/87**.
