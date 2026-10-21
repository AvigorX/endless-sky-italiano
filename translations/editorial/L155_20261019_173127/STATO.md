# STATO — L155 · `weapons.txt` (blaster e laser: le prime dieci armi (apre il file))

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L155_20261019_173127` |
| Righe / unità | **36–306** / **10** — file al **10/90 (11,1%)** |
| Tipi | 10 `DESCRIPTION` |
| `UI_LABEL` | **0** — asserzione vuota scritta |
| Token | **0** — asserzione vuota scritta |
| Contesti | **10** · **10 testi distinti** su 10 unità |
| Parole | **574 EN → 594 IT** (1.035); **0.97–1.23** |
| Tab · virgolette | **0 unità** · **0** |
| sha256 | `9ff81a5de32f81b0…` |
| Esiti | `check.py` **20** (`FAIL 0`) · `verify.py` **17**, exit **0** |

## Cosa contiene

| blocco | unità | righe | contenuto |
|---|---|---|---|
| blaster | 1-7 | 36-251 | `Energy Blaster`, `Twin Blaster`, le due torrette, le due versioni modificate, `Heavy Blaster` |
| laser | 8-10 | 277-306 | `Beam Laser`, `Laser Turret` |

## Rese che contano

| EN | IT |
|---|---|
| `gun port` | **alloggiamento per armi** |
| `tinkerers` | **smanettoni** |
| `turret` / `gun` | **torretta** / **cannone** |
| `Deep` (regione) | **Deep**, invariato |
| `Firebird` · `Particle Cannon` · `Plasma Cannon` | **invariati** |
| `The Heavy Blaster is…` | **Il Heavy Blaster è…** |

## Verifica

```bash
cd staging/editorial/L155_20261019_173127
python check.py     # FAIL totale: 0 (20 controlli)
python verify.py    # exit 0 (17 controlli)
```

**Il lotto **apre** `weapons.txt`: 0 unità prima della riga 36, 80 dopo la 306.**

**Non verificato**: nessuna missione o arma vista a schermo; i testi non sono stati caricati nel gioco.
