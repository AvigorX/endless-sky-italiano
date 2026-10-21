# L32 — REPORT (chiuso 2026-10-18)

`data/wanderer/wanderers start.txt`, righe 23–3092 — **805/805 unità**, file completo.

## Numeri misurati

| voce | valore |
|---|---|
| unità | 805 / 805 |
| contesti | 69 |
| parole | 24.166 EN → 22.753 IT (0,942) |
| parti | 13 (45, 55, 65, 66, 59, 80, 52, 61, 72, 57, 63, 61, 69) |
| tab | 512 IT = 512 EN |
| virgolette | 1.305 IT = 1.305 EN |
| token `<...>` | 173 IT = 173 EN |
| parentesi quadre | 112 unità, struttura identica al sorgente |
| rapporto per unità | 0,72 – 1,61 (gate 0,55–1,90) |
| `NT` | 3 (1 riferimento di dato, 2 `label` di salto) |
| `check.py` | `FAIL totale: 0` |
| `verify.py` | 26 controlli, exit 0, `FAIL: 0` |
| sha256[:16] `translation.json` | `bdabdc64ad3b7ce1` |
| sha256[:16] `source.json` | `48a76a8a4e01d07a` |
| sha256[:16] `check.py` | `5682d64b91dabd42` |
| sha256[:16] `verify.py` | `0566840e048275be` |
| dimensione directory | 1,5 MB (13 parti) |

## Tipi presenti (misurati sul `source.json`)

```
MISSION_TEXT 561 · DESCRIPTION 58 · VALUE 53 · CONVERSATION 47 · DIALOG 45 · LOGBOOK 40 · TEXT 1 · UI_LABEL 0
```

## Narrazione coperta

Il primo contatto con i Wanderers e la scoperta del loro mondo:

- primo contatto (1–100): la specie avicola, l'interprete Hai, l'ambasciatrice Sayari, la macchina
  parlante di Eruk e il furto del database culturale umano;
- fondamenti (101–165): Iktat Rek, **l'Occhio** e **la Muta**, il sospetto sui Pug, il primo trasporto
  di rifornimenti per Vara Ke'sok;
- diplomazia (166–231): difesa dall'incursione, il **tributo** agli Slegati, il cessate il fuoco;
- intelligence (232–370): la vendita del motore di salto, i cubi di sorveglianza, gli **Alphas**,
  il Carrier della Marina, il dispositivo di tracciamento dei Quarg;
- Alphas e Marina (371–483): Avalon, l'ammiraglio Danforth, l'assalto alla base, l'arresto da parte
  dell'intelligence, Elias Hanover e i suoi sei secoli;
- invasione (484–612): l'evacuazione dei mondi, Sobari Tele'ek, il consiglio di guerra, i Pug che
  rifiutano di aiutare, la mediazione con gli Hai, il rifiuto degli Slegati;
- la malattia di Rek (613–736): il Solifuge, il consiglio degli anziani, Osen, la **Muta** che avanza;
- Sko'karak (737–805): i tre viaggi nel sistema, il fenomeno cosmologico, la quarantena e l'arrivo
  dei **Custodi**.

## Comandi di verifica (eseguiti, non trascritti)

```bash
python staging/editorial/L32_20261018_112734/check.py    # FAIL totale: 0
python staging/editorial/L32_20261018_112734/verify.py    # exit 0, FAIL: 0, 26 controlli
python staging/editorial/tools/state.py                   # ESITO: OK
```

## Che cosa non è stato fatto

- **Nessun caricamento nel gioco**: le 805 unità non sono mai state lette da Endless Sky.
- **Nessuna approvazione**: restano `PENDING` nel database.
- **Nessun controllo a schermo** delle 47 `CONVERSATION` e delle righe con parentesi quadre: nel gioco
  il dispositivo di traduzione mostra una sola alternativa per volta, e non è verificato che le rese
  scelte stiano nella larghezza della finestra di dialogo.

## File del lotto

```
staging/editorial/L32_20261018_112734/
  source.json       805 unità esportate dal database (righe 23–3092)
  translation.json  traduzione completa, 805 unità
  check.py          controlli derivati da L31 + parentesi quadre
  verify.py         controlli indipendenti, copertura totale
  parts/part01..13.json   le 13 parti scritte a mano
  review.md · REPORT.md · STATO.md
```
