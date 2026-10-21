# REPORT — L307 (`data/avgi/avgi weapons.txt`, righe 25–203)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **23 controlli**; `verify.py` esce 0 con **25 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 12 (tutte `DESCRIPTION`) | 12 |
| parole | 497 | **521** (1,05) |
| tab | **6** | **6** |
| virgolette / segnaposto / alternative | 0 / 0 / 0 | **0 / 0 / 0** |
| apici | 1 | 10 |
| contesti | **6** (2 terzine + 2 coppie + 2 singole) | invariati |

Rapporto per unità **1,06 – 1,27**: il lotto è **sempre più lungo** in italiano, perché le schede tecniche inglesi usano
**composti nominali** che in italiano richiedono preposizioni e articoli.

## 2. La nota ripetuta è una **regola di gioco**

Le righe **69** e **108** dicono la stessa cosa sotto due armi:

> «Le munizioni di quest'arma si possono rifornire in qualsiasi **emporio**.»

Se una delle due avesse detto «emporio» e l'altra «negozio», il giocatore avrebbe letto **due regole diverse** per lo stesso
meccanismo. Il test confronta le stringhe **alla lettera** e le confronta con una **costante** (`NOTA`).

## 3. Il refuso del sorgente

| riga | inglese | italiano |
|---|---|---|
| 174 | `the coil **can altered** by swapping…` | «può essere **modificata** sostituendo…» |

L'inglese **non ha il verbo**: è un refuso dell'autore, non una forma arcaica. Riprodurlo avrebbe prodotto una frase italiana
**agrammaticale**; il test verifica che `'altered'` **non** compaia nella resa e che «può essere modificata» **sì**. Stesso
criterio di `Gypusm's` (L286) e `Although is it lightly armed` (L287).

## 4. Il collegamento fra due schede

La riga **203** (`Green Optical Laser`) dice che la torretta **richiede** un `Optical Lasing Generator`, cioè l'oggetto descritto
dalla **173**. Il test verifica che il nome compaia nella resa e che «tre Green Laser» sia citato: se la torretta avesse perso il
riferimento, il giocatore non saprebbe che serve un altro pezzo.

## 5. Verifica

```
check.py   23 controlli · FAIL totale: 0 · exit 0
verify.py  25 controlli · FAIL: 0 · exit 0
segmento   0 prima · 12 qui · 34 dopo la 203 · file 12/46 (26,1%)
```

**Primo giro verde**: il contratto aveva individuato la nota ripetuta, il refuso e il collegamento.

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 12 unità `PENDING`; **nessuna revisione umana**.
- **Nessun testo visto nel gioco**.
- **Il file resta aperto**: 12/46; restano **34 unità**.
