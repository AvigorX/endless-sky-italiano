# STATO — L183 · `human outfits.txt` (4 `VALUE`, armi d'abbordaggio, il Mug)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L183_20261019_192229` |
| Righe / unità | **390–514** / **15** — file al **50/63 (79,4%)** |
| Tipi | **11 `DESCRIPTION`** · **4 `VALUE`** — il massimo di `VALUE` finora |
| `UI_LABEL` · token · virgolette | **0** · **0** · **0** — tre asserzioni vuote scritte |
| Tab | **1** (idx 14) |
| Contesti | **10** (`Antigrav Glass` **3**, tre con 2, sei con 1) · **15 testi distinti** |
| Parole | **474 EN → 471 IT** (0,994) · rapporto **0,94–1,25**, media **1,07** |
| Apici | **3 inglesi**, tutti di elisione (`you're`, `you've`, `don't`) · **nessun possessivo** |
| sha256 | `c98a702886a3b041…` |
| Esiti | `check.py` **27** (`FAIL 0`) · `verify.py` **20**, exit **0** |

## I quattro `VALUE`

| idx | nome, copiato alla lettera | nota |
|---|---|---|
| 1 | `Luxury Accommodations` | plurale |
| 6 | `Fragmentation Grenades` | plurale |
| 9 | `Nerve Gas` | in prosa diventa «gas nervino» |
| 12 | `Antigrav Glasses` | **plurale nel nome, singolare nel contesto** (`outfit:Antigrav Glass`) |

L'ultimo è il caso interessante: il nome è **plurale** e il contesto **singolare**. Non è un errore da correggere — è il
dato, e il `check.py` verifica che il nome sia rimasto `Glasses`.

## Le tre voci del lotto

1. **Scheda tecnica** (idx 2–5, 7–8, 10): passeggeri, carburante, placcatura, fucili, barricata, gas.
2. **Battuta** (idx 11): «Puoi lanciarlo in caso di necessità, supponi.» — la scheda più corta del file.
3. **Mistero** (idx 15): la spada leggera con iscrizioni in una lingua che non è umana.

## Verifica

```bash
cd staging/editorial/L183_20261019_192229
python check.py     # FAIL totale: 0 (27 controlli)
python verify.py    # exit 0 (20 controlli)
```

**Non verificato**: nessun equipaggiamento visto a schermo; i testi non sono stati caricati nel gioco.
