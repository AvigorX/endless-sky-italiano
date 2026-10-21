# REPORT — L70 · `data/successors/successor 2 ghosts myurej.txt`

## 1. Cosa contiene il lotto

**La battaglia** (unità 1–10). Il giocatore scende nell'atmosfera di Maspa-Viir-Kella e gli scanner della
`<ship>` segnalano navi non identificate in una valle sotto le nubi. Due scelte: attaccare con la sorpresa o
negoziare. In entrambi i casi una raffica di vento lo scopre, e Riiria si prepara al decollo. Il ramo
d'arrembaggio finisce male: mentre si prepara a tagliare la porta di carico, una serie di esplosioni interne
distrugge la nave di Riiria **e i regali di nozze** che trasportava. Il diario (unità 8) lo registra in una
riga sola, e le unità 7 e 10 impostano il governo `People's Houses (Hostile)` per il seguito.

**La resa dei conti** (unità 11–20). Allo spazioporto di `<planet>`, in una sala con il solito schermo nero,
Casa Myurej accusa: «Ti avevamo dato un compito semplice». Tre possibili risposte (difendersi, ribellarsi,
scusarsi) e tre repliche della voce, che passa dalla collera al disprezzo e infine — con un'onda di colore —
all'offerta: **rimediare** con una nuova missione, recuperare «ninnoli» dal *gorgo dello Shroud*.

**La trattativa** (unità 21–39). Il giocatore può rifiutare («Con te ho chiuso») o chiedere dettagli; c'è un
intermezzo inquietante in cui il **dispositivo di traduzione** capta un suono che non dovrebbe esserci e la
voce lo zittisce («Non distrarti, capitano»). Il sospetto («qualche nave da guerra drone non mi verrà dietro?»,
ricordando **Casa Aqrabe**) viene liquidato con una battuta. Il lotto si chiude con i due diari alternativi
(accettato / rifiutato) e le due uscite.

## 2. Scelte editoriali

| nodo | scelta | perché |
|---|---|---|
| `government \`People's Houses (Hostile)\`` | **invariato** | nome di governo: è un riferimento di dato, non prosa; tradurlo romperebbe la missione |
| `not met solitude enforcers` | **invariato** | `label` di salto, bersaglio di `goto` |
| `Shroud` | **Shroud** | il toponimo resta in inglese in tutto lo staging (`Tangled Shroud`) |
| `gyre of the Shroud` | «il **gorgo** dello Shroud» | `gyre` è un vortice; «gorgo» tiene l'immagine e non introduce un toponimo nuovo |
| `trinkets` | **ninnoli** | è la parola con cui la Casa sminuisce gli artefatti dei Predecessori, ed è coerente in tre punti (20, 28, 34) |
| `Predecessor artifacts` | **manufatti dei Predecessori** | entrambe le forme sono già in staging |
| `aught so basic` / `thou shouldst leap at this` | «una cosa così elementare» / «dovresti cogliere l'occasione» | registro formale moderno (decisione 228), senza arcaismi italiani |
| `disposable` | **usa e getta** | resa corrente, e la replica della Casa («da coltivare, lucidare») la riprende |
| `Casa Aqrabe` | invariato | nome proprio; il riferimento è all'esperienza di un lotto precedente |
| `Raaqa-Kvelq-Ryuit` | invariato | toponimo |
| `Sconfiggi Riiria e torna` | titolo con verbo | i nomi di missione vivono in una lista: forma già usata in L68–L69 |

## 3. Difficoltà incontrate

1. **Due `MISSION_TEXT` che non sono testo** (unità 7 e 10): `government` con backtick. Se fossero stati
   tradotti, la missione avrebbe perso il governo ostile e il `check.py` «parole inglesi residue» non
   avrebbe detto nulla, perché il valore è un nome proprio. Il `verify.py` asserisce che nel `raw` ci sia
   davvero `government` e il nome esatto.
2. **Tre `LOGBOOK`, tutti forma diretta**, ma con una coppia alternativa (accettato 35 / rifiutato 37): se
   fossero stati resi con la stessa frase, il controllo dei duplicati non avrebbe potuto distinguerli
   dall'inglese (che è diverso). Sono due testi distinti e il checker lo asserisce.
3. **Un controllo scritto male**: la riga «due LOGBOOK alternativi presenti e distinti» passava il valore
   booleano come *dettaglio* e `None` come esito, quindi era rossa con la traduzione giusta. Corretta in
   `check.py` prima di dichiarare il lotto (un controllo che non può dire OK non è un controllo).
4. **Il testo più lungo del file finora** (unità 9, 90 parole): la tentazione è spezzarlo. È rimasto una
   unità sola, con lo stesso ritmo dell'originale (esplosione, seconda, terza, corsa alla plancia).
5. **Il suono che non c'è** (unità 23 e 26): due unità che descrivono la stessa percezione con intensità
   diversa («Qualcosa pulsa nelle tue orecchie» / «Lo senti di nuovo, molto più tenue»). Rese distinte, come
   l'inglese.

## 4. Numeri osservati (output letto)

```
unita' tradotte nell'intervallo   39/39
copertura del lotto               39/39
tab IT 28 / EN 28
virgolette IT 64 / EN 64
token IT 5 / EN 5
rapporto IT/EN 0.82 - 1.41
parole EN 1028 -> IT 953
prima/ultima riga del segmento: 215/307
duplicati inglese: 1 gruppi (2 unita)
FAIL totale: 0                     (38 controlli)
verify.py exit 0                   (48 controlli)
sha256[:16] translation.json      a767223f993886ef
```

## 5. Stato del progetto dopo il lotto

```
TOTALE staging: 24322 unita · 776629 EN · 736025 IT
APPROVED 364 · PENDING 32560 · totale 32924
lotti con translation.json: 74
```

`successor 2 ghosts myurej.txt` è coperto **119/211 unità (56,4%)**: restano **92 unità** dopo la riga 307.

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 2 parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`/`REPORT.md`/`review.md` |
| ESEGUITO | sì | `check.py` e `verify.py` lanciati, output letto per intero |
| **VERIFICATO** | **sì** | `check.py` → `FAIL totale: 0` (38 controlli) **e** `verify.py` → `FAIL: 0`, exit **0** (48 controlli) |
