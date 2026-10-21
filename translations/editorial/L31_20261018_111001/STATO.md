# L31 — stato di avanzamento (CHIUSO 2026-10-18)

Lotto `L31_20261018_111001` · `data/coalition/heliarch intro.txt` · righe 16–2140 · **663/663 unità**.
Undicesimo file completo dello staging. Tutti i numeri sono misurati, non stimati.

## Fatto

- `source.json`: 663 unità, 41 contesti, kind 571 `MISSION_TEXT` / 31 `VALUE` / 31 `DESCRIPTION` /
  16 `DIALOG` / 10 `UI_LABEL` / 4 `LOGBOOK`, 0 `CONVERSATION`.
- `check.py` derivato da L30 con `NT = {38, 82, 193, 207, 214, 219, 230, 399, 432, 459}` (le 10
  `UI_LABEL`, tutte etichette di salto); `TOKEN_EXC` vuoto, 14 famiglie di token tutte di dati.
- 11 parti scritte a mano, tutte a fine missione: 1–42, 43–101, 102–158, 159–238, 239–286, 287–363,
  364–436, 437–519, 520–575, 576–633, 634–663 (42, 59, 57, 80, 48, 77, 73, 83, 56, 58, 30). Ogni
  parte chiusa con `check.py --range` verde.
- `translation.json`: 663 unità, 21.729 EN → 20.845 IT (0,959), rapporto per unità 0,73–1,68,
  sha256[:16] `09e75a0528604150`.
- `verify.py`: **25 controlli**, `FAIL: 0`, exit 0. Copertura **663/663** asserita: il lotto è
  l'unico del file.
- `review.md`, `REPORT.md`, questo `STATO.md`.

## Regole applicate

- **Voce della Coalizione** coerente con L24–L26 e L30: Kimek, Saryd e Arach con l'ordine dei
  costituenti marcato (soggetto esplicito, verbo in coda), narrazione in italiano normale. Esempi in
  `review.md` §4.
- **Si riproduce il sorgente, non si normalizza**: virgolette aperte, tab iniziale, spazi ai bordi e
  troncamenti come nel file originale.
- **Niente trattino lungo né en-dash**: zero occorrenze. Nessun carattere non latino.
- **Tab derivati dal sorgente**, non digitati: 509 IT = 509 EN.
- **Nessun controllo allentato**: quattro titoli fuori banda (`576`, `595`/`607`/`611`, `617`) e tre
  battute corte (`88`, `111`, `450`) sono stati riscritti nel testo; una coppia di inglesi quasi
  identici (`270`/`303`) è stata differenziata in italiano perché il duplicato non era giustificato
  dal sorgente.
- **Numeri dai file, non dalla memoria**: la distribuzione dei kind, i 25 controlli di `verify.py`
  (contati con `grep -c ' OK'`) e i totali vengono da misure.
- **Nessuna scrittura sul database**: `state.db` aperto in sola lettura, 663 unità `PENDING`.

## Glossario del lotto

| inglese | italiano | nota |
|---|---|---|
| `Heliarch` / `Heliarchy` | Heliarch / Eliarchia | il popolo e il governo (già in L30) |
| `Coalition` | Coalizione | glossario generale |
| `console` / `consuls` | console / consoli | carica di governo dell'Eliarchia |
| `Arbiter` | arbitro | grado degli Heliarchs (`Arbiter Sedlitaris` → arbitro Sedlitaris) |
| `Magister` | magistra | grado femminile (`Magister Lotuora`) |
| `Punishers` / `Finishers` | invariati | classi di nave degli Heliarchs |
| `Judicators` / `Hunters` | invariati | navi da guerra e intercettori |
| `Wardragon` / `Spires` | invariati | navi dei Quarg e Kimek |
| `circlet` | cerchietto | interfaccia neurale degli Heliarchs |
| `jump drive` | motore di salto | precedente di L24 |
| `Drill` (titoli) | prova | `Refueling/Pursuit/Combat Drill` → prova di rifornimento/inseguimento/combattimento |
| `Spy Drone` | drone spia | da `repair drone` + modulo di scansione |
| `Finisher Pods` | pod Finisher | equipaggiamento, nome proprio della ditta |
| `plasma turrets` / `torpedo launchers` | torrette al plasma / lanciatori di siluri | attrezzature umane |
| `ring` / `ringworld` | anello / mondo ad anello | glossario della Coalizione |

Restano invariati i nomi di pianeti, sistemi, anelli e persone (`Anello dell'Amicizia`,
`Anello del Potere`, `Fourth Shadow`, `Remote Blue`, `Ashy Reach`, `Deneb`, `Zug`, `Ruin`,
`Zubeneschamali`, `Aulori`, `Iekie`, `Plortub`, `Lotuora`, `Sedlitaris`, `Kirrie`, `Tugroob`) e le
istituzioni (già in italiano: Senato, Repubblica, Sindacato, Mondi Liberi).

## Limiti dichiarati

- **Nessun rendering nel gioco.** Le 663 unità non sono mai state caricate da Endless Sky.
- **Nessuna approvazione.** `APPROVED 364 · PENDING 32.560`, invariato.
- **Lacuna di inventario di L30 non toccata**: riguarda `lunarium intro.txt`, non questo file; qui le
  4 righe `log` producono 4 unità `LOGBOOK` regolari.
- **Glossario non riconciliato** con i file non ancora affrontati: `coalition jobs/news/outfits/
  ships/weapons` restano da tradurre e potrebbero richiedere aggiunte.

## Prossimo passo

`heliarch intro.txt` è chiuso: L32 parte da un **file nuovo**, scelto misurando il residuo
(`state.py` + query su `state.db`), non a memoria. Il candidato misurato è
`data/wanderer/wanderers start.txt` (righe 23–3092, 805 unità, 24.166 parole, 69 contesti, confine
fine file): apre l'arco dei Wanderers, che l'editoriale tratta come fazione invariata (`Wanderers`),
con 47 `CONVERSATION` da valutare una per una.
Sequenza: `export_section.py` → ricognizione dei `kind` → `check.py` derivato con `NT` misurato →
parti a fine missione con `--range` verde → `verify.py` → `review.md` + `REPORT.md` + questo file →
handoff e checkpoint contestuali.

## Comandi di ripresa

```bash
cd ~/PROGETTI/G-DEV/GAME-SOURCE-LAB/endless-sky-l10n
python staging/editorial/tools/state.py
python staging/editorial/L31_20261018_111001/check.py
python staging/editorial/L31_20261018_111001/verify.py
python staging/editorial/tools/check_handoff.py HANDOFF_L32_20261018.md
```
