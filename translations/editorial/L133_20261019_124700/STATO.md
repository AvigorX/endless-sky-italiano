# STATO — L133 · `unfettered side missions.txt` (secondo lotto: 67 unità, la consegna e il duello)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L133_20261019_124700` |
| Righe / unità | **237–477** / **67** |
| Tipi | **50 `MISSION_TEXT`** · **9 `DIALOG`** · **2 `VALUE`** · **2 `DESCRIPTION`** · **2 `LOGBOOK`** · **2 `UI_LABEL`** |
| Stati | **67 `PENDING`** — misurato e **asserito** |
| Contesti | **2** — 10 / 57 |
| Testi distinti | **64** per 67 unità |
| Parole | **2007 EN → 1821 IT** (0,907); per unità 0,80–1,57, media 1,04 |
| Tab | **34 unità** su 67 |
| Virgolette | **98** — distribuzione **18 / 44 / 1 / 3 / 1** (0, 2, 4, 1, 3 virgolette) |
| Token | **8** in **6 famiglie**: `<planet>` 2, `<date>` 2, `<destination>` 1, `<last>` 1, `<payment>` 1, `<system>` 1 |
| sha256 | `c214c835e561be8e…` |
| `check.py` | **31 controlli**, `FAIL totale: 0` |
| `verify.py` | **32 controlli**, exit **0** — invariante di **segmento** |

## Il record delle virgolette

**98 virgolette in 67 unità**, con una distribuzione che il totale da solo non rivelerebbe:

| virgolette per unità | unità |
|---|---|
| 0 | **18** |
| 2 | **44** |
| 4 | **1** |
| 1 | **3** (47, 48, 65) |
| 3 | **1** (64) |

Le quattro unità **dispari** sono battute che il sorgente apre e non chiude (o apre due e ne chiude una): la resa le
riproduce esattamente (`[1, 1, 3, 1]`), e il controllo verifica la sequenza, non solo la somma.

## `VALUE`, `UI_LABEL` e i token nuovi

- **`VALUE`** (1, 11): `Heritage Reclaimed` · `Ancient Claim` — nomi di missione, **identici**.
- **`UI_LABEL`** (40, 44): `too many ships` — **lo stesso nome di nodo due volte**, identico in entrambe.
- **`<date>`** (2, 3) e **`<system>`** (12): famiglie di token che in questo file compaiono **per la prima volta**; la
  parità è verificata per unità.

## L'incoerenza del sorgente, riprodotta

Il `LOGBOOK` (unità 10) dice **`food shipment`** — «carico urgente di **cibo**» — mentre il testo della missione
(unità 9) parla di **`medical supplies`**, «**forniture mediche**». Le due rese sono fedeli a ciascuna frase, e il
controllo lo verifica **entrambe**: correggere l'una con l'altra sarebbe un'invenzione.

## Contenuto

- **`Hai Legacy 2`** (1–10): il `VALUE`, il `DESCRIPTION` con la scadenza, il carico già assegnato, il messaggio «porta
  l'Anomalocaris», gli Unfettered che smettono di sparare, i tre esiti (in ritardo, senza Anomalocaris, riuscito) e il
  pagamento con il ringraziamento.
- **`Hai Legacy 3`** (11–67): il `VALUE` e il `DESCRIPTION` del duello, **Mera** l'ingegnere, la sfida pubblica, le
  regole implicite spiegate dal capo, il decollo con la sola Anomalocaris, i forfait (troppe navi, flotta in orbita,
  relitto non in uso), il duello, la sconfitta, la distruzione della `Lightning Bug`, e il congedo con
  l'autorizzazione ad atterrare.

## Verifica

```bash
cd staging/editorial/L133_20261019_124700
python mkparts.py   # 67 unità · 64 testi distinti · 98 virgolette · 8 token in 6 famiglie
python check.py     # FAIL totale: 0 (31 controlli)
python verify.py    # exit 0 (32 controlli)
```
