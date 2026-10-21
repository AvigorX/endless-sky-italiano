# REPORT — L285 (`data/wanderer/wanderer missions.txt`, righe 169–182) — **LOTTO TERMINALE**

**Esito: lotto CHIUSO, file CHIUSO a 54/54.** `check.py` esce 0 con **23 controlli**; `verify.py` esce 0 con **22 controlli**.
`state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 9 (tutte `MISSION_TEXT`) | 9 |
| parole | 234 | **230** (0,98) |
| tab | 8 | 8 · primo carattere |
| virgolette | 8 | **8**, per unità |
| alternative | 6 | **6**, tutte coppie |
| segnaposto | 3 (3 famiglie) | **3** |
| apici | 2 | 1 |
| identiche per necessità | — | **1** (`"Sitrasanir?"`) |

Rapporto per unità **0,65 – 1,09**.

## 2. Invariante di FILE (non di segmento)

```
FILE         54/54 (100%) · righe distinte 54 · prima 16 · ultima 182 · zero dopo
SOMMA LOTTI  13 (L282) + 14 (L283) + 18 (L284) + 9 (L285) = 54
COPERTURA    nessuna unità del file fuori dallo staging
OVERLAP      nessun altro lotto rivendica le righe 169-182
```

Il `verify.py` riapre **tutti** i `translation.json` dello staging per contare i lotti del file e verificare la somma: non si
fida del proprio numero.

## 3. Le due scelte del giocatore

```
\t(Take a closer look.)   →  \t(Guarda più da vicino.)
\t(Not right now.)        →  \t(Non ora.)
```

Sono **opzioni** del motore di missione fra **parentesi tonde**, con il **punto finale dentro la parentesi**. Il test verifica:
le due unità (2 e 3), la forma `(…)` con punto, l'ordine, e che la prima inviti a guardare. Un refuso sulla parentesi
renderebbe la scelta **invisibile al parser del gioco** — è il difetto più costoso che questa struttura può avere.

## 4. `Sitrasanir?` — l'unica unità identica, dichiarata

L'unità 6 (`"\t\"Sitrasanir?\""`) è **identica** nelle due lingue: è il **nome del fiore**, che il drone pronuncia come domanda e
che il traduttore del gioco **non traduce**. Il test la elenca in `ID_OK` e verifica l'**identità**; le altre otto sono
verificate per **differenza**. In L281 lo stesso schema valeva per i 28 delimitatori `"`.

## 5. Un fuori-gate corretto sulla resa, non sul gate

La resa iniziale di `"You're welcome."` era **«Prego.»** (rapporto 0,50, sotto il gate 0,55). La traduzione era corretta ma
**troppo corta** rispetto al testo: sostituita con **«Di niente.»** (0,72), che è altrettanto naturale e resta nel gate. **Ho
corretto la resa, non la soglia.**

## 6. Verifica

```
check.py   23 controlli · FAIL totale: 0 · exit 0
verify.py  22 controlli · FAIL: 0 · exit 0
FILE       54/54 (100%) · ventiduesimo file completo
```

**Tre rossi al primo giro, tutti su controlli miei:**

1. il controllo «tutte tradotte» colpiva **`"Sitrasanir?"`**, che è identica **per necessità** → aggiunto `ID_OK` dichiarato;
2. la verifica del punto dentro la parentesi cercava `.` alla fine di una stringa che finisce con `.)` → corretto in `endswith('.)')`;
3. `sitrasanir` contato **2** invece di **3**: la domanda ha l'iniziale maiuscola (`Sitrasanir?`) → conteggio reso
   **case-insensitive** e controllo esplicito sulla forma maiuscola.

## 7. Il cerchio che si chiude

`[genitori, antenati]` (unità 8) è **la stessa coppia di L282** (`[parents? ancestors?]`, unità 5), dove il drone si era
interrotto. Il test verifica la **coerenza cross-lot** con la resa già usata: è il terzo caso di ripresa verbatim del corpus
dopo la scheda ionica (L267) e la formula Efreti (L275→L276).

## 8. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 9 unità `PENDING`; il file è **finito in staging**, non approvato.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Il file è completo al 100%** solo in staging.
- **Le scelte fra parentesi** sono verificate **per forma**, non eseguite nel motore di missione.
