# STATO — L78 · `data/successors/successor side missions.txt`

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L78_20261018_201938` |
| Righe / unità | **224–325** (finestra 221–325) / **53** |
| Parti | **3** — 18 · 18 · 17 |
| Contesto | **1 intero** — `Stargazing 1` (53 unità) |
| Tipi | **49 `MISSION_TEXT` + 1 `VALUE` + 1 `DESCRIPTION` + 2 `UI_LABEL`** |
| Parole | 1109 EN → 1060 IT (**0,956**) |
| Rapporto per unità | **0,74 – 1,53** |
| `NT` | **2** — unità **47** (`fah soom`) e **50** (`novel name`), identiche |
| `LOGBOOK`/`DIALOG`/`CONVERSATION`/`TEXT` | **0/0/0/0** — assenze dichiarate |
| Token `<…>` | **13** in 7 famiglie: `<ship>` 4, **`<home system>` 4**, `<planet stopovers>`/`<destination>`/`<date>`/`<origin>`/`<payment>` 1 |
| Tab · virgolette | **46** su **46** unità · **86** — **0 dispari** |
| Duplicati inglesi | **5 gruppi** — 13/20, 15/22, 16/23, 39/41, 45/49, resa identica **voluta** |
| sha256 | `a0ebf1dce186051d…` |
| `check.py` | **31 controlli**, `FAIL totale: 0` |
| `verify.py` | **39 controlli**, exit **0** |

## Dove siamo nel file

| Voce | Valore |
|---|---|
| Unità prima della riga 224 | **63** (L77) |
| Unità dopo la riga 325 | **48** |
| File | **164 unità**, `max(line) = 453` |
| Confine dopo | riga **336** apre `mission:Successors: People's Houses: First Contact` |
| Copertura | **116/164 (70,7%)** |

## Cosa è stato deciso qui

1. **`fah soom` e `novel name` restano identiche**: sono `label` di salto, non prosa.
2. **`stargazers` → «osservatori di stelle»**: due appassionati, non scienziati; il titolo della missione usa
   la stessa forma.
3. **5 gruppi di duplicati legittimi**: le due varianti dello stesso dialogo (13/20, 15/22, 16/23) e le due
   opzioni identiche (39/41, 45/49). Resa identica, dichiarata.
4. **`<home system>` nuovo**: parità per simbolo su 4 occorrenze, e le due opzioni «(Indica <home system>.)»
   restano identiche perché la scelta è la stessa.
5. **`Maspa-Mavra`, `Khosa-Kella-Oa`, `Saaqa-Viirja`** invariati; **`Sol`** invariato in entrambe le lingue.
6. **`repulsor lift` → «sollevatore a repulsione»**; **`tent` → «tenda»** con «planante» quando scivola.
7. **`Thour't` (refuso per `thou'rt`)** reso con «Sei», senza arcaismo.

## Verifica

```bash
cd staging/editorial/L78_20261018_201938
python check.py   # FAIL totale: 0   (31 controlli)
python verify.py  # exit 0           (39 controlli)
```

## Prossimo passo

**L79**: righe **326–400** (prima unità alla **336**), **29 unità**, **620 parole**, **1 contesto**
(`People's Houses: First Contact`), **tutte `MISSION_TEXT`**, tab **28** su 28 unità, virgolette **33**,
**3 dispari (10, 22, 27)**, **0 token**, **0 duplicati**.
