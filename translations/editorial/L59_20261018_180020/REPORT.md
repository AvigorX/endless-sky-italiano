# REPORT — L59 · `data/human/culture conversations.txt` (righe 225–423)

**Esito: CHIUSO.** 42/42 unità, `check.py` `FAIL totale: 0`, `verify.py` exit 0.

## 1. Che cosa contiene il lotto

Dieci micro-scene, tutte `MISSION_TEXT`, con due scene lunghe (la cena e l'incendio):

| Contesto | Unità | Scena |
|---|---|---|
| `Curious Waiter` | 1–11 | Un cameriere chiede com'è vedere le stelle; tre risposte, tre registri |
| `Syndicated Security Troops` | 12–13 | I `Tonner` che portano truppe; il camuffamento che si scioglie |
| `Class Trip to Port` | 14–14 | Una gita scolastica davanti alla nave |
| `Old Defense Turrets` | 15–16 | La torretta idraulica e la targa che la dedica |
| `Blind Landing` | 17–23 | Atterraggio nello smog: due esiti (fidarsi dell'autopilota / tornare in orbita) |
| `Forest Fire` | 24–34 | L'incendio delle piantagioni, la donna incinta, l'aiuto con la nave |
| `Local Politics` | 35–36 | Lo spazioporto vuoto e il biglietto per i «signori» |
| `Military Response Test` | 37–39 | La base militare, la donna con il pollice in su, la sirena |
| `Missed Mugging` | 40–41 | La borsetta rubata che non puoi fermare |
| `Sojourn Sunday Sales` | 42–42 | Le vacanze in svendita che restano inaccessibili |

## 2. Le scelte di traduzione che contano

**Il cameriere** (1–11) parla con esitazione e tatto: «Sorry… may I ask… what's it like to see the
stars?». Le tre risposte sono tre caratteri: cinico («La maggior parte dei mondi è uguale a questo, o
peggio»), poetico («Le stelle sono più belle sotto un'atmosfera»), prudente («È un'avventura, ma non per
i deboli di cuore»). La traduzione non le addolcisce né le rende equivalenti.

**«a local version of a katsu don»** → «una versione locale del katsu don». Il piatto resta invariato:
è reale, riconoscibile, e «versione locale» è il modo in cui il testo segnala che non è quello terrestre.

**I `Tonner`** (12) restano fra virgolette come nel sorgente (`` "Tonners" ``), al plurale inglese, perché
è un nomignolo dato dai locali: tradurlo («i Tonner») è giusto, declinarlo («i Tonneri») no.

**Il lessico tecnico dell'incendio** (24–34): «retardants» → **«ritardanti»** (termine tecnico corretto in
italiano, non «ritardatori»); «perimeter of the fire» → «perimetro dell'incendio»; «Air Traffic
Controller» → «controllore del traffico aereo»; «hunkering down» → «ci stiamo barricando».

**«their "overlords"»** (35) → i loro **«signori»**, fra virgolette: l'ironia è nel virgolettato e va
conservata, non spiegata.

**«I have a ship out there. Let me help.»** (28) → «Ho una nave là fuori. Lasciami aiutare.»: due frasi
brevi, nessuna subordinata. La fretta si rende con la sintassi.

**«a younger you could never have justified such expense»** (42) → «un te più giovane non avrebbe mai
potuto giustificare una spesa simile». Il «te» come nome è colloquiale e resta tale.

## 3. Difficoltà

- **Nessun duplicato inglese**: primo lotto della serie. Il controllo è stato riscritto come asserzione
  negativa, altrimenti «zero duplicati» sarebbe indistinguibile da «controllo dimenticato».
- **34 virgolette in 42 unità**: il numero più alto finora in questo file. Sono tutte coppie (dialoghi e
  nomignoli); 0 dispari, e la parità per unità è verde.
- **Rapporto 0,70–1,71**: il massimo (1,71) è un'unità breve con un nome proprio lungo («Tonner»), non un
  caso di espansione.

## 4. Verifica osservata

```
check.py   → 33 controlli · FAIL totale: 0
verify.py  → 35 controlli · exit 0
             unita 42 · righe 225-423 · 43 prima / 289 dopo · file 374 · max(line) 1122
             tipi 42 MISSION_TEXT · NT/DIALOG/LOGBOOK/CONVERSATION/TEXT 0 (assenze dichiarate)
             token 0 / 0 · tab 32 / 32 · virgolette 34 / 34 · dispari 0
             rapporto 0,70 - 1,71 · duplicati 0 gruppi (controllo negativo)
             parole 1.475 EN -> 1.402 IT
             sha256 translation.json 5d42121563e61f8d…
```

## 5. Stato del progetto dopo L59

| Voce | Prima (L58) | Dopo L59 |
|---|---|---|
| File completi | 30 | 30 |
| Unità in staging | 23.872 | **23.914** |
| Lotti con `translation.json` | 62 | **63** |
| `culture conversations.txt` | 43/374 | **85/374 (22,7%)** |

Nessuna scrittura su `state.db`: le 42 unità restano `PENDING`.

## 6. Prossimo passo

**L60**: righe **429–495**, **31 unità**, 2 contesti (`Tarazed Ship Christening` 29 unità, `Masquerade
Hanging` 2), 661 parole, tab 27, virgolette 40, **2 `UI_LABEL`**, 0 token, 0 virgolette dispari. Confine:
riga 511 apre `mission:News Reporter - Paradise`.
