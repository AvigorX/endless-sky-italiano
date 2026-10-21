# STATO — L72 · `data/successors/successor 2 ghosts myurej.txt`

**Lotto chiuso e file COMPLETO: 211/211 unità (100%).**

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L72_20261018_194753` |
| File | `data/successors/successor 2 ghosts myurej.txt` (quinto e ultimo lotto) |
| Unità | **50** (righe 407–531; finestra 402–531) |
| Parti | **3** — 17 · 19 · 14 |
| Contesti | **3** — `Myurej 6`, `Myurej 7`, `Myurej 8` |
| Tipi | **40 `MISSION_TEXT` + 3 `VALUE` + 3 `DESCRIPTION` + 2 `DIALOG` + 2 `LOGBOOK`** |
| Parole | 1763 EN → 1679 IT (**0,952**) |
| Rapporto per unità | **0,85 – 1,79** (gate 0,55–1,90) |
| `NT` | **vuoto** — 0 `UI_LABEL`, 0 riferimenti di dato |
| `LOGBOOK` | **2** — unità **5** e **30**, forma diretta, testi distinti |
| `DIALOG` | **2** — unità **3** e **4**: primi del file, sono **testo** (eventi), tradotti |
| `CONVERSATION` / `TEXT` | **0 / 0** — assenze dichiarate |
| Token `<…>` | **18** in 8 famiglie: `<planet>` 5, `<last>` 3, `<ship>` 2, `<destination>` 2, `<origin>` 2, `<tons>` 2, `<payment>` 1, `<first>` 1 |
| Tab · virgolette | **36** su 36 unità · **96** (0 dispari, 0 quadre, 0 backtick) |
| Duplicati inglesi | **0 gruppi** |
| sha256 `translation.json` | `bd09dd6de0b9ff04…` |
| `check.py` | **35 controlli**, `FAIL totale: 0` |
| `verify.py` | **46 controlli**, exit **0** |

## Il file è chiuso

| Lotto | Righe | Unità | EN → IT |
|---|---|---:|---|
| L68 | 16–113 | 49 | 1.502 → 1.447 |
| L69 | 118–197 | 31 | 687 → 704 |
| L70 | 215–307 | 39 | 1.028 → 953 |
| L71 | 311–401 | 42 | 1.632 → 1.546 |
| **L72** | **407–531** | **50** | **1.763 → 1.679** |
| **Totale** | | **211** | **6.612 → 6.329** |

`max(line) = 531`, **0 unità dopo la 531**, copertura **211/211**. L'invariante «di file» qui è legittimo
(decisione 181) ed è asserito **insieme**: chiusura, `max(line)`, copertura.

## Cosa è stato deciso qui

1. **Il lotto copre tre contesti invece di uno** (deviazione dal piano di `HANDOFF_L72`, che prevedeva
   402–464): chiudere il file in un lotto solo evita un ultimo lotto da 30 unità senza struttura, e il
   confine alla 531 è quello reale del file. La deviazione è dichiarata qui e nel `REPORT.md`.
2. **`DIALOG` = testo, non etichetta**: le unità 3 e 4 descrivono eventi («Quando la seconda nave drone
   esplode…», «Ijaset ti ordina di atterrare…»). Sono tradotte; il `verify.py` asserisce che **non** siano
   identiche all'inglese, così un'etichetta mascherata da `DIALOG` verrebbe scoperta.
3. **`Khiajsore`** è il primo erede di Myurej che parla in prima persona: voce **affettata, ridondante,
   autoironica** («Capitano, capitano…», «Myurej M- Khiajsore» ripetuto due volte in unità diverse). La
   ripetizione è nel sorgente (unità 38 e 39 la contengono entrambe) e non è stata normalizzata.
4. **`biped fever`** → «febbre dei bipedi», fra virgolette come nel testo: è una moda, e la resa la lascia
   tale.
5. **`Ribbons of Iret`** resta invariato fra virgolette: nome di un fenomeno, non descrizione.
6. **`scion` → erede** (già in L45), **`dockworker` → addetto portuale**, **`waypoint` → punto di rotta**.
7. **`<tons>`** entra per la prima volta: parità per simbolo su 2 occorrenze.

## Verifica

```bash
cd staging/editorial/L72_20261018_194753
python check.py                 # FAIL totale: 0   (35 controlli)
python verify.py                # exit 0           (46 controlli)
```

## Prossimo passo

**File nuovo**: `data/successors/successor 2 ghosts aqrabe.txt` (180 unità, `max(line) = 478`), che continua
la linea Successors citata in L70 (Casa Aqrabe). Primo lotto proposto: righe **1–158**, unità **23–158**,
**51 unità**, **1.330 parole**, 5 contesti, tab **38** su 38 unità (42 caratteri), virgolette **90**,
**9 token** in 6 famiglie, tipi `35 MISSION_TEXT + 3 VALUE + 3 DESCRIPTION + 3 LOGBOOK + 6 CONVERSATION +
1 DIALOG`. **Primo `CONVERSATION` della linea**: 6 unità da leggere come dialogo, non come righe isolate.
