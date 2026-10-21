# REPORT — L267 (`data/human/engines.txt`, righe 27–194)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **23 controlli**; `verify.py` esce 0 con **22 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 12 (11 `DESCRIPTION`, 1 `VALUE`) | 12 |
| parole | 438 | **440** (1,00) |
| tab | 3 (141, 159, 177) | 3, primo carattere |
| virgolette | 2 (121) | 2, dritte |
| apici | 1 | 6 |
| segnaposto | 0 | 0 |

Rapporto per unità **0,96 – 1,25**.

## 2. Il lotto

Tre **postbruciatori** (Volcano, Caldera, Ionic) e cinque **propulsori** (X1050, X1700, X2700, X3700, X4700). Le schede
spiegano il **compromesso** del gioco: i postbruciatori bruciano carburante per l'iperspazio e possono lasciare la nave a
secco; i motori ionici consumano poca energia e producono poco calore, ma **occupano più spazio a parità di spinta**.

La scheda ionica compare **tre volte identica** (righe 141, 159, 177, con tab iniziale): una sola resa, e il test verifica
che l'insieme delle tre abbia un solo elemento.

## 3. Le virgolette di «adeguato»

L'unità 5 parla del motore integrato del **Barb**: «non è molto utile su altro che un caccia, e in quel ruolo è appena
**"adeguato"**». Le due virgolette sono **dritte**, come nel sorgente, e la resa le conserva: usarle caporali avrebbe
cambiato il testo che il giocatore vede e fatto fallire il conteggio.

## 4. Terminologia presa dal corpus

Ogni scelta è stata **verificata** in `tooltips.txt` e negli altri file già tradotti, non dedotta:

```
afterburner → postbruciatore (21)      thrust → spinta (55)
thruster    → propulsore (31)          hyperspace fuel → carburante per l'iperspazio (17)
capital ship → nave capitale (6)       freighter → mercantile (68)
batteries   → batterie (34)            hull → scafo (244)
```

Il `check.py` verifica che **`afterburner` non compaia** in nessuna resa italiana delle `DESCRIPTION`: se una scheda avesse
lasciato il termine inglese, il controllo sarebbe rosso.

## 5. Verifica

```
check.py   23 controlli · FAIL totale: 0 · exit 0
verify.py  22 controlli · FAIL: 0 · exit 0
segmento   0 prima (apre il file) · 12 qui · 49 dopo la 194 · copertura 12/61 (19,7%)
```

Un rosso al primo giro, sugli **apici italiani**: ne avevo dichiarati 5 su 4 unità, misurati **6 su 5** (mancava
`l'occasione` nell'unità 5). Corretta la mappa dopo la misura.

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 12 unità `PENDING`.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Il file resta aperto**: 12/61.
