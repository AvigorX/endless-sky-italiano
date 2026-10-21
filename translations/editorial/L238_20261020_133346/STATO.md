# STATO — L238 (`data/avgi/avgi news.txt`, righe 418–507)

**Stato: CHIUSO.** Sesto e **ultimo** lotto del file, **21 unità**, tutte `NEWS`. **`data/avgi/avgi news.txt` è
COMPLETO: 115/115 (100%)**, 2.164 EN → 2.124 IT in sei lotti — **ottavo file chiuso** della campagna.

| voce | valore |
|---|---|
| directory | `staging/editorial/L238_20261020_133346/` |
| file | `data/avgi/avgi news.txt` (115 unità · 2.164 parole) |
| righe | 418–507 (**507 = ultima del file**) |
| unità | **21** |
| parole | **502 EN → 508 IT** |
| rapporto | **0,95 – 1,23** (media 1,10), gate 0,55–1,90 |
| contesti | **4** — `engineer` 7 (418–424), `artist` 3 (452–454), `performer` 3 (478–480), `doctor` 8 (500–507) |
| tipi | **21 `NEWS`** |
| tab / virgolette | **0 / 42** (2 per unità, 21/21) |
| apici | **15 EN** su 10 unità · **20 IT** su 11 · massimo 4 in una sola (11) |
| segnaposto / identiche | **0 / 0** |
| etichette | **20 in testa** + **1 a metà frase** (454: «… uno spreco, enfasi.») |
| etichette nuove | `Fascination` → Fascinazione (2) · `Appreciation` → Apprezzamento (3) · `Advisement` → Avviso (1) · `Consideration` → Considerazione (2) · `Recollection` → Rievocazione (2) |
| `check.py` | **37 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **21 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di FILE**: 22 + 20 + 15 + 23 + 14 + 21 = **115/115**, riga 507 ultima, 0 dopo, 0 sovrapposizioni |
| `sha256[:16]` | **`21ea58dec8dd91bb`** |

## Comandi

```bash
python staging/editorial/L238_20261020_133346/check.py     # FAIL totale: 0 (37 controlli)
python staging/editorial/L238_20261020_133346/verify.py    # FAIL: 0 (21 controlli, FILE 115/115)
```

## Cosa contiene

Sette **ingegneri** (la fascinazione per gli scudi «anche deboli», la scienza dei materiali contro gli scafi degli
Aberrant, l'iperpropulsore, la torcia a fusione, le navi a torcia prima degli scudi energetici, l'officina meccanica
contro la «tolleranza al nanometro»), tre **artisti** (l'opera nuova, il mercato dell'arte fermo, l'arte che non toglie
risorse allo sforzo bellico), tre **artisti dello spettacolo** (l'esibizione davanti all'Assemblea, la Twilight Guard che
li scrittura per intrattenere le Guardie, la paga di chi si è comprato l'uscita dall'assedio) e otto **medici** (i
sessant'anni di vita naturale, i mediciti che non fanno miracoli, i cervelli di quarzo, la morte che spegne i ricordi, il
sistema nervoso ottico, la luce ultravioletta di Anax, due ricordi di lavoro — la nave mercantile e la manifattura su
asteroide).

## Limiti dichiarati

Nessuna approvazione (21 unità `PENDING`), nessuna notizia vista nel gioco, nessuna revisione umana. Il file è completo
**in staging**, non nel database.
