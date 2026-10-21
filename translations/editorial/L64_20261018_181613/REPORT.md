# REPORT — L64 · `data/human/culture conversations.txt` (righe 723–810)

**Esito: CHIUSO.** 42/42 unità, `check.py` `FAIL totale: 0`, `verify.py` exit 0.

## 1. Che cosa contiene il lotto

| Contesto | Unità | Scena |
|---|---|---|
| `Burthen Triathlon` | 1–25 | Il triathlon su un pianeta ad alta gravità: il tendone del ristoro, l'«Antigrav», lo schermo portatile, Abernathy che taglia il traguardo |
| `CCOR Guerrilla Standoff` | 26–42 | Gagarin: i guerriglieri CCOR che installano una statua al posto del simbolo del governo, il comizio, i gendarmi che non intervengono |

## 2. Le scelte di traduzione che contano

**L'alta gravità è un personaggio.** «Each step takes significantly more effort than you're used to»,
le sedie «built sturdily to allow offworlders to pull themselves up», il consiglio di non far cadere il
bicchiere «unless you want a munted foot for a few weeks» → «a meno che tu non voglia un piede maciullato
per qualche settimana». La fatica fisica resta nel testo, non viene spiegata.

**L'«Antigrav»** è un nome commerciale: resta fra virgolette e invariato, con la sua pubblicità fra
virgolette («alleviare i visitatori dal richiamo naturale di Burthen»).

**La cronaca sportiva** usa il lessico dell'atletica: «rettilineo finale», «nastro», «a un braccio dal
traguardo», «guaito di gioia e sollievo insieme» per «a yelp of simultaneous joy and relief».

**Il comizio** è retorica politica: anafore («Possiamo… Possiamo… Possiamo…»), enumerazioni ternarie
(«Gagariani e forestieri. Capitani e viaggiatori. Militari e contadini.»), invettiva. La traduzione
mantiene l'anafora e la cadenza, **senza** aggiungere aggettivi che l'inglese non ha.

**I nomi propri restano**: Abernathy, Caldarone, Alastair Korban, Belenos, Gagarin, Novo Minho, Martini,
Burthen, Westland, Prime, Foundry, Valhalla, Hestia, Bourne.

## 3. Difficoltà

- **Un duplicato italiano non voluto** (7/29): l'inglese distingue *Return to my ship* da *Go back to my
  ship*; la prima stesura li aveva fusi. Corretto: 29 → «(Torna indietro alla mia nave.)». Trovato dal
  controllo, non dalla rilettura.
- **Tre virgolette dispari** (35, 36, 37) riprodotte: sono gli incipit del discorso, aperti e non chiusi.
- **Nessun token**, nessun `DIALOG`, nessuna quadra.

## 4. Verifica osservata

```
check.py   → 33 controlli · FAIL totale: 0
verify.py  → 36 controlli · exit 0
             unita 42 · righe 723-810 · 209 prima / 123 dopo · file 374 · max(line) 1122
             tipi 38 MISSION_TEXT + 4 UI_LABEL (15, 18, 22, 24)
             token 0 / 0 · tab 45 / 45 · virgolette 23 / 23 · dispari (35, 36, 37) riprodotte
             rapporto 0,85 - 1,27 · duplicati 0 gruppi
             parole 1.652 EN -> 1.598 IT
             sha256 translation.json 57a238ca0241c4ca…
```

## 5. Stato del progetto dopo L64

| Voce | Prima (L63) | Dopo L64 |
|---|---|---|
| File completi | 30 | 30 |
| Unità in staging | 24.038 | **24.080** |
| `culture conversations.txt` | 209/374 | **251/374 (67,1%)** |

## 6. Prossimo passo

**L65**: righe **819–920**, **43 unità**, 4 contesti (`Raider returning to Mordente-Bridi`,
`Militia returning to Solace`, `Republic 300 Year Anniversary`, `Exotic Life: Buccaneer Bay`),
1.666 parole, tab 45, virgolette 22, **4 `UI_LABEL`** (10, 12, 14, 16), **2 token** (`<origin>`, `<ship>`),
1 gruppo di duplicati (26/30). Confine: riga 1062 apre `mission:Exotic Life: Delve`.
