# L26 — stato di avanzamento (CHIUSO il 2026-10-17)

`data/coalition/coalition missions.txt`, righe **2913–3868**, **406 unità**, 10.765 parole, 19 contesti.
Ultimo segmento del file: dopo la riga 3868 non resta nulla, quindi L26 **chiude** `coalition missions.txt`
a 1.580/1.580. Deviazione dal target: **−73%**, dichiarata (`HANDOFF_L26` §3): lotto corto per chiudere il file.

## Fatto

| parte | unità | righe | esito |
|---|---|---|---|
| part01 | 1–90 | 2913–3187 | `check.py --range 1 90` verde |
| part02 | 91–180 | 3190–3396 | `check.py --range 91 180` verde |
| part03 | 181–270 | 3398–3599 | `check.py --range 181 270` verde |
| part04 | 271–360 | 3604–3742 | `check.py --range 271 360` verde |
| part05 | 361–406 | 3743–3868 | `check.py --range 361 406` verde |

**406 / 406 unità · 10.765 EN → 10.151 IT (100%) — file completo**

Misure dell'esecuzione completa su tutte le 406 unità (lette, non dedotte): tab **308/308**, virgolette
**593/593**, token **69/69**, backtick 0/0, rapporto 0,69–1,86, nessuna parola inglese residua, nessun duplicato
italiano non giustificato dal sorgente.

## Regole specifiche di questo lotto

- **`NT` = 27 unità**, tutte `UI_LABEL`: righe `label "…"` con un `goto` a monte, quindi nomi di nodo.
  Elenco: 115, 117, 119, 133, 135, 160, 162, 167, 171, 175, 179, 181, 185, 260, 310, 317, 319, 323,
  332, 335, 337, 344, 347, 350, 353, 359, 361.
- **`CONVERSATION` (23 unità) non è un'etichetta**: è il **testo visibile** dentro un blocco
  `conversation`, delimitato da backtick nel `raw`. Il delimitatore è già rimosso in `english`, quindi il
  testo si traduce come prosa e il controllo dei backtick resta 0/0. Unità: 383–405.
- **`TOKEN_EXC` vuoto**: nessun pronome-token. Token presenti: `<system>`, `<last>`, `<planet>`,
  `<destination>`, `<payment>`, `<waypoints>`, `<origin>`, `<ship>`, `<stopovers>`, `<model>`, `<first>`.
- **99 unità senza tab iniziale** (`VALUE`, `DESCRIPTION`, `DIALOG`, `UI_LABEL`, e le `CONVERSATION` che
  iniziano con il testo): il tab va confrontato **per unità**, non per totale.
- **7 gruppi di duplicati inglesi / 15 unità**: l'italiano identico è ammesso solo dentro un gruppo.
  Attenzione: **9 e 122** hanno lo stesso inglese (`Sorry, I'm not interested.`), quindi la stessa resa;
  **51 e 54** (`Fine, just tell me already.`) idem.

## La voce dei popoli della Coalizione (vale anche qui)

