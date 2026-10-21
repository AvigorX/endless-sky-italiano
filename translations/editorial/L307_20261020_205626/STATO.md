# STATO — L307 (`data/avgi/avgi weapons.txt`, righe 25–203)

**Stato: CHIUSO.** Primo lotto del file: **dodici schede** in **sei contesti** — **due terzine**, **due coppie** e **due singole**,
con una **nota di gioco ripetuta** sotto due armi diverse. File a **12/46 (26,1%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L307_20261020_205626/` |
| file | `data/avgi/avgi weapons.txt` (**46 unità · 1.432 parole · righe 25–969 · 35 `DESCRIPTION` + 7 `TEXT` + 4 `VALUE`**) |
| righe | 25–203 |
| unità | **12**, tutte `DESCRIPTION` |
| contesti | **6** — 2 terzine + 2 coppie + 2 singole |
| terzine | `Speckle Coilgun` 67/68/69 · `Speckle Turret` 106/107/108 |
| coppie | `Optical Lasing Generator` 173/174 · `Green Optical Laser` 202/203 |
| singole | `Speck Round` 25 · `Speck Magazine` 38 |
| parole | **497 EN → 521 IT** (1,05) |
| rapporto | **1,06 – 1,27** |
| tab | **6** — righe **68, 69, 107, 108, 174, 203** |
| virgolette / segnaposto / alternative | **0 / 0 / 0** (asserzioni vuote) |
| apici | **1 EN / 10 IT** |
| ripetizione | **unità 5 e 8 identiche** (righe 69 e 108) |
| refuso del sorgente | **non riprodotto** (riga 174 `can altered`) |
| `check.py` | **23 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **25 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: **0 prima** · 12 qui · **34 dopo** la 203 |
| `sha256[:16]` | **`7de7ed1f00e0f2c7`** |

## Comandi

```bash
python staging/editorial/L307_20261020_205626/check.py     # FAIL totale: 0 (23 controlli)
python staging/editorial/L307_20261020_205626/verify.py    # FAIL: 0 (25 controlli)
```

## La nota di gioco ripetuta

Le righe **69** e **108** sono **identiche**:

> *Ammunition for this weapon can be restocked at any outfitter.*

Compare sotto `Speckle Coilgun` e sotto `Speckle Turret`. La resa è **una sola**: «Le munizioni di quest'arma si possono
rifornire in qualsiasi **emporio**.» (`outfitter` → **emporio**, dal corpus). È una **nota di sistema**, non prosa: cambiarla in
una delle due armi avrebbe dato due regole diverse per lo stesso gioco.

## Il refuso del sorgente non si riproduce

La riga 174 dice, in inglese:

> *The wavelength of light produced in the coil **can altered** by swapping the diodes…*

Manca il verbo. L'italiano è **corretto** — «può essere modificata» — e il test **verifica** che il refuso non sia stato ricopiato
(`'altered' not in …`). Stessa regola di `Gypusm's` (L286) e di `Although is it lightly armed` (L287).

## Le due terzine

| gruppo | righe | struttura |
|---|---|---|
| `Speckle Coilgun` | 67 (descrizione) · **68** arma · **69** nota munizioni | tre stringhe, tab sulla 2ª e 3ª |
| `Speckle Turret` | 106 (descrizione) · **107** arma · **108** nota munizioni | idem |

La terza unità delle due terzine è **la stessa nota**: la struttura `[arma] → [tattica] → [nota di sistema]` si ripete, ma solo la
nota è **condivisa** alla lettera.

## Terminologia

| inglese | resa | nota |
|---|---|---|
| `outfitter` | **emporio** | corpus |
| `coilgun` | **coilgun** | invariato |
| `mass driver rounds` | **colpi da cannone a massa** | |
| `momentum-repulsion shield systems` | **scudi a repulsione di quantità di moto** | |
| `antimissile system` | **sistema antimissile** | |
| `doped optical fiber` | **fibra ottica drogata** | |
| `lasing medium` | **mezzo attivo** | |
| `gain-switched` | **commutate in guadagno** | |
| `Speckle Coilgun`, `Speckle Turret`, `Optical Lasing Generator`, `Green Optical Laser`, `Blue Optical Laser` | **invariati** | |

## Limiti dichiarati

Nessuna approvazione (12 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Restano **34 unità**.
