# STATO — L274 (`data/korath/korath ships.txt`, righe 364–602)

**Stato: CHIUSO.** Secondo lotto del file: **8 `DESCRIPTION` + 1 `VALUE`** su **quattro contesti**. Il file è aperto a
**17/50 (34,0%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L274_20261020_173814/` |
| file | `data/korath/korath ships.txt` (50 unità · 2.049 parole · righe 95–2363) |
| righe | 364–602 |
| unità | **9** — 8 `DESCRIPTION` + 1 `VALUE` |
| parole | **430 EN → 477 IT** (1,11) |
| rapporto | **1,00 – 1,31** |
| contesti | **4** — `'olofez` (tre righe), `Kas'ik Tek 7`, `Rai'alorej`, `Ikatila'ej` |
| tab | **4** (unità 3, 5, 7, 9) |
| virgolette / segnaposto | **0 / 0** (asserzioni negative) |
| apici | **5 EN** / **13 IT** su 7 unità |
| `check.py` | **25 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **21 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 8 prima · 9 qui · **33 dopo** la 602 |
| `sha256[:16]` | **`7f062853da3fb523`** |

## Comandi

```bash
python staging/editorial/L274_20261020_173814/check.py     # FAIL totale: 0 (25 controlli)
python staging/editorial/L274_20261020_173814/verify.py    # FAIL: 0 (21 controlli, 17/50)
```

## Il `VALUE` è un plurale

Unico `VALUE` del lotto: **`'olofezes`** — il **plurale** del nome del caccia. Si **copia**, e il test lo distingue dagli altri
otto («identico» per quell'indice, «tradotto» per le `DESCRIPTION`).

## Due stringhe già tradotte, riprese alla lettera

Le unità 3 e 5 (caccia e droni senza iperguida) esistono **identiche** nel corpus, decine di volte. La resa è ripresa **alla
lettera**, e il `check.py` la confronta con la variante **più frequente** di tutti i `translation.json`:

```
"I caccia non sono dotati di iperguida. …una nave con una baia di caccia."
"I droni non sono dotati di iperguida. …una nave con una baia per droni."
```

**Divergenza dichiarata**: `fighter bay` ha nel corpus **due** rese — «baia di caccia» (9) e «baia per caccia» (2). Il lotto usa
la **maggioritaria**; sanare le due unità difformi richiede autorizzazione su lotti chiusi.

## Le quattro schede

| contesto | che cos'è |
|---|---|
| `'olofez` | caccia imbarcato, il più diffuso sulle navi capitali dell'Esilio |
| `Kas'ik Tek 7` | **sonde**: ricognizione, valutazione di vascelli stranieri, recupero di microbot |
| `Rai'alorej` | **rifugio-ospedale**: i Korath non guariscono facilmente dalle ferite |
| `Ikatila'ej` | **fabbrica volante**: supporto critico a stazioni e navi-mondo, riciclaggio |

## Limiti dichiarati

Nessuna approvazione (9 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Restano **33 unità**.
