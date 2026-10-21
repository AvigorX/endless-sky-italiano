# REPORT — L233 (`data/avgi/avgi news.txt`, righe 32–91)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **33 controlli** (`FAIL totale: 0`); `verify.py` esce 0 con **20
controlli** (invariante di segmento: 0 prima della 32, 93 dopo la 91). `state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna
scrittura su `state.db`: le 22 unità restano `PENDING`.

## 1. Cosa contiene il lotto

Ventidue notizie Avgi, ognuna una citazione intera che comincia con l'etichetta di modalità. Tre contesti:

| contesto | righe | unità | chi parla |
|---|---|---|---|
| `news:avgi siege civilian` | 32–42 | 11 | civili sotto assedio: perdita del sistema, sfiducia nella Consonance, ricordi dei cilindri distrutti, rabbia per l'abbandono |
| `news:avgi siege merchant` | 62–66 | 5 | mercanti che forzano il blocco: sollievo, frustrazione, la quota di evacuazione, il recupero di equipaggiamento dai mondi d'origine |
| `news:avgi siege hatchling` | 86–91 | 6 | i nati dopo la guerra: meraviglia per le stelle, confusione, offesa, perdita, disperazione |

## 2. Misure

```
unità             22            (tutte NEWS; zero VALUE, zero UI_LABEL)
parole            447 EN -> 441 IT
rapporto          0,93 - 1,25 (media 1,11)   gate 0,55-1,90
contesti          3              (civilian 11, merchant 5, hatchling 6)
tab               0              asserzione negativa scritta, in EN e in IT
virgolette        44             esattamente 2 per unità, in tutte e 22
apici             12 EN / 5 IT   EN (9,12,13,14,15x2,16x2,17,18,19x2) · IT (3,11,14,16,18)
segnaposto        0              asserzione negativa scritta
identiche         0              22 tradotte
```

## 3. Copertura del file

```
L233   22 unità   righe 32 - 91     (la 32 è la PRIMA unità del file)
residuo 93 unità  righe 115 - 507
------------------------------------
22 + 93 = 115 = unità del file (min 32, max 507)
```

Confine misurato: **riga 115**, `news:avgi merchant`. Fra la riga 92 e la 114 il database non ha unità di questo
percorso: il confine è il primo contesto successivo, non la riga immediatamente dopo (trappola 59, misurata).

## 4. Controlli che hanno morso

Nessun rosso: il lotto è passato al primo giro a `check.py` e a `verify.py`. Le tre cose verificate **prima** di
scrivere, perché potevano rompere:

- **la citazione è intera**: se una sola unità avesse perso la virgoletta di chiusura, il controllo per unità
  (`2 == count('"')`) l'avrebbe vista, mentre un totale di 44 no;
- **le etichette sono 22, non 21**: `Remembrance` e `Frustration` compaiono due volte ciascuna perché l'inglese le
  ripete, e una deduplica per testo avrebbe lasciato due unità non verificate (decisione 139);
- **`Aberrations` e `Aberration` sono la stessa fazione**: entrambe rese «Aberrant» (7 occorrenze contro 5 inglesi +
  2 forme singolari), come da decisione 25. Il controllo vieta esplicitamente «Aberrazione».

## 5. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: le 22 unità sono `PENDING`.
- **Nessuna notizia vista nel gioco**: le stringhe non sono state caricate da Endless Sky; non è verificato che le
  citazioni lunghe stiano nella finestra delle notizie né che le etichette di modalità siano leggibili come tali.
- **Nessuna revisione umana**.
- **Il file non è completo**: 22/115 (19,1%).
