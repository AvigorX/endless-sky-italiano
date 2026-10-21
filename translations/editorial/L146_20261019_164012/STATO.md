# STATO — L146 · `unfettered 0 prologue.txt` (**il file è chiuso: 147/147**)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L146_20261019_164012` |
| Righe / unità | **460–530** / **19** — file al **100%** (**147/147**) |
| Tipi | **17 `MISSION_TEXT`** · **2 `UI_LABEL`** (unità 1 e 8) |
| `VALUE` | **0** — asserzione vuota scritta |
| Token | **4** in 4 unità: `<origin>` (9), `<as before (run)>` (11), `<as before (flee)>` (13), `<leave>` (17) |
| Stati | **19 `PENDING`** — misurato e **asserito** |
| Contesto | **1** — `Jump Drive Trading`, chiuso con questo lotto |
| Testi | **19 distinti** |
| Parole | **656 EN → 586 IT** (0,893); per unità **0,86–1,38**, media **1,02** |
| Tab · virgolette | **17 unità** · **28**, **zero dispari** |
| sha256 | `7aaadc8a4d2d1252…` |
| `check.py` | **31 controlli**, `FAIL totale: 0` |
| `verify.py` | **26 controlli**, exit **0** — **invariante di file** |

## Il cinquantesimo file completo

```
L140 25 + L141 20 + L142 20 + L143 30 + L144 20 + L145 13 + L146 19 = 147
```

La somma **si calcola dai `translation.json`** dei sette lotti, non si scrive a mano; `max(line) = 530` e
`count(*) = 147` si interrogano sul database; zero sovrapposizioni fra i sette intervalli. Se un solo lotto avesse
rivendicato una riga in più o in meno, il `verify.py` sarebbe rosso.

## Due `UI_LABEL` che restano inglesi

| riga | label | trattamento |
|---|---|---|
| 460 | `back to choose` | **identica** al sorgente, in `ID_OK` |
| 482 | `buy tripulse` | **identica** al sorgente, in `ID_OK` |

Non sono asserzioni vuote: `check.py` e `verify.py` le confrontano una per una con il sorgente, e la regola «tutte
tradotte» le **esclude** esplicitamente invece di dimenticarle.

## Quattro token, due con parentesi

`<as before (run)>` e `<as before (flee)>` sono **soggetti di frase** (`<…> riesci a schivare`, `<…> fuggi`): il testo
italiano comincia con il segnaposto e il verbo segue. Le parentesi fanno parte del simbolo, e il confronto è **intero**:
uno `split()` sui caratteri non alfanumerici li spezzerebbe in `<as`, `before`, `(run)>`.

`<leave>` apre una frase seguita dalla maiuscola (`<leave> L'ingegnere…`), `<origin>` sta dentro la frase («possiamo fare
questo scambio solo **qui su `<origin>`**»).

## Verifica

```bash
cd staging/editorial/L146_20261019_164012
python mkparts.py   # 19 unità · 17 MISSION_TEXT + 2 UI_LABEL · 4 token · 28 virgolette, zero dispari · 17 tab
python check.py     # FAIL totale: 0 (31 controlli)
python verify.py    # exit 0 (26 controlli, invariante di file: 147/147)
```

**Non verificato**: nessuna missione giocata; nessuna delle due ramificazioni (schivare, fuggire) è stata vista a
schermo.
