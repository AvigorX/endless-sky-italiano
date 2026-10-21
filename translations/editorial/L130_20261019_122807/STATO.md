# STATO — L130 · `boarding missions.txt` (secondo lotto: 75 unità, il capitano Tarquin)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L130_20261019_122807` |
| Righe / unità | **417–686** / **75** |
| Tipi | **50 `MISSION_TEXT`** · **22 `UI_LABEL`** · **1 `CONVERSATION`** · **1 `DESCRIPTION`** · **1 `DIALOG`** |
| `VALUE` | **0** — asserzione **vuota scritta** (`Counter(...) == {}`) |
| Stati | **75 `PENDING`** — misurato e **asserito** |
| Contesti | **4** — 1 / 1 / 6 / **67** |
| Testi distinti | **74** per 75 unità (35 e 59 identiche) |
| Parole | **2087 EN → 2067 IT** (0,990); per unità 0,77–1,46, media 1,06 |
| Tab · virgolette | **45 unità** · **31** (unità 21 con **tre**) |
| Token | **19** in **5 famiglie**: `<origin>` 12, `<payment>` 2, `<bunks>` 2, `<destination>` 2, `<planet>` 1 |
| sha256 | `53f6d41b0bfedb6c…` |
| `check.py` | **30 controlli**, `FAIL totale: 0` |
| `verify.py` | **30 controlli**, exit **0** — invariante di **segmento** |

## Le 22 `UI_LABEL`, isolate una per una

`boarding alone` · `flagship is empty` · `first mate left on flagship` · `boarding with a big boarding party` ·
`first decision` · `crew missing` · `get to work` · `trickster or monster` · `attack with the element of surprise` ·
`attack but tarquin is prepared` · `attack alone with the element of surprise` · `attack alone but tarquin is
prepared` · `attack with a big boarding party` · `has brig` · `blackmailing with a big boarding party` ·
`blackmailing alone` · `the direct approach` · `acting stupid alone` · `bad luck` · `good luck` · `rescue the crew` ·
`rescue the crew with tarquin captured`

Sono **nomi di nodo** (unità 9, 10, 12, 14, 16, 22, 24, 36, 40, 41, 42, 44, 45, 54, 57, 60, 62, 63, 65, 67, 69, 72):
restano **identiche al sorgente**, escluse da «tutte tradotte», verificate con la lista esatta. Tutte le 22 del file
stanno in questo segmento: i lotti successivi non ne hanno.

## Zero `VALUE`

In questa finestra non c'è nessun `VALUE`. Il controllo è un'**asserzione vuota scritta**:

```python
ck('ZERO VALUE (asserzione vuota scritta)', collections.Counter(...) == {})
```

Non è un'omissione: se un lotto futuro introducesse un `VALUE` senza dichiararlo, il controllo resterebbe verde solo
perché scritto male — e non è questo il caso, perché la lista `[u['idx'] for u in SRC if u['kind'] == 'VALUE']` è
verificata `== []` **e** il `verify.py` la ripete.

## La battuta non chiusa

L'unità 21 (`Tarquin laughs self-consciously. "The truth is…`) ha **tre** virgolette: il sorgente apre due battute e
ne chiude una. La resa riproduce **tre** virgolette, e il `check.py` verifica che l'unica unità dispari sia la 21, con
esattamente 3.

## Le ripetizioni

`74` testi distinti su 75: le unità **35** e **59** hanno lo stesso inglese («You feel relieved that the whole
situation is over…») e quindi **la stessa resa**. Il costruttore la garantisce per costruzione, perché la resa è
indicizzata per indice ma il controllo finale confronta «stesso inglese ⇒ stessa resa» su tutte le 75.

## Contenuto

| contesto | unità | cosa succede |
|---|---|---|
| `boarding pirate` | 1 | la cassa di gettoni di credito |
| `Pirate Ambush` | 2 | la capsula che fugge, l'autodistruzione |
| `Pirate Mutiny` | 3–8 | i superstiti, i due diari, il pagamento |
| `Slave Crew Rescue` | 9–75 | Tarquin, il ponte di comando, le quattro strade: pagare, insistere, ricattare, attaccare — e i loro esiti |

## Verifica

```bash
cd staging/editorial/L130_20261019_122807
python mkparts.py   # 75 unità · 53 tradotti + 22 UI_LABEL identiche · 4 contesti · 0 VALUE
python check.py     # FAIL totale: 0 (30 controlli)
python verify.py    # exit 0 (30 controlli)
```
