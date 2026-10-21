# REPORT — L108 · `korath missions.txt` (frammenti `phrase:`, consegna, chiamata di soccorso)

## 1. Contenuto

| contesto | righe | unità | cosa succede |
|---|---|---|---|
| `kor efret small package offer` (`phrase:`) | 216–241 | 14 | i frammenti che compongono la richiesta di un Korath |
| `Small Scale Delivery` | 244–260 | 3 | pacco consegnato a un Kor Efret che attende a mani tese |
| `Efreti: Distress Call 1` | 269–303 | 11 | il Quarg in tono arcaico, i droni Mereti, 40 Korath da salvare, le risposte del giocatore |
| `Efreti: Distress Call 2` | 309–326 | 8 | le cuccette dimenticate, il fucile termico, la nave-ospedale, il trasbordo |

## 2. Scelte

| nodo | scelta | perché |
|---|---|---|
| `A Korath` · `A Kor Efret` · `A local` | **Un Korath · Un Kor Efret · Un locale** | casella **soggetto**: maiuscola, nessun punto |
| `communicates using gestures that it wants you to` | **con gesti ti comunica che devi** | regge un **infinito** («che devi **portare**») |
| `uses gestures to ask you to` | **con gesti ti chiede di** | idem («chiede di **portare**») |
| `bring a small crate` | **portare una piccola cassa** | infinito in testa |
| `bring a package` | **portare un pacco** | |
| `take a shipment weighing less than one ton` | **accettare una spedizione che pesa meno di una tonnellata** | verbo distinto dagli altri tre |
| `carry a box` | **portare una scatola** | *carry* → «portare»: «trasportare» superava il gate di lunghezza (2,09) |
| `to <destination> for <payment>.` | **a <destination> per <payment>.** | inizia con `a `, un solo punto, in coda |
| `It shouldn't take up any significant room on your ship.` | **Non dovrebbe occupare spazio di rilievo sulla vostra nave.** | frase finale autonoma |
| `It's small enough to fit below your seat.` | **È abbastanza piccolo da stare sotto il vostro sedile.** | |
| `The item is small enough for you to hold in your hands.` | **L'oggetto è abbastanza piccolo da stare nelle vostre mani.** | |
| `It's small enough that it won't take up any cargo space.` | **È abbastanza piccolo da non occupare spazio di carico.** | |
| `Package to <planet>` | **identico** | `VALUE` |
| `Take a small delivery to <destination> for <payment> for a Kor Efret.` | **Porta una piccola consegna a <destination> per <payment> per un Kor Efret.** | `DESCRIPTION` |
| `They greet you by showing their palms` | **Vi saluta mostrando i palmi** | saluto Korath, coerente con L106–L107 |
| `Distress call from the <EDC-ship>` | **identico** | `VALUE` |
| `Salutations, Captain of the <ship>.` | **Salute, Capitano della <ship>.** | registro arcaico del Quarg |
| `Victims of uncertain fate` | **Vittime di sorte incerta** | |
| `lest many families mourn the dead` | **perché molte famiglie non abbiano a piangere i morti** | congiuntivo esortativo, non «per non» |
| `waylayed … ere it could elude` | **hanno teso un agguato … prima che potesse sottrarsi** | `waylayed` è un errore del sorgente: reso |
| `Two score Korath still live` | **Quaranta Korath vivono ancora** | *score* = venti |
| `We vanquished the Mereti` | **Abbiamo vinto i Mereti** | |
| `Without strong plate, we fare ill on a heavy world.` | **Senza una corazza robusta, su un mondo pesante si patisce assai.** | |
| `Life is rare and precious across the vastness of space` | **La vita è rara e preziosa nella vastità dello spazio** | |
| `when one cares not what others suffer` | **quando non ci si cura di ciò che gli altri soffrono** | impersonale, come il sorgente |
| `Return the <EDC-ship> survivors` | **identico** | `VALUE` |
| `Transport the <bunks> survivors … to <planet>.` | **Trasporta i <bunks> superstiti … su <planet>.** | `<bunks>` = numero |
| `the <bunks> bunks you need for the evacuees` | **le <bunks> cuccette che vi servono per gli evacuati** | |
| `staring down a thermal rifle` | **vi trovate di fronte un fucile termico puntato** | |
| `makeshift hospital` | **ospedale di fortuna** | |
| `running on emergency power` | **vanno con l'energia di emergenza** | |
| `incapacitated or unconscious` | **inabile o incosciente** | |
| `spaceworthy` | **in grado di volare nello spazio** | |

