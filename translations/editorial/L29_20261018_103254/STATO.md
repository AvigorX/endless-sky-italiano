# L29 — stato di avanzamento (CHIUSO 2026-10-18)

Lotto `L29_20261018_103254` · `data/hai/hai missions.txt` · righe 23–2696 · **823/823 unità**.
Nono file completo dello staging. Tutti i numeri sono misurati, non stimati.

## Fatto

- `source.json`: 823 unità, 54 contesti, kind 685 `MISSION_TEXT` / 41 `DESCRIPTION` /
  35 `VALUE` / 34 `DIALOG` / 15 `UI_LABEL` / 13 `LOGBOOK`, 0 `CONVERSATION`.
- `check.py` derivato da L28 con `NT = {77, 84, 86, 365, 455, 465, 469, 473, 478, 481, 483,
  599, 659, 741, 796, 800, 808}` (15 `UI_LABEL` + 2 riferimenti di dato).
- 10 parti scritte a mano: 1–80, 81–165, 166–250, 251–335, 336–420, 421–505, 506–590,
  591–675, 676–760, 761–823. Ogni parte chiusa con `check.py --range` verde.
- `translation.json`: 823 unità, 23.926 EN → 22.373 IT (0,935), rapporto per unità 0,64–1,68,
  sha256[:16] `b8bf47375f390542`.
- `verify.py`: **25 controlli**, `FAIL: 0`, exit 0. Copertura **823/823** asserita: il lotto è
  l'unico del file.
- `review.md`, `REPORT.md`, questo `STATO.md`.

## Regole applicate

- **Si riproduce il sorgente, non si normalizza.** Ventitré battute di questo file lasciano la
  citazione aperta perché continua nell'unità successiva: la normalizzazione meccanica le aveva
  chiuse, e il ciclo le ha riaperte rimuovendo la virgoletta in eccesso.
- **Nessun trattino lungo né en-dash.** Zero occorrenze in 823 unità.
- **Numeri dai file, non dalla memoria.** La distribuzione dei kind, il conteggio dei controlli
  di `verify.py` (25, contati sull'output) e i totali di staging vengono da misure, non da
  assunzioni copiate dai lotti precedenti.
- **Nessuna scrittura sul database.** `state.db` è stato aperto in sola lettura
  (`mode=ro`): le 823 unità restano `PENDING`.

## Glossario del lotto

| inglese | italiano | nota |
|---|---|---|
| `Unfettered Hai` | Hai Slegati / gli Slegati | usato anche da solo |
| `keystone` / `Key Stone` | pietra chiave / Pietra Chiave | centrale nelle missioni di Hareek |
| `Tree Skeleton Key Stone` | Pietra Chiave Scheletro d'Albero | nome proprio di oggetto |
| `ringworld` | mondo ad anello | |
| `drone carrier` | porta-droni | |
| `Scar's Legion` | Legione di Scar | `Scab` → «Crosta», per conservare la battuta |
| `Pond Strider` / `Flea` / `Solifuge` | invariati | nomi di progetto o di modello |

Nomi di nave e di luogo restano in inglese (`Star Queen`, `Bulk Freighter`, `Heavy Shuttle`,
`Aphid`, `Star Barge`, `Shield Beetle`, `Geocoris`, `Leviathan`, `Starling`, `Gull`, `Keloid`,
`Greenwater`, `Follower`, `Kornephoros`, `Darkrest`, `Prime`, `Darkcloak`, `Cloudfire`,
`Stonebreak`, `Frostmark`, `Hai-home`, `Allhome`, `Giverstone`, `Featherweight`, `Gienah`,
`Covert`): sono etichette condivise con l'interfaccia del gioco.

## Limiti dichiarati

- **Nessun rendering nel gioco.** Il testo non è mai stato caricato da Endless Sky. Non è
  verificato che le righe lunghe stiano nelle schermate di dialogo.
- **Nessuna approvazione.** Lo staging non è approvazione: `APPROVED 364 · PENDING 32.560`
  nel database, invariato.
- **Glossario non riconciliato.** I termini nuovi di L29 non sono stati confrontati con altri
  file non ancora tradotti che potrebbero introdurre gli stessi concetti.
- **Due unità non traducibili per necessità tecnica** (455, 599): sono comandi di dato, non
  prosa. Se un domani il parser le classificasse diversamente, `NT` andrebbe rivisto.

## Prossimo passo

`hai missions.txt` è chiuso: L30 parte da un **file nuovo**, scelto misurando il residuo con
`state.py` e la ricognizione, non a memoria. Sequenza: `export_section.py` → `check.py` derivato
con `NT` misurato → parti da 85 unità con `--range` verde → `verify.py` → `review.md` +
`REPORT.md` + questo file → handoff e checkpoint contestuali.

## Comandi di ripresa

```bash
cd ~/PROGETTI/G-DEV/GAME-SOURCE-LAB/endless-sky-l10n
python staging/editorial/tools/state.py
python staging/editorial/L29_20261018_103254/check.py
python staging/editorial/L29_20261018_103254/verify.py
python staging/editorial/tools/check_handoff.py HANDOFF_L30_20261018.md
```
