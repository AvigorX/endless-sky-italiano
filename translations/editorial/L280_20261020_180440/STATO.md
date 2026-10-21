# STATO — L280 (`data/human/kestrel.txt`, righe 252–402)

**Stato: CHIUSO — LOTTO TERMINALE.** Il file è **completo: 51/51 (100%)**, **ventesimo file interamente tradotto** su 167.

| voce | valore |
|---|---|
| directory | `staging/editorial/L280_20261020_180440/` |
| file | `data/human/kestrel.txt` (**51/51 unità · 1.064 parole · righe 15–402**) |
| righe | 252–402 |
| unità | **2** — 1 `MISSION_TEXT` + 1 `DESCRIPTION` |
| parole | **105 EN → 103 IT** (0,98) |
| rapporto | **1,02 – 1,05** |
| contesti | **2** — `mission:Kestrel Available` · `ship:Kestrel` |
| tab / virgolette | **0** / **2** (dritte) |
| segnaposto | **1** — `<last>` |
| apici | **2 EN** (`We've`, `Tarazed's`) / **1 IT** (`un'astronave`) |
| `check.py` | **22 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **19 controlli, `FAIL: 0`**, exit 0 |
| invarianti | **di segmento** (49 prima · 2 qui · **0 dopo**) **e di FILE** (51 unità · righe distinte · ultima 402 · somma dei 3 lotti = 51) |
| `sha256[:16]` | **`79738400502412fd`** |

## Comandi

```bash
python staging/editorial/L280_20261020_180440/check.py     # FAIL totale: 0 (22 controlli)
python staging/editorial/L280_20261020_180440/verify.py    # FAIL: 0 (19 controlli, 51/51)
```

## Le due unità

1. **il messaggio** (`MISSION_TEXT`): Atinoda annuncia che «la nostra ultima nave da guerra è ora in vendita qui su
   Wayfarer», ringrazia e conferma che i suggerimenti sono entrati nel progetto finale;
2. **la scheda della nave** (`DESCRIPTION`): il **progettista capo** cadde in trance in una **capanna del sudore** e vide «un
   astronauta strana ed elegante»; tornò al lavoro e passò **sette anni** a rendere reale la Kestrel.

## Coerenza con L278

La `DESCRIPTION` racconta **la stessa scena** dell'unità 6 di L278. Il `check.py` riapre `L278/translation.json` e verifica che
le espressioni chiave — «capanna del sudore», «trance» — siano **le stesse**. Senza quel confronto, la scheda avrebbe potuto
descrivere la visione con parole diverse da quelle usate nel dialogo, e il giocatore avrebbe letto due versioni.

## Limiti dichiarati

Nessuna approvazione (2 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Il file è **finito in
staging**, non **approvato**.
