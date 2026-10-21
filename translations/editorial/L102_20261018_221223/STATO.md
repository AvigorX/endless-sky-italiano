# STATO — L102 · `data/quarg/quarg missions.txt` (file nuovo, **primo `LOGBOOK`**)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L102_20261018_221223` |
| Righe / unità | **1–117** / **48** |
| Tipi | **46 `MISSION_TEXT`** + **2 `LOGBOOK`** (unità 1 e 2: schede di Quarg e Drak) |
| Contesti | **2** in ordine di riga: `First Contact: Quarg` (19–69), `First Contact: Kuwaru Efreti` (81–117) |
| Parole | **1675 EN → 1632 IT** (0,974); per unità 0,70–1,24 |
| Tab · virgolette | **44** · **98** |
| Token · quadre | **2** nella stessa unità (42): `<first>` e `<last>` · **0** |
| Ripetizioni | **3 gruppi**: 17/20 (`"Who are the Drak?"`), 35/40, 37/38 — resi identici |
| sha256 | `d1e12262951885ee…` |
| `check.py` | **29 controlli**, `FAIL totale: 0` |
| `verify.py` | **27 controlli**, exit **0** |

## Invariante di segmento (primo lotto del file)

| Voce | Valore |
|---|---|
| Unità prima della riga 19 | **0** — nessun lotto precedente su questo file |
| Unità dopo la riga 117 | **130** |
| Confine | riga **124** apre `mission:Quarg Satellites` |
| File | **178 unità**, `max(line) = 506` |
| Copertura | **48/178 (27,0%)** |

## Il primo `LOGBOOK` della campagna

Le unità 1 e 2 **non sono etichette**: sono le schede che il gioco scrive nel diario di bordo quando si incontra
una specie. Il `check.py` di L101 dichiarava `LOGBOOK assente`; qui il controllo è **rovesciato** — tipo
presente, elencato per indice, tradotto per intero e **non identico** al sorgente (oltre 200 caratteri ciascuno).

## Contenuto

- **`First Contact: Quarg`**: lo spazioporto Quarg, l'architettura aliena (soffitti alti, pareti che non si
  incontrano ad angolo retto), il Quarg che si accovaccia per mettersi all'altezza dei vostri occhi e parla con
  una voce «come una fisarmonica o il ronzio di un alveare». Poi la storia della specie: nati sulla luna di un
  gigante gassoso, polmoni «assai delicati», il dono dei **Drak**, i sentieri fra le stelle «potati», le armi del
  caos («consumare pianeti, spegnere stelle, strappare la carne dello spazio e del tempo»).
- **`First Contact: Kuwaru Efreti`**: l'incontro con il Quarg che parla in **inglese arcaico** («Whither came
  you», «bring you can we no succor», «lest awaken in you we»), il cimitero dei Korathi, le macchine da guerra
  pensanti, i **Korath Efreti** («Amici dei Korath») sotto protezione Quarg, e il saluto del Korath con entrambe
  le mani aperte.

## Verifica

```bash
cd staging/editorial/L102_20261018_221223
python check.py   # FAIL totale: 0 (29 controlli)
python verify.py  # exit 0 (27 controlli)
```
