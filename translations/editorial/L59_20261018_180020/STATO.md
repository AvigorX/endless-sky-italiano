# STATO — L59 · `data/human/culture conversations.txt`

**Lotto chiuso.** 42/42 unità tradotte, righe **225–423**.

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L59_20261018_180020` |
| File | `data/human/culture conversations.txt` (secondo lotto sul file) |
| Unità | **42** (righe 225–423) |
| Parti | **4** — 11 · 12 · 18 · 1 |
| Contesti | **10** — `Curious Waiter` 1–11, `Syndicated Security Troops` 12–13, `Class Trip to Port` 14–14, `Old Defense Turrets` 15–16, `Blind Landing` 17–23, `Forest Fire` 24–34, `Local Politics` 35–36, `Military Response Test` 37–39, `Missed Mugging` 40–41, `Sojourn Sunday Sales` 42–42 |
| Tipi | **42 `MISSION_TEXT`** e nient'altro |
| Parole | 1.475 EN → 1.402 IT (**0,950**) |
| Rapporto per unità | **0,70 – 1,71** (gate 0,55–1,90) |
| `UI_LABEL` / `DIALOG` / `LOGBOOK` / `CONVERSATION` / `TEXT` | **0 / 0 / 0 / 0 / 0** — assenze dichiarate |
| Tab · virgolette | **32** · **34** (0 dispari, 0 quadre, 0 backtick) |
| Token `<…>` | **0** (parità 0/0 asserita) |
| Duplicati inglesi | **0 gruppi** — controllo negativo dichiarato |
| sha256 `translation.json` | `5d42121563e61f8d…` |
| `check.py` | **33 controlli**, `FAIL totale: 0` |
| `verify.py` | **35 controlli**, exit **0** |

## Dove siamo nel file

| Voce | Valore |
|---|---|
| Unità prima della 225 | **43** (L58) |
| Unità dopo la 423 | **289** |
| Unità totali del file | **374** |
| Copertura | **85/374 (22,7%)** |
| `max(line)` | **1122** |

Segmento **interno**: né apre né chiude il file. `verify.py` asserisce `43 prima / 289 dopo / 374 totali`
e la copertura **per segmento** (decisione 158).

## Cosa è stato deciso qui

1. **Primo lotto della serie con 0 duplicati inglesi.** Il controllo non sparisce: diventa un'asserzione
   negativa (`len(dup_en) == 0`), altrimenti «nessun duplicato» e «controllo assente» sarebbero la stessa
   cosa nel referto.
2. **`katsu don`** (unità 1) resta invariato: è un piatto reale e il testo dice «a local version of». La
   traduzione mantiene il nome e aggiunge solo «versione locale».
3. **`Tonner`** (unità 12) resta invariato e fra virgolette: nel sorgente è il nomignolo fra virgolette
   (`` "Tonners" ``), non un nome proprio nudo. La parità delle virgolette (34 = 34) lo impone.
4. **Il cameriere curioso** (unità 1–11) è il primo personaggio del file che fa una domanda diretta al
   giocatore: tre risposte, tre registri (cinico, poetico, prudente). La traduzione non le mescola.
5. **L'incendio** (24–34) è la scena più lunga del lotto e ha un lessico tecnico preciso: «retardants» →
   «ritardanti», «perimeter» → «perimetro», «air traffic control» → «controllo del traffico aereo».
6. **`"overlords"`** (unità 35) resta fra virgolette e reso «signori»: il virgolettato è ironico nel
   sorgente e deve restarlo.

## Verifica

```bash
cd staging/editorial/L59_20261018_180020
python check.py                 # FAIL totale: 0   (33 controlli)
python verify.py                # exit 0           (35 controlli)
```

## Prossimo passo

**L60** — stesso file, righe **429–…**, primo contesto `Tarazed Ship Christening`. Il file resta aperto:
289 unità dopo la 423.
