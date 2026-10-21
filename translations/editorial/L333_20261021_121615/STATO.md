# STATO — L333 (`data/persons.txt`, righe 186–2263) — **TERMINALE, FILE INTERO** (modalità batch)

Gate: `staging/editorial/tools/batch_lot.py` (check e verify, entrambi **exit 0**). `state.py` `ESITO: OK`. `state.db` non toccato.

| voce | valore |
|---|---|
| directory | `staging/editorial/L333_20261021_121615/` |
| righe | 186–2263 (**tutto il file**) |
| unità | **49** = **27 `TEXT` + 20 `DESCRIPTION` + 2 `VALUE`** |
| contesti | **21** (`Wardragon`, `Marauder Fury`, `Captain Nate`, `Power of the People` 15, `Shooting Star`, `Ursa Polaris`, `Modified Boxwing/Battleship/Ladybug/Hauler VI`, `Waverider`, `Rais Iris XVIII`, `MasterOfGrey`, …) |
| parole | **752 EN → 806 IT** (1,072) |
| tab / virgolette | **4** (1086, 1119, 2075, 2081) / **54** |
| segnaposto | **0** |
| invariante | **di FILE**: 49/49, prima 186, ultima 2263 |
| `sha256[:16]` | **`84c91bb0dfa29bc4`** |

## Note di resa

- **I nomi delle apparecchiature restano inglesi** dove il corpus li copia da sempre: `"Biroo" Atomic Thruster`, `"Benga" Atomic
  Steering`, `"Basrem" Atomic Thruster`, `"Biroo" Reverse Thruster`, `"Bondir" Atomic Steering`, `"Bufaer" Atomic Thruster` (21 e 19
  occorrenze identiche nei lotti precedenti). I `VALUE` `Marauder Furies` e `Ursa Polaris` sono copiati.
- **`Power of the People`**: 15 battute, citazioni da film, tradotte come **frasi dette**, non come didascalie: «Ridi, ridi, palla di
  pelo», «Sono un ghiacciolo di carne», «Nei panini si trova sicurezza», «Consiglio l'astice».
- **`Reviewers`, `Waverider`, `Shooting Star`, `Wardragon`, `Ladybug`, `Hauler`, `Southbound Shipyards`, `Delta V`**: invariati.
- **`Command Centers`** → «Centri di Comando»; **`spinal mount slot`** → «slot di montaggio spinale»; **`boxwing`** → «boxwing».

## Deviazione dichiarata

Questo lotto è documentato con **un** file (`STATO.md`) invece dei tre (STATO/REPORT/review) e verifica con il **gate generico**
`batch_lot.py` invece di due script su misura: è la modalità **batch** richiesta dalla direttiva operativa («non moltiplicare i report,
non costruire script inutili»). I controlli restano equivalenti: tipi, tab, virgolette e segnaposto **per unità**, gate sul rapporto,
riga grezza, campi del DB, copertura del file, `mtime` di `state.db`.
