# L32 — stato di avanzamento (CHIUSO 2026-10-18)

Lotto `L32_20261018_112734` · `data/wanderer/wanderers start.txt` · righe 23–3092 · **805/805 unità**.
Dodicesimo file completo dello staging. Tutti i numeri sono misurati, non stimati.

## Fatto

- `source.json`: 805 unità, 69 contesti, kind 561 `MISSION_TEXT` / 58 `DESCRIPTION` / 53 `VALUE` /
  47 `CONVERSATION` / 45 `DIALOG` / 40 `LOGBOOK` / 1 `TEXT`, **0 `UI_LABEL`**.
- `check.py` derivato da L31 con `NT = {346, 646, 671}`: il riferimento all'outfit
  `"Bondir" Atomic Thruster` (riga 1231, dentro la lista `outfits` della Carrier) e le due `label` di
  salto `alt start` / `alt end`, che il database classifica `CONVERSATION`. `TOKEN_EXC` vuoto,
  11 famiglie di token di dati.
- **Controllo nuovo**: le parentesi quadre `[a, b]` del dispositivo di traduzione (112 unità). Il
  checker verifica che numero di gruppi e numero di alternative per gruppo siano identici al
  sorgente: le alternative si traducono, la struttura no.
- 13 parti scritte a mano, tutte a fine missione: 1–45, 46–100, 101–165, 166–231, 232–290, 291–370,
  371–422, 423–483, 484–555, 556–612, 613–675, 676–736, 737–805
  (45, 55, 65, 66, 59, 80, 52, 61, 72, 57, 63, 61, 69). Ogni parte chiusa con `check.py --range` verde.
- `translation.json`: 805 unità, 24.166 EN → 22.753 IT (0,942), rapporto per unità 0,72–1,61,
  sha256[:16] `bdabdc64ad3b7ce1`.
- `verify.py`: **26 controlli**, `FAIL: 0`, exit 0. Copertura **805/805** asserita: il lotto è
  l'unico del file.
- `review.md`, `REPORT.md`, questo `STATO.md`.

## Regole applicate

- **Voce dei Wanderers ricavata dal testo, non trasportata dalla Coalizione**: frase piana, cortesia
  formale, nessun ordine marcato. Il dispositivo di traduzione parla in modo diverso: la scelta è in
  `review.md` §4.
- **La sintassi delle parentesi quadre è un dato, non stile**: 112 unità con `[parola, parola]`, e ogni
  alternativa deve reggere la frase da sola. Esempi in `review.md` §5.
- **Si riproduce il sorgente**: unità 161 lascia la citazione aperta (la battuta continua nella 162),
  tab e virgolette identici (512/512, 1.305/1.305).
- **Nessun controllo allentato**: due coppie di inglesi quasi identici (516/540, 202/516) sono state
  differenziate in italiano; 562 e 620 riscritte per il rapporto minimo; 797 riscritta perché la resa
  con le parentesi quadre era goffa.
- **Numeri dai file, non dalla memoria**: kind, 26 controlli (contati con `grep -c ' OK'`) e totali
  vengono da misure.
- **Nessuna scrittura sul database**: `state.db` in sola lettura, 805 unità `PENDING`.

## Glossario del lotto

| inglese | italiano | nota |
|---|---|---|
| `Wanderers` | invariato | fazione (decisione 32) |
| `the Eye` | **l'Occhio** | il cunicolo, così chiamato dai Wanderers |
| `the Molt` | **la Muta** | la trasformazione; `molt` = muta |
| `Keepers` (dei Pug) | **Custodi** | `Keepers of the Eye` → Custodi dell'Occhio |
| `Unfettered` (Hai) | **Slegati** | glossario di L29 |
| `unfettered humans` (gli Alphas) | **umani senza freni** | distinto da «Slegati»: sono i Pug a chiamare così gli Alphas |
| `Alphas` | invariato | la specie nemica |
| `jump drive` / `hyperdrive` | motore di salto / iperpropulsore | glossario generale |
| `Carrier` / `Cruiser` | invariati | classi di nave della Marina |
| `speaking machine` / `translation device` | macchina parlante / dispositivo di traduzione | due oggetti distinti |
| `jump drive` + `portale? identità? unità?` | le parentesi restano, le alternative si traducono | |

Restano invariati specie, pianeti, sistemi e persone: `Hai`, `Pug`, `Quarg`, `Korath`, `Hai-home`,
`Alta Hai`, `Vara Ke'sok`, `Varu Mer'ek`, `Cloudfire`, `Darkcloak`, `Farpoint`, `Avalon`, `Sko'karak`,
`Tik Klai`, `Ap'arak`, `Prakacha'a`, `Hi Yahr`, `Chirr'ay'akai`, `Sayari`, `Eruk`, `Iktat Rek`,
`Melaka Esta'a`, `Emeka'a Isai`, `Sobari Tele'ek`, `Elias Hanover`, `Danforth`, `Osen`, `Nguyen`.

## Limiti dichiarati

- **Nessun rendering nel gioco.** Le 805 unità non sono mai state caricate da Endless Sky.
- **Nessuna approvazione.** `APPROVED 364 · PENDING 32.560`, invariato.
- **Lacuna di inventario diversa da L30**: le 12 righe `log "Categoria" "Nome" `testo`` producono una
  sola unità per riga, e quell'unità è il **testo** del diario (quindi tradotto); categoria e nome non
  sono inventariati e restano in inglese. In L30 l'unità prodotta era la categoria e il testo si
  perdeva. Dettaglio in `review.md` §7.
- **Glossario non riconciliato** con i file non ancora affrontati.

## Prossimo passo

`wanderers start.txt` è chiuso: L33 parte da **`data/wanderer/wanderers middle.txt`** (righe 22–3601,
731 unità, 22.378 parole, 75 contesti, tab/virgolette 408/1.002, confine fine file), misurato con
`state.py` + query su `state.db`, non dedotto. Prosegue l'arco dei Wanderers con lo stesso lessico
(Occhio, Muta, Custodi, Slegati).
Sequenza: `export_section.py` → ricognizione dei `kind` (qui 11 `UI_LABEL`: non copiare `NT` di L32) →
`check.py` derivato → parti con `--range` verde → `verify.py` → documenti → handoff e checkpoint.

## Comandi di ripresa

```bash
cd ~/PROGETTI/G-DEV/GAME-SOURCE-LAB/endless-sky-l10n
python staging/editorial/tools/state.py
python staging/editorial/L32_20261018_112734/check.py
python staging/editorial/L32_20261018_112734/verify.py
python staging/editorial/tools/check_handoff.py HANDOFF_L33_20261018.md
```
