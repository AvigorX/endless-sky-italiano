# REPORT — L110 · `korath missions.txt` (**file completo**: il recupero, il coro di ologrammi, la dedica)

## 1. Contenuto

| contesto | righe | unità | cosa succede |
|---|---|---|---|
| `Efreti: Distress Call 6` | 474–479 | 3 | il requisito dei posti letto, il nome della missione ripetuto |
| `Efreti: Distress Call 7` | 508–558 | 16 | atmosfera «tropicale», scelta di portare o abbandonare, padiglione, coro di ologrammi, bevanda, trucco |
| `Efreti: Distress Call 8` | 570–580 | 7 | il Quarg che traduce il chip, la dedica, il chip riposto |

## 2. Scelte

| nodo | scelta | perché |
|---|---|---|
| `Salvage the <EDC-ship>` | **identico** | `VALUE`, e **ripetuto** in 1 e 4 |
| `Salvage the <EDC-ship> and return it to <planet> to claim rights to it.` | **Recupera la `<EDC-ship>` e riportala su `<planet>` per rivendicarne la proprietà.** | `DESCRIPTION`, **ripetuta** in 2 e 5, resa identica |
| `claim rights to it` | **rivendicarne la proprietà** | il recupero serve a **rivendicare** la nave |
| `<bunks> additional crew` | **`<bunks>` membri d'equipaggio in più** | |
| `sufficient crew capacity` | **capienza sufficiente per l'equipaggio** | |
| `brought to human standards, if a bit tropical` | **portata agli standard umani, anche se un po' tropicali** | |
| `battery systems are beyond repair` | **i sistemi delle batterie sono irrecuperabili** | |
| `shield regeneration is impossible` | **la rigenerazione degli scudi è impossibile** | |
| `abandons the Korath ship to the elements` | **abbandona la nave Korath alle intemperie** | |
| `just one more tragic story amid the ruins of their civilization` | **solo un'altra storia tragica fra le rovine della loro civiltà** | |
| `bring up the shields` | **attivare gli scudi** | |
| `evade Mereti patrols` | **evitare le pattuglie Mereti** | |
| `the <EDC-ship> is absent` | **la `<EDC-ship>` non c'è** | `DIALOG`, arrivo senza nave |
| `the ground crews seem astonished` | **le squadre di terra sembrano stupite** | |
| `a pavilion has been set up` | **un padiglione è stato montato** | |
| `arranged like a choir, but standing oddly still` | **disposti come un coro, ma stranamente immobili** | |
| `a table piled with sweets and cups of some kind of thick drink` | **un tavolo ingombro di dolciumi e di coppe colme di una bevanda densa** | |
| `the "choir" is made of holograms` | **il "coro" è fatto di ologrammi** | le virgolette restano |
| `some type of memorial` | **una specie di memoriale** | |
| `presses a cup into your hand` | **vi preme una coppa in mano** | |
| `either the Efret don't notice your ruse, or they are too polite to say` | **o gli Efret non si accorgono del vostro trucco, o sono troppo educati per dirlo** | |
| `They press the sweets on you` | **Vi insistono con i dolciumi** | *press on* = insistere |
| `humbly accept them` | **li accettate con umiltà** | |
| `The drink is fermented` | **La bevanda è fermentata** | |
| `a sweet and sour taste` | **un sapore agrodolce** | |
| `leaves your lips and mouth tingling, eventually numbing them` | **lascia le labbra e la bocca formicolanti, finché non le intorpidisce** | |
| `have translated the Korath language for you in the past` | **In passato i Quarg vi hanno tradotto la lingua Korath** | |
| `request assistance with the data chip` | **chiedete aiuto con il chip dati** | |
| `slots it into a communicator of some sort` | **lo inserisce in una specie di comunicatore** | |
| `a ship of grief` | **una nave di dolore** | dedica |
| `memories that sing for generations` | **memorie che cantano per generazioni** | |
| `Love is a void in the souls of many` | **L'amore è un vuoto nell'anima di molti** | |
| `a true Efret by heart, if not by skin` | **un Efret autentico di cuore, se non di pelle** | **nessun genere attribuito al giocatore** |
| `to save lives and keep memories` | **per salvare vite e custodire memorie** | |
| `store the chip in a safe place` | **Riponete con cura il chip in un posto sicuro** | |

## 3. Difficoltà

1. **Due coppie di ripetizioni identiche** (1/4 e 2/5): il criterio «zero ripetizioni» dei lotti precedenti qui va
   **rovesciato**. Il `check.py` verifica che le due coppie siano **esattamente** quelle e che ogni coppia sia resa
   identica; il `verify.py` rifà il conto dai dati del sorgente.
2. **Invariante di file, non di segmento**: il `verify.py` rilegge i `translation.json` di **tutti** i lotti del
   file e verifica **158 `id` distinti**, somma 25+38+36+33+26 = 158, copertura completa degli `id` del database,
   nessuna sovrapposizione. È la prova che il file è chiuso.
3. **`<first>` e `<last>` nello stesso testo**, dentro una citazione con due virgolette: la dedica è l'unico punto
   del file in cui il giocatore è nominato per nome.
4. **Nessun genere attribuito al giocatore**: «un Efret autentico di cuore» evita la concordanza che in italiano
   tradirebbe il sesso del personaggio.
5. **Il `DIALOG` (unità 11)** descrive un arrivo **senza** la nave: è testo di scena, non una battuta, e contiene il
   token `<EDC-ship>`.
6. **Il coro di ologrammi** ha due virgolette nel sorgente e due nella resa: la parola «coro» resta fra virgolette
   in tutte e tre le occorrenze del lotto (15, 18, 19), perché il narratore la usa come citazione del proprio
   fraintendimento.

## 4. Numeri osservati

```
unita' 26/26 · 21 MISSION_TEXT + 2 VALUE + 2 DESCRIPTION + 1 DIALOG
tab 17 · virgolette 8 = 8 (tutte binate) · token 19 = 19 in sette famiglie
quadre 0 · citazioni aperte 0 · ripetizioni: ESATTAMENTE 2 coppie (1/4, 2/5) rese identiche
parole EN 730 -> IT 669 · rapporto 0.67 - 1.19
righe 474/580 · file 158 unita · max(line) 580 · 132 prima / 0 dopo
cinque lotti (25+38+36+33+26) = 158 · 158 id distinti · 0 sovrapposizioni
FAIL totale: 0 (28 controlli) · verify exit 0 (35 controlli)
sha256[:16] 741adbe5e3ce5afc · copertura file 158/158 (100%)
```

## 5. Stato del progetto

```
TOTALE staging: 25627 unita · 822054 EN · 779416 IT
korath missions.txt: 158/158 (100%) · 5 lotti · 5268 EN -> 5103 IT
file completi: QUARANTUNO · residuo traducibile (formula state.py): 6303
residuo misurato: 6882 unità / 154001 parole su 125 file
avanzamento: 25627/32924 unità (77,8%) · 822054/979975 parole (83,9%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | due parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (28 controlli), `verify.py` exit **0** (35 controlli, invariante di file) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 26 unità restano `PENDING`; il gioco non è stato caricato.
- **Il file è completo ma non approvato**: `korath missions.txt` 158/158 in staging, **quarantunesimo file**.
- **Prossimo file**: `data/_ui/tooltips.txt` (667 unità, `max(line) = 1865`), primo lotto `HANDOFF_L111_20261018.md`
  righe 16–328, **104 `TUTORIAL_TIP`**.
- **Nessuna revisione umana**.
