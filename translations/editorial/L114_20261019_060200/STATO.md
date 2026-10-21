# STATO — L114 · `data/_ui/tooltips.txt` (**110 contesti per 110 unità**)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L114_20261019_060200` |
| Righe / unità | **976–1309** / **110** |
| Tipo | **110 `TUTORIAL_TIP`**, nient'altro |
| Stati | **110 `PENDING`** — misurato con `select state` e **asserito** in `mkparts.py` |
| Contesti | **110**, **uno per unità** (nessun doppio: la forma di L113 qui sarebbe un errore) |
| Parole | **1816 EN → 1905 IT** (1,049); per unità 0,93–1,56, media 1,18 |
| Tab · token · quadre | **0** · **0** · **0** |
| Ripetizioni | **4 coppie legittime** rese identiche: 17/64, 18/65, 19/66, 36/83 |
| Virgolette | **12** (unità 19, 38, 66, 85 con 2; unità 52 con 4) |
| sha256 | `83513c92ec109aa8…` |
| `check.py` | **36 controlli**, `FAIL totale: 0` |
| `verify.py` | **41 controlli**, exit **0** |

## La forma dei contesti è tornata «uno per unità»

L113 aveva **87 contesti per 96 unità** (nove doppi). Qui ogni unità ha il suo contesto, e il controllo è
scritto al contrario: **110 contesti distinti**, `max(Counter) == 1`. Copiare il controllo del lotto
precedente avrebbe bocciato un lotto corretto; copiare questo avrebbe bocciato L113.

## Le quattro coppie di ripetizioni

Le armi hanno **due misure dello stesso effetto** — per secondo e per colpo — e l'inglese è **identico**
nelle due voci. Solo il contesto le distingue:

| coppia | contesti | inglese |
|---|---|---|
| **17 / 64** | `tip:scrambling damage / second` · `/ shot` | `Increases the target's chance of weapon failure…` |
| **18 / 65** | `tip:slowing damage / second` · `/ shot` | `Reduces the target's turn rate, acceleration, and top speed…` |
| **19 / 66** | `tip:disruption damage / second` · `/ shot` | `Allows weapon damage to "leak through"…` |
| **36 / 83** | `tip:firing scramble / second` · `/ shot` | `Increases the chance of weapon failure for some time…` |

Qui il criterio «zero ripetizioni» di L111–L113 è **rovesciato**: la ripetizione è voluta dal sorgente, la
resa ripete, e il controllo la **elenca** e la verifica identica. Le altre due voci quasi-parallele
(`firing slowing` 37 e 84, `firing disruption` 38 e 85) **non** sono identiche in inglese e hanno due rese
diverse: differenziarle sarebbe stato l'errore opposto.

## Le 12 virgolette

Sono citazioni interne, non discorso:

- unità **19, 66** (disruzione): `"passare"`;
- unità **38, 85** (disruzione allo sparo): `"passare"`;
- unità **52** (`homing type`): **quattro**, perché cita due parole del pannello — `"diretta"` e `"anticipata"`.

Nella finestra precedente erano 22, in L112 zero: il numero va misurato a ogni finestra, mai ereditato.

## Contenuto

- **Armi, danni per secondo** (10–47): scudi, scafo, oggetti estraibili, carburante, calore, energia,
  ionizzazione, disturbo, interferenza sui motori, disruzione, scarica, corrosione, perdita di carburante,
  ustione; le stesse voci in **percentuale** e le voci **allo sparo** (consumo e danno alla propria nave).
- **Cadenza e torrette** (48–51): colpi al secondo con la nota sulle batterie, velocità di virata della
  torretta e moltiplicatore, ampiezza dell'arco di protezione.
- **Inseguimento** (52–56): tipo di guida, aggancio, aggancio ottico, a infrarossi, radar.
- **Armi, danni per colpo** (57–94): la stessa serie misurata **per colpo**, con le quattro coppie identiche.
- **Precisione e area** (95–100): imprecisione, raggio di esplosione, robustezza del missile, anti-missile,
  raggio traente, precisione di estrazione.
- **Avvisi del cantiere** (101–110): cuccette mancanti o insufficienti, surriscaldamento, energia, carburante,
  propulsori, governo, nave troppo fredda, solo postbruciatore, solo spinta inversa.

## Invariante di segmento

| Voce | Valore |
|---|---|
| Unità prima della riga 976 | **320** (L111+L112+L113) |
| Unità dopo la riga 1309 | **237** |
| Confine | riga **1312** apre `tip:battery only?` |
| File | **667 unità**, `max(line) = 1865` |
| Copertura | **430/667 (64,5%)** |

## Verifica

```bash
cd staging/editorial/L114_20261019_060200
python mkparts.py   # 110 unità · 110 contesti · 12 virgolette · 4 coppie identiche · tutte PENDING
python check.py     # FAIL totale: 0 (36 controlli)
python verify.py    # exit 0 (41 controlli)
```
