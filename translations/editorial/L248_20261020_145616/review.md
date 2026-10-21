# review.md — L248 (`data/human/syndicate jobs.txt`, righe 157–275)

Registro delle decisioni editoriali del **secondo lotto** di `syndicate jobs.txt`: due consegne urgenti, una missione
ripetuta in tre contesti, cinque nomi di lavoro da copiare.

## 1. Che cosa si copia e che cosa si traduce

| tipo | unità | trattamento | esempio |
|---|---|---|---|
| `VALUE` | 5 | **copiato** | `Rush fuel delivery to <planet>`, `Syndicate target practice` |
| `DESCRIPTION` | 5 | **tradotto** | la scheda del lavoro |
| `DIALOG` | 10 | **tradotto** | le battute alla consegna |

I tre `VALUE` distinti sono **nomi di lavoro**: si copiano anche quando coincidono col nome della missione
(`Syndicate target practice` ×3).

## 2. Le rese

| unità | inglese | resa |
|---|---|---|
| 2 | `A civilian reactor on <destination> is running low on fuel…` | «Un reattore civile su `<destination>` ha il carburante quasi esaurito e ha bisogno di una fornitura d'emergenza di `<cargo>` entro il `<date>`.» |
| 3 | `You drop off your cargo of <commodity> at the loading bay of a towering nuclear complex…` | «Scarichi il tuo carico di `<commodity>` alla baia di carico di un imponente complesso nucleare e incassi il pagamento di `<payment>`.» |
| 5 | `Syndicate techs on <destination> need a rush shipment of <tons> of specialized <commodity>…` | «I tecnici del Sindacato su `<destination>` chiedono una spedizione urgente di `<tons>` di `<commodity>` per uso specialistico entro il `<date>`.» |
| 8 | `Disable the robotic target dummy ship in <system>…` | «Disabilita la nave-bersaglio robotica in `<system>`, raccogli i dati di collaudo per gli ingegneri del Sindacato scansionandone il carico, e atterra su `<planet>`. Attenzione: la nave bersaglio è programmata per mettersi sulla difensiva…» |
| 10 | `You forgot to either disable or scan the target dummy ship in <system>!` | «Hai dimenticato di disabilitare o scansionare la nave-bersaglio in `<system>`! Dovrai tornare là e farlo prima di poter tornare qui a riscuotere.» |
| 11 | `You are hailed by an angry Syndicate official who fines you <payment>…` | «Ti contatta un funzionario del Sindacato furioso, che ti multa di `<payment>` e ti avverte che altri errori di questo tipo potrebbero escluderti da questi lavori.» |

## 3. Una missione, tre contesti

`Syndicate target practice` esiste nei contesti **`[0]`, `[1]`, `[2]`** con la **stessa prosa**: la scheda (unità 8, 14, 20)
e quattro battute (9–12, 15–18). Una sola resa per ogni stringa, verificata come **famiglia**; il gruppo più numeroso ha
**tre** copie e il controllo lo asserisce esplicitamente (`max(mult.values()) == 3`).

È il punto in cui un lotto può «sembrare» coerente e non esserlo: tre varianti lievemente diverse non spostano né le unità né
le parole.

## 4. Le scelte che non sono ovvie

| punto | decisione | perché |
|---|---|---|
| `specialized <commodity>` | **«`<commodity>` per uso specialistico»** | il nome inserito dal motore non ha genere noto: un aggettivo concordato sbaglierebbe metà delle merci |
| `rush shipment` | **«spedizione urgente»** | |
| `target dummy ship` | **«nave-bersaglio»** (scheda e battute) / **«nave bersaglio»** (seconda menzione, senza trattino) | il composto con trattino quando è il nome della cosa; forma piana nel discorso |
| `robotic target ship` | **«nave-bersaglio robotica»** | |
| `self-defense behaviors` | **«mettersi sulla difensiva»** | «comportamenti di autodifesa» è burocratese |
| `realistic simulation` | **«simulazione realistica»** | |
| `test data` | **«dati di collaudo»** | non «dati di test»: registro tecnico |
| `disables craft` | **«mezzo disabilitato»** | «craft» qui è il bersaglio, non una nave militare |
| `battle damage` | **«danni da combattimento»** | |
| `fines you <payment>` | **«ti multa di `<payment>`»** | |
| `remove you from eligibility` | **«escluderti da questi lavori»** | |
| `towering nuclear complex` | **«imponente complesso nucleare»** | |
| `loading bay` | **«baia di carico»** | coerente con L244–L246 |
| `Syndicate` | **«Sindacato»** | `Syndicated Systems` resta, se compare |

## 5. Differenze dichiarate fra le due lingue

| cosa | inglese | italiano |
|---|---|---|
| apici | **2** (unità 10 e 16: `You'll`) | **1** (unità 2: `d'emergenza`) |
| virgolette | **0** | **0** |
| tab | **0** | **0** |

Il `You'll` diventa «Dovrai» (nessun apice) e compare **una** elisione dove l'inglese non ne aveva: la differenza è
**elencata per unità**, non nascosta nel totale.

## 6. Struttura e assenze

- **32 segnaposto in 8 famiglie**, confrontati come multiset **e** per ordine dentro ogni unità.
- **`<tons>` senza articolo** e sempre seguito da «di».
- **`<commodity>` mai seguito da un aggettivo**: le tre forme misurate sono `alla`, `per`, `alla`.
- **Nessun `Syndicate` residuo** come fazione (resa «Sindacato»), e la verifica usa `\bSyndicate\b` per non colpire i nomi
  propri composti.
