# STATO — L326 (`data/_deprecated/deprecated outfits.txt`, righe 25–792)

**Stato: CHIUSO — LOTTO TERMINALE, FILE INTERO.** Il file è **completo: 47/47 (100%)**, **quarantesimo file interamente tradotto**
(**99** su 167). `check.py` esce 0 con **28 controlli**; `verify.py` esce 0 con **17 controlli**. `state.py` esce 0 (`ESITO: OK`, 8/8).
Nessuna scrittura su `state.db`.

**Primo lotto del ciclo chiuso al primo giro**, `check.py` e `verify.py` verdi **senza correzioni**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L326_20261020_231245/` |
| file | `data/_deprecated/deprecated outfits.txt` (**47/47 unità · 1.186 parole · righe 25–792**) |
| righe | 25–792 (**tutto il file**) |
| unità | **42 `DESCRIPTION` + 3 `VALUE` + 2 `TEXT`** |
| contesti | **39** — **otto** coppie e **trentuno** singoli |
| parole | **1.186 EN → 1.233 IT** (1,04) |
| rapporto | **0,86 – 1,28** |
| tab | **3** — righe **709, 776, 792** |
| virgolette | **8** in **4** righe (722, 736, 740, **776**) |
| segnaposto / alternative | **0 / 0** |
| apici | **12 EN in 8 unità** (618 ne ha **tre**) / 16 IT |
| `check.py` | **28 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **17 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di FILE**: 47 unità · **0 prima, 0 dopo** · prima **25** · ultima **792** |
| `sha256[:16]` | **`1b8fc5c1e88c6e69`** |

## Comandi

```bash
python staging/editorial/L326_20261020_231245/check.py     # FAIL totale: 0 (28 controlli)
python staging/editorial/L326_20261020_231245/verify.py    # FAIL: 0 (17 controlli, FILE 47/47)
```

## Cinque copiati, e una distinzione che il test fa per la prima volta

| riga | tipo | stringa | precedenti nel corpus |
|---|---|---|---|
| 621 | `VALUE` | `Nanotech Batteries` | **0** |
| 641 | `VALUE` | `Intrusion Countermeasures` | **0** |
| 740 | `VALUE` | `Z-3600 "Beam" Amat Torches` | **0** |
| 722 | `TEXT` | `"Nettle" KKV` | **13** (L176, L177, L309…) |
| 736 | `TEXT` | `"Orchid" Nuclear Missile` | **8** (L176, L177, L309…) |

I due `TEXT` **hanno una resa già stabilita** e il test la cerca **in almeno 5 lotti**; i tre `VALUE` **non hanno precedenti** e si
verificano **solo** per identità all'inglese. È la prima volta che il lotto distingue **due copiati con statuto diverso**: un conto è
«questo nome non si traduce», un altro è «questo nome è **già** stato reso così nel corpus e va ripetuto alla lettera».

## Il file è sotto `_deprecated/`

Materiale **ritirato dal gioco ma ancora nei dati**. Il contratto lo dichiara perché la cartella potrebbe far pensare «non si tocca»:
il trattamento è **identico** a tutti gli altri file (tradotto, verificato, `PENDING`).

## Le due coppie gemelle

| righe | inglese | resa |
|---|---|---|
| 70 / 82 | `This engine is used by Korath fighters.` | **«Questo motore è usato dai caccia Korath.»** (identica) |
| 97 / 109 | `This engine is used in the Korath capital ships.` | **«Questo motore è usato nelle navi capitali Korath.»** (identica) |

Sono **ripetizioni del sorgente** (quattro equipaggiamenti diversi — due propulsori e due timoni — descritti con la stessa frase). La
resa è **una sola**, e `verify.py` la verifica **sul DB** (stesso inglese) **e** sul testo italiano, non solo sul testo.

## Cosa il test pretende

| oggetto | verifica |
|---|---|
| tipi | **42 `DESCRIPTION` + 3 `VALUE` + 2 `TEXT`**, separati |
| copiati | i due `VALUE` senza virgolette, il `VALUE` con virgolette, i due `TEXT` — **quattro asserzioni distinte** |
| gemelle | stesso inglese **nel DB** e stessa resa |
| contesti | **39**; otto coppie esatte |
| tab | **3** (709, 776, 792) e **allineate al conteggio inglese** riga per riga |
| virgolette | **8** in **4** righe; la **776** ha **tab e virgolette insieme** |
| apici | **12** in 8 unità; 618 tripla |
| vuote | **0 segnaposto**, **0 alternative** |
| FILE | **0 prima · 47 qui · 0 dopo** · prima 25 · ultima 792 · **47/47 asserita** |

## Limiti dichiarati

Nessuna approvazione (47 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. I tre `VALUE` non hanno precedenti:
la loro forma è **copiata dal sorgente**, non confermata da un uso precedente nel corpus.
