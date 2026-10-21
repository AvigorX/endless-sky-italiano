# STATO — L263 (`data/remnant/remnant jobs.txt`, righe 491–682)

**Stato: CHIUSO.** Terzo lotto del file: **24 unità** su **6 contesti**, sei missioni di soccorso. Il file è aperto a
**78/87 (89,7%)**: resta **L264**, che sarà **terminale**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L263_20261020_164216/` |
| file | `data/remnant/remnant jobs.txt` (87 unità · 1.462 parole · righe 19–741) |
| righe | 491–682 |
| unità | **24** — 13 `MISSION_TEXT` + 6 `DESCRIPTION` + 5 `VALUE` |
| parole | **432 EN → 410 IT** |
| rapporto | **0,68 – 1,19** |
| contesti | **6** — `Rescue 2`, `Rescue 2B`, `Rescue 3`, `Rescue 3B`, `Rescue 4`, `Rescue 5` |
| tab / virgolette | **1** (unità 21, primo carattere) / **2** (unità 20) |
| apici | **0 EN** / **13 IT** su 11 unità |
| segnaposto | **28** in 3 famiglie — `<npc>` 17, `<destination>` 6, `<payment>` 5 |
| `check.py` | **23 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **21 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 54 prima · 24 qui · **9 dopo** la 682 |
| `sha256[:16]` | **`4c5f704d21f3c5fc`** |

## Comandi

```bash
python staging/editorial/L263_20261020_164216/check.py     # FAIL totale: 0 (23 controlli)
python staging/editorial/L263_20261020_164216/verify.py    # FAIL: 0 (21 controlli, 78/87)
```

## Eredità da L262 (8 unità verificate alla lettera)

| stringa inglese | unità | resa (ripresa da L262) |
|---|---|---|
| `You have returned, yet the <npc> is still missing.` | 3, 8, 12, 17 | «Sei tornato, ma la `<npc>` risulta ancora dispersa.» |
| `As you enter the system…The <npc> has been destroyed…` | 6, 15 | «Appena entri nel sistema… La `<npc>` è stata distrutta…» |
| `You land, and with a heavy heart…` | 7, 16 | «Atterri e, con il cuore pesante…» |
| `Search and Rescue: Retrieval` | 4 | copiato (`VALUE`) |

Il `check.py` **rilegge** `L262/translation.json` e pretende l'identità carattere per carattere.

## `<npc>` è una nave: 17 volte, sempre al femminile

«la `<npc>`», «è **scomparsa**», «è stata **distrutta**», «risulta ancora **dispersa**», «è **andata perduta** con tutto
l'equipaggio», «**Trovala**», «**aiutala** a tornare». Il `check.py` e il `verify.py` vietano le forme maschili
(`scomparso`, `distrutto`, `disperso`, `perduto`) e l'articolo maschile davanti al segnaposto.

## Anomalia misurata (da risolvere, non risolta qui)

`Ember Waste` nel corpus ha **due rese**: **«Distesa di Braci» in 69 unità** e **`Ember Waste` in 16** (su 85 unità che
contengono il nome). Il contratto di questo lotto impone **`Ember Waste` invariato**, ed è quello che il lotto fa (4
occorrenze); la discrepanza è **dichiarata** e non viene sanata qui, perché tocca 85 unità di lotti già chiusi.

## Limiti dichiarati

Nessuna approvazione (24 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana.
