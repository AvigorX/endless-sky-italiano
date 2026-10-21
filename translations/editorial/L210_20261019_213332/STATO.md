# STATO — L210 · `coalition news.txt` (quinto lotto)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L210_20261019_213332` |
| Righe / unità | **309–400** / **19** — file al **96/112 (85,7%)** |
| Tipi | {'NEWS': 19} |
| Tab · virgolette · apici | **0** · **38** (2 per unità) · **4 EN / 24 IT** |
| Segnaposto | **0** (asserzione negativa scritta) |
| Contesti | **5** — vendor 2, civilian expeditions past 5, heliarch expeditions past 5, games people 6, games planet heliarch 1 |
| Parole | **458 EN → 437 IT** (rapporto 0,94–1,30, media 1,09) |
| sha256 | `ee5ce8eed7ac5542…` |
| Esiti | `check.py` **23** (`FAIL totale: 0`) · `verify.py` **17** (`FAIL: 0`) |

## Cosa contiene

Il lotto entra nei **Giochi della Coalizione** — un venditore di ninnoli, sei spettatori, un ex atleta che ora organizza
l'evento — e chiude il filone della **spedizione dell'ispettrice Sedlitaris**, promossa *arbiter* al ritorno
dall'esterno: cinque voci tra civili e Heliarch, con i consoli furiosi l'uno con l'altro.

## Difficoltà

1. **`Coalition Games` → «Giochi della Coalizione»**, sette occorrenze, coerente con la scelta di L206. Il controllo
   confronta il numero di occorrenze nelle due lingue invece di fissare una costante.
2. **Titoli della Coalizione**: `arbiter` resta prestito latino (come `magister` e `consul`), `consuls` al plurale diventa
   «consoli», `tribune` diventa «tribuno». Sono titoli comuni, non nomi propri: si traducono, ma `arbiter` no perché in
   italiano «arbitro» significa altro.
3. **22 apici italiani contro 4 inglesi**: il testo è pieno di elisioni (`dall'esterno`, `quell'ispettrice`, `l'uno`,
   `Un'esperienza`). Ogni apice è legato alla sua unità nel controllo.
4. **Unità 9 con `'spedizione'` fra apici singoli**: il disprezzo del parlante sta nelle virgolette, e va conservato.
5. **Due errori miei corretti prima di chiudere**: cercavo `'field trip'` senza la virgola interna; e pretendevo
   `endswith('acquisto')` su una stringa che finisce con `acquisto."` — il punto e la virgoletta fanno parte della
   stringa.

## Verifica

```bash
cd staging/editorial/L210_20261019_213332
python check.py     # FAIL totale: 0 (23 controlli)
python verify.py    # FAIL: 0 (17 controlli) · confine riga 401, stesso contesto
```

**Non verificato**: nessuna schermata vista, nessuna revisione umana; 19 unità `PENDING`.
