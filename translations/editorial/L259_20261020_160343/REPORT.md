# REPORT — L259 (`data/human/post-war reactions.txt`, righe 222–250)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **23 controlli**; `verify.py` esce 0 con **23 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 15 | 15 |
| parole | 426 | **441** (1,04) |
| tab | 15 | 15 · tutte le unità · primo carattere |
| virgolette | 45 | 45 · **mappa per unità identica** |
| apici | 19 su 10 unità | 17 su 8 unità |
| segnaposto | 4 (`<first>` 2, `<last>` 2) | 4 · stesso ordine per unità |

Rapporto per unità **0,93 – 1,53**: nessuna resa fuori gate. Il massimo è la **6** (`"A dire il vero, ho guidato io la
battaglia."` per `"Actually, I led the battle."`): la battuta è di quattro parole in inglese, e in italiano non scende sotto
le sette senza perdere il «io» enfatico che è il punto della battuta.

## 2. Terza citazione non chiusa (unità 2)

```
"The Syndicate lets some of us orphans work in industry. In return they give us better schooling, nicer housing, and doctor's visits." He puffs himself up. "Only the cleverest of us get to do it. … Just ordinary stuff, like hammers, soldering irons, or sewing machines.
```

**Cinque** virgolette: due coppie chiuse e una che **apre** l'ultima citazione senza chiuderla. La resa italiana ne ha
cinque, con la frase che finisce in `cucire.` — verificato in entrambe le lingue.

La ricorrenza (L257 u12, L258 u5, L259 u2) dice che **non è un difetto dell'estrattore**: il sorgente contiene citazioni
aperte e non chiuse, e il compito del lotto è **riprodurle**, non correggerle.

## 3. Le unità 7 e 8

| unità | inglese | italiano |
|---|---|---|
| 7 | `…he declares, "You're Captain <first> <last>! Wow! …` | «…dichiara: "Sei il capitano `<first>` `<last>`! Wow! …» |
| 8 | `…he declares, "You led the attack! Wow! …` | «…dichiara: "Hai guidato tu l'attacco! Wow! …» |

Sono **lo stesso testo** tranne una battuta. Il `check.py` verifica che la testa (60 caratteri) e la coda siano **identiche**,
che la battuta diversa ci sia in una e **non** nell'altra, e che entrambe finiscano con `Ti tende la mano e tu la stringi.`
Un controllo sui soli conteggi non distinguerebbe «tradotte bene» da «copiate l'una dall'altra».

## 4. Il contenuto

Gus racconta il fratello (soldato semplice di terza classe del **Servizio di Sicurezza Ausiliario del Sindacato**), spiega
di essere **orfano** e di lavorare nell'industria in cambio di scuola, casa e visite mediche, riconosce il capitano dal
tablet (**Dispositivo per l'Infanzia del Sindacato**) e fa il tifo per la guerra; il capitano risponde su tre toni — «Ho
fatto saltare la mia parte di navi Pug», «A dire il vero, ho guidato io la battaglia», «La guerra è un inferno, ragazzo» — e
chiude sul piano dei Pug: «era un trucco per farci smettere di combattere tra noi».

## 5. Lessico nuovo, fissato qui

| inglese | resa |
|---|---|
| `Ancillary Security Service` | **Servizio di Sicurezza Ausiliario** |
| `Syndicate Childcare Device` | **Dispositivo per l'Infanzia del Sindacato** |
| `data pad` | **tablet** |
| `private, third class` | **soldato semplice di terza classe** |
| `edu-screen` | **schermo didattico** |
| `warship` | **nave da guerra** |
| `soldering irons` | **saldatori** |
| `chess with guns and engines` | **scacchi con cannoni e motori** |
| `self-destruction` | **autodistruzione** |
| `Woah` | **Uau** |

## 6. Verifica

```
check.py   23 controlli · FAIL totale: 0 · exit 0
verify.py  23 controlli · FAIL: 0 · exit 0
segmento   65 prima · 15 qui · 7 dopo la 250 · 80 righe distinte su 87 · copertura 80/87 (92,0%)
```

Un solo rosso, **nel `check.py`, al primo giro**: il confronto delle code fra 7 e 8 usava `[-34:]` contro una costante di 32
caratteri, quindi falliva per **due caratteri di troppo** nel campione. Corretto separando le due cose — `[-60:] == [-60:]`
fra le unità, e `endswith(...)` contro la costante — invece di allargare la costante.

## 7. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 15 unità `PENDING`.
- **Nessun testo visto nel gioco**.
- **Nessuna revisione umana**.
- **Il file resta aperto a 80/87**: L260, **terminale**, chiuderà le ultime 7 unità.
