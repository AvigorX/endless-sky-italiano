# STATO — L286 (`data/gegno/gegno ships.txt`, righe 53–302)

**Stato: CHIUSO.** Primo lotto del file: **sette descrizioni di nave** dei **Gegno**, in **prosa tecnica**. Il file è aperto a
**7/37 (18,9%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L286_20261020_184802/` |
| file | `data/gegno/gegno ships.txt` (37 unità · 2.036 parole · righe 53–1.616 · 36 `DESCRIPTION` + 1 `VALUE`) |
| righe | 53–302 |
| unità | **7**, tutte `DESCRIPTION` |
| parole | **454 EN → 466 IT** (1,03) |
| rapporto | **1,01 – 1,11** |
| contesti | **6** — `Shale` · `Dolomite` · `Conglomerate` · `Granofel` · `Gypsum` (×2) · `Corundum` |
| tab | **1** (unità 6, la seconda metà del `Gypsum`) |
| virgolette | **0** · apici **4 EN / 6 IT** |
| segnaposto / alternative | **0 / 0** (asserzioni vuote) |
| `check.py` | **25 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **23 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 0 prima (il lotto **apre** il file) · 7 qui · **30 dopo** la 302 |
| `sha256[:16]` | **`8b6255a50fb2b4a2`** |

## Comandi

```bash
python staging/editorial/L286_20261020_184802/check.py     # FAIL totale: 0 (25 controlli)
python staging/editorial/L286_20261020_184802/verify.py    # FAIL: 0 (23 controlli)
```

## Il registro cambia: terza persona

Per la prima volta il lotto **non ha «tu»**: sono **descrizioni di nave**, non dialoghi. Il test verifica l'**assenza** di
`tu/tuo/tua/tuoi/tue/ti/te` — un controllo che in un lotto di missioni sarebbe sbagliato e qui è necessario.

## `Gypsum`: una descrizione su due unità

La descrizione del `Gypsum` è **spezzata** in due unità consecutive (243 e 244) e la seconda **continua** la prima:

> «…La piattaforma che ne risultò, il Gypsum, non è molto più che un trapano volante…»
> «**Poiché i motori Gegno non sono molto potenti**, il Gypsum ha difficoltà a inseguire gli asteroidi più veloci…»

Il test verifica che la seconda **non ricominci** con «Il Gypsum» e che il testo prosegua con `Poiché`: tradurre le due metà come
frasi autonome avrebbe prodotto una ripetizione visibile nel gioco.

## Il refuso del sorgente

L'unità 7 scrive **`Gypusm's`** (una `m` di troppo) invece di `Gypsum's`. In italiano il nome resta **`Gypsum`**, quindi il refuso
**non si riproduce**: il test verifica che `Gypusm` **non** compaia nella resa e che il nome corretto sì. È il caso opposto della
citazione non chiusa (L257–L259), che invece si riproduce: **un refuso su una parola italiana si corregge, un refuso su un nome
proprio si neutralizza, una citazione si conserva**.

## I nomi di modello

`Shale` · `Dolomite` · `Conglomerate` · `Granofel` · `Gypsum` · `Corundum` · `Gegno` · `Vi` · `Scin` · `Shuttle` ·
**`Excavator Drill`** — tutti **invariati**. `Excavator Drill` è un **equipaggiamento** (nome proprio di oggetto), non un
«escavatore»: resta inglese come i nomi delle navi.

## Limiti dichiarati

Nessuna approvazione (7 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Restano **30 unità**.
