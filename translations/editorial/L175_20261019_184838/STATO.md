# STATO — L175 · `avgi ships.txt` (Phononos, Frequentia, Polari, Entasi — e un nome che non si traduce)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L175_20261019_184838` |
| Righe / unità | **526–885** / **10** — file al **24/102 (23,5%)** |
| Tipi | **7 `DESCRIPTION`** · **2 `TEXT`** · **1 `VALUE`** |
| `UI_LABEL` · token | **0** · **0** — due asserzioni vuote scritte |
| Contesti | **4** (2 + 2 + 3 + 3) · **9 testi distinti** su 10 |
| Parole | **490 EN → 504 IT** (1,029) · rapporto DESCRIPTION **1,06–1,23**, media **1,13** |
| Tab · virgolette | **3** (idx 3, 8, 10) · **4** (idx 4 e 6) |
| Apici | **3**, tutti in idx 5 (`fleet's`, `bay's`, `can't`) · **nessun possessivo in italiano** |
| sha256 | `0bb78b20aa2af987…` |
| Esiti | `check.py` **24** (`FAIL 0`) · `verify.py` **22**, exit **0** |

## La novità: un `TEXT` che è un NOME

Le due unità `TEXT` (idx 4 e 6, nei contesti `Frequentia` e `Polari`) contengono **`Z-333 "Spark" Fusion Torch`**: è il
nome di un motore, **non prosa**. Resta **identico al sorgente**, e le **4 virgolette** del lotto sono tutte lì (2 + 2).
Un controllo pretende l'uguaglianza carattere per carattere; un altro impedisce che un possessivo inglese (`'s`) resti
in italiano.

## Cosa contiene

| nave | unità | righe | contenuto |
|---|---|---|---|
| `Phononos` | 1-3 | 526-586 | retrofit di un `Photikon` dismesso, mercantile automatizzato, convogli |
| `Frequentia` | 4-5 | 623-658 | nave rifornitrice di deuterio criogenico, la porta di stiva proverbialmente stretta |
| `Polari` | 6-8 | 705-746 | ricognitore scientifico, laboratorio, droni `Optikon`, `Akoustiki Excursion Vehicle` |
| `Entasi` | 9-10 | 884-885 | nave mineraria, generatori solari termici, droni cargo `Sonikis` |

## Nomi rimasti in inglese

`Phononos`, `Photikon`, `Frequentia`, `Polari`, `Entasi`, `Avlaki`, `Harmonikos`, `Optikon`,
`Akoustiki Excursion Vehicle`, `Sonikis`, `Dissonance`, `Aberrant`, `Twilight Guard`, `Avgi`.

## Verifica

```bash
cd staging/editorial/L175_20261019_184838
python check.py     # FAIL totale: 0 (24 controlli)
python verify.py    # exit 0 (22 controlli)
```

**Non verificato**: nessuna astronave vista a schermo; i testi non sono stati caricati nel gioco.
