# REPORT — L125 · `ships.txt` (Roost, Sparrow, Star Queen, Wasp) · **file chiuso**

## 1. Contenuto

| blocco | unità | righe | navi |
|---|---|---|---|
| portatrici civili | 1, 7 | 3491–3770 | Roost (Hauler II Type F), Skein (Hauler III Type F) |
| navi da guerra | 2, 10, 18–19 | 3549–4214 | Saber, Splinter, Valkyrie, Vanguard |
| piccole e diffuse | 3–6, 8–9, 20 | 3602–4266 | Scoutship, Shuttle, Sparrow, Wasp, Scrapper |
| carico e miniera | 11–12, 15–16 | 3923–4083 | CT-50 Star Barge, Sunder, Surveillance Drone |
| lusso | 13–14 | 3986–3987 | Star Queen |

## 2. Scelte

| nodo | IT | nota |
|---|---|---|
| `fighter-carrying containers` | **container portacaccia** | |
| `pod` (Type F) | **pod** | nome tecnico, invariato |
| `Nest` · `Roost` · `Skein` | invariati | nomi di nave |
| `caravan era` | **era delle carovane** | |
| `powerhouses of military might` | **potenze militari** | |
| `patent-infringing death traps` | **trappole mortali in violazione di brevetto** | |
| `as useless as a blaster cannon on a shuttlecraft` | **inutile come un cannone blaster su uno shuttle** | detto, tradotto |
| `medium-strength interceptor` | **intercettore di forza media** | |
| `luxury liner` · `mini-bar` | **transatlantico di lusso** · **minibar** | |
| `sonic vibrations` | **vibrazioni soniche** | |
| `fuel cells · nuclear reactors` | **celle a combustibile · reattori nucleari** | |
| `clean fusion reactors` | **reattori a fusione puliti** | |
| `Sol Main Belt` | **Cintura Principale del Sol** | |
| `Core's mineral wealth` | **ricchezza mineraria del Nucleo** | |
| `undercarriage` | **sottoscocca** | |
| `automation technologies` | **tecnologie di automazione** | |
| `withering fusillade of gunfire` | **fucileria sferzante** | |

## 3. Difficoltà

1. **Zero `VALUE` e zero token**: due asserzioni vuote, scritte (`not [...]`, `== {}`). In un file di sole
   descrizioni sono il controllo più facile da dimenticare.
2. **Le virgolette sono nomi di modelli** (`"Nest"`, `"Roost"`, `"Skein"`, `"Type F"`) tranne il detto dell'unità 6:
   si traducono solo le battute, e il conteggio per unità (6/2/6) lo verifica.
3. **La nota sui droni** (unità 17) viene da L123/L124: resa riletta e confrontata, non riscritta.
4. **Un atteso sbagliato**: la lista dei termini chiave includeva «scafo», assente in questo lotto; sostituito con
   «abitacolo» (unità 7 e 11). Corretto l'atteso, non il dato.
5. **Invariante di file**: il `verify.py` legge i tre lotti e dimostra **103/103** righe coperte,
   `sovrapposti = 0`, `max(line) = 4266`.
6. **I nomi di nave neutralizzati prima** della scansione dei residui inglesi: ventinove nomi, altrimenti rossa su
   una traduzione corretta.

## 4. Numeri osservati

```
unita' 20/20 · DESCRIPTION 20 · VALUE 0 · token 0 · tutte PENDING
contesti 15 (10x1, 5x2) · testi distinti 20 (1 nota da L123/L124)
tab 5 unita (6, 9, 12, 14, 17) · virgolette 14 (6+2+6) · quadre 0
parole EN 1180 -> IT 1200 (1.017) · rapporto 0.93 - 1.25, media 1.07
righe 3491/4266 · file 103/103 (100,0%) · 3 lotti · 5083 EN -> 5286 IT
FAIL totale: 0 (28 controlli) · verify exit 0 (29 controlli)
sha256[:16] e2309e1d7fee3d39
```

## 5. Stato del progetto

```
TOTALE staging: 26826 unita · 850962 EN · 808720 IT
ships.txt: 103/103 (100.0%) · 3 lotti · FILE COMPLETO
file completi: quarantacinque · residuo traducibile (formula state.py): 5104
residuo misurato: 5736 unità / 126022 parole su 121 file
avanzamento: 26826/32924 unità (81,5%) · 850962/979975 parole (86,8%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 2 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (28 controlli), `verify.py` exit **0** (29 controlli, invariante di file) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: le 20 unità restano `PENDING`; nessuna nave è stata caricata nel gioco.
- **Nessuna revisione umana**.
- **Il file è chiuso in staging, non nel gioco**: 103 unità tradotte, zero viste.
- **Prossimo file**: `data/incipias/incipias first contact.txt` (161 unità, 4.662 parole, **10 contesti**,
  **122 unità con tab**, 206 virgolette, 7 token) — primo lotto **L126**, righe 22–218, 55 unità, 1.788 parole
  (`HANDOFF_L126_20261019.md`).
