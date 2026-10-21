# STATO — L218 · `successor ships.txt` (primo lotto — **file nuovo**)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L218_20261019_221520` |
| Righe / unità | **17–381** / **45** — file a **45/146 (30,8%)** |
| Tipi | {'TEXT': 35, 'DESCRIPTION': 6, 'VALUE': 4} |
| Tab · virgolette · apici | **1** (unità 32) · **70** (2 × 35) · **4 EN / 4 IT** |
| Segnaposto | **0** — il file non ne ha |
| Contesti | **4** — `Aaulqra` 16, `Kaskhorade` 13, `Ejniisde-Khora` 9, `Ejniisde` 7 |
| Parole | **499 EN → 549 IT** (1,00–1,15, media 1,02) |
| sha256 | `9e3e6ea15d7e3638…` |
| Esiti | `check.py` **28** (`FAIL totale: 0`) · `verify.py` **17** (`FAIL: 0`) |

## La regola che cambia: `TEXT` che sono **nomi**, non prosa

39 unità su 45 restano **identiche all'inglese**: 35 `TEXT` che sono nomi di equipaggiamento (`"Ojet" Bimodal Coilgun`,
`"Nnesa" Fusion Core`, `6-"Ruuv" Betavoltaic Cell`) e 4 `VALUE` che sono nomi di specie (`Aaulqran`, `Ejniisden`,
`Ejniisden-Khora`, `Kaskhoraden`). Si traducono solo le **6 `DESCRIPTION`**.

La regola si decide dal **contenuto**, non dall'etichetta del tipo: in `coalition news.txt` i `TEXT` erano citazioni di
giornale e si traducevano; qui sono nomi di prodotto mostrati nella schermata della nave, e virgolette comprese fanno
parte del nome. Il `verify.py` asserisce il numero **39 identici / 6 tradotti** — se un domani un `TEXT` venisse tradotto
per distrazione, il controllo cadrebbe.

## Cosa contiene

Le schede di **quattro navi dei Successori**: l'**Aaulqra** (nave da guerra più antica delle Alte Case), l'**Ejniisde**
(trasporto passeggeri), l'**Ejniisde-Khora** (la versione militarizzata e illegale delle Case del Popolo) e la
**Kaskhorade** (spina dorsale pesante e polivalente delle flotte).

## Difficoltà

1. **Il confine fra «nome da copiare» e «testo da tradurre».** Con 35 `TEXT` in un lotto solo, un errore di classificazione
   non si vede nel conteggio: si vede solo confrontando le unità. Il controllo confronta **testo per testo**.
2. **Nomi composti con prefisso e virgolette**: `6-"Ruuv"`, `1-"Uurau"`, `OC-"Mavra"`, `"Ej"`. Il numero e il prefisso
   fanno parte del nome e restano attaccati.
3. **Terminologia politica**: `High Houses` → **Alte Case**, `People's Houses` → **Case del Popolo**, `Successors` →
   **Successori**, `Successor space` → **spazio dei Successori**. Il controllo verifica che `High Houses` **non** compaia.
4. **Le virgolette dritte sono legittime** in questo lotto (sono nei nomi): il controllo tipografico verifica solo
   caporali, trattini lunghi e puntini di sospensione, non `"`.
5. **Apici in unità diverse fra le due lingue**: inglese 15 (*ship's*), 31 (*People's*, *liner's*), 32 (*People's*);
   italiano 15 (*L'Aaulqra*), 31 (*all'interno*, *dell'Ejniisde*), 45 (*un'ampia*). La mia prima asserzione pretendeva le
   stesse unità: sbagliata, corretta con i conteggi per unità.

## Verifica

```bash
cd staging/editorial/L218_20261019_221520
python check.py     # FAIL totale: 0 (28 controlli)
python verify.py    # FAIL: 0 (17 controlli) · 45/146 · 101 dopo la 381 · confine 386
```

**Non verificato**: nessuna nave vista nel gioco, nessuna schermata di allestimento aperta; 45 unità `PENDING`.
