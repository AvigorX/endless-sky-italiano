# REPORT — L60 · `data/human/culture conversations.txt` (righe 437–495)

**Esito: CHIUSO.** 31/31 unità, `check.py` `FAIL totale: 0`, `verify.py` exit 0.

## 1. Che cosa contiene il lotto

| Contesto | Unità | Scena |
|---|---|---|
| `Tarazed Ship Christening` | 1–29 | Il varo della prima nave di una giovane pilota: bottiglia di champagne, imbarazzo, quattro rami (ignorare, gridare gli auguri, avvicinarsi, consigliare) e il padre che ringrazia |
| `Masquerade Hanging` | 30–31 | Una piazza, la polvere da sparo, un'esecuzione in maschera: il corpo fatto rotolare dalla piattaforma, la pistola alla tempia, il colpo che non arriva |

## 2. Le scelte di traduzione che contano

**Il registro brillante del varo.** «a rather cheesy pilot uniform» → «un'uniforme da pilota piuttosto
pacchiana»; «earns an embarrassed blush» → «fa arrossire la giovane donna per l'imbarazzo». Il tono è
affettuoso e prende in giro la scena senza deriderla.

**La battuta del giocatore** (18) è la più delicata del lotto: «I'm just messing with you, my psychiatrist
doesn't think it's very funny when I do it to him either.» → «Ti sto solo prendendo in giro; anche il mio
psichiatra non la trova divertente quando lo faccio a lui.» La battuta è sgraziata **apposta**, e il
seguito («Oh… that's nice, I guess») la punisce: la traduzione non la migliora.

**Il ramo cattivo** (17, 20–22) ha un'etichetta `get out` e una conseguenza esplicita: «You realize that
you have made this random young lady quite uncomfortable». → «Ti rendi conto di aver messo parecchio a
disagio questa giovane signora piombandole addosso con il tuo parere.» Il narratore giudica il giocatore,
e in italiano il giudizio resta.

**«the mortgage»** (24): «il mutuo». Nel gioco la nave si compra a rate; «mutuo» è il termine che il
testo usa, non «prestito».

**La scena dell'esecuzione** (30–31): «old-fashioned pistol» → «una pistola vecchio stile»; «knocking her
out with his weapon» → «la stende con l'arma stessa» (non «la tramortisce», che aggiungerebbe un tecnicismo
medico). «without incident and without explanation» → «senza incidenti e senza spiegazioni».

## 3. Difficoltà

- **Il controllo `parole inglesi residue` ha colpito «Guardare»**: il filtro rimuove i titoli di nave e di
  fazione (`Guard`, `Captain`, …) prima di cercare parole inglesi, quindi «Guardare» − «Guard» = «are»,
  che è nella lista. La correzione giusta era **riscrivere la traduzione** (`(Dare un'occhiata più da
  vicino.)`), non allargare l'eccezione. Registrata come decisione 205.
- **La finestra di export (429) non è la prima unità (437)**: asserito il valore misurato (decisione 196),
  non l'inizio della finestra.
- **40 virgolette in 31 unità**, il massimo del file finora: parità verificata per unità.

## 4. Verifica osservata

```
check.py   → 33 controlli · FAIL totale: 0
verify.py  → 36 controlli · exit 0
             unita 31 · righe 437-495 · 85 prima / 258 dopo · file 374 · max(line) 1122
             tipi 29 MISSION_TEXT + 2 UI_LABEL (6, 20) · DIALOG/LOGBOOK/CONVERSATION/TEXT 0
             token 0 / 0 · tab 27 / 27 · virgolette 40 / 40 · dispari 0
             rapporto 0,88 - 1,54 · duplicati 0 gruppi (controllo negativo)
             parole 661 EN -> 626 IT
             sha256 translation.json 412787a6b5f31400…
```

## 5. Stato del progetto dopo L60

| Voce | Prima (L59) | Dopo L60 |
|---|---|---|
| File completi | 30 | 30 |
| Unità in staging | 23.914 | **23.945** |
| Lotti con `translation.json` | 63 | **64** |
| `culture conversations.txt` | 85/374 | **116/374 (31,0%)** |

## 6. Prossimo passo

**L61**: righe **511–552**, **26 unità**, 1 contesto (`News Reporter - Paradise`), 394 parole, tab 25,
virgolette 38, **1 token** `<origin>`, **0 `UI_LABEL`**.
