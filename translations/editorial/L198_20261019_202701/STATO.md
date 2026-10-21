# STATO — L198 · `hai jobs.txt` (terzo lotto, il più grande)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L198_20261019_202701` |
| Righe / unità | **988–1565** / **51** — file al **126/175 (72,0%)** |
| Tipi | {'VALUE': 22, 'DESCRIPTION': 24, 'DIALOG': 5} |
| Tab · virgolette · apici | **0** · **2** (nel `VALUE` `Hai "prison" cruise`) · **1 EN / 3 IT** |
| Segnaposto | **112** su **7** simboli — 29 `<payment>` · 28 `<planet>` · 21 `<destination>` · 19 `<cargo>` · 8 `<date>` · 5 `<bunks>` · 2 `<tons>` |
| Contesti | **25** — da `Transport Hai farmers to <planet>` a `Swiftsong Business Convention [2]` |
| Parole | **472 EN → 481 IT** (rapporto 0,91–1,17, media 1,05) |
| sha256 | `7465d06d0b238ebf…` |
| Esiti | `check.py` **29** (`FAIL 0`, exit 0) · `verify.py` **21** (`FAIL: 0`, exit 0) |

## Cosa contiene

| blocco | unità | righe | contenuto |
|---|---|---|---|
| mestieri Hai | 1–5 | 988–1040 | contadini, operai tessili, operai di fabbrica: trovare lavoro su un altro mondo |
| Hai Cargo [0]–[4] | 6–15 | 1045–1147 | cinque consegne semplici, `Delivery to <planet>` |
| Hai Bulk Delivery [0]–[2] | 16–27 | 1170–1324 | tre consegne all'ingrosso, stesso testo |
| Hai Rush Delivery [0]–[3] | 28–35 | 1328–1399 | quattro consegne urgenti con `<date>` |
| Hai Large Rush Delivery [0]–[3] | 36–43 | 1418–1492 | altre quattro urgenti, taglia grande |
| «prigionia» | 44–46 | 1514–1535 | `Hai "prison" cruise`: due virgolette, una cella, un pagamento |
| Swiftsong Business Convention | 47–51 | 1542–1565 | due `VALUE`, due `DESCRIPTION` identiche, un `DIALOG` |

## Difficoltà

1. **Due template dominano il lotto**: `Deliver <cargo> to <destination>…` **11 copie**, `…by <date>…` **8 copie**. Il `check.py` verifica le famiglie come famiglie (indici attesi + una sola resa), non unità per unità.
2. **Rese precedenti concorrenti**: per quelle due stringhe in staging esistono **tre** e **due** varianti (`a`/`su <destination>`, `pagamento`/`compenso`). La scelta è dichiarata: `su <destination>` + `Il pagamento è`, coerente con L196–L197 dello stesso file e con una delle rese esistenti.
3. **`operai tessili`** (unità 2): resa **unica** già in staging, riusata alla lettera; `operai di fabbrica` (unità 4) segue la stessa cornice.
4. **Apici asimmetrici**: 1 inglese (`it's`) contro 3 italiani (`l'esperienza`, `d'affari` ×2) — elisione, non contrazione.
5. **Virgolette dentro un `VALUE`**: `Hai "prison" cruise to <planet>` resta inglese e conserva le due virgolette; sono le uniche del lotto.
6. **L198 ha fatto emergere un errore in L197**: la resa di `You wish the mining family…` era già in L22 e io ne avevo creato una variante. Riallineata, L197 rieseguito a exit 0, sha aggiornato.

## Verifica

```bash
cd staging/editorial/L198_20261019_202701
python check.py     # FAIL totale: 0 (29 controlli)
python verify.py    # FAIL: 0 · exit 0 (21 controlli)
```

**Non verificato**: nessun lavoro accettato nel gioco, nessuna schermata vista, nessuna revisione umana; le 51 unità restano `PENDING`.
