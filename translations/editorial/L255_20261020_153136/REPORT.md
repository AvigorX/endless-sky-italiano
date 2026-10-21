# REPORT — L255 (`data/wanderer/wanderer jobs.txt`, riga 891) — LOTTO TERMINALE

**Esito: lotto CHIUSO, file COMPLETO.** `check.py` esce 0 con **19 controlli**; `verify.py` esce 0 con **19 controlli**
(invariante di **file**: 92/92). `state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

**`data/wanderer/wanderer jobs.txt` è il tredicesimo file chiuso della campagna: 92/92 unità.**

## 1. La unità

| campo | valore |
|---|---|
| riga / contesto | **891** · `mission:Wanderers to Kor Efreti` |
| tipo | `DIALOG` |
| inglese | `When you return, the Wanderers thank you for taking them to the Kor Efreti and hand you <payment> before disembarking.` |
| italiano | «Al ritorno, i Wanderer ti ringraziano per averli portati dai Kor Efreti e ti consegnano `<payment>` prima di scendere.» |
| parole | 20 → **19** (rapporto 0,98) |
| segnaposto | `<payment>` (1) |

## 2. Un lotto piccolo non è un lotto senza controlli

Diciannove controlli per unità, in ciascuno dei due script:

```
tipo DIALOG · contesto di L254 · riga 891 · traduzione (non copia) · <payment> al suo posto
zero tab / virgolette / apici · «Wanderer» e «Kor Efreti» invariati · nessun «Wanderers» né «Unfettered»
rapporto 0,98 nel gate · nessun carattere tipografico · nessuno spazio finale
```

e, sul file:

```
91 unità prima · 0 dopo · 891 ultima riga · 92 righe distinte su 92 · nessun buco · nessun lotto che rivendichi la riga
```

## 3. L'invariante di FILE

```
L252  26 · L253  24 · L254  41 · L255  1  =  92 unità = 92 righe distinte
```

Il `verify.py` non si limita a contare: confronta l'insieme delle righe dei quattro `translation.json` con **quello del
database**. Un buco interno (per esempio una riga saltata da un export) sarebbe rosso anche se il totale tornasse.

## 4. Difetti trovati

**Nessuno**: `check.py` e `verify.py` sono passati al primo giro. Il contratto `HANDOFF_L255` aveva due celle sbagliate
(parole **22** invece di **20**, e `Contesti` senza la forma `da … a …`), entrambe corrette **prima** di aprire il lotto.

## 5. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: l'unità è `PENDING` come tutte le altre.
- **Nessun testo visto nel gioco**.
- **Nessuna revisione umana**.
- **«Completo» significa completo in staging**, non nel gioco.
