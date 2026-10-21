# STATO — L127 · `data/incipias/incipias first contact.txt` (secondo lotto: 63 unità, un contesto intero)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L127_20261019_073900` |
| Righe / unità | **224–331** / **63** — **tutto** il contesto `Help The Stranded 1` |
| Tipi | **58 `MISSION_TEXT`** · **3 `LOGBOOK`** · **1 `VALUE`** · **1 `DESCRIPTION`** |
| Stati | **63 `PENDING`** — misurato e **asserito** in `mkparts.py` |
| Contesti | **1** per tutte e 63 le unità |
| Testi distinti | **63** per 63 unità — nessuna ripetizione |
| Parole | **1697 EN → 1556 IT** (0,917); per unità 0,65–1,36, media 1,01 |
| Tab | **55 unità** su 63 con `\t` iniziale |
| Virgolette | **98** (nessuna unità con numero dispari) |
| Token | **2** — `<first>` 1, `<last>` 1, **entrambi nella sola unità 38** |
| Quadre · backtick | **0** · **0** |
| sha256 | `d811d1921f891627…` |
| `check.py` | **30 controlli**, `FAIL totale: 0` |
| `verify.py` | **28 controlli**, exit **0** — invariante di **segmento** |

## Il `VALUE` e i due token, isolati

- **`VALUE`** (unità 1): `Seek help from the Incipias` — **nome di missione**, identico al sorgente (decisione 259).
  Verificato con `VAL == [1]` e confronto stringa, non con «tutti tranne».
- **Token** (unità 38): `"Salve. Sono il capitano <first> <last>, qui per stabilire un contatto."` — parità per simbolo
  *e* per unità: il controllo verifica che i token siano solo nell'unità 38 e nello stesso ordine.

## Lo stile degli Incipias: composti con trattino

Il sorgente rende la lingua aliena con **composti legati da trattino**; la resa li riproduce con composti italiani,
scelta dichiarata e verificata:

| EN | IT |
|---|---|
| `world-traveler` | **viaggiatore-di-mondi** |
| `intention-goal` / `intention-goals` | **intenzione-scopo** / **intenzioni-scopo** |
| `capital-station` | **stazione-capitale** |
| `outer-being` | **essere-esterno** |
| `far-stranger` | **straniero-lontano** |
| `not-danger` | **non-pericolo** |
| `situation-opportunity` | **situazione-opportunità** |
| `air-planet` | **pianeta-d'aria** |
| `system-places` | **luoghi-sistema** |
| `future-time` | **futuro-tempo** |
| `out-question` | **interrogare-oltre** |

## Il Quarg parla di sé in terza persona

`this one` → **«questo uno»** (glossario, L102), **7 occorrenze**; il controllo ne pretende almeno sei. È la marca che
distingue il Quarg dai Quarg che parlano al plurale («Ti siamo grati», «ti forniremo»): entrambe le forme convivono, e
la resa le tiene distinte.

## Registri

| voce | forma | esempio |
|---|---|---|
| **Quarg** (singolo) | cerimoniale, terza persona | «Felice è questo uno che tu accetti quella condizione.» |
| **Quarg** (collettivo) | prima persona plurale | «Nessuno li danneggerà senza incorrere nella nostra ira.» |
| **Incipias** | composti, misurato, senza articoli davanti ai composti | «Qual è la tua intenzione-scopo qui?» |
| **Narrazione** | presente, «tu» | «Appena arrivi sul pianeta cerchi un Quarg che parli la tua lingua.» |

## Verifica

```bash
cd staging/editorial/L127_20261019_073900
python mkparts.py   # 63 unità · 62 prosaici + 1 VALUE identico · 1 contesto · 55 tab · 98 virgolette · 2 token
python check.py     # FAIL totale: 0 (30 controlli)
python verify.py    # exit 0 (28 controlli)
```

**Errore di misura corretto**: la prima stesura diceva «39 unità dopo la riga 331»; sono **43** (161 − 55 di L126 −
63 di L127). Corretto in `verify.py` e nei tre documenti a contratto.
