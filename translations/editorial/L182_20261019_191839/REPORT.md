# REPORT — L182 · `human outfits.txt` (terzo lotto)

## 1. Contenuto

Quattordici schede, quasi tutte indipendenti: il `Jump Drives (Broken)` (nome + descrizione), quattro scanner (cargo,
equipaggiamenti, asteroidi, tattico) più il `Surveillance Pod`, il `Cloaking Device` (una battuta), tre espansioni
(`Outfits`, `Cargo`) e le due stanze per l'equipaggio (`Bunk Room`, `Small Bunk Room`) fino alla `Brig`.

## 2. Scelte

| nodo | IT | unità |
|---|---|---|
| `cargo holds` | **stive cargo** | 3 |
| `Patrol craft` | **pattugliatori** | 3 |
| `contraband` | **merce di contrabbando** | 3 |
| `scan range and speed` | **portata e velocità di scansione** | 3, 4, 7 |
| `crew complement` | **numero di membri dell'equipaggio** | 6 |
| `the Navy` | **la Marina** | 6, 7 |
| `militia ships` | **navi della milizia** | 6 |
| `surveillance drones` | **droni di sorveglianza** | 7 |
| `outfits` (in prosa) | **equipaggiamenti** | 4, 9, 12 |
| `make space for more people` | **fare spazio a più persone** | 12, 13 |
| `bunk bed behind the power generator` | **un letto a castello dietro il generatore di corrente** | 13 |
| `hammocks from the engines` | **amache ai motori** | 13 |
| `the Republic's interstellar law enforcement` | **le forze dell'ordine interstellari della Repubblica** | 14 |

## 3. Difficoltà

1. **Sei apici inglesi**: il contratto li segnalava come il punto delicato. Legati uno per uno: 4 possessivi (`ship's` ×2,
   `Republic's`, e il `ship's` di idx 7) e 2 elisioni (`You're`, `can't`). In italiano **nessuno** sopravvive come apice —
   l'italiano usa «di + articolo», e gli apici italiani (9) nascono da elisione di articolo e dal troncamento `po'`.
2. **Un errore in corsa (mio)**: l'asserzione diceva «4 apici italiani». Erano **9** — avevo contato solo quelli che mi
   ricordavo (`po'`, `l'`, `un'`, `l'`), dimenticando tre `dell'`. Il numero è stato **misurato** e non indovinato; il
   controllo ora verifica anche che i due conteggi **non** coincidano.
3. **`Cloaking Device`** (idx 8) è l'unico nome di equipaggiamento reso in italiano — «dispositivo di occultamento» — perché
   la frase è una **battuta** («sei sicuro che sia qui, ma non riesci a vederlo») e il nome resta nel contesto.
4. **`Kraz Cybernetics`** e la `Marina della Repubblica` restano nomi propri.
5. **La frase ripetuta dei tre scanner** («Installarne più di uno aumenta portata e velocità di scansione») verificata
   identica in idx 3, 4 e 7.
6. **Gate**: 0,99–1,33, media 1,10.

## 4. Numeri osservati

```
unita' 14 · 13 DESCRIPTION · 1 VALUE (`Jump Drives (Broken)`) · tutte PENDING
token 0 · 1 tab (10) · 0 virgolette · 6 apici EN con causa · 9 apici IT (nessuna corrispondenza)
14 testi distinti · 12 contesti (2 + 2 + dieci con 1) · righe 236/387
parole 497 -> 498 (1.002) · rapporto 0.99 - 1.33, media 1.10
FAIL totale: 0 (29 controlli) · verify exit 0 (20 controlli) · sha256[:16] 227c7d7ef6b392c9
```

## 5. Stato del progetto (dopo L182)

```
TOTALE staging: 28264 unità · 889418 EN · 846357 IT
human outfits.txt: 35/63 (55,6%) · 3 lotti
residuo traducibile (formula state.py): 3666
residuo misurato: 4335 unità / 87686 parole su 111 file
endless-sky HEAD b4aa3bac3, 0 modifiche
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (29 controlli), `verify.py` exit **0** (20 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 14 unità `PENDING`.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Terzo lotto del file**: contratto successivo in `HANDOFF_L183_20261019.md`.
