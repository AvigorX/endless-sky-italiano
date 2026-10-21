# STATO — L320 (`data/wanderer/wanderer outfits.txt`, righe 40–450)

**Stato: CHIUSO.** Primo lotto del file: **18 unità su 31** (**58,1%**). `check.py` esce 0 con **22 controlli**; `verify.py` esce 0
con **19 controlli**. `state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

| voce | valore |
|---|---|
| directory | `staging/editorial/L320_20261020_222610/` |
| file | `data/wanderer/wanderer outfits.txt` (31 unità · 992 parole · righe 40–659 · 31 `DESCRIPTION`) |
| righe | 40–450 |
| unità | **18** — tutte `DESCRIPTION` |
| contesti | **17** — solo il `Thunderhead Launcher` è doppio |
| parole | **478 EN → 471 IT** (0,985) |
| rapporto | **0,91 – 1,27** |
| tab | **1** — riga 271 |
| virgolette | **0** |
| segnaposto / alternative | **0 / 0** |
| apici | **2 EN / 6 IT** |
| `check.py` | **22 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **19 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: **0 prima** (il lotto apre il file) · 18 qui · **13 dopo** (la prossima alla 463) |
| copertura | **18/31 (58,1%)** — **stampata, non asserita** |
| `sha256[:16]` | **`0a1138a5d4aa814f`** |

## Comandi

```bash
python staging/editorial/L320_20261020_222610/check.py     # FAIL totale: 0 (22 controlli)
python staging/editorial/L320_20261020_222610/verify.py    # FAIL: 0 (19 controlli, 18/31)
```

## Quattro famiglie

| famiglia | righe | che cosa raccontano |
|---|---|---|
| **raggi** | 40, 82, 114, 145, 195 | i Wanderer **non amano le armi** («più costruttive»), ma le poche che fanno sono **efficienti e letali**; il `Sunbeam` è **troppo grosso** per due in una torretta, il `Moonbeam` nasce contro **la corazza dei droni Korath** |
| **missili** | 219, 270–271, 283, 320 | l'antimissile contro i **pod inseguitori** degli **Hai Slegati**; il `Thunderhead` con **cinque submunizioni** indipendenti e **40** per lanciatore |
| **reattori** | 346, 361, 376, 391, 406, 421 | due **celle biochimiche** (microrganismi e bioreattore) e la **scala delle stelle**: `Red` → `Yellow` → `White` → `Blue Sun` |
| **scudi** | 436, 450 | lo **stesso scambio** in due taglie: ricarica più rapida, **consumo maggiore** |

## La scala dei quattro soli

```
Red Sun     «questo piccolo reattore»              → per «ricavare un po' più di energia»
Yellow Sun  «reattore nucleare compatto»           → genera e immagazzina
White Sun   «grande reattore nucleare»             → per le navi Strong Wind
Blue Sun    «nuclei di reattore sempre più grandi» → per le navi da guerra pesanti
```

La progressione è **del sorgente** e la resa la conserva **senza aggiungere commenti**: nessun aggettivo inventato, solo i quattro
gradi che il testo dà.

## Lo scambio replicato

| riga | guadagno | costo |
|---|---|---|
| 436 `Bright Cloud` | «ricaricare a una velocità considerevole» | «consuma anche più energia di altri generatori» |
| 450 `Dark Storm` | «più in fretta di qualsiasi tecnologia umana» | «assorbe anche molta più energia» |

Il test verifica **entrambi** i «ma»: sono la stessa frase in due taglie, e se una delle due avesse perso il costo, il giocatore
avrebbe letto uno scudo **gratis**.

## Cosa il test pretende

| oggetto | verifica |
|---|---|
| tab | **una sola**, riga 271: la nota dei rifornimenti |
| nota | resa **già presente** nel corpus (`check.py`: stringa attesa; `verify.py`: ricerca nel corpus, ≥2 occorrenze) |
| nomi | 13 nomi **invariati** dove compaiono; `Unfettered Hai` → **«Hai Slegati»** (corpus 241 vs 65) |
| numeri | `50%` in più (195), `40` munizioni (283) |
| scala | quattro gradi dei reattori **in crescendo** |
| scudi | lo **scambio** in entrambi |
| vuote | 0 virgolette, 0 segnaposto, 0 alternative |
| apici | **2** in inglese, righe **436** e **450** |

## Limiti dichiarati

Nessuna approvazione (18 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. **Il file non è finito**: restano
**13 unità / 514 parole** (righe 463–659), che lo chiudono in **L321**.
