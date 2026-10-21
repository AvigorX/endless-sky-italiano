# STATO — L262 (`data/remnant/remnant jobs.txt`, righe 226–490)

**Stato: CHIUSO.** Secondo lotto del file: **29 unità** su **quattro tipi** e **nove contesti**. Il file è aperto a
**54/87 (62,1%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L262_20261020_162037/` |
| file | `data/remnant/remnant jobs.txt` (87 unità · 1.462 parole · righe 19–741) |
| righe | 226–490 |
| unità | **29** — 9 `DIALOG` + 8 `VALUE` + 7 `DESCRIPTION` + **5 `MISSION_TEXT`** |
| parole | **423 EN → 439 IT** |
| rapporto | **0,95 – 1,34** |
| contesti | **9** — `Bounty 4`, `Bounty 5`, `Logistics Civil Engineering`, `… Industrial Delivery`, `… Outfitter Delivery`, `… Salvage Delivery`, `Rescue`, `Rescue 1B`, `Rescue 2` |
| tab / virgolette | **0 / 0** in entrambe le lingue |
| apici | **1 EN** (unità 6: `You've`) / **8 IT** su 7 unità (4, 15, 21, 22, 25, 26, 27:2) |
| segnaposto | **43** in **5** famiglie — `<payment>` 13, `<planet>` 12, `<npc>` 8, **`<cargo>` 8**, `<destination>` 2 |
| `check.py` | **25 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **21 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 25 prima · 29 qui · **33 dopo** la 490 |
| `sha256[:16]` | **`8b96c0e346eed37d`** |

## Comandi

```bash
python staging/editorial/L262_20261020_162037/check.py     # FAIL totale: 0 (25 controlli)
python staging/editorial/L262_20261020_162037/verify.py    # FAIL: 0 (21 controlli, 54/87)
```

## Le tre cose che il lotto doveva fare bene

1. **Le due stringhe iniziali ripetono L261** (`You have destroyed the Korath ship…`, `A Remnant military leader thanks
   you…`): riprese **alla lettera** dal `translation.json` di L261, e il `check.py` rilegge quel file per verificarlo —
   l'unico controllo del lotto che dipende da un altro lotto, ed è voluto.
2. **`Ember Waste` non si traduce**: 3 occorrenze, invariato; il corpus ha 13 casi identici. Il test vieta qualunque resa
   italiana («Brace», «braci»).
3. **`<cargo>` (8) senza articolo davanti** e `<planet>` (12) / `<destination>` (2) come **famiglie distinte**: verificati per
   famiglia, per ordine e con una regex che può fallire.

## `outfitter` → «emporio»

Il corpus traduce `outfitter` con **«emporio»** (59 occorrenze di «equipaggiamento», 63 di «fornitor-», ma il pannello di
gioco dice «emporio»). Il lotto usa «emporio» al singolare (unità 15) e «empori» al plurale (unità 18), e il test lo
verifica.

## Limiti dichiarati

Nessuna approvazione (29 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Restano **33 unità**.
