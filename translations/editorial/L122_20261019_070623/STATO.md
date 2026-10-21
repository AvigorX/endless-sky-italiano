# STATO — L122 · `data/human/campaign events.txt` (terzo lotto, **chiude il file**: 42 unità)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L122_20261019_070623` |
| Righe / unità | **1338–3468** / **42** — ultima unità del file |
| Tipi | **41 `DESCRIPTION`** · **1 `MISSION_TEXT`** |
| Stati | **42 `PENDING`** — misurato e **asserito** in `mkparts.py` |
| Contesti | **18** — 8×2, 4×1, 4×4, 2×3 |
| Testi distinti | **36** per 42 unità — **3 già resi in L120/L121**, 33 nuovi |
| Parole | **2220 EN → 2191 IT** (0,987); per unità 0,86–1,16, media 1,04 |
| Tab | **21 unità** con `\t` iniziale |
| Virgolette | **8** — solo nelle unità 19, 21 e 32 |
| Token · quadre | **0** · **0** — asserzioni scritte (`== {}`) |
| sha256 | `3ff793b7a7ed6422…` |
| `check.py` | **32 controlli**, `FAIL totale: 0` |
| `verify.py` | **30 controlli**, exit **0** — invariante **di file** |

## Il file è chiuso

```
data/human/campaign events.txt   150/150 unità (100,0%) · 6961 EN -> 6788 IT · 3 lotti
L120 28–242 (52) · L121 282–1332 (56) · L122 1338–3468 (42)
verify L122: 150/150 righe coperte · sovrapposti = 0 · max(line) = 3468
```

`campaign events.txt` è il **quarto file di grandi dimensioni chiuso** della campagna recente (dopo `human
missions`, `planets`, `tooltips`, `pirate jobs`) e porta i **file completi a quarantaquattro**.

## Zero token, zero quadre: asserzioni, non omissioni

Questo è il primo lotto di `campaign events.txt` **senza nessun token**. Il controllo è scritto
`Counter(...) == {}` per entrambi i lati (inglese e italiano) e `not [...]` per le quadre: se un token comparisse
dove non deve, il lotto fallisce. Un'asserzione omessa qui sarebbe una porta aperta.

## La memoria di traduzione

Cinque unità condividono il testo con i lotti precedenti e la resa è **la stessa**, verificata leggendo i
`translation.json` di L120 e L121:

| unità | testo | viene da |
|---|---|---|
| 1, 6, 33 | il porto di Deep con la Poseidon Industries | L121 |
| 9 | la colonia mineraria di Clink | L121 |
| 29 | New Austria, il mondo montuoso | L121 |

## Contenuto

- **Memoriale di Deep** (1–2, 6–7, 33–34): il porto, le pareti di granito, i tre stadi dell'ampliamento.
- **New Iceland** (3–5, 26–28): il mondo vulcanico, le maschere antipolvere, la base della Marina abbandonata.
- **Clink** (8–9): la colonia penale dei Mondi Liberi e la miniera di terre rare.
- **Poisonwood** (10–13): il porto di rottami, la taverna «The Parting Glass» e il ritorno della Repubblica.
- **Bloodsea** (14–21): il mondo rosso, il porto nuovo, il gergo dei pirati, l'«indipendenza».
- **Albatross** (22–23): gli anarchici, i pirati, la liberazione scettica.
- **Covert** (24–25): il cartello minerario, l'uranio, la flotta pirata.
- **Geminus ricostruita** (35–38): l'Arsenale nuovo, lo spazioporto funzionale, l'area ristorazione.
- **Martini** (39–42): la capitale nuova e il vecchio spazioporto con le guglie nere.

## Verifica

```bash
cd staging/editorial/L122_20261019_070623
python mkparts.py   # 42 unità · 36 testi distinti (3 da L120/L121) · 21 tab · 8 virgolette · 0 token
python check.py     # FAIL totale: 0 (32 controlli)
python verify.py    # exit 0 (30 controlli) — 150/150 righe coperte, sovrapposti 0
```
