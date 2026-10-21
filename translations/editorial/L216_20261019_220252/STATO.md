# STATO — L216 · `deep jobs.txt` (quinto lotto)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L216_20261019_220252` |
| Righe / unità | **866–929** / **30** — file a **157/187 tradotte + 1 `UI_LABEL`** (84,0%) |
| Tipi | {'TEXT': 15, 'MISSION_TEXT': 14, 'LOGBOOK': 1} |
| Tab · virgolette · apici | **13** · **26** · **15 EN / 9 IT** |
| Segnaposto | **7** su 3 simboli (`<passengers>` 4, `<payment>` 2, **`<last>` 1**) |
| Contesti | **3** — da `Deep Consultants` a `stranded consultant dropoff payment` |
| Parole | **439 EN → 443 IT** (rapporto 0,74–1,44, media 1,04) |
| sha256 | `193651028d79b6bd…` |
| Esiti | `check.py` **25** (`FAIL totale: 0`) · `verify.py` **19** (`FAIL: 0`) |

## Cosa contiene

La fine dell'incontro con **Julie Gillar** e la sua assistente: il dialogo (dodici battute con tab), il `LOGBOOK` che
riassume l'accordo, il viaggio e il congedo con la battuta sul capitano `<last>`. Poi i due blocchi di frammenti della
missione «consulenti bloccati»: come li trovi e come li lasci.

## Difficoltà

1. **Due segnaposto nuovi.** **`<last>`** è un **cognome**: non si traduce né si accorda, e «capitano `<last>`» regge sia
   un cognome italiano sia uno straniero. **`<passengers>`** è un numero, e l'articolo lo segue come in inglese
   (*the `<passengers>`*): scelta dichiarata, perché se il segnaposto sostituisse un numero nudo la frase sarebbe rotta
   **in entrambe** le lingue.
2. **Tre tipi in un lotto.** `MISSION_TEXT` con tab, `LOGBOOK` senza tab, `TEXT` frammentati: le regole di ognuno vanno
   applicate insieme senza confonderle.
3. **Il `LOGBOOK` non è in terza persona.** Avevo scritto un controllo «niente `tu`/`ti`», ed è caduto: il testo inglese
   dice *from you* e *showed you*, quindi il diario parla al giocatore. Il controllo ora verifica il contrario —
   apertura descrittiva in terza persona e poi seconda persona.
4. **Composizione dei frammenti**: due aperture («In base alla richiesta di alloggio, tu» / «Nonostante il preavviso
   breve, tu»), quattro modi di prelevare, tre luoghi, una chiusura. Tutti i gruppi devono restare distinti.
5. **`soon notifies`** invece di *immediately notifies*: la resa è «ti avvisa presto», e il controllo verifica che **non**
   sia ricaduta nella formula di L212/L214.

## Verifica

```bash
cd staging/editorial/L216_20261019_220252
python check.py     # FAIL totale: 0 (25 controlli)
python verify.py    # FAIL: 0 (19 controlli) · invariante 157 + 1 + 29 = 187
```

**Non verificato**: nessuna missione giocata, nessuna schermata vista; 30 unità `PENDING`.
