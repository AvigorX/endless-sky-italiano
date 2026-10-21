# REPORT — L291 (`data/avgi/avgi culture conversations.txt`, righe 122–227)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **26 controlli**; `verify.py` esce 0 con **23 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 12 (tutte `MISSION_TEXT`) | 12 |
| parole | 451 | **464** (1,03) |
| tab | 3 | 3 (righe 183, 198, 213) |
| virgolette | 16 | **16**, per unità |
| segnaposto | 3 (`<planet>`) | **3** |
| apici | 16 | 10 |
| coppie consecutive | 3 | 3 |

Rapporto per unità **0,96 – 1,21**.

## 2. Gli otto atti dichiarati

Il file conferma il tic degli Avgi: **la battuta comincia con l'atto che compie**. La forma viene da `avgi news` (tradotto in
lotti precedenti), dove l'inglese `Rejection.` / `Anger.` / `Exasperation.` era già reso «Rifiuto.» / «Rabbia.» /
«Esasperazione.»: **sostantivo astratto, maiuscola, punto**.

Qui la serie è: «Incredibile.» (aggettivo, unica eccezione), «Apprezzamento.», «Proclama.», «Dichiarazione.», «Attenzione!»,
«Scherno!», «Comando.», «Imbarazzo.». Il test verifica **tutte e otto** con una lista esatta.

## 3. Le due versioni del graffito (122 e 126)

Non sono consecutive (quattro righe di distanza) e non sono identiche: la prima dice «**non sei sicuro** di che cosa dicano», la
seconda **legge**. Il lessico comune — «simboli colorati e ricurvi», «un pugno di Avgi con spazzole e mocci» — è verificato
**case-insensitive** in entrambe: la seconda versione comincia con la maiuscola, la prima no, e un confronto sensibile al caso
fallisce sul testo corretto.

## 4. Il gioco di parole

`'Twilight Guard? More like Twilight Gourd.'` — **Guard/Gourd**. `Twilight Guard` è una **fazione** (40 occorrenze nel corpus,
sempre in inglese). Tradurre il nome avrebbe significato **rinominare una fazione** per salvare una battuta: la scelta è di
lasciare **nomi e gioco di parole in inglese** e **dichiararlo** come limite (un lettore italiano non coglie il bisticcio).
L'alternativa «Zucca del Crepuscolo» è stata **scartata** e il motivo è scritto qui, non solo pensato.

## 5. Le tre coppie consecutive

| coppia | righe | tab | contenuto |
|---|---|---|---|
| `General Ripper` | 182–183 | sulla 183 | la dichiarazione e l'arrivo della sicurezza |
| `Criminal Mischief` | 197–198 | sulla 198 | l'inseguimento e la battuta della ladra |
| `False Alarm` | 212–213 | sulla 213 | l'allarme e la smentita |

Il tab sulla **seconda** metà è verificato unità per unità, insieme all'assenza sulla prima.

## 6. Terminologia

| inglese | resa |
|---|---|
| `scrawled all across` | **tracciati su** |
| `brushes and mops` | **spazzole e mocci** |
| `less than amused` | **si divertono molto meno** |
| `head buried in` | **con la testa immersa in** |
| `megaphone` | **megafono** |
| `denizens` | **abitanti** |
| `precious bodily fluids` | **preziosi fluidi corporei** |
| `fluid gap` | **divario di fluidi** |
| `burlap sack` | **sacco di tela** |
| `batons` | **manganelli** |
| `squeal of static` | **stridio di statica** |
| `rapiers` | **stocchi** |

`Aberrant` → **gli Aberrant** (forma del corpus: 31 occorrenze con l'articolo e il nome inglese; esistono anche «Aberrante» 48 e
«Aberranti» 37 — **divergenza dichiarata, non sanata**).

## 7. Verifica

```
check.py   26 controlli · FAIL totale: 0 · exit 0
verify.py  23 controlli · FAIL: 0 · exit 0
segmento   8 prima · 12 qui · 26 dopo la 227 · 8 contesti
```

**Un rosso al primo giro** (controllo mio): cercavo «simboli colorati e ricurvi» **con la minuscola** in un'unità che comincia
con «Simboli» → confronto reso **case-insensitive**.

## 8. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 12 unità `PENDING`.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Il gioco di parole è intraducibile senza rinominare una fazione**: dichiarato, non risolto.
- **Il file resta aperto**: 20/46; restano **26 unità** (24 `MISSION_TEXT` + **2 `LOGBOOK`**, i primi del progetto).
