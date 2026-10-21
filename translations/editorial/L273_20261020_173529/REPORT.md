# REPORT — L273 (`data/korath/korath ships.txt`, righe 95–360)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **24 controlli**; `verify.py` esce 0 con **22 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 8 (tutte `DESCRIPTION`) | 8 |
| parole | 458 | **523** (1,14) |
| tab | 4 | 4 · primo carattere |
| virgolette | 0 | 0 |
| apici | 9 (tutti nei nomi) | 15 (nomi + elisioni) |
| segnaposto | 0 | 0 |

Rapporto per unità **1,05 – 1,20**. Sono testi lunghi (fino a 86 parole): il gate stretto su unità così lunghe è più
significativo che su una riga di due parole.

## 2. Il lotto

Quattro navi Korath, otto schede. La struttura è regolare: la **prima** unità di ogni nave racconta l'origine del nome, la
**seconda** (rientrata con tab) descrive il ruolo tattico.

| nave | origine del nome | ruolo |
|---|---|---|
| **Rano'erek** | un politico ed economista civile | raccogliere risorse senza rischiare le navi-mondo |
| **Palavret** | una capitana morta per salvare il carico | razzia; ospita quanti più Korath possibile |
| **Tubfalet** | un ammiraglio ferito che non lasciò il ponte | razziatore moderno |
| **'nra'ret** | un ingegnere delle armi che si uccise per non farsi catturare i segreti | cacciatore da pattuglia |

## 3. Il dettaglio che vale la pena non perdere

Tre informazioni **funzionali** stanno dentro la prosa e sono state conservate:

1. **la Palavret è gonfiata** per ospitare l'equipaggio («inflating its size beyond similarly armed warships») — spiega perché
   è grande e lenta;
2. **la 'nra'ret non è modulare** («non-modular nature… constructed wholesale at the largest Korath facilities») — spiega
   perché serve un cantiere grande;
3. **il suo armamento**: portelli lanciamissili per il fuoco a distanza, **lanciatori di mitraglia** per le operazioni
   prolungate, **due Lance di fuoco** per l'emergenza ravvicinata.

## 4. Nomi con apostrofo

`Rano'erek`, `'olofez`, `'nra'ret`, `Ik'atilajej`, `Korsmanath A'awoj` restano **identici**, compreso l'apostrofo **iniziale**
di `'nra'ret` e `'olofez`. Il `check.py` verifica i nomi **dove l'inglese li nomina** (unità 1, 7, 8), non globalmente: una
verifica «il nome compare nel lotto» sarebbe passata anche se l'avesse perso in una scheda sola.

## 5. Verifica

```
check.py   24 controlli · FAIL totale: 0 · exit 0
verify.py  22 controlli · FAIL: 0 · exit 0
segmento   0 prima (apre il file) · 8 qui · 42 dopo la 360 · copertura 8/50 (16,0%)
```

Un rosso al primo giro: dichiaravo il file `righe 95-1470`; il database dice **2363**. Corretto il numero, non
l'asserzione.

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 8 unità `PENDING`.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Il file resta aperto**: 8/50.
