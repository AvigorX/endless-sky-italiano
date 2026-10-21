# STATO — L165 · `avgi outfits.txt` (la torcia Arc, iniettore, estrattore, propulsori RCS)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L165_20261019_180721` |
| Righe / unità | **429–600** / **13** — file al **57/63 (90,5%)** |
| Tipi | **9 `DESCRIPTION`** · **4 `VALUE`** |
| `UI_LABEL` | **0** — asserzione vuota scritta |
| Token | **0** — asserzione vuota scritta |
| Contesti | **6** (Arc 3, Remass 2, Inductive 2, R-180 2, R-360 2, R-720 2) · **13 testi distinti** |
| Parole | **529 EN → 550 IT** (1,040); **0,99–1,20**, media **1,07** |
| Tab · virgolette | **2 unità** · **2** (in idx 1) |
| sha256 | `6081a66116d706e9…` |
| Esiti | `check.py` **22** (`FAIL 0`) · `verify.py` **19**, exit **0** |

## Cosa contiene

| blocco | unità | righe | contenuto |
|---|---|---|---|
| torcia `Arc` | 1-3 | 429-454 | `VALUE`, la fusione D-D catalizzata, la nota sull'ugello |
| componenti della torcia | 4-7 | 497-519 | `Remass Injector` (postbruciatore), `Inductive Extractor` (spinta in energia) |
| propulsori RCS | 8-13 | 523-600 | `R-180`, `R-360`, `R-720`: acqua surriscaldata, MHD, manovra |

## Rese che contano

| EN | IT |
|---|---|
| `specific impulse for raw thrust` | **impulso specifico con la spinta pura** |
| `catalyzed D-D fusion` | **fusione D-D catalizzata** |
| `afterburning capabilities` | **capacità di postbruciatore** |
| `magnetic nozzle slot` | **slot per ugello magnetico** |
| `inductively extracted` | **estratto per induzione** |
| `reaction control thrusters` | **propulsori per il controllo d'assetto** |
| `'teakettle' style` | **in stile 'teiera'** |

## Verifica

```bash
cd staging/editorial/L165_20261019_180721
python check.py     # FAIL totale: 0 (22 controlli)
python verify.py    # exit 0 (19 controlli)
```

**Segmento**: 44 unità prima della riga 429, 13 nel lotto, **6 dopo** la 600; confine alla riga 616.
**Riuso verificato**: idx 3 è la stessa nota sull'ugello di L164 e il controllo la confronta con la resa già scritta.

**Non verificato**: nessuna nave o equipaggiamento visto a schermo; i testi non sono stati caricati nel gioco.
