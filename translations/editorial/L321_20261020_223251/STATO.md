# STATO — L321 (`data/wanderer/wanderer outfits.txt`, righe 463–659)

**Stato: CHIUSO — LOTTO TERMINALE.** Il file è **completo: 31/31 (100%)**, **trentacinquesimo file interamente tradotto** (**94** su
167 nel progetto). `check.py` esce 0 con **21 controlli**; `verify.py` esce 0 con **19 controlli**. `state.py` esce 0 (`ESITO: OK`,
8/8). Nessuna scrittura su `state.db`.

| voce | valore |
|---|---|
| directory | `staging/editorial/L321_20261020_223251/` |
| file | `data/wanderer/wanderer outfits.txt` (**31/31 unità · 992 parole · righe 40–659**) |
| righe | 463–659 |
| unità | **13** — tutte `DESCRIPTION` |
| contesti | **13** — **uno per unità** |
| parole | **514 EN → 547 IT** (1,064) |
| rapporto | **0,95 – 1,27** |
| tab / virgolette | **0 / 0** |
| segnaposto / alternative | **0 / 0** |
| apici | **3 EN su 2 unità** (645 ×1, 652 ×2) / 5 IT |
| `check.py` | **21 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **19 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di FILE**: 31 unità · somma lotti **18+13** · 31 righe distinte · prima **40** · ultima **659** · **0 dopo** |
| `sha256[:16]` | **`bd400d1bce1ce3a8`** |

## Comandi

```bash
python staging/editorial/L321_20261020_223251/check.py     # FAIL totale: 0 (21 controlli)
python staging/editorial/L321_20261020_223251/verify.py    # FAIL: 0 (19 controlli, FILE 31/31)
```

## Due blocchi: i motori, poi le licenze

| righe | blocco | che cosa |
|---|---|---|
| 463–638 | **motori e radiatori** | `Ramscoop`, `Heat Sink`, **due scale di quattro** (`Type 1..4 Radiant Thruster` 498–558 e `Type 1..4 Radiant Steering` 578–638) |
| 645–659 | **le tre licenze** | `Outfits License`, `License`, `Military License` |

## I numeri restano numeri

```
Type 1 Radiant Thruster   «È il più piccolo motore Wanderer.»
Type 4 Radiant Thruster   «È il più grande motore che i Wanderer abbiano sviluppato.»
Type 1 Radiant Steering   il timone dei droni senza pilota
Type 4 Radiant Steering   «È il più grande sistema di timone che i Wanderer vendano.»
```

Il test verifica i **nomi esatti** dei quattro propulsori e dei quattro timoni e la **crescita** («più piccolo» → «più grande»). La
tentazione era rendere `Type 1..4` con «piccolo/medio/grande/massimo»: si sarebbe perso il fatto che il **gioco** chiama così gli
oggetti, e un giocatore che cerca «Type 3 Radiant Steering» nell'emporio non lo troverebbe.

## Il filo: **il calore**

Le otto schede dei motori dicono **la stessa cosa in modi diversi**, ed è la meccanica che il giocatore deve capire:

| riga | come lo dice |
|---|---|
| 498 | «funziona in parte **irradiando** il calore in eccesso» |
| 518 | «**trasferendo** il calore in eccesso … al plasma di scarico» |
| 538 | «usare il motore stesso per **espellere** il calore in eccesso» |
| 558 | «raffreddare la tua nave **anche mentre è in funzione**» |
| 598 | «espelle il calore … **anche quando non è in uso**» |
| 618 | «oltre a far girare la nave, **espellere** una quantità considerevole di calore» |

La resa conserva i **tre verbi** distinti (`radiating`, `transferring`, `vent`) perché descrivono **tre meccanismi**: se fossero
diventati tutti «dissipare», il lotto avrebbe detto tre volte la stessa cosa.

## Le tre licenze sono **oggetti**

| riga | oggetto | diritto |
|---|---|---|
| 645 | un **piatto** con semi di `Sentinel Skirtgrass` | **equipaggiamenti** Wanderer |
| 652 | un **ramo** del `Noble Watchwood` in **ambra** | **navi non militari** |
| 659 | lo **stesso ramo**, rinsecchito, in **bronzo** | **navi da guerra** |

La progressione è **narrativa**, non tecnica: semi → pace → guerra. Il test verifica **i tre oggetti** (piatto / ambra / bronzo) e **i
tre diritti distinti**. Se una licenza avesse concesso «tutto», il terzo oggetto — il ramo morto — avrebbe perso il suo senso.

## Cosa il test pretende

| oggetto | verifica |
|---|---|
| scale | `Type 1..4` per **Thruster** e per **Steering**, nomi esatti |
| crescita | «più piccolo» (498) → «più grande» (558, 638) |
| licenze | piatto / ambra / bronzo + tre diritti diversi |
| seconda persona | **solo** nelle quattro schede dei motori: `[498, 558, 598, 618]` |
| nomi | 9 nomi **invariati** dove compaiono |
| vuote | **0 tab, 0 virgolette, 0 segnaposto, 0 alternative** |
| apici | **3** in inglese su **2** unità (645 ×1, 652 ×2) |
| FILE | 31 unità · **18+13** · prima 40 · ultima 659 · **0 dopo** · copertura **31/31 asserita** |

## Limiti dichiarati

Nessuna approvazione (13 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Il file è **finito in staging**,
non approvato.
