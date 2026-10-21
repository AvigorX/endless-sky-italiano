# REPORT — L292 (`data/avgi/avgi culture conversations.txt`, righe 229–259)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **25 controlli**; `verify.py` esce 0 con **25 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 17 (15 `MISSION_TEXT` + 2 `LOGBOOK`) | 17 |
| parole | 464 | **436** (0,94) |
| tab | 15 | 15 (le `MISSION_TEXT`; **no** i `LOGBOOK`) |
| virgolette | 26 | **26**, per unità |
| apici | 5 | 17 |
| segnaposto / alternative | 0 / 0 | **0 / 0** |

Rapporto per unità **0,80 – 1,27**.

## 2. I `LOGBOOK`: un tipo nuovo

Il progetto incontra per la prima volta il tipo **`LOGBOOK`** (diario di bordo). Due differenze strutturali:

1. **niente tab**: non sono dialoghi né scelte;
2. **prima persona, passato**: l'inglese omette il soggetto (`Watched a fencing match…`), l'italiano lo **esplicita** («**Ho**
   assistito…», «**Ho** visto…»).

Il controllo che vale la pena è quello che li **separa per tipo**: filtrare per contesto li avrebbe confusi con le quindici
`MISSION_TEXT` (stesso `mission:Avgi Culture: Fencing`), e un `Counter(kind)` è l'unico modo per accorgersi che il lotto ne ha
**due** di un tipo che prima non esisteva.

## 3. Il tic delle domande

```
"Invitation. Human, are you perhaps interested in witnessing the ancient Avgi sport of fencing, question?"
→ "Invito. Umano, sei forse interessato ad assistere all'antico sport Avgi della scherma, domanda?"
```

`question?` è una **parola finale**, non un punto interrogativo: gli Avgi **dichiarano** di stare facendo una domanda, come
dichiarano tutto il resto («Invito.», «Rassicurazione.», «Aggiunta.», «Proclama.», «Attesa.»). La resa conserva `domanda?` in
**fondo**, e il test verifica le **due** occorrenze (232 e 258).

## 4. La scena ripetuta, e come è verificata

La 248 e la 251 descrivono **la stessa sala**; la 251 aggiunge **un cartello**. Il test non si accontenta della somiglianza:

```python
at[251]['italian'].startswith(at[248]['italian']) and len(at[251]['italian']) > len(at[248]['italian'])
```

**prefisso esatto**, non «simile». È la stessa regola di L290 (insegna 82/86, protesta 102/106), applicata qui con un prefisso
lungo 376 caratteri.

## 5. Le scelte del giocatore

`(Approach them.)` / `(Ignore them.)` → **`(Avvicinati.)`** / **`(Ignorali.)`**, parentesi tonde e **punto dentro**. Sono le
opzioni del primo bivio del dialogo: se la parentesi o il punto si perdono, la scelta non compare.

## 6. Terminologia

| inglese | resa |
|---|---|
| `vibrantly colored` | **dai colori vivaci** |
| `muted teal` | **verde acqua spento** |
| `bright blue and purple sheen` | **blu brillante con riflessi viola** |
| `gymnasium` | **palestra** |
| `skate park` | **skate park** |
| `packed to the brim` | **stipate fino all'orlo** |
| `perched Avgi` | **Avgi appollaiati** |
| `rowdy and excitable crowd` | **folla chiassosa ed eccitabile** |
| `an upset` | **una sorpresa** |
| `glistening purple` | **viola scintillante** |
| `flurry of wing flapping` | **turbinio di battiti d'ala** |
| `the upstart challenger` | **lo sfidante arrivato dal nulla** |
| `paragons of the blade` | **paradigmi della lama** |
| `the duel… begin` | **che il duello… cominci** |

## 7. Verifica

```
check.py   25 controlli · FAIL totale: 0 · exit 0
verify.py  25 controlli · FAIL: 0 · exit 0
segmento   20 prima · 17 qui · 9 dopo la 259 · 1 contesto · 15 tab · 26 virgolette
```

**Due rossi al primo giro**, entrambi su controlli miei:
1. cercavo `Zomp` con la **maiuscola iniziale** nell'unità del cartello, dove è `ZOMP` tutto maiuscolo → conteggio reso
   **case-insensitive**;
2. cercavo `Razmatazz` nell'unità **sbagliata** (la 257, dove i duellanti sono descritti senza nome): il nome compare nella
   **258**, che è l'annuncio → indice corretto.

## 8. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 17 unità `PENDING`.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Il file resta aperto**: 37/46; restano **9 unità** (righe 260–270), tutte nello stesso contesto: sarà il lotto **terminale**.
