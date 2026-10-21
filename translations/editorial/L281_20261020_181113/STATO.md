# STATO — L281 (`data/quarg/quarg news.txt`, righe 23–490)

**Stato: CHIUSO — LOTTO TERMINALE.** Il file è **completo: 50/50 (100%)**, **ventunesimo file interamente tradotto** su 167.

| voce | valore |
|---|---|
| directory | `staging/editorial/L281_20261020_181113/` |
| file | `data/quarg/quarg news.txt` (**50/50 unità · 778 parole · righe 23–490**) |
| righe | 23–490 (**l'intero file**: il contratto ne prevedeva 23–483) |
| unità | **50** — 40 `NEWS` + 10 `TEXT` |
| di cui | **22 di prosa** (tradotte) + **28 delimitatori** (`"`, copiati e dichiarati `ID_OK`) |
| parole | **778 EN → 727 IT** (0,93) |
| rapporto | **0,82 – 1,28** (sulle 22 di prosa) |
| contesti | **10** `news:` / `phrase:` |
| tab / segnaposto | **0 / 0** (asserzioni negative) |
| virgolette | **44** (28 nei delimitatori + 16 nella prosa), **per unità** |
| apici | **14 EN** / **20 IT** |
| `check.py` | **22 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **19 controlli, `FAIL: 0`**, exit 0 |
| invarianti | **di segmento** (0 prima · 50 qui · **0 dopo**) **e di FILE** (50 unità · righe distinte · ultima 490 · copertura 50/50) |
| `sha256[:16]` | **`ae78081e75f50c86`** |

## Comandi

```bash
python staging/editorial/L281_20261020_181113/check.py     # FAIL totale: 0 (22 controlli)
python staging/editorial/L281_20261020_181113/verify.py    # FAIL: 0 (19 controlli, 50/50)
```

## Il contratto era sbagliato, e il workspace ha vinto

Il contratto L281 prevedeva **43 unità alle righe 23–483**. Misurato, il file è diverso:

1. **è composto da frammenti**: le notizie sono costruite da blocchi `word` con frammenti fra virgolette (`"Are you"`,
   `" "`, `"a merchant"`…), e l'estrattore espone **solo** le stringhe fra backtick;
2. di conseguenza le unità sono **50**: **28 delimitatori** (l'unica stringa `` `"` ``) sparse fino alla riga 444, e **22
   unità di prosa** concentrate alle righe 23, 455-465 e **481-490**;
3. la finestra 23–483 **tagliava sette unità di prosa** (484-490) e includeva quasi solo delimitatori.

Il lotto è stato quindi **risegato sull'intero file (23–490)**, che chiude: 22 traduzioni reali + 28 copie dichiarate.

## La lacuna dell'estrattore, dichiarata

I frammenti **senza backtick** (`` "Are you" ``, `` " " ``, `` "a merchant" ``…) **non sono nel database** e non sono
traducibili: la notizia composta resta in inglese in quei pezzi. Non è stato «riparato» (gli strumenti sono protetti): è
**dichiarato qui** e nel `check.py`, che stampa la nota a ogni esecuzione.

## Il contenuto tradotto

- **`news:quarg anywhere`** (11 unità): i Quarg che parlano al giocatore — rifiuto della tecnologia («È meglio che gli umani
  crescano e si sviluppino da soli»), pazienza, benvenuto condizionato — e quattro **scene di vita** (la folla silenziosa, il
  barattolo che cambia forma, i piccoli in gita, il gruppo che si alza all'unisono);
- **`phrase:ringworld quarg phrases`** (10 unità): **istantanee** del mondo ad anello — il genitore che mostra l'anello al
  piccolo, i Quarg che toccano le pareti, la scorta corazzata, i carrelli da laboratorio, le centinaia sedute in silenzio, lo
  sguardo che ti fissa, il conteggio dei container, lo scambio di equipaggi, il festival del frutto, il Quarg svanito.

## Limiti dichiarati

Nessuna approvazione (50 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Il file è **finito in
staging**, non **approvato**.
