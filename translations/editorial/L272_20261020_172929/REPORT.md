# REPORT — L272 (`data/dialog phrases.txt`, righe 102–172) — **LOTTO TERMINALE**

**Esito: lotto CHIUSO, file CHIUSO.** `check.py` esce 0 con **26 controlli**; `verify.py` esce 0 con **21 controlli**.
`state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 25 (tutte `TEXT`) | 25 |
| parole | 446 | **438** (0,98) |
| contesti | 18 | 18 |
| segnaposto | 30 in 6 famiglie | **30 in 6 famiglie** |
| tab / virgolette | 0 / 0 | 0 / 0 |
| apici | 7 | 4 |

Rapporto per unità **0,92 – 1,31**.

## 2. Il lotto

| gruppo | frasi |
|---|---|
| **taglia eliminata** | 2 frasi (bersaglio singolo, con o senza pagamento immediato) |
| **taglia con flotta** | 4 frasi (bersaglio + flotta) |
| **taglia non ancora eliminata** | 3 frasi, di cui una che chiede di **abbordare** invece di distruggere |
| **flotta pirata in orbita** | «ci sono ancora pirati che girano in cielo» |
| **contrabbando concluso** | 2 frasi (carico normale e **altamente illegale**) |
| **contrabbando abortito** | 3 frasi (passeggero, carico, **schiavi**) |
| **Free Worlds** | 2 frasi (missione essenziale fallita / rifiutata) |
| **tributo pacifista** | **8 frasi** |

## 3. Distruggere o abbordare: la differenza è nel testo

Le tre frasi «non ancora eliminata» non sono equivalenti:

| unità | inglese | resa |
|---|---|---|
| 3 | `Hunt it down and destroy it` | **Dalle la caccia e distruggila** |
| 4 | `Hunt it down and board it` | **Dalle la caccia e abbordala** |
| 8 | `Hunt it down and destroy it` (bersaglio + flotta) | **…e distruggile** |

Se l'unità 4 avesse usato «distruggila», il giocatore avrebbe distrutto una nave che la missione chiede di **catturare**: è
il tipo di errore che cambia il gameplay, non lo stile.

## 4. Il tributo pacifista

Otto risposte **non violente** allo stesso evento, con toni diversi: dalla minaccia ferma («Non ti combatteremo. Non ti
uccideremo. Ma non ti pagheremo nemmeno un solo credito di tributo.») alla supplica («Ti supplichiamo di ripensare a questa
decisione avventata.»). Sono **otto stringhe distinte**, verificate come tali: se due fossero diventate identiche in
italiano, il controllo sull'insieme sarebbe rosso.

## 5. Verifica

```
check.py   26 controlli · FAIL totale: 0 · exit 0
verify.py  21 controlli · FAIL: 0 · exit 0
segmento   29 prima · 25 qui · 0 dopo (fine file) · 18 contesti
FILE       54/54 (100%) · somma dei due lotti 54 · righe distinte 54 · ultima 172
```

Un rosso al primo giro: contavo **tre** occorrenze di «sono state eliminate», ma sono **due** (unità 5 e 6); la terza forma
è «non sono **ancora** state eliminate» (unità 8). Corretto misurando le unità, non allargando l'asserzione.

Un **errore del contratto** corretto nel documento, non nel codice: `HANDOFF_L272` dichiarava **tre** unità pacifiste
(165, 167, 171); sono **otto** (165–172). Vince il workspace.

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 25 unità `PENDING`; il file è **finito in staging**, non approvato.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Il file è completo al 100%** solo in staging: 54 unità su 54, tutte `PENDING`.
