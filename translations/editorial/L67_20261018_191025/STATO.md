# STATO — L67 · `data/human/culture conversations.txt`

**Lotto chiuso, e chiude il file: 374/374.**

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L67_20261018_191025` |
| File | `data/human/culture conversations.txt` (decimo e ultimo lotto) |
| Unità | **35** (righe 1062–1122) |
| Parti | **2** — 17 · 18 |
| Contesti | **2** — `Exotic Life: Delve` 1–17, `Exotic Life: Ada` 18–35 |
| Tipi | **34 `MISSION_TEXT` + 1 `LOGBOOK`** |
| Parole | 811 EN → 787 IT (**0,971**) |
| Rapporto per unità | **0,81 – 1,38** (gate 0,55–1,90) |
| `UI_LABEL` / `DIALOG` / `CONVERSATION` / `TEXT` | **0 / 0 / 0 / 0** — assenze dichiarate |
| `LOGBOOK` | **1** — unità **1** (riga 1062), forma **backtick**, testo tradotto |
| Token `<…>` | **2** — `<ship>` (unità 2 e 17), parità 2/2 |
| Tab · virgolette | **32** · **68** (0 dispari, 0 quadre, 0 backtick) |
| Duplicati inglesi | **0 gruppi** |
| sha256 `translation.json` | `ad997eaa9007d7c2…` |
| `check.py` | **33 controlli**, `FAIL totale: 0` |
| `verify.py` | **38 controlli**, exit **0** |

## Dove siamo nel file

| Voce | Valore |
|---|---|
| Unità prima della 1062 | **339** (L58–L66) |
| Unità dopo la 1122 | **0** |
| Copertura | **374/374 (100%)** — `max(line) = 1122` |

L'invariante «di file» qui è legittimo (decisione 181) ed è asserito **insieme**: `0 dopo`, `max(line)`,
copertura 374/374. Se il file crescesse di una unità, i tre controlli diventerebbero rossi.

## Cosa è stato deciso qui

1. **Il primo `LOGBOOK` del file** (unità 1): forma `log` **fra backtick**, testo completo estratto (non è
   uno dei sei casi lacunosi noti). Il `check.py` ha dovuto **cambiare segno**: da «assenza dichiarata» a
   «1 attesa, controllo positivo» (decisione 190). Il primo tentativo era rosso proprio su quella riga.
2. **«Teredini di Delve»** resta identico a L66: la parola ricorre qui in tre forme (l'oggetto del diario,
   la diagnosi del tecnico, la battuta legale sul marchio). La coerenza fra i due lotti è il punto.
3. **Il tecnico è un dipendente del Sindacato che parla da dipendente del Sindacato**: «Come modello di
   dipendente del Sindacato, posso dirti che le voci… sono false». L'ironia è nella formula, e la
   traduzione non la spiega.
4. **La guardia dei Lovelace Labs** è il secondo personaggio femminile del file con un registro proprio
   (noia professionale, poi divertimento): «Di. Cosa. Sono. Fatte?» con i punti come pause.
5. **`decon` / `decontamination`** → «decon» / «decontaminazione»: nel parlato la forma breve resta breve.

## Verifica

```bash
cd staging/editorial/L67_20261018_191025
python check.py                 # FAIL totale: 0   (33 controlli)
python verify.py                # exit 0           (38 controlli)
```

## Prossimo passo

Il file è chiuso. **L68** apre un **file nuovo**: `data/successors/successor 2 ghosts myurej.txt`,
righe **16–113**, **49 unità**, 1 contesto (`Successors: Ghosts Myurej 1`), 1.502 parole, tab 42,
virgolette 90, **1 `UI_LABEL`** (unità 20), **2 `LOGBOOK`** (unità 23, 24), **10 token** in 5 famiglie
(`<first>` 3, `<last>` 3, `<ship>` 2, `<destination>` 1, `<planet>` 1 — corretto il 2026-10-18 in L68:
questo documento diceva 13, ma la somma della sua stessa tabella e il `source.json` danno 10).
