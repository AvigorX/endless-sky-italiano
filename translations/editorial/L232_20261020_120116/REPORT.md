# REPORT — L232 (`data/korath/korath outfits.txt`, righe 809–908)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **31 controlli** (`FAIL totale: 0`); `verify.py` esce 0 con
**19 controlli** e l'**invariante di file** che porta `korath outfits.txt` a **92/92**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`: le 10 unità restano `PENDING`.

## 1. Cosa contiene il lotto

Sette schede di equipaggiamento Korath/Efreti, tutte `DESCRIPTION` (nessun nome, nessun dato):

| unità | riga | contesto | contenuto |
|---|---|---|---|
| 1 | 809 | `Nelmeb GP Hybrid Thruster` | i più grandi propulsori a gravitoplasma Efreti, solo su navi civili enormi; i Quarg non ne sono impressionati |
| 2 | 826 | `Arkrof GP Hybrid Steering` | i motori Efreti non usano solo plasma; il più piccolo sistema di sterzata sviluppa molta coppia |
| 3 | 843 | `Farves GP Hybrid Steering` | prodotto dello sforzo teorico Efreti; esempio classico di tecnologia Korath, inefficiente |
| 4 | 861 | `Gaktem GP Hybrid Steering` | la gravità quantistica unita alle forze nucleari |
| 5 | 862 | `Gaktem GP Hybrid Steering` | consumi energetici alti, calore ridotto rispetto ai motori Korath equivalenti |
| 6 | 879 | `Nelmeb GP Hybrid Steering` | la propulsione gravitazionale entra nei motori al plasma a fusione |
| 7 | 880 | `Nelmeb GP Hybrid Steering` | stabilità e massa: i reattori a fusione più grandi li alimentano |
| 8 | 892 | `Thermal Repeater Rifle` | il fucile al plasma surriscaldato, due secoli prima del Thermal Repeater per nave |
| 9 | 907 | `Microbot Defense Station` | la trappola per chi tenta di catturare una nave-mondo: microbot e nutrigel |
| 10 | 908 | `Microbot Defense Station` | le multe per chi possiede queste camere di equilibrio |

## 2. Misure

```
unità             10            (tutte DESCRIPTION, zero VALUE)
parole            454 EN -> 508 IT
rapporto          1,04 - 1,25 (media 1,12)   gate 0,55-1,90, banda comoda 0,70-1,75
contesti          7             (Gaktem, Nelmeb e Microbot ne hanno 2 ciascuno)
tab               4             unità 1, 5, 7, 10; sempre iniziali; IT == EN per unità
virgolette        2             entrambe nell'unità 10 (`"escape,"`)
apici             5 EN / 3 IT   EN (3,1) (5,1) (8,3) · IT (1,1) (3,1) (6,1)
segnaposto        0             asserzione negativa scritta
identiche         0             primo lotto di sola prosa: 0 identiche / 10 tradotte
```

## 3. Copertura del file — invariante di FILE

```
L228  20 unità   righe  16 - 195
L229  15 unità   righe 208 - 318
L230  26 unità   righe 319 - 581
L231  21 unità   righe 596 - 808
L232  10 unità   righe 809 - 908
------------------------------------------
20 + 15 + 26 + 21 + 10 = 92 = 92 righe distinte, sovrapposti 0, min 16, max 908
```

Il `verify.py` legge **tutti** i `translation.json` del workspace, filtra il percorso, somma le unità e
confronta con il database: nessun buco, nessuna sovrapposizione. Verifica inoltre che la riga **908** sia
l'ultima riga di contenuto del sorgente (`raw_lines[908:]` contiene solo righe vuote).

## 4. Controlli che hanno morso

Nessun controllo è diventato rosso: la prima stesura è passata a `check.py` e a `verify.py` al primo colpo.
Le due cose che potevano rompere e che sono state verificate **prima** di scrivere:

- **la virgola dentro le virgolette** (`"escape,"`): spostarla fuori avrebbe lasciato il conteggio a 2 e
  cambiato il testo. È riprodotta così com'è;
- **gli apici**: 5 inglesi contro 3 italiani non sono un errore ma due lingue diverse (contrazione contro
  elisione); il controllo elenca le unità, non solo il totale (decisione 202).

## 5. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: le 10 unità sono `PENDING`, come tutto lo staging (`APPROVED 364`, ferme al
  2026-10-17).
- **Nessun equipaggiamento visto nel gioco**: le schede non sono state caricate in Endless Sky.
- **Nessuna revisione umana**.
- **`L1` e `L2` senza `verify.py`**: lacuna storica dichiarata, non toccata.
