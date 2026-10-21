# L41 — rapporto del lotto

`data/human/free worlds war jobs.txt` · righe **16–927** · lotto `L41_20261018_153942` ·
**72/72 unità** · ventunesimo file completo dello staging · chiuso il 2026-10-18.

## Numeri

| voce | valore |
|---|---|
| unità | **72 / 72** (file completo) |
| parole | 1.124 EN → **1.140 IT** (1,014) |
| contesti | 34 (`free worlds scanner payment` … `FW Bulk Refugees [0]`) |
| parti | 2 — 40, 32 |
| tab | **0 = 0** |
| virgolette | **0 = 0** |
| token `<...>` | **172 = 172** (10 famiglie) |
| quadre `[` `]` | **0 unità** (asserito) |
| rapporto per unità | 0,81 – 1,25 |
| `check.py` | **FAIL totale: 0** (22 controlli) |
| `verify.py` | **30 controlli**, exit 0, `FAIL: 0` |
| sha256[:16] | `translation.json` `17727c643c46cd38` · `source.json` `2d80ef7e236ca99e` · `check.py` `271ae4de36299aa1` · `verify.py` `b5b4874cdaa51d1d` |

Il file parte dalla riga **16**; il `verify.py` asserisce `(first, last) == (16, 927)`.

## Tipi

29 `VALUE` · 29 `DESCRIPTION` · 8 `DIALOG` · **6 `TEXT`** · **0 `UI_LABEL`** · 0 `CONVERSATION` ·
0 `LOGBOOK`.

I 6 `TEXT` sono testi di `phrase`: compaiono nel `raw` fra backtick (`` `...` ``) e vanno tradotti come
una frase, senza toccare la cornice.

## Unità non traducibili (`NT`)

**Nessuna.** Il file non contiene `UI_LABEL`, quindi nessuna `label` di salto da lasciare in inglese.
Il `verify.py` lo asserisce come assenza (`ui == []`), non come omissione.

## Le 10 famiglie di token

| token | volte |
|---|---|
| `<planet>` | 46 |
| `<payment>` | 35 |
| `<date>` | 29 |
| `<destination>` | 28 |
| `<cargo>` | 11 |
| `<commodity>` | 7 |
| `<bunks>` | 6 |
| `<tons>` | 6 |
| `<waypoints>` | 3 |
| `<npc>` | 1 |

172 token su 72 unità: è la densità più alta della serie, e la ragione è strutturale — i lavori di
guerra sono testi parametrici, generati per pianeta, data, paga e carico.

## Controlli eseguiti

`check.py` (22 controlli): copertura, unità vuote, `NT`, duplicati italiano spiegati dal sorgente, tab
per unità e come totale, virgolette per unità e come totale, quadre per unità, token `<...>`, backtick,
spazi iniziali/finali e doppi, rapporto lunghezze, tipografia, caratteri non latini, parole inglesi
residue, stato del database.

`verify.py` (30 controlli): riga grezza contro il file sorgente, `english`/`kind`/`path` contro
`state.db`, stato `PENDING`, id univoci e ordine, collocazione **16–927**, copertura totale 72/72 da un
solo lotto, distribuzione dei kind, `NT` vuoto (asserzione di assenza), **6 `TEXT`** tradotte e senza
backtick nell'italiano, tab e virgolette a zero in entrambe le lingue, token, insieme delle virgolette
dispari (vuoto in entrambe le lingue), italiano non vuoto, caratteri non latini, trattini lunghi,
rapporto, e ricostruzione di `translation.json` dalle 2 parti.

## Duplicati

17 gruppi di inglese identico per **64 unità su 72**. Sono lavori ripetuti per sistema: dove l'inglese è
identico l'italiano è identico, e dove l'inglese differisce per una parola l'italiano differisce:

| unità | differenza inglese | differenza italiana |
|---|---|---|
| 27 / 28 | `captain` / `captains` | «Un capitano» / «I capitani» (verbo al plurale) |
| 57 / 59 | `Free Worlds` / `Free Worlds` (identici) | identici |
| 61 / 63 | `Republic` / `Republic` (identici) | identici |
| 57 / 61 | `Free Worlds` / `Republic` | «delle Free Worlds» / «della Repubblica» |
| 30 / 34 … 40 | con `/` senza `a <destination>` | con `/` senza «a <destination>» |

## Nota di inventario

Il file **non ha righe `log`**: 0 `LOGBOOK`, quindi nessuna lacuna di inventario possibile. È l'unico
lotto della serie in questa condizione (misura, non assenza di controllo).

## Non fatto (dichiarato)

- Nessuna approvazione nel database: 72 unità `PENDING`.
- Nessun caricamento nel gioco, nessuna verifica a schermo dei titoli nella lista lavori.
- Nessun test di gameplay dei lavori di guerra.
