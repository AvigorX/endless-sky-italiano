# L29 — revisione di chiusura

Lotto `L29_20261018_103254` · `data/hai/hai missions.txt` · righe 23–2696 · 823 unità ·
aperto e chiuso il 2026-10-18.

Tutti i numeri di questo documento sono misurati con `check.py`, `verify.py`, `state.py`
e i file su disco. Nessun valore è dedotto da un lotto precedente.

## 1. Collocazione nel file

`hai missions.txt` conta 823 unità nel database, dalla riga 23 alla 2696. L29 le copre tutte:
è l'unico lotto di questo file, quindi la copertura totale 823/823 è un invariante asserito e
non una stima. Prima della riga 23 e dopo la 2696 non esiste alcuna unità (`where line < 23` → 0,
`where line > 2696` → 0, `max(line)` → 2696).

## 2. Le dieci parti

| parte | unità | righe | EN → IT | ratio | min–max |
|---|---|---|---|---|---|
| 01 | 1–80 (80) | 23–273 | 2.575 → 2.418 | 0,939 | 0,64–1,37 |
| 02 | 81–165 (85) | 274–522 | 2.107 → 1.920 | 0,911 | 0,73–1,44 |
| 03 | 166–250 (85) | 527–951 | 2.206 → 2.048 | 0,928 | 0,78–1,39 |
| 04 | 251–335 (85) | 952–1331 | 2.505 → 2.323 | 0,927 | 0,76–1,38 |
| 05 | 336–420 (85) | 1332–1546 | 3.228 → 2.954 | 0,915 | 0,82–1,29 |
| 06 | 421–505 (85) | 1547–1828 | 2.772 → 2.665 | 0,961 | 0,65–1,68 |
| 07 | 506–590 (85) | 1829–2069 | 2.677 → 2.542 | 0,950 | 0,79–1,29 |
| 08 | 591–675 (85) | 2070–2312 | 1.976 → 1.786 | 0,904 | 0,71–1,56 |
| 09 | 676–760 (85) | 2313–2560 | 2.359 → 2.247 | 0,953 | 0,75–1,23 |
| 10 | 761–823 (63) | 2561–2696 | 1.521 → 1.470 | 0,966 | 0,82–1,52 |

Nove parti da 85 unità e una da 63, perché 823 non è divisibile per 85: l'ultima parte assorbe
il resto invece di produrre una parte di tre unità. Ogni parte è stata chiusa con
`check.py --range` verde prima di aprire la successiva.

## 3. Conteggi strutturali (verificati per unità)

| grandezza | valore |
|---|---|
| unità | 823 |
| parole EN → IT | 23.926 → 22.373 (0,935) |
| contesti | 54 |
| parti | 10 |
| tab | 606 = 606 |
| virgolette | 1.260 = 1.260 |
| token `<...>` | 247 = 247 |
| unità con virgolette dispari nel sorgente | 30 |
| `MISSION_TEXT` / `DESCRIPTION` / `VALUE` | 685 / 41 / 35 |
| `DIALOG` / `UI_LABEL` / `LOGBOOK` | 34 / 15 / 13 |
| `CONVERSATION` | 0 |
| non traducibili (NT) | 17 |
| rapporto per unità | 0,64 – 1,68 |
| sha256[:16] di `translation.json` | `b8bf47375f390542` |

I kind sono misurati sul `source.json` del lotto: la somma (685+41+35+34+15+13) fa 823, e
`verify.py` la confronta con un valore atteso esplicito, non con un conteggio ricavato al volo.

## 4. Famiglie lessicali nuove di questo lotto

- **`Unfettered Hai` → «Hai Slegati»**, con «Slegati» usato anche da solo. Il testo li chiama così
  in entrambe le direzioni (i Slegati si definiscono i «veri Hai», gli altri li chiamano «fratelli
  traviati»), e la traduzione mantiene la differenza di tono lasciando le due formule distinte.
- **`keystone` → «pietra chiave»**, con la variante `Key Stone` → «Pietra Chiave» e
  `Tree Skeleton Key Stone` → «Pietra Chiave Scheletro d'Albero». Il termine è centrale nelle
  missioni di Hareek: la resa è tenuta letterale perché il testo ci costruisce sopra un discorso
  religioso.
- **`ringworld` → «mondo ad anello»**, usato dalle missioni degli Hai e poi dagli Heliarch.
- **`drone carrier` → «porta-droni»**, con `Pond Strider` e il drone `Flea` lasciati in inglese
  come nomi propri di progetto.
- **Nomi di nave lasciati in inglese**: `Star Queen`, `Bulk Freighter`, `Heavy Shuttle`, `Aphid`,
  `Star Barge`, `Shield Beetle`, `Geocoris`, `Leviathan`, `Solifuge`, `Starling`, `Gull`, `Keloid`.
  Sono etichette di modello, non prosa: tradurle renderebbe il testo incoerente con l'interfaccia.
