# STATO — L308 (`data/avgi/avgi weapons.txt`, righe 264–703)

**Stato: CHIUSO.** Secondo lotto del file: **ventuno unità di tre tipi** — **13 `DESCRIPTION`** da tradurre, **5 `TEXT`** e **3
`VALUE`** da copiare — con **tre terzine** VLS e **due famiglie** di frasi ripetute. File a **33/46 (71,7%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L308_20261020_210241/` |
| file | `data/avgi/avgi weapons.txt` (**46 unità · 1.432 parole · righe 25–969 · 35 `DESCRIPTION` + 7 `TEXT` + 4 `VALUE`**) |
| righe | 264–703 |
| unità | **21** — **13 `DESCRIPTION` + 5 `TEXT` + 3 `VALUE`** |
| contesti | **6** — `Blue Optical Laser` (2) · `External Launch Rail` (2) · `External Launch Tube` (2) · `Tiny/Small/Medium VLS` (5 ciascuno) |
| parole | **489 EN → 537 IT** (1,10) |
| rapporto | **0,97 – 1,29** |
| tab | **7** — righe **265, 614, 615, 658, 659, 702, 703** |
| virgolette | **10** — 5 coppie, una per unità `TEXT` |
| segnaposto / alternative | **0 / 0** (asserzioni vuote) |
| apici | **3 EN / 9 IT** |
| copiati | **5 `TEXT`** (`"Ophrys" Nuclear Torpedo`, `"Orchid" Nuclear Missile`, `"Nettle" KKV` ×3) + **3 `VALUE`** (`Vertical Launch Array (9/18/36)`) |
| `check.py` | **26 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **25 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: **12 prima** · 21 qui · **13 dopo** la 703 |
| `sha256[:16]` | **`274df52c61b68041`** |

## Comandi

```bash
python staging/editorial/L308_20261020_210241/check.py     # FAIL totale: 0 (26 controlli)
python staging/editorial/L308_20261020_210241/verify.py    # FAIL: 0 (25 controlli)
```

## Tre tipi in un solo lotto

| tipo | n | trattamento |
|---|---|---|
| `DESCRIPTION` | 13 | **tradotto** |
| `TEXT` | 5 | **copiato** — sono **designazioni di munizione fra virgolette** |
| `VALUE` | 3 | **copiato** — `Vertical Launch Array (9)`, `(18)`, `(36)` |

I `TEXT` sono la **prima volta** che questo file ne espone: nel corpus queste stringhe sono **già identiche all'inglese**
(`"Nettle" KKV` → `"Nettle" KKV`), ed è la conferma che la regola «il nome fra virgolette si copia» vale anche qui.

## Due famiglie di frasi ripetute

| famiglia | righe | forma |
|---|---|---|
| **paragrafo VLS** | 614, 658, 702 | «I sistemi di lancio verticale permettono un dispiegamento rapido e versatile dei missili, ma, essendo insieme lanciatori e caricatori, non lasciano spazio a un deposito separato per i missili.» |
| **nota munizioni** | 615, 659, 703 | «Le munizioni di quest'arma si possono rifornire in qualsiasi emporio.» |

La nota munizioni **non è nuova**: le righe **69 e 108 di L307** la contengono già. Il `check.py` **riapre** il
`translation.json` precedente e confronta: ora la famiglia conta **cinque** occorrenze identiche.

## Le tre VLS differiscono solo per il numero di celle

| VLS | celle | `VALUE` |
|---|---|---|
| `Tiny` | 9 | `Vertical Launch Array (9)` |
| `Small` | 18 | `Vertical Launch Array (18)` |
| `Medium` | 36 | `Vertical Launch Array (36)` |

Le tre `DESCRIPTION` che le presentano sono **diverse** (una per droni e caccia, una a schiera rettangolare, una a lancio a
freddo); i **due paragrafi successivi** sono **identici** alle tre.

## La sorellanza 265/203

La **265** (`Blue Optical Laser`) e la **203** di L307 (`Green Optical Laser`) hanno **la stessa frase**: «La torretta contiene
solo l'ottica…». Cambia **solo** la potenza: «un solo **Blue Laser**» contro «tre **Green Laser**».

Il `check.py` confronta le due stringhe **sostituendo** la parte variabile: se la struttura divergesse, il test fallirebbe.

## Limiti dichiarati

Nessuna approvazione (21 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Restano **13 unità**: il
prossimo lotto è **terminale**.
