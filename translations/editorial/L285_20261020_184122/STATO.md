# STATO — L285 (`data/wanderer/wanderer missions.txt`, righe 169–182)

**Stato: CHIUSO — LOTTO TERMINALE.** Il file è **completo: 54/54 (100%)**, **ventiduesimo file interamente tradotto** su 167.

| voce | valore |
|---|---|
| directory | `staging/editorial/L285_20261020_184122/` |
| file | `data/wanderer/wanderer missions.txt` (**54/54 unità · 1.727 parole · righe 16–182**) |
| righe | 169–182 (l'**epilogo**) |
| unità | **9**, tutte `MISSION_TEXT` |
| parole | **234 EN → 230 IT** (0,98) |
| rapporto | **0,65 – 1,09** |
| contesti | **1** — `mission:Wanderers: Mereti: The Plant Epilogue` |
| tab | **8** (unità 2–9; la 1 è l'unica non rientrata) |
| virgolette | **8**, per unità |
| scelte del giocatore | **2** fra parentesi tonde, **punto dentro** |
| alternative | **6**, tutte coppie (`[presenti? vivi?]` con `?`) |
| segnaposto | **3** in 3 famiglie — `<planet>` · `<first>` · `<last>` |
| apici | **2 EN** / **1 IT** |
| identica per necessità | **1** (`"Sitrasanir?"`, `ID_OK`) |
| `check.py` | **23 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **22 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di FILE**: 54 unità · somma lotti **13+14+18+9** · righe distinte · ultima **182** · **0 dopo** |
| `sha256[:16]` | **`f4c76137328e36a2`** |

## Comandi

```bash
python staging/editorial/L285_20261020_184122/check.py     # FAIL totale: 0 (23 controlli)
python staging/editorial/L285_20261020_184122/verify.py    # FAIL: 0 (22 controlli, FILE 54/54)
```

## La scena

Anni dopo, il giocatore torna sul pianeta e vede «un minuscolo puntino blu in fondo a una valle». Il campo è **fiorito**: la
**Strong Wind** è parcheggiata in mezzo ai fiori, «i cui petali brillano di un bellissimo blu intenso». Un drone Mereti gli vola
incontro «con una voce molto più sommessa di quanto ti aspetti» — **la prima volta che un Mereti ringrazia** — e dice:

> «Grazie, `<first> <last>`. Hai `[salvato, riportato in vita]` il **sitrasanir**.»

Il **traduttore non prova nemmeno a rendere la parola**: il testo dice esplicitamente che non somiglia a nulla di Hai né di
Wanderer. È il **nome del fiore**, e resta **invariato** — il test lo verifica tre volte e verifica anche che il traduttore se ne
chiami fuori.

Il drone spiega: «Il suo `[simbolo, aspetto]` era di `[importanza, rilevanza]` per i nostri creatori quando erano
`[presenti? vivi?]`. Lo abbiamo `[abbandonato, ignorato]` per anni, ma i nostri `[genitori, antenati]` ci hanno aiutato a
ricordarlo.»

## Il cerchio che si chiude

`[genitori, antenati]` è **la stessa coppia di L282** (unità 5: `[parents? ancestors?]`), dove il drone si era interrotto su
«È la nostra...». Qui la frase si completa: la pianta **era** ciò che i loro creatori avevano lasciato, e i Mereti l'avevano
**dimenticata**. Il test verifica che la resa sia la stessa coppia di parole, come per la scheda ionica di L267 e la formula
Efreti di L275–L276.

## Le scelte del giocatore

Due battute fra **parentesi tonde**, con il **punto finale dentro**: `(Guarda più da vicino.)` / `(Non ora.)`. Sono **opzioni di
scelta** del motore di missione, non prosa: la forma è verificata (parentesi, punto dentro, ordine) e la prima **non** è
rientrata mentre entrambe hanno lo stesso rientro del resto.

## Limiti dichiarati

Nessuna approvazione (9 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana.
