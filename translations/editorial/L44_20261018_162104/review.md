# L44 — revisione editoriale

Lotto `L44_20261018_162104` · `data/sheragi/archaeology missions.txt` · righe 16–1718 · 625 unità ·
18.966 parole EN → 17.522 IT · `check.py` `FAIL totale: 0` · `verify.py` 37 controlli, exit 0.

Questo documento registra **le decisioni**, non i numeri: i numeri stanno in `REPORT.md` e sono
rigenerabili con i due comandi di verifica.

---

## 1. Che cosa copre il lotto

La linea **Sheragi**, la stessa che nella trama Remnant aveva fornito il reattore citato di sfuggita:
Deep Archaeology 1–7 (leggende del Deep, la chiesa di Midgard, la singolarità), la difesa di Zug, il
museo sotto la lava, il cubo e la scatola nera, Mammon su Stormhold, il Museo di Storia Galattica degli
Hai, il Ministero della Cultura, la squadra Hai (Eyama, Rakei, Desyo), e infine **la Spada di Smeraldo**:
la nave da guerra Sheragi trovata a Zubenelhakrabi, i suoi morti, il guardiano-Archon e il Cannone Fiamma
di Drago.

## 2. Ricognizione (misurata sul `source.json`)

```
MISSION_TEXT 535 · DESCRIPTION 30 · VALUE 28 · LOGBOOK 12 · DIALOG 10 · UI_LABEL 10
contesti 33 · tab 483 · virgolette 921 · token 73 (8 famiglie) · quadre 0
unità con virgolette dispari: 17
15 gruppi di inglese identico (37 unità su 625)
```

## 3. Metodo

1. `export_section.py` su righe 16–1718 → 625 unità, 33 contesti.
2. Ricognizione: 10 label (`raw`), 12 `log` (`raw`), 17 virgolette dispari, 15 gruppi di duplicati, token.
3. `check.py` derivato da L43: `NT` rimisurato a 10, **controllo `LOGBOOK` riscritto in positivo**,
   `TITLES` esteso (There Might Be Riots, Oxyrhynchus, Sibyl Greythatch, Sindacato) perché il controllo
   «parole inglesi residue» non deve scambiare nomi propri per testo non tradotto.
4. Traduzione in 13 parti da 25–50 unità, a fine contesto; `check.py --range` dopo ogni parte e
   controllo completo a metà (unità 300) e alla fine.
5. `check.py` completo **verde al primo colpo**; `verify.py` indipendente, 37 controlli.

## 4. La voce

Il lotto attraversa tre registri e li tiene distinti:

- **Foster, l'archeologo.** Vanitoso, impaziente, disposto a scavalcare le regole, ma capace di
  commuoversi davanti ai morti. La resa usa frasi brevi e un po' telegrafiche quando è eccitato
  («Straordinaria, ma tragica. Ma straordinaria»), e si spezza quando è scosso («Quello che abbiamo
  trovato. Quello che abbiamo trovato...»).
- **Le tre Hai.** Tecniche, allegre, con un registro da colleghe affiatate («questi due nerd»); Eyama è
  la più giocosa (si traveste da «Signorina Deus ex Machina»), Rakei la più concreta, Desyo la più
  precisa. Il femminile è quello del sorgente (`she`), e la traduzione lo segue senza ambiguità.
- **Il guardiano (Archon).** Frasi scandite, senza contrazioni, con tre sostantivi in fila («terrore.
  Rimpianto. Perdita.»). Il «voi» non compare: parla all'umanità al singolare, come nel sorgente.

## 5. Le scelte terminologiche

| inglese | italiano | nota |
|---|---|---|
| the Deep | **il Deep** | invariato, come in L2/L11/L14/L15/L19/L21b/L23/L24/L32/L38 |
| the Dirt Belt | **la Dirt Belt** | invariato (141 occorrenze nei lotti precedenti) |
| the Rim | **il Bordo** | già usato in altri lotti |
| Sheragi, Zug, Midgard, Vinci, Ildaria, Stormhold, Algieba, Watcher, Zubenelhakrabi, Zubeneschamali, Hai-home, Mirrorlake, Skymoot | invariati | toponimi e specie |
| Albert Foster, John, Amelia Lee, Yarthis Amorthee Dek-Farsook Nai, Eyama, Rakei, Desyo, Mammon, Sibyl Greythatch, Hiyamaharu | invariati | persone |
| Emerald Sword | **Spada di Smeraldo** | il testo stesso dice «whose name translates to the Emerald Sword»: è un nome tradotto nel gioco, non un nome proprio straniero |
| Dragonflame Cannon | **Cannone Fiamma di Drago** | Eyama lo battezza nel testo |
| GRASER | **GRASER** | acronimo tecnico; la sigla italiana non esiste |
| black box | **scatola nera** | termine comune, non un nome proprio |
| hyperdrive / jump drive | **iperpropulsore / motore di salto** | da L21/L24 |
| the Unfettered | **gli Slegati** | da L29/L32 |
| ringworld | **ringworld** | invariato, come nei lotti Coalition/Remnant |
| Oneirological archaeology | **archeologia oneirologica** | resa dotta, coerente col personaggio |
| hatchery | **cova** | non «incubatoio»: è una stanza-nido, non un impianto |
| Oxyrhynchus | **Oxyrhynchus** | nome di nave, invariato anche dentro le virgolette |

