# REPORT — L144 · `unfettered 0 prologue.txt` (la prova della lama e il primo equipaggiamento Slegato)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| l'attesa al portello | 1–3 | 367–374 | l'ingegnere `<hood>`, l'attrezzatura, l'offerta, la scelta |
| la lama | 4–7 | 377–382 | `(No.)`/`(Sì.)`, la lama appena sbarcato, un secondo Slegato che la lancia |
| dal fornitore | 8–13 | 386–404 | «armi da mostrarti», la diffidenza, i tre rifiuti, la lama «non standard» |
| il controllo di sicurezza | 14–20 | 407–420 | la zona nascosta, la lama in faccia, le quattro reazioni, Desneeparu |

## 2. Scelte

| nodo | IT | nota |
|---|---|---|
| `an Unfettered Hai<hood>` | **un Hai Slegato`<hood>`** | token **incollato**, come il suffisso inglese |
| `<learned>I am Desneeparu` | **`<learned>`Sono Desneeparu** | token a inizio frase, maiuscola dopo |
| `outfitter` | **fornitore** | 45 occorrenze in staging contro 2 di «equipaggiatore» |
| `the Unfettered who threw a blade at you` | **lo Slegato che ti ha lanciato la lama** | |
| `your unorthodox tactics` | **le tue tattiche poco ortodosse** | |
| `a tactic is only as good as…` | **una tattica è buona solo se riesci a trovarla ed eseguirla abbastanza in fretta** | |
| `(No.)` · `(Yes.)` | **`(No.)`** · **`(Sì.)`** | 4 · 5 |

## 3. Difficoltà

1. **I primi token del file** in due unità diverse: parità per simbolo **e** per unità, più la posizione.
2. **`<hood>` è un suffisso**, non una parola: va incollato al nome, senza spazio, o il motore stampa «Slegato  »
   con un buco.
3. **`<learned>` apre una frase**: la maiuscola che segue è nel testo italiano («Sono»), non nel token.
4. **Le due virgolette dispari** non ci sono in questa finestra, ma **due rifiuti consecutivi** sì: unità 10 e 11, con
   battute diverse, e nessuna delle due si accorcia.
5. **`(No.)` identico** in `ID_OK` e **`(Yes.)` → «(Sì.)»**, come in L142–L143: la convenzione regge.
6. **Gate**: minimo **0,73**, massimo **1,28**, media **0,96**.

## 4. Numeri osservati

```
unita' 20/20 · MISSION_TEXT 20 · VALUE 0 · LOGBOOK 0 · UI_LABEL 0 · token 2 · tutte PENDING
contesto 1 (aperto): Jump Drive Trading 20 nella finestra · 20 testi distinti
token: <hood> unita 1 (incollato) · <learned> unita 20 (a inizio frase) · parita 1 = 1
tab 19 unita (la prima no) · virgolette 12 (unita 8, 10, 11, 12, 13, 20), nessuna dispari
parole EN 486 -> IT 406 (0.835) · rapporto 0.73 - 1.28, media 0.96
righe 367/420 · 95 prima / 32 dopo · confine riga 423, stessa missione
FAIL totale: 0 (31 controlli) · verify exit 0 (25 controlli)
sha256[:16] 794b9584fd67c6a0
```

## 5. Stato del progetto

```
TOTALE staging: 27614 unità · 871547 EN · 828016 IT
unfettered 0 prologue.txt: 115/147 (78,2%) · 5 lotti · 2698 EN -> 2446 IT
file completi: quarantanove · residuo traducibile (formula state.py): 4316
residuo misurato: 4983 unità / 105552 parole su 117 file
avanzamento: 27614/32924 unità (83,9%) · 871547/979975 parole (88,9%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (31 controlli), `verify.py` exit **0** (25 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 20 unità `PENDING`, nessun equipaggiamento sbloccato nel gioco.
- **Nessuna partita avviata**: la lama non è stata schivata né afferrata.
- **Nessuna revisione umana**.
- **`unfettered 0 prologue.txt` è al 78,2%**: restano **32 unità**, tutte in `Jump Drive Trading`.
- **Prossimo lotto**: `HANDOFF_L145_20261019.md` — righe **423–459**, **13 unità**, 703 parole, **12 `MISSION_TEXT`**,
  **1 `LOGBOOK`**, **3 token** (`<learned>`, `<last>`, `<The engineer>`), **2 virgolette dispari** da lasciare aperte.
