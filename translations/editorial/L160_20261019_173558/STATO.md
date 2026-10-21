# STATO — L160 · `weapons.txt` (Heavy Rocket Pod, il Nuclear Missile e la Gatling (chiude il file))

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L160_20261019_173558` |
| Righe / unità | **1640–1844** / **13** — file al **90/90 (100%)** |
| Tipi | 11 `DESCRIPTION` · 2 `VALUE` |
| `UI_LABEL` | **0** — asserzione vuota scritta |
| Token | **0** — asserzione vuota scritta |
| Contesti | **6** · **11 testi distinti** su 13 unità |
| Parole | **408 EN → 421 IT** (1.032); **1.00–1.27** |
| Tab · virgolette | **5 unità** · **0** |
| sha256 | `b2663bd3f42fddc7…` |
| Esiti | `check.py` **27** (`FAIL 0`) · `verify.py` **23**, exit **0** |

## Cosa contiene

| blocco | unità | righe | contenuto |
|---|---|---|---|
| razzi pesanti | 1-3 | 1640-1642 | pod: descrizione, nota sui pod, munizioni |
| missile nucleare | 4-5 | 1715-1716 | la descrizione e la nota fra parentesi quadre |
| Gatling | 6-13 | 1751-1844 | `VALUE` delle munizioni, cartuccia, `VALUE` delle scatole, scatole, `Gatling Gun`, `Gatling Turret` |

## Rese che contano

| EN | IT |
|---|---|
| `Gatling Gun Ammo` · `Bullet Boxes` | **identici** (2 `VALUE`) |
| `one-shot weapon` | **arma a colpo singolo** |
| `depleted nuclear fuel` | **combustibile nucleare esaurito** |
| `muzzle velocity` | **velocità alla bocca** |
| `19th century` | **XIX secolo** |
| `spin in his grave` | **rotolare nella tomba** |
| `tear apart the hulls` | **squarciare gli scafi** |

## Verifica

```bash
cd staging/editorial/L160_20261019_173558
python check.py     # FAIL totale: 0 (27 controlli)
python verify.py    # exit 0 (23 controlli)
```

**53esimo file completo della campagna; 90 unità / 3241 parole EN in sei lotti.**

**Non verificato**: nessuna missione o arma vista a schermo; i testi non sono stati caricati nel gioco.
