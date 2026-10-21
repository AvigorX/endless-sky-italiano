# STATO — L104 · `data/quarg/quarg missions.txt` (cinque citazioni aperte)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L104_20261018_222145` |
| Righe / unità | **250–334** / **27** |
| Tipi | **27 `MISSION_TEXT`** — 0 `UI_LABEL`, 0 `VALUE` |
| Contesti | **2** in ordine di riga: `Ask Quarg About Coalition Early` (265–284), `Quarg Pug Arfecta Warning` (302–334) |
| Parole | **631 EN → 597 IT** (0,946); per unità 0,86–1,22 |
| Tab · virgolette | **24** · **37**, con **cinque citazioni aperte** (unità 5, 19, 22, 23, 24) |
| Token · quadre | **0** · **0** — entrambi asseriti |
| Ripetizioni | **nessuna** (asserita vuota) |
| Unità identica al sorgente | **una sola, l'unità 3**: `(No.)` = `(No.)`, coincidenza linguistica dichiarata |
| sha256 | `1186c7b9ae462081…` |
| `check.py` | **27 controlli**, `FAIL totale: 0` |
| `verify.py` | **27 controlli**, exit **0** |

## Invariante di segmento

| Voce | Valore |
|---|---|
| Unità prima della riga 265 | **90** (L102 + L103) |
| Unità dopo la riga 334 | **61** |
| Confine | riga **356** apre `mission:Ask Quarg About Coalition Late` |
| File | **178 unità**, `max(line) = 506` |
| Copertura | **117/178 (65,7%)** |

## Contenuto

- **`Ask Quarg About Coalition Early`**: la versione dei Quarg sulla Coalizione — «Ah, dunque hai incontrato la
  stolta Coalizione; un tempo erano tre specie promettenti, prima di cedere al desiderio insensato di usurpare le
  grandi imprese altrui» — le due domande del giocatore sulla sconfitta e sull'oppressione, e la risposta
  «Non sottovalutarci, umano. Siamo numerosi, e siamo forti… Sappiamo solo che è meglio non massacrare miliardi
  di esseri per mantenere la nostra posizione».
- **`Quarg Pug Arfecta Warning`**: il Quarg che attende la nave con le scorte Pug — «È come se un bambino in fasce
  avesse addomesticato un drago» — le quattro risposte possibili del giocatore, e l'avvertimento: «Non sapete cosa
  avete, umano - quale arma impugnate… Fate attenzione a essere voi a dirigere questo potere, e non lui a
  dirigere voi».

## Verifica

```bash
cd staging/editorial/L104_20261018_222145
python check.py   # FAIL totale: 0 (27 controlli)
python verify.py  # exit 0 (27 controlli)
```
