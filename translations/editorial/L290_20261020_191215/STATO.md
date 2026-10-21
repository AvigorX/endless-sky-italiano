# STATO — L290 (`data/avgi/avgi culture conversations.txt`, righe 24–106)

**Stato: CHIUSO.** Primo lotto del file: **otto scene di vita Avgi** in **seconda persona**. Il file è aperto a **8/46 (17,4%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L290_20261020_191215/` |
| file | `data/avgi/avgi culture conversations.txt` (46 unità · 1.657 parole · righe 24–270 · 44 `MISSION_TEXT` + 2 `LOGBOOK`) |
| righe | 24–106 |
| unità | **8**, tutte `MISSION_TEXT` |
| parole | **468 EN → 450 IT** (0,96) |
| rapporto (caratteri) | **1,06 – 1,17** |
| contesti | **6** — `Verticality` · `Free Fuel` · `Playfight` · `Cocoon` · `Zapchannel Ad` ×2 · `Dissonance Protest 1` ×2 |
| tab | **0** (asserzione vuota) |
| virgolette | **10**, per unità |
| apici | **9 EN / 9 IT** |
| segnaposto | **1** — `<ship>` |
| alternative | **0** (asserzione vuota) |
| `check.py` | **24 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **24 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 0 prima (il lotto **apre** il file) · 8 qui · **38 dopo** la 106 |
| `sha256[:16]` | **`43628edbfe1ff1a2`** |

## Comandi

```bash
python staging/editorial/L290_20261020_191215/check.py     # FAIL totale: 0 (24 controlli)
python staging/editorial/L290_20261020_191215/verify.py    # FAIL: 0 (24 controlli)
```

## Il registro si inverte

L286–L289 erano **schede tecniche impersonali** e il test verificava l'**assenza** di «tu». Qui il testo **parla al giocatore**
(«scopri», «sei costretto», «riesci a capirla», «senti borbottare»): il controllo è **invertito** — la seconda persona deve
comparire in almeno **cinque** unità su otto. Lo stesso tipo di controllo, con il segno opposto, perché il **tipo di testo** è
cambiato.

## Le scene ripetute, e la coerenza fra le due versioni

Due scene compaiono **due volte**, in versioni quasi identiche (il gioco le usa in contesti diversi):

| coppia | righe | condiviso | differenza |
|---|---|---|---|
| insegna | 82 / 86 | **tutto l'inizio** («Un'insegna elettronica economica, appiccicata alla parete…») | la seconda **legge** il messaggio |
| protesta | 102 / 106 | **inizio e chiusura** identici | la seconda riporta **tre slogan** |

Il test verifica che le parti comuni siano **parola per parola identiche** nelle due rese: un testo che il giocatore vede due
volte non può cambiare forma. È la regola di coerenza cross-lot applicata **dentro lo stesso lotto**.

## I tre slogan

```
"STOP CONSONANCE TAXES"        → "BASTA CON LE TASSE DELLA CONSONANCE"
"ABOLISH MINERAL FEUDALISM"    → "ABOLIAMO IL FEUDALESIMO MINERALE"
"STOP SENDING US TO DIE"       → "SMETTETE DI MANDARCI A MORIRE"
```

Restano in **maiuscolo** e fra **virgolette**: sono cartelli, non prosa. `Consonance` resta **invariato** e **femminile**
(«DELLA CONSONANCE»), come nel corpus di `avgi news`.

## Le parole inventate

| parola | trattamento | nota |
|---|---|---|
| `Incredulation` | **invariata** | imprecazione Avgi coniata; non è italiano né inglese |
| `dee` | **invariata** | sostanza non altrimenti descritta |
| `Zapchannel Ray Energy` | **invariata** | nome commerciale, già nel corpus (`avgi side missions`) |
| `Consonance` | **invariata**, femminile | il governo Avgi, già nel corpus (`avgi news`) |

## Limiti dichiarati

Nessuna approvazione (8 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Restano **38 unità**.
