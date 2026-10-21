# REPORT — L146 · `unfettered 0 prologue.txt` (**cinquantesimo file completo**)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| la porta | 1–6 | 460–473 | `back to choose`, le scorte limitate, il rifiuto, la bacheca dei lavori |
| il Tripulse | 7–9 | 480–485 | la descrizione dell'arma, `buy tripulse`, le condizioni dello scambio |
| l'uscita | 10 | 492 | «L'ingegnere se ne va» |
| schivare | 11–12 | 499–502 | `<as before (run)>`: la lama evitata, poi la disapprovazione |
| fuggire | 13–15 | 508–515 | `<as before (flee)>`: la corsa inutile, «Hai solo mostrato paura» |
| il verdetto | 16–19 | 519–530 | la lezione negata, `<leave>`, la promessa del perdono futuro |

## 2. Scelte

| nodo | IT | nota |
|---|---|---|
| `back to choose` · `buy tripulse` | **identiche** | `UI_LABEL`, in `ID_OK` |
| `<as before (run)> manage to dodge` | **`<as before (run)>` riesci a schivare** | token soggetto, parentesi intere |
| `<as before (flee)> run away` | **`<as before (flee)>` fuggi** | idem |
| `<leave> The engineer…` | **`<leave>` L'ingegnere…** | token + maiuscola |
| `here on <origin>` | **qui su `<origin>`** | nome del mondo |
| `hit and run tactics` | **tattiche mordi e fuggi** | |
| `one gun slot` | **un solo alloggiamento per arma** | |
| `our vault` | **la nostra camera blindata** | |
| `this mistake is not permanent` | **questo errore non è definitivo** | |

## 3. Difficoltà

1. **Le due `UI_LABEL` sono testo non traducibile** e vanno verificate a parte: un controllo unico con le altre unità
   avrebbe dovuto ammetterle identiche, mescolando due regole diverse.
2. **Token con parentesi**: `<as before (run)>` non è tre parole, è **un simbolo**. Confronto intero, e in più la
   posizione a inizio frase.
3. **Nessuna virgoletta dispari**: dopo due lotti con dispari (L145 12 e 13, L138 26/36/37/38) l'assenza è
   **dichiarata** e verificata, non presunta.
4. **Invariante di file**: la somma dei sette lotti si calcola dai `translation.json`; `max(line)` e `count(*)` dal
   database.
5. **Il verdetto di Desneeparu** è duro e va reso senza addolcire: «Hai solo mostrato paura», «Non possiamo accettare
   chi non impara dai propri errori».
6. **Gate**: minimo **0,86**, massimo **1,38**, media **1,02**.

## 4. Numeri osservati

```
unita' 19/19 · MISSION_TEXT 17 · UI_LABEL 2 · VALUE 0 · token 4 · tutte PENDING
contesto 1 (chiuso): Jump Drive Trading · 19 testi distinti
token: <origin> (9) · <as before (run)> (11) · <as before (flee)> (13) · <leave> (17) · parita 1 = 1
tab 17 unita (le 2 UI_LABEL no) · virgolette 28, ZERO dispari
parole EN 656 -> IT 586 (0.893) · rapporto 0.86 - 1.38, media 1.02
righe 460/530 · 128 prima / 0 dopo · max(line) del file = 530
FILE CHIUSO: 25+20+20+30+20+13+19 = 147/147 · 7 lotti · zero sovrapposizioni
FAIL totale: 0 (31 controlli) · verify exit 0 (26 controlli)
sha256[:16] 7aaadc8a4d2d1252
```

## 5. Stato del progetto

```
TOTALE staging: 27646 unità · 872906 EN · 829237 IT
unfettered 0 prologue.txt: 147/147 (100%) · 7 lotti · 4057 EN -> 3667 IT
file completi: CINQUANTA · residuo traducibile (formula state.py): 4284
residuo misurato: 4953 unità / 104193 parole su 116 file
avanzamento: 27646/32924 unità (84,0%) · 872906/979975 parole (89,1%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (31 controlli), `verify.py` exit **0** (26 controlli, invariante di file) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 19 unità `PENDING`, nessun motore scambiato nel gioco.
- **Nessuna partita avviata**: né la ramificazione «schivare» né quella «fuggire» sono state giocate.
- **Nessuna revisione umana**.
- **`data/human/news.txt` è stato scartato** come prossimo bersaglio: **164 delle sue 202 unità sono solo una
  virgoletta** (delimitatori `` `"` ``), e **1.356 righe sorgente con una frase quotata non sono inventariate** (0 nel
  database). Tradurre quel file così com'è significherebbe copiare `"` per 164 volte e chiamarlo lavoro. Il difetto è
  documentato nel checkpoint; il prossimo lotto va su un file con inventario reale.
- **Prossimo lotto**: `HANDOFF_L147_20261019.md` — `data/coalition/coalition jobs.txt`, righe **16–293**, **30 unità**,
  **437 parole**, **13 `VALUE`**, **13 `DESCRIPTION`**, **4 `TEXT`**, **65 occorrenze di token** su 7 simboli.