## 6. Numeri e misure: non si normalizzano

Le cifre restano quelle del sorgente: `28 tons` → «28 tonnellate», `150 additional crew` → «150 persone
in più», `50 tons` → «50 tonnellate», `120 years` → «120 anni», `8 meters` → «8 metri», `10 million
credits` → «10 milioni di crediti», `three hundred thousand credits` → «trecentomila crediti». Le cifre
in lettere del sorgente sono state rese in lettere («trecentomila», «quattrocentomila»), quelle in cifre
in cifre.

## 7. Lacuna di inventario

**Cinque righe `log` a tre argomenti** (unità 49, 180, 409, 410, 411): il `raw` è
`log "Categoria" "Nome" `testo``, l'unità estratta è solo il testo, quindi **categoria e nome restano in
inglese** nel gioco. È il difetto noto di `tools/l10n.py` (protetto, non si ripara): si documenta.
Qui è cosmetico, perché i nomi sono invarianti per scelta (`People`, `Factions`, `Albert Foster`,
`Sheragi`, `Desyo`, `Rakei`, `Eyama`).

Le altre **sette** righe `log` a un argomento sono interamente tradotte.

## 8. Cosa è stato corretto e perché

Il `check.py` completo è passato **al primo colpo**: nessuna unità è stata riscritta per il gate. Le
uniche correzioni sono avvenute durante la scrittura:

- **unità 92**: il controllo «parole inglesi residue» segnalava `be` e `there` — erano dentro il nome
  della band **There Might Be Riots**, non testo non tradotto. Corretto il `check.py` (`TITLES`), non la
  traduzione: è il caso in cui il difetto è dello strumento.
- **unità 322**: una battuta aperta nel sorgente; la prima stesura del file JSON conteneva uno spazio e
  un a capo finali che rompevano il JSON. Corretto il file della parte, non la regola.
- **unità 625**: un carattere non latino (una `Ɵ` al posto della `t`) è stato intercettato dal controllo
  tipografico prima della chiusura.

## 9. Controlli e limiti

`check.py` (25 controlli): copertura, unità vuote, `NT` (10), righe `log` 12/12, duplicati italiano
spiegati dal sorgente, tab per unità e come totale, tab iniziale, virgolette per unità e come totale,
quadre, token, backtick, spazi, rapporto, tipografia, caratteri non latini, parole residue, stato del
database.

`verify.py` (37 controlli) ricostruisce tutto da `source.json`, dal file sorgente e da `state.db` in sola
lettura. In più asserisce: le 10 `UI_LABEL` identiche **come elenco**, le **12 `LOGBOOK`** presenti,
tradotte, con tab, e le **5 a tre argomenti** identificate per indice con la verifica che categoria e
nome **non** siano finiti dentro l'unità, l'assenza di `CONVERSATION` e di quadre, l'insieme delle 17
virgolette dispari, la parità di tab e virgolette per unità, la copertura 625/625 e la coppia (16, 1718).

Limiti, dichiarati:

- **Il lotto non è nel gioco.** Nessuna approvazione nel database, nessun caricamento: 625 unità `PENDING`.
- **Nessuna verifica a schermo.** Non ho visto la città sotto la lava, Mammon, né la Spada di Smeraldo
  nello spazioptorto: i `goto` sono intatti per costruzione (le 10 label sono byte-identiche), ma il
  percorso non è stato giocato.
- **Il rapporto 0,61–1,77 non è un giudizio di qualità.**
- **`Emerald Sword` → «Spada di Smeraldo» è una scelta, non una svista**: il sorgente la presenta come
  traduzione di un nome Sheragi, e il gioco la usa come nome della nave acquisita. Chi riprende la serie
  deve mantenerla, non «ripristinare» l'inglese.
