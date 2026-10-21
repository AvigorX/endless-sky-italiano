# L49 — revisione editoriale

`data/avgi/avgi side missions.txt` · righe 524–1117 · 256 unità · chiuso il 2026-10-18.
Questo file registra le **decisioni di traduzione** e i **limiti osservati**, non le lodi.

## 1. Cinque voci Avgi diverse, una sola convenzione

Il file contiene cinque episodi con cinque personaggi: **Gamboge** (costruttore, lamentoso e preciso),
**Hansa** (corriere nostalgico), **Claret** (militare, entusiasta della dottrina), **Aliza** (scienziata
delle armi nucleari, entusiasta e un po' cinica), **Yinmn** (contabile della sicurezza, ironico).

La convenzione di specie (etichetta di modalità + «, domanda?», cfr. L48 §1) è **mantenuta identica in
tutti e cinque**, ma il registro cambia:

| personaggio | etichette ricorrenti | tratto reso |
|---|---|---|
| Gamboge | Curiosità, Divertimento, Chiarimento, Riconoscenza, Gratitudine | burocratico, si lamenta per mestiere |
| Hansa | Sorpresa, Considerazione, Nostalgia, Comprensione, Entusiasmo | malinconico, parla al passato |
| Claret | Divertimento, Sdegno, Incredulità, Disprezzo, Impazienza, Lode, Disperazione, Apprensione, Orgoglio | marziale, interrompe, si accalora |
| Aliza | Curiosità, Entusiasmo, Considerazione, Preoccupazione, Delusione, Gioia | velocissima, salta di argomento |
| Yinmn | Divertimento, Spiegazione, Orgoglio | pacato, umorismo asciutto |

Le etichette **non sono state ridotte a un insieme comune**: dove il sorgente usa `Praise` si legge
«Lode», dove usa `Discomfort` si legge «Disagio». Unificare avrebbe appiattito cinque voci in una.

## 2. Il controllo duplicati ha trovato un errore vero

Le unità **25** e **236** sono entrambe `"No."` in inglese; l'unità **95** è `"Nope."`. La prima stesura
rendeva tutte e tre «No.» e il `check.py` ha segnalato:

```
| duplicati italiano non spiegati dal sorgente | [('\t"No."', 3, [25, 95, 236])] | FAIL |
```

95 è stata corretta in **«Macché.»**. Non è un dettaglio di stile: la domanda a cui risponde è «non sei
mica un Aberrante travestito, vero?», e in italiano «No.» suona come una smentita formale, «Macché.»
come la battuta che il personaggio fa.

## 3. Le armi, senza addolcire

Il testo parla di **test atomici**, megatoni, fasci di particelle e armi a guida nucleare. La traduzione
tiene il registro tecnico e non edulcora:

- `megatons` → **megatoni**; `two-stage device` → **dispositivo a due stadi**; `yield` → **resa**;
  `lithium deuteride` → **deuteruro di litio**; `breeder reactors` → **reattori autofertilizzanti**;
  `fissiles` → **materiali fissili**; `implosion and ablation modeling` → **modellistica di implosione e
  ablazione**.
- `atomics` → **atomiche** (sostantivo comune) e `atomics test` → **test atomico**; la maiuscola resta
  al nome proprio del poligono (**Poligono di Dokimi**).
- `nuclear weapons? Fascinating.` → **«Armi nucleari? Affascinante.»**: la meraviglia del capitano è
  tradotta alla lettera, anche se urta; è il testo a volerla.

## 4. Decisioni puntuali

1. **`Cylinder` → «Cilindro»** con la maiuscola nel nome proprio (*Cilindro Aktina*): è un tipo di
   habitat, ma nel testo funziona come nome dell'opera.
2. **`Akoustiki Excursion Vehicle`** invariato (modello), **`Polari`** invariato (classe di nave),
   **`Navigeo Yards`**, **`Ergastirio`**, **`Dokimi`** invariati (luoghi).
3. **`Infocourier` → «infocorriere»**, e `courier system` → **«sistema dei corrieri»**: il composto
   italiano è trasparente e tiene la radice.
4. **`memory diamond` → «diamante di memoria»** con la spiegazione in scena (catene di carbonio-12 e
   carbonio-13) resa alla lettera.
5. **`Trefoil` e `the Foil`** restano invariati anche qui (cfr. L48 §2): la scena del bar non li nomina,
   ma la coerenza con il lotto precedente è un requisito.
6. **`hyperdrive`, `Twilight`, `Outer Limits`, `Twilight Guard`, `Tangled Shroud`** invariati, come in
   L48 §3, con la stessa motivazione (forma dominante nel corpus).
7. **`the War` → «la Guerra»** con la maiuscola; `the Incursion` → **«l'Incursione»**.
8. **`twelve, eleven, ten, nine...` → «Dodici, undici, dieci, nove...»**: il conto alla rovescia è
   scritto in lettere nel sorgente ed è rimasto in lettere. È il punto in cui il testo costruisce la
   tensione, e cifre lo avrebbero freddato.
9. **Unità 220–222**, la descrizione dell'esplosione, è tradotta **senza abbreviazioni** e con la
   ripetizione voluta («luce. Luce. Nient'altro che luce»): il sorgente insiste, e l'insistenza è
   l'effetto.
10. **`she` per Claret e Aliza, `he` per Gamboge, Hansa, Yinmn**: il genere dei personaggi è quello del
    sorgente, come già deciso in L44 (decisione 149).

## 5. Cosa il lotto **non** dimostra

- Non dimostra che la linea Avgi sia giocabile: i 5 contesti hanno `goto` e nessuno è stato percorso.
- Non dimostra la resa **a schermo** delle etichette di modalità né del conto alla rovescia.
- Il rapporto lunghezze (0,65–1,46) è dentro il gate ma **non è un giudizio di qualità**.
- Il file è completo **in staging**, non nel database: 436 unità `PENDING`, nessuna approvata.
