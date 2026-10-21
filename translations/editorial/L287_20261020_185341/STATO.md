# STATO — L287 (`data/gegno/gegno ships.txt`, righe 303–658)

**Stato: CHIUSO.** Secondo lotto del file: **9 descrizioni**, **tre spezzate su due unità consecutive** e una che **continua**
la scheda del `Corundum` aperta in L286. File a **16/37 (43,2%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L287_20261020_185341/` |
| righe | 303–658 |
| unità | **9**, tutte `DESCRIPTION` |
| parole | **466 EN → 446 IT** (0,96) |
| rapporto | **0,85 – 1,06** |
| contesti | **6** — `Corundum` · `Protolith` · `Dunite` ×2 · `Augen` ×2 · `Slate` · `Schist` ×2 |
| coppie consecutive | **3** — 417–418, 553–554, 657–658 |
| tab | **4** (unità 1, 4, 6, 9) |
| virgolette | **0** · apici **4 EN / 10 IT** |
| segnaposto / alternative | **0 / 0** (asserzioni vuote) |
| `check.py` | **24 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **22 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 7 prima · 9 qui · **21 dopo** la 658 |
| `sha256[:16]` | **`4298463b944df0ab`** |

## Comandi

```bash
python staging/editorial/L287_20261020_185341/check.py     # FAIL totale: 0 (24 controlli)
python staging/editorial/L287_20261020_185341/verify.py    # FAIL: 0 (22 controlli)
```

## Le tre coppie spezzate

| nave | righe | la seconda metà comincia con | come continua |
|---|---|---|---|
| `Dunite` | 417–418 | «**Essendo** un ammasso di macchinari…» | senza ripetere «I Dunite sono» |
| `Augen` | 553–554 | «**Il progetto** doveva produrre due colossi gemelli…» | il soggetto è **il progetto**, non la nave |
| `Schist` | 657–658 | «**Benché** siano armati in modo leggero…» | subordinata concessiva, soggetto implicito |

Tutte e tre **non ricominciano**: il test verifica le tre aperture e che la seconda metà dell'`Augen` **non** si apra con «L'Augen».

## Il `Corundum` che attraversa due lotti

L286 chiudeva la scheda del `Corundum` con «…due sistemi di trivellazione regolabili, capaci di montare strumenti minerari più
avanzati.» L287 riprende:

> «**Pur non potendo montare** il potente Excavator Drill, la capacità motore del Corundum è doppia rispetto a quella del
> Gypsum…»

Il testo **prosegue**: nessuna nuova introduzione della nave. Il `verify.py` **riapre il `translation.json` di L286**, prende la
riga 302 e verifica che finisca con «avanzati.» e che questa unità cominci con «Pur non potendo»: una continuità **fra due
lotti**, controllata da codice.

## Terminologia

| inglese | resa | nota |
|---|---|---|
| `Generation ships` | **navi generazionali** | come in L286 |
| `hyperdrive-capable` | **capaci di iperguida** | |
| `intrastellar craft` | **vascelli puramente intrastellari** | |
| `hodgepodge of parts` | **guazzabuglio di parti** | |
| `mace-like protrusion` | **sporgenza a forma di mazza** | |
| `jousting and ramming` | **giostrare e speronare** | |
| `bunks` / `platoon` | **cuccette** / **plotone** | |
| `Irate Cannon`, `Ballistic Cannons`, `Excavator Drill` | **invariati** | nomi di equipaggiamento |
| `Augen-Class` | **L'Augen-Class** | elisione, non «La Augen» |
| `Enbi`, `Heutesl`, `Sopi Lefarkata` | **invariati** | luoghi |

## Limiti dichiarati

Nessuna approvazione (9 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Restano **21 unità**.
