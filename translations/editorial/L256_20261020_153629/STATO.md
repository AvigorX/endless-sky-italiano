# STATO — L256 (`data/human/post-war reactions.txt`, righe 40–74)

**Stato: CHIUSO.** Primo lotto del file: **22 unità** di dialogo, tutte `MISSION_TEXT`, nello stesso contesto
(`mission:War Reactions: Asteroid Miners`). Il file è aperto a **22/87 (25,3%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L256_20261020_153629/` |
| file | `data/human/post-war reactions.txt` (87 unità · 1.925 parole · righe 40–264) |
| righe | 40–74 |
| unità | **22** |
| parole | **433 EN → 422 IT** |
| rapporto | **0,83 – 1,32** |
| contesti | **1** — `mission:War Reactions: Asteroid Miners` |
| tab | **21** in inglese, **21** in italiano, sulle **stesse** unità (2–22), come primo carattere |
| virgolette | **34** in inglese, **34** in italiano, **per unità identiche** (17 unità × 2) |
| apici | **19 EN** su 10 unità / **9 IT** su 7 unità |
| segnaposto | **0** (asserzione negativa doppia) |
| tipi | **22 `MISSION_TEXT`** |
| `check.py` | **23 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **21 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 0 prima · 22 qui · **65 dopo** la 74 · confine riga **76** (stesso contesto) |
| `sha256[:16]` | **`112f4a79b1436634`** |

## Comandi

```bash
python staging/editorial/L256_20261020_153629/check.py     # FAIL totale: 0 (23 controlli)
python staging/editorial/L256_20261020_153629/verify.py    # FAIL: 0 (21 controlli, 22/87)
```

## Perché questo lotto è tipografico

È un **dialogo** fra due gemelli capitani: 21 battute rientrate da un tab, 17 battute fra virgolette dritte, e 19 apici
inglesi (`you're`, `It's`, `they're`, `everyone's`, `won't`, `'Pug'`, `Navy's`, `don't`, `Danforth's`…). Il lotto non poteva
essere verificato «a occhio»: tab, virgolette e apici sono asseriti **per unità**, con l'elenco delle unità interessate.

## Il refuso voluto

Alla riga **73** il gemello di sinistra sbaglia il nome: `Admiral Danforts`; alla **74** il gemello lo corregge
(`Danforth. Admiral Danforth.`). La resa **conserva** l'errore e la correzione: senza il refuso la seconda battuta non
avrebbe senso. Il `check.py` lo verifica in entrambe le direzioni.

## Limiti dichiarati

Nessuna approvazione (22 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Il file è a **22/87**.
