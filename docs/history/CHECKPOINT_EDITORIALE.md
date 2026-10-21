> **Aggiornamento 2026-10-20 — L332 chiuso: `south jobs.txt` COMPLETO 40/40.** Questo documento è la storia delle **decisioni
> editoriali**: le sue tabelle di stato restano ferme a L153. Lo stato corrente e misurato è in `RIPRESA_L324_20261020.md`:
> staging **31.341 unità · 961.693 EN · 918.875 IT**, **336 directory** con `translation.json`, **334** `verify.py`, residuo
> traducibile **589** (misurato: 1.336 unità su 64 file), **103 file interamente tradotti** su 167. **Tutte le 364 unità `APPROVED`
> stanno in tre file `_ui/`** (`interfaces` 244, `help` 68, `tooltips` 52): prima di tradurre, si guarda la colonna `italian`.

# CHECKPOINT EDITORIALE — Endless Sky IT
> **Nota di formato (2026-10-20).** Questo documento **non è in formato handoff**: è il registro delle decisioni
> editoriali e della tabella dei lotti. `check_handoff.py` su di lui dà **4 OK / 12 FAIL su 16 controlli**
> *per costruzione* — non contiene le righe a contratto (copertura per file, riga del database, residuo, tabella del
> prossimo lotto, hash degli altri tre protetti), e il primo `TOTALE staging` che il checker incontra è quello
> **storico** della tabella L153. Non va «aggiustato» per farle passare: i file **a contratto** sono
> `HANDOFF_L333_20261020.md`, `RIPRESA_L333_20261020.md` e `CHECKPOINT_SESSIONE_20261018.md`, che danno tutti
> `FAIL: 0` (il primo e il terzo su 21 controlli, il secondo su 140).

**Data:** 2026-10-18 · **Workspace:** `endless-sky-l10n` · **Metodo:** traduzione editoriale diretta
**Stato:** 364 unità approvate · **27.802 unità tradotte in staging** · **cinquanta file COMPLETI** · **batch L150–L153 chiuso** (`coalition jobs.txt` al 79,2%) · nessun lotto in corso: **L154 da aprire** (righe 1475–1807, **chiude il file**)
**Lotti chiusi:** L1 · L2 · L3 (4 sezioni) · L4 · L5 · L6 · L7 · L8 · L9 · L10 · L11 · L12 · L13 · L14 · L15 · L16 · L17 · L18 · L19 · L20 · **L21a** · **L21b** · **L22** · **L23** · **L24** · **L25** · **L26** · **L27** · **L28** · **L29** · **L30** · **L31** · **L32** · **L33** · **L34** · **L35** · **L36** · **L37** · **L38** · **L39** · **L40** · **L41** · **L42** · **L43** · **L44** · **L45** · **L46** · **L47** · **L48** · **L49** · **L50** · **L51** · **L52** · **L53** · **L54** · **L55** — tutti con `FAIL totale: 0` e `verify.py` verde. **L'elenco si ferma a L55 per ragioni di spazio:**
i lotti **L56–L93** sono nella tabella §4.2, con i numeri aggiornati. Nessun lotto in corso: **L94 da aprire**
`map planets.txt`: **nessuna unità non tradotta**. Copertura verificata da `L15/verify.py`: 1544 / 1544.
`human missions.txt`: **4.253 unità su 4.253 — file completo** (righe 23–11777, lotti L16–L21a).
`remnant 2 cognizance.txt`: **572 unità su 572 — file completo** (righe 16–1747, lotto L42).
`remnant 2 side missions.txt`: **299 unità su 299 — file completo** (righe 17–775, lotto L43).
`archaeology missions.txt`: **625 unità su 625 — file completo** (righe 16–1718, lotto L44).
`successor 2 ghosts.txt`: **680 unità su 680 — file completo** (righe 37–2167, lotto L45).
`successor 1 prologue.txt`: **345 unità su 345 — file completo** (L46 righe 24–664, L47 righe 680–1024).
`avgi side missions.txt`: **436 unità su 436 — file completo** (L48 righe 26–499, L49 righe 524–1117).
`avgi 0 first contact.txt`: **406 unità su 406 — file completo** (L50 righe 22–402, L51 righe 413–869,
L52 righe 873–1120).
`gegno intro missions.txt`: **276 unità su 276 — file completo** (L53 righe 17–230, L54 righe 280–676,
L55 righe 677–954).
`intro missions.txt`: **637 unità su 637 — file completo** (righe 23–2319, lotto L21b).
`jobs.txt`: **390 unità su 390 — file completo** (righe 15–4600, lotto L22).
`kahet missions.txt`: **1.738 unità su 1.738 — file completo** (lotti L27 righe 39–3048 e L28 righe 3051–5297).
`hai missions.txt`: **823 unità su 823 — file completo** (righe 23–2696, lotto L29).
`lunarium intro.txt`: **730 unità su 730 — file completo** (righe 21–2111, lotto L30).
`heliarch intro.txt`: **663 unità su 663 — file completo** (righe 16–2140, lotto L31).
`wanderers start.txt`: **805 unità su 805 — file completo** (righe 23–3092, lotto L32).

Leggi questo file e riparti da §8. Non serve altro: i report K1–K4 sono chiusi e non vanno rifatti.
**Ripresa a freddo:** `HANDOFF_L33_20261018.md` (workspace root) è il documento da dare a un agente nuovo —
stato misurato, metodo, trappole, divieti, definizione di "lotto fatto", e `staging/editorial/tools/` con gli
strumenti riutilizzabili (`state.py`, `export_section.py`, `next_section.py`, `check_handoff.py`, che dal 2026-10-17 legge i valori dal documento invece di confrontarli con costanti cablate).
`python staging/editorial/tools/state.py` deve uscire **0** prima di iniziare e dopo aver chiuso un lotto.

---

## 1. Obiettivo

Localizzare in italiano Endless Sky traducendo il testo originale come un libro, con il modello della
sessione. Niente nuove pipeline: la traduzione è il prodotto, i controlli sono proporzionati.

---

## 2. Metodo operativo

- Lotti editoriali di **~40.000 parole sorgente** (target della sessione; i lotti L1–L18 erano da ~5.000 e ~20.000),
  divisi in **sezioni coerenti da 3.000–5.000 parole** (per pianeta, per famiglia di equipaggiamenti, per
  capitolo di missioni).
- Per ogni sezione: leggere il contesto → tradurre → rileggere il solo italiano → uniformare i termini.
- Un **checkpoint** alla fine di ogni lotto (questo file, aggiornato) e una directory per lotto.
- Nessun framework nuovo, nessun classificatore, nessun validatore: controlli semplici (completezza,
  tab, virgolette, token, duplicati).
- Le decisioni terminologiche si annotano in `review.md` del lotto, non si spargono nel glossario.

---

## 3. Regole inderogabili

1. `endless-sky` resta `b4aa3bac3` e pulito: **non si tocca**.
2. Non si modificano `state.db`, batch, `inventory_fields.csv`, `glossary.csv`, gli output approvati.
3. Non si applicano le patch K4 (sono pronte ma non ratificate).
4. Non si eseguono build, test di gioco o packaging; le traduzioni non si applicano al gioco.
5. Chiavi, identificatori interni (`label`, `branch`, nomi di oggetti), token `<...>`, tab, virgolette e
   delimitatori restano **esattamente** come nel sorgente.
