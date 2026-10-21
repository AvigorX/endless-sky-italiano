# STATO — L62 · `data/human/culture conversations.txt`

**Lotto chiuso.** 30/30 unità tradotte, righe **566–611** (finestra di export 555–611: la prima unità sta
sulla 566).

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L62_20261018_181058` |
| File | `data/human/culture conversations.txt` (quinto lotto sul file) |
| Unità | **30** (righe 566–611) |
| Parti | **1** — 30 (un solo contesto, chiuso in un lotto) |
| Contesti | **1** — `Scientists at the Pub after a Conference` |
| Tipi | **27 `MISSION_TEXT` + 3 `UI_LABEL`** |
| Parole | 674 EN → 681 IT (**1,010**) |
| Rapporto per unità | **0,81 – 1,37** (gate 0,55–1,90) |
| `UI_LABEL` (`NT`) | **3** — unità **4** `overheard scientists 1`, **15** `overheard scientists 2`, **26** `overheard scientists 3` |
| `DIALOG` / `LOGBOOK` / `CONVERSATION` / `TEXT` | **0 / 0 / 0 / 0** — assenze dichiarate |
| Token `<…>` | **0** — assenza dichiarata |
| Tab · virgolette | **26** · **36** (0 dispari, 0 quadre, 0 backtick) |
| Duplicati inglesi | **0 gruppi** — controllo negativo |
| sha256 `translation.json` | `8b9f92399b32c32a…` |
| `check.py` | **33 controlli**, `FAIL totale: 0` |
| `verify.py` | **36 controlli**, exit **0** |

## Dove siamo nel file

| Voce | Valore |
|---|---|
| Unità prima della 566 | **142** (L58–L61) |
| Unità dopo la 611 | **202** |
| Copertura | **172/374 (46,0%)** |

## Cosa è stato deciso qui

1. **`NT` positivo con tre etichette numerate** (`overheard scientists 1/2/3`): sono **chiavi di salto**,
   restano identiche, compreso il numero finale che il gioco usa per concatenare le scene.
2. **Un solo contesto di 30 unità**, chiuso in una parte sola: nessun taglio arbitrario.
3. **Registro colloquiale colto**: «Insegnare fa schifo», «Che buffo!», «dei gran presuntuosi». È
   accademico che parla da ubriaco, non divulgazione: la sintassi italiana resta piana e colloquiale.
4. **Il lessico tecnico resta tecnico**: `nucleotide evidence` → «prove sui nucleotidi», `proteomic data`
   → «dati proteomici», `synonymous mutations` → «mutazioni sinonime», `positive feedback loop` → «ciclo
   di retroazione positivo». Sono termini che un lettore italiano del campo riconosce.
5. **`grad students` → «dottorandi»**, non «studenti laureati»: nel contesto della ricerca italiana il
   dottorando è la figura equivalente.
6. **Il badge** («Attendee — 35th Annual…») non poteva usare il simbolo `°`: il controllo
   `caratteri non latini` lo rifiuta (0xB0). Reso con **«Trentacinquesimo Congresso»**: il senso resta e
   il carattere sparisce. Il controllo ha avuto ragione, la traduzione è stata riscritta.
7. **Istituzioni**: `Republic Medical Research Agency` → «Agenzia Repubblicana per la Ricerca Medica»;
   `University of Chiron Department of Microbiology` → «Dipartimento di Microbiologia dell'Università di
   Chiron»; `Syndicate` → «il Sindacato».

## Verifica

```bash
cd staging/editorial/L62_20261018_181058
python check.py                 # FAIL totale: 0   (33 controlli)
python verify.py                # exit 0           (36 controlli)
```

## Prossimo passo

**L63** — stesso file, righe **624–711**, **37 unità**, 2 contesti (`Sol-Bound Shuttle` 10,
`Earth Day Blackout` 27), 1.087 parole, tab 35, virgolette 51 con **3 dispari** (unità 18, 29, 31),
1 `UI_LABEL` (unità 30, `way in`), 0 token.
