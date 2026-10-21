# L25 — data/coalition/coalition missions.txt, righe 16–2907

Revisione del lotto chiuso. Tutti i numeri qui sotto sono misurati (`check.py`, `verify.py`,
`translation.json`, `state.db`); le cifre del documento non sostituiscono quelle del workspace.

## 1. Che cosa contiene il lotto

**1.174 unità** (righe 16–2907 di 1.580 unità del file), **37.459 parole EN → 35.851 IT** (rapporto
complessivo **0,957**). **65 contesti** distinti, **13 parti** da 80–94 unità.

| tipo | unità | note |
|---|---|---|
| `MISSION_TEXT` | 975 | testo di missione, offre, dialoghi, rami |
| `DIALOG` | 64 | righe mostrate all'atterraggio (scorta, rilevamento) |
| `VALUE` | 56 | nomi di missione (`name`) |
| `DESCRIPTION` | 56 | descrizioni brevi nel pannello missioni |
| `UI_LABEL` | 16 | **non traducibili**: bersagli di `goto` |
| `LOGBOOK` | 7 | voci di registro |

Nessun blocco `conversation`, nessun `label` fuori dai 16 `UI_LABEL`: verificato sul file prima
dell'export, quindi `TOKEN_EXC` è vuoto e non ci sono pronomi-token da ammettere.

## 2. La voce della Coalizione (decisione linguistica centrale)

Saryd, Kimek e Arachi parlano con **ordine rovesciato**: complemento, poi soggetto esplicito, poi
verbo in fondo, e il verbo regge l'ausiliare in coda.

> «Aiutato molto a sistemare tutto, voi ci avete, capitano <last>.» (452)
> «In debito con voi, siamo, capitano.» · «Prendersi cura di loro, i Saryd lì lo faranno.» (488)

Tre vincoli applicati per non renderlo illeggibile:
1. **un solo rovesciamento per frase** quando la frase è lunga, per non perdere il filo;
2. i **numeri, i nomi e i token** restano al loro posto sintattico naturale;
3. la voce è **dei tre popoli**, non dello stile globale del testo.

Chi **non** parla rovesciato, e perché:
- **Alitis l'Alpha** (549–578): parla italiano normale, aggressivo e diretto. È il contrasto che lo
  distingue dai tre popoli, e nel sorgente è evidente (nessun rovesciamento nelle sue battute).
- il **narratore**, i **log** (`LOGBOOK`), le **descrizioni** delle missioni e i `DIALOG` di atterraggio.
- l'**Heliarch militare** che spiega le regole e i **consoli** quando parlano in registro
  amministrativo: restano rovesciati solo dove il sorgente lo fa.

## 3. Terminologia

Voci nuove di L25 (in `STATO.md`, con la resa scelta): `Starlit University` (invariato), `Secret Sky`
(invariato), `rum Arach`, `Arach Courier`, `Casa Idriss`, `Casa Mallob`, `Casa Oberegt`,
`Casa Garbarag`, `Casa Bebliss`, `Casa Chamgar`, `Casa Ablomab`, `Debdo`, `Dipartimento della Salute`,
`longcow` (invariato), `Leviathan`, `Cantiere Betelgeuse`, `Cantiere Sindacato`, `Deep Sky`, `Drugub`,
`casa affidataria`, `Alitis`/`Athis`, `Fascia di Terra`, `struttura di detenzione`, `xenologia`,
`Aelbris`, `Lor Ie Vees`, `Ensu Uri`, `Aul Kell`, `Velaulra`, `Magl Ina`, `Vellorae`, `Adfices`,
`Consiglio di Ahr`, `Second Cerulean`, `Acque Pallide`, `Apri'ie`, `Sedlitaris Quatcid`, `Mimodum`,
`Kicharri`, `Repilor`, `ispettore`, `Tribuna`, `arbitro`, `consoli`, `pilone di decrittazione`,
`controsegnali`, `mondo ad anello`.

Nomi di pianeta **tradotti** e usati anche dentro i registri audio, per coerenza interna:
`Distant Home → Casa Lontana`, `Ancient Light → Luce Antica`, `Summit → Vetta`.

Restano invariati: navi (`Punisher`, `Kimek Thorn`, `Sojourner`, `Traveler`, `Leviathan`), specie
(`Sheragi`, `Hai`, `Unfettered`, `Korath`), toponimi non descrittivi (`Saros`, `Zug`, `Ahr`,
`Algieba`, `Ablub`, `Hopper`, `Harmony`, `Rand`), nomi propri.

