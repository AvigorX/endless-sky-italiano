# STATO — L327 (`data/_ui/help.txt`, righe 15–69) — **PRIMO DI TRE LOTTI**

**Stato: CHIUSO.** 28 unità, **14 contesti**. `check.py` esce 0 con **20 controlli**; `verify.py` esce 0 con **14 controlli**.
`state.py` esce 0 (`ESITO: OK`, 8/8). **Nessuna scrittura su `state.db`** (verificato anche dal **mtime**: il database è più vecchio di
`translation.json`).

## ⚠️ Il lotto NON è una traduzione: è una **trascrizione di testo approvato**

Le ventotto unità della finestra 15–69 sono **già `APPROVED`** nel database, con il testo italiano nella colonna `italian`. Il lotto
prende quel testo come **autorità**, lo porta in staging e lo verifica.

| voce | valore |
|---|---|
| directory | `staging/editorial/L327_20261020_232043/` |
| file | `data/_ui/help.txt` (**113 unità** · righe 15–212 · **68 `APPROVED` + 45 `PENDING`**) |
| righe | 15–69 (**prima parte**: 28 di 113 unità) |
| unità | **28 `HELP`** — **tutte `APPROVED`** |
| contesti | **14** — due terzine, dieci coppie, due singoli |
| parole | **1.138 EN → 1.043 IT** (0,917) |
| rapporto | **0,82 – 1,38** |
| tab | **0** |
| virgolette | **12** su quattro righe (19, 20, 24, 45) |
| segnaposto | **5 forme, 14 occorrenze** |
| `check.py` | **20 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **14 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di SEGMENTO**: 28 unità proprie nella finestra, nessun altro lotto sulle stesse righe, confine alla **72** |
| `sha256[:16]` | **`fbe829e6548efe43`** |

## Il primo tentativo: 25 divergenze su 28, tutte mie

Avevo tradotto le 28 unità in modo indipendente e solo **3** coincidevano con il testo approvato. Le differenze non erano refusi ma
**scelte lessicali diverse**:

| riga | testo approvato | la mia versione |
|---|---|---|
| 15 | «nuovi **mutui** … rate del **mutuo**» | «nuove **ipoteche** … rate dell'**ipoteca**» |
| 19 | «migliaia, milioni, miliardi e **trilioni**» | «… e **bilioni**» |
| 27 | «La tua nave è appena stata **neutralizzata**!» | «… **disabilitata**!» |
| 36 | «Accettare **incarichi** … bacheca degli **incarichi**» | «Accettare **lavori** … bacheca dei **lavori**» |
| 38 | «dare la caccia ai **ricercati**» | «la caccia alle **taglie**» |
| 24 | «clicca su "**Gestisci piloti**" e su "**Entra nella nave**"» | «clicca su "**Manage Pilots**" e su "**Enter Ship.**"» |
| 45 | «clicca su "**Preferenze**" … clicca su "**Manuale**"» | «"**Preferences**" … "**Manual.**"» |

**Il testo approvato vince**, per definizione: è passato per una revisione. Il lotto lo adotta **alla lettera**, e il controllo centrale
(`check.py`, `verify.py`) confronta **unità per unità** con la colonna `italian` del database.

## Due convinzioni sbagliate, corrette dai fatti

1. **«Le etichette dell'interfaccia restano in inglese».**
   Il testo approvato le **traduce**: «Gestisci piloti», «Entra nella nave», «Preferenze», «Manuale». Le 630 unità `UI_LABEL` **in
   attesa** sono un'altra cosa: sono le etichette **dentro `_ui/tooltips.txt`** (615 `PENDING` su 667), non le citazioni dentro la prosa
   di aiuto. La regola giusta è: **una citazione di interfaccia si traduce come il resto della prosa**, e solo dove il testo la mette fra
   virgolette si conservano le virgolette.
2. **«Le 364 unità `APPROVED` sono ferme e non ci riguardano».**
   Vivono in **tre file**: `_ui/interfaces.txt` (**244**, tutte approvate), `_ui/help.txt` (**68** su 113), `_ui/tooltips.txt` (**52**
   su 667). Un lotto precedente aveva già trascritto le **52** dei tooltips, e un controllo su tutto lo staging conferma che le **80**
   unità approvate già presenti sono **identiche** al testo del database (**80 su 80**, zero divergenze). L327 aggiunge le 28 di `help`.

## Cosa il test pretende

| oggetto | verifica |
|---|---|
| principale | **28/28** identiche alla colonna `italian` del database |
| stato | **28 `APPROVED`**, nessun cambio di stato |
| segnaposto | **14** in **5 forme**, e **per unità** gli stessi del sorgente: `<Show main menu>` non diventa `<Mostra menu principale>` |
| virgolette | **12** su quattro righe; le etichette **tradotte** presenti |
| numeri | «100 crediti al giorno», «K, M, B e T», «100.000 crediti» |
| comica | la scala dei `lost`: «Il Tao che può essere detto non è il vero Tao», «davvero, davvero scarso», chiusura su «tace...» |
| SEGMENTO | 28 righe distinte, prima 15, ultima 69, **nessun altro lotto** sulle stesse righe, confine **72** |
| database | **nessuna scrittura**: `mtime(state.db) < mtime(translation.json)` |

## Limiti dichiarati

- **Il testo non è mio**: è quello approvato nel database, trascritto. Il valore del lotto è la **verifica strutturale** (segnaposto,
  virgolette, numeri) e la **documentazione**, non una nuova resa.
- **Copertura parziale dichiarata**: **28 su 113** unità del file. Restano **85** unità: **40 approvate** (righe 72–116 e parte di
  119–212) e **45 `PENDING`**.
- **Nessun testo visto nel gioco**.
