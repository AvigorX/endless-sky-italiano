# STATO — L156 · `weapons.txt` (laser pesanti, mining laser, raggi traenti e antimissili)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L156_20261019_173237` |
| Righe / unità | **341–589** / **11** — file al **21/90 (23,3%)** |
| Tipi | 11 `DESCRIPTION` |
| `UI_LABEL` | **0** — asserzione vuota scritta |
| Token | **0** — asserzione vuota scritta |
| Contesti | **9** · **11 testi distinti** su 11 unità |
| Parole | **527 EN → 548 IT** (1.040); **1.02–1.17** |
| Tab · virgolette | **2 unità** · **0** |
| sha256 | `ecb449525eca318b…` |
| Esiti | `check.py` **22** (`FAIL 0`) · `verify.py` **17**, exit **0** |

## Cosa contiene

| blocco | unità | righe | contenuto |
|---|---|---|---|
| laser pesanti | 1-2 | 341-370 | `Heavy Laser`, `Heavy Laser Turret` |
| estrazione | 3-6 | 407-441 | `Mining Laser` e `Mining Laser Turret` (2 unità ciascuno) |
| raggi traenti | 7 | 465 | `Tractor Beam` |
| Deep Sky | 8-9 | 496-525 | `Electron Beam`, `Electron Turret` |
| antimissili | 10-11 | 557-589 | `Anti-Missile Turret`, `Heavy Anti-Missile Turret` |

## Rese che contano

| EN | IT |
|---|---|
| `mid-2400s` | **metà degli anni 2400** |
| `24th century` | **XXIV secolo** |
| `tractor beams` | **raggi traenti** |
| `Deep Sky labs` | **laboratori Deep Sky** |
| `electron beam weapons` | **armi a fascio di elettroni** |
| `its smaller sibling` | **la sua sorella minore** |
| `firing in clusters` | **sparano in grappolo** |

## Verifica

```bash
cd staging/editorial/L156_20261019_173237
python check.py     # FAIL totale: 0 (22 controlli)
python verify.py    # exit 0 (17 controlli)
```

**Segmento verificato: 10 unità prima, 11 nel lotto, 69 dopo, confine alla riga 625.**

**Non verificato**: nessuna missione o arma vista a schermo; i testi non sono stati caricati nel gioco.
