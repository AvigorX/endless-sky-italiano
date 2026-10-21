# REPORT — L314 (`data/drak/drak culture conversations.txt`, righe 26–79)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **22 controlli**; `verify.py` esce 0 con **20 controlli**. Il file è a **16/32
(50,0%)**. `state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 16 (`MISSION_TEXT`) | 16 |
| parole | 550 | **556** (1,011) |
| tab | **13** | **13** |
| virgolette | **2** | **2** |
| segnaposto | **4** | **4** |
| alternative | 0 | **0** |
| apici | **6** | **14** |

Rapporto per unità **0,77 – 1,29**. Il minimo è la riga 79 — `You open them again to find yourself lying down in your bed.` — dove
l'italiano («Li riapri e ti ritrovi sdraiato nel tuo letto.») **perde** le parole inglesi di comodo (`to find yourself`).

## 2. Invariante di segmento (il file non è finito)

```
PRIMA     zero unità prima della 26: il lotto APRE il file
QUI       16 unità, righe distinte 26–79
DOPO      16 unità / 603 parole (la prossima alla 93)
COPERTURA 16/32 (50,0%) — STAMPATA, non asserita
```

## 3. Che cos'è un `Drak Revelations`

Sono **visioni**: il giocatore non viaggia, **sogna**. Ogni blocco comincia con un **arrivo** e finisce con uno **svelamento**:

| blocco | arrivo | svelamento |
|---|---|---|
| `Arachi` | la `<ship>` sale attraverso l'ultimo strato di **nuvole**… e il giocatore si ritrova **fuori dalla nave, sottoterra** | la marea di creature riempie i fori, **tutto si fa buio**, e si è appena **usciti dall'atmosfera** |
| `Hai` | si **scende** dalla `<ship>` e si guarda una **pozzanghera** | si **battono le palpebre**: la pozzanghera è **tornata normale** |
| `Humanity` | la `<ship>` atterra su `<origin>` e il giocatore **si ritira a riposare** | **riapre gli occhi** ed è **sdraiato nel proprio letto** |

Il test verifica **tutti e tre** gli svelamenti: sono la struttura, non un dettaglio.

## 4. La scala delle tre visioni

| | che cosa mostra | scala |
|---|---|---|
| `Arachi` | creature che si nascondono, poi **marciano**, poi si lanciano contro un **gigante** | **individuale** |
| `Hai` | un **arcipelago** in una pozzanghera, il calore che **bolle i mari**, le onde che **tentano di spegnere il sole** | **planetaria** |
| `Humanity` | una **culla** nel buio, un **masso**, **fiamme**, una **battaglia di entità senza forma** | **cosmica** |

La progressione è **del sorgente** e la resa la conserva: si passa dal **singolo** al **mondo** al **cosmo**, e l'ultima è anche
l'unica in cui il giocatore è **passivo** («i tuoi occhi sono costretti a chiudersi»).

## 5. Verifica

```
check.py   22 controlli · FAIL totale: 0 · exit 0
verify.py  20 controlli · FAIL: 0 · exit 0
copertura  16/32 (50,0%) — stampata, non asserita
```

**Un rosso al primo giro**, mio: il controllo della seconda persona cercava **pronomi** (`ti|tu|tuo…`) e nel blocco `Hai`
ne trovava **2** su 5, perché l'italiano la esprime nel **verbo** («Scendi», «Batti le palpebre», «riesci»). Corretto con un elenco
di **forme verbali** e una soglia **per blocco** (≥3), che è anche più informativa della somma.

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 16 unità `PENDING`; il lotto è **in staging**.
- **Nessun testo visto nel gioco**: il **ritorno alla realtà** delle tre visioni è verificato **nei dati**.
- **Il file non è finito**: 16/32; restano **16 unità / 603 parole** (L315, lotto terminale).
