# STATO — L157 · `weapons.txt` (plasma, lanciafiamme e la famiglia Meteor)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L157_20261019_173323` |
| Righe / unità | **625–983** / **16** — file al **37/90 (41,1%)** |
| Tipi | 15 `DESCRIPTION` · 1 `VALUE` |
| `UI_LABEL` | **0** — asserzione vuota scritta |
| Token | **0** — asserzione vuota scritta |
| Contesti | **11** · **14 testi distinti** su 16 unità |
| Parole | **592 EN → 621 IT** (1.049); **0.98–1.27** |
| Tab · virgolette | **4 unità** · **0** |
| sha256 | `44b8d641c08a7203…` |
| Esiti | `check.py` **24** (`FAIL 0`) · `verify.py` **19**, exit **0** |

## Cosa contiene

| blocco | unità | righe | contenuto |
|---|---|---|---|
| cannoni al plasma | 1-7 | 625-796 | `Particle Cannon`, `Proton Gun`, `Proton Turret`, `Plasma Cannon`, `Plasma Turret`, `Plasma Repeater` (2 unità) |
| lanciafiamme | 8 | 834 | `Flamethrower` |
| famiglia Meteor | 9-16 | 885-983 | munizione, `VALUE` della cassa, cassa, lanciatore (2 unità), pod (3 unità) |

## Rese che contano

| EN | IT |
|---|---|
| `Syndicate` | **Sindacato** |
| `Southern Rim` | **Bordo Meridionale** |
| `outfitter` | **emporio** |
| `reverse engineer` | **ricostruire a ritroso** |
| `repeater` | **repeater**, invariato |
| `trades off its larger bursts for a much faster rate of fire` | **sacrifica le raffiche più ampie in cambio di una cadenza di fuoco molto più rapida** |

## Verifica

```bash
cd staging/editorial/L157_20261019_173323
python check.py     # FAIL totale: 0 (24 controlli)
python verify.py    # exit 0 (19 controlli)
```

**14 testi inglesi distinti su 16 unità, per le due coppie ripetute.**

**Non verificato**: nessuna missione o arma vista a schermo; i testi non sono stati caricati nel gioco.
