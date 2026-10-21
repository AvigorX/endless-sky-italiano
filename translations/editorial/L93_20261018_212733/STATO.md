# STATO — L93 · `data/coalition/coalition culture conversations.txt` (primo lotto del file)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L93_20261018_212733` |
| Righe / unità | **24–66** (finestra 1–66) / **31** |
| Tipi | **31 `MISSION_TEXT`** — **0 `UI_LABEL`** in questa finestra (il file ne ha 8 più avanti) |
| Contesti | **1** (`Coalition Folklore: Saryd`) |
| Parole | **1744 EN → 1616 IT** (0,927); per unità 0,93–1,55 |
| Tab · virgolette · token | **30** (tutte tranne la 1) · **22** (4 nell'unità 5) · **0** (asserzione) |
| Ripetizione | **15/20/25**: la descrizione del palco nei tre sentieri, resa identica |
| sha256 | `f11dbf2fa0744173…` |
| `check.py` | **28 controlli**, `FAIL totale: 0` |
| `verify.py` | **27 controlli**, exit **0** |

## Dove siamo

| Voce | Valore |
|---|---|
| Unità prima della riga 24 | **0** (primo lotto del file) |
| Unità dopo la riga 66 | **126** (riga 81, contesto `Arach`) |
| File | **157 unità**, `max(line) = 462` |
| Copertura | **31/157 (19,7%)** · 1744 EN → 1616 IT · 1 lotto |

## Contenuto

L'invito di un **Saryd in vesti tradizionali** a una celebrazione del folklore; la radura con tre sentieri e
i tre scrigni (semi, conchiglie, piume); il palco di legno nel bosco con le figure di carta in stile origami;
e — a seconda dell'oggetto scelto — la **caccia al leone da siepe** (piuma), la **fuga dal temporale sotto la
grande quercia** (seme) o il **pescatore salvato dalla balena volante** (conchiglia). Il congedo del Saryd.

**Voce della specie**: il parlato dei Saryd ha **sintassi invertita** nel sorgente («choose your path, you
must», «That you enjoyed the spectacle, I hope»). È caratterizzazione, non refuso: è riprodotta con un ordine
marcato italiano («scegliere il vostro sentiero, dovete»), non normalizzata.

## Verifica

```bash
cd staging/editorial/L93_20261018_212733
python check.py   # FAIL totale: 0 (28 controlli)
python verify.py  # exit 0 (27 controlli)
```
