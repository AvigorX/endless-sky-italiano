# STATO — L199 · `hai jobs.txt` (quarto lotto)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L199_20261019_203531` |
| Righe / unità | **1579–1750** / **26** — file al **152/175 (86,9%)** |
| Tipi | {'VALUE': 9, 'DESCRIPTION': 8, 'DIALOG': 9} |
| Tab · virgolette · apici | **0** · **0** · **2 EN / 0 IT** |
| Segnaposto | **42** su **3** simboli — 17 `<payment>` · 17 `<planet>` · 8 `<bunks>` |
| Contesti | **10** — da `Swiftsong Business Convention [2]` a `Superstitious Hai [1]` |
| Parole | **489 EN → 488 IT** (rapporto 0,89–1,22, media 1,03) |
| sha256 | `6af91de2eec66a88…` |
| Esiti | `check.py` **28** (`FAIL 0`, exit 0) · `verify.py` **21** (`FAIL: 0`, exit 0) |

## Cosa contiene

| blocco | unità | righe | contenuto |
|---|---|---|---|
| convention [2] | 1 | 1579 | l'arrivo: resa **identica** a quella di L198 (stessa stringa) |
| festival del cinema | 2–7 | 1586–1621 | `[1]` e `[2]`: trame sconcertanti |
| festival musicale | 8–13 | 1628–1663 | `[1]` e `[2]`: la musica si sente dallo spazioporto |
| conferenza sicurezza informatica | 14–19 | 1670–1705 | `[1]` e `[2]`: conversazioni sopra la testa |
| convention di fantascienza | 20–25 | 1711–1746 | `[1]` e `[2]`: un gesto da vecchia serie |
| `Superstitious Hai [1]` | 26 | 1750 | il `VALUE` che apre la missione che continua in L200 |

## Difficoltà

1. **Quattro famiglie × due taglie**: le coppie `[1]`/`[2]` differiscono **solo** per `grande`. Il controllo lo verifica togliendo `grande` e confrontando le stringhe, non a occhio.
2. **Quattro `DIALOG` in coppia identica** (4=7, 10=13, 16=19, 22=25): il rischio è tradurre due volte la stessa battuta con due rese.
3. **Il confine non chiude la missione**: l'unità 26 (riga 1750, `VALUE` di `Superstitious Hai [1]`) e la prima di L200 (riga 1753, `DESCRIPTION` della **stessa** missione) sono contigue. Il `verify.py` confronta i contesti invece di assumere la separazione.
4. **Apici asimmetrici**: 2 inglesi (`passengers'`) contro 0 italiani — il possessivo inglese non ha equivalente con apostrofo.
5. **Solo tre simboli** e nessuno nuovo; `<date>`, `<cargo>`, `<destination>` spariscono rispetto a L198 (asserzione vuota scritta).

## Verifica

```bash
cd staging/editorial/L199_20261019_203531
python check.py     # FAIL totale: 0 (28 controlli)
python verify.py    # FAIL: 0 · exit 0 (21 controlli)
```

**Non verificato**: nessun lavoro accettato nel gioco, nessuna schermata vista, nessuna revisione umana; le 26 unità restano `PENDING`.
