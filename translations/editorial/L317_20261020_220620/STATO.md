# STATO — L317 (`data/coalition/coalition ships.txt`, righe 1141–2195)

**Stato: CHIUSO — LOTTO TERMINALE.** Il file è **completo: 27/27 (100%)**, **trentatreesimo file interamente tradotto** (**92** su 167
nel progetto). `check.py` esce 0 con **24 controlli**; `verify.py` esce 0 con **23 controlli**. `state.py` esce 0 (`ESITO: OK`,
8/8). Nessuna scrittura su `state.db`.

| voce | valore |
|---|---|
| directory | `staging/editorial/L317_20261020_220620/` |
| file | `data/coalition/coalition ships.txt` (**27/27 unità · 1.105 parole · righe 59–2195**) |
| righe | 1141–2195 |
| unità | **17** — tutte `DESCRIPTION` |
| contesti | **13** — `Pursuer` ×3, `Rover` ×2, `Stalker` ×2, dieci singoli |
| parole | **632 EN → 645 IT** (1,021) |
| rapporto | **0,99 – 1,17** |
| tab | **4** — 1504, 1505, 1564, 1621 |
| virgolette | **0** |
| segnaposto / alternative | **0 / 0** |
| apici | **1 EN / 7 IT** |
| `check.py` | **24 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **23 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di FILE**: 27 unità · somma lotti **10+17** · 27 righe distinte · prima **59** · ultima **2195** · **0 dopo** |
| `sha256[:16]` | **`6a01542305e995d0`** |

## Comandi

```bash
python staging/editorial/L317_20261020_220620/check.py     # FAIL totale: 0 (24 controlli)
python staging/editorial/L317_20261020_220620/verify.py    # FAIL: 0 (23 controlli, FILE 27/27)
```

## La nota dei caccia, misurata **prima** di tradurla

Il contratto diceva di misurarla, non di presumerla. Misura:

```
1505 == 1564 == 1621     la STESSA nota, «Fighters do not come equipped with a hyperdrive…»
1504 != 1505             altra nota del Pursuer: progetto Kimek, più economico e più veloce
```

Quindi **una frase ripetuta tre volte** in **tre navi diverse** — non tre note di una stessa nave come in L312. La resa è **identica
nelle tre** e il test lo verifica a **tre lati**, in entrambe le lingue:

> «I caccia non sono dotati di motore iperspaziale. Non puoi trasportare un caccia se non hai nella tua flotta una nave con una baia di
> caccia.»

## L'unica seconda persona del file, e dove sta

In un file impersonale da catalogo, la **seconda persona** compare **solo** nella nota dei caccia («You cannot carry a fighter»),
perché è un'**istruzione all'acquirente**, non una descrizione. Il test la **elenca** invece di lasciarla passare:

```
unità con seconda persona = [1505, 1564, 1621]   esattamente le tre note
```

## I tre popoli, e le loro navi

| popolo | navi | che cosa dicono di loro |
|---|---|---|
| **Heliarch** | `Neutralizer`, `Punisher`, `Pursuer` ×3, `Rover`, `Stalker` | pattugliatori «appena abbastanza forti», i **Skylance rubati ai Quarg** per la guerra, il **cadetto** che si guadagna un caccia |
| **Kimek** | `Briar`, `Spire`, `Thistle`, `Thorn` | **popolazione doppia** rispetto a Saryd e Arachi insieme: trasporti come necessità; lo `Spire` con **cabine per un Kimek**, soffitti bassi per un Saryd, letti corti per un Arach |
| **Saryd** | `Runabout`, `Sojourner`, `Traveler`, `Visitor` | **solitudine e collaborazione** insieme (due persone minime per nave), **diecimila anni** di spazio prima dei Kimek, navi **scientifiche** diventate **case** |

## Cosa il test pretende

| oggetto | verifica |
|---|---|
| famiglia | nota identica in **1505, 1564, 1621**; **1504 diversa** |
| seconda persona | **solo** nelle tre note (`[1505, 1564, 1621]`) |
| tab | righe esatte `[1504, 1505, 1564, 1621]` |
| nomi | 13 nomi di nave + `Skylance` **invariati**; `Coalition` → «Coalizione» |
| contenuti | Spire (cuccette/soffitti/letti), Visitor (versatilità), Traveler (navi scientifiche, radici) |
| vuote | 0 virgolette, 0 segnaposto, 0 alternative |
| FILE | 27 unità · **10+17** · prima 59 · ultima 2195 · **0 dopo** · copertura **27/27 asserita** |

## Limiti dichiarati

Nessuna approvazione (17 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Il file è **finito in staging**,
non approvato.
