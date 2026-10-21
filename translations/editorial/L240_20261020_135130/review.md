# review.md — L240 (`data/avgi/avgi jobs.txt`, righe 684–1156)

Registro delle decisioni editoriali del **secondo e ultimo lotto** di `avgi jobs.txt`: venti lavori, otto formule, due
segnaposto nuovi.

## 1. Le otto formule

| inglese | resa | n. |
|---|---|---|
| `Take these <bunks> doctors to <destination> to provide treatment and medical services in exchange for <payment>.` | **Porta questi `<bunks>` medici su `<destination>` per fornire cure e servizi medici in cambio di `<payment>`.** | 3 |
| `Bring <cargo> from <origin> to the <destination> to support the construction of the <destination> in exchange for <payment>.` | **Porta `<cargo>` da `<origin>` a `<destination>` per sostenere la costruzione di `<destination>` in cambio di `<payment>`.** | 6 |
| `Deliver <cargo> to <destination> by <date> in exchange for <payment>. Be on the lookout for pirates looking to steal the nuclear material for nefarious purposes.` | **Consegna `<cargo>` su `<destination>` entro il `<date>` in cambio di `<payment>`. Tieni gli occhi aperti: ci sono pirati che cercano di rubare il materiale nucleare per scopi loschi.** | 3 |
| `Bring <cargo> storage media to <destination> to update <planet>'s local network by <date> in exchange for <payment>.` | **Porta `<cargo>` supporti di memoria su `<destination>` per aggiornare la rete locale di `<planet>` entro il `<date>` in cambio di `<payment>`.** | 2 |
| `These <bunks> Twilight Guardsmen need transportation to <destination>. They are willing to pay you <payment> in exchange.` | **Questi `<bunks>` membri della Twilight Guard hanno bisogno di un trasporto su `<destination>`. Sono disposti a pagarti `<payment>` in cambio.** | 1 |
| `These <bunks> Twilight Guard officers need comfortable transportation to <destination>. …` | **Questi `<bunks>` ufficiali della Twilight Guard hanno bisogno di un trasporto confortevole su `<destination>`. …** | 1 |
| `These <bunks> Twilight Guard flag officers need comfortable transportation to <destination>. …` | **Questi `<bunks>` ufficiali superiori della Twilight Guard hanno bisogno di un trasporto confortevole su `<destination>`. …** | 1 |
| `Take these <bunks> Twilight Guards to <destination> to recover from their rotation on the front lines in exchange for <payment>.` | **Porta queste `<bunks>` Guardie su `<destination>` per riprendersi dal turno di servizio al fronte in cambio di `<payment>`.** | 3 |

## 2. `<origin>` e `<destination>`: due segnaposto, un ordine

Sei unità contengono **entrambi**: `<cargo>` parte da `<origin>` e arriva a `<destination>`. Un confronto sui totali
(`<destination>` 26, `<origin>` 6) non vedrebbe uno scambio; il `verify.py` confronta la **posizione** dei due simboli
dentro ogni unità. È la stessa lezione di L239 (`<planet>` = `<destination>` = 31), applicata a una coppia che significa
cose **opposte**.

## 3. Il `the` dentro un `VALUE`

`Construction materials to the <planet>` e `Bulk materials to the <planet>` sono **nomi di lavoro** con l'articolo inglese
in mezzo. Restano identici: sono dati, e il `the` fa parte della stringa che il gioco mostra. In prosa, invece, l'articolo
si gestisce in italiano:

| inglese | italiano |
|---|---|
| `to the <destination>` | **a `<destination>`** (l'articolo italiano dipende dal nome del pianeta e non si può anteporre) |
| `the construction of the <destination>` | **la costruzione di `<destination>`** |
| `update <planet>'s local network` | **aggiornare la rete locale di `<planet>`** |

## 4. Il possessivo inglese e gli apici

`<planet>'s` è l'unico possessivo del lotto: **2 apici in inglese**, **0 in italiano**. La resa usa «di `<planet>`», che
non richiede né apostrofo né articolo. Chi rifà il conto trova 2 contro 0 e potrebbe pensare a un errore: la differenza è
dichiarata qui e asserita nel `check.py` e nel `verify.py`.

## 5. I gradi dei Twilight Guard

| inglese | nella prosa italiana | nel `VALUE` |
|---|---|---|
| `Twilight Guardsmen` | **membri della Twilight Guard** | `Twilight Guardsmen to <planet>` (invariato) |
| `Twilight Guard officers` | **ufficiali della Twilight Guard** | `Twilight Guard Officers to <planet>` (invariato) |
| `Twilight Guard flag officers` | **ufficiali superiori della Twilight Guard** | `Twilight Guard Flag Officers to <planet>` (invariato) |
| `Twilight Guards` | **Guardie** | `Shore leave on <planet>` (il grado non compare) |

La regola è quella di L238: **il nome della fazione resta, il grado è un nome comune e si traduce**. «membri» invece di
«uomini» perché il testo non dice chi sono, e l'italiano non deve aggiungere un genere che l'inglese non ha.

## 6. Lessico

| inglese | resa | nota |
|---|---|---|
| `treatment and medical services` | **cure e servizi medici** | |
| `support the construction of` | **sostenere la costruzione di** | |
| `Be on the lookout for pirates` | **Tieni gli occhi aperti: ci sono pirati che…** | l'inglese è un imperativo; l'italiano spezza in due frasi per non perdere il ritmo |
| `nefarious purposes` | **scopi loschi** | «malvagi» suonerebbe morale, «loschi» è il registro del contrabbando |
| `storage media` | **supporti di memoria** | coerente con «fogli di memoria» del corpus |
| `their rotation on the front lines` | **il turno di servizio al fronte** | «rotazione» in italiano è un'altra cosa |
| `comfortable transportation` | **un trasporto confortevole** | distingue i tre gradi |
| `in exchange` (in coda) | **in cambio** | |

## 7. Il file, chiuso

Due lotti (L239–L240), **102 unità**, 902 EN → 959 IT. Le decisioni che restano valide per chi riprende: i `VALUE` sono
**dati** e si copiano; le `DESCRIPTION` si traducono con **una resa per stringa inglese**, verificata come famiglia; i
segnaposto si confrontano **per simbolo e per ordine**; `<origin>` non si scambia con `<destination>`; il `the` dentro un
`VALUE` non si tocca.
