# STATO — L202 · `hai outfits.txt` (secondo lotto)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L202_20261019_205624` |
| Righe / unità | **205–484** / **16** — file al **24/65 (36,9%)** |
| Tipi | {'DESCRIPTION': 13, 'VALUE': 3} |
| Tab · virgolette · apici | **4** (unità 3, 10, 11, 15) · **0** · **2 EN / 10 IT** |
| Segnaposto | **0** (asserzione negativa scritta) |
| Contesti | **9** — da `Ionic Blaster Prototype` a `Bullfrog Anti-Missile` |
| Parole | **436 EN → 434 IT** (rapporto 0,98–1,50, media 1,12) |
| sha256 | `2281312fe0da11a4…` |
| Esiti | `check.py` **24** (`FAIL 0`, exit 0) · `verify.py` **17** (`FAIL: 0`, exit 0) |

## Cosa contiene

Armi e munizioni Hai: tre prototipi ionici, la famiglia Railgun dei droni Flea, i Tracker e la difesa anti-missile.

| blocco | unità | righe | contenuto |
|---|---|---|---|
| Ionic Blaster Prototype | 1 | 205 | pressione tecnologica degli Unfettered |
| Ionic Turret Prototype | 2–3 | 239–240 | più ionizzazione, meno danni; non producibile in serie |
| Skipper Railgun Slug / Rack / Railgun | 4–11 | 254–309 | tre `VALUE` e le loro descrizioni, più la battuta dei piloti |
| Hai Tracker | 12 | 361 | munizioni di un Tracker Pod |
| Tracker Storage Pod | 13 | 373 | deposito di munizioni |
| Hai Tracker Pod | 14–15 | 415–416 | armi a ricerca e la nota sulle munizioni |
| Bullfrog Anti-Missile | 16 | 484 | la difesa storica contro i Tracker |

## Difficoltà

1. **Tre `VALUE`** (`Skipper Railgun Slug`, `Skipper Slug Rack`, `Skipper Railgun`) copiati alla lettera; il testo intorno li usa come nomi propri.
2. **Stringa ripetuta**: le unità 11 e 15 hanno lo stesso inglese (`Ammunition for this weapon…`) e devono avere la stessa resa — verificato, non solo contato.
3. **Apici 2 contro 10**: l'inglese contrae (`There's`, `it's`), l'italiano elide (`L'Ionic`, `dell'energia`, `Quest'arma`, `dell'Ion Cannon`, `quest'arma` ×3, `d'urto`) e contrae una volta (`C'è`). Il numero non torna perché non deve.
4. **`outfitter`**: il glossario vieta il prestito e vuole «fornitore» come termine, «negozio di equipaggiamenti» nella prosa. Il lotto usa la forma di prosa, due volte.
5. **Resa tecnica**: `hit force` → «forza d'urto» (già in staging), `homing` → «a ricerca», `ionization` → «ionizzazione», `raw damage` → «danni grezzi», `recoil` → «rinculo».
6. **Errore del sorgente conservato**: l'inglese scrive *weapon jamming affects* (per *effects*). La resa traduce il senso, non l'errore — e lo dichiara in `review.md`.

## Verifica

```bash
cd staging/editorial/L202_20261019_205624
python check.py     # FAIL totale: 0 (24 controlli)
python verify.py    # FAIL: 0 · exit 0 (17 controlli)
```

**Non verificato**: nessun equipaggiamento installato nel gioco, nessuna schermata vista, nessuna revisione umana; le 16 unità restano `PENDING`.
