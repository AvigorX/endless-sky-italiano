# STATO — L206 · `coalition news.txt` (primo lotto)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L206_20261019_211311` |
| Righe / unità | **28–94** / **20** — file al **20/112 (17,9%)** |
| Tipi | {'NEWS': 20} — **primo lotto di tipo `NEWS`** della campagna |
| Tab · virgolette · apici | **0** · **40** (2 per unità, tutte citate) · **5 EN / 9 IT** |
| Segnaposto | **0** (asserzione negativa scritta) |
| Contesti | **4** — `heliarch news` 1, `longcow rancher` 5, `kimek farmer` 4, `heliarch agent` 10 |
| Parole | **440 EN → 415 IT** (rapporto 0,90–1,28, media 1,09) |
| sha256 | `7cff828f2fb7e44b…` |
| Esiti | `check.py` **25** (`FAIL totale: 0`) · `verify.py` **17** (`FAIL: 0`) |

## La decisione del lotto: il registro Saryd

I Saryd parlano con **l'ordine delle parole invertito** (*«Caring for longcows, hard work it is.»*). Non è un errore
del sorgente: è una caratterizzazione. Regola applicata:

- **narrazione in italiano naturale** (unità 1 e 10, dove parla il notiziario);
- **discorso citato con l'inversione riprodotta** (le altre 18), usando i mezzi dell'italiano: complemento o predicato
  in testa, copula e verbo in coda, soggetto dopo.

Il marcatore è **misurabile**: 9 unità citate finiscono con un verbo flesso (*«un duro lavoro è»*, *«a tua
disposizione sono»*, *«impegnati siamo»*, *«maggiore ho»*), mentre la narrazione no. Il controllo verifica l'insieme
esatto delle unità, non la sensazione di lettura.

## Cosa contiene

Venti voci: un servizio sugli arresti degli Heliarch, cinque battute di un allevatore di longcow, quattro di un
contadino Kimek e dieci di un agente Heliarch.

| contesto | unità | righe | registro |
|---|---|---|---|
| `heliarch news` | 1 | 28 | narrazione |
| `longcow rancher` | 5 | 52–56 | Saryd invertito, comico |
| `kimek farmer` | 4 | 69–73 | Saryd invertito, 1 narrazione (unità 10) |
| `heliarch agent` | 10 | 83–94 | Saryd invertito, istituzionale |

## Difficoltà

1. **Il registro**, non il lessico: è la prima volta che un lotto richiede una regola sintattica esplicita. Va
   applicata a tutta la Coalizione nei lotti successivi (92 unità di questo file).
2. **40 virgolette**: ogni unità è una citazione completa. Il controllo verifica 2 virgolette per unità in entrambe le
   lingue e la coerenza di apertura/chiusura.
3. **`Coalition Games`** è un nome comune di evento (come «Giochi Olimpici»): tradotto «Giochi della Coalizione». La mia
   prima asserzione lo metteva fra i nomi da conservare: era sbagliata l'asserzione, non la resa.
4. **`longcow`** resta invariato al singolare e al plurale, senza «longcowghi»: verificato sul conteggio delle occorrenze.

## Verifica

```bash
cd staging/editorial/L206_20261019_211311
python check.py     # FAIL totale: 0 (25 controlli)
python verify.py    # FAIL: 0 (17 controlli) · confine riga 95, stesso contesto
```

**Non verificato**: nessuna schermata del notiziario vista nel gioco, nessuna revisione umana; 20 unità `PENDING`.
