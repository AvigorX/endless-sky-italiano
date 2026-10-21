# STATO — L254 (`data/wanderer/wanderer jobs.txt`, righe 458–888)

**Stato: CHIUSO.** Terzo lotto del file, **41 unità** (18 `VALUE` + 18 `DESCRIPTION` + 4 `DIALOG` + 1 `TEXT`). Il file sale a
**91/92 (98,9%)**: **resta una sola unità** alla riga 891.

| voce | valore |
|---|---|
| directory | `staging/editorial/L254_20261020_152543/` |
| file | `data/wanderer/wanderer jobs.txt` (92 unità · 1.303 parole · righe 15–891) |
| righe | 458–888 |
| unità | **41** |
| parole | **426 EN → 434 IT** |
| rapporto | **0,94 – 1,17** (media 1,06), gate 0,55–1,90 |
| contesti | **20** — 19 missioni + il blocco `phrase:wanderer cargo delivery payment` |
| tab / virgolette | **0** / **0** (asserzioni negative scritte) |
| apici | **3 EN** (unità 29, 41) / **1 IT** (unità 1, `un'ora`) |
| segnaposto | **83** in **9** famiglie; `<cargo>` e `<destination>` **15 e 15**, ordine verificato |
| copiati | **18** `VALUE` (6 distinti) |
| tradotti | **22** prosa + **1** `TEXT` di blocco `phrase` — **17 stringhe distinte**, **6 gruppi** (8/8/4/4/3/3) |
| `check.py` | **32 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **28 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 50 prima · 41 qui · **1** dopo · confine riga **891** |
| copertura del file | **91/92 (98,9%)** |
| `sha256[:16]` | **`12c0d8ec6bb65b18`** |

## Comandi

```bash
python staging/editorial/L254_20261020_152543/check.py     # FAIL totale: 0 (32 controlli)
python staging/editorial/L254_20261020_152543/verify.py    # FAIL: 0 (28 controlli, 91/92)
```

## Cosa contiene

Il grosso dei **lavori di carico dei Wanderer**: cinque `Delivery`, quattro `Rush Delivery`, tre `Bulk Delivery`, le tre
forniture ai **Kor Efreti**, il trasporto di **soldati Slegati catturati**, del **governatore**, e la missione di studio sui
**mondi Kor Efret**, più il **blocco `phrase`** che il gioco usa come battuta di consegna dei carichi.

## Le due cose che contano

- **Le schede generiche sono ripetute 8 e 4 volte**: la resa è quella **dominante del corpus** (39 e 17 occorrenze), e il
  controllo la **calcola a runtime**, non la confronta con una costante scritta a mano.
- **Il `TEXT` è un blocco `phrase:`**: è prosa, quindi si traduce; il `check.py` lo verifica **separatamente** dagli altri
  tipi, e il `verify.py` pretende che resti una frase intera.

## Limiti dichiarati

Nessuna approvazione (41 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Il file **non** è
completo: 91/92; resta **una** unità, che sarà il lotto terminale.
