# STATO — L126 · `data/incipias/incipias first contact.txt` (primo lotto: 55 unità)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L126_20261019_073300` |
| Righe / unità | **22–218** / **55** — il lotto **apre** il file (0 unità prima) |
| Tipi | **48 `MISSION_TEXT`** · **4 `UI_LABEL`** · **3 `LOGBOOK`** |
| Stati | **55 `PENDING`** — misurato e **asserito** in `mkparts.py` |
| Contesti | **6** — 23 / 13 / 13 / 2 / 2 / 2 |
| Testi distinti | **52** per 55 unità — **3 coppie** ripetute |
| Parole | **1788 EN → 1626 IT** (0,909); per unità 0,69–1,44, media 1,01 |
| Tab | **37 unità** su 55 con `\t` iniziale |
| Virgolette | **65**, comprese le **3 dell'unità 23** (una in più nel sorgente) |
| Token · quadre | **0** · **0** — asserzioni scritte |
| sha256 | `c928bf1d8815cac5…` |
| `check.py` | **31 controlli**, `FAIL totale: 0` |
| `verify.py` | **28 controlli**, exit **0** — invariante di **segmento** |

## Le 4 `UI_LABEL`, isolate

`ut divitas` · `spec inci` · `both planets` · `new species` (unità 30, 32, 34, 39) sono **testi di nodo** e restano
**identici al sorgente**. Sono esclusi dal controllo «tutte tradotte» e verificati in un controllo loro, con la
lista esatta. Senza questa distinzione due controlli su tre sarebbero rossi su un lotto corretto.

## Due registri, dichiarati

| personaggio | forma | esempio |
|---|---|---|
| **Il Guardiano** | alto, arcaico, profetico | «Ignorare queste parole è pura follia. Torna indietro, viaggiatore.» · «Qui giacciono i fiori non ancora nati…» |
| **I Quarg** | cerimoniale, leggermente stucchevole | «I tuoi lunghi vagabondaggi ti hanno condotto fin qui…» · «non peregrinare per questo quarto di spazio con leggerezza» |

Il `check.py` verifica che le forme caratteristiche di **entrambi** i registri siano presenti: se un lotto futuro
appiattisse il Guardiano o i Quarg sul parlato comune, il controllo diventerebbe rosso.

## La virgoletta in più

L'unità 23 ha **tre** virgolette: il sorgente chiude la battuta e poi lascia un'ulteriore virgoletta dopo il punto
(`…being watched."`). La resa la **riproduce**; il controllo verifica che l'unità 23 abbia 3 virgolette in inglese e
3 in italiano.

## Contenuto

- **Avvertimento del Guardiano** (1–23): la voce incorporea, i fiori non nati, il pittore e il quadro, il permesso
  con sorveglianza.
- **Presenza del Guardiano** (24–27): Dom'us e Hui'uc, due sistemi con lo stesso rimprovero.
- **Primo contatto** (28–29): navi sconosciute, solo fruscio.
- **Visita ai Quarg** (30–42): i Quarg cerimoniali, le due domande, l'avvertimento sui confini.
- **Il relitto** (43–55): la nave aliena, i cinque polpi-medusa, le tre scelte e il finale.

## Verifica

```bash
cd staging/editorial/L126_20261019_073300
python mkparts.py   # 55 unità · 52 testi distinti · 4 UI_LABEL identiche · 37 tab · 65 virgolette
python check.py     # FAIL totale: 0 (31 controlli)
python verify.py    # exit 0 (28 controlli)
```
