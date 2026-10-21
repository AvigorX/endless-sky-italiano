# REPORT — L153 · `coalition jobs.txt` (delegazione, vendita, criminali)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| la scheda Arach | 1 | 1360 | `LOGBOOK` sulle Case Arach |
| la delegazione | 2–8 | 1361–1370 | il commiato, i tre Heliarch, il Kimek, l'Arach, il Saryd, il congedo |
| seconda vendita | 9–11 | 1380–1393 | `Sell Jump Drive`, la descrizione, il `DIALOG` della consegna |
| criminali, successo | 12–14 | 1403–1422 | `Contain Criminals`, «on site», lo scontro a fuoco |
| criminali, fallimento | 15–17 | 1427–1445 | stesso lavoro, la fuga |
| criminali, imboscata | 18–20 | 1450–1469 | «on the site», la resa immediata |

## 2. Scelte

| nodo | IT | nota |
|---|---|---|
| `Sell Jump Drive` · `Contain Criminals` | **identici** | `VALUE` |
| `Sell a jump drive to the Heliarchs for <payment>.` | **Vendi un motore di salto agli Heliarch per `<payment>`.** | riletta da L152 |
| `on site` | **sul posto** | due copie |
| `on the site` | **sul luogo** | una copia, resa diversa |
| `to you our weapons and warships we still cannot sell` | **a te le nostre armi e le nostre navi da guerra ancora non possiamo vendere** | inversione Arach |
| `for defense and only for justice, they are` | **per difesa e solo per giustizia, è** | inversione Saryd |
| `a team of Heliarch engineers` | **una squadra di ingegneri Heliarch** | |
| `cut off any exits` | **tagliare ogni via di fuga** | |
| `catches the targets entirely by surprise` | **coglie del tutto di sorpresa i bersagli** | |

## 3. Difficoltà

1. **Due inversioni** (Arach e Saryd) nella stessa unità lunga e in quella dell'Arach: vanno conservate, non «corrette».
2. **`on site` / `on the site`**: due stringhe quasi identiche con **rese diverse**, verificate come diverse.
3. **Tre `DIALOG` dello stesso lavoro**: gli esiti diversi (resa, fuga, sorpresa) devono restare riconoscibili.
4. **7 unità con tab** e **20 virgolette**: contate una per una contro l'inglese.
5. **Errore in corsa**: un controllo cercava «ogni è impegnato», che non esiste — il testo dice «ognuno è impegnato».
   Corretto in `check.py` e `verify.py` dopo averlo letto nell'output.
6. **Gate**: 0,77–1,27, media 1,05.

## 4. Numeri osservati

```
unita' 20/20 · LOGBOOK 1 · MISSION_TEXT 7 · VALUE 4 · DESCRIPTION 4 · DIALOG 4 · tutte PENDING
token 16 su 4 simboli: <payment> 7, <destination> 3, <date> 3, <bunks> 3
7 unita con tab · 20 virgolette, nessuna dispari · 17 testi distinti · 2 contesti
parole 582 -> 601 (1.033) · rapporto 0.77 - 1.27, media 1.05
righe 1360/1469 · 136 prima / 41 dopo · confine riga 1475
FAIL totale: 0 (27 controlli) · verify exit 0 (25 controlli) · sha256[:16] 7b5d3d976e20fb6c
```

## 5. Stato del progetto (dopo L153)

```
TOTALE staging: 27802 unità · 875439 EN · 831788 IT
coalition jobs.txt: 156/197 (79,2%) · 7 lotti
residuo misurato: 4797 unità / 101660 parole su 116 file
formula state.py: 4128 · avanzamento 84,4% unità · 89,3% parole
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (27 controlli), `verify.py` exit **0** (25 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 20 unità `PENDING`.
- **Nessuna partita avviata**.
- **Quarto lotto del batch** (L150–L153): contratto = piano del batch, nessun `HANDOFF_L153` separato.
- **Prossimo**: L154 dalla riga 1475, **41 unità / 725 parole** — il lotto più grande della campagna, che **chiude** il
  file. Se in esecuzione risultasse troppo, si taglia al primo confine che non spezzi una coppia `VALUE`+`DESCRIPTION`.
