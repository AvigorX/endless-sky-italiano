# BATCH_LEDGER — fase batch ENDLESS SKY IT · **CHIUSA**

## 1. Stato finale misurato

```
STAGING         32.924 unità · 979.975 EN · 936.995 IT · 402 lotti · 400 con check.py/verify.py
DB              32.560 PENDING + 364 APPROVED = 32.924 → 0 unità fuori dallo staging
FILE            167 file, tutti coperti (nessuna unità PENDING residua)
```
Ogni unità del database ha una resa in `staging/editorial/`: il residuo editoriale è **zero**.

Lo staging **non è approvazione**: `state.db` non è stato scritto (mtime invariato), nessun caricamento nel gioco,
`git -C ../endless-sky status --porcelain` = 0 righe, HEAD `b4aa3bac3`.

## 2. Lotti della fase batch (L333–L398, gate `batch_lot.py`, check+verify exit 0)

| lotto | file | unità | parole EN → IT | sha256[:16] |
|---|---|---|---|---|
| L333 | `persons.txt` | 49 | 752 → 745 | `84c91bb0dfa29bc4` |
| L334 | `human/news.txt` | 202 | 716 → 704 | `d553d288aa8897ce` |
| L335 | `successors/successor weapons.txt` | 14 | 708 → 696 | `515e305fe707f1d6` |
| L336 | `pug/pug missions.txt` | 16 | 685 → 584 | `6817947cd3b0a5a6` |
| L337 | `sheragi/sheragi outfits.txt` | 14 | 666 → 659 | `bc15082656909178` |
| L338 | `remnant/remnant events.txt` | 11 | 564 → 554 | `535b43dbd0ef5c8e` |
| L339 | `_ui/flight checks.txt` | 10 | 542 → 525 | `d6b853fc760fce0f` |
| L340 | `coalition/coalition weapons.txt` | 16 | 523 → 518 | `2a7b49214c28c9e1` |
| L341 | `hai/unfettered jobs.txt` | 49 | 858 → 841 | `486bd18fa99cbf20` |
| L342 | `wanderer/wanderer ships.txt` | 17 | 510 → 523 | `b496522870d1d46b` |
| L343 | `successors/successor variants.txt` | 162 | 486 → 486 | `5acd17346229484c` |
| L344 | `drak/drak missions.txt` | 27 | 508 → 454 | `6988338eeeb181a6` |
| L345 | `pug/pug outfits.txt` | 16 | 504 → 450 | `9b66f2fcf10d1acb` |
| L346 | `bunrodea/bunrodea ships.txt` | 10 | 490 → 498 | `cc0152a30fa0fd61` |
| L347 | `harvesting.txt` | 45 | 484 → 480 | `d0b41bbdb5d8d72f` |
| L348 | `human/near earth jobs.txt` | 32 | 470 → 482 | `b20b5ce10f6414d0` |
| L349 | `kahet/aberrant outfits.txt` | 9 | 364 → 365 | `31bd5f118349aaf3` |
| L350 | `bunrodea/bunrodea weapons.txt` | 9 | 359 → 360 | `bdcbce184b4088b9` |
| L351 | `kahet/aberrant missions.txt` | 7 | 349 → 323 | `7ea5ae81f42e1ab5` |
| L352 | `human/dirt belt jobs.txt` | 33 | 459 → 492 | `cbb241390cf60f04` |
| L353 | `human/rim jobs.txt` | 26 | 392 → 411 | `1e61b258ad1513fa` |
| L354 | `human/hails.txt` | 30 | 392 → 361 | `c728d1eeac9357ee` |
| L355 | `korath/korath jobs.txt` | 25 | 331 → 345 | `f221dc5bd4185d3f` |
| L356 | `gegno/gegno jobs.txt` | 18 | 330 → 288 | `2dee142bb2460ee5` |
| L357 | `kahet/beyond patir assets.txt` | 26 | 330 → 322 | `423151906046f288` |
| L358 | `drak/indigenous.txt` | 8 | 326 → 352 | `2ed7b7a8df965138` |
| L359 | `quarg/quarg.txt` | 7 | 311 → 282 | `7ee593a9853d122f` |
| L360 | `_ui/messages.txt` | 53 | 307 → 329 | `18caef0d7c9f9c20` |
| L361 | `quarg/quarg ships.txt` | 6 | 297 → 325 | `201748a4a5e92468` |
| L362 | `drak/drak outfits.txt` | 12 | 291 → 292 | `984579a25032d05b` |
| L363 | `incipias/incipias ships.txt` | 10 | 291 → 312 | `89f932aa55f79c3f` |
| L364 | `kahet/kahet ships.txt` | 12 | 291 → 282 | `b2494d92f32e1732` |
| L365 | `gegno/gegno events.txt` | 4 | 239 → 238 | `41fb732ebb99129d` |
| L366 | `sheragi/sheragi ships.txt` | 5 | 220 → 234 | `633e4463bf9577fb` |
| L367 | `human/message buoys.txt` | 10 | 210 → 227 | `f3234a127b83cf13` |
| L368 | `vyrmeid/vyrmeid.txt` | 7 | 170 → 184 | `1fc5782498c29105` |
| L369 | `_deprecated/deprecated ships.txt` | 7 | 191 → 216 | `17496fdf7de4cbb2` |
| L370 | `successors/successor events.txt` | 4 | 164 → 167 | `0dfb0e9f71b104f2` |
| L371 | `pug/pug ships.txt` | 4 | 156 → 168 | `abea7ceb6ac01479` |
| L372 | `avgi/windjammers.txt` | 8 | 153 → 152 | `79d10e01258ba129` |
| L373 | `map beyond patir.txt` | 3 | 110 → 103 | `a599a0c1bf748192` |
| L374 | `human/far north jobs.txt` | 8 | 101 → 112 | `5c2f5d882a24a0fc` |
| L375 | `successors/successor sales.txt` | 32 | 96 → 96 | `f25c57f08e99ee49` |
| L376 | `successors/successor hails.txt` | 14 | 94 → 100 | `1f452e5017cb3074` |
| L377 | `rulei/rulei outfits.txt` | 3 | 90 → 83 | `5795ef4dff05e137` |
| L378 | `iije/iije.txt` | 4 | 82 → 77 | `88944d1da88588f5` |
| L379 | `incipias/tace mesa.txt` | 3 | 80 → 70 | `5ff615dfd57202a1` |
| L380 | `remnant/remnant.txt` | 4 | 64 → 60 | `49bdf1d1e55be08c` |
| L381 | `avgi/avgi events.txt` | 2 | 59 → 58 | `6793441858fd140a` |
| L382 | `rulei/rulei ships.txt` | 1 | 54 → 48 | `554a591c7024be24` |
| L383 | `globals.txt` | 2 | 46 → 44 | `dfb7f941ce91c6f0` |
| L384 | `drak/drak ships.txt` | 1 | 40 → 39 | `4c938a75aa9493e2` |
| L385 | `_deprecated/deprecated events.txt` | 1 | 29 → 26 | `9e4c25f67088140c` |
| L386 | `gamerules.txt` | 1 | 11 → 13 | `2609953f414178b6` |
| L387 | `hai/hai news.txt` | 46 | 46 → 46 | `e5f1695205b1c22c` |
| L388 | `wanderer/wanderer news.txt` | 24 | 24 → 24 | `b1ae0d102c94da56` |
| L389 | `remnant/remnant news.txt` | 8 | 8 → 8 | `32ada82ea09963b1` |
| L390 | `korath/korath news.txt` | 2 | 2 → 2 | `c615cce19dca1bd9` |
| L391 | `successors/successors.txt` | 2 | 6 → 8 | `e3e7c25c54ef68b0` |
| L392 | `successors/successor news.txt` | 14 | 73 → 86 | `1671bd3fe40c543c` |
| L393 | `avgi/avgi sales.txt` | 11 | 34 → 34 | `3016626821380f92` |
| L394 | `hai/hai.txt` | 27 | 81 → 81 | `b76bf84895e3f914` |
| L395 | `human/variants.txt` | 37 | 105 → 105 | `4ee547ad78970a24` |
| L396 | `governments.txt` | 58 | 79 → 94 | `2acafa0d1bb73ef7` |
| L397 | `human/deep jobs.txt` | 1 | 2 → 2 | `43bc19cf2235ec69` |
| L398 | `_ui/interfaces.txt` | 244 | 477 → 475 | `7536df83bf668744` |

