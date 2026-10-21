# STATO — L191 · `bunrodea missions.txt` (primo lotto: **apre il file**)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L191_20261019_194730` |
| Righe / unità | **16–52** / **12** — file al **12/77 (15,6%)** |
| Tipi | {'VALUE': 1, 'DESCRIPTION': 1, 'MISSION_TEXT': 10} |
| Tab · virgolette | **9** · **6** |
| Contesti | **1** (una sola missione) · **12** testi distinti |
| Parole | **466 EN → 434 IT** |
| Apici | **13** inglesi · **6** italiani |
| sha256 | `a1c782a568e872ed…` |
| Esiti | `check.py` **25** (`FAIL 0`) · `verify.py` **21**, exit **0** |

## Cosa contiene

| blocco | unità | righe | contenuto |
|---|---|---|---|
| invito e arrivo | 1-2 | 16-17 | il `VALUE` «An Intriguing Invitation» e l'invito nel sistema indicato |
| l'incontro notturno | 3-4 | 38-39 | due mantidi armati, uno con modifiche cibernetiche |
| le tre battute | 5-7 | 41-43 | pace, incomprensione, resa |
| il dispositivo | 8-12 | 44-52 | la mappa olografica e le due varianti (raccogliere o schivare) |

## Difficoltà

1. **1 segnaposto `<origin>`** da conservare alla lettera (idx 3), in inglese e in italiano.
2. **6 virgolette di dialogo** (idx 5, 6, 7) e **9 tab**: le virgolette sono diritte, mai caporali.
3. **Le due varianti 11 e 12** condividono la seconda metà (mappa, sistema evidenziato, partenza) e la resa deve coincidere: il controllo confronta le due stringhe.
4. Un'asserzione sbagliata (mia): il controllo pretendeva `(Schivi` mentre l'imperativo corretto è **Schiva**.

## Verifica

```bash
cd staging/editorial/L191_20261019_194730
python check.py     # FAIL totale: 0 (25 controlli)
python verify.py    # exit 0 (21 controlli)
```

**Non verificato**: nessuna missione giocata; i testi non sono stati caricati nel gioco.
