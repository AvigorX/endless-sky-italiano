# STATO — L306 (`data/quarg/quarg outfits.txt`, righe 257–579)

**Stato: CHIUSO — LOTTO TERMINALE.** Il file è **completo: 31/31 (100%)**, **ventottesimo file interamente tradotto**
(**87** su 167 nel progetto).

| voce | valore |
|---|---|
| directory | `staging/editorial/L306_20261020_205023/` |
| file | `data/quarg/quarg outfits.txt` (**31/31 unità · 1.506 parole · righe 37–579**) |
| righe | 257–579 |
| unità | **10**, tutte `DESCRIPTION` |
| contesti | **10**, **una sola unità ciascuno** (nessuna coppia) |
| contenuto | 2 **hub di riparazione** (`Peripheral`, `Central`) + 8 **armi** (`Skydagger`, `Skylance`, `Stratospear`, `Elysian Ranseur`, `Celestial Culverin`, `Astral Ribault`, `Slipstream Projector`, `Phalanx System`) |
| parole | **530 EN → 514 IT** (0,97) |
| rapporto | **0,88 – 1,19** |
| tab | **0** (asserzione vuota) |
| virgolette / segnaposto / alternative | **0 / 0 / 0** (asserzioni vuote) |
| apici | **5 EN / 10 IT** |
| `check.py` | **23 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **22 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di FILE**: 31 unità · somma **11+10+10** · righe distinte · prima **37** · ultima **579** · **0 dopo** |
| `sha256[:16]` | **`62365e7d4828f1ec`** |

## Comandi

```bash
python staging/editorial/L306_20261020_205023/check.py     # FAIL totale: 0 (23 controlli)
python staging/editorial/L306_20261020_205023/verify.py    # FAIL: 0 (22 controlli, FILE 31/31)
```

## Dieci contesti, dieci unità: le asserzioni sono vuote

Questo lotto **non ha coppie, non ha tab, non ha virgolette, non ha segnaposto**. Il test lo **dichiara** invece di saltarlo:

```python
set(grp.values()) == {1}                       # nessun contesto doppio
sum(u['english'].count(TAB) ...) == 0          # nessuna tab
sum(u['english'].count(QUOTE) ...) == 0        # nessuna virgoletta
```

Un controllo assente non è un controllo superato: qui l'assenza è **verificata**.

## I nomi delle armi restano inglesi

| nome | traduzione **rifiutata** |
|---|---|
| `Skydagger` | «Pugnale del cielo» |
| `Skylance` | «Lancia delle stelle» |
| `Stratospear` | «Lancia della stratosfera» |
| `Elysian Ranseur` | «Ranseur elisio» |
| `Celestial Culverin` | «Culverina celeste» |
| `Astral Ribault` | «Ribault astrale» |
| `Slipstream Projector` | «Proiettore della scia» |
| `Phalanx System` | «Falange» |

Sono **nomi propri di equipaggiamento**: il test rifiuta le traduzioni tentatrici. **Una sola** arma è nominata **in prosa** — lo
`Skylance` («lo Skylance è un'arma elegante») — e il test verifica che compaia **solo** in quella scheda.

## I due hub

`Peripheral Repair Hub` e `Central Repair Hub` **non si nominano** nelle rispettive schede: dicono «questo sistema» e «un grande
**hub** centrale di fili e tubi». Il test verifica che «hub centrale» compaia e che «hub di riparazione periferico» **non** compaia.

## Il trattino conservato

L'unità 1 ha un elenco con **trattino**:

> «…giova agli aspetti fondamentali del volo spaziale **- durabilità, longevità e, soprattutto, capacità di sopravvivenza.**»

Due punti o virgola sarebbero più eleganti; il trattino è **del sorgente** e resta.

## Limiti dichiarati

Nessuna approvazione (10 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Il file è **finito in
staging**, non approvato.
