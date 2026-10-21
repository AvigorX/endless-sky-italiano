# STATO — L117 · `data/human/pirate jobs.txt` (primo lotto: 98 unità, 31 missioni)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L117_20261019_063154` |
| Righe / unità | **20–1624** / **98** |
| Tipi | **31 `VALUE`** · **31 `DESCRIPTION`** · **31 `MISSION_TEXT`** · **5 `DIALOG`** |
| Stati | **98 `PENDING`** — misurato con `select state` e **asserito** in `mkparts2.py` |
| Contesti | **31** — 26 con tre unità, 5 con quattro: **ogni contesto è una missione** |
| Testi distinti | **26** per 98 unità — 9 nomi + 17 testi prosaici |
| Parole | **1804 EN → 1715 IT** (0,951); per unità 0,91–1,22, media 1,02 |
| Tab · quadre | **0** · **0** |
| Token | **108** in sei famiglie: `<payment>` 36, `<planet>` 31, `<cargo>` 31, `<destination>` 31, `<passengers>` 4, `<bunks>` 3 |
| Virgolette | **2**, solo nell'unità 81 (l'urlo del criminale) |
| sha256 | `6ed8bb0de3875183…` |
| `check.py` | **29 controlli**, `FAIL totale: 0` |
| `verify.py` | **38 controlli**, exit **0** |

## Il blocco è fatto di stampi

98 unità ma **26 testi distinti**: nove nomi di missione (uno per famiglia di lavoro: contrabbando, droga,
grosse partite, stealth, ricercati, criminale galattico) e diciassette testi, con il messaggio di fallimento
ripetuto **26 volte**.

| testo | unità | resa |
|---|---|---|
| `In addition to the fine…` | **26** | una sola resa, identica |
| `Run <cargo> … consequences may be severe…` | **11** | una sola resa |
| `Smuggle <cargo> …` | **7** | una sola resa |
| `Run <cargo> … without being scanned…` | **6** | una sola resa |
| dialoghi di consegna (singolare/plurale) | **4 + 1** | due rese, distinte per numero |
| altri 20 testi | 1 ciascuno | resa propria |

Il `mkparts2.py` assegna le rese **per firma dell'inglese** e asserisce che ogni firma combacia con **un solo**
testo: lo stesso inglese non può ricevere due italiani diversi.

## I 31 `VALUE` restano in inglese

Sono **nomi di missione** (`Smuggling to <planet>`, `Bulk drug run to <planet>`, `Wanted individuals to
<planet>`, `Galactic criminal to <planet>`…): decisione 259/L103, restano identici al sorgente. Il `check.py` li
**elenca** (31 indici) e li **esclude** dal controllo «nessuna unità identica al sorgente»; il `verify.py`
ricalcola l'elenco dai `kind`.

**Errore corretto in corso d'opera**: la prima stesura (`mkparts.py`) traduceva anche i nomi e il `check.py` è
diventato rosso su «i 31 VALUE sono identici al sorgente». La correzione è stata **togliere i nomi da `UNIQ`**
(seconda stesura in `mkparts2.py`), non allentare il controllo.

## I 108 token

| famiglia | n | dove |
|---|---|---|
| `<payment>` | 36 | descrizioni, dialoghi, testo del criminale galattico |
| `<planet>` | 31 | tutti nei nomi di missione (uno per missione) |
| `<cargo>` | 31 | descrizioni |
| `<destination>` | 31 | descrizioni |
| `<passengers>` | 4 | dialoghi di consegna |
| `<bunks>` | 3 | descrizione dei ricercati multipli |

Parità verificata **per simbolo e per unità** (stessi simboli, stesso ordine); il testo italiano si costruisce
intorno ai token, che restano intatti.

## Invariante di segmento

| Voce | Valore |
|---|---|
| Unità prima della riga 20 | **0** — è il primo lotto del file |
| Unità dopo la riga 1624 | **181** |
| Confine | riga **1627** apre `mission:Highly Wanted Passenger (Core)` |
| File | **279 unità**, `max(line) = 3706` |
| Copertura | **98/279 (35,1%)** |

## Verifica

```bash
cd staging/editorial/L117_20261019_063154
python mkparts2.py   # 98 unità · 31 VALUE identici · 17 testi prosaici · 108 token
python check.py      # FAIL totale: 0 (29 controlli)
python verify.py     # exit 0 (38 controlli)
```
