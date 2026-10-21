# REPORT — L123 · `ships.txt` (dalla Aerie alla Fury)

## 1. Contenuto

| blocco | unità | righe | navi |
|---|---|---|---|
| portatrici e capitali | 1–12, 26, 39 | 78–1549 | Aerie, Bactrian, Carrier, Dreadnought |
| caccia e droni | 13–15, 21–22, 30–31, 37–38, 40–41, 46–47 | 432–1990 | Barb, Boxwing, Combat Drone, Dagger, Dropship, Finch |
| navi da carico | 17, 23–24, 27–28, 32–33 | 562–1647 | Behemoth, Bulk Freighter, Class C, Container Transport |
| Marina | 7–8, 16, 34–35, 42–43, 52 | 268–1990 | Auxiliary, Bastion, Corvette, Cruiser, Enforcer, Frigate |
| civili e pirati | 3–5, 18–20, 25, 29, 36, 44, 48–51, 54 | 140–2044 | Argosy, Arrow, Berserker, Blackbird, Bounder, Bulwark, Clipper, Cutthroat, Falcon, Firebird, Flivver, Freighter, Fury |

## 2. Scelte

| nodo | IT | nota |
|---|---|---|
| `fighter bay` · `drone bay` | **baia di caccia** · **baia per droni** | |
| `carrier` · `light carrier` | **portatrice** · **portatrice leggera** | |
| `warship` · `capital ship` | **nave da guerra** · **nave capitale** | |
| `interceptor-class ships` | **navi intercettori** | |
| `hyperdrive` · `jump` | **iperguida** · **salto** | |
| `turret mount` · `gun port` | **alloggiamento per torretta** · **portello del cannone** | coerente con L113 |
| `shield matrix` | **matrice di scudi** | coerente con `shield cortex` (invariato) |
| `city-ship` | **nave-città** | |
| `Q-ship` | **Q-ship** | termine tecnico, invariato |
| `intermodal containers` | **container intermodali** | |
| `bunks` | **cuccette** | |
| `freight caravan` | **carovana di merci** | |
| `turrets · anti-missile turret` | **torrette** · **torretta antimissile** | |
| `warlords` | **signori della guerra** | coerente con L118 |
| `\"Flying Coffin\"` · `\"bara volante\"` | citazione tradotta | unità 21 |
| `\"governing corporate entities\"` | **"entità aziendali di governo"** | unità 42 |

## 3. Difficoltà

1. **I `VALUE` sono nomi propri al plurale** (`Argosies`, `Auxiliaries`, `Finches`, `Furies`): restano identici e
   il controllo li elenca; il resto del lotto è tradotto.
2. **Un contesto per nave**: 33 contesti su 54 unità, 18 da una sola. La distribuzione è opposta a quella dei file
   di eventi e non va «normalizzata».
3. **La nota sui caccia cinque volte**: un'unica resa, verificata sul gruppo (non solo sul singolo testo).
4. **`startswith` su unità con tab**: l'asserzione «la nota compare 5 volte» falliva perché le unità iniziano con
   `\t`; corretto con `.strip().startswith(...)` — è la trappola 9 del checkpoint, riemersa qui.
5. **Una firma sbagliata**: `sleek and more maneuverable` non combaciava con `a sleeker and more maneuverable
   alternative`; corretta in `sleeker`.
6. **`cargo` è un prestito italiano**: il primo `check.py` è fallito sui residui inglesi per «cargo» in «modulo
   cargo» e «cassa cargo»; la parola è stata tolta dalla lista dei residui (è italiana), non tradotta a forza.
7. **Zero token e zero quadre**: asserzioni scritte.
8. **I nomi di nave restano inglesi**: la scansione dei residui li neutralizza **prima** di cercare parole inglesi.

## 4. Numeri osservati

```
unita' 54/54 · DESCRIPTION 48 · VALUE 6 (4 nomi) · tutte PENDING
contesti 33 (18x1, 11x2, 3x3, 1x5) · testi distinti 48 (nota caccia x5)
tab 14 unita · virgolette 16 (unita 13, 21, 27, 36, 42) · token 0 · quadre 0
parole EN 2364 -> IT 2483 (1.050) · rapporto 0.97 - 1.28, media 1.08
righe 78/2044 · file 54/103 (52,4%) · 0 prima / 49 dopo · confine riga 2102
FAIL totale: 0 (29 controlli) · verify exit 0 (29 controlli)
sha256[:16] dce934d804256232
```

## 5. Stato del progetto

```
TOTALE staging: 26777 unita · 848243 EN · 805917 IT
ships.txt: 54/103 (52.4%) · 1 lotto · 2364 EN -> 2483 IT
file completi: quarantaquattro · residuo traducibile (formula state.py): 5153
residuo misurato: 5785 unità / 128741 parole su 122 file
avanzamento: 26777/32924 unità (81,3%) · 848243/979975 parole (86,6%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (29 controlli), `verify.py` exit **0** (29 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: le 54 unità restano `PENDING`; nessuna nave è stata caricata nel gioco.
- **Nessuna revisione umana**.
- **Il file non è completo**: **49 unità** residue (righe 2102–4266), due lotti previsti; il prossimo è
  `HANDOFF_L124_20261019.md` (29 unità, 1.539 parole, 24 contesti, 3 unità con tab, 14 virgolette, **un solo
  `VALUE`**).
