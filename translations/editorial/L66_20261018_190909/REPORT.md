# REPORT — L66 · `data/human/culture conversations.txt` (righe 930–1053)

**Esito: CHIUSO.** 45/45 unità, `check.py` `FAIL totale: 0`, `verify.py` exit 0.

## 1. Che cosa contiene il lotto

| Contesto | Unità | Scena |
|---|---|---|
| `Exotic Life: New Greenland` | 1–8 | Il Mastino Mammut e il suo conduttore nella nebbia ghiacciata |
| `Exotic Life: Mainsail` | 9–17 | Il Cane di Mare, la città-nave, lo skiff trainato dalla bestia |
| `Struggling Author Gone Missing` | 18–25 | Anna Fangvin scomparsa: i manifesti, la Coalizione degli Amanti dei Libri |
| `Exotic Life: Bloodsea` | 26–45 | Il mercato nero, l'uomo malato, la Fioritura, la trattativa sul pesce |

## 2. Le scelte di traduzione che contano

**Le schede di «vita esotica» sono descrizioni da documentario**, non racconti: la bestia viene descritta
per parti (zanne, pelliccia, narici, occhi) e la traduzione non aggiunge movimento dove l'inglese è
statico.

**Il venditore di Mainsail parla come un imbonitore**: «they marry old water-dog stock with dolphin and
otter blood, with a touch of beaver for the tail…» → «uniscono vecchi ceppi di cani d'acqua con sangue di
delfino e di lontra, con un tocco di castoro per la coda…». La lista va tenuta come lista.

**`the Bloom`** → «la Fioritura». È una malattia inventata con un nome floreale: «la Fioritura» conserva
l'ironia del nome inglese, «il Fiore» sarebbe troppo grazioso.

**Il vecchio di Bloodsea** ha una sintassi da venditore di fiera: «Bloody sea and bloody fools.» → «Mare di
sangue e sciocchi di sangue.» L'unità 34 è una delle **due virgolette dispari** del lotto (l'altra è la
10): il discorso resta aperto come nel sorgente.

**I numeri della trattativa** (43–45) sono nel testo e non si arrotondano: 1000 crediti al barile, 2100 per
tre barili venduti, 1400 per due, e 294 crediti persi nella fuga finale.

## 3. Difficoltà

- **Un rapporto fuori banda**: l'unità 41 rendeva 0,48 («(Make a run for it.)» → «(Scappa.)»), sotto il
  minimo 0,55. Riscritta «(Scappo via.)» il minimo del lotto è 0,64. Il gate non è stato toccato.
- **Due virgolette dispari** (10, 34) riprodotte e confrontate come insieme di indici.
- **Nessun token**, nessun `LOGBOOK`, nessun `DIALOG`.

## 4. Verifica osservata

```
check.py   → 33 controlli · FAIL totale: 0
verify.py  → 36 controlli · exit 0
             unita 45 · righe 930-1053 · 294 prima / 35 dopo · file 374 · max(line) 1122
             tipi 45 MISSION_TEXT · NT/DIALOG/LOGBOOK/CONVERSATION/TEXT 0 (assenze dichiarate)
             token 0 / 0 · tab 41 / 41 · virgolette 52 / 52 · dispari (10, 34) riprodotte
             rapporto 0,64 - 1,20 · duplicati 1 gruppo
             parole 1.239 EN -> 1.176 IT
             sha256 translation.json 41a48d5412d5b7c6…
```

## 5. Stato del progetto dopo L66

| Voce | Prima (L65) | Dopo L66 |
|---|---|---|
| File completi | 30 | 30 |
| Unità in staging | 24.123 | **24.168** |
| `culture conversations.txt` | 294/374 | **339/374 (90,6%)** |

## 6. Prossimo passo

**L67**: righe **1062–1122**, **35 unità**, 2 contesti (`Exotic Life: Delve`, `Exotic Life: Ada`),
811 parole, tab 32, virgolette 68, **1 `LOGBOOK`** (unità 1, forma backtick), **2 token** `<ship>`,
0 dispari, 0 duplicati. **Chiude il file** a 374/374 e porta i file completi a **trentuno**.
