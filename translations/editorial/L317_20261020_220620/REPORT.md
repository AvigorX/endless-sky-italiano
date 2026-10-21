# REPORT — L317 (`data/coalition/coalition ships.txt`, righe 1141–2195) — **LOTTO TERMINALE**

**Esito: lotto CHIUSO, file CHIUSO a 27/27.** `check.py` esce 0 con **24 controlli**; `verify.py` esce 0 con **23 controlli**.
`state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 17 (`DESCRIPTION`) | 17 |
| parole | 632 | **645** (1,021) |
| tab | **4** | **4** |
| virgolette | **0** | **0** |
| segnaposto / alternative | 0 / 0 | **0 / 0** |
| apici | **1** | 7 |

Rapporto per unità **0,99 – 1,17**: il lotto è **regolare**, e il minimo (riga 1902, il `Thorn`) è dovuto al **plurale collettivo**
inglese (`they are used`), che in italiano resta al plurale ma con meno parole.

## 2. Invariante di FILE

```
FILE        27/27 (100%) · somma lotti 10 (L316) + 17 (L317) = 27
RIGHE       27 distinte · prima 59 · ultima 2195 · zero dopo
```

`data/coalition/coalition ships.txt` è il **trentatreesimo** file chiuso nel progetto (**92** su 167).

## 3. La misura che il contratto imponeva

Il contratto diceva: **misurare le note dei caccia prima di tradurle**, senza presumere che fossero uguali. Misura eseguita
all'apertura del lotto:

| confronto | esito |
|---|---|
| 1505 vs 1564 | **identiche** |
| 1564 vs 1621 | **identiche** |
| 1504 vs 1505 | **diverse** |

Quindi **una** frase ripetuta in **tre navi diverse** (`Pursuer`, `Rover`, `Stalker`) e **una** nota autonoma del `Pursuer`. Se avessi
presunto «due note diverse per il Pursuer e una per gli altri», avrei reso **due frasi identiche in modo diverso** — un errore
invisibile a un controllo sul totale delle parole.

## 4. Le tre civiltà viste dai loro trasporti

| | che cosa manca | come lo risolvono |
|---|---|---|
| **Heliarch** | la forza: i `Neutralizer` sono «appena abbastanza forti» | **pattugliatori** che tengono occupato il nemico fino ai rinforzi; `Skylance` **rubati** ai Quarg per i tempi di guerra |
| **Kimek** | lo spazio: sono **più del doppio** di Saryd e Arachi insieme | trasporti **continui**; lo `Spire` porta **trecento** persone in cabine **progettate per un Kimek** |
| **Saryd** | il tempo: **diecimila anni** di volo spaziale | navi **scientifiche** diventate **case**; il `Runabout` che richiede **due persone** perché la solitudine da sola non basta |

La riga 1753 è la più **fisica** del file: i soffitti dello `Spire` sono **troppo bassi** per un Saryd e i letti **troppo corti** per
un Arach — le taglie delle tre specie diventano **architettura**. La resa conserva i tre dettagli separati, perché sono tre
**misure** diverse.

## 5. L'unica seconda persona del file

`You cannot carry a fighter unless you have a ship in your fleet with a fighter bay.` è un'**istruzione all'acquirente**, non una
descrizione. Il test la **elenca** invece di allentare il registro:

```
unità con seconda persona = [1505, 1564, 1621]   (le tre note, e solo quelle)
```

Una lista esplicita rende il controllo **falsificabile**: se una quarta unità avesse preso il «tu», il test lo direbbe.

## 6. Verifica

```
check.py   24 controlli · FAIL totale: 0 · exit 0
verify.py  23 controlli · FAIL: 0 · exit 0
FILE       27/27 (100%) · trentatreesimo file completo
```

**Nessun rosso**: primo giro verde. Unica correzione **prima** di eseguire: un controllo conteneva un'espressione senza senso
(`u'' .join([])`), sostituita con la verifica reale (`Coalizione` presente nella 1753, `Coalition` assente).

## 7. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 17 unità `PENDING`; il file è **finito in staging**, non approvato.
- **Nessun testo visto nel gioco**: le **taglie** delle tre specie (soffitti, letti, cuccette) sono verificate **nei dati**.
- **I valori di gioco** (resistenza, velocità, stiva) **non** sono nel testo: le schede sono descrittive.