- **Nomi propri lasciati in inglese**: `Greenwater`, `Follower`, `Kornephoros`, `Darkrest`, `Prime`,
  `Darkcloak`, `Cloudfire`, `Stonebreak`, `Frostmark`, `Hai-home`, `Allhome`, `Giverstone`,
  `Featherweight`, `Gienah`, `Covert`. Persone e organizzazioni: `Sayari`, `Yashili`, `Osen`, `Rayn`,
  `Nanachi`, `Likeet`, `Hareek`, `Eeeya`, `Anoo`, `Tagreep`, `Narancia`, `Xavier`, `Vanessa`,
  `Turner`, `Elliot`, `Anaya`, `Touhar`, `Kiru`, `Arthur`, `Scar`, `Megaparsec`, `Kraz Cybernetics`.
- **`Scar's Legion` → «Legione di Scar»**; il soprannome `Scab` è reso con «Crosta» per conservare
  la battuta, che nel testo è un gioco sulla cicatrice.

## 5. Difficoltà incontrate e come sono state risolte

1. **Due unità che non sono prosa.** La 455 (`outfit/crystal pendant`, dentro un comando `scene`)
   e la 599 (`thumbnail/hai pond strider`) finiscono nel `source.json` come `MISSION_TEXT`, ma sono
   riferimenti di dato: tradurle rompe il gioco. Sono state aggiunte a `NT` con la motivazione
   scritta in `check.py`, portando le unità non traducibili da 15 a 17. Il controllo
   «non traducibili lasciate identiche» verifica che siano **identiche**, non che siano tradotte.
2. **Una sorgente che duplica un titolo con due testi diversi.** Le unità 734, 757 e 763 hanno
   inglese `Acorns for Anoo`, mentre la 780 ha `Acorn Delights`: stessa traduzione avrebbe creato
   un duplicato non spiegato dal sorgente. La 780 è diventata «Delizie di Ghiande», il nome del
   negozio, distinto dal titolo della missione «Ghiande per Anoo».
3. **Una battuta troppo lunga per il rapporto.** La 675 `(Bail.)` era resa con
   «(Tagliare la corda.)»: rapporto 2,625, oltre il limite 1,75. Riscritta «(Fuggi.)».
4. **Battute aperte dal sorgente.** In questo file molte righe di dialogo non chiudono la
   virgoletta, perché la citazione continua nell'unità successiva. La normalizzazione meccanica
   aveva chiuso la citazione in ventitré casi (81, 107, 108, 159, 160, 161, 171, 217, 276, 277,
   690, 748, 749, 750, 751, 752, 753, 754, 768, 776, 790, 791, 801): il ciclo ha rimosso la
   virgoletta in eccesso e il conteggio per unità è tornato pari. **Regola**: si riproduce il
   sorgente, non si normalizza la citazione.
5. **Un refuso mio.** La 415 diceva «facendo di nuovo la avida»: corretto in «l'avida».
6. **Una resa corta non segnalata dal controllo.** La 68 `"I am."` era resa «"Sono io."» con
   rapporto 0,55: il controllo la accettava, ma la battuta suonava monca ed è stata portata a
   «"Sì, sono io."». Non era un FAIL: è una scelta di qualità, e va dichiarata come tale.

## 6. Che cosa è stato verificato e che cosa no

**Verificato** (exit code o stato osservato prima/dopo):

- `check.py` completo: `FAIL totale: 0`, 823/823, 10 parti, 0 unità mancanti.
- `verify.py`: **25 controlli**, `FAIL: 0`, exit 0. Fra questi: riga grezza identica al file
  sorgente per tutte le 823 unità, `english/kind/path` identici a `state.db`, stato `PENDING`
  per tutte, nessuna `APPROVED`, id univoci, ordine identico al sorgente, copertura 823/823 da
  un solo lotto senza sovrapposizioni, NT identiche, parità esatta di token/tab/virgolette/backtick,
  nessun trattino lungo o en-dash, rapporto definito per ogni unità, parti su disco che
  ricostruiscono `translation.json`.
- `state.py`: `ESITO: OK`, integrità di `state.db`, `glossary.csv`, `inventory_fields.csv`,
  `tools/l10n.py`, dei tre file `output/l10n-it/data/_ui/*` e del repo originale
  (`endless-sky HEAD b4aa3bac3`, modifiche: nessuna).

**Non verificato:**

- Nessun rendering nel gioco: lo staging non è stato compilato né caricato da Endless Sky.
- Nessuna approvazione nel database: le 823 unità restano `PENDING`.
- La resa dei termini nuovi (Slegati, pietra chiave, porta-droni) non è stata confrontata con
  altri lotti che potrebbero introdurre gli stessi concetti: il glossario è locale al lotto.

## 7. Riproducibilità

```bash
cd ~/PROGETTI/G-DEV/GAME-SOURCE-LAB/endless-sky-l10n
python staging/editorial/L29_20261018_103254/check.py            # FAIL totale: 0
python staging/editorial/L29_20261018_103254/verify.py           # FAIL: 0, exit 0
python staging/editorial/L29_20261018_103254/check.py --range 1 80
python staging/editorial/tools/state.py                          # ESITO: OK
```

Le parti si ricostruiscono in ordine con `parts/part01..part10.json`; `translation.json` è la
loro unione per `idx`, e `verify.py` la confronta con i file su disco.

## 8. Stato finale

`data/hai/hai missions.txt` è **completo**: 823/823 unità, nono file chiuso dello staging.
`hai missions` non ha segmenti residui, quindi L30 dovrà partire da un file diverso.
Lo staging passa a **13.570 unità · 431.733 EN → 409.002 IT**, residuo **18.360** unità.
