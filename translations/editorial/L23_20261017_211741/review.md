# review.md — L23 · `data/human/deep missions.txt` (Endless Sky IT)

**Unità** 1.355 (righe 16–4293, file completo) · **contesti** 83 · **parole** 38.724 EN → 36.319 IT
(rapporto complessivo 0,938; estremi per unità 0,58–1,65) · **parti** 15.
Traduzione eseguita in sessione, senza servizi esterni né sub-agenti.

## 1. Struttura e tipi di unità

| tipo | unità | cosa sono | trattamento |
|---|---:|---|---|
| `MISSION_TEXT` | 1.041 | prosa di missione, con `\t` iniziale e virgolette esterne | tradotte |
| `CONVERSATION` | 122 | dialoghi con `goto`; 6 contengono `label` di condizione | tradotte tranne le 6 `label` |
| `DESCRIPTION` | 54 | istruzioni di missione, con `<destination>`, `<stopovers>`, `<payment>` | tradotte, token intatti |
| `VALUE` | 52 | nomi di missione (`name "…"`) | tradotti (52/52) |
| `DIALOG` | 43 | avvisi di sistema ("Hai raggiunto `<planet>`, ma…") | tradotte |
| `UI_LABEL` | 22 | nomi di nodo, bersagli di `goto` | **identiche** |
| `LOGBOOK` | 19 | voci di diario | tradotte |
| `TEXT` | 2 | nomi di equipaggiamento dentro la descrizione della Bactrian | **identiche** |

`NT` = 30: le 22 `UI_LABEL`, le 2 `TEXT`, e 6 `label` di condizione dentro `conversation`
(373, 375, 383, 386, 389, 404), riconosciute leggendo il `raw` e non dal `kind`.

## 2. Casi linguistici nuovi

1. **Registro di Hjlod.** Parla un italiano con articoli caduti e frasi brevi, coerente con
   l'Ondurdis già chiusa in L21a: «Io sono di qui. Ho passato tutta vita a attraversare questa
   tundra», «Tu hai domande?», «Loro mangiano molti ricercatori stupidi e turisti». L'inglese
   storpiato dell'originale (`velcome`, `vork`, `veapon`, `novhere`) **non** è trasportabile: in
   italiano non significa nulla e il controllo delle parole residue lo rifiuterebbe.
2. **Burocratese aziendale** (Jakob Forsyth, Kaiden e soci): registro opposto, sostenuto e pieno di
   formule («un rapporto duraturo e vantaggioso», «riurbanizzazione», «detrazione fiscale»).
   Il contrasto con Hjlod è la caratterizzazione: non va appiattito.
3. **Aldfrith** parla per immagini (onda, vento, tempesta) e con un tono da vecchio marinaio:
   conservato il parlato lento, senza spezzare le frasi.
4. **Gergo dei trasportatori** (Hroar): «pivello assassino», «ti storpiaccio e basta», «sacco di
   plastica», «bel guaio». Registro basso ma italiano, non calco.
