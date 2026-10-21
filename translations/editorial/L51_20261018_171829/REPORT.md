# L51 — rapporto del lotto

`data/avgi/avgi 0 first contact.txt` · righe **413–869** · lotto `L51_20261018_171829` ·
**152/152 unità** · file a **271/406** (66,7%) con L50 · chiuso il 2026-10-18.

## Numeri

| voce | valore |
|---|---|
| unità | **152 / 152** del segmento; file a **271 / 406** (66,7%) |
| parole | 4.314 EN → **3.971 IT** (0,921) |
| contesti | 5 — `Defend Ensemble 1` (43) · `Defend Ensemble 2` (61) · `Scout Rescue` (28) · `Frontline Combat` (11) · `Dissonance Outreach 0.5` (9) |
| parti | 5 — 43 · 32 · 29 · 39 · 9 |
| tab | **113 = 113** (113 unità su 152 iniziano con tab) |
| virgolette | **252 = 252** |
| virgolette dispari | **0** (asserzione di assenza dichiarata) |
| token `<...>` | **32 = 32** (7 famiglie: `<ship>` 14, `<planet>` 6, `<first>` 4, `<destination>` 3, `<last>` 3, `<npc>` 1, `<capacity>` 1) |
| quadre `[` `]` | **0 unità** · backtick **0** (assenze dichiarate) |
| `LOGBOOK` | **10** (6 a tre argomenti, 4 fra backtick, 0 dirette) |
| `DIALOG` | **6** (43, 60, 119, 132, 143, 152) — controllo positivo |
| `UI_LABEL` | **0** → **`NT` vuoto** (assenza dichiarata) |
| `TEXT` / `CONVERSATION` | **0 / 0** (assenze dichiarate) |
| rapporto per unità | 0,60 – 1,38 |
| `check.py` | **FAIL totale: 0** (31 controlli) |
| `verify.py` | **45 controlli**, exit 0, `FAIL: 0` |
| sha256[:16] | `translation.json` `62a89c1348ea5162` · `source.json` `3f96e9004d7b2891` · `check.py` `b3b908d065ad143f` · `verify.py` `4ef248efa3e933c3` |

Segmento **interno**: `verify.py` asserisce `(first, last) == (413, 869)`, **119** unità prima (L50) e
**135** dopo (`tot = 406`).

## Tipi

126 `MISSION_TEXT` · 10 `LOGBOOK` · 6 `DIALOG` · 5 `VALUE` · 5 `DESCRIPTION` · 0 `UI_LABEL` ·
0 `TEXT` · 0 `CONVERSATION`.

## Unità non traducibili (`NT`) — nessuna

In questo lotto **non c'è nessuna** `UI_LABEL` e nessun riferimento di dato: `NT` è vuoto e il controllo
è un'asserzione di assenza (`unita UI_LABEL nel segmento (0 attese: NT vuoto)`), non un elenco vuoto
lasciato passare. È il **primo lotto della serie** in questa condizione: tutti i precedenti avevano
etichette di salto da elencare una per una.

## Le 10 righe `log`

| idx | riga | forma | contenuto |
|---:|---:|---|---|
| 4 | 422 | 3 argomenti | **People / Darius Caldwell**: il capitano della Deep Security e l'ipervia anomala |
| 47 | 530 | backtick | l'accordo con la Twilight Guard, le armi nucleari e il tabù umano |
| 48 | 531 | 3 argomenti | **Factions / Twilight Guard**: braccio militare della Consonanza |
| 49 | 532 | 3 argomenti | **Factions / Avgi**: nessun tabù sulle armi nucleari |
| 61 | 638 | backtick | Ensemble difeso con una flotta armata di testate nucleari |
| 62 | 639 | 3 argomenti | **People / Sora Kun**: ingegnera della spedizione Deep |
| 63 | 640 | 3 argomenti | **People / Darius Caldwell**: l'equipaggio non lo incolpa del tutto |
| 64 | 641 | 3 argomenti | **People / Kokkino**: capitano della Twilight Guard |
| 118 | 741 | backtick | l'accordo per salvare l'equipaggio dell'esploratrice |
| 142 | 803 | backtick | l'accordo per ripulire gli Aberranti dietro la prima linea |

## Le 6 righe `dialog`

| idx | riga | quando compare |
|---:|---:|---|
| 43 | 515 | atterrato ma la scorta con Darius non è entrata nel sistema |
| 60 | 635 | atterrato ma ci sono ancora Aberranti che attaccano |
| 119 | 745 | arrivato a Twirl ma nessuna traccia della Silver Albedo |
| 132 | 775 | atterrato ma la scorta con l'equipaggio salvato non è arrivata |
| 143 | 805 | atterrato ma restano Aberranti a nord |
| 152 | 869 | atterrato ma la scorta con Darius e Sora non è arrivata |

Sono tutti messaggi di **blocco del progresso**: dicono al giocatore che la missione non è conclusa e
cosa deve fare. Tradotti con lo stesso schema (constatazione + «Meglio ripartire e aspettare…»).

## Verifica

```
python staging/editorial/L51_20261018_171829/check.py    → FAIL totale: 0
python staging/editorial/L51_20261018_171829/verify.py   → exit 0, FAIL: 0
```

Dopo la chiusura: **23.120 unità · 736.637 EN · 698.859 IT**, **55 directory** con `translation.json`,
integrità dei file protetti e del repository (`b4aa3bac3`, nessuna modifica).

## Non fatto (dichiarato)

- **Nessuna approvazione nel database**: 152 unità `PENDING`.
- **Nessun caricamento nel gioco**: nessuna delle cinque missioni è stata percorsa.
- **Il file resta aperto**: 135 unità (dalla riga 873 in poi) non sono state toccate.
