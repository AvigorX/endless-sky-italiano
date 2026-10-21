# STATO — L64 · `data/human/culture conversations.txt`

**Lotto chiuso.** 42/42 unità tradotte, righe **723–810** (finestra di export 712–810: la prima unità sta
sulla 723).

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L64_20261018_181613` |
| File | `data/human/culture conversations.txt` (settimo lotto sul file) |
| Unità | **42** (righe 723–810) |
| Parti | **2** — 25 · 17 |
| Contesti | **2** — `Burthen Triathlon` 1–25, `CCOR Guerrilla Standoff` 26–42 |
| Tipi | **38 `MISSION_TEXT` + 4 `UI_LABEL`** |
| Parole | 1.652 EN → 1.598 IT (**0,967**) |
| Rapporto per unità | **0,85 – 1,27** (gate 0,55–1,90) |
| `UI_LABEL` (`NT`) | **4** — unità **15** `no credits`, **18** `leave tent`, **22** `after tent`, **24** `end` |
| `DIALOG` / `LOGBOOK` / `CONVERSATION` / `TEXT` | **0 / 0 / 0 / 0** — assenze dichiarate |
| Token `<…>` | **0** — assenza dichiarata |
| Tab · virgolette | **45** (36 righe con tab iniziale) · **23**, con **3 dispari** (unità **35, 36, 37**) riprodotte |
| Duplicati inglesi | **0 gruppi** |
| sha256 `translation.json` | `57a238ca0241c4ca…` |
| `check.py` | **33 controlli**, `FAIL totale: 0` |
| `verify.py` | **36 controlli**, exit **0** |

## Dove siamo nel file

| Voce | Valore |
|---|---|
| Unità prima della 723 | **209** (L58–L63) |
| Unità dopo la 810 | **123** |
| Copertura | **251/374 (67,1%)** |

## Cosa è stato deciso qui

1. **Quattro `UI_LABEL` come chiavi di diramazione**: `no credits`, `leave tent`, `after tent`, `end`
   selezionano rami diversi della missione. Restano identiche: tradurle cambierebbe il flusso, non il testo.
2. **Tre virgolette dispari consecutive** (35, 36, 37): sono gli incipit dei tre passaggi del discorso del
   guerrigliero CCOR, aperti e **non chiusi** nel sorgente. Riprodotte; `verify.py` confronta l'insieme
   `(35, 36, 37)`.
3. **Due registri**: la gara su Burthen (cronaca sportiva, folla, altoparlante) e il comizio a Gagarin
   (oratoria politica, esortativa). Non si uniformano: la prima è descrittiva, la seconda è retorica.
4. **Il lessico politico** si ancora a quello già usato nei lotti delle campagne:
   `Syndicate` → **Sindacato**, `Paradise Worlds` → **Mondi del Paradiso**, `Outer Rim` → **Bordo Esterno**,
   `Republic` → **Repubblica**, `Confederated Councils` → **Consigli Confederati**.
5. **Un errore trovato dai controlli**: le unità 7 e 29 erano rese entrambe «(Torna alla mia nave.)» ma
   l'inglese distingue *Return to my ship* da *Go back to my ship*: la 29 è diventata «(Torna indietro alla
   mia nave.)». Il controllo `duplicati italiano non spiegati dal sorgente` l'ha rilevato.
6. **`Antigrav`** resta invariato (nome commerciale della bibita), fra virgolette come nel sorgente.

## Verifica

```bash
cd staging/editorial/L64_20261018_181613
python check.py                 # FAIL totale: 0   (33 controlli)
python verify.py                # exit 0           (36 controlli)
```

## Prossimo passo

**L65** — stesso file, righe **819–920**, **43 unità**, 4 contesti, 1.666 parole, tab 45, virgolette 22,
4 `UI_LABEL` (10, 12, 14, 16), **2 token** (`<origin>`, `<ship>`), 1 gruppo di duplicati.
