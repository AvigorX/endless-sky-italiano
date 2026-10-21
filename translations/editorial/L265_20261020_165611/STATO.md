# STATO — L265 (`data/kahet/aberrant ships.txt`, righe 16–685)

**Stato: CHIUSO.** Primo lotto del file delle navi **Aberrant**: **43 unità** (26 `VALUE` + 17 `DESCRIPTION`) su **9
contesti**. Il file è aperto a **43/65 (66,2%)**; resta **L266**, che sarà **terminale**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L265_20261020_165611/` |
| file | `data/kahet/aberrant ships.txt` (65 unità · 646 parole · righe 16–1007) |
| righe | 16–685 |
| unità | **43** — 26 `VALUE` + 17 `DESCRIPTION` |
| parole | **429 EN → 418 IT** |
| rapporto | **1,00 – 1,32** |
| contesti | **9** — Latte, Chomper, Pileup, Hugger, Longfellow, Dancer, Junior, Icebreaker, Pike |
| tab / virgolette | **0** / **32** (tutte nelle designazioni) |
| apici | **0 EN** / **10 IT** (le elisioni delle schede) |
| segnaposto | **0** (asserzione negativa) |
| `check.py` | **23 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **21 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 0 prima (il lotto **apre** il file) · 43 qui · **22 dopo** la 685 |
| `sha256[:16]` | **`5e1de6bbd0d2b20c`** |

## Comandi

```bash
python staging/editorial/L265_20261020_165611/check.py     # FAIL totale: 0 (23 controlli)
python staging/editorial/L265_20261020_165611/verify.py    # FAIL: 0 (21 controlli, 43/65)
```

## Le 9 schede distinte

| stringa | unità | resa |
|---|---|---|
| nota organo-metallica (identica) | 3, 8, 13, 18, 23, 28, 33, 38, 43 | «Sembra essere una sorta di entità organo-metallica…» — **una sola resa** |
| `as close to the baseline…` | 4 | «…quanto più vicina al modello di base…» |
| `much more heavily armed…` | 9 | «…molto più armata della maggior parte delle altre della sua specie.» |
| `somewhat larger and sturdier…` | 14 | «…un po' più grande e più robusta…» |
| `lighter and capable of higher speeds…` | 19 | «…più leggera e capace di velocità superiori…» |
| `grown extra thrusters…` | 24 | «…propulsori supplementari attorno a una fusoliera snella e affusolata.» |
| `several hardpoints…` | 29 | «…diversi punti di attacco progettati per montare torrette.» |
| `compact, smaller-than-average…` | 34 | «…compatta, più piccola della media e ancora in fase di crescita.» |
| `growing more elongated…` | 39 | «…in fase di allungamento e ha uno scafo più resistente…» |

## Le designazioni

`K-IA "Latte"`, `Lattes`, `K-IB "Chomper"`, `Chompers`, …, `K-IIC "Pike"`, `Pikes`: **26 `VALUE` copiati**, apice delle
virgolette compreso. Dieci non hanno virgolette: i **nove plurali** e la sigla nuda **`K-IC Pileup`** (unità 15), che il
sorgente scrive **senza** — e la resa conserva l'irregolarità.

## Limiti dichiarati

Nessuna approvazione (43 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Restano **22 unità**.
