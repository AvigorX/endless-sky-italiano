# REVIEW — L70 · `data/successors/successor 2 ghosts myurej.txt`

## 1. Coerenza con L68–L69 (stesso file)

- **Casa Myurej**, **le Casate**, **Successori**, **sfera di dati**, **dispositivo di traduzione**,
  **piazzola**, **stiva**: forme già fissate e riusate.
- **`Casa Aqrabe`** è citata come esperienza passata: nome invariato, come in L45.
- **Voce cerimoniosa** resa con «tu» moderno e sintassi formale (decisione 228), anche nei momenti di
  collera e di mellifluità. Nessun «voi», nessun «codesto».
- **`ninnoli`** è la parola con cui la Casa sminuisce gli artefatti: ritorna tre volte (20, 28, 34) e regge
  il disprezzo del personaggio.

## 2. Nodi traduttivi aperti (dichiarati)

- **`the gyre of the Shroud`** (unità 28): «il gorgo dello Shroud». `Shroud` resta in inglese (come
  `Tangled Shroud` in staging); `gyre` → «gorgo» è una scelta di resa, non un toponimo ufficiale.
- **`solitude enforcers`** (unità 30, label di salto): resta in inglese. Se un lotto futuro traducesse la
  label visibile corrispondente, il `goto` va lasciato com'è e la traduzione va messa **altrove**.
- **`People's Houses (Hostile)`** (unità 7, 10): nome di governo, **non** la resa italiana «Casate del
  Popolo» usata nella prosa. Sono due cose diverse: la prosa è tradotta, il riferimento di dato no.
- **`aught`** (unità 12): reso «una cosa», non con un arcaismo. La voce resta sostenuta ma moderna.

## 3. Il doppio `LOGBOOK` alternativo

Unità 35 (accettato) e 37 (rifiutato) sono due voci di diario **alternative** dello stesso bivio. Devono
restare distinte: il controllo lo asserisce (`by_idx[35] != by_idx[37]`), e il testo rifiutato conserva
l'informazione pratica («Puoi tornare allo spazioporto di Raaqa-Kvelq-Ryuit per accettarla in un secondo
momento»), che nel gioco serve al giocatore.

## 4. Duplicati, virgolette, tab

- **1 gruppo di duplicati**: unità 7 e 10, entrambe `government \`People's Houses (Hostile)\``. Sono lo
  stesso riferimento ripetuto in due punti della missione; la resa identica è obbligatoria (sono in `NT`).
- **64 virgolette** su 39 unità, **0 dispari**: parità per unità verde. Il lotto è quasi tutto dialogo.
- **28 tab su 28 unità** tradotte; 11 unità senza tab (nome, descrizione, tre testi non indentati, due
  `government`, tre `log`, la label). Il costruttore li deriva dal sorgente.
- **0 quadre**, **0 backtick** nel testo tradotto (i backtick delle due `government` sono nel `raw`, non
  nell'`english`).

## 5. Cosa NON è stato fatto

- **Nessuna scrittura su `state.db`**: le 39 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: nessun test a schermo della battaglia, delle esplosioni o delle tre
  diramazioni della scena con la Casa.
- **Nessuna verifica del registro**: la voce della Casa è valutata come testo, non misurata.
- **`solitude enforcers`** resta non tradotta: è una label di salto.

## 6. Rischi residui

- **Il `verify.py` cita 80 unità prima e 92 dopo**: sono i conteggi veri del file oggi (L68+L69 prima,
  Myurej 5–8 dopo). Se un lotto futuro coprisse le righe 215–307, il numero cambierebbe — ma il controllo
  misura il **segmento**, non una copertura cumulativa.
- **Il gruppo di duplicati 7/10** è asserito per indice: se il file cambiasse e il governo fosse impostato
  una sola volta, il lotto diventerebbe rosso. È voluto (cambio di inventario).
- **`gyre` → «gorgo»** è reversibile: se in un lotto futuro emergesse un toponimo ufficiale `Gyre`, la resa
  andrebbe rivista in questo lotto e nei successivi.

## 7. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 2 parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì — entrambi gli script lanciati, output letto per intero |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (38 controlli), `verify.py` exit 0 (48 controlli), sha256 `a767223f993886ef` |
