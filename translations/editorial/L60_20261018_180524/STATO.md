# STATO — L60 · `data/human/culture conversations.txt`

**Lotto chiuso.** 31/31 unità tradotte, righe **437–495** (finestra di export 429–495: la prima unità sta
sulla 437).

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L60_20261018_180524` |
| File | `data/human/culture conversations.txt` (terzo lotto sul file) |
| Unità | **31** (righe 437–495) |
| Parti | **2** — 29 · 2 |
| Contesti | **2** — `Tarazed Ship Christening` 1–29, `Masquerade Hanging` 30–31 |
| Tipi | **29 `MISSION_TEXT` + 2 `UI_LABEL`** |
| Parole | 661 EN → 626 IT (**0,947**) |
| Rapporto per unità | **0,88 – 1,54** (gate 0,55–1,90) |
| `UI_LABEL` (`NT`) | **2** — unità **6** `pass by`, unità **20** `get out` (identiche al sorgente) |
| `DIALOG` / `LOGBOOK` / `CONVERSATION` / `TEXT` | **0 / 0 / 0 / 0** — assenze dichiarate |
| Tab · virgolette | **27** · **40** (0 dispari, 0 quadre, 0 backtick) |
| Token `<…>` | **0** (parità 0/0 asserita) |
| Duplicati inglesi | **0 gruppi** — controllo negativo dichiarato |
| sha256 `translation.json` | `412787a6b5f31400…` |
| `check.py` | **33 controlli**, `FAIL totale: 0` |
| `verify.py` | **36 controlli**, exit **0** |

## Dove siamo nel file

| Voce | Valore |
|---|---|
| Unità prima della 437 | **85** (L58+L59) |
| Unità dopo la 495 | **258** |
| Unità totali del file | **374** |
| Copertura | **116/374 (31,0%)** |
| `max(line)` | **1122** |

## Cosa è stato deciso qui

1. **`NT` torna positivo** dopo due lotti a zero: due `UI_LABEL`, entrambe di **salto** (`pass by`,
   `get out`), elencate per indice (6, 20) e verificate identiche al sorgente.
2. **Due registri in un lotto.** Il varo di una nave (1–29) è una scena pubblica, affettuosa, con
   battute: registro brillante. `Masquerade Hanging` (30–31) è una scena di giustizia sommaria: registro
   cupo, impersonale, con il corpo che rotola dalla piattaforma. Non si uniformano.
3. **La parola «Guardare» è stata cambiata in «Dare un'occhiata».** Non per stile: il controllo
   `parole inglesi residue` rimuove i titoli (`Guard`, `Captain`, …) prima di cercare parole inglesi, e
   «Guardare» − «Guard» lasciava **«are»**, che è nella lista. Il controllo ha funzionato come doveva; la
   traduzione è stata riscritta, non il controllo.
4. **`Champagne` → «champagne»**: il prodotto resta, non è un nome proprio di nave.
5. **`Shuttle`** resta invariato e maiuscolo: è una classe di nave del gioco.
6. **«my psychiatrist doesn't think it's very funny»** → «anche il mio psichiatra non la trova divertente
   quando lo faccio a lui»: la battuta è cattiva nel sorgente e resta cattiva.

## Verifica

```bash
cd staging/editorial/L60_20261018_180524
python check.py                 # FAIL totale: 0   (33 controlli)
python verify.py                # exit 0           (36 controlli)
```

## Prossimo passo

**L61** — stesso file, righe **511–552**, **26 unità**, 1 contesto (`News Reporter - Paradise`),
394 parole, tab 25, virgolette 38, 1 token `<origin>`, 0 `UI_LABEL`.
