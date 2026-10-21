# STATO — L313 (`data/bunrodea/bunrodea outfits.txt`, righe 250–402)

**Stato: CHIUSO — LOTTO TERMINALE.** Il file è **completo: 33/33 (100%)**, **trentunesimo file interamente tradotto** (**90** su 167
nel progetto). `check.py` esce 0 con **25 controlli**; `verify.py` esce 0 con **22 controlli**. `state.py` esce 0 (`ESITO: OK`,
8/8). Nessuna scrittura su `state.db`.

| voce | valore |
|---|---|
| directory | `staging/editorial/L313_20261020_214051/` |
| file | `data/bunrodea/bunrodea outfits.txt` (**33/33 unità · 1.252 parole · righe 25–402**) |
| righe | 250–402 |
| unità | **9** — tutte `DESCRIPTION` |
| contesti | **9** — **uno per unità** (struttura piatta) |
| parole | **327 EN → 339 IT** (1,037) |
| rapporto | **1,02 – 1,31** |
| tab / virgolette | **0 / 0** |
| segnaposto / alternative | **0 / 0** |
| apici | **2 EN / 6 IT** |
| `check.py` | **25 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **22 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di FILE**: 33 unità · somma lotti **12+12+9** · 33 righe distinte · prima **25** · ultima **402** · **0 dopo** |
| `sha256[:16]` | **`e70ea6641bcda78c`** |

## Comandi

```bash
python staging/editorial/L313_20261020_214051/check.py     # FAIL totale: 0 (25 controlli)
python staging/editorial/L313_20261020_214051/verify.py    # FAIL: 0 (22 controlli, FILE 33/33)
```

## Com'è fatto il lotto

Nove unità, **nove contesti**, **un contesto per unità** — struttura piatta, l'opposto delle coppie di L311 e delle terzine di
L312:

| righe | contesto | che cosa |
|---|---|---|
| 250 | `Lasher Pistol` | **armi leggere** contro gli **abbordaggi** dei predoni Korath |
| 271–327 | `Chiisana` → `Nami` → `Ookii` → `Subarashii Rift Thruster` | quattro **propulsori**: efficienza invece di potenza bruta |
| 346–402 | `Chiisana` → `Nami` → `Ookii` → `Subarashii Rift Steering` | quattro **timoni**: virata invece di velocità |

## La scala dei nomi

I quattro prefissi giapponesi compaiono **due volte ciascuno** — una per i propulsori, una per i timoni — e restano **invariati**:

```
Chiisana (piccolo) -> Nami (onda) -> Ookii (grande) -> Subarashii (meraviglioso)
```

Il test verifica il **conteggio per prefisso** (`2, 2, 2, 2`) e che `rift` **non** sia stato tradotto in «frattura».

## Cosa il test pretende

| oggetto | verifica |
|---|---|
| nomi | quattro prefissi × 2, `rift` conservato, nessuna «frattura» |
| vuote | **0 tab, 0 virgolette, 0 segnaposto, 0 alternative** |
| apici | **2** in inglese, alle righe **327** e **402** (esatte) |
| filo | il confronto con i **Korath** in ≥4 unità; «potenza bruta», «fabbisogno», «riserva antica», «cometa» |
| finale | «cannoniere», «bersaglio» |
| FILE | 33 unità · somma **12+12+9** · prima 25 · ultima 402 · **0 dopo** · copertura **33/33 asserita** |

## Limiti dichiarati

Nessuna approvazione (9 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Il file è **finito in staging**,
non approvato.