6. Niente accenti sostitutivi: `è`, `à`, `ù`, non `e'`. Apostrofo dritto. Niente `…`, `«»`, em dash
   (fuori dal set Latin-1 dell'atlante).
7. Si conservano le traduzioni già prodotte: mai sovrascrivere una directory di lotto.

---

## 4. Stato misurato

### 4.1 Database (autorevole, non modificato)

| Voce | Valore |
|---|---:|
| Unità totali | 32.924 |
| `APPROVED` | **364** (B001–B006) |
| `PENDING` | **32.560** |
| Parole inglesi `PENDING` | 976.352 |
| Batch | B001 · B002 · B003 · B004 · B005 · B006 (nessun B007) |
| Ultimo evento | `2026-10-17T14:33:18Z` |
| `state.db` sha256[:16] | `9125282973ddc8b9` |

### 4.2 Staging editoriale (tradotto ma **non** nel database)

| Lotto | File | Righe | Unità | Parole EN | Parole IT |
|---|---|---|---:|---:|---:|
| L1 | `data/map planets.txt` | 3851–4295 | 120 | 5.230 | 5.167 |
| L2 | `data/map planets.txt` | 4308–4781 | 101 | 5.552 | 5.472 |
| L3 (sezione 1) | `data/map planets.txt` | 4790–5121 | 79 | 4.509 | 4.506 |
| L3b (sezione 2) | `data/map planets.txt` | 5129–5456 | 84 | 4.504 | 4.516 |
| L3c (sezione 3) | `data/map planets.txt` | 5465–5829 | 84 | 4.597 | 4.563 |
| L3d (sezione 4) | `data/map planets.txt` | 5836–6371 | 122 | 6.469 | 6.412 |
| L4 | `data/map planets.txt` | 6383–6802 | 83 | 4.734 | 4.752 |
| L5 | `data/map planets.txt` | 17–356 | 84 | 4.632 | 4.578 |
| L6 | `data/map planets.txt` | 357–728 | 84 | 4.586 | 4.564 |
| L7 | `data/map planets.txt` | 733–1077 | 84 | 4.452 | 4.385 |
| L8 | `data/map planets.txt` | 1082–1389 | 77 | 4.534 | 4.486 |
| L9 | `data/map planets.txt` | 1395–1820 | 82 | 4.523 | 4.460 |
| L10 | `data/map planets.txt` | 1826–2163 | 81 | 4.549 | 4.567 |
| L11 | `data/map planets.txt` | 2171–2551 | 80 | 4.597 | 4.629 |
| L12 | `data/map planets.txt` | 2555–2908 | 88 | 4.471 | 4.514 |
| L13 | `data/map planets.txt` | 2913–3231 | 79 | 4.585 | 4.592 |
| L14 | `data/map planets.txt` | 3239–3607 | 83 | 4.470 | 4.534 |
| L15 | `data/map planets.txt` | 3614–3845 | 49 | 2.693 | 2.756 |
| L16 | `data/human/human missions.txt` | 23–562 | 181 | 4.986 | 4.745 |
| L17 | `data/human/human missions.txt` | 568–980 | 133 | 4.128 | 3.788 |
| L18 | `data/human/human missions.txt` | 985–1806 | 187 | 4.255 | 4.050 |
| L19 | `data/human/human missions.txt` | 1811–6428 | 1.611 | 39.968 | 37.324 |
| L20 | `data/human/human missions.txt` | 6432–10806 | 1.676 | 40.112 | 38.248 |
| L21a | `data/human/human missions.txt` | 10812–11777 | 465 | 11.046 | 10.356 |
| L21b | `data/human/intro missions.txt` | 23–2319 | 637 | 19.451 | 17.681 |
| L22 | `data/human/jobs.txt` | 15–4600 | 390 | 5.823 | 5.969 |
| L23 | `data/human/deep missions.txt` | 16–4293 | 1.355 | 38.724 | 36.319 |
| L24 | `data/remnant/remnant 1 introduction.txt` | 23–3923 | 1.250 | 41.087 | 38.140 |
| L25 | `data/coalition/coalition missions.txt` | 16–2907 | 1.174 | 37.459 | 35.851 |
| L26 | `data/coalition/coalition missions.txt` | 2913–3868 | 406 | 10.765 | 10.151 |
| L27 | `data/kahet/kahet missions.txt` | 39–3048 | 917 | 35.520 | 32.640 |
| L28 | `data/kahet/kahet missions.txt` | 3051–5297 | 821 | 30.796 | 27.914 |
| L29 | `data/hai/hai missions.txt` | 23–2696 | 823 | 23.926 | 22.373 |
| L30 | `data/coalition/lunarium intro.txt` | 21–2111 | 730 | 29.208 | 28.079 |
| L31 | `data/coalition/heliarch intro.txt` | 16–2140 | 663 | 21.729 | 20.845 |
| L32 | `data/wanderer/wanderers start.txt` | 23–3092 | 805 | 24.166 | 22.753 |
| L33 | `data/wanderer/wanderers middle.txt` | 22–3601 | 731 | 22.378 | 21.188 |
| L34 | `data/human/free worlds 0 prologue.txt` | 16–2502 | 703 | 18.612 | 17.855 |
| L35 | `data/human/free worlds 1 start.txt` | 16–2343 | 663 | 21.140 | 20.273 |
| L36 | `data/human/free worlds 2 middle.txt` | 16–2336 | 552 | 16.290 | 15.323 |
| L37 | `data/human/free worlds 3 checkmate.txt` | 16–2463 | 482 | 16.244 | 15.239 |
| L38 | `data/human/free worlds 3 reconciliation.txt` | 31–2729 | 596 | 21.021 | 20.228 |
| L39 | `data/human/free worlds 4 epilogue.txt` | 22–341 | 114 | 3.487 | 3.209 |
| L40 | `data/human/free worlds side plots.txt` | 18–888 | 211 | 5.683 | 5.339 |
| L41 | `data/human/free worlds war jobs.txt` | 16–927 | 72 | 1.124 | 1.140 |
| L42 | `data/remnant/remnant 2 cognizance.txt` | 16–1747 | 572 | 22.761 | 21.522 |
| L43 | `data/remnant/remnant 2 side missions.txt` | 17–775 | 299 | 10.539 | 9.870 |
| L44 | `data/sheragi/archaeology missions.txt` | 16–1718 | 625 | 18.966 | 17.522 |
| L45 | `data/successors/successor 2 ghosts.txt` | 37–2167 | 680 | 18.302 | 17.736 |
| L46 | `data/successors/successor 1 prologue.txt` | 24–664 | 221 | 7.180 | 6.973 |
| L47 | `data/successors/successor 1 prologue.txt` | 680–1024 | 124 | 4.128 | 4.032 |
| L48 | `data/avgi/avgi side missions.txt` | 26–499 | 180 | 5.627 | 5.297 |
| L49 | `data/avgi/avgi side missions.txt` | 524–1117 | 256 | 7.606 | 7.324 |
| L50 | `data/avgi/avgi 0 first contact.txt` | 22–402 | 119 | 4.399 | 4.139 |
| L51 | `data/avgi/avgi 0 first contact.txt` | 413–869 | 152 | 4.314 | 3.971 |
| L52 | `data/avgi/avgi 0 first contact.txt` | 873–1120 | 135 | 3.538 | 3.373 |
| L53 | `data/gegno/gegno intro missions.txt` | 17–230 | 89 | 4.287 | 3.896 |
| L54 | `data/gegno/gegno intro missions.txt` | 280–676 | 159 | 5.975 | 5.274 |
| L55 | `data/gegno/gegno intro missions.txt` | 677–954 | 28 | 1.061 | 1.009 |
| L56 | `data/gegno/gegno I corroboration.txt` | 29–904 | 171 | 5.671 | 5.138 |
| L57 | `data/gegno/gegno I corroboration.txt` | 943–1287 | 127 | 4.974 | 4.514 |
| L58 | `data/human/culture conversations.txt` | 25–209 | 43 | 1.610 | 1.532 |
| L59 | `data/human/culture conversations.txt` | 225–423 | 42 | 1.475 | 1.402 |
| L60 | `data/human/culture conversations.txt` | 437–495 | 31 | 661 | 626 |
| L61 | `data/human/culture conversations.txt` | 511–552 | 26 | 394 | 355 |
| L62 | `data/human/culture conversations.txt` | 566–611 | 30 | 674 | 681 |
| L63 | `data/human/culture conversations.txt` | 624–711 | 37 | 1.087 | 1.025 |
| L64 | `data/human/culture conversations.txt` | 723–810 | 42 | 1.652 | 1.598 |
| L65 | `data/human/culture conversations.txt` | 819–920 | 43 | 1.666 | 1.676 |
| L66 | `data/human/culture conversations.txt` | 930–1053 | 45 | 1.239 | 1.176 |
| L67 | `data/human/culture conversations.txt` | 1062–1122 | 35 | 811 | 787 |
| L68 | `data/successors/successor 2 ghosts myurej.txt` | 16–113 | 49 | 1.502 | 1.447 |
| L69 | `data/successors/successor 2 ghosts myurej.txt` | 118–197 | 31 | 687 | 704 |
| L70 | `data/successors/successor 2 ghosts myurej.txt` | 215–307 | 39 | 1.028 | 953 |
| L71 | `data/successors/successor 2 ghosts myurej.txt` | 311–401 | 42 | 1.632 | 1.546 |
| L72 | `data/successors/successor 2 ghosts myurej.txt` | 407–531 | 50 | 1.763 | 1.679 |
| L73 | `data/successors/successor 2 ghosts aqrabe.txt` | 23–158 | 51 | 1.330 | 1.281 |
| L74 | `data/successors/successor 2 ghosts aqrabe.txt` | 161–255 | 38 | 1.106 | 1.077 |
| L75 | `data/successors/successor 2 ghosts aqrabe.txt` | 259–400 | 61 | 1.889 | 1.796 |
| L76 | `data/successors/successor 2 ghosts aqrabe.txt` | 404–478 | 30 | 822 | 788 |
| L77 | `data/successors/successor side missions.txt` | 17–220 | 63 | 1.909 | 1.829 |
| L78 | `data/successors/successor side missions.txt` | 224–325 | 53 | 1.109 | 1.060 |
| L79 | `data/successors/successor side missions.txt` | 336–381 | 29 | 620 | 611 |
| L80 | `data/successors/successor side missions.txt` | 416–453 | 19 | 363 | 354 |
| L81 | `data/successors/predecessors.txt` | 17–196 | 22 | 106 | 106 |
| L82 | `data/successors/predecessors.txt` | 208–381 | 15 | 220 | 220 |
| L83 | `data/successors/predecessors.txt` | 446–520 | 11 | 153 | 166 |
| L84 | `data/successors/predecessors.txt` | 534–608 | 4 | 169 | 177 |
| L85 | `data/successors/predecessors.txt` | 648–782 | 7 | 250 | 258 |
| L86 | `data/successors/successor outfits.txt` | 19–235 | 21 | 1021 | 1042 |
| L87 | `data/successors/successor outfits.txt` | 251–409 | 13 | 572 | 591 |
| L88 | `data/successors/successor outfits.txt` | 429–560 | 10 | 329 | 343 |
| L89 | `data/successors/successor outfits.txt` | 574–647 | 12 | 347 | 388 |
| L90 | `data/successors/successor culture conversations.txt` | 23–142 | 34 | 1.098 | 1.014 |
| L91 | `data/successors/successor culture conversations.txt` | 155–229 | 34 | 1.117 | 1.084 |
| L92 | `data/successors/successor culture conversations.txt` | 230–351 | 46 | 1.848 | 1.775 |
| L93 | `data/coalition/coalition culture conversations.txt` | 24–66 | 31 | 1.744 | 1.616 |
| L94 | `data/coalition/coalition culture conversations.txt` | 81–133 | 36 | 2.321 | 2.115 |
| L95 | `data/coalition/coalition culture conversations.txt` | 148–190 | 27 | 1.382 | 1.242 |
| L96 | `data/coalition/coalition culture conversations.txt` | 192–234 | 27 | 2.248 | 2.023 |
| L97 | `data/coalition/coalition culture conversations.txt` | 251–462 | 36 | 2.269 | 2.142 |
| L98 | `data/hai/hai culture conversations.txt` | 1–105 | 39 | 1.262 | 1.180 |
| L99 | `data/hai/hai culture conversations.txt` | 106–211 | 38 | 1.183 | 1.151 |
| L100 | `data/hai/hai culture conversations.txt` | 212–320 | 44 | 1.587 | 1.512 |
| L101 | `data/hai/hai culture conversations.txt` | 321–386 | 26 | 971 | 938 |
| L102 | `data/quarg/quarg missions.txt` | 1–117 | 48 | 1.675 | 1.632 |
| L103 | `data/quarg/quarg missions.txt` | 118–249 | 42 | 956 | 882 |
| L104 | `data/quarg/quarg missions.txt` | 250–334 | 27 | 631 | 597 |
| L105 | `data/quarg/quarg missions.txt` | 335–506 | 61 | 2.155 | 2.073 |
| L106 | `data/korath/korath missions.txt` | 1–120 | 25 | 854 | 833 |
| L107 | `data/korath/korath missions.txt` | 121–212 | 38 | 1.742 | 1.683 |
| L108 | `data/korath/korath missions.txt` | 216–335 | 36 | 737 | 730 |
| L109 | `data/korath/korath missions.txt` | 338–451 | 33 | 1.205 | 1.188 |
| L110 | `data/korath/korath missions.txt` | 474–580 | 26 | 730 | 669 |
| L111 | `data/_ui/tooltips.txt` | 16–328 | 104 | 1.810 | 1.848 |
| L112 | `data/_ui/tooltips.txt` | 331–688 | 120 | 1.813 | 2.044 |
| L113 | `data/_ui/tooltips.txt` | 691–973 | 96 | 1.808 | 1.864 |
| L114 | `data/_ui/tooltips.txt` | 976–1309 | 110 | 1.816 | 1.905 |
| L115 | `data/_ui/tooltips.txt` | 1312–1566 | 104 | 1.819 | 1.839 |
| L116 | `data/_ui/tooltips.txt` | 1569–1865 | 133 | 3.018 | 2.995 |
| L117 | `data/human/pirate jobs.txt` | 20–1624 | 98 | 1.804 | 1.715 |
| L118 | `data/human/pirate jobs.txt` | 1627–2955 | 104 | 1.753 | 1.774 |
| L119 | `data/human/pirate jobs.txt` | 2958–3706 | 77 | 1.223 | 1.246 |
| L120 | `data/human/campaign events.txt` | 28–242 | 52 | 2.255 | 2.193 |
| L121 | `data/human/campaign events.txt` | 282–1332 | 56 | 2.486 | 2.404 |
| L122 | `data/human/campaign events.txt` | 1338–3468 | 42 | 2.220 | 2.191 |
| L123 | `data/human/ships.txt` | 78–2044 | 54 | 2.364 | 2.483 |
| L124 | `data/human/ships.txt` | 2102–3422 | 29 | 1.539 | 1.603 |
| L125 | `data/human/ships.txt` | 3491–4266 | 20 | 1.180 | 1.200 |
| L126 | `data/incipias/incipias first contact.txt` | 22–218 | 55 | 1.788 | 1.626 |
| L127 | `data/incipias/incipias first contact.txt` | 224–331 | 63 | 1.697 | 1.556 |
| L128 | `data/incipias/incipias first contact.txt` | 343–439 | 43 | 1.177 | 1.100 |
| L129 | `data/human/boarding missions.txt` | 15–386 | 89 | 852 | 819 |
| L130 | `data/human/boarding missions.txt` | 417–686 | 75 | 2.087 | 2.067 |
| L131 | `data/human/boarding missions.txt` | 695–959 | 76 | 1.632 | 1.594 |
| L132 | `data/hai/unfettered side missions.txt` | 17–229 | 84 | 2.055 | 1.850 |
| L133 | `data/hai/unfettered side missions.txt` | 237–477 | 67 | 2.007 | 1.821 |
| L134 | `data/hai/unfettered side missions.txt` | 494–510 | 8 | 356 | 323 |
| L135 | `data/starts.txt` | 18–130 | 32 | 1.485 | 1.448 |
| L136 | `data/starts.txt` | 135–167 | 15 | 587 | 559 |
| L137 | `data/starts.txt` | 172–210 | 17 | 802 | 786 |
| L138 | `data/starts.txt` | 215–358 | 47 | 1.356 | 1.295 |
| L139 | `data/starts.txt` | 365–366 | 2 | 6 | 6 |
| L140 | `data/hai/unfettered 0 prologue.txt` | 22–81 | 25 | 405 | 375 |
| L141 | `data/hai/unfettered 0 prologue.txt` | 83–132 | 20 | 591 | 566 |
| L142 | `data/hai/unfettered 0 prologue.txt` | 139–201 | 20 | 493 | 456 |
| L143 | `data/hai/unfettered 0 prologue.txt` | 214–317 | 30 | 723 | 643 |
| L144 | `data/hai/unfettered 0 prologue.txt` | 367–420 | 20 | 486 | 406 |
| L145 | `data/hai/unfettered 0 prologue.txt` | 423–459 | 13 | 703 | 635 |
| L146 | `data/hai/unfettered 0 prologue.txt` | 460–530 | 19 | 656 | 586 |
| L147 | `data/coalition/coalition jobs.txt` | 16–293 | 30 | 437 | 412 |
| L148 | `data/coalition/coalition jobs.txt` | 309–435 | 16 | 205 | 207 |
| L149 | `data/coalition/coalition jobs.txt` | 455–634 | 18 | 246 | 268 |
| L150 | `data/coalition/coalition jobs.txt` | 639–794 | 14 | 234 | 216 |
| L151 | `data/coalition/coalition jobs.txt` | 799–1171 | 37 | 302 | 316 |
| L152 | `data/coalition/coalition jobs.txt` | 1191–1359 | 21 | 527 | 531 |
| L153 | `data/coalition/coalition jobs.txt` | 1360–1469 | 20 | 582 | 601 |
| **Totale** | | | **27.802** | **875.439** | **831.788** |

TOTALE staging: 27802 unità · 875439 EN · 831788 IT

Le 27.802 unità sono **ancora `PENDING` nel database**: sono tradotte solo in staging. Non vanno sommate
alle 364 approvate. **`map planets.txt` è al 100% in staging** (1.544 unità su 1.544);
**`human missions.txt`, `intro missions.txt`, `jobs.txt`, `deep missions.txt`, `remnant 1 introduction.txt`
e `coalition missions.txt` al 100%** (4.253, 637, 390, 1.355, 1.250 e 1.580 unità). `kahet missions.txt`
è al **100%** (1.738 su 1.738), `hai missions.txt` è al **100%** (823 su 823), `lunarium intro.txt`
è al **100%** (730 su 730), `heliarch intro.txt` è al **100%** (663 su 663), `wanderers start.txt`
è al **100%** (805 su 805), `wanderers middle.txt` è al **100%** (731 su 731),
`free worlds 0 prologue.txt` è al **100%** (703 su 703), `free worlds 1 start.txt` è al **100%**
(663 su 663), `free worlds 2 middle.txt` è al **100%** (552 su 552), `free worlds 3 checkmate.txt` è al **100%**
(482 su 482), `free worlds 3 reconciliation.txt` è al **100%** (596 su 596) e
`free worlds 4 epilogue.txt` è al **100%** (114 su 114) e `free worlds side plots.txt` è al **100%**
(211 su 211). Con L39 la **campagna principale** delle Free Worlds è completa (prologo, start, middle,
checkmate, reconciliation, epilogue); con L40 lo sono anche le **trame secondarie**; con L41 anche i
**lavori di guerra** delle Free Worlds (72 unità, il lotto più piccolo della serie); con L42 il primo
capitolo della **seconda campagna Remnant** (`Cognizance 1–38`, 572 unità, 22.761 parole); con L43 le
**trame secondarie Remnant** (`Visit to Paradise`, `Celebration`, `Teciimach Deployment`,
`Shattered Light 2–6`, `Scent of Rain`, `Will Not Someone Please Think Of The Children`; 299 unità,
10.539 parole); con L44 la linea **Sheragi** (`Deep Archaeology` 1–7, la difesa di Zug, il cubo, Mammon,
il Museo Hai, la Spada di Smeraldo; 625 unità, 18.966 parole) e con L45 la linea **Successors**
(`Ghosts Prelude`, `QSI 1–3`, `Ghosts 1–20`, i due nodi di conversazione, il matrimonio Chydiyi–Myurej,
la cittadella di Kasii-Sola, la nave da guerra di famiglia; 680 unità, 18.302 parole, **16 nodi
`CONVERSATION`**), che portano a **venticinque** i file coperti al 100%; con L46 e L47 il **prologo dei
Successors** (`Entering the Scar`, `First Contact 1–3`, `Kaatrij Monoglot Prompt`, `Kaatrij First
Contact`, `Trusted`; 345 unità, 11.308 parole), che porta a **ventisei** i file completi; con L48 e L49 la
linea **Avgi** (`Park Politics`, `Zapchannel Energy`, `Cylinder Construction`, `Infocourier Encounter`,
`Twilight Tavern Guard`, `Atomics Testing 1–2`; 436 unità, 13.233 parole), che porta a **ventisette** i
file completi; con L50–L52 la **prima linea Avgi** (`Avgi: Lost in Twilight`, `Avgi: First Contact`,
`Avgi: Humans From the Deep`, `Defend Ensemble 1–2`, `Scout Rescue`, `Frontline Combat`, `Dissonance
Outreach 0.5` e `Dissonance Outreach`, `Twilight Escape 1–3`, `Discovery of Decet Magnetar`; 406 unità,
12.251 parole), che porta a **ventotto**; con L53–L55 la **linea Gegno** (`First Contact: Gegno Vi`,
`Visit Quarg in Gegno Space`, `Discover Hostile Quarg`, `Giaru Gegno: Quarg Contact`, `Gegno Quarg
Direction to Ringworld`, `Giaru Gegno: Revisit`, `Suspicious Scin`, `First Contact: Gegno Scin`,
`Exploration Nudge`, `Genocide Defense`, `Unwelcoming`, `conversation:interfered with duel`; 276 unità,
11.323 parole), che porta a **ventinove**; infine con **L56+L57** `gegno I corroboration.txt`
(`Passive-Aggressive Observations`, `Foreign Spectator I`, `Brief Bystander`, `Scin on Cyife`, `Battle
over Zydee`, `Gegno Suspicions`, `Return to Giaru Gegno`, `Gegno Anticipation`, `Gegno Intervention`,
`Acquiescence`, `Gegno Asteroid Mining Prologue`; **298 unità**, 10.645 parole), che porta a **trenta**.
Con **L58–L67** `culture conversations.txt` arriva al **100%** (374 unità su dieci lotti, 11.269 EN →
10.858 IT) ed è il **trentunesimo file completo**. Con **L68** si apre invece un **file nuovo che NON è completo** — `successor 2 ghosts myurej.txt` — e con
**L69**, **L70**, **L71** e **L72** arriva a **211 unità su 211 (100%)**, 6.612 EN → 6.329 IT: il file è
**completo** ed è il **trentaduesimo** dello staging. Con **L73** si apre un altro file Successors,
`successor 2 ghosts aqrabe.txt` **completo** (180 unità su 180) dopo L73–L76: **trentatreesimo file completo**.

### 4.3 Da tradurre

| Voce | Valore |
|---|---:|
| Unità `PENDING` non ancora in staging | 4.810 |
| di cui nomi di nodo `label` non traducibili | 13 |
| **Unità realmente traducibili residue (misurate)** | **4.797** su **116 file** |
| Parole inglesi residue (misurate) | 101.660 |
| Residuo secondo la formula di `state.py` (sottrae due volte le label già in staging) | 4.128 |
| `successor 2 ghosts myurej.txt`: unità tradotte | **211 di 211 (100%)** — file completo |
| `successor 2 ghosts aqrabe.txt`: unità tradotte | **180 di 180 (100%)** — file completo |
| `map planets.txt`: unità tradotte | **1.544 (tutto il file)** |
| `map planets.txt`: unità **mai affrontate** | **0** |
| `human missions.txt`: unità tradotte | **4.253 (file completo)** |
| `human missions.txt`: unità **mai affrontate** | **0** |
| `intro missions.txt`: unità tradotte | **637 (file completo)** |
| `intro missions.txt`: unità **mai affrontate** | **0** |
| `jobs.txt`: unità tradotte | **390 (file completo)** |
| `jobs.txt`: unità **mai affrontate** | **0** |
| `deep missions.txt`: unità tradotte | **1.355 (file completo)** |
| `deep missions.txt`: unità **mai affrontate** | **0** |
| `remnant 1 introduction.txt`: unità tradotte | **1.250 (file completo)** |
| `remnant 1 introduction.txt`: unità **mai affrontate** | **0** |
| `remnant 2 cognizance.txt`: unità tradotte | **572 (file completo)** |
| `remnant 2 cognizance.txt`: unità **mai affrontate** | **0** |
| `remnant 2 side missions.txt`: unità tradotte | **299 (file completo)** |
| `remnant 2 side missions.txt`: unità **mai affrontate** | **0** |
| `archaeology missions.txt`: unità tradotte | **625 (file completo)** |
| `archaeology missions.txt`: unità **mai affrontate** | **0** |
| `coalition missions.txt`: unità tradotte | **1.580 (file completo)** |
| `coalition missions.txt`: unità **mai affrontate** | **0** |
| `kahet missions.txt`: unità tradotte | **1.738 (file completo)** |
| `kahet missions.txt`: unità **mai affrontate** | **0** |
| `hai missions.txt`: unità tradotte | **823 (file completo)** |
| `hai missions.txt`: unità **mai affrontate** | **0** |
| `lunarium intro.txt`: unità tradotte | **730 (file completo)** |
| `lunarium intro.txt`: unità **mai affrontate** | **0** |
| `heliarch intro.txt`: unità tradotte | **663 (file completo)** |
| `heliarch intro.txt`: unità **mai affrontate** | **0** |
| `wanderers start.txt`: unità tradotte | **805 (file completo)** |
| `wanderers start.txt`: unità **mai affrontate** | **0** |
| `wanderers middle.txt`: unità tradotte | **731 (file completo)** |
| `wanderers middle.txt`: unità **mai affrontate** | **0** |
| `free worlds 0 prologue.txt`: unità tradotte | **703 (file completo)** |
| `free worlds 0 prologue.txt`: unità **mai affrontate** | **0** |
| `free worlds 1 start.txt`: unità tradotte | **663 (file completo)** |
| `free worlds 1 start.txt`: unità **mai affrontate** | **0** |
| `free worlds 2 middle.txt`: unità tradotte | **552 (file completo)** |
| `free worlds 2 middle.txt`: unità **mai affrontate** | **0** |
| `free worlds 3 checkmate.txt`: unità tradotte | **482 (file completo)** |
| `free worlds 3 checkmate.txt`: unità **mai affrontate** | **0** |
| `free worlds 3 reconciliation.txt`: unità tradotte | **596 (file completo)** |
| `free worlds 3 reconciliation.txt`: unità **mai affrontate** | **0** |
| `free worlds 4 epilogue.txt`: unità tradotte | **114 (file completo)** |
| `free worlds 4 epilogue.txt`: unità **mai affrontate** | **0** |
| `free worlds side plots.txt`: unità tradotte | **211 (file completo)** |
| `free worlds side plots.txt`: unità **mai affrontate** | **0** |
| `free worlds war jobs.txt`: unità tradotte | **72 (file completo)** |
| `free worlds war jobs.txt`: unità **mai affrontate** | **0** |

### 4.4 Questioni tecniche aperte (bloccano il "gioco in italiano", non la traduzione)

- **Nessun loader i18n**: `UniverseObjects::Load` legge solo `<resources>/data`. Servono
  `Preferences::{Get,Set}Language` e una radice `Resources()/l10n/<lang>` in `GameData::BeginLoad`.
- **Font**: atlante esteso a 224 celle e `Font.cpp` patchato **nella copia di lavoro** `endless-sky-mingw`
  (4 file modificati, build e 46/46 test verdi). **Rendering a schermo non osservato.**
- **Stringhe inglesi generate dal motore** dentro i token (`<destination>` → "Vail in the Sol system",
  `<fare>` → "4 passengers"): restano inglesi anche con i dati tradotti.
- **Patch K4 pronte e non applicate**: `0001-placeholder-families.patch` (validatore) e
  `0002-inventory-label-classification.patch` (classificazione delle 630 `label`). Il validatore attuale
  non vede i token comando (`<View star map>`).

---

## 5. Riferimenti (non ricostruire a memoria)

| Cosa | Percorso |
|---|---|
| Stato e batch | `endless-sky-l10n/state.db` (sola lettura) |
| Glossario (81 voci, vincolante) | `endless-sky-l10n/glossary.csv` |
| Style guide | `endless-sky-l10n/style_guide.md` |
| Output approvati | `endless-sky-l10n/output/l10n-it/data/_ui/{interfaces,tooltips,help}.txt` |
| Inventario e rischi | `endless-sky-l10n/staging/inventory_fields.csv` |
| L1 | `staging/editorial/L1_20261017_174418/` (report, source, translation) |
| L2 | `staging/editorial/L2_20261017_175057/` (report, source, translation) |
| L3 (sezione 1) | `staging/editorial/L3_20261017_180114/` (report, source, translation, parts, check) |
| L3b (sezione 2) | `staging/editorial/L3b_20261017_180831/` (report, source, translation, parts, check) |
| L3c (sezione 3) | `staging/editorial/L3c_20261017_181211/` (report, source, translation, parts, check) |
| L3d (sezione 4) | `staging/editorial/L3d_20261017_181538/` (report, source, translation, parts, check) |
| L4 | `staging/editorial/L4_20261017_182100/` (report, source, translation, parts, check) |
| L5 | `staging/editorial/L5_20261017_184433/` (report, source, translation, parts, check) |
| L6 | `staging/editorial/L6_20261017_184826/` (report, source, translation, parts, check) |
| L7 | `staging/editorial/L7_20261017_185227/` (report, source, translation, parts, check) |
| L8 | `staging/editorial/L8_20261017_185714/` (report, source, translation, parts, check) |
| L9 | `staging/editorial/L9_20261017_192218/` (report, source, translation, parts, check) |
| L10 | `staging/editorial/L10_20261017_192600/` (report, source, translation, parts, check) |
| L11 | `staging/editorial/L11_20261017_193303/` (report, source, translation, parts, check) |
| L12 | `staging/editorial/L12_20261017_193627/` (report, source, translation, parts, check) |
| L13 | `staging/editorial/L13_20261017_193954/` (report, source, translation, parts, check) |
| L14 | `staging/editorial/L14_20261017_194328/` (report, source, translation, parts, check) |
| L15 | `staging/editorial/L15_20261017_194639/` (report, source, translation, parts, check, `verify.py` riscritto per la fine file) |
| L16 | `staging/editorial/L16_20261017_195126/` (primo lotto di `human missions.txt`: 5 parts, `check.py` con elenco esplicito delle `label` non tradotte, `verify.py` con controllo del tripletto `log`) |
| L17 | `staging/editorial/L17_20261017_195800/` (4 parts; `check.py` con `TITLES` per escludere i titoli di band/canzoni dal controllo delle parole inglesi) |
| L18 | `staging/editorial/L18_20261017_200248/` (6 parts; primo lotto con `TEXT`: `check.py` verifica la **firma dello spazio** e **compone la `phrase`** in EN e IT, `verify.py` controlla che i 27 frammenti stiano nel blocco e che le opzioni non vuote siano 27) |
| L19 | `staging/editorial/L19_20261017_201414/` (25 parts, 9 sezioni; `check.py` con **39 `label`** in `NT`, `DUP_OK` derivato dai duplicati del sorgente, controllo **caratteri non latini**; `verify.py` indipendente, 17 controlli) |
| L19 (export scartato) | `staging/editorial/L19_20261017_201342/` — solo `source.json` + `NOTE.md`: confine a 40.689 parole cadeva dentro `Care Package to South 1` |
| L20 | `staging/editorial/L20_20261017_203734/` (19 parts; `check.py` con **71 `label`** in `NT` e `TITLES` esteso a `they/them`, `DUP_OK` dal sorgente, controllo caratteri non latini; `verify.py` indipendente, **22 controlli**) |
| L21a | `staging/editorial/L21a_20261017_205715/` (5 parts; coda di `human missions.txt`, `check.py` con **19 non traducibili** = 12 `label` + 7 `label` dentro `conversation`; `verify.py` 22 controlli) |
| L21b (chiuso) | `staging/editorial/L21b_20261017_210204/` (7 parti · 637 unità · 19.451 EN → 17.681 IT · `check.py` FAIL 0 · `verify.py` 24 controlli 0 FAIL · `TOKEN_EXC` per i 5 pronomi) |
| K3 (benchmark placeholder) | `staging/benchmarks/hermes_deepseek_k3_20261017_164617/REPORT.md` |
| K4 (validatore + label) | `staging/benchmarks/k4_20261017_173349/REPORT.md` + `patches/` |
| Testo del gioco | `GAME-SOURCE-LAB/endless-sky/data/` (sola lettura) |

Formato di un lotto: `source.json` (id, riga, contesto, inglese, riga grezza) · `translation.json`
(id, riga, inglese, italiano, ratio) · `review.md` · `REPORT.md`.

---

## 6. Convenzioni terminologiche

- **Registro**: il giocatore è "tu"; equipaggi e collettivi "voi". Niente calchi.
- **Glossario vincolante** per i termini tecnici: nave, scafo, scudi, carico/stiva, carburante, salto,
  iperspazio, spazioporto, fornitore, cantiere, missione/incarico, posti letto, neutralizzare.
- **Nomi propri invariati**: pianeti, sistemi, fazioni, specie, regioni, aziende
  (`New Argentina`, `Tangled Shroud`, `Deep`, `Dirt Belt`, `Hai`, `Avgi`, `Pug`, `Remnant`, `Heliarch`…).
- **Eccezioni deliberate**: `Mars` → Marte, `Earth` → Terra (corpi reali); `Syndicate` → Sindacato;
  `Coalition` → Coalizione *(da ratificare)*; `Paradise World` → Mondo Paradisiaco; `hyperdrive` →
  iperpropulsore; `the Incursion` → l'Incursione; `house X` → Casata X; `Predecessors` → Predecessori.
- **Invariati per scelta**: `Remembrance Day`, `Alpha Wars`, `Turf Wars`, `New Houses` → Nuove Casate
  *(da ratificare)*.
- **Forme**: maiuscola solo alla prima parola nelle etichette; numeri con il punto delle migliaia;
  niente inglese nel testo tranne i termini marcati invariati nel glossario.

---

## 7. Decisioni aperte (brevi, non bloccanti)

1. `Coalition` → **Coalizione**: ratificare (usata in L2, 5 occorrenze).
2. **`Consonance` / "Assemblea delle Entità Consonanti"**: incoerenza in L2 (unità 36 e 59). Scegliere:
   "Consonanza" ovunque, oppure "Entità della Consonance".
3. `Paradise World` → Mondo Paradisiaco: allineare se compare nella UI.
4. `hyperdrive` → iperpropulsore: verificare l'eventuale nome dell'equipaggiamento.
5. `Bunrodean` al plurale: invariato ("i Bunrodean") o adattato ("i Bunrodeani").
6. `New Houses` → Nuove Casate e `Remembrance Day` invariato: ratificare una volta per tutto il corpus.
7. **K4, note contestuali** (non applicare a testi che non le contengono): `discharge` → "scarica",
   `disruption` → "perturbazione" (alternativa "disruzione"), `scrambling` → "disturbo" (già approvato
   in B002), `cloakDisruption` → meccanismo diverso, "disturbo dell'occultamento".
8. **`Successors` invariato** (8 occorrenze in L3) mentre `Predecessors` → Predecessori (2): asimmetria
   accettata in §6. Ratificare "Successori" oppure mantenere l'invariato una volta per tutto il corpus.
9. `the Rim` → **"il Rim"** (1 in L3, forma breve di `Southern Rim`): alternativa "il Margine".
10. `vault` → **caveau** (6 in L3): alternativa "camera blindata". Decidere se il tema Bunrodea ricorre.
11. `wormhole` **invariato** (1 in L3): termine tecnico; l'alternativa narrativa è "varco".
12. **Unità 21 e 70 di L3** hanno lo stesso inglese: tradotte con varianti lessicali per non avere
    duplicati identici nel lotto. Se si vuole la memoria di traduzione rigida, riallineare la 70 alla 21.
13. `the Builders` → **Costruttori** (1 in L6): unico epiteto di specie tradotto invece che invariato.
    Se si preferisce l'invariato "Builders", la modifica è locale (L6 unità 84).
14. `Halite` **invariato** (1 in L7): classe di nave Scin; da uniformare se altrove è reso come nome comune.
15. **Refuso del sorgente** (L7 unità 31): `Cavasaa-Vasa-Tej` → **Cavaasa-Vasa-Tej**. Correzione locale,
    da replicare se il refuso ricompare in altri file.
16. `Twilight Guard` **invariato** (1 in L8): nome di fazione, come `Remnant`/`Unfettered`. Alternativa:
    "Guardia del Crepuscolo".
17. `Bulk Freighter` **invariato** (1 in L8): classe di nave, come `Halite` (L7). Le classi restano
    invariate: ratificare una volta per tutto il corpus.
18. **Secondo refuso del sorgente** (L8 unità 52): `Unlikely many other worlds` → letto "Unlike".
    L'unità 53 contiene inoltre una frase agrammaticale, resa secondo il senso.
19. **`Consonance` invariato** (1 in L9, unità 41): scelta provvisoria coerente con L2 unità 36 ma non con
    L2 unità 59. La ratifica di §7 punto 2 vale per tutto il corpus.
20. **`Bunrodean Hegemony` → Egemonia Bunrodean** (1 in L9): primo uso del nome dello Stato.
21. **`the Core` → "il Nucleo"** (1 in L9): alternativa "il Centro".
22. **Terzo refuso del sorgente** (L9 unità 58): `Kasii-Cavasaa` → **Kasii-Cavaasa**, coerente con
    `Cavaasa-Vasa-Tej` e con L7.
23. **`Confederated Councils of the Outer Rim` → Consigli Confederati del Bordo Esterno (CCOR)** (L10,
    1 occorrenza): necessaria perché l'invariato lasciava visibile l'articolo inglese. **In L6 la forma
    breve `Confederated Councils` è invece invariata**: o si allinea L6, o si accetta la differenza.
24. `CCOR` (acronimo) **invariato** (3 in L10). `Syndicated Shipyards` **invariato** (1 in L10): ragione
    sociale.
25. `Aberrations` → **"Aberrant"** (1 in L10): un solo nome per la fazione e per i suoi individui.
    Alternativa: "Aberrazioni" per gli individui.
26. `Paradise Planets` → **Pianeti Paradisiaci** (1 in L10), coerente con `Paradise World` → Mondo
    Paradisiaco.
27. **Istituzioni lasciate in inglese** (elenco in crescita): `Starlit University`, `Royal University of
    Dogen`, `Military Academy of Fuhtiiski`, `Academy of Planetary Sciences` (L11). Ratificare in blocco.
28. `Syndicated Systems` e `Syndicated Shipyards` **invariati** (L10, L11): ragioni sociali. Se si traduce
    "Sindacato", cambiano due lotti.
29. **`Confederated Councils`, stato delle tre scelte**: invariato in L6, tradotto in "Consigli Confederati"
    in L10 e L12. La ratifica deve chiudere la questione e decidere se allineare L6 (§7 punto 23).
30. **`Jupiter` → Giove** (2 in L12), `Great Red Spot` → Grande Macchia Rossa: corpi e nomi astronomici
    reali trattati come Marte e Terra.
31. **Unità con inglese identico nel sorgente** (L12 unità 62/64, stazioni `Iritoroost` e `Ironfirth`):
    italiano differenziato in due punti per evitare duplicati nel lotto; reversibile.
32. `Wanderers` **invariato** (6 in L13): fazione nuova, coerente con `Remnant`/`Heliarch`. Da ratificare.
33. **`House Kaatriij` / `House Kaatrij`**: il sorgente alterna le due grafie (L12 e L13). Non normalizzato:
    se è un refuso, va corretto in entrambi i lotti.
34. **Quarto refuso del sorgente** (L13 unità 37): `Kissara` → **Kisarra**, coerente con il nome del nodo e
    con l'unità 35.
35. **`"tributation"` → "tributazione"** (L14 unità 79): termine inventato; il calco funziona ma se
    ricompare in testi di missione va tenuto identico.
36. **`Earth` / `Mars` / `the Moon`** → Terra / Marte / la Luna (L14): corpi reali, quarta occorrenza della
    stessa eccezione dopo Marte, Terra e Giove.
37. **`void sprites` → "spiriti del vuoto"** (2 in L15): nome di creatura, da ratificare.
38. **`Pulse Laser` → "Laser a impulsi"** (2 in L15): nome di equipaggiamento reso come prodotto; va
    verificato contro `glossary.csv` quando si tradurranno i file degli equipaggiamenti.
39. **`the Assembly` → l'Assemblea** (1 in L15): organo della Consonance, coerente con L2.
40. **Unità con inglese identico** (L15 unità 22/24, lavori di ampliamento dello spazioporto di
    Mosaa-Oa-Vyret): italiano differenziato per evitare duplicati nel lotto; reversibile.
41. **`label` di missione non tradotte** (L16: `not poor`, `no bet`, `nope late`, `remember decline`):
    sono bersagli di `goto`; restano identiche e sono elencate in modo esplicito in `L16/check.py`.
42. **Riga `log` tripla** (L16 riga 555): ``log `Minor People` `Puny` `A poodle ...` `` → tre unità sulla
    stessa riga (categoria, nome, testo). Chi applica le traduzioni deve ricomporre la riga con tutte e tre.
43. **`Minor People` → "Personaggi minori"** (L16 unità 176): categoria di diario mostrata al giocatore.
    Se il gioco la usasse come chiave di raggruppamento la traduzione spezzerebbe il gruppo: **non
    verificato** (nessun avvio). Reversibile.
44. **`Stray Dog` → "Cane randagio"** (L16 unità 56, `name` della missione): nome mostrato nell'elenco
    missioni. `Pookie` resta invariato perché nome proprio (unità 40 e 45, duplicato ammesso).
45. **Nomi di animali e persone invariati** (L16: `Pookie`, `Puny`, `Bleedbug`, `Doom`, `Zinc`, `Walters`,
    `Pemefrey`, `Pocahontas`): da ratificare insieme agli altri nomi propri.
46. **Titoli di band e canzoni invariati** (L17: `There Might Be Riots`, `Henhouse In Your Soul`,
    `Sad Archie`): restano in inglese per scelta, come i nomi propri. `check.py` di L17 li sottrae dal testo
    prima del controllo delle parole residue (`TITLES`); l'elenco è esplicito, non una deroga generale.
47. **`rimway` invariato** (3 in L17): passaggio principale dell'anello di una stazione. Se compare in altri
    file va tenuta la stessa resa.
48. **`phrase` = frammenti concatenati, non frasi** (L18, `generic human package offer`, 27 unità `TEXT`):
    lo spazio iniziale/finale fa parte del testo e i saluti devono chiudere il periodo, perché lo slot
    successivo inizia con la maiuscola. I verbi non portano participi concordati perché il soggetto può
    essere maschile o femminile. `check.py` compone la frase e la verifica in EN e IT.
49. **`label` non tradotte anche nel terzo lotto di missioni** (L18: `shoot and die`, `more money`,
    `shoot and live`): elencate in `check.py` (`NT`) insieme ai due frammenti di pura punteggiatura (164, 180).
50. **`Argosy Modificata`** (L18, 1): classe di nave resa come prodotto. Da verificare contro `glossary.csv`
    quando si tradurranno i file delle navi; potrebbe dover restare `Modified Argosy`.
51. **Come il motore compone la `phrase`** (scelta casuale delle opzioni, ordine degli slot): **non
    verificato** nel runtime. La verifica è sui dati.
52. **Acrostico `N-O-R-T-H`** (L19, `Dangerous Games 2`, righe 1106–1110): le cinque righe italiane
    conservano le iniziali inglesi con parole italiane (Nessun'altra / Oliate / Rasoi / Titaniche / Hai da).
    Un acrostico non è ornamentale: è il meccanismo dell'indovinello. Se cambia una riga, l'indovinello
    smette di funzionare; il test esiste solo nei dati, non nel runtime.
53. **Secondo indovinello: bisticcio *beast/bee* perduto** (L19, righe 1129–1132). L'italiano non ha un
    gioco equivalente fra «bestia» e «ape»; ho tradotto il senso letterale. Recuperarlo richiederebbe
    riscrivere l'indovinello e la soluzione (rotta a est), cioè cambiare il gameplay: **non fatto**.
    Anche la rima dei distici è caduta, a favore del contenuto.
54. **`Free Worlds` invariato** con articolo italiano («i Free Worlds», 18 occorrenze in L19): prima
    occorrenza della fazione in un lotto tradotto. Da ratificare una volta per tutto il corpus, come
    `Wanderers` e `Remnant`.
55. **`Dragonriders` → «Cavalcaladri»** (13 in L19): nomignolo che il gruppo conia per sé, non classe di
    nave. Se si preferisce l'invariato, la modifica è locale (sezioni 7 di L19).
56. **`subpods` → «sottopodi»** (29 in L19): termine mai comparso nei lotti precedenti. Da allineare ai file
    degli equipaggiamenti.
57. **`Core` invariato** (9 in L19) per il dispositivo su cui viene caricata una mente: **non** è `the Core`
    → «il Nucleo» (decisione 21, la regione galattica). L'omonimia è documentata perché altrimenti sembra
    un'incoerenza.
58. **`interference plating` → «piastre di interferenza»** (1 in L19): reso come descrizione, non come nome di
    equipaggiamento. Da verificare contro i file degli outfit, come `Pulse Laser` (decisione 38).
59. **23 unità di L19 con citazione non chiusa nel sorgente** (207, 208, 209, 257, 320, 446, 481, 482, 491,
    512, 530, 576, 577, 702, 961, 962, 963, 968, 969, 970, 1440, 1587, 1591): il numero dispari di
    virgolette è **riprodotto**, non corretto. `check.py` confronta il conteggio per unità.
60. **Un cirillico omografo in L19** (unità 1102, `а` U+0430 in «echeggiа»): refuso di stesura, corretto.
    Nessun controllo precedente lo vedeva; `check.py` di L19 include ora la riga «caratteri non latini».
61. **`they/them` lasciato in inglese** (L20, unità 214: «Kris Brecht, they/them.»). È un'autodichiarazione
    di identità del personaggio, non prosa non tradotta; `check.py` di L20 ha `'they/them'` in `TITLES`.
    Nella prosa italiana l'accordo di genere su Kris è **evitato** (forme senza participio concordato),
    non risolto con neologismi: la scelta è sistematica nelle unità 208–253 e spiegata in `L20/review.md`.
62. **`Family-Cairn` invariato** (L20, `Stone to Hope`): termine culturale della tradizione Hlewagasti/Snaiwaz
    che funziona da nome proprio. «Cairn di famiglia» avrebbe perso il valore di istituzione.
63. **Nomi candidati del sondaggio navale invariati** (L20, unità 364–368: `Star Empress`, `Tycho's Legacy`,
    `Shippy McShipface`, `It's Dark Here`, `What Asteroid`): la gag sta nei nomi, non nel loro significato.
64. **`sweatshop` → «fabbrica di sfruttamento»** (L20, missione Adelita): «laboratorio clandestino» confondeva
    con la clandestinità della mostra. **`Ion Cannon` → «cannone ionico»** in prosa, come da decisione 38.
65. **40 unità di L20 con citazione non chiusa nel sorgente** (64, 82, 83, 107, 120, 129, 173, 179, 185, 226,
    309, 461, 507, 508, 555, 599, 672, 699, 701, 758, 770, 771, 772, 777, 779, 801, 806, 807, 917, 933, 1079,
    1086, 1185, 1202, 1204, 1298, 1404, 1627, 1640, 1663): conteggio dispari **riprodotto**, non corretto.
66. **Sezioni L20 più piccole del target** (1.331–3.091 parole EN, media 2.111 invece di 3.000–5.000): il taglio
    segue i confini delle missioni e il controllo strutturale avviene a ogni parte. Deviazione dichiarata in
    `L20/review.md` §1, non mascherata come conforme.
67. **`label` dentro un blocco `conversation`** (L21a 14, 20, 28, 35, 63, 69, 82; L21b 113): il database le
    classifica `CONVERSATION` perché costruisce l'id dal testo, ma sono **bersagli di `goto`** e restano
    identiche. Vanno individuate dal `delimiter` quote, non dal `kind`.
68. **Pronomi inglesi come token** (L21b 54, 84, 85, 145, 148: `<they>`, `<they've>`, `<they're>`, `<they are>`,
    `<their>`): il motore li sostituisce con parole inglesi, che in italiano non reggono l'accordo. Sono resi con
    possessivo, «che» o soggetto sottinteso, e il token sparisce. `check.py` ha `TOKEN_EXC` **enumerato** e
    verifica che solo quelle unità perdano token, e solo quelli: nessun'altra unità può perdere un token.
69. **Pulsante `"Spaceport"`** citato nelle istruzioni di missione: reso «Spazioporto». Quando le interfacce
    saranno tradotte, l'etichetta del pulsante dovrà corrispondere; se resta `Spaceport`, queste righe vanno
    riallineate (sono 4 in L21b).
70. **Lotto multi-file**: L21 è composto da L21a (coda di `human missions.txt`) e L21b (`intro missions.txt`),
    con directory e artefatti separati. `check_handoff.py` legge ora la cella `File` della tabella del prossimo
    lotto, così un lotto può proseguire in un file diverso senza valori cablati.

71. **L21b copre `intro missions.txt` per intero** (637 unità, righe 23–2319): il file è finito, nessuna
    unità resta dopo la riga 2319. Il lotto L21 si chiude a 30.497 parole, −23,8% dal target: la deviazione
    è dichiarata e non recuperata allungando il lotto con un terzo file.
72. **Duplicati per differenza minima**: in L21b tre coppie di unità condividono quasi tutta la frase
    (246/352 `, and deliver` vs `and deliver`; 249/468 `help` vs `help out`; 55/571 `glance` vs `look`).
    La traduzione mantiene la differenza invece di appiattirla, perché `DUP_OK` deriva dal sorgente.
73. **Una chiave in due file di parte è invisibile**: l'unità 465 era scritta in `part05` e in `part06`;
    il merge caricava `part06` per ultimo e sovrascriveva la versione corretta, facendo fallire il
    controllo duplicati su un testo che sembrava a posto. Dopo ogni parte va verificato il numero di
    chiavi rispetto all'intervallo atteso.

74. **Le virgolette dipendono dal file**: in `human missions.txt` e `intro missions.txt` il campo
    `english` contiene le virgolette che avvolgono la stringa, in `jobs.txt` no (le ha solo la riga
    grezza). Il criterio è il campo `english`, non la riga del file: 100 unità di L22 sono state
    bocciate per aver replicato l'uso dei lotti precedenti.
75. **L22 chiuso a 5.823 parole (−85,4%)**: `jobs.txt` è un file intero di 390 unità e non ha un
    confine a 40.000 parole. Allargare il lotto ai sei file di job board successivi avrebbe dato
    12.000 parole miste a sette file: preferito un lotto per file e L23 su un file da 38.724 parole.
76. **Token aggettivali** (`<student research>` in L22 380–390): il motore inserisce un aggettivo
    inglese (`farming`, `volcanic`) che non può reggere un accordo italiano; reso con «di tipo
    `<student research>`» conservando il segnaposto e `<planet>`.

77. **`label` di condizione dentro `conversation`** (L23: 373, 375, 383, 386, 389, 404): stringhe corte
    e minuscole come `on first mission` o `know now`, bersagli di `goto`. Il database le classifica
    `CONVERSATION`, quindi non si riconoscono dal `kind`: vanno cercate a mano nel blocco e aggiunte a
    `NT`. Con queste, `NT` di L23 sale a 30 unità (22 `UI_LABEL` + 2 `TEXT` + 6 label).
78. **Citazioni dal conteggio dispari in L23**: `68`, `79`, `178`, `183`, `199`, `285`, `286`, `291`,
    `292`, `303`, `308`, `332`, `376`, `379`, `382`, `384`, `434`, `457`, `465`, `499`. Sono citazioni
    mai chiuse nel sorgente: si riproducono, non si normalizzano. Le parti 09–12 ne hanno aggiunte
    altre tredici (`776`, `825`, `932`, `933`, `971`, `1002`, `1007`, `1010`, `1031`, `1057`, `1067`,
    `1069`, `1074`): l'elenco completo sta nell'handoff §4.4.3.
79. **Famiglia delle pietre in L23** (parti 09–12): `Elf-Stone → Pietra-Elfica`, `God-Stone →
    Pietra-Divina` (già in L21a), `Goddess-Stone → Pietra della Dea`, `Ran-Stone → Pietra di Ran`. La
    placca di Helsingor (unità 1045–1047) spiega che sono scafi di navi coloniali: tradurle come una
    famiglia sola evita di alternare italiano e invariati nella stessa pagina.
80. **`Transport Union` → «Unione dei Trasporti»** (unità 1015, 1072–1078), non «Sindacato»: `Syndicate`
    resta «Sindacato» e due organizzazioni con lo stesso nome confonderebbero il giocatore.
81. **`Ice-Crawler` → «cingolato del ghiaccio»** (veicolo narrativo: nel repository non esiste nessuna
    `ship`/`outfit` con quel nome) e **Hjlod** con articoli caduti, come l'Ondurdis di L21a. L'inglese
    storpiato di Hjlod (`velcome`, `vork`, `veapon`) non si trasporta: il controllo delle parole
    residue lo rifiuterebbe e in italiano non significa nulla.

82. **L27 — voce dei Ka'het e resa dei Remnant** (2026-10-18): i Ka'het non sono Coalizione, quindi la voce
    rovesciata di L25/L26 non è stata applicata. Il verbo `sign` dei Remnant è reso con **accennare**, e
    `chant` con **canta**; `slug` → **lumaca**, `airlock` → **camera di equilibrio**, `Builders` →
    **Costruttori**, `Graveyard` → **Cimitero**, `Ember Waste` → **Distesa di Braci**. Le classi Ka'het e
    Ka'sei restano invariate.
83. **L27 — un testo troncato nel sorgente si riproduce** (unità 188: `on anoth.` → `su un altr.`). Non si
    completa il periodo inventando la parola mancante: il difetto è del testo di partenza e va conservato,
    altrimenti la traduzione "corregge" l'originale.
84. **L27 — il `verify.py` di un lotto non finale non asserisce la copertura cumulativa**: usa l'invariante
    di segmento (lotto dentro il file, zero sovrapposizioni, copertura stampata). Il `verify.py` di L28, che
    chiude `kahet missions.txt`, **può invece** asserire 1.738/1.738.

85. **L28 — chiusura di `kahet missions.txt`** (2026-10-18): 917 unità di L27 + 821 di L28 = **1.738/1.738**.
    Ottavo file completo. Il `verify.py` di L28 asserisce la copertura totale perché è l'ultimo segmento;
    quello di L27 resta a invariante di segmento. Regola: **la copertura si asserisce solo nel lotto che
    chiude il file**, negli altri si stampa.
86. **L28 — navi e tecnologia invariati**: `Swan`, `Petrel`, `Tern`, `Peregrine`, `Smew`, `Merganser`,
    `Albatross`, `Ibis`, `Calm Sea Afire`, `Snipes` restano in inglese; `liveship` → **nave viva**,
    `ramscoop` invariato, `gaslining ship` → **nave adatta all'atmosfera**, `Inhibitor Turret` →
    **Torretta Inibitrice**, `zombie satellite` → **satellite zombi**, `Void Sprite` → **spettro del vuoto**.

87. **L29 — chiusura di `hai missions.txt`** (2026-10-18): 823/823 da un solo lotto, **nono file completo**.
    Il `verify.py` asserisce la copertura totale (823/823, un solo lotto senza sovrapposizioni) perché il
    lotto è l'intero file. Regola confermata: **la copertura si asserisce solo nel lotto che chiude il file**.
88. **L29 — glossario Hai**: `Unfettered Hai` → **Hai Slegati** / **gli Slegati**; `keystone` → **pietra
    chiave** (con `Key Stone` → **Pietra Chiave** e `Tree Skeleton Key Stone` → **Pietra Chiave Scheletro
    d'Albero**); `ringworld` → **mondo ad anello**; `drone carrier` → **porta-droni**; `Scar's Legion` →
    **Legione di Scar** (`Scab` → **Crosta**, per conservare la battuta). Navi e modelli restano in inglese
    (`Star Queen`, `Bulk Freighter`, `Heavy Shuttle`, `Aphid`, `Star Barge`, `Shield Beetle`, `Geocoris`,
    `Leviathan`, `Solifuge`, `Starling`, `Gull`, `Keloid`), così come luoghi e persone.
89. **L29 — due riferimenti di dato non sono prosa**: le unità 455 (`outfit/crystal pendant`, dentro un
    comando `scene`) e 599 (`thumbnail/hai pond strider`) arrivano dal parser come `MISSION_TEXT` ma non
    vanno tradotte: stanno in `NT` con la motivazione scritta in `check.py` (17 non traducibili invece di 15).
    Cercali leggendo `raw` e `id`, non solo `english`.
90. **L29 — le battute aperte si riproducono**: in `hai missions.txt` la citazione continua nell'unità
    successiva, quindi molte righe non chiudono la virgoletta. La normalizzazione in blocco ne aveva chiuse
    23: il ciclo le ha riaperte togliendo la virgoletta in eccesso. Non si normalizza il sorgente.
91. **L30 — chiusura di `lunarium intro.txt`** (2026-10-18): 730/730 da un solo lotto, **decimo file
    completo** (13 parti, da 30 a 81 unità, tutte a fine missione). `verify.py` con 25 controlli, exit 0;
    copertura totale asserita perché il lotto è l'intero file. 29.208 EN → 28.079 IT (0,961),
    rapporto 0,70–1,66, sha256[:16] `5adcc2bfda276f8f`.
92. **L30 — voce della Coalizione**: Kimek, Saryd e Arach parlano con l'ordine dei costituenti marcato
    (oggetto o complemento prima, soggetto esplicito, verbo in coda), come in L24–L26; la narrazione
    resta in italiano normale. Esempi: `Grateful I am, Captain.` → «Riconoscente, io sono, Capitano.»;
    `Interested in helping with some charity work, would you be?` → «A dare una mano con un po' di
    beneficenza, tu interessato saresti?». Il dispositivo vale anche per i messaggi scritti dei
    dispositivi di traduzione.
93. **L30 — `Factions` resta in inglese**: è la categoria del diario (`log "Factions" …`), non prosa.
    Tradurla spezzerebbe il raggruppamento con gli altri file che usano la stessa stringa e non sono
    ancora tradotti. Sta in `NT` con la motivazione in `check.py` (9 non traducibili: 7 `UI_LABEL` +
    2 `Factions`), non in una regola generale. **Da rivedere** quando l'intero corpus sarà tradotto.
94. **L30 — lacuna dichiarata dell'inventario**: le righe `log "Factions" "Lunarium Redoubt" "<testo>"`
    (righe 21 e 467) producono **una sola unità** nel database: nome e testo della voce di diario non
    esistono in `state.db` e restano in inglese. `tools/l10n.py` e `state.db` sono protetti, quindi la
    lacuna si documenta in `review.md` §7 e non si ripara da un lotto. Quando si affronterà l'inventario,
    queste due voci vanno aggiunte e tradotte a parte.
95. **L30 — tipografia delle opere inventate**: i titoli di opere teatrali interne alla finzione si
    traducono (`Twin Eclipse` → «Eclissi Gemella», `Down with the Tyrant House!` → «Abbasso la Casata
    Tiranna!»), mentre i nomi di nave restano invariati (`Bastion`, `Argosy`, `Clipper`, `Thistle`,
    `Finishers`, `Punishers`, `Spire`, `Spindle`, `Fuso`). L'equipaggiamento descrittivo si traduce
    (`Heavy Anti-Missile Turrets` → «torrette antimissile pesanti», `jump drive` → «motore di salto»).
96. **L31 — chiusura di `heliarch intro.txt`** (2026-10-18): 663/663 da un solo lotto, **undicesimo file
    completo** (11 parti, da 30 a 83 unità, tutte a fine missione). `verify.py` con 25 controlli, exit 0;
    copertura totale asserita perché il lotto è l'intero file. 21.729 EN → 20.845 IT (0,959), rapporto
    0,73–1,68, tab 509/509, virgolette 878/878, token 181/181, sha256[:16] `09e75a0528604150`.
97. **L31 — i titoli con `Drill` sono «prova», non «esercitazione»**: `Refueling Drill` → «Prova di
    rifornimento» (1,93 era «Esercitazione di rifornimento»), `Pursuit Drill` → «Prova di inseguimento»
    (2,23), `Combat Drill` → «Scontro di prova» (2,50). Il testo narrativo continua a dire «esercitazione»
    dove è la parola del discorso; solo i **titoli di missione** stanno nella banda comoda. La soglia del
    rapporto (gate 0,55–1,90) non è stata toccata in nessun lotto finora: si riscrive il titolo.
98. **L31 — due inglesi quasi identici vanno resi in modo distinto**: 134/153 (`clearer` / `more clearly`)
    e 270/303 (`Scanning Preparations` / `Preparations for Scanning`). Appiattirli produce un duplicato
    italiano che il sorgente non giustifica, e il controllo lo boccia. Le differenze minime si riproducono.
99. **Residuo traducibile: due formule diverse, una sola vera.** `state.py` e `check_handoff.py` calcolano
    `PENDING − staging − 630 label` = **16.967**; ma 294 delle 630 `UI_LABEL` sono **già dentro** le
    unità esportate nei lotti, quindi vengono sottratte due volte. Il valore misurato
    (`PENDING` non `UI_LABEL` meno le unità già in staging) è **17.261 unità / 492.803 parole**. L'handoff
    continua a dichiarare 16.967 perché è il numero che il checker ricalcola (contratto dello strumento);
    il valore vero sta in §4.3. Allineare i due strumenti è un lavoro a parte, non un effetto di un lotto.
100. **L32 — `CONVERSATION` è un contenitore misto**: in `wanderers start.txt` il tipo esiste (47 unità) e
    contiene sia il testo dei blocchi `conversation` (da tradurre, backtick riprodotto) sia le `label` di
    salto (identiche, in `NT`). È la decisione 77 misurata in L21/L23, che qui torna per la prima volta in
    un file intero. Si distinguono leggendo il `raw`, non il `kind`.
101. **L32 — chiusura di `wanderers start.txt`** (2026-10-18): 805/805 da un solo lotto, **dodicesimo
    file completo** (13 parti, da 45 a 80 unità, tutte a fine missione). `verify.py` con 26 controlli,
    exit 0; copertura totale asserita perché il lotto è l'intero file. 24.166 EN → 22.753 IT (0,942),
    rapporto 0,72–1,61, tab 512/512, virgolette 1.305/1.305, token 173/173,
    sha256[:16] `bdabdc64ad3b7ce1`. Apre l'arco dei Wanderers.
102. **L32 — le parentesi quadre `[a, b]` sono struttura, non stile**: 112 unità del dispositivo di
    traduzione. Il gioco mostra una sola alternativa per volta, quindi ogni alternativa deve reggere la
    frase da sola e il numero di alternative deve restare quello del sorgente. `check.py` di L32 ha un
    controllo apposta (gruppi e alternative per gruppo): una parentesi chiusa male passa il controllo
    delle virgolette e fallisce questo. Quando la resa letterale non regge, si riscrive la frase
    **intorno** alla parentesi (unità 797: `[combattere? preoccuparci de]` → `[combattere contro?
    preoccuparci di?]`).
103. **L32 — la lacuna di `log` a tre argomenti ha la forma opposta a L30**: qui `log "Factions"
    "Wanderers" `testo`` produce una sola unità che è il **testo** del diario (quindi tradotto), mentre
    in L30 l'unità era la **categoria** e il testo si perdeva. Categoria e nome restano fuori
    dall'inventario in entrambi i casi. Conseguenza operativa: la forma della lacuna va misurata
    sull'`english` di ogni riga, non dedotta dal `raw` o dal tipo.
104. **L32 — `unfettered humans` ≠ `Unfettered`**: i Pug chiamano così gli Alphas, e in italiano sono
    **«umani senza freni»**, non «Slegati» (che è la fazione Hai). Due parole inglesi identiche nella
    radice, due referenti diversi: la distinzione va tenuta o il dialogo dei Pug accusa gli Hai di cose
    che non hanno fatto.
105. **L33 — le parentesi quadre si controllano, non si "tiene il conto"**: in 731 unità, tre rese
    avevano perso un gruppo (324, 685) o ne avevano invertito l'ordine (286). Passavano i controlli su
    tab e virgolette. Solo il controllo strutturale le ferma: il `check.py` di un lotto con `[a, b]`
    deve portarsi il confronto gruppi/alternative, sempre.
106. **L33 — `NT` non si eredita**: in L32 erano 3 elementi misti (riferimento di dato + due `label`),
    in L33 sono 11 `UI_LABEL` (`skip unmark <stella>`) e **zero** `CONVERSATION`. Copiare la lista
    produce due errori opposti: unità non traducibili segnalate come mancanti e unità traducibili
    lasciate in inglese.
107. **L34 — un controllo che non può fallire non è un controllo**: in `free worlds 0 prologue.txt`
    le unità con parentesi quadre `[a, b]` sono **0**. Copiare il controllo strutturale di L32/L33 avrebbe
    confrontato due liste vuote su ogni unità, producendo una riga «OK» che dichiara verificato ciò che
    non esiste. Forma corretta: il controllo si toglie dal `check.py` e si mette un'asserzione nel
    `verify.py` («0 unità con parentesi quadre»), così se le premesse cambiano il lotto diventa rosso.
108. **L34 — `NT` vuoto è una misura, non un default**: in L34 non c'era nessuna unità non traducibile
    (0 `UI_LABEL`, 0 `CONVERSATION`, nessun riferimento di dato, nessuna `label` di salto) e la lista è
    stata azzerata; il `verify.py` asserisce che i tre insiemi siano vuoti. Il lotto successivo ha **1**
    `UI_LABEL`: la lista si rimisura a ogni file, non si eredita.
109. **L34 — il registro religioso va distinto per personaggio**: «I pray» è formula di cortesia in
    Freya («Confido»), fede dichiarata in JJ («Prego» + «se Dio vuole»), preghiera vera nei monaci
    (litania resa come formula, non parafrasata). Una traduzione unica per tutti e tre appiattisce tre
    personaggi diversi.
110. **L35 — la lacuna `log` può avere due forme nello stesso file**: in `free worlds 1 start.txt` 24
    righe producono il testo del diario e una (unità 547) produce la categoria `People`. La categoria
    resta identica e va in `NT`: le altre categorie del file non sono inventariate e quindi restano in
    inglese, e tradurne una sola crea una categoria doppia nel diario del giocatore.
111. **L35 — i nomi inglesi con articolo non possono restare invariati**: `Confederated Councils of the
    Outer Rim` contiene `the` e `of`, che il controllo delle parole residue intercetta. Va sciolto in
    italiano tenendo invariata la sigla: «Consigli Confederati del Bordo Esterno (CCOR)».
112. **L35 — lo stesso personaggio, in un ruolo cambiato, cambia tono e non voce**: Tomek è il mentore
    asciutto di L34 e il ribelle che urla in L35. La voce (frase piana, nessun ordine marcato) si
    mantiene; il registro si ricava dalla scena, e il monologo conserva la maiuscola enfatica
    («la NOSTRA milizia») perché è un tratto del testo, non una scelta tipografica.
113. **L36 — una `label` di salto può essere visibile al giocatore come scelta di dialogo**: le tre
    `UI_LABEL` di `free worlds 2 middle.txt` (`me too`, `definitely surrender`, `definitely rescue`)
    stanno dentro un dialogo a scelte e restano identiche. Copiare `NT = {513, 547}` da L35 — una label
    e una categoria di diario — avrebbe fatto tradurre queste tre e rotto tre `goto`: `NT` si rimisura
    sul `raw` a ogni file.
114. **L36 — se l'inglese spezza una battuta, l'italiano deve spezzarla con lo stesso numero di
    virgolette**: l'unità 543 aveva quattro virgolette nell'inglese (`"..." he says. "..."`) e la prima
    stesura ne aveva due. Il controllo conta le virgolette **per unità**, quindi l'errore non si vede
    nel totale.
115. **L36 — le quadre non sono solo il dispositivo `[a, b]`**: `source/text/Format.cpp` definisce `[`
    e `]` come `LPAREN`/`RPAREN` per il testo fra parentesi. Un'unità può avere una coppia di quadre che
    racchiude l'intera riga (in `free worlds 3 checkmate.txt`, unità 143) e quella cornice **va
    conservata e tradotta**, non trattata come label. Per L37 il controllo da mettere è sul numero di
    coppie per unità, non sulle alternative.
116. **L37 — le quadre possono essere una cornice, non il dispositivo `[a, b]`**: l'unità 143 di
    `free worlds 3 checkmate.txt` è un avviso al giocatore racchiuso fra `[` e `]`, una sola coppia per
    l'intera riga. Il controllo va sul **numero di coppie per unità** (e il testo dentro si traduce per
    intero); un'asserzione «0 unità con quadre» sarebbe semplicemente falsa, e un controllo sulle
    alternative confronterebbe due liste vuote.
117. **L37 — `NT` vuoto è una misura, e il verify la difende**: con 0 `UI_LABEL` e 0 categorie emerse,
    il `verify.py` asserisce che nel file non ci sia nessuna `UI_LABEL`. Copiare `{407, 501, 503}` da
    L36 avrebbe messo in `NT` tre unità che qui sono testo normale, lasciandole in inglese.
118. **L38 — un file può non iniziare a riga 16**: `free worlds 3 reconciliation.txt` produce unità
    dalla riga **31** (le prime trenta sono intestazione e `mission` senza testo traducibile). L'export
    parte da 31 e il `verify.py` deve asserire `(first, last) == (31, 2729)`: copiare la coppia 16 da
    L37 renderebbe il lotto falso invece che rosso.
119. **L38 — un file può iniziare a riga 31, non 16**: `free worlds 3 reconciliation.txt` produce unità
    dalla riga **31** (le prime trenta sono intestazione e blocchi `mission` senza testo traducibile).
    L'export parte da lì e il `verify.py` asserisce `(first, last) == (31, 2729)`. La coppia di righe è
    una **misura**, non un'abitudine: copiarla dal lotto precedente renderebbe il lotto falso.
120. **L38 — il primo blocco `CONVERSATION` della serie va trattato come dialogo, non come righe
    isolate**: le unità 403–411 sono un colloquio continuo (supervisore, ingegneri, Freya) e i turni si
    rispondono. Il `verify.py` asserisce il conteggio (9) e che nessuna sia vuota; in L39 lo stesso tipo
    copre 34 unità su 114.
121. **L38 — un titolo può uscire dalla banda comoda senza essere un errore**: `Cloaking Device` →
    «Dispositivo di occultamento» sta a 1,80, dentro il gate 0,55–1,90 ma fuori dalla banda 0,70–1,75.
    Abbreviarlo in «Occultamento» scenderebbe sotto 0,70 e perderebbe la natura di equipaggiamento: la
    scelta si documenta nel `review.md`, la soglia non si tocca.
122. **L39 — il file più corto della serie è anche quello con più `CONVERSATION`**: 114 unità, di cui 34
    `CONVERSATION` (30%), e **zero** unità con quadre o virgolette dispari. Le asserzioni «zero» vanno
    scritte come tali nel `verify.py`: un controllo che si limita a omettere il caso non distingue
    «nessuna occorrenza» da «controllo non eseguito».
123. **L39 — le battute metaletterarie sono battute, non note dell'autore**: «quella parte del gioco non
    è ancora stata implementata del tutto» e «è caduta la quarta parete» si traducono alla lettera, senza
    virgolette di scusa e senza spiegarle, altrimenti il gioco sembra chiedere scusa di sé.
124. **L40 — quattro varianti quasi identiche dello stesso messaggio sono quattro unità diverse**: in
    `free worlds side plots.txt` le unità 15, 65/69 e 190 differiscono per «the»/«your» o per il **punto
    finale assente**, e il controllo dei duplicati le vede come distinte. Vanno differenziate anche in
    italiano, altrimenti il lotto è rosso su un controllo corretto.
125. **L40 — un file di trame secondarie non eredita il registro della campagna**: i personaggi nuovi
    (il monaco David, Rex e Fido, l'Agente Falco, il capitano di Greenrock) si definiscono in poche
    battute e vanno resi con la loro voce, non con quella dei cinque del Consiglio.
126. **L41 — un lavoro ripetibile si traduce per la ventesima lettura, non per la prima**: i lavori di
    guerra hanno testi parametrici che il giocatore vede decine di volte; una sintassi piana e senza
    effetti regge, una brillante stanca. Il registro resta amministrativo («richiedono un trasporto
    immediato», «è a corto di scorte e deve essere rifornito subito»).
127. **L41 — i titoli dei lavori stanno in una lista, e lì conta la lunghezza**: `Resupply <planet>` è
    diventato «Rifornisci <planet>» (verbo, non sostantivo) perché in italiano «Rifornimento <planet>»
    sembra un nome di prodotto, e la lista deve dire cosa farai. `Scouting Run` → «Ricognizione», più
    corto dell'inglese.
128. **L41 — tab 0 e virgolette 0 non rendono inutili i controlli**: i controlli restano e asseriscono
    la parità su zero, così un salto di formattazione nel costruttore non passa inosservato. Il file è
    anche l'unico della serie senza righe `log` (0 `LOGBOOK`): nessuna lacuna di inventario possibile.
129. **L33 — il tab lo aggiunge il costruttore, mai la mano**: tre unità riscritte via script avevano
    `\t` nel valore e il costruttore ne ha aggiunto un secondo (408 → 411 tab). Il conteggio dei tab è
    l'unico controllo che se ne accorge.
130. **L42 — le label di salto si elencano una per una, anche quando sembrano testo**: le 35 `UI_LABEL`
    di `remnant 2 cognizance.txt` sono tutte `label "..."` bersagli di `goto`, ma cinque (`good idea`,
    `lets go`, `maybe later`, `turn down`, `not thirsty`) sembrano battute visibili. Restano identiche in
    entrambi i casi — tradurle romperebbe il salto — e la motivazione va scritta come «label di salto»,
    non come «testo non traducibile». Una deroga generale («salta le non traducibili») nasconde le
    omissioni vere; un elenco no.
131. **L42 — il `verify.py` deve rimettere i tab prima di confrontare le parti con `translation.json`**:
    le parti si scrivono senza tab e il costruttore li antepone, quindi il confronto diretto fallisce su
    un lotto corretto. La forma che regge è `'\t' * ntab + valore` ricostruito da `source.json`, e il
    fallimento va attribuito allo strumento, non alla traduzione (misurato: 1 FAIL su un lotto verde).
132. **L42 — undici virgolette dispari si confrontano come insiemi di idx, non come totali**: le
    battute aperte nel sorgente (32, 48, 50, 201, 240, 241, 245, 246, 342, 485, 558) sono state
    riprodotte aperte. Il totale delle virgolette torna anche con la virgoletta nel punto sbagliato; il
    confronto per unità e l'insieme degli idx no.
133. **L42 — Gavriil non ha genere, e la traduzione non può inventarlo**: nel sorgente è `they/them`.
    La linea tenuta è: niente participi o aggettivi concordati sul soggetto quando si può evitare
    («Annuisce», «Gesticola»), presentazione senza genere («del nostro team tecnico»), e forme
    invariabili dove il genere è inevitabile. Chi riprende la serie deve mantenerla: rimettere
    «l'astrobiologo» sarebbe un'informazione assente dal testo.
134. **L42 — il quasi-duplicato si differenzia dove l'inglese differisce**: `(Accept.)` (354, 377) e
    `(Agree.)` (469) sono due testi distinti, quindi l'italiano non può essere «(Accetta.)» in tutti e
    tre. Il `check.py --range` non vede i duplicati fra parti: il controllo **completo** ogni due parti è
    quello che li trova (misurato: 1 gruppo, 3 unità).
135. **L42 — una riga `log` a tre argomenti inventaria solo il testo**: la riga
    `log "People" "Gavriil"` con il testo fra backtick produce una sola unità, che è il testo del
    diario; categoria e nome restano in inglese e la lacuna si documenta nel `review.md` §7, senza
    toccare `tools/l10n.py` (protetto).
136. **L42 — i nomi di tecnologia si traducono, i nomi propri no**: `Aeon Cell` → «Cella Aeon»,
    `liveship` → «nave viva», `tackling` → «aggancio», `Ember Node` → «Nodo di Braci»; restano in inglese
    navi (`Merganser`, `Peregrine`, `Starling`, `Puffin`, `Pelican`), toponimi (`Ssil Vida`, `Esquiline`,
    `Postverta`, `Patir`) e l'organizzazione `Remnant Logistics`. La distinzione è la stessa dei lotti
    precedenti: si traduce ciò che il giocatore deve capire, non ciò che identifica un oggetto.

137. **L43 — il lessico tessile della Trama si traduce in blocco**: `Primary Weft` → «Trama Primaria»,
    `Secondary Weft` → «Trama Secondaria», `weft field` → «campo di trama», `Warp` → «Ordito». La
    spiegazione di Ruach funziona solo se ordito e trama restano due parole tessili coerenti fra loro:
    tradurne una sola e lasciare l'altra in inglese rompe l'analogia che il testo sta costruendo.
138. **L43 — `LOGBOOK` 0 si asserisce come assenza, non si omette**: nel `verify.py` la forma è
    `log == []`, esattamente come per `CONVERSATION`. Un controllo che sparisce quando il numero è zero è
    un controllo che non protegge nulla. Avvertenza per chi riprende: in L44 i `LOGBOOK` sono **12**,
    quindi il controllo va *riscritto in positivo*, non ereditato.
139. **L43 — le label ripetute si elencano comunque**: `shattered help` (226, 253) e `rather not`
    (268, 291) compaiono due volte perché servono rami diversi della stessa conversazione. `NT` è una
    lista di **indici**, non di stringhe: deduplicarla per testo lascerebbe due salti non verificati.
140. **L43 — il rapporto lunghezze è un rilevatore di omissione, non un giudizio di stile**: l'unità 3 era
    stata scritta con la sola battuta, perdendo la cornice narrativa. Il numero è uscito a 0,33 e ha
    segnalato un testo mancante che la rilettura non aveva visto. Se il gate è rosso, prima si cerca cosa
    manca, poi si riscrive.
141. **L43 — `hoverboard` e i suoi composti restano inglesi**: `hoverboard`, `hovercar`, `hovercart` sono
    il termine usato anche in italiano corrente per quel veicolo, e il gioco li tratta come oggetti di
    scena. È una scelta registrata, non una dimenticanza; `hoverboarding` come attività si è resa con
    «hoverboard» perché servono tre parole in inglese e una sola in italiano.
142. **L43 — nei numeri tecnici si converte solo il separatore delle migliaia**: `299.792.458 m/s`,
    `2.99792458x10^8`, `1.1DE784Ax10^7` restano tali (coefficiente, base ed esponente non si toccano);
    `11D.E78` e `1.1DE79` non si toccano affatto, perché `D.E` è la scrittura del motore. Normalizzare
    questi numeri «all'italiana» produrrebbe dati falsi.
143. **L43 — la dimensione delle parti segue i contesti, non le unità**: 299 unità in **8** parti (41 · 30
    · 38 · 39 · 36 · 45 · 29 · 41) contro le 14 di L42, perché qui gli episodi sono 11 e ognuno si chiude
    in sé. Spezzare a 22 unità come in L42 avrebbe tagliato le conversazioni a metà.
144. **L43 — un `.md` lungo si rigenera con `rm` + `write_file`, non con `write_file` diretto**: quando la
    lettura precedente è stata paginata (`read_file` con `offset`/`limit`), il guard rifiuta la
    sovrascrittura anche se il file era stato letto per intero («Refusing to overwrite … last read with
    offset/limit pagination»). Procedura verificata: leggere il file, `rm -f` con il terminale, poi
    `write_file`; le correzioni puntuali restano `patch`. Vale per `CHECKPOINT_AGENTE`, `HANDOFF_*` e
    `CHECKPOINT_SESSIONE`, che si rigenerano a ogni chiusura di lotto.

145. **L44 — `LOGBOOK` e `CONVERSATION` cambiano di segno, e il controllo si riscrive in positivo**: in
    L43 il `log` era assente e il `verify.py` asseriva `log == []`; in L44 le righe sono 12, in L45
    saranno 23 e le `CONVERSATION` 16. Un'asserzione di assenza ereditata sarebbe un test che passa senza
    controllare niente: il controllo va riscritto come «N attese, N tradotte, nessuna identica
    all'inglese», con l'elenco degli indici.
146. **L44 — `Emerald Sword` → «Spada di Smeraldo» è una traduzione, non un nome proprio**: il sorgente
    dice «an ancient Sheragi warship whose name translates to the Emerald Sword», e la nave entra
    nell'inventario del giocatore con quel nome. Chi riprende la serie **non** deve «ripristinare»
    l'inglese: la scelta è registrata qui e nel §5 del `review.md` di L44.
147. **L44 — il guardiano parla per sostantivi**: l'Archon di Zubenelhakrabi usa frasi scandite e tre
    termini in fila («terrore. Rimpianto. Perdita.»). La resa mantiene il punto fermo come scansione e
    non introduce contrazioni: è l'unico personaggio del lotto senza registro colloquiale, e la
    differenza deve restare udibile.
148. **L44 — il `check.py` può sbagliare, la traduzione no**: il controllo «parole inglesi residue» ha
    segnalato `be` e `there` dentro il nome della band *There Might Be Riots*. La correzione giusta è
    estendere `TITLES` (nomi propri invarianti), non riscrivere la frase; l'episodio va dichiarato nel
    `review.md` §8. In L45 il rischio si ripete con i nomi Successors: `TITLES` si estende **prima**.
149. **L44 — il femminile delle tre Hai è informazione, non stile**: il sorgente usa `she` per Eyama,
    Rakei e Desyo e `they/them` per Mammon e per l'Archon. La traduzione segue: femminile per le tre
    archeologhe, forme senza concordanza per Mammon e per la voce del guardiano. Non è una preferenza
    stilistica, è il dato del testo.
150. **L44 — la dimensione delle parti segue i blocchi di missione**: 625 unità in **13** parti da 50
    (l'ultima da 25) contro le 8 di L43 e le 14 di L42. Il criterio non è il numero di unità ma dove
    finisce un episodio: le parti di L44 coincidono con i confini delle missioni (Deep Archaeology,
    difesa di Zug, cubo, Mammon, Museo, squadra Hai, Spada di Smeraldo).
151. **L45 — `NT` non è sinonimo di `UI_LABEL`**: nel lotto ci sono 26 label di salto **e** 8
    riferimenti di dato (4 categorie di diario, 4 nomi di `government`). Elencarli tutti e 34, per
    indice, è l'unico modo per non lasciare che una label cambi sotto il naso; una deroga generica
    («le label restano uguali») sarebbe un controllo che non controlla.
152. **L45 — il segno dei controlli segue il lotto, non la serie**: L43 aveva 0 `LOGBOOK` (asserzione di
    assenza), L44 ne aveva 12 (controllo positivo), L45 ne ha 23 con 16 `CONVERSATION` (due controlli
    dedicati). Un'asserzione ereditata passerebbe senza verificare nulla.
153. **L45 — il conteggio delle quadre è un invariante del testo redatto**: i frammenti dei file
    recuperati usano `[...]` e il numero di `[` e `]` per unità deve restare identico. Due unità (657,
    669) avevano una quadra in più in prima stesura: corrette sul numero misurato, non a occhio.
154. **L45 — un'opzione identica per necessità si dichiara, non si forza**: il nodo di conversazione 137
    è `(No.)` → `(No.)`. Scriverlo diverso per far passare un controllo cambierebbe il senso; la
    deroga va nel codice (`CONV_SAME`), non nella traduzione.
155. **L45 — due nomi con la stessa grafia sbagliata non si inventano**: `Sirja` (unità 146–147) è un
    refuso del sorgente; il corpus ha 51 `Sijra` e 0 `Sirja`, quindi si allinea alla forma dominante
    senza introdurre una terza variante.
156. **L45 — i frammenti dei file hanno titoli tradotti perché sono titoli**: `"Lost"`, `"Heart"`,
    `"Trial"`, `"Emptiness"` → «Persa», «Cuore», «Processo», «Vuoto». Sono intestazioni di documento,
    ripetute identiche nelle due occorrenze (651/666, 652/667, 655/668, 657/669) e distinguibili dai
    nomi invarianti delle persone e delle Casate.
157. **L45 — un falso positivo del controllo duplicati può essere una traduzione migliore**: 193 `"Yes."`
    e 470 `"I have."` erano entrambi «Sì.»; l'italiano ha una forma naturale per il secondo caso
    (**«L'ho fatto.»**) e il duplicato sparisce senza perdere nulla.
158. **L46 — il segmento interno non chiude il file**: `successor 1 prologue.txt` ha 345 unità e L46 ne
    copre 221 (righe 24-664). Il `verify.py` asserisce **0 prima / 124 dopo**, non «0 dopo»: un
    `verify.py` copiato da L45 (che chiudeva il file) avrebbe asserito la fine del file e fallito.
    La copertura totale è un invariante **solo** per i lotti che chiudono un file.
159. **L46 — tre forme di `log` nello stesso segmento**: `log "testo"` (6 unità), `` log `testo` `` (1),
    `log "Categoria" "Nome" `testo`` (1). Il controllo le identifica **sul `raw`** e le elenca; assumere
    una forma sola renderebbe cieco il controllo sulle altre due. La nona riga `LOGBOOK` è la
    **categoria** (`People`), che resta in inglese.
160. **L46 — le assenze si dichiarano**: `CONVERSATION` 0, quadre 0, virgolette dispari 0. In ognuno dei
    tre casi il `check.py` porta un'asserzione esplicita con la parola «assenza dichiarata»: un controllo
    che non c'è non è un controllo che passa.
161. **L46 — `Graveyard` resta invariato**: 372 occorrenze nel corpus contro 49 «Cimitero» (tutte in
    L27/L28). La forma dominante vince, e cambiarla qui creerebbe una terza variante.
162. **L47 — il duplicato era un errore vero**: le unità 94 e 103 erano identiche in italiano, ma il
    sorgente differisce nel **vocativo** (`House Sioeora.` contro `House Kaatrij.`). Il `check.py` le ha
    segnalate sul lotto completo; 103 è stata corretta. I paragrafi cerimoniali ripetuti (sei coppie in
    L47) non sono copie: la differenza sta nel nome della Casata, nel soggetto o nel destinatario.
163. **L47 — due rami dello stesso evento restano paralleli, non unificati**: il consiglio si svolge in
    due versioni (dono proposto da Sioeora, unità 91-99; dono proposto da Kaatrij, 100-108). Ogni ramo
    nomina la Casata che parla; armonizzarli con un'unica formulazione cancellerebbe informazione di gioco.
164. **L47 — `Old and New Houses` → «Casate Vecchie e Casate Nuove»** con la maiuscola: è un nome
    istituzionale ricorrente, non una descrizione. Le Casate estinte (`Jaasii`, `Vejret`, `Ijridanii`,
    `Sejra`) restano invariate come nomi propri.
165. **L47 — un `check.py` che esplode non è un `check.py` che fallisce**: in L46 due `rows.append` con
    una tupla a 2 elementi hanno prodotto `ValueError: not enough values to unpack` a metà tabella. Il
    traceback va letto come difetto dello strumento; la traduzione non c'entra. Ogni riga di `rows` deve
    essere una tupla a tre elementi (nome, esito, booleano).
166. **Un lotto chiuso può diventare rosso quando il file prosegue**: il `verify.py` di L46 asseriva
    `copertura 221/221` e «un solo lotto sul file»; dopo L47 lo stesso controllo leggeva `345/221` e
    falliva, pur con la traduzione intatta. La correzione è nel **controllo**, non nel dato: la copertura
    va asserita **per segmento** (le unità con `line between first and last` prese da `state.db`) e si
    verifica che **nessun altro lotto** copra quelle unità. Un invariante «di file» vale solo per i lotti
    che chiudono il file.
167. **L48 — gli Avgi dichiarano la modalità prima della frase**: ogni battuta comincia con
    un'etichetta di specie («Divertimento.», «Approvazione.», «Curiosità.») e molte finiscono con
    «, domanda?». Il dispositivo è **riprodotto**, non normalizzato in avverbi: è la firma della specie,
    e appiattirlo renderebbe gli Avgi indistinguibili dai Successori. Il costo è che le etichette si
    ripetono; il controllo duplicati lavora sulle unità intere e non le segnala — corretto così.
168. **L48 — la forma dominante nel corpus vince anche quando è l'inglese**: `Twilight` (10 contro 2
    «Crepuscolo»), `Outer Limits` (4 contro 1), `hyperdrive` (75 contro 40 «iperguida») restano
    invariati; `polities` no, perché «politia» in italiano si legge come refuso di «polizia».
    Tradurre un termine «perché si capisce meglio» crea una terza variante, non una migliore.
169. **L48 — i nomi dei giochi restano**: `Trefoil` e `the Foil` invariati, come `GRASER` e `Shroud`.
    Il testo definisce il Foil in scena, quindi la spiegazione la dà il gioco, non il traduttore.
170. **L49 — il controllo duplicati ha trovato un errore vero**: `"No."` (25, 236) e `"Nope."` (95)
    erano resi tutti e tre «No.». La correzione è «Macché.» per 95, che è anche la battuta giusta.
    Tre «No.» identici in italiano non erano una scelta stilistica, erano una perdita di differenza.
171. **L49 — il conto alla rovescia resta in lettere**: «Dodici, undici, dieci, nove…». Il sorgente
    scrive in parole nel punto di massima tensione; le cifre l'avrebbero raffreddato.
172. **L48 e L49 — la lacuna dell'estrattore dipende dalla forma, non dal file**: in entrambi i lotti
    tutte le righe `LOGBOOK` hanno il testo fra backtick e il testo è stato estratto (14/14 e 5/5).
    La lacuna dei sei casi precedenti (testo fra **virgolette**) qui non si presenta, e i due `check.py`
    lo **asseriscono** invece di darlo per scontato.
173. **L50 — il primo contatto ha tre registri, e vanno tenuti distinti**: narratore al presente
    (frasi lunghe, dettagli accumulati), messaggio Avgi telegrafico (unità 39: niente articoli, verbi
    all'infinito, «Tu umano, domanda?»), voce mediata dal traduttore (unità 62 e seguenti: etichette di
    modalità + sintassi corretta). La differenza fra i due parlati Avgi **è** la scena: prima un codice,
    poi una voce. Il parlato rotto si rende con la **sintassi**, non con errori di ortografia: uno
    sgrammaticato italiano avrebbe fatto sembrare l'alieno ignorante.
174. **L50 — il `TEXT` duplicato è un invariante, non una svista**: l'unità 3 (contesto `phrase:`) ripete
    parola per parola la missione 2. La traduzione **deve** essere identica, e `verify.py` lo asserisce
    in inglese e in italiano. Un revisore che trovasse due rese diverse troverebbe un errore.
175. **L50 — `Assembly of Polities` e `Consonance Assembly` sono due cose**: la prima è «Assemblea delle
    Entità» (come in L48), la seconda «Assemblea della Consonanza», che è già la forma del corpus. Due
    nomi distinti per due istituzioni distinte, non un'incoerenza da sanare.
176. **L50 — incoerenza di genere nel sorgente**: Prasinos è «She» nel diario (unità 52) ma «he trails
    off» (103) e «Asime continues for him» (104). In italiano si evita di **aggiungere** un secondo
    errore («e si interrompe», «al posto suo») senza correggere l'inglese: il testo sorgente non si
    tocca, e un'eventuale unificazione va decisa sul corpus intero.
177. **L51 — primo lotto con `NT` vuoto**: 0 `UI_LABEL` e 0 riferimenti di dato. Un `check.py` ereditato
    con un elenco di indici avrebbe controllato unità inesistenti **e sarebbe passato lo stesso**,
    perché un elenco vuoto è silenzioso. Serve un'asserzione di assenza esplicita
    (`unita UI_LABEL nel segmento (0 attese: NT vuoto)`), falsificabile se comparisse una label.
178. **L51 — gli insiemi non hanno ordine**: il confronto `tuple(x for x in DIALOG …)` dentro `--range`
    ha prodotto `(132, 143, 119)` contro `(119, 132, 143)` e un FAIL falso. Il rimedio è
    `tuple(sorted(...))`: un difetto dello strumento, non della traduzione (cfr. decisione 165).
179. **L51 — i nomi propri incoerenti nel sorgente si riproducono**: `Darius Caldwell` (unità 4) e
    `Darius Calwell` (unità 129/148, e L50). Il nome non si traduce, quindi l'italiano mostra entrambe
    le grafie. Chi cerca il personaggio deve cercare entrambe; unificarle sarebbe una scelta sul corpus,
    non su un lotto.
180. **L51 — `Wardragon` → «Dragoguardia»**: la nave Quarg non era ancora nel corpus. Ho scelto un
    composto trasparente invece di lasciare l'inglese, perché il testo la nomina come oggetto di
    scansione e il lettore deve capire che è una nave. È una decisione **nuova**, non un'eredità.
181. **L52 — l'invariante «di file» torna legittimo quando il lotto chiude il file, e solo allora**:
    L52 porta `avgi 0 first contact.txt` a 406/406 e lo asserisce con tre condizioni insieme
    (`0 dopo la 1120`, `max(line) = 1120`, copertura 406/406 su tre lotti). Se il file crescesse di una
    sola unità, i primi due diventerebbero rossi: è la differenza fra un invariante e un'asserzione che
    passa per caso (cfr. decisione 166).
182. **L52 — `gateway` → «varco», non «portale»**: in italiano «portale» evoca la fantasia, e il testo
    parla di un manufatto alieno costruito dagli Antecessors. `Antecessors` resta invariato (forma del
    corpus), `magnetar` resta invariato (termine astronomico internazionale).
183. **L52 — il refuso `Darious` non si replica, l'incoerenza `Caldwell`/`Calwell` sì**: la differenza è
    che il secondo è una variante del cognome presente in più unità e in più lotti, il primo una svista
    di battitura isolata. Si riproducono le varianti, non gli errori di digitazione.
184. **L53 — una specie che non parla cambia il lavoro**: i Gegno comunicano con grugniti, gesti e un solo
    vocabolo («Oukeug», invariato). Il lotto è quasi tutto **narrazione al presente**: la qualità sta nei
    verbi d'azione e nel ritmo, non nel lessico dei dialoghi. La resa dei versi (brontolio, sbuffo,
    ruggito, «stridisce a scatti brevi, quasi dei cinguettii») è parte del testo, non decorazione.
185. **L53 — `<Alien>`, `<alien>` e `<aliens>` sono tre famiglie di token**: il controllo confronta i
    multiset **con le maiuscole**, e `<Alien>` compare solo nel nome della missione (unità 1). Normalizzare
    le maiuscole avrebbe fatto passare per corretto un token sbagliato.
186. **L53 — `translation.json` non contiene `raw`**: i controlli sulla riga grezza devono leggere
    `source.json`. `verify.py` è esploso con `KeyError: 'raw'` usando `translation['units']`: difetto
    dello strumento, non della traduzione (cfr. decisioni 165 e 178).
187. **L54 — la voce dei Quarg ha più registri, e vanno distinti**: in L54 il Quarg parla con sintassi
    invertita e aggettivi celebrativi («This must be for you an exhilarating day», «the imperious
    Gegno»); in L55 parla **freddo e amministrativo** («It was incredibly unwise», «the end of our
    patience»). La traduzione riproduce l'inversione dove c'è e non la aggiunge dove non c'è: un registro
    unico avrebbe cancellato la differenza fra il Quarg cerimonioso e quello che giudica.
188. **L54 — il parlato Scin distingue grafia e pronuncia**: nella prima visita il testo scrive
    `Vi`/`Scin`; dentro la nave, alla seconda visita, scrive `Vie`/`Sinn` con il verbo `enunciates`.
    La differenza è nel sorgente e va riprodotta: `Vie` e `Sinn` restano distinti da `Vi` e `Scin`.
189. **L55 — un'etichetta può essere una frase**: `corroboration provocation homeworld` è una `label` di
    salto di tre parole e resta **invariata in blocco**, non tradotta parola per parola come farebbe un
    traduttore di testo corrente. Le `UI_LABEL` si elencano una per una proprio per questo.
190. **L54/L55 — un tipo assente in un lotto può essere presente in quello dopo, e il controllo deve
    cambiare segno**: `CONVERSATION` è 1 in L55 (controllo **positivo**) e 0 in L56 (assenza dichiarata);
    `LOGBOOK` è 3 in L54 e 0 in L55. Il `check.py` si deriva dal lotto precedente ma le **asserzioni** si
    ricostruiscono sul `source.json` di quello nuovo.
191. **L55 — un duplicato inglese può nascondersi in un lotto corto**: `"I do not care."` compare due
    volte (unità 10 e 19) e il primo `verify.py` assumeva «0 gruppi». Il controllo corretto è duplice:
    ogni gruppo duplicato ha **una sola** resa, e le rese **non** si ripetono fra unità con inglese
    **diverso**.
192. **L54 — `str.replace` con una sottostringa corta colpisce altre variabili**: sostituire `LOG = set()`
    ha modificato anche `DIALOG = set()`, perché «DIA» + «LOG = set()» contiene la stringa. Dopo ogni
    patch generata si verifica con `grep` il risultato, non si presume.
193. **L56 — `NT` 28 è il massimo della serie e va elencato per intero**: molte sono verbi singoli
    (`ask`, `escort`, `work`, `alone`, `tech`, `interest`), altre composte (`negative rep` due volte,
    `quarg escort`, `no escort`, `visit a`/`visit b`, `epilogue a`/`end a`), una conserva un refuso
    (`dont know`, senza apostrofo). Sono chiavi di salto: restano **identiche** e nessuna deroga
    generica è ammessa.
194. **L56/L57 — la stessa scena in due lotti deve avere la stessa resa, e va asserita come stringa**:
    `DIALOG` 170/171 (L56) e 22/23 (L57) sono lo stesso testo inglese in due esiti della missione. La
    traduzione è identica per necessità dichiarata; il `verify.py` di L57 confronta la **stringa
    letterale** con quella di L56, così una deriva futura diventa rossa.
195. **L56 — il lessico del rifiuto non si appiattisce**: `dismissed` → «congedato», `exiled` →
    «esiliato», `shunned` → «ripudiato». Il Quarg li distingue esplicitamente e la scala è parte del
    testo.
196. **L57 — la finestra di export non è la prima unità del lotto**: l'export 905–1287 produce un lotto
    la cui prima unità sta sulla **943** (le righe 905–942 non contengono unità). Il controllo va
    asserito sul valore **misurato**, non sulla finestra richiesta: il primo `verify.py` era rosso su
    `(905, 1287)` ed è stato corretto in `(943, 1287)`.
197. **L57 — `<payment>` entra nella linea Gegno**: unità 126, «ti paga una somma di `<payment>`». Il
    token resta invariato e la frase regge sia con un numero sia con una descrizione: nessuna
    preposizione aggiunta che presupponga la forma del valore.
198. **L57 — due duplicati italiani non voluti sono stati trovati dai controlli, non dalla rilettura**:
    52/58 (`Stay where I am.` vs `Remain where I stand.`) e 109/162 (`prevent` vs `deny`). Il controllo
    `duplicati italiano non spiegati dal sorgente` resta anche quando sembra rumore: è l'unico che vede
    la perdita di distinzione fra due scelte diverse.
199. **L58 — un file nuovo si apre con le assenze dichiarate**: `culture conversations.txt` è fatto di
    micro-scene e il primo lotto non ha né `UI_LABEL` né token né duplicati anomali. Il `check.py`
    derivato da L57 è stato **riscritto nelle asserzioni**, non riusato: 17 `UI_LABEL` e 13 token di L57
    sarebbero diventati controlli verdi su un insieme vuoto.
200. **L58 — il registro è il rischio, non i simboli**: nove scene di gente comune (lotteria, posto di
    blocco, negozio, funerale, cantiere, raccolto bruciato, ristorante, donna delle pulizie). La voce
    resta quotidiana e non commenta: nessun avverbio di giudizio aggiunto dove l'inglese è asciutto.
201. **L58 — i nomi di regione non si traducono**: `Deep` resta `Deep`, anche dentro la scritta sulla
    tazza («Pace, Prosperità, Progresso» è il testo stampato, `Deep` è l'insegna).
202. **L59 — zero duplicati è un'asserzione, non un'assenza di controllo**: primo lotto della serie con
    0 gruppi. In `verify.py` c'è `len(dup_en) == 0` esplicito, altrimenti «nessun duplicato» e «controllo
    dimenticato» sarebbero indistinguibili.
203. **L59 — il lessico tecnico non si addolcisce**: `retardants` → «ritardanti» (non «estinguenti»),
    `perimeter` → «perimetro», `hunkering down` → «ci stiamo barricando». La scena dell'incendio è
    descritta con i termini di chi la affronta.
204. **L59 — le patch si copiano dal file, non si ricostruiscono a memoria**: la sostituzione del blocco
    `for ch, nome, atteso_n in (('	', …` è fallita perché nel file ci sono **due parentesi aperte**. Il
    pattern va estratto dal file (`grep -n`) e incollato, poi verificato con un secondo `grep`.
205. **L60 — il filtro `parole inglesi residue` rimuove i titoli prima di cercare**: `Guard` è nella lista
    `TITLES`, quindi «Guardare» − «Guard» = «are», che è fra le parole inglesi. Il segnale era **vero**
    (un controllo ha funzionato), ma la correzione è **riscrivere la traduzione** («Dare un'occhiata»),
    non allargare l'eccezione. Un falso positivo del filtro non autorizza a indebolire il filtro.
206. **L60 — due registri in un lotto**: il varo (1–29, brillante, affettuoso, con battute) e
    `Masquerade Hanging` (30–31, cupo, impersonale). Non si uniformano, e il contrasto è nel sorgente.
207. **L60 — `mortgage` → «mutuo»**: nel gioco la prima nave si compra a rate; il testo alterna «mutuo» e
    «debito della nave» e la traduzione fa lo stesso.
208. **L61 — `NT` torna vuoto e il token resta**: il segno dei controlli segue il lotto (decisione 190);
    L61 ha 0 `UI_LABEL` ma **1 token** `<origin>` dentro il discorso diretto della giornalista, e il
    simbolo resta perché la frase italiana regge («Sono qui su `<origin>`…»).
209. **L61 — le istituzioni non si traducono oltre il necessario**: `Parliament` → «Parlamento»,
    `Navy` → «Marina», `Free Worlds` → **invariato**. Il collegamento con i lotti delle campagne
    Free Worlds (L32–L41) dipende da questa coerenza.
210. **L61 — `I'd rather not` ≠ `I would prefer to not answer`**: due formule diverse nel sorgente (9 vs
    18/24) e due rese diverse («No, preferirei di no» / «Preferirei non rispondere»). Non sono la stessa
    battuta e non si unificano, anche se il senso è lo stesso.
211. **L63 — un rapporto fuori banda si corregge riscrivendo la battuta, non allargando il gate**:
    l'unità 27 («Earth Day?») rendeva 2,08 perché l'italiano aggiunge l'articolo. Resa «Giornata della
    Terra?» rende 1,85, dentro il gate. Il gate non è un giudizio di qualità ma un rilevatore di
    espansione: se lo si allarga, smette di segnalare.
212. **L62 — il simbolo `°` è un carattere non latino per il controllo**: «35° Congresso» è stato
    rifiutato (0xB0) e riscritto «Trentacinquesimo Congresso». Il controllo ha ragione: nei dati di gioco
    i caratteri non ASCII sono a rischio di rendering, e la parola costa poco.
213. **L62 — le etichette numerate sono chiavi complete**: `overheard scientists 1`, `… 2`, `… 3` non sono
    tre varianti grafiche dello stesso nome; il numero fa parte della chiave e resta identico.
214. **L63 — tre virgolette dispari consecutive (18, 29, 31)**: sono discorsi diretti aperti e non chiusi
    nel sorgente. Si confrontano come **insieme di indici** fra inglese e italiano; chiuderle «per pulizia»
    romperebbe la parità e il rendering del dialogo.
215. **L63 — un'intraducibilità dichiarata**: la capitana dice «the Moon» e il testo commenta che è «the
    archaic term for Luna». In italiano «la Luna» è il termine corrente, quindi il commento resta
    paradossale. La resa conserva la struttura e dichiara il limite nel `review.md`; non finge di averlo
    risolto.
216. **L64 — due scelte simili non sono la stessa scelta**: «(Return to my ship.)» e «(Go back to my
    ship.)» erano state rese entrambe «(Torna alla mia nave.)». Il controllo dei duplicati l'ha rilevato:
    quando l'inglese distingue due opzioni, l'italiano deve distinguerle, anche se il senso pratico
    coincide.
217. **L64 — l'anafora del comizio si mantiene**: «Possiamo… Possiamo… Possiamo…» e le enumerazioni
    ternarie («Gagariani e forestieri. Capitani e viaggiatori. Militari e contadini.») sono struttura
    retorica, non ripetizione da sfoltire. Aggiungere aggettivi per «fluidità» snaturerebbe il personaggio.
218. **L65 — le etichette di stato del mondo sono selettori**: `war ongoing`, `war over`, `zenith bombed`,
    `sestor beaten at farpoint` non sono testo descrittivo ma chiavi che scelgono quale paragrafo
    mostrare. Restano identiche, e il `verify.py` le elenca una per una.
219. **L65 — la parità dei token si verifica per simbolo, non sul totale**: con `<origin>` e `<ship>` un
    controllo di solo conteggio (2 = 2) passerebbe anche se i due simboli fossero stati scambiati. Il
    `verify.py` confronta `Counter` per famiglia.
220. **L65 — «Dish Fish» → «Pesce Piatto»**: il bisticcio dell'originale (*fish that's a dish*) si regge in
    italiano su «piatto», che è sia il recipiente sia l'aggettivo. La ripetizione del cameriere
    («Piatto. Pesce.») resta perché è il carattere del personaggio, non un difetto da correggere.
221. **L67 — `LOGBOOK` cambia segno quando compare**: il `check.py` derivato da L66 asseriva «0 attese:
    assenza dichiarata» e diventava rosso con un diario nel lotto, pur con la traduzione giusta. La riga è
    stata resa **positiva** («1 attesa») e affiancata dall'asserzione sulle tre forme `log` (tre argomenti,
    backtick, diretta). Un tipo assente non è un tipo vietato.
222. **L67 — `LOG` definito due volte**: la patch ha inserito `LOG = set([1])` lasciando in piedi un
    `LOG = set()` precedente, e Python usava il secondo. La correzione giusta è un filtro **per riga** sul
    file, non `str.replace` su una sottostringa corta (che è già la trappola 192).
223. **L66 — il rapporto può uscire dal gate anche dal basso**: «(Make a run for it.)» → «(Scappa.)»
    rendeva 0,48, sotto il minimo 0,55. La battuta è stata riscritta «(Scappo via.)» e il minimo del lotto
    è tornato 0,64. Il gate non si allarga in nessuna direzione.
224. **L66 — i nomi di razza inventati si traducono, i toponimi no**: «Mammoth Mastiff» → «Mastino Mammut»,
    «Mainsail Seadog» → «Cane di Mare di Mainsail». La razza è descrittiva e si traduce; il luogo resta in
    inglese, come per ogni altro toponimo del gioco.
225. **L67 — la chiusura del file si asserisce in modo rigido**: `0 dopo`, `max(line) = 1122`, copertura
    374/374. Se il sorgente crescesse, i tre controlli diventerebbero rossi — è il comportamento voluto
    (decisione 181), non un numero da correggere.
226. **L68 — `log` ha quattro forme, non tre**: `log "Categoria" "Nome" "Testo"` (tre argomenti *tutti* fra
    virgolette) fa estrarre all'estrattore protetto la **categoria** e **perde il testo**. Il `check.py`
    separa `LOG_CAT` da `LOG_TEXT`: la categoria resta identica (in `NT`), il testo si traduce. È la settima
    occorrenza della lacuna (L45 195/305/357/418, L46 62, L47 54, **L68 23**); il testo perso va dichiarato
    nel `review.md`, non ricostruito.
227. **L68 — «House X» → «Casa X», plurale «Casate»**: misurato in staging, `Casa Kaatrij` 51, `Casa
    Sioeora` 35, `Casa Myurej` 4, contro 2 `Casata Myurej`. Le due occorrenze residue restano nel lotto
    chiuso: non si riscrive un lotto per allinearlo. `the People's Houses` → **`Casate del Popolo`**.
228. **L68 — il registro arcaico non si rende con pronomi arcaici italiani**: la voce di Casa Myurej parla
    in inglese elisabettiano (`thou / thee / thy / dost / shalt`), e L45–L47 lo rendono già con «tu» moderno
    in sintassi formale («Cessa il tuo avvicinamento…»). L'arcaismo sta nella costruzione, non nel pronome;
    introdurre «voi» o «codesto» cambierebbe il registro rispetto a tre lotti chiusi.
229. **L68 — un numero dell'handoff può essere falso, e la ricognizione serve a questo**: L68 dichiarava
    «13 token», ma la somma della sua stessa tabella e il `source.json` danno **10**. Il `check.py` è stato
    scritto su 10 e il documento corretto (anche `L67/STATO.md`, che ripeteva il numero). Regola già nota
    (decisione 119) ma qui ha morso un documento, non un lotto.
230. **L68 — `next_section.py` può sovrapporre la finestra**: propone di ripartire dall'ultima riga del lotto
    precedente (113 per L69), che è già coperta. La finestra corretta si sposta a 114 e si verifica con
    `state.db`; il numero da asserire resta quello **misurato** (prima unità 118).
231. **L69 — un tipo assente si dichiara, e si asserisce anche la premessa**: `NT` e `LOGBOOK` tornano a
    zero dopo L68. Oltre a `== set()` / `== []`, il `check.py` asserisce che nel `raw` del lotto **non
    esista nessuna riga `log`**: senza quella premessa, un cambio di inventario passerebbe in silenzio
    dietro un controllo che confronta due insiemi vuoti.
232. **L69 — due missioni possono avere lo stesso nome**: `Track down Riiria` compare due volte (unità 28 e
    30) perché sono due missioni distinte con lo stesso titolo. La resa identica è **corretta** perché
    l'inglese è identico; il controllo dei duplicati continua a segnalare solo le rese ripetute fra inglesi
    **diversi**, e il `verify.py` asserisce il gruppo esatto `{28, 30}`.
233. **L69 — refuso del sorgente**: unità 12 dice «Not longer after» (per «Not long after»). Si traduce il
    senso («Poco dopo…»), non si replica l'errore, e il difetto si annota nel `review.md`: il repository del
    gioco resta intatto.
234. **L70 — `MISSION_TEXT` non significa prosa**: le unità 7 e 10 sono
    `government \`People's Houses (Hostile)\``, cioè un **nome di governo** con cui la missione imposta lo
    stato ostile. Tradurlo romperebbe la logica; resta identico e il `verify.py` asserisce che nel `raw` ci
    siano davvero `government` e quel nome. La prosa dice «Casate del Popolo», il riferimento no.
235. **L70 — due `LOGBOOK` alternativi devono restare distinti**: accettare (35) e rifiutare (37) producono
    due diari diversi; una resa unica sarebbe stata segnalata solo dal confronto per indice, non dai
    duplicati (gli inglesi sono diversi).
239. **L72 — un lotto può coprire più contesti per chiudere un file**: il piano prevedeva 20 unità
    (402–464), ma chiudere il file in un lotto da 50 evita un ultimo lotto da 30 unità senza struttura. La
    deviazione si dichiara nel `STATO.md` e nel `REPORT.md` del lotto, non si nasconde.
240. **L72 — `DIALOG` può essere testo, non etichetta**: le due unità del lotto sono descrizioni di evento in
    un blocco `dialog`. Si traduce, e il `verify.py` asserisce che **non** siano identiche all'inglese: così
    un'etichetta mascherata da `DIALOG` verrebbe scoperta.
241. **L72 — `check_handoff.py` toglie un solo prefisso**: `bare()` fa `split(':', 1)[1]`, quindi per
    `mission:Successors: Ghosts Aqrabe 1` il valore atteso nella cella `Contesti` è
    **`Successors: Ghosts Aqrabe 1`**, non `Ghosts Aqrabe 1`. Due tentativi persi per questo.
237. **L71 — `vault` → «cripta»**: il termine non aveva precedenti nello staging. Il testo descrive una
    camera sotterranea, riservata ai nobili, con scatole di legno: «cripta» regge e va riusato se il gioco
    torna su questi luoghi. Se altrove `vault` indicasse un caveau tecnico, la resa va distinta.
238. **L71 — un personaggio può non avere genere**: l'inglese usa `they` per i Successori; l'italiano deve
    concordare. Per Ijaset si evitano i participi («La posizione e la chiave… sono state impresse in me») e
    si usa il riflessivo («Ijaset si irrigidisce»): la scelta va mantenuta, non «corretta» in un lotto
    futuro.
236. **L70 — un controllo scritto male è rosso con la traduzione giusta**: la riga «due LOGBOOK alternativi
    presenti e distinti» passava l'esito booleano come *dettaglio* della tabella e `None` come condizione,
    quindi stampava FAIL. Corretta nel `check.py` prima di chiudere il lotto: ogni riga di `rows` deve essere
    una tupla `(nome, valore mostrato, booleano)`, e il booleano deve essere il terzo elemento.

---

242. **L73 — `CONVERSATION` è testo, e va contato**: in questo file le sei unità sono il corpo del blocco
     (backtick nel `raw`, non nell'`english`). Si traducono come prosa, e il `verify.py` asserisce **due**
     cose: il **conteggio** (6) e che nessuna resti identica all'inglese. Un inventario che cambiasse
     passerebbe inosservato senza il conteggio.
243. **L73 — il registro dei Successori non è uno solo**: Sola è cerimonioso e ironico, Tiliia è pratica, i
     «santi» parlano in frammenti. La resa distingue i tre registri senza toccare le forme fisse (`Casa X`,
     «tu» formale, nomi propri invariati).
244. **L73 — una categoria di diario in mezzo al lotto** (unità 43, `People`): separare `LOG_CAT` da
     `LOG_TEXT`, come in L68; la categoria resta identica e il testo della stessa unità non esiste.

245. **L74 — due unità con lo stesso inglese hanno la stessa resa, e va dichiarato**: `(Retreat.)` alle
     unità 12 e 16 e' un duplicato legittimo (due missioni diverse, stesso pulsante). Il `check.py` lo
     elenca come gruppo con gli indici e il `verify.py` pretende che la resa sia **identica**; le scelte
     opposte restano distinte (`(Press on.)` → «(Insisti.)», `(Keep going.)` → «(Continua.)»).
246. **L74 — un numero sbagliato nel `verify.py` e' rosso come un errore di traduzione**: avevo asserito
     «94 unità dopo la riga 255», il workspace ne dava **91** (180 − 51 − 38). Il numero si ricalcola dal
     file (`count where line > last`) e si confronta col totale, mai a mente.

247. **L75 — un controllo troppo largo e' rosso con la traduzione giusta**: la verifica «la virgoletta
     chiude nelle unita' 6 e 8» confrontava l'elenco di **tutte** le unita' che finiscono con `"`, e in un
     dialogo fitto sono quasi tutte. Il controllo va **ristretto alle unita' dispari**: la domanda ha senso
     solo li'. Regola: un invariante si formula sulle unita' a cui si riferisce, non sul file intero.
248. **L75 — un inglese tronco si lascia tronco**: `our allies in the New` non dice «Houses»; reso «i nostri
     alleati nel Nuovo», senza completare l'ellissi. Completare un testo incompleto e' un'invenzione, non una
     correzione.

249. **L76 — una coppia quasi identica si risolve riproducendo la differenza, non annullandola**: le
     unita' 23 e 25 dicono la stessa frase, ma la 25 **non chiude** la virgoletta. La resa differisce solo
     li', e il `verify.py` lo asserisce con `rstrip('"')`; chiudere la 25 «per pulizia» romperebbe il testo.
250. **L76 — chiudere un file cambia l'invariante e il `verify.py` deve diventare piu' severo**: non basta
     `0 dopo`, servono `max(line)`, totale file e copertura dell'**intero** file letta da **tutti** i
     `translation.json` dei lotti (qui 180 id distinti su 180 righe).

251. **L77 — due inglesi diversi non sono la stessa scelta, anche se differiscono di un pronome**:
     `(Don't ask them anything.)` e `(Don't ask anything.)` vanno resi «(Non chiedere loro nulla.)» e
     «(Non chiedere nulla.)». Il controllo `duplicati italiano non spiegati dal sorgente` lo ha colto.
252. **L77 — i refusi dei nomi propri non si replicano**: `Katiiora` (unita' 61) diventa Kaatiora, come nel
     resto del file, e la correzione si dichiara nel `review.md`.

253. **L78 — cinque gruppi di duplicati legittimi in un solo lotto**: due varianti dello stesso dialogo
     (13/20, 15/22, 16/23) e due opzioni ripetute (39/41, 45/49). Si rendono identici e si **dichiarano**;
     il controllo rifiuta solo le ripetizioni che il sorgente non spiega.
254. **L78 — zero token e' un'asserzione**: in un segmento senza `<…>` la parita' per simbolo diventa
     `0 = 0` e va scritta; omettere il controllo e' un'omissione, non una semplificazione.

255. **L79 — l'inglese volgare e contratto si rende con italiano corrente, non con arcaismi**:
     `vis'tor`, `t'which`, `'round` sono elisioni colloquiali di un parlante risentito. La resa spezza la
     sintassi, non inventa un registro antico.
256. **L79 — `Old Houses` / `New Houses` / `People's Houses` sono tre istituzioni e tre rese**: «Vecchie
     Casate», «Nuove Casate», «Casate del Popolo». Il lotto le mette in opposizione e non vanno confuse.

257. **L80 — quattro `UI_LABEL` in un lotto solo**: vanno elencate per indice e verificate identiche; sono
     quattro bersagli di salto distinti (`populated language`, `uninhabited language`, `never again`,
     `deserved it`) e tradurne una romperebbe il ramo corrispondente.
258. **L81 — i contesti possono essere `ship:` invece di `mission:`**: nella tabella dell'handoff la cella
     vuole il nome **senza** prefisso e in **ordine di riga** (il checker applica `bare()` ai valori del DB).
     Misurato: `Resja, of the Nine Eyes` (17–112) prima, `Hasur, Vowsworn` (123–196) dopo; avevo scritto il
     contrario, e il checker lo ha colto.

259. **L81 — un nome di equipaggiamento e' un dato, non prosa**: `Hyperdrive`, `"Jiita" Heirloom Shielding`,
     `Multimodal Armor: Regen` restano identici nella scheda della nave, perche' sono definiti altrove e
     tradurli qui creerebbe un riferimento rotto. In prosa (`corazza plurimodale`, L73/L76) la stessa cosa si
     traduce: descrivere e nominare sono due funzioni diverse.
260. **L81 — la rima si controlla sulle desinenze**: confrontare le parole intere (`dimora`, `divora`)
     produce un rosso con la poesia giusta; il confronto va fatto sugli ultimi tre caratteri.

261. **L82 — `Visions of Rime` compare due volte con ruoli diversi**: come `TEXT` (nome di equipaggiamento,
     dato, identico) e come contesto `outfit:` (blocco con prosa). Sono unità distinte, e il controllo deve
     trattarle diversamente nello stesso lotto.
262. **L82 — condizione e dettaglio non si invertono**: `rows.append((nome, tok == 0, tok))` mette il numero
     nel terzo campo, che è il booleano, e stampa `FAIL True`. Il formato è `(nome, valore, booleano)`.

263. **L83 — due grafie dello stesso nome nel sorgente non si unificano**: `Valkkyiara-Khorasaqran` (unita'
     4) e `Valkkyiara-Khorasaqra` (contesto di riga 483) convivono, e il lotto lo dichiara.
264. **L83 — `cortex` resta `cortex`**: «corteccia» suonerebbe biologico su un componente di scudi; il
     termine tecnico del gioco si tiene.

## 8. Prossimo passo concreto

**Trappola del checker (misurata in L222)**: `check_handoff.py` riconosce un lotto **terminale** solo se la cella «Confine
dopo» **inizia** con le parole «**fine file**». Una formulazione equivalente («nessuno — la riga 1338 è l'ultima») viene
bocciata come `FAIL`, perché il checker cerca la regex `riga N apre ...` e, non trovandola, ripiega sul caso terminale solo
per prefisso. La cella corretta è «**fine file** — la riga N è l'ultima del file: non esiste un'unità successiva, e
`line > N` vale 0».

**L191–L332 chiusi il 2026-10-20** — centoquarantadue lotti, **3009 unità**, tutti con `check.py` a `FAIL totale: 0` e `verify.py`
a exit 0:

| lotto | file | righe | unità | EN → IT | check / verify | sha256[:16] |
|---|---|---|---|---|---|---|
| L191 | `bunrodea missions.txt` | 16–52 | 12 | 466 → 434 | 25 / 21 | `a1c782a568e872ed` |
| L192 | `bunrodea missions.txt` | 64–91 | 12 | 465 → 418 | 24 / 21 | `6a45d9d51cb156e7` |
| L193 | `bunrodea missions.txt` | 92–150 | 30 | 500 → 463 | 23 / 21 | `0ba103f679e3b8cc` |
| L194 | `bunrodea missions.txt` | 152–203 | 18 | 488 → 479 | 21 / 21 | `5b5071523577ff54` |
| L195 | `bunrodea missions.txt` | 207–219 | 5 | 397 → 361 | 20 / 17 | `a75a3d4708ee72a5` |
| L196 | `hai jobs.txt` | 15–489 | 39 | 499 → 466 | 26 / 19 | `e69389281fc1e23f` |
| L197 | `hai jobs.txt` | 492–967 | 36 | 488 → 462 | 29 / 19 | `0ff30f8bb315b0ad` |
| L198 | `hai jobs.txt` | 988–1565 | 51 | 472 → 481 | 29 / 21 | `7465d06d0b238ebf` |
| L199 | `hai jobs.txt` | 1579–1750 | 26 | 489 → 488 | 28 / 21 | `6af91de2eec66a88` |
| L200 | `hai jobs.txt` | 1753–2067 | 23 | 354 → 422 | 25 / 17 | `3ff06bf4f8b326c1` |
| L201 | `hai outfits.txt` | 27–164 | 8 | 450 → 458 | 24 / 15 | `76f769f988aefc73` |
| L202 | `hai outfits.txt` | 205–484 | 16 | 436 → 434 | 24 / 17 | `2281312fe0da11a4` |
| L203 | `hai outfits.txt` | 508–600 | 9 | 442 → 472 | 24 / 17 | `81a25808d92d805f` |
| L204 | `hai outfits.txt` | 603–788 | 19 | 441 → 454 | 22 / 18 | `12342441647f81f7` |
| L205 | `hai outfits.txt` | 805–984 | 13 | 520 → 524 | 23 / 16 | `968d32112e56b1d4` |
| L206 | `coalition news.txt` | 28–94 | 20 | 440 → 415 | 25 / 17 | `7cff828f2fb7e44b` |
| L207 | `coalition news.txt` | 95–176 | 17 | 432 → 407 | 23 / 17 | `af8d352da08f8841` |
| L208 | `coalition news.txt` | 177–246 | 19 | 436 → 421 | 24 / 17 | `a7a74f3da74a7f29` |
| L209 | `coalition news.txt` | 247–308 | 21 | 432 → 450 | 24 / 19 | `7e550942341d014e` |
| L210 | `coalition news.txt` | 309–400 | 19 | 458 → 437 | 23 / 17 | `ee5ce8eed7ac5542` |
| L211 | `coalition news.txt` | 401–496 | 16 | 378 → 352 | 25 / 19 | `2a3bcc367bdd3978` |
| L212 | `deep jobs.txt` | 16–322 | 45 | 442 → 454 | 26 / 19 | `d3561b72157dd31c` |
| L213 | `deep jobs.txt` | 333–453 | 22 | 436 → 413 | 25 / 18 | `a1c19c89ae374d9f` |
| L214 | `deep jobs.txt` | 457–682 | 35 | 431 → 430 | 26 / 19 | `e2d9f07af3bd3c95` |
| L215 | `deep jobs.txt` | 684–864 | 25 | 431 → 427 | 25 / 19 | `0b4212a734b678ff` |
| L216 | `deep jobs.txt` | 866–929 | 30 | 439 → 443 | 25 / 19 | `193651028d79b6bd` |
| L217 | `deep jobs.txt` | 935–1234 | 29 | 375 → 398 | 27 / 18 | `379596a8a8be9b81` |
| L218 | `successor ships.txt` | 17–381 | 45 | 499 → 549 | 28 / 17 | `9e3e6ea15d7e3638` |
| L219 | `successor ships.txt` | 386–629 | 25 | 467 → 487 | 27 / 16 | `26062019d4d6d536` |
| L220 | `successor ships.txt` | 634–873 | 26 | 440 → 487 | 28 / 18 | `3373e098d9af319f` |
| L221 | `successor ships.txt` | 904–1137 | 24 | 451 → 481 | 28 / 18 | `b7a2199bbf3b9e42` |
| L222 | `successor ships.txt` | 1141–1338 | 26 | 431 → 472 | 29 / 20 | `30ae0dcd3ae347d4` |
| L223 | `remnant outfits.txt` | 48–297 | 12 | 463 → 458 | 28 / 18 | `865540cb64989e26` |
| L224 | `remnant outfits.txt` | 298–565 | 13 | 472 → 483 | 28 / 18 | `bee38f3d2fc80881` |
| L225 | `remnant outfits.txt` | 581–674 | 11 | 455 → 461 | 25 / 18 | `66b157150c05ada7` |
| L226 | `remnant outfits.txt` | 675–864 | 11 | 445 → 447 | 26 / 19 | `7418d831f5d6ba86` |
| L227 | `remnant outfits.txt` | 884–979 | 10 | 382 → 376 | 24 / 20 | `ba3673a78c7a0d5e` |
| L228 | `korath outfits.txt` | 16–195 | 20 | 434 → 474 | 27 / 20 | `49228f599876094f` |
| L229 | `korath outfits.txt` | 208–318 | 15 | 431 → 442 | 27 / 18 | `b85fa00ea11fb613` |
| L230 | `korath outfits.txt` | 319–581 | 26 | 430 → 448 | 27 / 19 | `d246b4e6c38a2e78` |
| L231 | `korath outfits.txt` | 596–808 | 21 | 455 → 498 | 27 / 19 | `39c7cbdeb1825d8b` |
| L232 | `korath outfits.txt` | 809–908 | 10 | 454 → 508 | 31 / 19 | `f0ac63cba4ffbcb3` |
| L233 | `avgi news.txt` | 32–91 | 22 | 447 → 441 | 33 / 20 | `14b34f5d9e29558c` |
| L234 | `avgi news.txt` | 115–180 | 20 | 439 → 433 | 33 / 21 | `a1598c95777cbd57` |
| L235 | `avgi news.txt` | 197–280 | 15 | 72 → 68 | 32 / 21 | `d6825410bf2929d6` |
| L236 | `avgi news.txt` | 301–344 | 23 | 348 → 320 | 36 / 21 | `df51440678f593e2` |
| L237 | `avgi news.txt` | 369–399 | 14 | 356 → 354 | 36 / 21 | `4ffa812d37566858` |
| L238 | `avgi news.txt` | 418–507 | 21 | 502 → 508 | 37 / 21 | `21ea58dec8dd91bb` |
| L239 | `avgi jobs.txt` | 20–656 | 62 | 432 → 483 | 30 / 22 | `09003f2358701239` |
| L240 | `avgi jobs.txt` | 684–1156 | 40 | 470 → 476 | 31 / 25 | `50d99adb0435c12d` |
| L241 | `successor jobs.txt` | 16–280 | 86 | 428 → 445 | 33 / 28 | `19c694523a5473df` |
| L242 | `successor jobs.txt` | 306–802 | 38 | 480 → 435 | 30 / 24 | `c24851e11b618bfb` |
| L243 | `hai ships.txt` | 15–332 | 29 | 451 → 456 | 30 / 23 | `b21c7a4b97f7f745` |
| L244 | `hai ships.txt` | 362–885 | 45 | 466 → 498 | 33 / 25 | `2121d513cf0c67e2` |
| L245 | `hai ships.txt` | 901–1516 | 46 | 442 → 441 | 32 / 26 | `b2a073e1977f8e1f` |
| L246 | `hai ships.txt` | 1517–1860 | 37 | 327 → 324 | 33 / 27 | `2b2115dc3e8187c7` |
| L247 | `syndicate jobs.txt` | 19–153 | 16 | 488 → 510 | 32 / 27 | `197077aa944ef85a` |
| L248 | `syndicate jobs.txt` | 157–275 | 20 | 430 → 422 | 33 / 28 | `fe1a653311604b88` |
| L249 | `syndicate jobs.txt` | 291–431 | 19 | 438 → 419 | 32 / 28 | `ebc4407313c132bf` |
| L250 | `syndicate jobs.txt` | 435–678 | 27 | 432 → 454 | 32 / 27 | `e6cc884c3a1e258a` |
| L251 | `syndicate jobs.txt` | 701–814 | 12 | 139 → 150 | 30 / 25 | `2462a6148f0bcfcd` |
| L252 | `wanderer jobs.txt` | 15–261 | 26 | 430 → 426 | 32 / 27 | `ef6589a611039978` |
| L253 | `wanderer jobs.txt` | 264–442 | 24 | 427 → 406 | 34 / 29 | `be58cd9fe1075809` |
| L254 | `wanderer jobs.txt` | 458–888 | 41 | 426 → 434 | 32 / 28 | `12c0d8ec6bb65b18` |
| L255 | `wanderer jobs.txt` | 891 | 1 | 20 → 19 | 19 / 19 | `efc5d0fa26a5605d` |
| L256 | `post-war reactions.txt` | 40–74 | 22 | 433 → 422 | 23 / 21 | `112f4a79b1436634` |
| L257 | `post-war reactions.txt` | 76–151 | 23 | 406 → 408 | 22 / 23 | `bce2d751217d9e1c` |
| L258 | `post-war reactions.txt` | 152–215 | 20 | 422 → 403 | 23 / 24 | `3b8455b11a9d8aca` |
| L259 | `post-war reactions.txt` | 222–250 | 15 | 426 → 441 | 23 / 23 | `b4019aeff69585da` |
| L260 | `post-war reactions.txt` | 253–264 | 7 | 238 → 214 | 23 / 21 | `23c97f17fb69e7db` |
| L261 | `remnant jobs.txt` | 19–209 | 25 | 404 → 419 | 23 / 20 | `14b2dd524975c4fe` |
| L262 | `remnant jobs.txt` | 226–490 | 29 | 423 → 439 | 25 / 21 | `8b96c0e346eed37d` |
| L263 | `remnant jobs.txt` | 491–682 | 24 | 432 → 410 | 23 / 21 | `4c5f704d21f3c5fc` |
| L264 | `remnant jobs.txt` | 703–741 | 9 | 203 → 196 | 24 / 20 | `941b0ec0fdf96ef4` |
| L265 | `aberrant ships.txt` | 16–685 | 43 | 429 → 418 | 23 / 21 | `5e1de6bbd0d2b20c` |
| L266 | `aberrant ships.txt` | 686–1007 | 22 | 217 → 210 | 26 / 21 | `4c56d5f85bae96b5` |
| L267 | `engines.txt` | 27–194 | 12 | 438 → 440 | 23 / 22 | `8705fb2d52c02da2` |
| L268 | `engines.txt` | 195–323 | 15 | 450 → 459 | 21 / 21 | `60e7d90fa1230d16` |
| L269 | `engines.txt` | 342–487 | 17 | 449 → 511 | 25 / 22 | `dda3b3d775c7cced` |
| L270 | `engines.txt` | 488–717 | 17 | 545 → 527 | 26 / 23 | `dfffe22b6a49a5c1` |
| L271 | `dialog phrases.txt` | 16–98 | 29 | 430 → 400 | 27 / 20 | `f97f37769e07cdec` |
| L272 | `dialog phrases.txt` | 102–172 | 25 | 446 → 438 | 26 / 21 | `87672d3cd0cc297b` |
| L273 | `korath ships.txt` | 95–360 | 8 | 458 → 523 | 24 / 22 | `6e61f954c3436a8c` |
| L274 | `korath ships.txt` | 364–602 | 9 | 430 → 477 | 25 / 21 | `7f062853da3fb523` |
| L275 | `korath ships.txt` | 606–1311 | 14 | 495 → 545 | 25 / 21 | `92155f43b9321f83` |
| L276 | `korath ships.txt` | 1375–1961 | 12 | 453 → 474 | 25 / 21 | `34f555cb0f44679d` |
| L277 | `korath ships.txt` | 2010–2363 | 7 | 213 → 230 | 22 / 19 | `fa3db55b5821855f` |
| L278 | `kestrel.txt` | 15–54 | 16 | 458 → 422 | 25 / 22 | `689dfc9e941857f3` |
| L279 | `kestrel.txt` | 56–164 | 33 | 501 → 439 | 26 / 22 | `291865dbb02348f9` |
| L280 | `kestrel.txt` | 252–402 | 2 | 105 → 103 | 22 / 19 | `79738400502412fd` |
| L281 | `quarg news.txt` | 23–490 | 50 | 778 → 727 | 22 / 19 | `ae78081e75f50c86` |
| L282 | `wanderer missions.txt` | 16–41 | 13 | 449 → 420 | 24 / 22 | `0e77aed1e368033c` |
| L283 | `wanderer missions.txt` | 42–88 | 14 | 495 → 435 | 27 / 24 | `21980307855f6086` |
| L284 | `wanderer missions.txt` | 93–136 | 18 | 549 → 513 | 27 / 24 | `ed34b1008a5507c9` |
| L285 | `wanderer missions.txt` | 169–182 | 9 | 234 → 230 | 23 / 22 | `f4c76137328e36a2` |
| L286 | `gegno ships.txt` | 53–302 | 7 | 454 → 466 | 25 / 23 | `8b6255a50fb2b4a2` |
| L287 | `gegno ships.txt` | 303–658 | 9 | 466 → 446 | 24 / 22 | `4298463b944df0ab` |
| L288 | `gegno ships.txt` | 725–1192 | 9 | 469 → 525 | 24 / 22 | `5b059851c79ed419` |
| L289 | `gegno ships.txt` | 1193–1616 | 12 | 647 → 718 | 24 / 21 | `82591c748393fdf3` |
| L290 | `avgi culture conversations.txt` | 24–106 | 8 | 468 → 450 | 24 / 24 | `43628edbfe1ff1a2` |
| L291 | `avgi culture conversations.txt` | 122–227 | 12 | 451 → 464 | 26 / 23 | `af1c7ffcd6ec5b6e` |
| L292 | `avgi culture conversations.txt` | 229–259 | 17 | 464 → 436 | 25 / 25 | `1b567ec16d25227d` |
| L293 | `avgi culture conversations.txt` | 260–270 | 9 | 274 → 270 | 21 / 20 | `c1bf446c7b612229` |
| L294 | `marauders.txt` | 62–484 | 12 | 493 → 549 | 19 / 21 | `a6077032b4a171fb` |
| L295 | `marauders.txt` | 548–858 | 9 | 494 → 534 | 19 / 22 | `5a651fec0023b77d` |
| L296 | `marauders.txt` | 884–1146 | 8 | 505 → 532 | 21 / 23 | `69471807998be973` |
| L297 | `coalition outfits.txt` | 26–187 | 15 | 461 → 487 | 22 / 23 | `77085abfe85d1e13` |
| L298 | `coalition outfits.txt` | 202–337 | 15 | 471 → 491 | 22 / 23 | `619c7e3eb590cdc6` |
| L299 | `coalition outfits.txt` | 356–509 | 14 | 467 → 463 | 24 / 25 | `3d68cd4b1f275625` |
| L300 | `coalition outfits.txt` | 516–533 | 5 | 209 → 195 | 21 / 21 | `3c9e7d59af2f404c` |
| L301 | `remnant ships.txt` | 17–806 | 12 | 477 → 483 | 22 / 24 | `a0e73ad200bf1785` |
| L302 | `remnant ships.txt` | 807–1291 | 12 | 486 → 509 | 24 / 24 | `c01aa63657ca9588` |
| L303 | `remnant ships.txt` | 1378–1826 | 14 | 670 → 701 | 25 / 26 | `1c2733c4e66a7841` |
| L304 | `quarg outfits.txt` | 37–137 | 11 | 466 → 473 | 21 / 22 | `20e913ff49c84acc` |
| L305 | `quarg outfits.txt` | 138–243 | 10 | 510 → 529 | 23 / 24 | `f067a63cbdd8ea64` |
| L306 | `quarg outfits.txt` | 257–579 | 10 | 530 → 514 | 23 / 22 | `62365e7d4828f1ec` |
| L307 | `avgi weapons.txt` | 25–203 | 12 | 497 → 521 | 23 / 25 | `7de7ed1f00e0f2c7` |
| L308 | `avgi weapons.txt` | 264–703 | 21 | 489 → 537 | 26 / 25 | `274df52c61b68041` |
| L309 | `avgi weapons.txt` | 716–969 | 13 | 446 → 465 | 26 / 25 | `2562eff1fd37187c` |
| L310 | `korath culture conversations.txt` | 26–75 | 27 | 1295 → 1187 | 23 / 23 | `47768e1cd5729025` |
| L311 | `bunrodea outfits.txt` | 25–130 | 12 | 480 → 449 | 22 / 18 | `f5639f821a4e7bef` |
| L312 | `bunrodea outfits.txt` | 135–236 | 12 | 445 → 433 | 25 / 23 | `af2956256bea6c7a` |
| L313 | `bunrodea outfits.txt` | 250–402 | 9 | 327 → 339 | 25 / 22 | `e70ea6641bcda78c` |
| L314 | `drak culture conversations.txt` | 26–79 | 16 | 550 → 556 | 22 / 20 | `162eb068dd20a5d2` |
| L315 | `drak culture conversations.txt` | 93–138 | 16 | 603 → 596 | 23 / 22 | `bc21cf2aa1469868` |
| L316 | `coalition ships.txt` | 59–969 | 10 | 473 → 496 | 23 / 20 | `223f6b9e162366d6` |
| L317 | `coalition ships.txt` | 1141–2195 | 17 | 632 → 645 | 24 / 23 | `6a01542305e995d0` |
| L318 | `korath weapons.txt` | 53–603 | 17 | 477 → 493 | 22 / 20 | `3b472973d562863b` |
| L319 | `korath weapons.txt` | 615–1222 | 22 | 612 → 643 | 24 / 22 | `d1ca5ae4de7938e8` |
| L320 | `wanderer outfits.txt` | 40–450 | 18 | 478 → 471 | 22 / 19 | `0a1138a5d4aa814f` |
| L321 | `wanderer outfits.txt` | 463–659 | 13 | 514 → 547 | 21 / 19 | `bd400d1bce1ce3a8` |
| L322 | `frontier jobs.txt` | 16–318 | 45 | 1014 → 999 | 24 / 21 | `e2cd7a9a14ff7c62` |
| L323 | `rulei.txt` | 38–157 | 41 | 919 → 871 | 22 / 19 | `abd649cfcc0e1085` |
| L324 | `incipias outfits.txt` | 40–388 | 23 | 853 → 831 | 23 / 18 | `8bb5e39597a524ab` |
| L325 | `kahet outfits.txt` | 54–573 | 25 | 848 → 870 | 27 / 20 | `cd118d0935e22235` |
| L326 | `deprecated outfits.txt` | 25–792 | 47 | 1186 → 1233 | 28 / 17 | `1b8fc5c1e88c6e69` |
| L327 | `_ui/help.txt` | 15–69 | 28 | 1138 → 1043 | 20 / 14 | `fbe829e6548efe43` |
| L328 | `_ui/help.txt` | 72–116 | 25 | 988 → 850 | 20 / 15 | `412625a95434a977` |
| L329 | `_ui/help.txt` | 119–212 | 60 | 1322 → 1265 | 15 / 13 | `95524fd2552bc0b9` |
| L330 | `wanderers.txt` | 778–1042 | 15 | 876 → 852 | 13 / 10 | `6322eb8c1d398d1a` |
| L331 | `power.txt` | 23–272 | 22 | 842 → 829 | 14 / 9 | `48c8ef78b4d66af7` |
| L332 | `south jobs.txt` | 15–347 | 40 | 720 → 687 | 16 / 12 | `3da37b24c5169ccc` |

`bunrodea missions.txt`, **`hai jobs.txt`** (175/175) e **`hai outfits.txt`** (65/65, L201–L205) sono **chiusi**. È
**`coalition news.txt` chiuso (112/112, L206–L211)**; **`deep jobs.txt` CHIUSO 187/187**; **`successor ships.txt` CHIUSO 146/146**; **`remnant outfits.txt` CHIUSO 57/57**; **`korath outfits.txt` CHIUSO 92/92 (L228–L232)**. **File interamente tradotti: 64 su 167** (65 contando `deep jobs.txt`, con 1 `UI_LABEL`).

**La convenzione nuova è il registro Saryd.** I Saryd parlano con l'ordine delle parole invertito e non è un refuso:
è una caratterizzazione. Regola:

| caso | resa |
|---|---|
| narrazione (unità senza virgolette) | italiano naturale |
| discorso diretto della Coalizione | inversione riprodotta: predicato/complemento in testa, verbo in coda |
| motti brevi (*Protect and serve*) | resi diritti, senza forzare l'inversione |
| sorgente che chiude in ordine normale | chiusura in ordine normale: **l'inversione non si aggiunge** |

**Marcatore verificabile**: nelle unità citate la frase finisce con un **verbo flesso**. Si asserisce l'insieme esatto
delle unità, non l'impressione di lettura. Vale per tutte le 112 unità di `coalition news.txt` e per qualunque altro
file della Coalizione.

**La seconda convenzione nuova è la composizione dei frammenti** (`phrase:` in `deep jobs.txt`). Le unità non sono frasi:
il gioco le concatena. «Come da istruzioni, tu» + «apri una cassetta di sicurezza» + «in un magazzino anonimo e
disabitato» + «e prelevi il pacco misterioso.» La resa di ogni pezzo è vincolata dagli altri.

| regola | perché |
|---|---|
| maiuscola/minuscola iniziale invariata | una maiuscola di troppo spezza la frase a metà |
| spazi iniziali e finali conservati | fanno parte della stringa concatenata |
| «tu» esplicito nel primo frammento | l'italiano non può lasciare il verbo senza soggetto in un frammento isolato |
| nessuna variante nuova nelle `DESCRIPTION` | «su <destination>» e «Il pagamento è <payment>» vengono da L198 |

**Marcatore verificabile**: confronto dell'iniziale con l'inglese, unità per unità.

**La quarta convenzione è tradurre i legami come sistemi** (L215). Una battuta che vive di una ripetizione (*at any rate*
detto due volte, citato la terza) esiste solo se la **stessa espressione** compare nei punti collegati: la resa si sceglie
una volta e si verifica con un conteggio **simmetrico** nelle due lingue, più la posizione di ogni occorrenza. Lo stesso
vale per i richiami fra unità distanti (una frase citata in una missione e ripresa in un'altra).

**La terza convenzione è la struttura dei `MISSION_TEXT`** (`deep jobs.txt`, da L214). I **tab** non sono spaziatura: sono
separatori di paragrafo e ognuno apre il proprio (`	"Sure. Who are you?"`). Si verificano **per unità** — uno in ciascuna
unità del dialogo, sempre iniziale, mai interno — e valgono sia per l'inglese sia per l'italiano. Lo stesso vale per i
`LOGBOOK`, che sono prosa narrativa in terza persona.

**La lezione del batch**: la convenzione si misura sul workspace e vince sul documento. L196 ha trovato **due numeri
sbagliati** nel contratto d'ingresso — `Token` dichiarato **0** contro **72 segnaposto** misurati, e la regola
«`VALUE` **e** `TEXT` restano inglesi» contro i dati (i `TEXT` in prosa sono tradotti da L108 a L152, restano inglesi
solo i nomi sotto contesti `ship:`). `check_handoff.py` non copre i segnaposto: la parola «token» non compare nel
checker, quindi i 21 controlli verdi non bastavano.

**La seconda lezione (L197)**: due stringhe erano **già tradotte** in staging (`Bring <fare> to <destination>…`,
`This human wishes for <cargo>…`). Il `check.py` ora le confronta con i `translation.json` degli altri lotti: stessa
stringa inglese → **stessa resa italiana**. E un `FAIL 1` iniziale è stato corretto **nell'asserzione** (confrontava
tutto ciò che segue `<planet>` invece della sola frase condivisa), non nel testo.

**La terza lezione (L198)**: un lotto di **ripetizioni** (11 copie di una stringa, 8 di un'altra) non si verifica
unità per unità ma come **famiglia** — indici attesi e una sola resa. E le due stringhe avevano **rese precedenti
concorrenti** (`a`/`su <destination>`, `pagamento`/`compenso`): non esiste «la» traduzione giusta da recuperare, esiste
**una scelta da dichiarare**, presa fra quelle già in staging. Lo stesso lotto ha fatto emergere che in L197 avevo
creato una variante di una frase già resa in L22: riallineata, rieseguita, sha aggiornato.

**La quarta lezione (L199)**: le **relazioni** fra unità si verificano meglio delle unità. Quattro coppie `[1]`/`[2]`
che devono differire solo per `grande` e quattro coppie di `DIALOG` che devono essere identiche: un controllo che
toglie l'aggettivo e confronta, o che confronta dentro la coppia, scopre errori che nessuna asserzione per-unità vede.
E il confine di L199 non chiude una missione (`Superstitious Hai [1]` a cavallo di 1750/1753): il `verify.py` misura
l'identità del contesto invece di assumere che ogni confine separi due missioni.

**La settima lezione (L202)**: due lingue possono divergere nel numero di apostrofi **per ragioni opposte** — l'inglese
contrae (`There's`, `it's`), l'italiano elide (`dell'energia`, `quest'arma`, `d'urto`) e contrae una volta (`C'è`).
2 contro 10 non è un errore: è la lingua. Il controllo elenca le unità e la causa, non solo il conteggio. E il refuso del
sorgente (*jamming affects*) si dichiara, non si corregge.

**L234 chiuso il 2026-10-20 — secondo lotto di `avgi news.txt`**: righe **115–180**, **20 unità**, 439 parole EN → 433
IT, **3 contesti** (`merchant` 10, `politician` 6, `military` 4), **20 `NEWS`**, **0 tab**, **40 virgolette** (2 per
unità), 6 apici EN / 12 IT, 0 segnaposto. `check.py` 33 controlli, `verify.py` 21 con invariante di **segmento**
(42/115). `sha256[:16]` = `a1598c95777cbd57`. **19 etichette su 20**: la 177 è una **domanda Avgi** che finisce con
«, domanda?». Chiusa la questione di L233: `the Guard` → «la Guardia»; `polities` → «entità politiche».

**L241 chiuso il 2026-10-20 — primo lotto di `successor jobs.txt`**: righe **16–280**, **86 unità** (76 `TEXT` + 5
`VALUE` + 5 `DESCRIPTION`), 428 parole EN → 445 IT, **18 contesti**, **0 tab**, **0 virgolette**, **0 apici**, **45
segnaposto** in 8 famiglie. `check.py` 33 controlli, `verify.py` 28 con invariante di **segmento** (86/124). `sha256[:16]`
= `19c694523a5473df`. **66 unità sono frammenti** che il gioco concatena: **1104 combinazioni** per lingua verificate una
per una, con i gruppi ricostruiti dal file del gioco nel `verify.py`. **4 frammenti** hanno uno spazio finale in meno
dell'inglese, perché l'oggetto comincia con uno spazio (altrimenti **due** spazi); l'**opzione vuota** del quarto gruppo
non è inventariata: lacuna dichiarata.

**L242 da aprire — TERMINALE, secondo e ultimo di `data/successors/successor jobs.txt`**: righe **306–802**, **38 unità**
(19 `VALUE` + 19 `DESCRIPTION`), 480 parole, **19 contesti**, **0 tab**, **0 virgolette**, **0 apici**, **98 segnaposto** in
**10** famiglie (entra **`<tons>`** 11). Niente frammenti: 19 descrizioni distinte. `Old Houses` → «Vecchie Casate»,
`New Houses` → «Nuove Casate» nella prosa, invariati nei `VALUE`. Invariante di **FILE**: `86 + 38 = 124`, riga **802**
ultima, `sovrapposti = 0`. **Chiude il decimo file** della campagna. Contratto verificato in `HANDOFF_L242_20261020.md`
(`check_handoff.py` → `FAIL: 0 / 21`).

TOTALE staging: 29565 unità · 914932 EN · 872245 IT, **245 directory**. Residuo misurato: **3.034 unità / 62.172 parole** su
99 file; **68 file interamente tradotti** su 167 (il conteggio include `deep jobs.txt`, con 1 `UI_LABEL` fuori staging);
la formula di `state.py` stampa 2365.
