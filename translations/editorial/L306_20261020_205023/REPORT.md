# REPORT — L306 (`data/quarg/quarg outfits.txt`, righe 257–579) — **LOTTO TERMINALE**

**Esito: lotto CHIUSO, file CHIUSO a 31/31.** `check.py` esce 0 con **23 controlli**; `verify.py` esce 0 con **22 controlli**.
`state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 10 (tutte `DESCRIPTION`) | 10 |
| parole | 530 | **514** (0,97) |
| tab | **0** | **0** |
| virgolette / segnaposto / alternative | 0 / 0 / 0 | **0 / 0 / 0** |
| apici | 5 | 10 |
| contesti | **10** (uno per unità) | invariati |

Rapporto per unità **0,88 – 1,19**.

## 2. Invariante di FILE

```
FILE         31/31 (100%) · 31 righe distinte · prima 37 · ultima 579 · zero dopo
SOMMA LOTTI  11 (L304) + 10 (L305) + 10 (L306) = 31
OVERLAP      nessun altro lotto rivendica le righe 257-579
```

`data/quarg/quarg outfits.txt` è il **ventottesimo** file chiuso nel progetto (**87** su 167).

## 3. Che cosa chiude il file: la tecnologia come incomprensibilità

Le ultime dieci schede portano a compimento il tema degli equipaggiamenti Quarg: **nessuno sa come funzionino**.

| riga | oggetto | formula dell'ignoranza |
|---|---|---|
| 257/271 | **hub di riparazione** | «in modi che sembrano **sfidare la realtà**», «in un modo **non facilmente distinguibile** per gli umani» |
| 305/336 | **raggi** (`Skydagger`, `Skylance`) | «un progetto sopravvissuto **più a lungo dell'umanità stessa**» |
| 366 | **antimissile** (`Stratospear`) | le giovani razze «hanno tentato» e hanno fallito |
| 402/449/496 | **gravitazionali** | «piegano lo **spaziotempo**», «in modi **incomprensibili**» |
| 566 | `Slipstream Projector` | «il funzionamento esatto è **un mistero**» |
| 579 | `Phalanx System` | la prudenza dei Quarg «si potrebbe definire **eccessiva**» |

## 4. I nomi: otto rifiuti deliberati

Il test **rifiuta** esplicitamente:

«Pugnale del cielo» · «Lancia delle stelle» · «Falange» · «Proiettore della scia» · «Culverina celeste» · «Ribault astrale»

Sono **nomi propri** di equipaggiamento, e la tentazione di tradurli è forte perché sono **parole inglesi comuni**. Il criterio è
lo stesso dei nomi di nave e dei `VALUE`: **ciò che l'interfaccia mostra come nome resta invariato**.

## 5. Verifica

```
check.py   23 controlli · FAIL totale: 0 · exit 0
verify.py  22 controlli · FAIL: 0 · exit 0
FILE       31/31 (100%) · ventottesimo file completo
```

**Un rosso al primo giro** (controllo mio): chiedevo che **ogni** nome d'arma comparisse **nella propria scheda**, ma solo lo
`Skylance` è nominato in prosa (le altre schede dicono «queste armi», «questa torretta»). Sostituito con: i **dieci contesti**
sono esattamente hub + armi, e l'**unica** arma nominata (`Skylance`, 336) compare **solo** lì.

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 10 unità `PENDING`; il file è **finito in staging**, non approvato.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Il file è completo al 100%** solo in staging.
