# STATO — L200 · `hai jobs.txt` (quinto lotto: **chiude il file, 175/175**)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L200_20261019_204235` |
| Righe / unità | **1753–2067** / **23** — file al **175/175 (100%)** |
| Tipi | {'VALUE': 11, 'DESCRIPTION': 12} — nessun `DIALOG` |
| Tab · virgolette · apici | **0** · **0** · **0** (in entrambe le lingue) |
| Segnaposto | **57** su **5** simboli — 12 `<payment>` · 12 `<destination>` · 12 `<date>` · 11 `<planet>` · 10 `<bunks>` |
| Contesti | **12** — `Superstitious Hai [1]` … `[12]`, in ordine |
| Parole | **354 EN → 422 IT** (rapporto 1,00–1,22, media 1,09) |
| sha256 | `3ff06bf4f8b326c1…` |
| Esiti | `check.py` **25** (`FAIL 0`, exit 0) · `verify.py` **17** (`FAIL: 0`, exit 0) |

## Cosa contiene

Un'unica famiglia numerata: dodici `Superstitious Hai`, ognuna con un `VALUE` (il nome del lavoro) e una
`DESCRIPTION` (chi parte, dove, entro quando).

| blocco | unità | righe | soggetto |
|---|---|---|---|
| `[1]` e `[7]` | 1–2 / 13–14 | 1753–1777 / 1921–1948 | la matriarca con la sua famiglia |
| `[2]` e `[8]` | 3–4 / 15–16 | 1780–1805 / 1951–1976 | allevatori |
| `[3]` e `[9]` | 5–6 / 17–18 | 1808–1835 / 1979–2006 | un anziano diretto alla casa di riposo |
| `[4]` e `[10]` | 7–8 / 19–20 | 1838–1864 / 2009–2035 | braccianti |
| `[5]` e `[11]` | 9–10 / 21–22 | 1867–1893 / 2038–2064 | anziani in vacanza |
| `[6]` e `[12]` | 11–12 / 23 | 1896–1921 / 2067 | una famiglia Hai |

## Difficoltà

1. **Lotto terminale**: il `verify.py` usa l'**invariante di FILE** sulle cinque finestre L196…L200 = **175/175**
   unità su 175 righe distinte, lette dai `translation.json` e non dai numeri del contratto.
2. **Sei coppie con/senza keystone**: le `[1]…[6]` portano in coda la frase sul keystone, le `[7]…[12]` sono le
   stesse **senza**. Il controllo toglie la frase dalle prime e confronta con le seconde, una per una.
3. **Accordo del verbo**: «Ha chiesto» per matriarca e anziano (soggetto singolare), «Hanno chiesto» per famiglie e
   gruppi. La frase condivisa non è identica carattere per carattere, ed è corretto: il controllo accetta le due forme.
4. **Un solo termine per `keystone`**: in staging convivono «chiave di volta» (22) e «pietra chiave» (13). Il lotto usa
   **solo** «chiave di volta» (18 occorrenze) e il controllo pretende che «pietra chiave» non compaia.
5. **Zero tab, zero virgolette, zero apici**: tre asserzioni vuote, scritte comunque.

## Verifica

```bash
cd staging/editorial/L200_20261019_204235
python check.py     # FAIL totale: 0 (25 controlli)
python verify.py    # FAIL: 0 · exit 0 (17 controlli) — FILE CHIUSO 175/175
```

**Non verificato**: nessun lavoro accettato nel gioco, nessuna schermata vista, nessuna revisione umana; le 23 unità restano `PENDING`.
