# STATO — L110 · `data/korath/korath missions.txt` (**il file è completo**: 158/158)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L110_20261018_225501` |
| Righe / unità | **474–580** / **26** |
| Tipi | **21 `MISSION_TEXT`** + **2 `VALUE`** + **2 `DESCRIPTION`** + **1 `DIALOG`** |
| `VALUE` (identici) | 1 e 4: `Salvage the <EDC-ship>` — **lo stesso testo** |
| `DESCRIPTION` | 2 e 5: `Salvage the <EDC-ship> and return it to <planet> to claim rights to it.` — **lo stesso testo**, tradotto |
| Contesti | **3**: `Efreti: Distress Call 6` (474–479), `7` (508–558), `8` (570–580) |
| Parole | **730 EN → 669 IT** (0,916); per unità 0,67–1,19 |
| Tab · virgolette | **17** · **8**, tutte binate |
| Token | **19** in sette famiglie (`<EDC-ship>` 12, `<planet>` 2, `<bunks>` 1, `<ship>` 1, `<destination>` 1, `<first>` 1, `<last>` 1) |
| Ripetizioni | **2 coppie** (1/4, 2/5), entrambe rese identiche |
| Quadre · citazioni aperte | **0** · **0** |
| sha256 | `741adbe5e3ce5afc…` |
| `check.py` | **28 controlli**, `FAIL totale: 0` |
| `verify.py` | **35 controlli**, exit **0** |

## Il criterio rovesciato: due ripetizioni da conservare

In tutti i lotti precedenti «zero ripetizioni» era una regola. Qui il sorgente **ripete**:

| coppia | tipo | testo | resa |
|---|---|---|---|
| 1 / 4 | `VALUE` | `Salvage the <EDC-ship>` | **identico** all'inglese, e uguale fra le due unità |
| 2 / 5 | `DESCRIPTION` | `Salvage the <EDC-ship> and return it to <planet> to claim rights to it.` | **identica fra le due**, tradotta «Recupera la <EDC-ship> e riportala su `<planet>` per rivendicarne la proprietà.» |

Il `check.py` verifica **esattamente** le due coppie e che **non ce ne siano altre**; il `verify.py` rifà lo
stesso conto in modo indipendente. Se una revisione futura «differenziasse» le due `DESCRIPTION` per eleganza,
romperebbe la coerenza del gioco: il tabellone mostra lo stesso nome per la stessa missione.

## La dedica: `<first>` e `<last>` nello stesso testo

L'unità 25 è il cuore del file: il chip dati tradotto dai Quarg contiene una **dedica** al giocatore.

> «La `<EDC-ship>` è una nave di dolore, che porta grande pena in memorie che cantano per generazioni. L'amore è un
> vuoto nell'anima di molti. Sappiate tutti che `<first> <last>` è un Efret autentico di cuore, se non di pelle.
> La `<EDC-ship>` è sua, per salvare vite e custodire memorie.»

Due dettagli che il controllo fissa: `<first>` e `<last>` stanno **insieme e in quest'ordine**, la nave è nominata
**due volte** (apertura e chiusura della dedica), e l'italiano non attribuisce un genere al giocatore — «un Efret
autentico», non «un vero Efret» né un participio concordato.

## Il resto

- **`Distress Call 6`** (1–3): il requisito tecnico — «Devi poter trasportare `<bunks>` membri d'equipaggio in più» —
  e il `VALUE` ripetuto.
- **`Distress Call 7`** (4–19): l'atmosfera portata «agli standard umani, anche se un po' tropicali»; la nave che
  «non ha quasi armi, i sistemi delle batterie sono irrecuperabili»; la scelta fra **portarla a casa** e
  **abbandonarla** («solo un'altra storia tragica fra le rovine della loro civiltà»); il padiglione, il **coro di
  ologrammi** dei morti, la bevanda fermentata che «lascia le labbra formicolanti, finché non le intorpidisce», e
  il trucco di chi finge di bere: «o gli Efret non si accorgono del vostro trucco, o sono troppo educati per dirlo».
- **`Distress Call 8`** (20–26): il Quarg che «si ferma e vi riconosce, ma non parla», il chip tradotto, la dedica.

## Invariante di file (non più di segmento)

| Voce | Valore |
|---|---|
| Unità prima della riga 474 | **132** (L106+L107+L108+L109) |
| Unità dopo la riga 580 | **0** — il lotto chiude il file |
| File | **158 unità**, `max(line) = 580` |
| Lotti | **5** (25 + 38 + 36 + 33 + 26 = **158**) con **158 `id` distinti**, 0 sovrapposizioni |
| Copertura | **158/158 (100%)** — **quarantunesimo file completo**, non approvato |

Il `verify.py` non si limita al segmento: rilegge i `translation.json` di **tutti** i lotti del file e verifica che
la somma copra le 158 unità del database senza duplicati. È la prova che il file è completo, non la dichiarazione.

## Verifica

```bash
cd staging/editorial/L110_20261018_225501
python check.py   # FAIL totale: 0 (28 controlli)
python verify.py  # exit 0 (35 controlli, invariante di file)
```
