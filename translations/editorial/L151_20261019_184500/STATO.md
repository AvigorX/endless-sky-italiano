# STATO — L151 · `coalition jobs.txt` (corriere veloce, carichi, medici, allievi)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L151_20261019_184500` |
| Righe / unità | **799–1171** / **37** — file al **58,4%** (115/197) |
| Tipi | **17 `VALUE`** (identici) · **17 `DESCRIPTION`** · **2 `TEXT`** · **1 `DIALOG`** |
| `LOGBOOK` · `UI_LABEL` | **0** · **0** |
| Token | **81** su **7** simboli |
| Contesti | **19** · **14 testi distinti** su 37 unità |
| Parole | **302 EN → 316 IT** (1,046); **0,90–1,20** |
| Tab · virgolette | **0** · **0** |
| sha256 | `8faf5d133a5b433c…` |
| Esiti | `check.py` **27** (`FAIL 0`) · `verify.py` **24**, exit **0** |

## Un lotto di 37 unità ma di 14 testi

Le unità sono **corte** e ripetute: `Cargo 1..4` e `Bulk 1..4` condividono la **stessa `DESCRIPTION`** — 8 unità, una
resa. La traduzione è quindi una **mappa per stringa inglese**, non una resa per unità: così due copie non possono
divergere. Il `verify.py` confronta le 8 rese e le trova **una sola**.

## Un errore corretto in corsa

`check.py` pretendeva la parola «corriere» fra i termini attesi: non c'è, perché `Fast courier to <planet>` è un `VALUE`
**inglese** e la `DESCRIPTION` dice solo «Consegna». Il controllo è stato corretto — ora **verifica l'assenza** di
«corriere» nel testo tradotto, che è l'informazione vera.

## Verifica

```bash
cd staging/editorial/L151_20261019_184500
python mkparts.py   # 37 unità · 17 VALUE + 17 DESCRIPTION + 2 TEXT + 1 DIALOG · 81 token
python check.py     # FAIL totale: 0 (27 controlli)
python verify.py    # exit 0 (24 controlli, invariante di segmento)
```

**Non verificato**: nessuna missione giocata; il `DIALOG` dei medici non è stato visto a schermo.