Gli Arachi di questo lotto (Flopug, i due operai, l'Arach del deposito) parlano con **ordine rovesciato**:
complemento → soggetto esplicito → verbo in fondo, un solo verbo finale per proposizione.

> «Scusarci dovete, capitano, ma in bisogno del vostro aiuto, noi siamo.» (3)
> «Lavorare per la Casa Idriss, noi lo facciamo.» (4) · «Arrivare lì, la sonda presto dovrebbe.» (18)

Narratore, log, descrizioni, `DIALOG` e **personaggi umani** (il pirata del deposito, il contadino)
restano in italiano normale: è il contrasto che rende leggibile il testo.

## Glossario L26 (aggiunte)

| inglese | italiano | nota |
|---|---|---|
| `House Idriss` | Casa Idriss | già in L25 |
| `Flopug` | Flopug | presidentessa facente funzioni |
| `probe` | sonda | |
| `Quicksilver` | Quicksilver | nave, invariata |
| `Outskirts Gauger` | Outskirts Gauger | nome dello scanner, invariato (nome commerciale) |
| `jump drive` | motore di salto | coerente con L24/L25 |
| `junkyard` | deposito di rottami | |
| `Darkstone`, `Han` | invariati | pianeta / sistema umano |
| `Long Lost Property` | Proprietà perduta da tempo | |
| `Lost and Found` | Smarrimento e ritrovamento | |
| `Reclaim the Probe` | Recuperare la sonda | |
| `Comparing Binaries` | Confrontare le binarie | |
| `South` (`outside the South`) | Sud | regione dello spazio pirata |
| `Kachachee` | Kachachee | Kimek, collezionista di letteratura |
| `Anna Fangvin` | Anna Fangvin | autrice umana |
| `Beyond the Hyperdrive` | Oltre l'Iperguida | libro di Anna |
| `Worlds Wide Web` | Rete Mondiale | rete umana |
| `Alexandria` | Alessandria | archivio già noto dalle missioni umane |
| `datachip` / `data card` | chip dati / scheda dati | |
| `hypernet` | iperrete | |
| `Wardragon` | Wardragon | nave Quarg, invariata |
| `Starcross` | Starcross | pianeta, invariato |
| `Rim` / `Paradise Worlds` / `Dirt Belt` | Bordo / Mondi del Paradiso / Fascia di Terra | da `TITLES` |
| `book club` | club del libro | |
| unità 116, 118, 172, 186 | 3 virgolette nel sorgente (battuta non chiusa) | riprodotte: 3 in italiano |
| unità 252 | 1 virgoletta nel sorgente (solo apertura) | riprodotta: 1 in italiano |
| `Heliarchy` | Heliarchia | istituzione, distinta dagli Heliarchs |
| `Ring of Friendship` | Anello dell'Amicizia | |
| `Temporo` | Temporo | Heliarch Saryd |
| `Humanika` | Humanika | pianeta Quarg, invariato |
| `hyperlane` / `hyperspace relay` | ipervia / relè iperspaziale | coerente con L25 |
| `Priyepichia Publishing` | Priyepichia Publishing | casa editrice, invariata |
| `Ikiyachee` | Ikiyachee | caporedattore |
| `Ki Patek Ka` | Ki Patek Ka | pianeta Kimek, invariato |
| `Akacharra` | Akacharra | Kimek del lounge |
| unità 309, 311 | 1 virgoletta nel sorgente (solo apertura) | riprodotta: 1 in italiano |
| unità 313 | 2 virgolette, identica a 309 tranne la chiusura | 2 in italiano, con la chiusura (e quindi distinguibile da 309) |
| unità 346 | 3 virgolette (battuta non chiusa) | 3 in italiano |
| `longcow steak` | bistecca di longcow | animale già in L25 |

## Chiusura (esito misurato)

```
check.py (intero lotto)   FAIL totale: 0
  tab 308/308 · virgolette 593/593 · token 69/69 · backtick 0/0
  rapporto 0,69-1,86 · caratteri non latini: nessuno · trattini lunghi: nessuno
verify.py                 28 controlli · FAIL: 0 · exit 0
translation.json          sha256[:16] 889ca7d8935e9ac0
```

`verify.py` asserisce che il lotto finisce **alla riga 3868** con **0 unità dopo**, che prima ce ne sono
**1.174** (L25) e che il file è coperto **1580/1580** da **due** lotti, con **zero** unità sovrapposte.
Asserisce anche che le **23 `CONVERSATION`** sono tradotte e che **nessuna** di esse è finita in `NT`:
è il controllo che avrebbe colto l'errore opposto a quello che l'handoff di L25 temeva.

Documenti di chiusura: `review.md` (8 sezioni) e `REPORT.md`. Le 406 unità sono **`PENDING`** nel DB:
lo staging **non** è approvazione, e nulla è mai stato renderizzato nel gioco.

Con L26 `data/coalition/coalition missions.txt` è **completo**: 1.580/1.580 unità, 48.224 EN → 46.002 IT.

## Dopo L26

L27: `data/kahet/kahet missions.txt`, righe **39–3048**, **917 unità**, **35.520 parole**, **49 contesti**
(confine misurato con `next_section.py`). Dopo la riga 3048 resta `Ka'het: Patir Mystery 20`, che apre
il segmento successivo: **821 unità / 30.796 parole**.
