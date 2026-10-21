# STATO — L214 · `deep jobs.txt` (terzo lotto)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L214_20261019_215024` |
| Righe / unità | **457–682** / **35** — file al **102/187 (54,5%)** |
| Tipi | {'MISSION_TEXT': 16, 'TEXT': 8, 'VALUE': 5, 'DESCRIPTION': 5, 'LOGBOOK': 1} |
| Tab · virgolette · apici | **15** · **22** · **6 EN / 6 IT** |
| Segnaposto | **16** su 3 simboli (`<payment>` 6, `<planet>` 5, `<destination>` 5) |
| Contesti | **7** — da `secure package dropoff payment` a `Deep Security Package Reveal` |
| Parole | **431 EN → 430 IT** (rapporto 0,74–1,51, media 1,07) |
| sha256 | `e2d9f07af3bd3c95…` |
| Esiti | `check.py` **26** (`FAIL totale: 0`) · `verify.py` **19** (`FAIL: 0`) |

## Il tratto del lotto: i tab come struttura

**15 tab** dentro 16 `MISSION_TEXT` e 1 `LOGBOOK`. Non sono spaziatura: sono i **separatori di paragrafo** dei testi di
missione lunghi, e ognuno apre il proprio paragrafo (`\t(Go over to him.)`, `\t"Sure. Who are you?"`). Il controllo li
verifica **per unità**: uno in ognuna delle unità 21–35, zero altrove, e sempre **iniziale** — un tab rimosso o spostato
cambierebbe l'impaginazione a schermo.

## Cosa contiene

La consegna del **pacco sicuro** (sei destinatari diversi), cinque missioni di trasporto identiche («Secure delivery to
`<planet>`»), e la **rivelazione**: un agente della **Deep Security**, **Wayde**, ferma il giocatore su una panchina dello
spazioporto e gli spiega che i pacchi che ha trasportato erano suoi.

## Difficoltà

1. **La preposizione sta nell'alternativa, non nel frammento d'apertura.** «Come da istruzioni, consegni il pacco» + «alla
   reception di un'azienda tecnologica»: in inglese la preposizione non c'è (*deliver the package to* + *the counter*), in
   italiano cambia con il genere della destinazione, quindi deve stare **dentro** l'alternativa. Il controllo verifica che
   le sei alternative inizino tutte con preposizione e che il frammento d'apertura non ne porti.
2. **Le alternative devono restare distinte**: sei destinatari (azienda, addetto, negozio, agente in borghese, signora,
   capitano). Se due collassassero sulla stessa resa, il gioco perderebbe una variante.
3. **Registro «tu» contro cortesia inglese.** Wayde dice *Please, have a seat and allow me to take a moment of your
   time*: in italiano la resa naturale sarebbe col «Lei», ma il registro unico della campagna è il «tu». Ho scelto
   «Accomodati e concedimi un momento del tuo tempo» e il controllo **verifica l'assenza** di «Lei» e «Si accomodi».
4. **Le 10 unità ripetute** (5 `VALUE` + 5 `DESCRIPTION`): i `VALUE` restano inglesi, le `DESCRIPTION` usano la resa di
   L198 («su `<destination>`», «Il pagamento è `<payment>`»).
5. **Confine su un `UI_LABEL`**: la riga 683 è un tipo che non entra mai in staging. Il `verify.py` lo dichiara, così il
   lotto successivo sa che quell'unità non comparirà in nessun `translation.json`.

## Verifica

```bash
cd staging/editorial/L214_20261019_215024
python check.py     # FAIL totale: 0 (26 controlli)
python verify.py    # FAIL: 0 (19 controlli) · tab per unità, confine UI_LABEL
```

**Non verificato**: nessuna missione giocata, nessuna schermata vista; 35 unità `PENDING`.
