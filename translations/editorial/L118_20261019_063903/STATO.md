# STATO — L118 · `data/human/pirate jobs.txt` (secondo lotto: 104 unità, 33 missioni)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L118_20261019_063903` |
| Righe / unità | **1627–2955** / **104** |
| Tipi | **36 `DIALOG`** · **33 `VALUE`** · **33 `DESCRIPTION`** · **2 `MISSION_TEXT`** |
| Stati | **104 `PENDING`** — misurato con `select state` e **asserito** in `mkparts.py` |
| Contesti | **33** — 19 con quattro unità, 14 con due |
| Testi distinti | **39** per 104 unità — 11 nomi + 28 testi prosaici (3 già resi in L117) |
| Parole | **1753 EN → 1774 IT** (1,012); per unità 0,88–1,27, media 1,04 |
| Tab · virgolette · quadre | **0** · **0** · **0** |
| Token | **192** in **nove famiglie**: `<planet>` 53, `<payment>` 52, `<destination>` 33, `<system>` 33, `<day>` 17, `<npc>` 9, `<date>` 9, `<bunks>` 5, `<cargo>` 2 |
| sha256 | `31bb9438bee96230…` |
| `check.py` | **28 controlli**, `FAIL totale: 0` |
| `verify.py` | **38 controlli**, exit **0** |

## La forma cambia dentro lo stesso file

| | L117 | **L118** |
|---|---|---|
| `DESCRIPTION` | 31 | 33 |
| `MISSION_TEXT` | 31 | **2** |
| `DIALOG` | 5 | **36** |
| `VALUE` | 31 | 33 |
| famiglie di token | 6 | **9** (aggiunte `<system>`, `<day>`, `<npc>`, `<date>`) |
| virgolette | 2 | **0** |

Il `check.py` di L117 (108 token in sei famiglie, 2 virgolette) qui era rosso per costruzione: la forma è stata
**rimisurata** e il controllo riscritto, con lo **zero virgolette asserito** (`0 = 0`).

## I 33 `VALUE` e i token dentro i nomi

Sono nomi di missione: `Transfer slaves to <planet>`, `Protection to <planet>`, `Protect cargo to <planet>`,
`Protect ship to <planet>`, `Navy near <system>`, `Syndicate near <system>`, `Militia near <system>`,
`Competition near <system>`, `Marauders near <system>`, `Merchants near <system>`, `Marauder Elimination`,
`Galactic criminal to <planet>`. Restano **identici** al sorgente (decisione 259/L103) e molti **contengono un
token**: il nome identico protegge il token per costruzione.

## Tre testi vengono da L117

Il blocco si apre con `Highly Wanted Passenger (Core)` e `(South)`, che ripetono i testi già tradotti in L117.
La resa è stata **riletta** dal `translation.json` di L117 invece di riscritta, e il controllo verifica che le
**8 unità condivise** abbiano la stessa resa: la memoria di traduzione è un dato, non una buona intenzione.

## Contenuto

- **Criminale galattico** (1–8): Core e Sud, con il testo di L117.
- **Trasporto di schiavi** (9–18): cinque missioni, «in celle sicure», con la pena di morte come avvertimento.
- **Mercenari e scorte** (19–36): protezione, scorta di carico illegale, scorta di nave rubata — tre regioni
  (Nord, Centro, Sud) e `<date>` come scadenza.
- **Eliminazione delle forze dell'ordine** (37–60): Marina, Sindacato, milizia, in due taglie.
- **Eliminazione della concorrenza** (61–96): bande rivali e predoni, cinque varianti.
- **Razzie ai mercanti** (97–104): Repubblica e Sindacato, con la quota del bottino.

## Invariante di segmento

| Voce | Valore |
|---|---|
| Unità prima della riga 1627 | **98** (L117) |
| Unità dopo la riga 2955 | **77** |
| Confine | riga **2958** apre `mission:Raid on Merchants (South)` |
| File | **279 unità**, `max(line) = 3706` |
| Copertura | **202/279 (72,4%)** |

## Verifica

```bash
cd staging/editorial/L118_20261019_063903
python mkparts.py   # 104 unità · 33 VALUE identici · 28 testi prosaici (3 da L117) · 192 token
python check.py     # FAIL totale: 0 (28 controlli)
python verify.py    # exit 0 (38 controlli)
```
