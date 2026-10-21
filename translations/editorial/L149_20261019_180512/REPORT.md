# REPORT — L149 · `coalition jobs.txt` (scambi interspecie, trasferimenti, turisti in partenza)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| coloni Saryd | 1–2 | 455–456 | `Saryds to <planet>`, la descrizione del Programma di Scambio |
| coloni Kimek | 3–6 | 476–498 | due livelli, stessa descrizione |
| coloni Arach | 7–10 | 518–540 | due livelli, `Arachi to <planet>` |
| trasferimenti | 11–17 | 560–612 | il `TEXT` degli operai e tre livelli del Programma di Piena Occupazione |
| turisti in partenza | 18 | 634 | `TEXT`: ringraziamento e paga |

## 2. Scelte

| nodo | IT | nota |
|---|---|---|
| `Saryds to <planet>` · `Kimek to <planet>` · `Arachi to <planet>` | **identici** | `VALUE` |
| `Transfer to <planet>` | **identico** | tre volte |
| `As part of the Interspecies Exchange Program` | **Nell'ambito del Programma di Scambio tra Specie** | **riletta da L148** |
| `As a part of the Full Employment Program` | **Nell'ambito del Programma di Piena Occupazione** | resa nuova |
| `need transportation to <destination>` | **hanno bisogno di essere trasportati a `<destination>`** | |
| `transport fee of <payment>` | **tariffa di trasporto di `<payment>`** | |
| `You drop off the workers on <planet>` | **Scarichi gli operai su `<planet>`** | **senza «the»**, quindi «su» e non «sul» |
| `The tourists thank you for bringing them to <planet>` | **I turisti ti ringraziano per averli portati su `<planet>`** | |

## 3. Difficoltà

1. **Due coppie di conteggi uguali** (10/10 e 8/8): il multiset non distingue uno scambio, l'ordine per unità sì.
2. **Una frase «quasi uguale» a L147**: `on <planet>` contro `on the <planet>`. Il costruttore l'ha rifiutata e la resa
   è nuova — «su» invece di «sul».
3. **Cinque `DESCRIPTION` identiche** (i quattro scambi della prima riga + il Saryd di L148): resa unica, verificata
   con l'uguaglianza alla stringa di L148.
4. **Un controllo fittizio** (`or True`) sostituito con un'asserzione vera sulle chiavi di L147.
5. **Zero tab e zero virgolette** per il terzo lotto consecutivo: asserzioni vuote scritte.
6. **Gate**: minimo **0,88**, massimo **1,18**, media **1,06**.

## 4. Numeri osservati

```
unita' 18/18 · VALUE 8 · DESCRIPTION 8 · TEXT 2 · LOGBOOK 0 · DIALOG 0 · UI_LABEL 0 · tutte PENDING
token 36 su 4 simboli: <planet> 10, <payment> 10, <bunks> 8, <destination> 8 (DUE coppie uguali)
parita per simbolo E ordine per unita · 8 VALUE identici · 8 testi distinti · 10 contesti
1 frase riletta da L148 · 1 frase con variante senza «the» rispetto a L147 (resa nuova)
tab 0 · virgolette 0 · parole EN 246 -> IT 268 (1.089) · rapporto 0.88 - 1.18, media 1.06
righe 455/634 · 46 prima / 133 dopo · confine riga 639 (Tourists Out 1)
FAIL totale: 0 (31 controlli) · verify exit 0 (25 controlli)
sha256[:16] b5f2ed112da6516f
```

## 5. Stato del progetto

```
TOTALE staging: 27710 unità · 873794 EN · 830124 IT
coalition jobs.txt: 64/197 (32,5%) · 3 lotti
file completi: cinquanta · residuo traducibile (formula state.py): 4220
residuo misurato: 4889 unità / 103305 parole su 116 file
avanzamento: 27710/32924 unità (84,2%) · 873794/979975 parole (89,2%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (31 controlli), `verify.py` exit **0** (25 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 18 unità `PENDING`, nessuna missione accettata.
- **Nessuna partita avviata**: i tre livelli dei turisti non sono stati giocati.
- **Nessuna revisione umana**.
- **`coalition jobs.txt` è al 32,5%**: restano **133 unità**.
- **Prossimo lotto**: `HANDOFF_L150_20261019.md` — righe **639–794**, **14 unità**, 234 parole, **6 `VALUE`**,
  **6 `DESCRIPTION`**, **2 `TEXT`**, **8 contesti**, **33 token** su **6 simboli** (arriva `<commodity>`).
