# STATO — L108 · `data/korath/korath missions.txt` (**frammenti `phrase:` composti a runtime**)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L108_20261018_224456` |
| Righe / unità | **216–335** / **36** |
| Tipi | **14 `TEXT`** + **15 `MISSION_TEXT`** + **3 `VALUE`** + **3 `DESCRIPTION`** + **1 `DIALOG`** |
| `VALUE` (identici) | 15 `Package to <planet>` · 18 `Distress call from the <EDC-ship>` · 29 `Return the <EDC-ship> survivors` |
| Contesti | **4**: `kor efret small package offer` (`phrase:`), `Small Scale Delivery`, `Efreti: Distress Call 1`, `Efreti: Distress Call 2` |
| Parole | **737 EN → 730 IT** (0,991); per unità 0,62–1,73 |
| Tab · virgolette | **12** (unità 21–28, 33–36) · **18**, tutte binate |
| Token | **23** in sei famiglie (**`<EDC-ship>` 8**, `<planet>` 4, `<destination>` 3, `<payment>` 3, `<ship>` 3, `<bunks>` 2) |
| Quadre · citazioni aperte · ripetizioni | **0** · **0** · **0** |
| sha256 | `c429ddeb0b22241c…` |
| `check.py` | **33 controlli**, `FAIL totale: 0` |
| `verify.py` | **36 controlli**, exit **0** |

## Il nodo del lotto: quattordici frammenti, non quattordici frasi

Il blocco `phrase:kor efret small package offer` (unità 1–14) costruisce una frase **unendo un elemento per
casella**:

```
soggetto        Un Korath | Un Kor Efret | Un locale
verbo           con gesti ti comunica che devi | con gesti ti chiede di
oggetto         portare una piccola cassa | portare un pacco | accettare una spedizione … | portare una scatola
destinazione    a <destination> per <payment>.
frase finale    Non dovrebbe occupare spazio di rilievo sulla vostra nave. | …
```

Composizione verificata (una delle 24 possibili):

```
Un Korath con gesti ti chiede di portare un pacco a <destination> per <payment>.
Non dovrebbe occupare spazio di rilievo sulla vostra nave.
```

**I vincoli sono per casella**, e `check.py` e `verify.py` li ricalcolano ognuno per conto proprio:

| casella | unità | vincolo |
|---|---|---|
| soggetto | 1–3 | **maiuscola**, nessun punto finale |
| verbo | 4–5 | **minuscola**, chiude con `devi`/`di`, regge un infinito |
| oggetto | 6–9 | **minuscola**, **infinito in testa** (`-are`), nessun punto |
| destinazione | 10 | **inizia con `a `**, **un solo punto**, in coda |
| frase finale | 11–14 | **maiuscola** e **punto** |

Il `verify.py` compone **tutte e 24** le frasi soggetto × verbo × oggetto e verifica che nessuna produca
punteggiatura doppia, doppie maiuscole o `di di`. Un frammento con il punto al posto sbagliato produrrebbe
«…chiede di. portare…» nel gioco, e nessun conteggio totale lo rivelerebbe.

## Il resto

- **`Small Scale Delivery`** (15–17): la consegna di un pacco a un Kor Efret che attende nello spazioporto con le
  mani tese.
- **`Distress Call 1`** (18–28): il Quarg che parla in tono arcaico — «Vittime di sorte incerta esigono il vostro
  zelo più diligente, perché molte famiglie non abbiano a piangere i morti» —, i droni Mereti che hanno teso
  l'agguato alla `<EDC-ship>`, **quaranta** Korath ancora vivi, le risposte del giocatore («Non possono
  intervenire i Quarg?», «I Korath non mi interessano») e la replica finale: «La vita è rara e preziosa nella
  vastità dello spazio».
- **`Distress Call 2`** (29–36, resta aperto): le **`<bunks>` cuccette** dimenticate, il portello che si apre su
  un **fucile termico**, il comunicatore con la registrazione Quarg, la nave all'energia di emergenza, la zona
  abitativa ridotta a ospedale di fortuna e il trasbordo dei superstiti.

## Invariante di segmento

| Voce | Valore |
|---|---|
| Unità prima della riga 216 | **63** (L106+L107) |
| Unità dopo la riga 326 | **59** |
| Confine | riga **338** apre `mission:Efreti: Distress Call 2` |
| File | **158 unità**, `max(line) = 580` |
| Copertura | **99/158 (62,7%)** |

## Verifica

```bash
cd staging/editorial/L108_20261018_224456
python check.py   # FAIL totale: 0 (33 controlli)
python verify.py  # exit 0 (36 controlli)
```
