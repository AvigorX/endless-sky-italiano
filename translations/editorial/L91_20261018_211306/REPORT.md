# REPORT — L91 · `data/successors/successor culture conversations.txt`

## 1. Contenuto

Secondo segmento del file, righe 155–229, due contesti contigui:

- **Successors: Graffiti** (1–27): il tintinnio alle spalle della nave, la scelta fra **andare a vedere** e
  **ignorare**; i tre Successori colti a spalmare soluzione colorata sullo scafo; il dialogo fra minaccia,
  domanda tecnica e presa in giro; tre uscite (farli togliere la soluzione, smascherarli, congedarli) e i tre
  esiti — la scritta con il proprio nome e quello degli amici, oppure l'insulto con la caricatura del volto.
- **Successors: Stage Play** (28–34): i manifesti di **«Myiara l'Immortale»**, il Successore che invita a
  teatro, le due risposte del giocatore e il congedo («non faremo tardi»).

## 2. Scelte

| nodo | scelta | perché |
|---|---|---|
| `hull solution` | **soluzione per lo scafo** | è il nome che i Successori danno al prodotto; `hull repair` resta «riparazione dello scafo» (glossario) |
| `correct thou art!` | **hai ragione tu!** | `thou` reso con «tu» moderno, mai arcaismi finti (glossario) |
| `milling amongst themselves` | **conciliaboli** / **qualche conciliabolo** | due inglesi diversi, due sfumature: la variante breve del secondo ramo è resa più corta |
| `mirthful shade of pink` | **rosa divertita** | `mirthful` è l'emozione, non il colore: «ridente» su una tinta non regge in italiano |
| `the defacement` | **il disegno** / **raschiarla via** | in italiano «deturpazione» è burocratico; il soggetto della rimozione resta la soluzione |
| `for the foreseeable future` | **per molto tempo a venire** | «futuro prevedibile» è un calco |
| `Deathless Myiara` | **Myiara l'Immortale** | titolo di spettacolo: si traduce, `Myiara` resta |
| `myiara system` | **identico** | `UI_LABEL`: riferimento di dato, non testo |

## 3. Difficoltà

1. **60 virgolette su 34 unità**, quattro unità con quattro virgolette (19, 27, 31, 34): il conteggio del lotto
   torna anche con una coppia spostata, quindi il controllo è **per unità**, non sul totale.
2. **Il parlato dei Successori mescola `thou` e inglese moderno nella stessa battuta** (19: «if thou'r'nt
   trained… 'tis bright in color»): reso con «tu» e sintassi piana, senza arcaismi, come da glossario.
3. **Tre unità quasi identiche a due a due** (7/11 sullo stesso inglese con due incisi diversi): le rese sono
   volutamente diverse solo nei punti in cui differisce l'inglese; 8/12, 9/13, 10/14 sono identiche perché
   l'inglese è identico.
4. **Un `UI_LABEL` in mezzo alla prosa** (idx 29): il costruttore lo scrive dal sorgente, senza tab, e il
   `check.py` lo asserisce identico invece di escluderlo con una deroga generale.
5. **`<origin>` accanto a `<ship>`** nella prima unità: cinque token in quattro unità, verificati per unità.

## 4. Numeri osservati

```
unita' coperte 34/34 (33 tradotte + 1 UI_LABEL) · tab 30 · virgolette 60 = 60 · token 5 = 5
parole EN 1117 -> IT 1084 · rapporto 0.92 - 1.54
righe 155/229 · file 114 unita · max(line) 351 · 34 prima / 46 dopo
FAIL totale: 0 (28 controlli) · verify exit 0 (28 controlli)
sha256[:16] 9a8dcdeaee3a69af
```

## 5. Stato del progetto

```
TOTALE staging: 24941 unita · 794554 EN · 753435 IT
successor culture conversations.txt: 68/114 (59,6%) · 2215 EN -> 2098 IT · 2 lotti
residuo traducibile (formula state.py): 6989
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | due parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (28 controlli) **e** `verify.py` exit **0** (28 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 34 unità restano `PENDING`; il gioco non è stato caricato con questa traduzione.
- **Il file non è completo**: restano **46 unità / 1848 parole** (righe 230–351), contratto in
  `HANDOFF_L92_20261018.md`; è l'ultimo segmento e chiude il file.
- **Nessuna revisione umana**.
