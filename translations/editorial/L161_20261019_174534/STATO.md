# STATO — L161 · `avgi outfits.txt` (le lamine radiative e i ramscoop; apre il file)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L161_20261019_174534` |
| Righe / unità | **18–99** / **11** — file al **11/63 (17,5%)** |
| Tipi | **9 `DESCRIPTION`** · **2 `VALUE`** |
| `UI_LABEL` | **0** — asserzione vuota scritta |
| Token | **0** — asserzione vuota scritta |
| Contesti | **5** (Radiative 3, Concealment 3, Magnetic 2, Plasmadyne 2, Slush 1) · **10 testi distinti** |
| Parole | **578 EN → 608 IT** (1,052); **1,00–1,27**, media **1,11** |
| Tab · virgolette | **4 unità** · **0** |
| sha256 | `342d227d771ad013…` |
| Esiti | `check.py` **24** (`FAIL 0`) · `verify.py` **20**, exit **0** |

## Cosa contiene

| blocco | unità | righe | contenuto |
|---|---|---|---|
| lamine radiative | 1-3 | 18-29 | `VALUE`, i radiatori a microcanali, i punti di attacco esterni |
| lamine mimetiche | 4-6 | 33-48 | `VALUE`, il rivestimento a punti quantici, la nota sugli attacchi |
| Magnetic Scoop | 7-8 | 63-64 | la storia dei ramscoop Avgi, i laser ionizzanti |
| Plasmadyne Scoop | 9-10 | 84-85 | il magnete al plasma, il campo di centinaia di chilometri |
| Deuterium Slush Tank | 11 | 99 | la poltiglia di deuterio e il criorefrigeratore |

## Rese che contano

| EN | IT |
|---|---|
| `Radiative Laminae` · `Concealment Laminae` | **identici** (2 `VALUE`) |
| `graphene microchannel radiators` | **radiatori a microcanali di grafene** |
| `mounted conformally to a ship's hull` | **montato in modo conforme allo scafo** |
| `outfit space` | **spazio per gli equipaggiamenti** |
| `quantum dot phased array` | **schiera in fase a punti quantici** |
| `ramscoop` (prosa) | **ramscoop**, invariato |
| `deuterium slush` | **poltiglia di deuterio** |
| `zero-boiloff system` | **sistema a zero ebollizione** |

## Verifica

```bash
cd staging/editorial/L161_20261019_174534
python check.py     # FAIL totale: 0 (24 controlli)
python verify.py    # exit 0 (20 controlli)
```

**Il lotto apre il file**: 0 unità prima della riga 18, 52 dopo la 99, confine alla riga 112.

**Non verificato**: nessuna nave o equipaggiamento visto a schermo; i testi non sono stati caricati nel gioco.