## 3. Difficoltà

1. **Quattordici frammenti composti a runtime**: il vincolo non è il significato ma la **forma** — maiuscola,
   minuscola, infinito, punto in coda solo nella casella giusta. Il `verify.py` compone **tutte e 24** le frasi
   soggetto × verbo × oggetto e verifica che nessuna produca punteggiatura doppia, doppie maiuscole o `di di`.
2. **`ratio` fuori gate su un frammento corto**: `carry a box` → «trasportare una scatola» dava **2,09**, sopra il
   limite di 1,90. Il gate ha fatto il suo lavoro: sostituito con «portare una scatola» (1,63) e «accettare» per
   l'unità 8, così le quattro caselle oggetto non ripetono tutte lo stesso verbo.
3. **Cinque tipi con tre regole opposte**: `VALUE` identici (15, 18, 29); `TEXT`, `MISSION_TEXT`, `DESCRIPTION`,
   `DIALOG` tradotti. Il controllo «tutte tradotte» deve **escludere i `VALUE`**, altrimenti fallisce — errore
   già commesso in L107.
4. **`<EDC-ship>` otto volte**, tre delle quali dentro `VALUE` che restano identici: un token sbagliato rende
   rosso il totale e due controlli insieme.
5. **Quattro contesti con un `phrase:` in testa**: il `verify.py` li elenca in ordine di riga.
6. **Il Quarg arcaico** (21, 25, 28) non è il Quarg storpiato di L107: qui parla **bene ma in registro alto** —
   «esigono il vostro zelo più diligente», «prima che potesse sottrarsi», «si patisce assai». Due voci diverse,
   due rese diverse, nello stesso file.
7. **`Distress Call 2` resta aperto** alla riga 326: il lotto chiude a metà contesto e il `verify.py` dichiara
   **59 unità dopo**, non zero.

## 4. Numeri osservati

```
unita' 36/36 · 14 TEXT + 15 MISSION_TEXT + 3 VALUE + 3 DESCRIPTION + 1 DIALOG
tab 12 (21-28, 33-36) · virgolette 18 = 18 (tutte binate) · token 23 = 23 in sei famiglie
quadre 0 · citazioni aperte 0 · ripetizioni 0 · identiche: 15, 18, 29 (VALUE)
24 combinazioni di frammenti composte e verificate
parole EN 737 -> IT 730 · rapporto 0.62 - 1.73
righe 216/326 · file 158 unita · max(line) 580 · 63 prima / 59 dopo
FAIL totale: 0 (33 controlli) · verify exit 0 (36 controlli)
sha256[:16] c429ddeb0b22241c · copertura file 99/158 (62,7%)
```

## 5. Stato del progetto

```
TOTALE staging: 25568 unita · 820119 EN · 777559 IT
korath missions.txt: 99/158 (62,7%) · 3 lotti
file completi: 40 · residuo traducibile (formula state.py): 6362
residuo misurato: 6941 unità / 155936 parole su 126 file
avanzamento: 25568/32924 unità (77,7%) · 820119/979975 parole (83,7%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | due parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (33 controlli), `verify.py` exit **0** (36 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 36 unità restano `PENDING`; il gioco non è stato caricato.
- **La composizione dei frammenti non è stata vista a schermo**: verificata sui **vincoli di forma** e sulle 24
  combinazioni, non sull'output del motore.
- **Il file non è completo**: 59 unità residue; prossimo contratto `HANDOFF_L109_20261018.md` (righe 338–451).
- **Nessuna revisione umana**.
