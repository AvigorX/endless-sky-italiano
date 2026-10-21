# STATO — L197 · `hai jobs.txt` (secondo lotto)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L197_20261019_202004` |
| Righe / unità | **492–967** / **36** — file al **75/175 (42,9%)** |
| Tipi | {'VALUE': 12, 'DESCRIPTION': 15, 'DIALOG': 9} |
| Tab · virgolette · apici | **0** · **0** · **0** (in entrambe le lingue) |
| Segnaposto | **81** su **11** simboli — 21 `<payment>` · 16 `<planet>` · 12 `<destination>` · 7 `<date>` · 4 `<cargo>` · 4 `<commodity>` · 4 `<npc>` · 4 `<bunks>` · 3 `<stopovers>` · 3 `<planet stopovers>` · 3 `<fare>` |
| Contesti | **15** — da `Delivery to Human Space [2]` a `Transport Hai farmers to <planet>` |
| Parole | **488 EN → 462 IT** (rapporto 0,86–1,14, media 1,02) |
| sha256 | `0ff30f8bb315b0ad…` |
| Esiti | `check.py` **29** (`FAIL 0`, exit 0) · `verify.py` **19** (`FAIL: 0`, exit 0) |

## Cosa contiene

| blocco | unità | righe | contenuto |
|---|---|---|---|
| consegna residua | 1 | 492 | la `DESCRIPTION` che il confine di L196 annunciava |
| ordini speciali Hai (3 tipi) | 2–13 | 516–601 | beni di lusso, cibo, elettronica: `<cargo>` da `<stopovers>`, `<commodity>` al ritorno |
| scorte verso spazio umano (4 taglie) | 14–21 | 606–756 | Small, Medium, Large, Extra Large: una sola resa per quattro `VALUE` |
| passeggeri Hai (3 taglie) | 22–27 | 811–862 | `Porta <fare> su <destination>` — stringa già presente in staging |
| famiglie Hai | 28–33 | 883–936 | trasloco e sbarco, due `VALUE` e due `DIALOG` uguali |
| minatori e contadini | 34–36 | 941–967 | due mestieri, stessa cornice; il contadino apre L198 |

## Difficoltà

1. **Nessun `TEXT`: i dialoghi sono `DIALOG`** (9 unità con contesto proprio). Il `TEXT` di L196 non si ripete.
2. **Tre simboli nuovi** nel file: `<stopovers>` (3), `<planet stopovers>` (3, **con uno spazio**) e `<fare>` (3). Un regex `<[^>]{1,10}>` troncherebbe il secondo.
3. **Zero virgolette e zero apici**: tre asserzioni vuote scritte comunque, per distinguere «niente da controllare» da «controllo mancato».
4. **Coerenza cross-lot**: `Bring <fare> to <destination>…` esisteva già ed era reso `Porta <fare> su <destination>…`; `This human wishes for <cargo>…` era già reso in L196. Il `check.py` confronta la resa con i lotti precedenti, non solo con se stessa.
5. **Quattro taglie, una resa**: le scorte Small/Medium/Large/Extra Large hanno lo stesso testo inglese e devono avere lo stesso italiano.

## Verifica

```bash
cd staging/editorial/L197_20261019_202004
python check.py     # FAIL totale: 0 (29 controlli)
python verify.py    # FAIL: 0 · exit 0 (19 controlli)
```

**Non verificato**: nessun lavoro accettato nel gioco, nessuna schermata vista, nessuna revisione umana; le 36 unità restano `PENDING`.
