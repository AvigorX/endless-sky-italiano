# STATO — L299 (`data/coalition/coalition outfits.txt`, righe 356–509)

**Stato: CHIUSO.** Terzo lotto del file: **quattordici schede** in **dieci contesti** — **due coppie**, **una terzina** (prima
del file) e **sette singole**. File a **44/49 (89,8%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L299_20261020_201104/` |
| file | `data/coalition/coalition outfits.txt` (**49 unità · 1.608 parole · righe 26–533 · 49 `DESCRIPTION`**) |
| righe | 356–509 |
| unità | **14**, tutte `DESCRIPTION` |
| contesti | **10** — 2 doppi + **1 triplo** + 7 singoli |
| coppie | `Small Reverse` 394/395 · `Large Reverse` 414/415 |
| terzina | **`Guardian Turret` 495/496/497**, tab su **496 e 497** |
| singole | `Small Thrust` 356 · `Large Thrust` 375 · `Small Steering` 434 · `Large Steering` 453 · `Enforcer Confrontation Gear` 467 · `Enforcer Riot Staff` 481 · `Anti-Materiel Gun` 509 |
| parole | **467 EN → 463 IT** (0,99) |
| rapporto | **0,90 – 1,22** |
| tab | **4** — righe **395, 415, 496, 497** |
| virgolette / segnaposto / alternative | **0 / 0 / 0** (asserzioni vuote) |
| apici | **4 EN / 13 IT** |
| ripetizione | **unità 4 e 6 identiche** (righe 395 e 415) |
| seconda persona | **2 unità** (4, 6) — istruzioni di installazione |
| `check.py` | **24 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **25 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: **30 prima** · 14 qui · **5 dopo** la 509 |
| `sha256[:16]` | **`3d68cd4b1f275625`** |

## Comandi

```bash
python staging/editorial/L299_20261020_201104/check.py     # FAIL totale: 0 (24 controlli)
python staging/editorial/L299_20261020_201104/verify.py    # FAIL: 0 (25 controlli)
```

## La prima terzina del file

`Guardian Turret` occupa **tre righe consecutive** (495, 496, 497) e le ultime **due** iniziano con `\t`: è **una** scheda
spezzata in **tre** stringhe. Il test verifica:

1. **tre** unità dello stesso contesto, su righe **consecutive**;
2. la tab sulla **seconda e sulla terza**, **non** sulla prima;
3. **quattro** tab in tutto il lotto, alle righe dichiarate.

Un controllo scritto come «coppia» avrebbe fallito su un testo corretto: qui il gruppo è di **tre**.

## La frase ripetuta

Le unità **4** (395) e **6** (415) hanno **lo stesso testo inglese** — l'istruzione «Because a reverse thruster must be facing
forwards…» compare sotto **entrambi** i moduli di spinta inversa. La resa è **identica**, verificata in entrambe le lingue: è
un'**istruzione**, non una descrizione, e il giocatore deve leggere la stessa frase sotto lo stesso vincolo.

## Registro: seconda persona solo dove serve

Solo le unità **4 e 6** dicono «della **tua** nave»: sono le **uniche** istruzioni di installazione del lotto («va installato
nella sezione armi»). Tutte le altre quattordici schede restano in terza persona. Il test **elenca** le due righe ammesse.

## Terminologia

| inglese | resa | nota |
|---|---|---|
| `reverse thruster` | **propulsore di spinta inversa** | **corpus** (74 occorrenze), non «invertitore» |
| `steering systems` | **sistemi di governo** / **governo** | corpus |
| `capital ship drives` | **propulsori per navi capitali** | |
| `anti-boarder equipment` | **attrezzatura antiabbordaggio** | |
| `sniping attacks` | **attacchi di cecchinaggio** | |
| `boarding encounters` | **scontri di abbordaggio** | |
| `dissidents` | **dissidenti** | |
| `non-lethal manner` | **modo non letale** | |
| `Heliarch` / `Quarg` | **invariati** | |

## Limiti dichiarati

Nessuna approvazione (14 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Restano **5 unità**: il
prossimo lotto è **terminale**.
