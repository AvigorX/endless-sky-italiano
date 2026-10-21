# STATO — L196 · `hai jobs.txt` (primo lotto: **apre il file**)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L196_20261019_200808` |
| Righe / unità | **15–489** / **39** — file al **39/175 (22,3%)** |
| Tipi | {'VALUE': 17, 'DESCRIPTION': 16, 'TEXT': 6} |
| Tab · virgolette | **0** · **6** (tutte nei tre `TEXT` citati) |
| Segnaposto | **72** su **32** unità — 19 `<planet>` · 18 `<payment>` · 11 `<destination>` · 9 `<bunks>` · 6 `<tons>` · 5 `<date>` · 2 `<cargo>` · 1 `<passengers>` · 1 `<origin>` |
| Contesti | **20** — da `Human Vacation [1]` a `Delivery to Human Space [2]` |
| Parole | **499 EN → 466 IT** (rapporto 0,91–1,12, media 1,02) |
| Apici | **1** inglese (`didn't`) · **3** italiani (`all'anno`) |
| sha256 | `e69389281fc1e23f…` |
| Esiti | `check.py` **26** (`FAIL 0`, exit 0) · `verify.py` **19** (`FAIL: 0`, exit 0) |

## Cosa contiene

| blocco | unità | righe | contenuto |
|---|---|---|---|
| Human Vacation | 1–4 | 15–42 | vacanza di un umano e di un gruppo, verso un mondo Hai |
| Hai Vacation | 5–12 | 63–141 | quattro lavori, singolo e gruppi; «lo strano mondo Hai» |
| Wealthy Hai | 13–16 | 165–196 | famiglia benestante, viaggio rapido entro una data |
| Hai Festival | 17–23 | 223–299 | il dialogo del pagamento e tre lavori (Hai, umani, misto) |
| Unfettered Aid | 24–34 | 333–410 | cinque battute di dialogo e tre consegne di cibo |
| Delivery to Human Space | 35–39 | 437–489 | due consegne e il nome del terzo lavoro |

## Difficoltà

1. **`VALUE` non si traducono**: 17 nomi di lavoro restano inglesi alla lettera (`Human vacationer to <planet>`, `Special Delivery to <planet>`, parentesi quadre comprese). Precedente misurato: nei lotti L117…L195 i `VALUE` sono identici all'inglese su tutte le occorrenze; i `VALUE` tradotti si fermano a L16–L18.
2. **`TEXT` invece si traducono**: sono tre battute di dialogo (`phrase:…`), e i `TEXT` in prosa sono tradotti da L108 a L152. Restano inglesi solo i nomi di armi/outfit sotto contesti `ship:` (L139, L176–L178).
3. **72 segnaposto**: il lotto non ha un solo tipo di token ma nove. Il controllo confronta il **multiset per unità**, non il totale, perché `<payment>` (18) e `<planet>` (19) si compensano facilmente.
4. **Famiglie di testi ripetuti**: 8/10/12 identici; 19/21/23 con la stessa cornice e soggetto diverso; 30/32/34 identici; 36/38 diversi solo nel soggetto. Il `check.py` verifica le quattro famiglie, non solo l'unità singola.
5. **Apici asimmetrici**: 1 in inglese (`didn't`, contrazione) contro 3 in italiano (`all'anno`, elisione). Non è un errore: il controllo lega ogni apice alla sua causa.

## Verifica

```bash
cd staging/editorial/L196_20261019_200808
python check.py     # FAIL totale: 0 (26 controlli)
python verify.py    # FAIL: 0 · exit 0 (19 controlli)
```

**Non verificato**: nessun lavoro accettato nel gioco, nessuna schermata vista, nessuna revisione umana; le 39 unità restano `PENDING`.
