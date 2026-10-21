# STATO — L164 · `avgi outfits.txt` (razzi a fissione, motori ad antimateria, torce a fusione)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L164_20261019_180227` |
| Righe / unità | **337–425** / **9** — file al **44/63 (69,8%)** |
| Tipi | **7 `DESCRIPTION`** · **2 `VALUE`** |
| `UI_LABEL` | **0** — asserzione vuota scritta |
| Token | **0** — asserzione vuota scritta |
| Contesti | **4** (Vapor 2, A-3600 1, Z-333 3, Z-666 3) · **8 testi distinti** |
| Parole | **582 EN → 615 IT** (1,057); **1,00–1,23**, media **1,10** |
| Tab · virgolette | **3 unità** · **4** (nei due `VALUE`) |
| sha256 | `48d48f5b2d2db7dc…` |
| Esiti | `check.py` **22** (`FAIL 0`) · `verify.py` **20**, exit **0** |

## Cosa contiene

| blocco | unità | righe | contenuto |
|---|---|---|---|
| razzo a fissione | 1-2 | 337-338 | `Vapor Nuclear Rocket`: perché esiste, il progetto derivato dal Lantern |
| motore ad antimateria | 3 | 368 | `A-3600 "Beam" Amat Drive`, i banchi di fasci di Anax, l'obsolescenza |
| torce `Spark` | 4-6 | 372-397 | `VALUE`, la polarizzazione di spin, la nota sull'ugello |
| torce `Zap` | 7-9 | 401-425 | `VALUE`, lo Z-pinch, la stessa nota sull'ugello |

## Rese che contano

| EN | IT |
|---|---|
| `thrust-to-weight ratio` | **rapporto spinta-peso** |
| `gas core nuclear fission thermal rockets` | **razzi termici a fissione nucleare a nucleo gassoso** |
| `thermionic converters` | **convertitori termoionici** |
| `beam-core antimatter drive` | **motore ad antimateria a nucleo di fasci** |
| `spin polarized` | **polarizzato di spin** |
| `magnetic nozzle` | **ugello magnetico** |
| `Z-pinch` | **Z-pinch**, invariato |
| `annular flow` | **flusso anulare** |

## Verifica

```bash
cd staging/editorial/L164_20261019_180227
python check.py     # FAIL totale: 0 (22 controlli)
python verify.py    # exit 0 (20 controlli)
```

**Segmento**: 35 unità prima della riga 337, 9 nel lotto, 19 dopo la 425; confine alla riga 429 (un `VALUE`).
**Fedeltà**: i due `VALUE` contengono **virgolette interne** e sono riprodotti alla lettera; idx 6 e idx 9 sono la
stessa stringa e restano identiche.

**Non verificato**: nessuna nave o equipaggiamento visto a schermo; i testi non sono stati caricati nel gioco.
