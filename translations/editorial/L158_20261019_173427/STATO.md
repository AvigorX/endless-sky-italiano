# STATO — L158 · `weapons.txt` (Sidewinder e Javelin: munizioni, pod e lanciatori)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L158_20261019_173427` |
| Righe / unità | **1015–1228** / **18** — file al **55/90 (61,1%)** |
| Tipi | 18 `DESCRIPTION` |
| `UI_LABEL` | **0** — asserzione vuota scritta |
| Token | **0** — asserzione vuota scritta |
| Contesti | **8** · **11 testi distinti** su 18 unità |
| Parole | **564 EN → 578 IT** (1.025); **0.98–1.27** |
| Tab · virgolette | **10 unità** · **0** |
| sha256 | `7abe6d61b8ca79fa…` |
| Esiti | `check.py` **23** (`FAIL 0`) · `verify.py` **18**, exit **0** |

## Cosa contiene

| blocco | unità | righe | contenuto |
|---|---|---|---|
| Sidewinder | 1-9 | 1015-1116 | munizione, rack, lanciatore (3 unità), pod (4 unità) |
| Javelin | 10-18 | 1149-1228 | munizione, cassa, pod (3 unità), mini pod (4 unità) |

## Rese che contano

| EN | IT |
|---|---|
| `protective casings` | **involucri protettivi** |
| `saturating … anti-missile defenses` | **saturare le difese antimissile** |
| `sneak through` | **riescano a passare** |
| `Storage Rack` / `Storage Crate` / `Storage Tube` | **invariati** (nomi di oggetto) |
| `Ammunition for this weapon can be restocked at any outfitter.` | **Le munizioni per quest'arma possono essere rifornite presso qualsiasi emporio.** |

## Verifica

```bash
cd staging/editorial/L158_20261019_173427
python check.py     # FAIL totale: 0 (23 controlli)
python verify.py    # exit 0 (18 controlli)
```

**11 testi inglesi distinti su 18 unità.**

**Non verificato**: nessuna missione o arma vista a schermo; i testi non sono stati caricati nel gioco.
