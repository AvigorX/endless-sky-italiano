# review.md — L255 (`data/wanderer/wanderer jobs.txt`, riga 891) — LOTTO TERMINALE

Registro delle decisioni editoriali dell'**ultimo lotto** del file dei Wanderer: una sola unità, la chiusura di una missione
aperta in L254.

## 1. L'unità

| campo | valore |
|---|---|
| inglese | `When you return, the Wanderers thank you for taking them to the Kor Efreti and hand you <payment> before disembarking.` |
| italiano | «Al ritorno, i Wanderer ti ringraziano per averli portati dai Kor Efreti e ti consegnano `<payment>` prima di scendere.» |
| tipo | `DIALOG` |
| contesto | `mission:Wanderers to Kor Efreti` |

## 2. Le scelte

| punto | decisione | perché |
|---|---|---|
| `the Wanderers thank you` | **«i Wanderer ti ringraziano»** | nome **invariato** al plurale, come in tutto il file (`Wanderers` non si usa) |
| `for taking them to the Kor Efreti` | **«per averli portati dai Kor Efreti»** | «dai» = verso il loro mondo; `Kor Efreti` invariato |
| `hand you <payment>` | **«ti consegnano `<payment>`»** | forma dei Wanderer («ti consegna `<payment>`», L252–L254) |
| `before disembarking` | **«prima di scendere»** | «sbarcare» è troppo formale per una battuta di missione |
| `When you return` | **«Al ritorno»** | evita «Quando torni» mantenendo il senso temporale |

## 3. Coerenza con L254

La battuta **chiude** la missione `Wanderers to Kor Efreti` aperta in L254: là i Wanderer partivano per studiare un mondo
**Kor Efret**, qui tornano e pagano. I nomi (`Wanderer`, `Kor Efreti`) e la formula del pagamento sono gli stessi, e il
`check.py` verifica che `Wanderers` e `Unfettered` **non** compaiano.

## 4. Struttura

| cosa | inglese | italiano |
|---|---|---|
| tab | **0** | **0** |
| virgolette | **0** | **0** |
| apici | **0** | **0** |
| segnaposto | `<payment>` | `<payment>` |

Tre asserzioni negative su un'unica unità: non sono controlli «per riempire», sono i tre modi in cui un testo così corto può
rompersi (un tab copiato dalla formattazione, un apostrofo tipografico, un segnaposto perso).

## 5. Il file chiuso

`data/wanderer/wanderer jobs.txt`: **92 unità** in quattro lotti (L252–L255), **92 righe distinte**, dalla 15 alla 891.
Il `verify.py` confronta le righe dei quattro `translation.json` con quelle del database.

## 6. Cosa resta aperto (dichiarato)

- **Nessuna approvazione**: le 92 unità sono `PENDING`.
- **Nessun testo visto nel gioco**.
- **Nessuna revisione umana**.
- **Il resto della campagna**: 2.653 unità su 95 file; il prossimo è `data/human/post-war reactions.txt` (87 unità, 1.925
  parole).
