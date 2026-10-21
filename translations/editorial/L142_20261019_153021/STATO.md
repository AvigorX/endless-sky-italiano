# STATO — L142 · `unfettered 0 prologue.txt` (chiude `Unfettered Jump Drive 1`)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L142_20261019_153021` |
| Righe / unità | **139–201** / **20** — file al **44,2%** (65/147) |
| Tipi | **18 `MISSION_TEXT`** · **1 `VALUE`** (`More Jump Drives`) · **1 `DESCRIPTION`** |
| `UI_LABEL` · token | **0** · **0** — due asserzioni vuote scritte |
| Stati | **20 `PENDING`** — misurato e **asserito** |
| Contesto | **1**, e si **chiude**: `Unfettered Jump Drive 1` 20/20 |
| Testi | **19 distinti**: il rifiuto (13 e 18) due volte, `(No.)` identico |
| Parole | **493 EN → 456 IT** (0,925); per unità 0,74–1,24, media 1,02 |
| Tab · virgolette | **17 unità** · **38** (quattro unità con quattro) |
| sha256 | `1e2c9c50567e62e1…` |
| `check.py` | **29 controlli**, `FAIL totale: 0` |
| `verify.py` | **26 controlli**, exit **0** — invariante di **segmento** |

## Una trattativa in venti unità

La folla attorno alla nave, l'offerta («Un milione di crediti, e l'amicizia del vero popolo Hai»), le tre domande del
giocatore, la promessa dell'iperpropulsore, la minaccia appena velata («Non puoi fare a meno di chiederti se proveranno
a prendere la tua nave con la forza»), l'addio cerimoniale: «che la fortuna ti assista, amico umano».

## Due testi che devono restare identici, per ragioni opposte

| testo | unità | perché |
|---|---|---|
| il **rifiuto** («Mi dispiace, ma se ti do questo motore di salto perderò la capacità di catturarne altri…») | 13, 18 | è lo stesso ramo raggiunto per due strade: due rese diverse sarebbero due bug |
| **`(No.)`** | 4 | in italiano «No» **è** la stessa parola: l'identità è legittima, e va **dichiarata** in `ID_OK` con un controllo suo |

Senza `ID_OK`, il controllo «tutte tradotte» avrebbe bocciato `(No.)`; escludendolo dai controlli, l'unità sarebbe
sparita dall'inventario. La lista lo dichiara e lo verifica:

```python
ck('ID_OK: (No.) identico, dichiarato e verificato uno per uno',
   by[4]['italian'].lstrip('\t') == ID_OK[4] == by[4]['english'].lstrip('\t'))
```

## Un errore di misura, corretto in tre punti

L'handoff di L142 diceva «**81 dopo** la riga 201». Il conto vero è **82** (147 − 45 − 20), e il `verify.py` l'ha
bocciato subito. Corretto in `verify.py` e nell'handoff: un «dopo» scritto a mente è l'errore ricorrente di questa
serie, e l'unica difesa è una sottrazione misurata.

## Verifica

```bash
cd staging/editorial/L142_20261019_153021
python mkparts.py   # 20 unità · 19 distinti · rifiuto ×2 · (No.) in ID_OK · 17 tab · 38 virgolette
python check.py     # FAIL totale: 0 (29 controlli)
python verify.py    # exit 0 (26 controlli, invariante di segmento)
```

**Non verificato**: la trattativa non è stata giocata; lo scambio del motore di salto non è stato visto a schermo.
