# STATO — L99 · `data/hai/hai culture conversations.txt`

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L99_20261018_215807` |
| Righe / unità | **106–211** / **38** |
| Tipi | **38 `MISSION_TEXT`** — **0 `UI_LABEL`** (premessa asserita) |
| Contesti | **4** in ordine di riga: `Wrestling Star` (119–128), `Fencing Star` (142–151), `Mystery Sport Star` (165–174), `Gambling Judgment` (188–211) |
| Parole | **1183 EN → 1151 IT** (0,973); per unità 0,94–1,33 |
| Tab · virgolette | **34** · **23** — di cui **una sola** nell'unità 32 (citazione aperta e **non chiusa**: voluta) |
| Token · quadre | **0** · **0** — entrambi **asseriti** |
| Ripetizioni | **7 gruppi**: 1/8/15, 2/9/16, 3/10/17, 4/11/18, 6/13, 7/14/21, 24/27 — tutti resi identici |
| sha256 | `545c18fca521b07f…` |
| `check.py` | **30 controlli**, `FAIL totale: 0` |
| `verify.py` | **28 controlli**, exit **0** |

## Invariante di segmento

| Voce | Valore |
|---|---|
| Unità prima della riga 119 | **39** (solo L98) |
| Unità dopo la riga 211 | **70** |
| Confine | riga **227** apre `mission:Academy Motto` |
| File | **147 unità**, `max(line) = 386` |
| Copertura | **77/147 (52,4%)** |

## Contenuto

**Tre missioni gemelle** (`Wrestling Star`, `Fencing Star`, `Mystery Sport Star`): la folla di Hai che trilla,
l'evento di autografi con gli stendardi olografici, l'«effetto ottenuto solo con un trucco di prospettiva
spostata artificialmente». Cambia solo l'atleta: il wrestler muscoloso, la schermitrice snella, la coppia
misteriosa con la rete e il frisbee a lame — di cui nessuno vuole spiegare la disciplina.

**Gambling Judgment**: i capitani umani a poker nella tavola calda, gli sguardi torvi degli Hai, e il barista
che espone i **principi della maturità** — «Essere onesti negli affari», «Scommettere solo sull'abilità, non sul
caso», «Avere una chiara separazione fra fantasia e realtà» — fino a quella che sembra una battuta finale sui
principi oltre il decimo e il tredicesimo.

## Verifica

```bash
cd staging/editorial/L99_20261018_215807
python check.py   # FAIL totale: 0 (30 controlli)
python verify.py  # exit 0 (28 controlli)
```
