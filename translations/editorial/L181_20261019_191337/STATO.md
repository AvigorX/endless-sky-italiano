# STATO — L181 · `human outfits.txt` (disturbatori, ramscoop, iperguida)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L181_20261019_191337` |
| Righe / unità | **158–233** / **9** — file al **21/63 (33,3%)** |
| Tipi | **9 `DESCRIPTION`** · **0 `VALUE`** — niente da copiare |
| `UI_LABEL` · token · virgolette | **0** · **0** · **0** — tre asserzioni vuote scritte |
| Tab | **2** (idx 4 e 7) — in L180 erano 0 |
| Contesti | **7** (`Ramscoop` 2, `Hyperdrive` 2, cinque con 1) · **9 testi distinti** |
| Parole | **477 EN → 476 IT** (0,998) · rapporto **1,02–1,16**, media **1,09** |
| Apici | **1** in inglese (idx 2, `ship's`) · nessun possessivo in italiano |
| sha256 | `4a13b745b4c7e37b…` |
| Esiti | `check.py` **25** (`FAIL 0`) · `verify.py` **19**, exit **0** |

## Cosa contiene

| blocco | unità | righe | contenuto |
|---|---|---|---|
| disturbatori radar | 1-2 | 158-169 | `Small` e `Large Radar Jammer`, contro i missili a guida radar |
| ramscoop | 3-5 | 181-206 | il passato (colonie rade), il vento solare, il `Catalytic Ramscoop` del Deep |
| iperguida | 6-8 | 206-220 | la scatola misteriosa, la vespa e la foglia, i dodici che la capiscono, lo `Scram Drive` |
| jump drive | 9 | 233 | il campo di contenimento: **non** si può ricostruire a ritroso |

## Due cose che il lotto insegna

**Il `VALUE` può mancare**: nove unità di sola prosa, nessun nome da copiare. La riga 236 — **fuori** dal lotto — è
invece un `VALUE`: il tipo del confine si **misura**, non si eredita.

**La metafora non si spiega**: la vespa che punge la foglia di quercia per deporvi le uova resta una vespa, non diventa
«un meccanismo di inserimento». È la prova che la voce del file sa cambiare registro.

## Verifica

```bash
cd staging/editorial/L181_20261019_191337
python check.py     # FAIL totale: 0 (25 controlli)
python verify.py    # exit 0 (19 controlli)
```

**Non verificato**: nessun equipaggiamento visto a schermo; i testi non sono stati caricati nel gioco.