5. **Plurale collettivo `Skadenga`**: etnonimo invariato, con articolo italiano («gli Skadenga»,
   «figlie di Skade» quando parla l'Ondurdis, che usa il femminile del suo popolo).
6. **`they` neutro**: dove l'inglese usa `they` per una persona non identificata la traduzione usa
   perifrasi («è responsabile», «sono dispositivi»), mai un genere forzato. Per il giocatore si usa
   la seconda persona senza participi concordati («Sono sorpreso», «Ti hanno visto»).

## 3. Terminologia (decisioni di questo lotto)

| inglese | italiano | nota |
|---|---|---|
| `Elf-Stone` | Pietra-Elfica | famiglia coerente, non invariato |
| `God-Stone` | Pietra-Divina | già in uso in L21a |
| `Goddess-Stone` | Pietra della Dea | la pietra di Skade su Nifel |
| `Ran-Stone` | Pietra di Ran | la parete in mare di Windblain |
| `Jotun-Stones` | Pietre-Jotun | citate una volta, in elenco |
| `Ice-Crawler` | cingolato del ghiaccio | veicolo narrativo, non un `outfit` |
| `Ice-Slug` | Lumaca di Ghiaccio | creatura |
| `Transport Union` | Unione dei Trasporti | «Sindacato» resta la fazione (Syndicate) |
| `Census and Culture Bureau` | Ufficio del Censimento e della Cultura | |
| `Vice Planetary-Governor` | Vice Governatore Planetario | |
| `Tears of Skade` | Lacrime di Skade | già in L21a |
| `Setstokkr` | Setstokkr | invariato, reliquia |
| `Family-Cairn`, `cairn` | Family-Cairn, cairn | invariati, con articolo italiano |
| `Hardy Hroar's Haulers` | invariato | nome commerciale (e slogan tradotto) |
| `The Adventurer's Due` | Il Conto dell'Avventuriero | gioco di parole su *due/conto* |
| `Colonial Graffiti` | Graffiti Coloniali | targa del centro commerciale |

## 4. Ripetizioni e duplicati

- **58 gruppi / 127 unità** con inglese identico nel file: l'italiano identico è ammesso solo lì
  (`DUP_OK` deriva dal sorgente). Casi reali: le tre risposte «Woah, woah, woah!» (919/922/926),
  i due avvisi di scorta mancante (1113/1118, 1239/1252), le due `Evacuate <origin>` (1247/1253),
  le due `Stones of Skadenga` (1308/1311), i due `Hjlod Remembers` (1321/1333).
- **Falsi duplicati gestiti a mano**: 1350/1351/1352 (le tre varianti della recensione del libro,
  che differiscono per un inciso), 1310/1315 (gladdened/happy, mari invece di vento), 1116/1249/1255
  (over-crowded/crowded), 1312/1318 (identiche, mantenute identiche).

## 5. Correzioni fatte durante il lotto

| unità | difetto | correzione |
|---|---|---|
| 776 | citazione **mai chiusa** nel sorgente (1 sola virgoletta) | riprodotta aperta, non chiusa d'ufficio |
| 1023 | il nome del ristorante nel sorgente è fra virgolette **doppie** | virgolette doppie, non singole |
| 737 | «gli unici recenti hanno visto noi due», calco | «quelli recenti ci hanno visti insieme» |
| 789 | tu/voi incoerente nella liberatoria | «Tu non potrai citarci… e nemmeno i tuoi eredi» |
| 781 | mancava la virgola del vocativo | «è meraviglioso, ser, davvero meraviglioso!» |
| 971, 974 | `Ran-Stone` contro la famiglia delle pietre | «Pietra di Ran» |
| 1151 | il sorgente scrive «Clara Von Hausen» per Carla | normalizzato in Carla, senza toccare il gioco |

## 6. Esito dei controlli (misurato)

`check.py` (lotto completo): **`FAIL totale: 0`** · copertura **1355/1355** · tab **1064/1064** ·
virgolette **1816/1816** · token **280/280** · backtick 0/0 · nessuna parola inglese residua ·
tipografia pulita · rapporto 0,58–1,65 · `state.db` 364/32560 con tutte le unità del lotto `PENDING`.

`verify.py` (indipendente): **22 controlli, exit 0**. Include riga grezza identica al file su tutte
le 1.355 unità, `english`/`kind`/`path` identici al database, file completo (16–4293, nulla prima né
dopo), copertura dello staging 1355/1355 da un solo lotto, `NT` identiche, token in parità esatta,
ricostruzione di `translation.json` dalle 15 parti.

`translation.json` sha256[:16] **f745dd523ff32319** (dopo l'ultima esecuzione di `check.py`).

## 7. Cosa **non** è stato fatto

- **Rendering nel gioco**: non eseguito. La resa delle accentate dipende dall'atlante bitmap del font
  (vedi §4.4 del checkpoint) e resta **non verificata**. Nessuna riga di questo lotto è stata vista a
  schermo.
- **Database**: nessuna unità è stata approvata; lo staging non è approvazione (`APPROVED` resta 364).
- **Build e packaging**: non eseguiti, come da divieto §9.
- **Revisione umana**: il lotto è stato riletto in sessione, unità per unità, ma non da un revisore
  terzo. I controlli strutturali non certificano la qualità della lingua.
