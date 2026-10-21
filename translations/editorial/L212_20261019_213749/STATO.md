# STATO — L212 · `deep jobs.txt` (primo lotto)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L212_20261019_213749` |
| Righe / unità | **16–322** / **45** — file al **45/187 (24,1%)** |
| Tipi | {'TEXT': 28, 'VALUE': 8, 'DESCRIPTION': 9} |
| Tab · virgolette · apici | **0** · **4** (unità 19, 27) · **5 EN / 2 IT** |
| Segnaposto | **31** su 6 simboli, identici **per unità** |
| Contesti | **12** — dal primo `phrase:deep mystery cube pickup` a `mission:Transport scientists` |
| Parole | **442 EN → 454 IT** (rapporto 0,67–1,75: ci sono frammenti di due parole) |
| sha256 | `d3561b72157dd31c…` |
| Esiti | `check.py` **26** (`FAIL totale: 0`) · `verify.py` **19** (`FAIL: 0`) |

## Una forma nuova: frammenti che si compongono

Il file non è fatto di frasi, ma di **frammenti** che il gioco concatena. La frase

> «Come da istruzioni, tu» + «apri una cassetta di sicurezza» + «in un magazzino anonimo e disabitato» + «e prelevi il
> pacco misterioso.»

nasce da **quattro unità separate del database**. Tradurre ciascuna «bene in sé» non basta: il risultato deve comporre.

Il controllo verifica l'unica proprietà misurabile della composizione: **la maiuscola o minuscola iniziale di ogni
frammento resta quella inglese**. Se un frammento che in inglese inizia minuscolo («and pick up…») iniziasse con la
maiuscola in italiano, la concatenazione produrrebbe una frase spezzata a metà.

## I segnaposto

**31 su sei simboli**: `<payment>` 11, `<planet>` 8, `<destination>` 8, `<stopovers>` 2, `<planet stopovers>` 1,
`<bunks>` 1. Il controllo confronta il **multiset per unità**, non il totale: un totale giusto può nascondere un
segnaposto spostato da un'unità all'altra.

## Cosa contiene

La **missione del cubo misterioso** (prelievo, consegna in strada o su una stazione, con le varianti di pedinamento) e
le prime missioni di lavoro: consegna di un pacco, recupero, trasporto di scienziati.

## Difficoltà

1. **I frammenti** (28 su 45): la resa è vincolata dalla concatenazione, non dalla frase.
2. **8 `VALUE` restano inglesi** («Mystery delivery to <planet>», «Mystery retrieval from <planet stopovers>»): sono i
   nomi mostrati nella bacheca delle missioni, e seguono la regola dei lotti precedenti.
3. **Le `DESCRIPTION` usano la resa di L198**: «su <destination>» e «Il pagamento è <payment>», non varianti nuove.
4. **Famiglie**: 7 `VALUE` identici + 1, e tre testi di descrizione (7 + 1 + 1). Il controllo verifica le **dimensioni
   dei gruppi**, non i totali.
5. **Spazio iniziale** nelle unità 19 e 27: fa parte della stringa e va conservato, perché la concatenazione lo usa.

## Verifica

```bash
cd staging/editorial/L212_20261019_213749
python check.py     # FAIL totale: 0 (26 controlli)
python verify.py    # FAIL: 0 (19 controlli) · 31 segnaposto per unità
```

**Non verificato**: nessuna missione giocata, nessuna schermata vista, nessuna revisione umana; 45 unità `PENDING`.
