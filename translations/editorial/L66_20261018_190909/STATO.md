# STATO — L66 · `data/human/culture conversations.txt`

**Lotto chiuso.** 45/45 unità tradotte, righe **930–1053** (finestra di export 921–1053: la prima unità
sta sulla 930).

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L66_20261018_190909` |
| File | `data/human/culture conversations.txt` (nono lotto sul file) |
| Unità | **45** (righe 930–1053) |
| Parti | **2** — 17 · 28 |
| Contesti | **4** — `Exotic Life: New Greenland` 1–8, `Exotic Life: Mainsail` 9–17, `Struggling Author Gone Missing` 18–25, `Exotic Life: Bloodsea` 26–45 |
| Tipi | **45 `MISSION_TEXT`** e nient'altro |
| Parole | 1.239 EN → 1.176 IT (**0,949**) |
| Rapporto per unità | **0,64 – 1,20** (gate 0,55–1,90) |
| `UI_LABEL` / `DIALOG` / `LOGBOOK` / `CONVERSATION` / `TEXT` | **0 / 0 / 0 / 0 / 0** — assenze dichiarate |
| Token `<…>` | **0** — assenza dichiarata |
| Tab · virgolette | **41** (40 righe con tab iniziale) · **52**, con **2 dispari** (unità **10, 34**) riprodotte |
| Duplicati inglesi | **1 gruppo** (2 unità) |
| sha256 `translation.json` | `41a48d5412d5b7c6…` |
| `check.py` | **33 controlli**, `FAIL totale: 0` |
| `verify.py` | **36 controlli**, exit **0** |

## Dove siamo nel file

| Voce | Valore |
|---|---|
| Unità prima della 930 | **294** (L58–L65) |
| Unità dopo la 1053 | **35** |
| Copertura | **339/374 (90,6%)** |

## Cosa è stato deciso qui

1. **Due virgolette dispari non consecutive** (10 e 34): sono due battute aperte e **non chiuse** nel
   sorgente. Riprodotte; `verify.py` confronta l'insieme `(10, 34)`.
2. **Quattro scenette di «vita esotica»**: il Mastino Mammut su New Greenland, il Cane di Mare di
   Mainsail, l'autrice scomparsa, i teredini di Bloodsea. Ognuna ha un registro proprio, e non si
   uniformano: la prima è solenne, la seconda è da venditore, la terza è cronaca di sparizione, la quarta
   è commedia nera da mercato nero.
3. **`Mammoth Mastiff`** → «Mastino Mammut», **`Mainsail Seadog`** → «Cane di Mare di Mainsail»: sono nomi
   di razza inventati, tradotti perché descrittivi, con il toponimo lasciato in inglese.
4. **`the Bloom`** → «la Fioritura»: nome di una malattia, reso come nome comune con la maiuscola, coerente
   in tutte le occorrenze.
5. **Il vecchio di Bloodsea** parla per motti bislacchi («Mare di sangue e sciocchi di sangue», «ti farò a
   pezzi e ti getterò alla Fioritura»): la traduzione mantiene l'andamento da imbonitore sinistro.
6. **Un rapporto fuori banda corretto**: l'unità 41 «(Make a run for it.)» rendeva 0,48 con «(Scappa.)»;
   riscritta «(Scappo via.)» il lotto rientra nel gate (0,64 minimo). Non si è allargato il gate.

## Verifica

```bash
cd staging/editorial/L66_20261018_190909
python check.py                 # FAIL totale: 0   (33 controlli)
python verify.py                # exit 0           (36 controlli)
```

## Prossimo passo

**L67** — stesso file, righe **1062–1122**, **35 unità**, 2 contesti (`Exotic Life: Delve`,
`Exotic Life: Ada`), 811 parole, tab 32, virgolette 68, **1 `LOGBOOK`**, 2 token `<ship>`.
**Chiude il file** a 374/374.
