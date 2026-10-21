# STATO — L95 · `data/coalition/coalition culture conversations.txt` (terzo lotto)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L95_20261018_213812` |
| Righe / unità | **148–190** (finestra 134–190) / **27** |
| Tipi | **24 `MISSION_TEXT`** + **3 `UI_LABEL`** (`defend r`, `defend rw`, `defend w`: etichette di salto, **identiche**) |
| Contesti | **1** (`Coalition Folklore: Kimek`) |
| Parole | **1382 EN → 1242 IT** (0,899); per unità 0,75–1,41 |
| Tab · virgolette · token | **23** (tutte tranne 1, 18, 23, 25) · **38** (6 nell'unità 14; 4 in 1 e 10) · **0** (asserzione) |
| Ripetizione | **20/27** `(Aiuta a tenere chiuso il cancello principale.)` — resa identica |
| sha256 | `58cfe11da4d60c5c…` |
| `check.py` | **28 controlli**, `FAIL totale: 0` |
| `verify.py` | **29 controlli**, exit **0** |

## Dove siamo

| Voce | Valore |
|---|---|
| Unità prima della riga 148 | **67** (L93 + L94) |
| Unità dopo la riga 190 | **63** (riga 192, **stesso** contesto `Kimek`) |
| File | **157 unità**, `max(line) = 462` |
| Copertura | **94/157 (59,9%)** · 5447 EN → 4973 IT · 3 lotti |

## Contenuto

La **rievocazione dell'«Assedio di Primavera»** nella savana dei Kimek: l'invito del Kimek allo spazioporto,
il treno per il parco, i campi di accampamenti e forti sulla collina; la scelta della fazione; il racconto del
menestrello che vide la battaglia e perse i dettagli nel vento (per questo la storia ammette **entrambi** gli
esiti). Poi il forte: la «fattoria» con i raccolti di plastica, le spine sulle palizzate, il gilet di cuoio
come armatura, i secchi di liquido scivoloso. La battaglia si biforca: **difendere il cancello principale** o
**andare al cancello posteriore**, con i tre esiti (vittoria dei difensori, sconfitta per il cancello piccolo
aperto, e il ramo delle secchiaiate laterali). Il lotto si chiude sulla scelta ripetuta del cancello
principale.

**Le tre `UI_LABEL`** (`defend r`, `defend rw`, `defend w`) sono **bersagli di `goto`**: restano identiche e
sono elencate una per una nel `check.py`, che le asserisce uguali al sorgente.

## Verifica

```bash
cd staging/editorial/L95_20261018_213812
python check.py   # FAIL totale: 0 (28 controlli)
python verify.py  # exit 0 (29 controlli)
```
