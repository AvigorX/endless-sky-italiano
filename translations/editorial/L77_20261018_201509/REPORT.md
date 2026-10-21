# REPORT — L77 · `data/successors/successor side missions.txt`

## 1. Cosa contiene il lotto

**La richiesta dei ricercatori** (1–16). Allo spazioporto il capitano ritrova **Sieasej**, lo studioso che gli
ha fatto da traduttore al primo contatto con i Successori e l'ha assistito per Casa Sioeora. Con lui c'è un
gruppo di **ricercatori dei Predecessori**: le modifiche per attraversare i wormhole costano troppo e
l'Accademia impiegherebbe anni a fornire una nave, quindi chiedono un passaggio. Tre opzioni: accettare,
rimandare (con `label "has deferred"` che riapre la missione), rifiutare.

**Il viaggio e le domande** (17–37). Sul pianeta i ricercatori si sparpagliano con opuscoli e congegni;
tornano al tramonto, impolverati e in fermento. Sul viaggio di ritorno il capitano può interrogare il capo
gruppo: chi erano i Predecessori, che cosa ha causato il crollo (`Tracotanza, direi`), quanto era grande
l'impero, com'era la tecnologia (metallo vivo coltivato nelle stelle, opere invidiate dai Quarg). Al ritorno,
quasi dimenticano il pagamento.

**Il biologo** (38–63). Un Successore in abito verde, carico di attrezzatura, è rimasto bloccato perché il suo
pilota è stato trattenuto: è **Kaatiora**, biologo, diretto su un pianeta giovane per studiare la **vita
primordiale**. Durante il viaggio interroga il capitano su ogni dettaglio della biologia umana, poi su ogni
specie terrestre nota dai documenti dei Predecessori. Al ritorno tocca al capitano: biologia dei Successori
(respirazione subacquea, specie **ermafrodita**, pelle come **camuffamento**), differenze con i Predecessori
(nessuna di fondo, ma medicina superiore e tecnologia codificata per famiglia), la vita nell'ammasso.

## 2. Scelte editoriali

| nodo | scelta | perché |
|---|---|---|
| `has deferred` | **identica** | `label` di salto, in `NT` |
| `Hubris, methinks` | **Tracotanza, direi** | «hybris» sarebbe un prestito dotto, il tono è colloquiale-filosofico |
| `the flesh of space itself was rent` | **la carne dello spazio stesso fu lacerata** | immagine forte, non spiegata |
| `blinks of shots and drives` | **lampi degli spari e dei motori** | resa concreta di `blinks` |
| `living metal grown in stars` | **metallo vivo coltivato nelle stelle** | coerente con «giardini di metallo stellare» (L74) |
| `High Houses` | **Alte Casate** | forma nuova, coerente con `Casa X` |
| `heirlooms` | **cimeli** | forma fissa da L76 |
| `hermaphroditic` / `xenobiology` | **ermafrodita** / **xenobiologia** | termini tecnici correnti |
| `research leave` | **congedo di ricerca** | non «permesso», che qui suonerebbe burocratico |
| `Katiiora` (unità 61) | **Kaatiora** | refuso del sorgente non replicato |
| `fifteen hundred years` | **millecinquecento anni** | il numero si scrive in lettere nel parlato |
| `(Don't ask them anything.)` / `(Don't ask anything.)` | **«(Non chiedere loro nulla.)»** / **«(Non chiedere nulla.)»** | due inglesi distinti, due rese distinte |

## 3. Difficoltà incontrate

1. **Tre coppie di opzioni identiche** fra le due missioni: resa identica e dichiarata. Ma **22 e 50** sono
   inglesi **diversi** (`them` contro nulla) e il primo giro le aveva rese uguali: il `check.py` è diventato
   rosso su «duplicati italiano non spiegati dal sorgente», e ho riscritto la 22.
2. **Virgolette dispari in 56 e 57**: due unità **aprono** e nessuna chiude; la chiusura è in 58. Il
   `verify.py` verifica l'insieme **e** la direzione.
3. **`<planet stopovers>` contiene uno spazio**: una regex che si ferma al primo spazio spezzerebbe il token;
   la parità è sul token intero (13 = 13, 6 famiglie).
4. **Un numero nel testo**: `fifteen hundred years` reso «millecinquecento» — avevo scritto «milletrecento» e
   l'ho corretto leggendo il sorgente, non il documento.
5. **Un refuso del sorgente** (`Katiiora`): non replicato, dichiarato nel `review.md`.

## 4. Numeri osservati (output letto)

```
unita' tradotte nell'intervallo   63/63
copertura del lotto               63/63
tab IT 53 / EN 53
virgolette IT 68 / EN 68 · dispari (56, 57)
token IT 13 / EN 13 (6 famiglie)
rapporto IT/EN 0.78 - 1.30
parole EN 1909 -> IT 1829
prima/ultima riga del segmento: 17/220
duplicati inglese: 3 gruppi (7/42, 9/43, 28/55)
FAIL totale: 0                     (32 controlli)
verify.py exit 0                   (45 controlli)
sha256[:16] translation.json      5e8d1c0e38c05612
```

## 5. Stato del progetto dopo il lotto

```
TOTALE staging: 24657 unita · 787080 EN · 746021 IT
successor side missions.txt: 63/164 (38,4%) · 1909 EN -> 1829 IT · 1 lotto
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 4 parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`/`REPORT.md`/`review.md` |
| ESEGUITO | sì | entrambi gli script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` → `FAIL totale: 0` (32 controlli) **e** `verify.py` → `FAIL: 0`, exit **0** (45 controlli) |