**Totale fase batch**: 66 lotti, **1583 unità**, **18282 parole EN → 18120 IT**.

## 3. Metodo

```bash
R=$(python -c '…min(line),max(line)…')     # MISURA SEMPRE PRIMA
python staging/editorial/tools/export_section.py "staging/editorial/L<n>_$(date +%Y%m%d_%H%M%S)" "<path>" <min> <max>
#  → traduzione a mano in parts/*.json (o copia dichiarata per nomi propri, `???`, bersagli `goto`)
python staging/editorial/tools/batch_lot.py check|verify staging/editorial/L<n>_*/
```

`check.py`/`verify.py` = wrapper di 4 righe del gate; `id_ok.json` dichiara le unità identiche per necessità;
`STATO.md` per ogni lotto con dati (397 lotti in formato `L<n>_`; i 5 lotti storici a due caratteri — `L19`, `L21a`, `L3b`, `L3c`, `L3d` — hanno solo `NOTE.md`/`REPORT.md` d'epoca).

## 4. Difetti del gate trovati e corretti (con probe di falsificabilità)

| # | difetto misurato | correzione | probe |
|---|---|---|---|
| 1 | rapporto caratteri 0,55–1,90 inapplicabile alle etichette corte (`no fuel` 7 caratteri → 3,43) | sotto 8 parole inglesi vale `ratio ≤ 3,0` | unità corta gonfiata → `check` exit 1; L346/L350/L353 restano verdi |
| 2 | `SEGMENTO` pretendeva l'esclusività del file: impossibile per un lotto di completamento (1 unità `UI_LABEL` rimasta) | il lotto deve coprire **esattamente il residuo della finestra** | unità tolta → `verify` exit 1 |
| 3 | lo stato era ammesso solo `PENDING`: le 244 `APPROVED` di `interfaces.txt` non potevano passare | ammesso `APPROVED` **solo se il testo coincide col DB** | vedi §5 |

## 5. Trascrizioni `APPROVED` (il testo approvato vince)

| file | unità | lotto |
|---|---|---|
| `data/_ui/help.txt` | 68 | L327, L328, L329 |
| `data/_ui/tooltips.txt` | 52 | L111–L116 (667 unità del file, 52 approvate) |
| `data/_ui/interfaces.txt` | 244 | **L398** (lotto unico, file intero) |

## 6. Unità copiate per necessità (dichiarate in `id_ok.json`, mai tradotte)

- nomi di navi/equipaggiamenti con prefisso alieno (`"Basrem" Atomic Thruster`, `"Aqra" Inductive Reverser`, …);
- `???` delle navi/oggetti non identificati (`beyond patir`, `Magic Asteroid`, governi `Ember Waste`);
- bersagli `goto`/`label` (`blind acceptance` in `deep jobs.txt`) — etichette interne, non testo;
- frammenti di sola punteggiatura (`"` delle news estratte come unità singole).

## 7. Lacune dell'estrattore (dichiarate, non riparate)

I file `hai news.txt` (46 unità), `wanderer news.txt` (24), `remnant news.txt` (8), `korath news.txt` (2) e
`successor news.txt` (12 su 14) producono **solo il carattere `"`** come unità: il testo delle notizie non è stato
estratto. Le unità sono copiate e i lotti sono verdi, ma **il contenuto reale di quelle notizie non è in staging**
e richiede un intervento su `tools/l10n.py` (protetto: fuori dal perimetro dei lotti).

## 8. Prossimo passo (fuori dal batch)

1. voce `UI_LABEL` (630 etichette in `_ui/tooltips.txt`) — conteggiate a parte, non nel residuo dei lotti;
2. revisione linguistica umana sullo staging (97,2% di resa in parole);
3. solo dopo l'approvazione: scrittura su `state.db` e caricamento nel gioco.
