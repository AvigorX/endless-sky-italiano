# REPORT — L176 · `avgi ships.txt` (terzo lotto: Undsyni, Tachytia modificata, Tremoros, Prismaios)

## 1. Contenuto

**Otto `DESCRIPTION` da tradurre** e **dodici unità da copiare** (10 nomi + 2 `VALUE`). Le navi: il mercantile
ausiliario **Undsyni** (robusto, usato dai gruppi rinnegati, con una variante cisterna con `Plasmadyne Scoop`), una
**Tachytia** subluminale trasformata in nave-città, l'intercettore **Tremoros**, la fregata **Prismaios**.

## 2. Scelte

| nodo | IT | unità |
|---|---|---|
| `flimsy bulk freighter` | **fragile mercantile alla rinfusa** | 2 |
| `hold its own against attacks` | **tenere testa agli attacchi** | 2 |
| `payload efficient` · `spindly ships` | **efficiente nel carico utile** · **navi più esili** | 2 |
| `reinforced spine` | **spina dorsale rinforzata** | 4 |
| `ram-augmented fusion drives` | **motori a fusione assistiti da collettore di flusso** | 8 |
| `0.25c` / `0.4c` | **0,25c / 0,4c** (virgola decimale italiana) | 8 |
| `city ship` | **nave-città** | 9 |
| `transatmospheric hypersonic fighter` | **caccia ipersonico transatmosferico** | 12 |
| `multi-role warship` | **nave da guerra multiruolo** | 17 |

## 3. Difficoltà

1. **Metà lotto si copia**: 10 nomi di equipaggiamento, ognuno verificato **uno per uno** contro il sorgente, e contati
   per nome (6 + 2 + 1 + 1). Le 20 virgolette sono tutte lì.
2. **Il refuso `habitatation`** (idx 9): l'italiano scrive «cilindri abitativi» correttamente; un controllo lo pretende.
3. **Le classi**: `Tremoros-class` e `Prismaios-class` sono diventate, dopo il primo giro, «intercettore** classe**
   Tremoros» e «fregata **classe** Prismaios». **Questo è un difetto vero trovato dal controllo**, non un'asserzione
   sbagliata: avevo omesso «classe» in due unità.
4. **Decimali**: `0.25c` e `0.4c` resi con la **virgola** italiana (`0,25c`, `0,4c`).
5. **Errori in corsa (miei, tre)**: (a) tre asserzioni sbagliate — apici «2+1 in idx 2/3» invece di **1+1+1 in 2/3/4**,
   testi distinti 17 invece di **14**, contesti `[2,3,5,10]` invece di **`[3,4,6,7]`**; (b) un `verify.py` **non scritto
   su disco** nonostante l'esito «ok» dello strumento, riscritto e verificato con `ls`; (c) **aritmetica sbagliata**:
   «68 unità dopo la 1399» invece di **58** (102 − 44) — bocciata dal `verify.py`, corretta in `verify.py`,
   `HANDOFF_L176` e `RIPRESA_L176`.
6. **Gate**: 1,06–1,24, media 1,15.

## 4. Numeri osservati

```
unita' 20 · 10 TEXT (nomi) · 8 DESCRIPTION · 2 VALUE · tutte PENDING
token 0 · 4 tab · 20 virgolette (nei TEXT) · 3 apici inglesi (idx 2, 3, 4)
14 testi distinti · 4 contesti (3/4/6/7) · righe 930/1399
parole 463 -> 493 (1.065) · rapporto 1.06 - 1.24, media 1.15
FAIL totale: 0 (27 controlli) · verify exit 0 (25 controlli) · sha256[:16] e2d7853a434cdf00
```

## 5. Stato del progetto (dopo L176)

```
TOTALE staging: 28171 unità · 886879 EN · 843722 IT
avgi ships.txt: 44/102 (43,1%) · 3 lotti
residuo traducibile (formula state.py): 3759
residuo misurato: 4428 unità / 90225 parole su 112 file
endless-sky HEAD b4aa3bac3, 0 modifiche
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (27 controlli), `verify.py` exit **0** (25 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 20 unità `PENDING`.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Terzo lotto del file**: contratto successivo in `HANDOFF_L177_20261019.md`.