## 4. Duplicati

**42 gruppi di inglese identico, 110 unità.** Sono righe strutturali del gioco: le risposte
alternative che portano allo stesso esito, i `DIALOG` di scorta mancante, i blocchi di Drugub ripetuti
nelle due missioni del fumettista, le righe di capacità (`You need <capacity>…`).

Due casi in cui **il sorgente differisce per un dettaglio** e la traduzione lo riproduce:
- **521 / 537**: `thanks again, Captain` / `thanks again Captain` → «grazie ancora, capitano» /
  «grazie ancora capitano» (una virgola di differenza, come nel sorgente);
- **1172 / 1173**: la seconda aggiunge una frase finale (l'ora di riposo e la chiamata delle autorità).

## 5. Correzioni reali (FAIL trovati e risolti)

| unità | difetto | correzione |
|---|---|---|
| 62 | `Jump Drive Loan` → «Prestito di un motore di salto» dava rapporto 2,00 (> 1,9) | «Motore di salto in prestito» |
| 612 | `103°` conteneva `°` (U+00B0), rifiutato dal controllo tipografico | «il centotreesimo Seminario di Xenologia» |
| 718 | tab iniziale assente nel sorgente, presente in italiano | tab rimosso (tab 70/70) |
| 1034 | sorgente 6 virgolette, italiano 4 | aggiunta la chiusura prima di «Pensa per un momento, poi continua:» |
| 1022 | `Of course. Where are we heading?` traduceva come 761 (`Sure. Where are we going?`) | «Ma certo. Dove siamo diretti?» |

Nessun controllo è stato allentato: le correzioni sono sempre state fatte sul testo o sul formato,
mai sulla soglia.

## 6. Limiti noti (del sorgente, non correggibili da qui)

- **Unità 800**: il sorgente ha **una sola virgoletta** (aperta e mai chiusa) su un discorso lungo
  dell'Arach. L'italiano ne ha una sola, nello stesso punto. Se un giorno il testo inglese venisse
  corretto, questa unità andrebbe rifatta.
- **Unità 1004**: **5 virgolette** nel sorgente, con l'ultima battuta non chiusa. Riprodotte 5.
- **Unità 612**: il numero ordinale è scritto in lettere perché il simbolo `°` è vietato dalla
  tipografia del lotto. Non è una scelta stilistica, è un vincolo del checker.
- **Nomi di nave e di specie invariati** (Punisher, Skylance, Sheragi, Hai): non sono traducibili
  senza inventare un lessico che il gioco non usa altrove.
- **Il registro della Coalizione** è una scelta editoriale, non una traduzione letterale: chi legge
  l'inglese troverà frasi più brevi. La sintassi italiana è più lunga, e il rapporto complessivo
  0,957 lo mostra (leggermente sotto 1).

## 7. Esito misurato

```
check.py (intero lotto)   FAIL totale: 0
  tab 869/869 · virgolette 1746/1746 · token 331/331 · backtick 0/0
  rapporto 0,64–1,89 · caratteri non latini: nessuno
verify.py                 24 controlli · FAIL: 0 · exit 0
translation.json          sha256[:16] fc850daffc4363da
```

`verify.py` ricontrolla in modo indipendente: riga grezza contro il file, `english/kind/path` contro
`state.db`, stato `PENDING`, nessuna `APPROVED`, id e ordine, collocazione 1.174 unità righe 16–2907,
406 unità residue dopo la 2907, nessuna sovrapposizione con altri lotti sullo stesso file, 16 NT,
token, tab/virgolette/backtick,
italiano non vuoto, divieto di trattini lunghi, rapporto, ricostruzione da parti.

## 8. Che cosa non è stato fatto

- **Nessuna approvazione nel database**: le 1.174 unità sono `PENDING`. Lo staging **non** è
  approvazione.
- **Nessun rendering nel gioco**: la traduzione non è mai stata caricata nel motore né vista a schermo.
  Non sappiamo se le stringhe entrano nei riquadri, se i `VALUE` lunghi troncano, se il registro
  rovesciato regge la lettura a schermo.
- **Nessuna revisione umana terza**: questo documento è scritto da chi ha tradotto.
- **Il resto del file** (406 unità, righe 2913–3868, 10.765 parole) resta per il lotto successivo.
