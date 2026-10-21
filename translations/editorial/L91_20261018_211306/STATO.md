# STATO — L91 · `data/successors/successor culture conversations.txt` (secondo segmento)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L91_20261018_211306` |
| Righe / unità | **155–229** (finestra 143–229) / **34** |
| Tipi | **33 `MISSION_TEXT`** + **1 `UI_LABEL`** (`myiara system`, idx 29, identica) |
| Contesti | **2** in ordine di riga (`Graffiti` … `Stage Play`) |
| Parole | **1117 EN → 1084 IT** (0,971); per unità 0,92–1,54 |
| Tab · virgolette · token | **30** (tutte tranne 1, 28, 29, 30) · **60** · **5** (4 `<ship>` + 1 `<origin>`) |
| Ripetizioni | **8/12**, **9/13**, **10/14**: inglese identico, resa identica (dichiarate) |
| sha256 | `9a8dcdeaee3a69af…` |
| `check.py` | **28 controlli**, `FAIL totale: 0` |
| `verify.py` | **28 controlli**, exit **0** |

## Dove siamo

| Voce | Valore |
|---|---|
| Unità prima della riga 155 | **34** (L90, righe 23–142) |
| Unità dopo la riga 229 | **46** (righe 230–351, a L92) |
| File | **114 unità**, `max(line) = 351` |
| Confine dopo | riga 230, contesto `mission:Successors: Stage Play` (già aperto nel lotto) |
| Copertura | **68/114 (59,6%)** · 2215 EN → 2098 IT · 2 lotti |

## Contenuto

Il **Graffiti** (righe 155–204): il terzetto di Successori sorpreso a spalmare «soluzione per lo scafo» sul
fianco della nave, la recita della squadra di riparazione, le lattine nascoste dietro le braccia, e — a seconda
del ramo — la scritta **«Ryiaa è stata qui! Con gli amici.»** oppure **«'Erjn'... Stupido! Niente aculei,
niente cervello!»** con una caricatura del volto del giocatore. L'apertura di **Stage Play** (219–229): i
manifesti per **«Myiara l'Immortale»**, il Successore che invita a teatro.

## Verifica

```bash
cd staging/editorial/L91_20261018_211306
python check.py   # FAIL totale: 0 (28 controlli)
python verify.py  # exit 0 (28 controlli)
```
