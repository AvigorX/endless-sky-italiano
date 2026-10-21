# STATO — L140 · `data/hai/unfettered 0 prologue.txt` (file nuovo: il primo contatto con gli Slegati)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L140_20261019_145902` |
| Righe / unità | **22–81** / **25** — file al **17,0%** (25/147) |
| Tipi | **25 `MISSION_TEXT`** |
| `VALUE` · `UI_LABEL` · token | **0** · **0** · **0** — tre asserzioni vuote scritte |
| Stati | **25 `PENDING`** — misurato e **asserito** |
| Contesto | **1** — `mission:First Contact: Unfettered` |
| Testi | **21 distinti** su 25 — quattro coppie ripetute |
| Parole | **405 EN → 375 IT** (0,926); per unità 0,76–1,29, media 1,05 |
| Tab · virgolette | **23 unità** · **50** (sei unità con quattro), nessuna dispari |
| sha256 | `ed2e17388b122b8f…` |
| `check.py` | **31 controlli**, `FAIL totale: 0` |
| `verify.py` | **25 controlli**, exit **0** — invariante di **segmento** |

## Il primo contatto

Un pianeta di **Hai Slegati** — «una specie aliena ostile che somiglia a scoiattoli giganti e intelligenti» — e un
dialogo costruito su due rami paralleli (un primo incontro e un secondo, con le stesse battute al plurale), più le
domande del giocatore.

La voce degli Slegati è **sprezzante e mitologica**: chiamano gli umani «scimmie», si dicono «gli inalterati», «gli Hai
conquistatori», e ripetono il loro motto come una litania.

## Il motto, cinque volte identico

> «Eravamo padroni di cento mondi quando le scimmie umane non avevano ancora imparato a usare i pollici.»

Compare nelle unità **15, 16, 17, 20 e 23**, in quattro costruzioni diverse (due chiudono frasi già iniziate). È una
**costante sola**, e il controllo ne verifica il numero di occorrenze:

```python
ck('il motto degli Slegati compare 5 volte, sempre identico',
   ' '.join(v['italian'] for v in cov).count(MOTTO) == 5)
```

## Quattro coppie ripetute

| frase | unità |
|---|---|
| `(Sure.)` | 2, 9 |
| `(Not now, it's too risky.)` | 3, 10 |
| `"What do you mean, 'true Hai'?"` | 6, 13 |
| `"We fight to defend ourselves from extinction," they say.` | 18, 21 |

I due rami della missione devono dire le **stesse parole**: se divergessero, il giocatore leggerebbe due testi diversi
per la stessa scelta.

## Una sgrammaticatura riprodotta

Il sorgente scrive «Although despite their hostility while in orbit, they pay little mind to you on the surface» —
due connettivi in fila. La resa è «**Sebbene, nonostante** la loro ostilità in orbita…»: la goffaggine resta, perché
ripulirla sarebbe una scelta dell'autore, non del traduttore.

## Verifica

```bash
cd staging/editorial/L140_20261019_145902
python mkparts.py   # 25 unità · 21 distinti · motto ×5 · 23 tab · 50 virgolette
python check.py     # FAIL totale: 0 (31 controlli)
python verify.py    # exit 0 (25 controlli, invariante di segmento)
```

**Non verificato**: nessuna missione giocata; il primo contatto non è stato visto a schermo.
