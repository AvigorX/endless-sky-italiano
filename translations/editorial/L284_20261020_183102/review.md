# review.md — L284 (`data/wanderer/wanderer missions.txt`, righe 93–136)

Registro delle decisioni editoriali del **terzo lotto** delle missioni Wanderer: dal ritorno sul pianeta al congedo di Va'ika.

## 1. Che cosa succede

**`The Plant 4`** — Va'ika guida il giocatore in una **pianura equatoriale**: «arida ed erbosa», con un vento fresco, ma questa
volta si respira senza che l'aria **pizzichi** occhi e bocca. Prende un po' di terra, la mette in un dispositivo e dice:
«Qui. Qui `[crescerà, attecchirà]`». Le domande del giocatore sono due e brevi; la risposta tecnica è che serviva verificare
**di persona** la `[composizione, natura]` del terreno. Poi l'ordine: tornare a **Vara Kehi'ki**, mandare un **distaccamento**
di `[guaritori, giardinieri]` su `<planet>`, e riportare le piante su `<origin>` **quando sarà guarito**.

**`The Plant 5`** — la pianta viene caricata **con delicatezza** su una **Strong Wind**; i droni Mereti restano **immobili** sulla
piazzola e «hai la netta sensazione che ti stiano osservando». Va'ika guarda lontano **quasi con tristezza** e parla delle navi
da guerra: «È deplorevole che siamo stati `[costretti, obbligati]`…». **Una piuma cade a terra** mentre parla, poi si corregge:
«non dovrei essere così `[scoraggiata?]`». Il finale è un congedo: resterà a `[sovrintendere, osservare]` il lavoro e poi
ripartirà; «Ti ringrazio molto `[gratamente, sinceramente]` per il tuo aiuto, `<first>`».

## 2. La singola: un caso nuovo

Per la prima volta una parentesi quadra ha **una sola opzione** e un `?`: `[disheartened?]`. Non è una scelta fra due
possibilità, è **un'incertezza del personaggio** — Va'ika si riprende a metà frase. Trattarla come coppia avrebbe inventato una
variante; lasciarla in inglese avrebbe rotto la frase. Resa: **`[scoraggiata?]`**.

Il controllo è sulla **distribuzione**, non sul totale: `[2, 2, 2, 2, 2, 2, 1, 2, …]` in entrambe le lingue, unità per unità.
Il contratto diceva «tutte con due opzioni»: **era sbagliato**, e la correzione è scritta in `STATO.md` e `REPORT.md`.

## 3. L'articolo fuori dalla parentesi

Tre casi hanno richiesto attenzione, perché articolo e aggettivi stanno **fuori**:

| inglese | resa | motivo |
|---|---|---|
| `the purpose we originally [conceived, designed] them to [serve, fulfill]` | **lo scopo per cui le avevamo `[concepite, progettate]` e che dovevano `[servire, adempiere]`** | «adempiere» da solo non regge: la relativa «e che dovevano» rende entrambe le opzioni grammaticali |
| `[housing, growing] these plants here` | **`[ospitare, tenere]` queste piante qui** | «coltivare» è già usato nella parentesi successiva: evito la ripetizione a due righe di distanza |
| `a small specialist [group, team]` | **un piccolo `[gruppo, team]` di specialisti** | entrambi maschili singolari, «un piccolo» resta corretto |

## 4. Scelte di registro

| inglese | resa |
|---|---|
| `almost morosely` | **quasi con tristezza** |
| `speaks with clear confidence` | **parla con chiara sicurezza** |
| `I have the utmost confidence in their [knowledge, abilities]` | **Ho la massima fiducia nelle loro `[conoscenze, capacità]`** |
| `a distinct feeling that they are watching you intently` | **la netta sensazione che ti stiano osservando con attenzione** |
| `carefully, almost ceremoniously, taken and placed in the ground` | **presa con cura, quasi con cerimonia, e deposta nel terreno** |
| `It is regrettable that` | **È deplorevole che** |

Il **gesto della piuma** è l'unico dettaglio fisico del congedo ed è verificato lessicalmente (`piuma` nell'unità 14): è ciò che
dice, senza dirlo, che Va'ika è **vecchia** o **ferita**.

## 5. `UI_LABEL` e `VALUE`

| riga | tipo | testo | trattamento |
|---|---|---|---|
| 108 | `UI_LABEL` | `next steps` | **copiato** |
| 93 | `VALUE` | `Return to <planet>` | **copiato** |
| 115 | `VALUE` | `Plant to <planet>` | **copiato**, e **diverso** dall'altro |

## 6. Struttura

| cosa | inglese | italiano |
|---|---|---|
| tab | **8** (unità 4, 5, 6, 8, 14, 15, 16, 18) | **8**, primo carattere |
| virgolette | **20** | **20**, per unità |
| alternative | **18** (17 coppie + 1 singola) | **18**, stessa distribuzione |
| apici | **11** | **14** (`Va'ika` ×8) |
| segnaposto | **12** (5 famiglie) | **12** |

## 7. Cosa resta aperto (dichiarato)

- **Nessuna approvazione**: 18 unità `PENDING`; **nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Il file è a 45/54**: L285 sarà il lotto **terminale** — l'**epilogo** (righe 169–182, **9 unità**, 234 parole, 8 tab, 8
  virgolette, 6 alternative), e chiuderà il file a **54/54**.
