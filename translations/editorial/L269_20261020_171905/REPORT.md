# REPORT — L269 (`data/human/engines.txt`, righe 342–487)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **25 controlli**; `verify.py` esce 0 con **22 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 17 (tutte `DESCRIPTION`) | 17 |
| parole | 449 | **511** (1,14) |
| tab | 8 | 8 · primo carattere |
| virgolette | 0 | 0 |
| apici | 1 | 11 |
| segnaposto | 0 | 0 |

Rapporto per unità **1,00 – 1,24**. Il totale cresce più della media perché la **nota del plasma** (×8) passa da 26 a 29
parole: in italiano servono gli articoli davanti a «motori ionici» e «motori al plasma».

## 2. Il lotto

Cinque propulsori e quattro sterzate della **Delta V Corporation**, la casa che vende il plasma come «un po' più potente
dello ionico, ma inefficiente e caldo»:

| equipaggiamento | che cosa dice |
|---|---|
| **Chipmunk** thruster | il più piccolo sistema al plasma: caccia leggerissimi e intercettori |
| **Greyhound** thruster | navi piccole e mercantili; cassa con il disegno di un **levriero in corsa** |
| **Impala** thruster | molta forza, navi capitali piccole; possono servire **raffreddamenti extra** |
| **Orca** thruster | assorbe tanta energia che senza un **vero reattore nucleare** è inutilizzabile |
| **Tyrant** thruster | cassa enorme con il **Tyrannosaurus Rex** ghignante; poche navi lo possono montare |
| **Chipmunk** steering | il più piccolo: la confezione mostra un **roditore carico di caffeina** |
| **Greyhound** steering | il prodotto **più venduto** della Delta V |
| **Impala** steering | mercantili e quasi tutte le navi da guerra; **più compatto** dello ionico del Sindacato |
| **Orca** steering | fa girare una nave media **come un caccia**, e serve anche le navi più grandi |

Il tono è quello della **pubblicità**: nomi di animali, disegni sulle casse, una gag ricorrente (il roditore, il levriero,
il tirannosauro). La resa lo conserva invece di appiattirlo.

## 3. Nomi di modello contro nomi comuni

`greyhound` sulla cassa è **il cane** (→ «levriero»), `Tyrannosaurus Rex` è **la figura** (→ invariato) e `rodent` è **il
disegno** (→ «roditore»). Nessuno dei tre è il nome del modello. Il `check.py` verifica le due direzioni:

- i nomi di modello (`Greyhound`, `Impala`, `Orca`, `Tyrant`) compaiono in italiano **dove e solo dove** l'inglese li
  nomina (unità 3, 5, 7, 9, 13, 15, 17 — con `Greyhound` assente dall'unità 3, dove è il cane);
- `levriero`, `Tyrannosaurus Rex` e `roditore` compaiono come nomi comuni, e `Greyhound` **non** compare nell'unità 3.

## 4. La nota del plasma, otto copie

Una sola resa per otto unità. Se una copia divergesse — anche di una parola — il controllo sull'insieme sarebbe rosso con
conteggi di parole identici: è il tipo di errore che solo un'asserzione di unicità vede.

## 5. Verifica

```
check.py   25 controlli · FAIL totale: 0 · exit 0
verify.py  22 controlli · FAIL: 0 · exit 0
segmento   27 prima · 17 qui · 17 dopo la 487 · copertura 44/61 (72,1%)
```

Due rossi al primo giro, entrambi su **asserzioni mie troppo rigide**, non su rese:

1. **apici italiani**: ne avevo dichiarati 10, misurati **11** (l'unità 9 ne ha due: `L'enorme` **e** `l'immagine`);
2. **nomi di modello**: chiedevo `Greyhound` anche nell'unità 3, dove l'inglese parla del **cane** e non del modello.
   Riscritto come implicazione **misurata sull'inglese** (nome presente in inglese ⇒ presente in italiano) più un controllo
   esplicito sui tre nomi comuni.

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 17 unità `PENDING`.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Il file resta aperto**: 44/61; l'ultimo lotto (L270) è **terminale**.
