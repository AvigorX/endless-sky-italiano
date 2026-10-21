# REPORT — L65 · `data/human/culture conversations.txt` (righe 819–920)

**Esito: CHIUSO.** 43/43 unità, `check.py` `FAIL totale: 0`, `verify.py` exit 0.

## 1. Che cosa contiene il lotto

| Contesto | Unità | Scena |
|---|---|---|
| `Raider returning to Mordente-Bridi` | 1–3 | Un Bastion pirata che rientra ammaccato, i tecnici al lavoro, il bottino scaricato |
| `Militia returning to Solace` | 4–6 | L'inaugurazione del nuovo spazioporto Delta V e l'Argosy che sfiora le altre navi |
| `Republic 300 Year Anniversary` | 7–21 | Il trecentesimo anniversario: i titoli, la storia della Repubblica, le quattro varianti (guerra in corso, guerra finita, Zenith bombardata, Sestor battuti) |
| `Exotic Life: Buccaneer Bay` | 22–43 | Il ristorante del «Pesce Piatto»: il cameriere, il menù truffa, il pasto immangiabile |

## 2. Le scelte di traduzione che contano

**Il servizio giornalistico** (7–17) alterna cronaca e commento: «You can't help but feel that much of the
cheerfulness about this date has more to do with the national holiday than with a deep-rooted
appreciation…» → la frase resta un giudizio del narratore, non una notizia, e la traduzione non la
presenta come tale.

**Le quattro varianti** dell'anniversario dipendono dalle etichette (`war ongoing`, `war over`,
`zenith bombed`, `sestor beaten at farpoint`): ognuna cambia il paragrafo 11–17. Le etichette restano
identiche perché il gioco le usa come selettori.

**`Dish Fish`** → «Pesce Piatto». Il cameriere lo ripete con l'ossessione di uno slogan commerciale
(«Piatto. Pesce.»), e la traduzione mantiene la ripetizione spezzata.

**La lista dei piatti** (32): «Nine-Eye Pie» → «Torta Nove Occhi», «Hand-Mashed Helmet» → «Elmo Pestato a
Mano», «Hydrozoan Lasanga» → «Lasagna Idrozoica», «Captain's Catch» → «Pescato del Capitano». Sono nomi
inventati e grotteschi: la traduzione resta grottesca, non li normalizza.

**Il menù scientifico** (35–38) è una parodia di scheda divulgativa: «filter feeders, deposit feeders, and
grazers» → «filtratori, detritivori e brucatori». I termini tecnici sono corretti in italiano e la parodia
funziona proprio perché sono corretti.

## 3. Difficoltà

- **Un simbolo vietato**: il titolo dell'anniversario avrebbe voluto `300°`; il controllo `caratteri non
  latini` rifiuta `°` (0xB0) e la resa è «trecentesimo anniversario».
- **Due token diversi**: `<origin>` e `<ship>`; la parità è verificata per simbolo, non solo sul totale.
- **1 gruppo di duplicati** (26/30): le due risposte «No, grazie» sono la stessa opzione in due punti
  dell'albero, e la resa è identica per necessità.

## 4. Verifica osservata

```
check.py   → 33 controlli · FAIL totale: 0
verify.py  → 36 controlli · exit 0
             unita 43 · righe 819-920 · 251 prima / 80 dopo · file 374 · max(line) 1122
             tipi 39 MISSION_TEXT + 4 UI_LABEL (10, 12, 14, 16)
             token 2 / 2 (<origin>, <ship>) · tab 45 / 45 · virgolette 22 / 22 · dispari 0
             rapporto 0,91 - 1,58 · duplicati 1 gruppo (26/30)
             parole 1.666 EN -> 1.676 IT
             sha256 translation.json 8cde7537201a63c9…
```

## 5. Stato del progetto dopo L65

| Voce | Prima (L64) | Dopo L65 |
|---|---|---|
| File completi | 30 | 30 |
| Unità in staging | 24.080 | **24.123** |
| `culture conversations.txt` | 251/374 | **294/374 (78,6%)** |

## 6. Prossimo passo

**L66**: righe **921–1053**, **45 unità**, 4 contesti (`Exotic Life: New Greenland` 8,
`Exotic Life: Mainsail` 9, `Struggling Author Gone Missing` 8, `Exotic Life: Bloodsea` 20),
1.239 parole, tab 41, virgolette 52 con **2 dispari** (10, 34), **0 `UI_LABEL`**, 0 token.
Confine: riga 1062 apre `mission:Exotic Life: Delve`; restano 35 unità al file.
