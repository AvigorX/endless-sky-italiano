# STATO — L149 · `coalition jobs.txt` (scambi interspecie e trasferimenti)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L149_20261019_180512` |
| Righe / unità | **455–634** / **18** — file al **32,5%** (64/197) |
| Tipi | **8 `VALUE`** (identici) · **8 `DESCRIPTION`** · **2 `TEXT`** |
| `LOGBOOK` · `DIALOG` · `UI_LABEL` | **0** · **0** · **0** — asserzioni vuote |
| Token | **36** su **4** simboli, con **due coppie di conteggi uguali** |
| Stati | **18 `PENDING`** — misurato e **asserito** |
| Contesti | **10** |
| Testi | **8 distinti** su 18 unità |
| Parole | **246 EN → 268 IT** (1,089); per unità **0,88–1,18**, media **1,06** |
| Tab · virgolette | **0** · **0** |
| sha256 | `b5f2ed112da6516f…` |
| `check.py` | **31 controlli**, `FAIL totale: 0` |
| `verify.py` | **25 controlli**, exit **0** — invariante di **segmento** |

## Il caso in cui il multiset è cieco

| simbolo | conteggio |
|---|---|
| `<planet>` | **10** |
| `<payment>` | **10** |
| `<bunks>` | **8** |
| `<destination>` | **8** |

Scambiare `<planet>` con `<payment>` non cambierebbe **nessun totale**. Per questo il controllo che conta è l'**ordine
dei simboli per unità**: `TAGS.findall(italiano) == TAGS.findall(inglese)` su tutte e 18, più due conteggi nominati per
simbolo. Il multiset resta, ma da solo sarebbe una rassicurazione falsa.

## Due frasi vengono da fuori, e una no

| stringa | provenienza | esito |
|---|---|---|
| `As part of the Interspecies Exchange Program…` | **identica** a L148 unità 16 | **resa riletta** da L148, uguale per costruzione |
| `You drop off the workers on <planet>…` | **diversa** da L147 (`on **the** <planet>`) | **resa nuova**: «su `<planet>`», non «sul `<planet>`» |

La seconda è la trappola: sembrava la stessa frase, e il `mkparts.py` l'ha **rifiutata** (asserzione: la variante
senza «the» non deve esistere in L147). Riusare la resa di L147 avrebbe prodotto «sul `<planet>`» dove il sorgente dice
solo «su `<planet>`».

## Un controllo fittizio sostituito

Nel `check.py` avevo scritto una `ck(...)` con `or True` per la differenza con L147: non verificava nulla. Sostituita
con un'asserzione vera — la stringa di L149 **non è una chiave** di L147, mentre la variante con «the» **lo è**.

## Verifica

```bash
cd staging/editorial/L149_20261019_180512
python mkparts.py   # 18 unità · 8 VALUE + 8 DESCRIPTION + 2 TEXT · 36 token · 1 frase riletta
python check.py     # FAIL totale: 0 (31 controlli)
python verify.py    # exit 0 (25 controlli, invariante di segmento)
```

**Non verificato**: nessuna missione giocata; i tre livelli dei turisti non sono stati visti a schermo.
