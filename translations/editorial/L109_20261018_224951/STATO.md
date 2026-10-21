# STATO — L109 · `data/korath/korath missions.txt` (**recuperare i morti**, `<origin>` contro `<destination>`)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L109_20261018_224951` |
| Righe / unità | **338–451** / **33** |
| Tipi | **27 `MISSION_TEXT`** + **3 `VALUE`** + **3 `DESCRIPTION`** |
| `VALUE` (identici) | 4 `Recover the fallen crew of the <EDC-ship>` · 16 `Recover the fallen of <EDC-ship>` · 29 `<EDC-ship> salvage team` |
| `DESCRIPTION` (tradotte) | 5 · 17 · 30 |
| Contesti | **4**: `Efreti: Distress Call 2` (coda), `3`, `4`, `5` |
| Parole | **1205 EN → 1188 IT** (0,986); per unità 0,89–1,28 |
| Tab · virgolette | **20** · **14**, tutte binate |
| Token | **23** in sette famiglie (**`<EDC-ship>` 11**, `<destination>` 4, **`<origin>` 2**, `<planet>` 2, `<bunks>` 2, `<ship>` 1, `<payment>` 1) |
| Quadre · citazioni aperte | **0** · **0** |
| sha256 | `6e60f04cc8291cb4…` |
| `check.py` | **30 controlli**, `FAIL totale: 0` |
| `verify.py` | **33 controlli**, exit **0** |

## `<origin>` non è `<destination>`

Il token nuovo di questo lotto sta in **tre** unità e significa cose opposte:

| unità | testo | dove va |
|---|---|---|
| 5 | **Recupera i corpi … su `<destination>` e riportali a `<origin>`.** | corpi **presi** su `<destination>`, **riportati** a `<origin>` |
| 8 | **… di tornare su `<planet>` e di riportare i loro perduti a casa, su `<origin>`.** | viaggio di ritorno alla base |
| 17 | **Riporta i corpi … su `<planet>`.** | variante senza `<origin>` |

Scambiarli rovescia la missione: il giocatore andrebbe al pianeta di partenza a cercare i corpi. Il `check.py` e il
`verify.py` confrontano `<origin>` e `<destination>` **per unità**, non solo nel totale — un totale corretto con i
due token scambiati fra loro passerebbe.

## Tre quasi-duplicati, nessuna ripetizione

| gruppo | differenza | resa |
|---|---|---|
| 20 / 21 / 22 | chi raccoglie i corpi: **il resto dell'equipaggio** / **voi** / **uno alla volta** | tre frasi distinte, stesso nucleo («covata di uova in un nido») |
| 18 / 19 | c'è l'equipaggio o si è soli | coda diversa: «con le tute» contro «senza nessuno del vostro equipaggio ad aiutarvi» |
| 24 / 25 | «L'equipaggio fa un ultimo giro» / «Per precauzione, fate un ultimo giro» | stessa azione, registro diverso |

Nessuna delle tre coppie è identica al sorgente, quindi **zero ripetizioni** — ma le tre varianti vanno tenute
distinte anche in italiano, e il `check.py` lo verifica sull'apertura o sulla coda di ciascuna.

## Il resto

- **`Distress Call 2`** (1–3): l'evacuazione, i tre morti durante il volo, il messaggio dei Quarg — «Umano audace!
  Con copiosa gratitudine vi ricompensiamo…» — e la frase che dà il tono all'arco: «agli Efreti si ricorda perché
  vivono pigiati intorno a queste poche stelle».
- **`Distress Call 3`** (4–15): la delegazione in abiti migliori, l'ologramma del Quarg, i **principi del clan**,
  e il rifiuto («Non rischio la mia nave per i morti») che fa afflosciare il capo. Poi la proposta: «Vi offriamo il
  titolo per recuperare la `<EDC-ship>` e per portare il nostro lutto lontano da qui».
- **`Distress Call 4`** (16–28): le tute ambientali, le **bare fibrose a forma di uovo** che «si incastrano
  insieme come una covata di uova in un nido», gli effetti personali e le fotografie («non avete modo di sapere se
  i Korath delle fotografie … giacciano nella vostra stiva»), lo sbarco fra la folla che «scoppia in una cacofonia
  di suoni che abbaiano», e i **66 membri d'equipaggio** da trovare: «il sistema più vicino … è su Greenwater, nello
  spazio Hai».
- **`Distress Call 5`** (29–33): la squadra di recupero da assoldare, `<bunks>` cuccette libere, e gli Hai che
  «non hanno il coraggio» di toccare una nave finita nel fuoco incrociato fra Mereti e Sestor.

## Invariante di segmento

| Voce | Valore |
|---|---|
| Unità prima della riga 338 | **99** (L106+L107+L108) |
| Unità dopo la riga 451 | **26** |
| Confine | riga **474** apre `mission:Efreti: Distress Call 6` |
| File | **158 unità**, `max(line) = 580` |
| Copertura | **132/158 (83,5%)** |

## Verifica

```bash
cd staging/editorial/L109_20261018_224951
python check.py   # FAIL totale: 0 (30 controlli)
python verify.py  # exit 0 (33 controlli)
```
