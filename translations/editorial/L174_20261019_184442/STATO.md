# STATO — L174 · `avgi ships.txt` (quattro astronavi: Koryfi, Melodikos, Avlaki, Harmonikos)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L174_20261019_184442` |
| Righe / unità | **120–522** / **14** — file al **14/102 (13,7%)** |
| Tipi | **12 `DESCRIPTION`** · **2 `VALUE`** |
| `UI_LABEL` · token | **0** · **0** — due asserzioni vuote scritte |
| Contesti | **4** (Koryfi 3, Melodikos 4, Avlaki 3, Harmonikos 4) · **14 testi distinti** |
| Parole | **477 EN → 489 IT** (1,025); **0,94–1,21**, media **1,08** |
| Tab · virgolette | **8 unità** (2, 3, 6, 7, 9, 10, 13, 14) · **0** |
| Apici | **4 in inglese** (possessivi) · **0 possessivi in italiano** |
| sha256 | `c734fd303220cc1b…` |
| Esiti | `check.py` **26** (`FAIL 0`) · `verify.py` **21**, exit **0** |

## Cosa contiene

| nave | unità | righe | contenuto |
|---|---|---|---|
| `Koryfi` | 1-3 | 120-122 | trasporto passeggeri leggero, pre-iperguida, gravità per rotazione, propulsione fiacca |
| `Melodikos` | 4-7 | 126-268 | grande trasporto, distesa solare enorme, ex ciclatore interplanetario |
| `Avlaki` | 8-10 | 375-377 | mercantile medio, discendente di un rimorchiatore solare-elettrico |
| `Harmonikos` | 11-14 | 381-522 | grande mercantile con moduli cargo trainati, nave da carico interstellare |

## Le tre strutture verificate

1. **La formula dei propulsori** (unità 3, 7, 10, 14): identica in tutte e quattro, cambia **solo il nome** della nave.
   Il controllo sostituisce i nomi con `NOME` e pretende **una sola** stringa.
2. **La coppia speculare 2/9**: la Koryfi **toglie** la centrifuga per mettere i container, l'Avlaki fa l'**opposto**.
3. **Il rimando incrociato 6/13**: la Melodikos rimanda alla Harmonikos, la Harmonikos alla Melodikos.

## Verifica

```bash
cd staging/editorial/L174_20261019_184442
python check.py     # FAIL totale: 0 (26 controlli)
python verify.py    # exit 0 (21 controlli)
```

**Non verificato**: nessuna astronave vista a schermo; i testi non sono stati caricati nel gioco.
