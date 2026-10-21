# review.md — L238 (`data/avgi/avgi news.txt`, righe 418–507)

Registro delle decisioni editoriali del **sesto e ultimo lotto** di `avgi news.txt`: quattro mestieri, cinque etichette
nuove, un'etichetta che sta in mezzo al periodo.

## 1. Le etichette: cinque nuove, due scartate

| inglese | resa | perché non un'altra |
|---|---|---|
| `Fascination.` (×2) | **Fascinazione.** | «Fascino» è più corto ma è un sostantivo di qualità, non una modalità di enunciazione; il corpus usa già «fascinazione» in prosa (2) |
| `Appreciation.` (×3) | **Apprezzamento.** | distinto da `Gratitude` → «Gratitudine» e da «Riconoscenza» (15 in prosa): qui l'Avgi **valuta** qualcosa, non ringrazia |
| `Advisement.` (×1) | **Avviso.** | **non** «Avvertenza»: quella è già la resa di `Warning` (1 precedente). Due parole inglesi diverse, due parole italiane diverse |
| `Consideration.` (×2) | **Considerazione.** | |
| `Recollection.` (×2) | **Rievocazione.** | **non** «Ricordo»: quella è già la resa di `Remembrance` (2 precedenti). «Rievocazione» è nel corpus (2) e dice meglio il **richiamare** un ricordo |
| `emphasis.` (a metà frase) | **enfasi.** | minuscola, dopo la virgola, come l'inglese |

Il `check.py` verifica i **conteggi** (3, 2, 1, 2, 2) e l'**assenza** delle due forme scartate («Ricordo»,
«Avvertenza»): una scelta fra due parole si difende asserendo che l'altra non c'è.

## 2. L'etichetta a metà frase

L'unità 454 è l'unica della campagna in cui la modalità dell'Avgi non apre e non chiude la battuta:

> `"Don't believe people who say art is a waste, emphasis. It's not like we're taking resources away from the War effort."`
> «Non credere a chi dice che l'arte sia uno spreco, enfasi. Non è che stiamo togliendo risorse allo sforzo bellico.»

È lo stesso dispositivo di L236 (etichetta **in coda**, minuscola), spostato **dentro** il periodo. Tradurlo come
avverbio («soprattutto») avrebbe cancellato la firma della specie; sopprimerlo avrebbe perso un'informazione.
Il controllo pretende la virgola, la parola e la minuscola.

## 3. `Twilight Guard`: nome invariato, membri tradotti

| inglese | resa | perché |
|---|---|---|
| `the Twilight Guard` | **la Twilight Guard** | nome di fazione, **30 occorrenze invariate** nello staging (decisione 16) |
| `the Guards coming back from the front lines` | **le Guardie che tornano dal fronte** | sono le **persone**: nome comune, si traduce (decisione 259) |
| `the front lines` | **il fronte** | |
| `doing my part` | **fare la mia parte** | |

## 4. Lessico tecnico fissato

| inglese | resa | nota |
|---|---|---|
| `torchship` (×2) | **nave a torcia** / **nave mercantile a torcia** | nessun precedente nello staging: la propulsione è la *fusion torch*, quindi il composto resta trasparente |
| `fusion torch` | **torcia a fusione** | |
| `medicytes` | **mediciti** | formato sul modello di «nanociti», ma il corpus non aveva il termine: reso una volta e fissato |
| `nanomedicine` | **nanomedicina** | |
| `genetic engineering` | **ingegneria genetica** | |
| `teardrop-shaped brains` | **cervelli a forma di goccia** | |
| `opaque quartz` | **quarzo opaco** | |
| `foggy color` | **colore velato** | non «nebbioso»: è il cristallo, non il tempo |
| `crystal matrix` | **matrice cristallina** | |
| `optical nervous system` | **sistema nervoso ottico** | |
| `electrochemical` | **elettrochimico** | |
| `nerve interfaces` | **interfacce nervose** | |
| `nickelsteel` | **acciaio-nichel** | coerente con la resa dichiarata in L237 |
| `cylinder habitats` | **habitat cilindrici** | 5 precedenti nello staging |
| `asteroid manufactory` | **manifattura su asteroide** | |
| `machine shop` | **officina meccanica** | |
| `nanometer tolerance on a bolt` | **tolleranza al nanometro su un bullone** | |
| `radiation sickness` | **malattia da radiazioni** | |
| `radiation damage` | **danni da radiazioni** | |

## 5. Nomi propri, luoghi, istituzioni

`Avgi`, `Aberrant`, `Anax` (la stella), `Aviskir` (il mondo natale), `Twilight Guard` restano invariati; `the Assembly` →
**l'Assemblea**; `the War effort` → **lo sforzo bellico** (con `the War` → «la Guerra»); `the siege` → **l'assedio**.

## 6. Numeri e misure

`sixty years` → **«sessant'anni»** (in lettere, come l'inglese); nessuna cifra nel lotto, quindi nessuna convenzione
numerica da applicare. L'unità 501 chiude con **tre punti semplici** (`...`) e non con l'ellissi tipografica: asserito,
perché in italiano è la forma vietata dalla tipografia del progetto.

## 7. Struttura e assenze

- **Zero tab**, **zero segnaposto**, **zero righe `log`**, **`NT` vuoto** per misura: quattro asserzioni negative scritte.
- **Nessun gruppo di inglese identico**: 21 stringhe tutte diverse.
- **La finestra è discontinua**: 425–451, 455–477 e 481–499 non producono unità. Il `check.py` lo asserisce, così un
  cambio dell'inventario che riempisse quei vuoti diventerebbe rosso invece di passare inosservato.

## 8. Il file, chiuso

Sei lotti (L233–L238), **115 unità**, 2.164 EN → 2.124 IT. Le decisioni che restano valide per chi riprende: etichetta
sempre riprodotta come etichetta (in testa, in coda, o a metà frase); `Dejection` → «Scoramento»; `Recollection` →
«Rievocazione» ≠ `Remembrance` → «Ricordo»; `Advisement` → «Avviso» ≠ `Warning` → «Avvertenza»; `hyperdrive` →
«iperpropulsore»; `wormhole` invariato.
