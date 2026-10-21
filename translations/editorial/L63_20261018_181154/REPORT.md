# REPORT — L63 · `data/human/culture conversations.txt` (righe 624–711)

**Esito: CHIUSO.** 37/37 unità, `check.py` `FAIL totale: 0`, `verify.py` exit 0.

## 1. Che cosa contiene il lotto

| Contesto | Unità | Contenuto |
|---|---|---|
| `Sol-Bound Shuttle` | 1–10 | Un capitano che non lascia mai il sistema Sol: niente iperguida, traffico Terra–Marte–Luna, la scelta di restare «al sicuro» |
| `Earth Day Blackout` | 11–37 | La Terra al buio per la Giornata della Terra: candele nel terminale, l'addetto che spiega la tradizione, la viaggiatrice che aspetta la metropolitana, le luci che tornano a mezzanotte |

## 2. Le scelte di traduzione che contano

**Il primo contesto è un ritratto, non un'avventura.** La capitana dice «Call me paranoid» → «Dimmi che
sono paranoica», e la frase è un'offerta di complicità, non una confessione: la traduzione non la
ammorbidisce con «forse sono paranoica».

**`Moon` / `Luna`.** Il testo dice «the Moon» e commenta: «You notice that she uses the archaic term for
Luna. Must be a local expression». In italiano il problema si rovescia: «la Luna» **è** il termine
corrente. La resa conserva la struttura — la parola «Luna» e il commento sul termine arcaico — e il
risultato resta un'intraducibilità dichiarata, non un errore nascosto.

**La spiegazione della tradizione** (18, 21, 29, 31, 32) è lunga e piena di incisi. Il testo alterna frasi
spezzate («Che succede con il blackout?») e periodi lunghi; la traduzione segue la stessa alternanza.
L'unità 18 finisce con «Hai altre domande?» **senza** virgoletta di chiusura, come nell'inglese.

**`blackout`** resta invariato in tutte le occorrenze: è il prestito che userebbero i personaggi, e
«oscuramento totale» suonerebbe burocratico dove l'inglese è colloquiale.

**`offworlders`** → «noi che veniamo da fuori» (26): la donna parla dei viaggiatori come di una categoria
sociale, non di stranieri.

**Un rapporto fuori banda, corretto.** L'unità 27 «Earth Day?» rendeva 2,08 perché l'italiano aggiunge
l'articolo. Resa «Giornata della Terra?» il rapporto è **1,85**, dentro il gate 0,55–1,90: la battuta resta
un'eco, come nell'originale.

## 3. Difficoltà

- **Tre virgolette dispari** (18, 29, 31): sono discorsi diretti non chiusi nel sorgente. Il controllo le
  confronta come **insieme di indici**, non come conteggio: riprodurle è obbligatorio, chiuderle sarebbe un
  errore.
- **Un rapporto fuori gate** corretto riscrivendo la battuta (unità 27), non allargando la banda.
- **Nessun duplicato**, nessun token, nessuna quadra.

## 4. Verifica osservata

```
check.py   → 33 controlli · FAIL totale: 0
verify.py  → 36 controlli · exit 0
             unita 37 · righe 624-711 · 172 prima / 165 dopo · file 374 · max(line) 1122
             tipi 36 MISSION_TEXT + 1 UI_LABEL (30) · DIALOG/LOGBOOK/CONVERSATION/TEXT 0
             token 0 / 0 · tab 35 / 35 · virgolette 51 / 51 · dispari (18, 29, 31) riprodotte
             rapporto 0,75 - 1,85 · duplicati 0 gruppi (controllo negativo)
             parole 1.087 EN -> 1.025 IT
             sha256 translation.json 3535834a2a119c44…
```

## 5. Stato del progetto dopo L63

| Voce | Prima (L62) | Dopo L63 |
|---|---|---|
| File completi | 30 | 30 |
| Unità in staging | 24.001 | **24.038** |
| `culture conversations.txt` | 172/374 | **209/374 (55,9%)** |

## 6. Prossimo passo

**L64**: righe **712–810**, **42 unità**, 2 contesti (`Burthen Triathlon` 25, `CCOR Guerrilla Standoff`
17), 1.652 parole, tab 36, virgolette 23 con **3 dispari** (35, 36, 37), **4 `UI_LABEL`** (15, 18, 22, 24),
0 token. Confine: riga 819 apre `mission:Raider returning to Mordente-Bridi`; restano 123 unità.
