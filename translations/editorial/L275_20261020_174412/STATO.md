# STATO — L275 (`data/korath/korath ships.txt`, righe 606–1311)

**Stato: CHIUSO.** Terzo lotto del file: **9 `DESCRIPTION` + 5 `VALUE`** su **sette contesti**. Il file è aperto a
**31/50 (62,0%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L275_20261020_174412/` |
| file | `data/korath/korath ships.txt` (50 unità · 2.049 parole · righe 95–2363) |
| righe | 606–1311 |
| unità | **14** — 9 `DESCRIPTION` + 5 `VALUE` |
| parole | **495 EN → 545 IT** (1,10) |
| rapporto | **1,06 – 1,17** (sulle nove `DESCRIPTION`) |
| contesti | **7** — cinque «A'awoj» da produzione + `Kasichara` e `Korsmanath A'awoj` |
| tab | **2** (unità 12, 14) |
| virgolette | **2** (unità 11, `"navi-mondo"`), dritte |
| apici | **9 EN** (tutti in `A'awoj`) / **16 IT** su 13 unità |
| segnaposto | **0** (asserzione negativa) |
| `check.py` | **25 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **21 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 17 prima · 14 qui · **19 dopo** la 1311 |
| `sha256[:16]` | **`92155f43b9321f83`** |

## Comandi

```bash
python staging/editorial/L275_20261020_174412/check.py     # FAIL totale: 0 (25 controlli)
python staging/editorial/L275_20261020_174412/verify.py    # FAIL: 0 (21 controlli, 31/50)
```

## Le cinque navi da produzione

`Karek`, `Sapira`, `Dathnak`, `Spera`, `Ikfar` **A'awoj** — cinque varianti dello **stesso telaio antico**, e le schede lo
dicono con la **stessa formula** in apertura: «Le più grandi navi da produzione Korath derivano da un telaio comune e antico.»
Il `check.py` verifica che la prima frase sia **identica** nelle cinque: se una variante avesse cambiato forma, il test
sarebbe rosso.

I cinque `VALUE` sono i nomi di variante (`Karek A'awoj` …) e sono **copiati**.

## I due abitati nomadi

- **`Kasichara A'awoj`** — nata come **abitazione di lusso** per chi poteva evitare la superficie inquinata dei mondi Korath;
  nell'esilio divenne una `"nave-mondo"` (le **virgolette**, due, sono nel sorgente e restano dritte);
- **`Korsmanath A'awoj`** — «vere città volanti», ma la **militarizzazione** e i materiali insostenibili le tengono lontane
  dall'autosufficienza. La seconda scheda è un quadro politico: **navarchi** contro governo civile, civili che si contendono
  un posto, comitati che litigano con gli ingegneri.

## Limiti dichiarati

Nessuna approvazione (14 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Restano **19 unità**.
