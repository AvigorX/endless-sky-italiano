# REPORT — L299 (`data/coalition/coalition outfits.txt`, righe 356–509)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **24 controlli**; `verify.py` esce 0 con **25 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 14 (tutte `DESCRIPTION`) | 14 |
| parole | 467 | **463** (0,99) |
| tab | **4** | **4** |
| virgolette / segnaposto / alternative | 0 / 0 / 0 | **0 / 0 / 0** |
| apici | 4 | 13 |
| contesti | **10** (2 doppi + 1 triplo + 7 singoli) | invariati |

Rapporto per unità **0,90 – 1,22**. È il **primo lotto** di questo file in cui l'italiano è **più corto** dell'inglese: le schede
sono **istruzioni brevi** e **descrizioni tecniche** già compatte, senza elenchi di aggettivi da sciogliere.

## 2. La terzina `Guardian Turret`

| riga | tab | contenuto |
|---|---|---|
| 495 | — | che cos'è: torrette automatiche Heliarch derivate dal materiale antiabbordaggio **Quarg** |
| **496** | `\t` | l'**emettitore** che dà scudo attorno alla base, e i **cecchini** che non colpiscono più |
| **497** | `\t` | il **difetto**: registrare ogni membro dell'equipaggio per non sparare agli alleati |

Tre stringhe, **un** pannello. Il test verifica che le tre condividano il contesto e che le **due tab** siano sulla seconda e
sulla terza: è il controllo che distingue una terzina da una coppia più una scheda sciolta.

## 3. La frase ripetuta sotto due moduli

Le righe **395** e **415** hanno **lo stesso testo inglese**: l'istruzione sull'installazione nella **sezione armi** invece che in
quella dei **motori**. Compare sotto `Small Reverse Module` e sotto `Large Reverse Module` perché il vincolo è **lo stesso**.

La resa è **identica**, verificata in **entrambe le lingue**. È la terza ripetizione riprodotta nel progetto (`marauders.txt`
831/858 e 884/910) e la prima in un file di equipaggiamenti.

## 4. La seconda persona è un'istruzione, non una scelta di stile

Le unità 4 e 6 dicono «della **tua** nave». Sono le **uniche** due del lotto, e sono **istruzioni di gioco**: dicono al giocatore
dove va montato il pezzo. Il test **elenca** `[4, 6]`; un controllo «niente seconda persona» avrebbe fallito su un testo corretto,
e uno «seconda persona libera» non avrebbe verificato nulla.

## 5. Terminologia: il corpus vince di nuovo

`reverse thruster` → **propulsore di spinta inversa**, la forma usata dal corpus in **74** unità, invece di «invertitore di
spinta», che sarebbe più moderno. Il test **rifiuta** la variante elegante (`'invertitore' not in …`).

## 6. Verifica

```
check.py   24 controlli · FAIL totale: 0 · exit 0
verify.py  25 controlli · FAIL: 0 · exit 0
segmento   30 prima · 14 qui · 5 dopo la 509 · file 44/49 (89,8%)
```

**Primo giro verde**: il contratto aveva previsto la terzina con due tab consecutive, la ripetizione e il confine alla 516.

## 7. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 14 unità `PENDING`; **nessuna revisione umana**.
- **Nessun testo visto nel gioco**: le tre stringhe della terzina sono verificate **nei dati**, non nel pannello.
- **Il file è quasi chiuso**: 44/49; restano **5 unità** (516, 517, 524, 532, 533) per il lotto **terminale**.
