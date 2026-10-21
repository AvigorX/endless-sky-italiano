# REPORT — L326 (`data/_deprecated/deprecated outfits.txt`, righe 25–792) — **LOTTO TERMINALE**

**Esito: lotto CHIUSO, file CHIUSO a 47/47.** `check.py` esce 0 con **28 controlli**; `verify.py` esce 0 con **17 controlli**.
`state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`. **Nessun rosso, in nessuno dei due script.**

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 47 (42 `DESCRIPTION` + 3 `VALUE` + 2 `TEXT`) | 47 |
| parole | 1.186 | **1.233** (1,04) |
| contesti | 39 | **39** |
| tab | **3** | **3** |
| virgolette | **8** (4 righe) | **8** |
| segnaposto / alternative | 0 / 0 | **0 / 0** |
| apici | **12** (8 unità) | 16 |

Rapporto **0,86 – 1,28**. Estremi: **0,86** (riga 301, la battuta del `Banisher`) e **1,28** (riga 322, il `Warder`): sono le due unità
**più corte** del lotto, e su una frase sola il rapporto non misura nulla.

## 2. Invariante di FILE

```
FILE   47/47 (100%) · zero unità prima della 25 · zero dopo la 792
RIGHE  47 distinte · prima 25 · ultima 792 · un solo lotto
TIPI   42 DESCRIPTION + 3 VALUE + 2 TEXT
```

`data/_deprecated/deprecated outfits.txt` è il **quarantesimo** file chiuso (**99** su 167).

## 3. Cinque copiati, due statuti diversi

| riga | tipo | stringa | occorrenze **già** in staging |
|---|---|---|---|
| 621 | `VALUE` | `Nanotech Batteries` | **0** |
| 641 | `VALUE` | `Intrusion Countermeasures` | **0** |
| 740 | `VALUE` | `Z-3600 "Beam" Amat Torches` | **0** |
| 722 | `TEXT` | `"Nettle" KKV` | **13** |
| 736 | `TEXT` | `"Orchid" Nuclear Missile` | **8** |

Il test **separa i due casi**: per i `TEXT` cerca la resa nel **corpus** (≥5 lotti), perché **esiste già**; per i `VALUE` verifica
**soltanto** l'identità, perché sono **nomi nuovi** che il corpus non aveva mai reso. Trattarli allo stesso modo avrebbe prodotto un
controllo **cieco** su tre unità su cinque.

## 4. `Z-3600 "Beam" Amat Torches`: un nome con le virgolette dentro

```
context  outfit:Z-3600 "Beam" Amat Torch
english  Z-3600 "Beam" Amat Torches
italian  Z-3600 "Beam" Amat Torches
```

È il caso in cui **il contesto e la stringa contengono entrambi `"`**: in Python va scritto fra virgolette doppie con escape, e va
verificato **in byte** (nessun `0x08`), non solo con `ast.parse` — la lezione di L325.

## 5. Le due coppie gemelle

```
70   This engine is used by Korath fighters.        → Questo motore è usato dai caccia Korath.
82   This engine is used by Korath fighters.        → (identica)
97   This engine is used in the Korath capital ships. → Questo motore è usato nelle navi capitali Korath.
109  This engine is used in the Korath capital ships. → (identica)
```

Quattro equipaggiamenti (due propulsori `Ark'torbal`/`Jak'torbal` e due timoni `Ark'parat`/`Jak'parat`) descritti con **due frasi sole**.
La resa **non varia**: due testi uguali con rese diverse sarebbero un errore, non una scelta. `verify.py` lo verifica **sul DB** e in
italiano.

## 6. Quarantadue schede, cinque mondi

| mondo | righe | che cosa dice il file |
|---|---|---|
| **Korath** | 25–579 | reattori, dissipatori di calore, propulsori, armi: **il calore come problema centrale** («i sistemi di raffreddamento che richiedono sono enormi») |
| **Repubblica** | 192, 198 | due **licenze** (`Cruiser`, `Carrier`): «un privilegio molto raro», «una manciata di persone nel secolo scorso» |
| **Quarg** | 621–695 | batterie, scudi, contromisure: «**sbalorditi dalla pura efficienza**», «molti pensano ancora che sia magia» |
| **Successor** | 708–709 | l'armatura in **metamateriale**, modificabile in porto |
| **Avgi** | 765 | il motore a **antimateria a nucleo di raggi**: 0,2c con i banchi di laser di `Anax`, 0,4c con l'amat, reso **obsoleto in una notte** dal motore iperspaziale |
| **Teciimach** | 775–792 | siluri a impulso elettromagnetico che **evitano gli alleati** |

È un file **deprecato** che contiene però **la storia tecnologica** di cinque fazioni: le licenze della Repubblica, il salto
iperspaziale che uccide il motore a raggi, il passaggio dalle «EMP Torpedoes» ai `Teciimach`.

## 7. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 47 unità `PENDING`; il file è **finito in staging**, non approvato.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **I tre `VALUE` non hanno precedenti nel corpus**: la forma è copiata dal sorgente, non confermata da un uso precedente.
- **`amat`** resta **`amat`** («motore ad antimateria a nucleo di raggi», «fattorie di antimateria»): è un'abbreviazione di `antimatter`
  usata come **nome proprio di tecnologia** (`Amat Torch`), e non si traduce.
