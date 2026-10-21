# L30 — stato di avanzamento (CHIUSO 2026-10-18)

Lotto `L30_20261018_105244` · `data/coalition/lunarium intro.txt` · righe 21–2111 · **730/730 unità**.
Decimo file completo dello staging. Tutti i numeri sono misurati, non stimati.

## Fatto

- `source.json`: 730 unità, 35 contesti, kind 619 `MISSION_TEXT` / 33 `VALUE` / 33 `DESCRIPTION` /
  26 `DIALOG` / 12 `LOGBOOK` / 7 `UI_LABEL`, 0 `CONVERSATION`.
- `check.py` derivato da L29 con `NT = {1, 151, 215, 217, 236, 245, 678, 682, 729}` (7 `UI_LABEL` +
  2 categorie di diario `Factions`); `TOKEN_EXC` vuoto, 13 famiglie di token tutte di dati.
- 13 parti scritte a mano, tutte a fine missione: 1–57, 58–104, 105–158, 159–239, 240–310, 311–342,
  343–402, 403–479, 480–527, 528–574, 575–641, 642–700, 701–730. Ogni parte chiusa con
  `check.py --range` verde.
- `translation.json`: 730 unità, 29.208 EN → 28.079 IT (0,961), rapporto per unità 0,70–1,66,
  sha256[:16] `5adcc2bfda276f8f`.
- `verify.py`: **25 controlli**, `FAIL: 0`, exit 0. Copertura **730/730** asserita: il lotto è
  l'unico del file.
- `review.md`, `REPORT.md`, questo `STATO.md`.

## Regole applicate

- **Voce della Coalizione**: ordine dei costituenti marcato per Kimek, Saryd e Arach (soggetto
  esplicito, verbo in coda), narrazione in italiano normale. Stessi esempi in `review.md` §5.1.
- **Si riproduce il sorgente, non si normalizza**: l'unità 13 lascia la citazione aperta perché la
  battuta continua nella 14. Riprodotta.
- **Niente trattino lungo né en-dash**: zero occorrenze. Nessun carattere non latino.
- **Tab derivati dal sorgente**, non digitati: 550 IT = 550 EN.
- **Nessun controllo allentato**: due unità corte (`359`, `398`) e un titolo (`602`) sono stati
  riscritti per rientrare nel rapporto, non la soglia.
- **Numeri dai file, non dalla memoria**: la distribuzione dei kind, i 25 controlli di `verify.py`
  (contati con `grep -c ' OK'`) e i totali vengono da misure.
- **Nessuna scrittura sul database**: `state.db` aperto in sola lettura, 730 unità `PENDING`.

## Glossario del lotto

| inglese | italiano | nota |
|---|---|---|
| `Lunarium Redoubt` | invariato | nome della fazione di resistenza |
| `the Redoubt` | il Redoubt | forma breve usata nei dialoghi |
| `Heliarch` / `Heliarchy` | Heliarch / Eliarchia | il popolo e il governo |
| `Coalition` | Coalizione | glossario generale |
| `House Bebliss` / `House Idriss` / `House Plumtab` | Casa Bebliss / Casa Idriss / Casa Plumtab | `house X` → Casata/Casa |
| `Punishers` / `Finishers` | invariati | classi di nave degli Heliarchs |
| `Spire` / `Spindle` | invariati | navi Kimek e Arach, etichette dell'interfaccia |
| `Bastion` / `Argosy` / `Clipper` / `Thistle` | invariati | modelli comprati da Pyakri |
| `jump drive` | motore di salto | precedente di L24 |
| `Fragmentation Grenades` | granate a frammentazione | |
| `Heavy Anti-Missile Turrets` | torrette antimissile pesanti | |
| `Plasma Turrets` / `Flamethrowers` | torrette al plasma / lanciafiamme | |
| `Armageddon Core` / `Fusion Reactor` / `Breeder Reactor` | nucleo Armageddon / reattore a fusione / reattore autofertilizzante | |
| `longcow` | longcow | animale, invariato |
| `Twin Eclipse`, `Crumbling Winter Star`, `The Twins' Twin Ships`, `Down with the Tyrant House!` | Eclissi Gemella, Stella d'Inverno che Crolla, Le navi gemelle dei gemelli, Abbasso la Casata Tiranna! | titoli di opere teatrali inventate: tradotti |

Restano invariati i nomi di pianeti, sistemi e persone (`Second Viridian`, `Fourth Shadow`,
`Shifting Sand`, `Ablub's Invention`, `Remote Blue`, `Saros`, `Greenrock`, `Shaula`, `Wayfarer`,
`Deneb`, `Tarazed`, `Chiree`, `Elirom`, `Tummug`, `Pyakri`, `Oobat`, `Freya`, `JJ`, `Alondo`,
`Lobmab Bebliss`) e le istituzioni umane (`Southbound`, `Southbound Shipyards`, `Tarazed
Corporation`, `Starlit University`, `Bourne`, `Senato`, `Repubblica`, `Sindacato`, `Mondi Liberi`).

## Limiti dichiarati

- **Nessun rendering nel gioco.** Le 730 unità non sono mai state caricate da Endless Sky.
- **Nessuna approvazione.** `APPROVED 364 · PENDING 32.560`, invariato.
- **Due voci di diario restano in inglese** (righe 21 e 467, `log "Factions" "Lunarium Redoubt" "…"`):
  il nome e il testo non esistono nell'inventario. Causa e misura in `review.md` §7; non correggibile
  senza toccare `tools/l10n.py` e `state.db`, che sono protetti.
- **Glossario non riconciliato** con i file non ancora affrontati.

## Prossimo passo

`lunarium intro.txt` è chiuso: L31 parte da un **file nuovo**, scelto misurando il residuo
(`state.py` + query su `state.db`), non a memoria. Il candidato misurato è
`data/coalition/heliarch intro.txt` (righe 16–2140, 663 unità, 21.729 parole, 41 contesti, confine
fine file): stessa fazione, stesso lessico, nessuna riconciliazione di glossario da fare.
Sequenza: `export_section.py` → ricognizione dei `kind` → `check.py` derivato con `NT` misurato →
parti a fine missione con `--range` verde → `verify.py` → `review.md` + `REPORT.md` + questo file →
handoff e checkpoint contestuali.

## Comandi di ripresa

```bash
cd ~/PROGETTI/G-DEV/GAME-SOURCE-LAB/endless-sky-l10n
python staging/editorial/tools/state.py
python staging/editorial/L30_20261018_105244/check.py
python staging/editorial/L30_20261018_105244/verify.py
python staging/editorial/tools/check_handoff.py HANDOFF_L31_20261018.md
```
