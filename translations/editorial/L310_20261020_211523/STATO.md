# STATO — L310 (`data/korath/korath culture conversations.txt`, righe 26–75)

**Stato: CHIUSO — LOTTO TERMINALE, FILE INTERO.** Il file è **completo: 27/27 (100%)**, **trentesimo file interamente tradotto**
(**89** su 167 nel progetto). È il **primo file chiuso in un solo lotto** da quando esiste il ciclo editoriale.

| voce | valore |
|---|---|
| directory | `staging/editorial/L310_20261020_211523/` |
| file | `data/korath/korath culture conversations.txt` (**27/27 unità · 1.295 parole · righe 26–75**) |
| righe | 26–75 (**tutto il file**) |
| unità | **27** — **24 `MISSION_TEXT` + 3 `UI_LABEL`** |
| contesti | **1** — `mission:Korath Far'en Lai Prayer` |
| parole | **1.295 EN → 1.187 IT** (0,92) |
| rapporto | **0,82 – 1,48** |
| tab | **23** — tutte le `MISSION_TEXT` tranne la 26 |
| virgolette | **14** in **6 unità** (33: 2, 35: 2, 37: 2, 39: 2, **40: 4**, 56: 2) |
| segnaposto | **3** — `<origin>` ×2, `<home planet>` ×1, **identici** |
| alternative | **0** (asserzione vuota) |
| apici | **10 EN / 12 IT** |
| `check.py` | **23 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **23 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di FILE**: 27 unità · righe distinte · prima **26** · ultima **75** · **0 prima, 0 dopo** |
| `sha256[:16]` | **`47768e1cd5729025`** |

## Comandi

```bash
python staging/editorial/L310_20261020_211523/check.py     # FAIL totale: 0 (23 controlli)
python staging/editorial/L310_20261020_211523/verify.py    # FAIL: 0 (23 controlli, FILE 27/27)
```

## Un file in un solo lotto

Finora ogni file era diviso in due-tre lotti. Qui **no**: la conversazione è **corta** (26–75) e **unita** (un solo contesto), e
spezzarla avrebbe rotto proprio ciò che il test deve verificare — il **filo** della scena.

L'invariante diventa:

```
0 prima · 27 qui · 0 dopo        FILE 27/27 (100%)
```

## La scena, in 24 battute

| righe | momento |
|---|---|
| 26 | lo spazioporto **cupo**, la folla radunata accanto a un edificio annerito |
| 27 | i **bambini** disegnano un **pianeta** sul muro con qualcosa di simile a pastelli |
| 28–30 | il **santuario** di casse, la tela, gli oggetti personali alla base, le **lastre incise** con mappe stellari |
| 31–32 | il **vecchio** che guaisce; sulla cima **piuma, conchiglia, fiore** attorno a **una candela**; e su `<origin>` **non c'è vento** |
| 33–37 | la **giovane Korath** si avvicina, «**humani efreti**»; tre possibilità di risposta del giocatore |
| 39–41 | lei **disegna le braccia a spirale**, indica il centro, poi sé, poi il giocatore; «**Far'en Lai**»; depone il suo **dispositivo** fra le offerte |
| 43–56 | **quattro scelte**: 100 / 10.000 / 10.000.000 crediti / **una fotografia** / andarsene |
| 58 | la **fotografia** di `<home planet>`: il vecchio la guarda a lungo, poi le **palme alzate** di tutti |
| 60–73 | le tre risposte alle offerte in crediti, con i **tre `UI_LABEL`** |
| 75 | il **congedo**: le mani alzate, e lo spazioporto che guarda il santuario |

## Che cosa il test pretende

| oggetto | verifica |
|---|---|
| `UI_LABEL` | **copiati** (`small/medium/large credits`) e **senza tab** |
| virgolette | **14**, con la **quantità per unità** (la 40 ne ha **quattro**) |
| segnaposto | **identici** all'inglese, con il **conteggio** |
| tab | **23**: tutte le `MISSION_TEXT` tranne la 26 |
| seconda persona | **presente** (è la voce narrante: «ti serve», «noti», «Ti ricordi») |
| offerte | parentesi **e** valori **italiani** (`10.000`, `10.000.000`) |
| nomi | `Korath`, `Far'en Lai`, `"humani efreti"` **invariati** |

## Limiti dichiarati

Nessuna approvazione (27 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Il file è **finito in
staging**, non approvato.
