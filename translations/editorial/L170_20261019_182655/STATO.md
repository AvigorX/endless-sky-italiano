# STATO — L170 · `paradise world jobs.txt` (pensionati illegali, ritiro nella natura, quattro `Shipment`)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L170_20261019_182655` |
| Righe / unità | **526–691** / **20** — file al **89/131 (67,9%)** |
| Tipi | **8 `VALUE`** · **8 `DESCRIPTION`** · **3 `DIALOG`** · **1 `MISSION_TEXT`** |
| `UI_LABEL` | **0** — asserzione vuota scritta |
| Token | **39** su **7** simboli, con **`<martini house>`** 1 (composto) |
| Contesti | **8** · **14 testi distinti** su 20 |
| Parole | **496 EN → 516 IT** (1,040); **0,95–1,16**, media **1,00** |
| Tab · virgolette | **0** · **12** (record) in idx 2, 3, 6, 9, 10 |
| sha256 | `900e58542d06ef12…` |
| Esiti | `check.py` **27** (`FAIL 0`) · `verify.py` **23**, exit **0** |

## Cosa contiene

| blocco | unità | righe | contenuto |
|---|---|---|---|
| pensionati «illegali» | 1-7 | 526-574 | due missioni quasi identiche, una porta alla multa, l'altra no |
| ritiro nella natura | 8-10 | 578-599 | pseudo-celebrità e guide naturalistiche agghindate |
| quattro `Shipment` | 11-18 | 603-668 | Gemini Shipyards ×2, Lovelace Labs, Polymath Nanoinstruments |
| evacuazione Martini | 19-20 | 690-691 | la famiglia con la `<martini house>` distrutta |

## Le virgolette (record: 12)

| unità | virgolette | frase citata |
|---|---|---|
| 2, 6 | 2 + 2 | `"pensionati"` |
| 3 | 4 | `"pensionati"` + `"averi più cari"` |
| 9 | 2 | `"Ritiro nella Natura"` |
| 10 | 2 | `"guide naturalistiche"` |

## Il refuso del sorgente

`idx 4` dice `an anonymous source`, `idx 7` dice `an anyonymous source`: **un refuso nel testo inglese**, non una
differenza di senso. In italiano le due rese sono **identiche** («da una fonte anonima»), e un controllo lo pretende.
Le 20 unità producono così **14 testi distinti** invece di 13.

## Verifica

```bash
cd staging/editorial/L170_20261019_182655
python check.py     # FAIL totale: 0 (27 controlli)
python verify.py    # exit 0 (23 controlli)
```

**Non verificato**: nessuna missione vista a schermo; i testi non sono stati caricati nel gioco.
