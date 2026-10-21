# STATO — L137 · `data/starts.txt` (terzo inizio: `Escaping Squalor`)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L137_20261019_140902` |
| Righe / unità | **172–210** / **17** — file al **56,6%** (64/113) |
| Tipi | **10 `CONVERSATION`** · **4 `LOGBOOK`** · **2 `DESCRIPTION`** · **1 `VALUE`** (`Escaping Squalor`) |
| `UI_LABEL` · token | **0** · **0** — due asserzioni vuote scritte |
| Stati | **17 `PENDING`** — misurato e **asserito** |
| Contesti | **2 completi** — `start:syndicate` 3, `conversation:syndicate intro` 14 |
| Testi | **12 propri + 5 riletti** da L135 (unità 5–9), **17 distinti** |
| Parole | **802 EN → 786 IT** (0,980); per unità 0,85–1,28, media 1,04 |
| Tab · virgolette | **8 unità** · **12** (6:2, 11:2, 13:2, **14:4**, 17:2), nessuna dispari |
| sha256 | `24133aaf9c9f177d…` |
| `check.py` | **29 controlli**, `FAIL totale: 0` |
| `verify.py` | **28 controlli**, exit **0** — invariante di **segmento** |

## Il primo inizio «difficile»

`start:syndicate` è dichiarato tale dal gioco stesso: «È un inizio più difficile, con rate giornaliere più alte». E i
numeri lo dicono meglio di un aggettivo: **600.000 crediti** al **0,5%** giornaliero, **3.580** al giorno per un anno,
**706.571** di soli interessi — *più del prestito*. Sono i numeri del sorgente: la resa li riporta tutti e cinque in
convenzione italiana, con un controllo che **vieta** le forme inglesi (`600,000`, `0.5%`, `3,580`, `706,571`,
`480,000`).

## Cinque condivise, ancora rilette

Le unità **5–9** sono le stesse di L135 e L136. Non ricopiate: rilette dal `translation.json` di L135, con l'inglese
confrontato prima della resa e la resa confrontata dopo.

## La cortesia dentro la battuta

Il cassiere dà del **lei** al giocatore («Come possiamo aiutarla?»), e la narrazione resta al **tu**. Il controllo sulla
cortesia è stato scritto apposta per tollerare **al massimo una** forma, e a verificare che non si propaghi fuori dal
dialogo: la narrazione dice «Dici che ti serve un prestito», non «dice che le serve».

## I nomi

| EN | IT | nota |
|---|---|---|
| `Escaping Squalor` | **identico** | nome dell'inizio (`VALUE`) |
| `Earth` | **Terra** | come nel resto dello staging |
| `Antipode` · `Delve` | **Antipode** · **Delve** | pianeti: restano |
| `Syndicated Systems` | **Syndicated Systems** | nome del prodotto: resta |
| `Dirt Belt` | **Dirt Belt** | regione: resta |

## Verifica

```bash
cd staging/editorial/L137_20261019_140902
python mkparts.py   # 17 unità · 12 proprie + 5 rilette · 2 contesti completi · 8 tab · 12 virgolette
python check.py     # FAIL totale: 0 (29 controlli)
python verify.py    # exit 0 (28 controlli, invariante di segmento)
```

**Non verificato**: nessun inizio avviato nel gioco, nessuna rata pagata.
