# REPORT — L235 (`data/avgi/avgi news.txt`, righe 197–280)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **32 controlli** (`FAIL totale: 0`); `verify.py` esce 0 con **21
controlli** (invariante di segmento: 42 prima, 15 qui, 58 dopo). `state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura
su `state.db`: le 15 unità restano `PENDING`.

## 1. Cosa contiene il lotto

Due notizie Avgi, entrambe **composte** dal motore a partire da blocchi `word`:

**`avgi safety advisory`** (13 unità) — un bollettino di sicurezza in due parti:

| pezzo | unità | forma |
|---|---|---|
| 6 prefissi | 197–202 | `"Cautela. `, `"Avvertenza. `, `"Avviso. `, `"Diligenza. `, `"Allarme. `, `"Vigilanza. ` — virgoletta **aperta** e **uno spazio finale** |
| 7 messaggi | 204–210 | «Segnalato un grande sciame di Aberrant entrato nel Tangled Shroud.», «Convoglio disperso; si sospetta bloccato…», «… perduto…», «Flotta dispersa; … bloccata…», «… perduta…», «Il cordone difensivo di Arche non è impenetrabile. Restate vigili.», «Segnalate ogni avvistamento di Aberrant il prima possibile.» — ognuno chiuso da **punto e virgoletta** |

Il gioco sceglie un prefisso e un messaggio: **6 × 7 = 42 testi**, tutti controllati uno per uno in inglese e in
italiano.

**`avgi missing advisory`** (2 unità) — di questa notizia il database conserva solo il primo e l'ultimo blocco
(la virgoletta aperta e il punto finale); le parole interne non sono inventariate (§5 del `review.md`).

## 2. Misure

```
unità             15           (tutte NEWS)
parole            72 EN -> 68 IT
rapporto          0,69 - 1,30 (media 1,00)   gate 0,55-1,90
contesti          2            (safety advisory 13, missing advisory 2)
tab               0            asserzione negativa scritta
virgolette        14           6 prefissi + 7 messaggi + 1 virgoletta aperta
identiche         2            `"` e `.` — punteggiatura, in ID_OK
segnaposto        0            asserzione negativa scritta
composizioni      42           6 x 7, verificate in EN e in IT
```

## 3. Il meccanismo, letto nel sorgente del gioco

`source/Phrase.cpp`, `Phrase::Get()`:

```cpp
for(const auto &part : sentences[...]) { ... result += element.second ? ... : element.first; }
```

I blocchi si **concatenano senza separatore**. Da qui due conseguenze, entrambe verificate:

1. **lo spazio finale dei prefissi è testo**, non impaginazione: senza, il testo composto direbbe
   `"Cautela.Segnalato un grande sciame…"`;
2. **il punto e la virgoletta dei messaggi sono in coda**, non in testa: aggiungerli al prefisso produrrebbe due
   virgolette di apertura.

Per la seconda notizia lo stesso codice spiega perché i blocchi `" "` esistono: sono spazi espliciti fra le parole
composte (`Caution.` + `" "` + `Convoy` + …), e non sono nell'inventario.

## 4. Copertura del file

```
L233   22 unità   righe  32 -  91
L234   20 unità   righe 115 - 180
L235   15 unità   righe 197 - 280
residuo 58 unità  righe 301 - 507
------------------------------------
22 + 20 + 15 + 58 = 115 = unità del file (min 32, max 507)
```

Copertura **57/115 (49,6%)**. Confine misurato: **riga 301**, `news:avgi student happy`.

## 5. Controlli che hanno morso

Al primo giro due controlli sono diventati rossi, **entrambi per un numero mio sbagliato** e non per la traduzione:

- «`Tangled Shroud` 4 volte»: misurate **5** (i messaggi sono cinque, non quattro) — corretto il controllo;
- «convoglio/flotta»: cercati in minuscolo mentre in due unità aprono la frase con la maiuscola (`Convoglio disperso`,
  `Flotta dispersa`) — il controllo ora confronta in minuscolo e **dichiara** perché.

È la terza volta in tre lotti che il numero scritto a memoria è più sbagliato del dato: la regola resta «misura, poi
scrivi».

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: le 15 unità sono `PENDING`.
- **Nessuna notizia vista nel gioco**: non è verificato che il bollettino componga a schermo i 42 testi, né che lo
  spazio finale dei prefissi sopravviva al rendering.
- **Nessuna revisione umana**.
- **La seconda notizia resterà quasi tutta in inglese**: le parole interne non sono nell'inventario (§5 del
  `review.md`).
- **Il file non è completo**: 57/115 (49,6%).
