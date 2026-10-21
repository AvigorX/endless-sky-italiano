# STATO — L209 · `coalition news.txt` (quarto lotto)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L209_20261019_212543` |
| Righe / unità | **247–308** / **21** — file al **77/112 (68,8%)** |
| Tipi | {'NEWS': 21} |
| Tab · virgolette · apici | **0** · **42** (2 per unità, tutte citate) · **2 EN / 7 IT** |
| Segnaposto | **0** (asserzione negativa scritta) |
| Contesti | **5** — merchant 3, vendor 3, tre contesti civilian da 5 (arach, kimek, saryd) |
| Parole | **432 EN → 450 IT** (rapporto 0,93–1,26, media 1,09) |
| sha256 | `7e550942341d014e…` |
| Esiti | `check.py` **24** (`FAIL totale: 0`) · `verify.py` **19** (`FAIL: 0`) |

## Il tratto del lotto: tre stringhe ripetute tre volte

Le unità **4/9/14**, **5/10/15** e **6/11/16** sono **lo stesso testo inglese** sotto tre contesti diversi (`arach
civilian`, `kimek civilian`, `saryd civilian`). La traduzione deve essere **identica** nelle tre copie, e le famiglie
devono coincidere fra le due lingue.

Il controllo lo verifica in modo strutturale: raggruppa per testo e confronta le partizioni. Se una copia divergesse di
una parola, cadrebbero **due** controlli — quello delle famiglie e quello delle copie identiche.

## Cosa contiene

Un mercante invidioso dei jump drive, tre civili (Arach, Kimek, Saryd) che commentano le stesse tre cose — l'arresto dei
terroristi, il sole delle trasmissioni, la partenza di un amico per Ring of Wisdom — più tre voci specifiche per specie
(le Case confusa dai turisti, la sorella che impara l'Arachi, i bambini che si arrampicano) e un venditore di dolci,
arazzi e portachiavi.

## Difficoltà

1. **Famiglie di stringhe ripetute** (9 unità su 21): è il caso di L198 (11 copie di una stringa), ma qui le copie stanno
   in contesti **diversi**, non in missioni numerate.
2. **Registro**: 17 unità su 21 chiudono con un verbo. Le quattro eccezioni sono dichiarate e verificate: la famiglia
   5/10/15 chiude con «mai...» perché il sorgente chiude con *«never can...»*, e l'unità 21 chiude con «crediti!» come
   *«credits!»*.
3. **`Houses` → «Case»**: istituzione al plurale, tradotta; i nomi propri (`House Ablomab`, `House Plumtab`) restano
   inglesi. Stessa distinzione di `Coalition Games` in L206.
4. **`jump drive`** resta inglese: è un equipaggiamento, non un nome comune.
5. **Due asserzioni mie sbagliate corrette prima di chiudere**: i contesti civilian **non** hanno il prefisso
   `coalition`, e la citazione inglese è `'field trip,'` con la virgola **dentro** le virgolette.

## Verifica

```bash
cd staging/editorial/L209_20261019_212543
python check.py     # FAIL totale: 0 (24 controlli)
python verify.py    # FAIL: 0 (19 controlli) · famiglie + confine riga 309
```

**Non verificato**: nessuna schermata vista, nessuna revisione umana; 21 unità `PENDING`.
