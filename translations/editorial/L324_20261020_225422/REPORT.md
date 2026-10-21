# REPORT — L324 (`data/incipias/incipias outfits.txt`, righe 40–388) — **LOTTO TERMINALE**

**Esito: lotto CHIUSO, file CHIUSO a 23/23.** `check.py` esce 0 con **23 controlli**; `verify.py` esce 0 con **18 controlli**.
`state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 23 (`DESCRIPTION`) | 23 |
| parole | 853 | **831** (0,974) |
| contesti | 20 | **20** (i contesti non si traducono) |
| tab | **6** | **6** |
| virgolette | **0** | **0** |
| segnaposto / alternative | 0 / 0 | **0 / 0** |
| apici | **9** (5 unità) | 23 |

Rapporto **0,93 – 1,27**: il lotto più «piatto» del ciclo, perché i testi sono **schede tecniche** di lunghezza simile — nessuna battuta
di due parole, nessun rapporto estremo. Gli estremi:

| riga | inglese → italiano | rapporto |
|---|---|---|
| 177 | `The Star Tail needs an extreme amount of energy…` | **0,93** |
| 135 | la nota dei rifornimenti | **1,27** |

## 2. Invariante di FILE

```
FILE   23/23 (100%) · zero unità prima della 40 · zero dopo la 388
RIGHE  23 distinte · prima 40 · ultima 388 · un solo lotto
TIPI   23 DESCRIPTION
```

`data/incipias/incipias outfits.txt` è il **trentottesimo** file chiuso (**97** su 167).

## 3. La quarta nota dei rifornimenti: una famiglia che attraversa i file

```
L318  korath weapons.txt   473
L319  korath weapons.txt   659, 1051, 1222
L320  wanderer outfits.txt 271
L324  incipias outfits.txt 135
```

Sei occorrenze in **tre file** e **quattro lotti**. La resa è **una sola**:

> «Le munizioni per quest'arma possono essere rifornite presso qualsiasi emporio.»

`verify.py` la verifica **nel corpus intero** — cerca la stessa stringa italiana in **almeno 2 altri lotti** — perché una nota di
famiglia non si controlla dentro il file che la contiene: se la resa divergesse, il file da solo sarebbe **coerente con sé stesso** e
sbagliato rispetto al corpus.

## 4. La scala dei colori: quello che il testo dice e quello che non dice

| riga | inglese | resa | che cosa dichiara |
|---|---|---|---|
| 289 | `blue is the weakest color` | «il blu è il colore **più debole**» | **esplicito** |
| 320 | `a color of balance` | «un colore di **equilibrio**» | **esplicito** |
| 351 | `this potent source of energy` | «questa fonte di energia **potente**» | **implicito**: il rosso non è nominato come «il più forte» |
| 334 | `this steering is supposed to be an upgrade from the Blue-Class steering` | «dovrebbe essere un miglioramento rispetto a quello **Blue-Class**» | confronto **fra timoni**, non fra colori |

Il **rosso** è il più forte per **posizione nella serie**, non per una frase. La resa non aggiunge «il più forte», perché sarebbe
un'informazione che il testo non dà — e il test verifica **le tre parole che ci sono**.

## 5. Tre rossi, tutti da assunzioni mie

| # | asserzione scritta | realtà misurata |
|---|---|---|
| 1 | «17 contesti … dodici singoli» | **20 contesti**, **tredici** singoli |
| 2 | `count('balance') == 1` | **2**: «balance» **e** «balances». Il conteggio di **sottostringa** raddoppia |
| 3 | «le tre classi `MH` restano invariate nel testo» | solo **`Blue-Class`** compare in prosa (334): `Green` e `Red` vivono **solo nei contesti** |

Il terzo è il più utile: **i nomi dei contesti non sono testo** e non si traducono; nel corpo della scheda compaiono **solo dove
l'autore li ha messi**. Il controllo corretto è «il nome compare **dove compare nel sorgente**», non «il nome compare». Ed è lo stesso
errore fatto in L305 con i nomi dei pannelli Quarg.

## 6. Che cosa racconta il file

La tecnologia **Incipias** è descritta dal **punto di vista umano**, e il file ha una tesi: **gli Incipias sono più avanzati di noi in
poche cose e meno in molte**.

| riga | il fatto |
|---|---|
| 40 | il `Plasma Discharger` nasce **come strumento minerario**, prima del volo intrasistemico: «più avanzato della loro tecnologia generale, eppure non paragonabile all'efficienza delle armi umane» |
| 85 | lo `Stagnation Beam` è «una delle poche tecnologie che supera tutto ciò che l'umanità abbia fatto»: i prototipi precedono **il sogno** del volo spaziale |
| 87 | il segreto dei raggi è noto **a pochi scienziati controllati dallo stato**: pubblicarlo sarebbe disastroso per gli **Hicemus** |
| 177 | `Star Tail`: **una cella, un colpo** |
| 246 | gli scudi **bruciano idrogeno** nel nucleo e diventano **la fonte di energia di tutte le navi** |
| 225 | `Horizon Grappler`: «il **vertice**» della tecnologia Incipias |
| 388 | la licenza `Hicemus Conflict`: la tecnologia «pensata per dare loro un **vantaggio sulle altre fazioni**» |

Le tre note di `Stagnation Beam` (85, 86, 87) sono **una storia in tre tempi**: l'origine mineraria, l'evoluzione in raggi traenti
compatti, il **segreto di stato**. Non sono tre schede: sono **un racconto spezzato**, e la resa tiene i rimandi («questi raggi»,
«questi nuovi modelli»).

## 7. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 23 unità `PENDING`; il file è **finito in staging**, non approvato.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **`Incipias` invariabile** in italiano, anche come aggettivo («cultura Incipias», «navi Incipias»): scelta dichiarata. Il singolare
  `Incipian` del sorgente diventa «Incipias» invece di «Incipiano», per non introdurre una forma che il corpus non usa.
- **Il rosso non è detto «il più forte»**: verificato che il test non lo asserisca.
