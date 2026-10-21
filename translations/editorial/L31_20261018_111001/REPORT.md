# L31 — REPORT (chiuso 2026-10-18)

`data/coalition/heliarch intro.txt`, righe 16–2140 — **663/663 unità**, file completo.

## Numeri misurati

| voce | valore |
|---|---|
| unità | 663 / 663 |
| contesti | 41 |
| parole | 21.729 EN → 20.845 IT (0,959) |
| parti | 11 (42, 59, 57, 80, 48, 77, 73, 83, 56, 58, 30) |
| tab | 509 IT = 509 EN |
| virgolette | 878 IT = 878 EN |
| token `<...>` | 181 IT = 181 EN |
| rapporto per unità | 0,73 – 1,68 (gate 0,55–1,90) |
| `NT` | 10 `UI_LABEL` |
| `check.py` | `FAIL totale: 0` |
| `verify.py` | 25 controlli, exit 0, `FAIL: 0` |
| sha256[:16] `translation.json` | `09e75a0528604150` |
| sha256[:16] `source.json` | `5246846be56b224b` |
| sha256[:16] `check.py` | `c85286f9a8058835` |
| sha256[:16] `verify.py` | `9e249ffed933fbf4` |
| dimensione directory | 1,4 MB (11 parti) |

## Tipi presenti (misurati sul `source.json`)

```
MISSION_TEXT 571 · VALUE 31 · DESCRIPTION 31 · DIALOG 16 · UI_LABEL 10 · LOGBOOK 4 · CONVERSATION 0
```

## Narrazione coperta

L'arco che porta dall'indagine degli Heliarchs su mondi e navi dei Quarg alla **cerimonia di
incoronazione** con cui un esterno entra per la prima volta nei ranghi dell'Eliarchia:

- indagine su Kirrie, il cacciatore di taglie, e sul Saryd che protegge i rifugiati (1–158);
- spedizioni sul pianeta ghiacciato, i depositi minerari e il relitto (159–286);
- la scansione del Wardragon a Zubeneschamali e il console Aulori (287–363);
- l'indagine sul **mondo ad anello rotto** di Deneb: spedizione, base su Ruin, il frammento da un
  miliardo di kilotoni di materiale fissile, e il dibattito dei consoli (364–436);
- trasporto di agenti, droni spia, trasporti sotto copertura, navi in fuga armate con tecnologia
  umana (437–575);
- le esercitazioni della magistra Lotuora: rifornimento, inseguimento, duello (576–633);
- l'incorporazione: cerchietto, cerimonia, calibrazione, accesso alle sezioni riservate (634–663).

## Comandi di verifica (eseguiti, non trascritti)

```bash
python staging/editorial/L31_20261018_111001/check.py    # FAIL totale: 0
python staging/editorial/L31_20261018_111001/verify.py    # exit 0, FAIL: 0, 25 controlli
python staging/editorial/tools/state.py                   # ESITO: OK
```

## Che cosa non è stato fatto

- **Nessun caricamento nel gioco**: le 663 unità non sono mai state lette da Endless Sky.
- **Nessuna approvazione**: restano `PENDING` nel database.
- **Nessun controllo di resa a schermo** delle righe lunghe (le più lunghe superano le 1.400 battute).

## File del lotto

```
staging/editorial/L31_20261018_111001/
  source.json       663 unità esportate dal database (righe 16–2140)
  translation.json  traduzione completa, 663 unità
  check.py          controlli derivati da L30, NT misurato
  verify.py         controlli indipendenti, copertura totale
  parts/part01..11.json   le 11 parti scritte a mano
  review.md · REPORT.md · STATO.md
```
