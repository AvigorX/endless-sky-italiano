# STATO — L203 · `hai outfits.txt` (terzo lotto)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L203_20261019_210258` |
| Righe / unità | **508–600** / **9** — file al **33/65 (50,8%)** |
| Tipi | {'DESCRIPTION': 9} |
| Tab · virgolette · apici | **1** (unità 8) · **0** · **1 EN / 4 IT** |
| Segnaposto | **0** (asserzione negativa scritta) |
| Contesti | **8** — da `Chameleon Anti-Missile` a `Value Detector` |
| Parole | **442 EN → 472 IT** (rapporto 1,03–1,20, media 1,10) |
| sha256 | `81a25808d92d805f…` |
| Esiti | `check.py` **24** (`FAIL 0`, exit 0) · `verify.py` **17** (`FAIL: 0`, exit 0) |

## Cosa contiene

Difese e contromisure Hai: anti-missili, disturbatori per i Tracker, rigeneratori di scudi, raffreddamento, la chiave
di volta quantistica e uno scanner da preda.

| blocco | unità | righe | contenuto |
|---|---|---|---|
| Chameleon Anti-Missile | 1 | 508 | più gittata, più potenza, ricarica più breve del Bullfrog |
| Cuttlefish Jammer | 2 | 522 | bersaglio illusorio per i Tracker |
| Octopus Jammer | 3 | 534 | più aggressivo, più energia, più vulnerabilità agli ioni |
| Corundum Regenerator | 4 | 549 | geometria e armoniche della matrice dello scudo |
| Diamond Regenerator | 5 | 563 | ricarica avanzata, calore intenso, Williwaw Cooling |
| Williwaw Cooling | 6 | 574 | per le navi che si surriscaldano a intermittenza |
| Quantum Keystone | 7–8 | 585–586 | portafortuna, nausea dell'iperspazio, confezione con certificato |
| Value Detector | 9 | 600 | scanner da saccheggio, doppia funzione |

## Difficoltà

1. **Termini di glossario verificati alla lettera**: «generatori di scudi», «matrice dello scudo» (unità 4 e 5), «disturbatore» per *jammer*, «chiave di volta» per *keystone* (la scelta di L200).
2. **Unità 7–8 sono lo stesso oggetto** in due paragrafi, il secondo indentato: la seconda descrive la confezione, non ripete la prima.
3. **Apici 1 contro 4**: `Tracker's` in inglese, quattro elisioni in italiano (`l'aggancio`, `L'Octopus`, `nell'iperspazio`, `l'origine`).
4. **Nomi di prodotto** (`Cuttlefish Jammer`, `Octopus Jammer`, `Diamond`, `Williwaw Cooling`, `Bullfrog`, `Hai-home`): invariati anche quando il testo li usa come aggettivi.
5. **Errore d'accordo nel sorgente** (unità 5: *the shifts … causes*): la resa traduce il senso senza correggere il gioco, e lo dichiara.

## Verifica

```bash
cd staging/editorial/L203_20261019_210258
python check.py     # FAIL totale: 0 (24 controlli)
python verify.py    # FAIL: 0 · exit 0 (17 controlli)
```

**Non verificato**: nessun equipaggiamento installato nel gioco, nessuna schermata vista, nessuna revisione umana; le 9 unità restano `PENDING`.
