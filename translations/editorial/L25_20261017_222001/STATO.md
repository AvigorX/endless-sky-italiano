# L25 — stato di avanzamento (CHIUSO il 2026-10-17)

`data/coalition/coalition missions.txt`, righe **16–2907**, **1.174 unità**, 37.459 parole, 65 contesti.
Segmento di un file più grande: dopo la riga 2907 restano **406 unità** (righe 2913–3868) per un lotto
successivo. Deviazione dal target: **−6,4%**, dichiarata in `HANDOFF_L25` §3.

## Fatto

| parte | unità | righe | esito |
|---|---|---|---|
| part01 | 1–90 | 16–292 | `check.py --range 1 90` verde |
| part02 | 91–180 | 293–517 | `check.py --range 91 180` verde |
| part03 | 181–270 | 520–716 | `check.py --range 181 270` verde |
| part04 | 271–360 | 721–966 | `check.py --range 271 360` verde |
| part05 | 361–450 | 973–1198 | `check.py --range 361 450` verde |
| part06 | 451–540 | 1199–1439 | `check.py --range 451 540` verde |
| part07 | 541–630 | 1440–1632 | `check.py --range 541 630` verde |
| part08 | 631–720 | 1633–1869 | `check.py --range 631 720` verde |
| part09 | 721–810 | 1870–2076 | `check.py --range 721 810` verde |
| part10 | 811–900 | 2079–2321 | `check.py --range 811 900` verde |
| part11 | 901–990 | 2322–2516 | `check.py --range 901 990` verde |
| part12 | 991–1080 | 2517–2693 | `check.py --range 991 1080` verde |
| part13 | 1081–1174 | 2695–2907 | `check.py --range 1081 1174` verde |

**1.174 / 1.174 unità · 37.459 EN → 35.851 IT (100%)**

Misure dell'esecuzione completa su tutte le 1.174 unità (lette, non dedotte): tab **869/869**, virgolette
**1746/1746**, token **331/331**, backtick 0/0, rapporto 0,64–1,89, nessuna parola inglese residua,
nessun duplicato italiano non giustificato dal sorgente.

## Regole specifiche di questo lotto

- **`NT` = 16 unità**, tutte `UI_LABEL`: sono righe `label "…"` con un `goto` a monte, quindi nomi di
  nodo. Verificato: **zero** `label` fuori da `UI_LABEL` nel `raw`, e il file **non contiene blocchi
  `conversation`** (i tipi presenti sono `MISSION_TEXT`, `VALUE`, `DESCRIPTION`, `LOGBOOK`, `DIALOG`,
  `UI_LABEL`). Elenco: 109, 111, 509, 520, 536, 558, 602, 630, 640, 646, 648, 661, 710, 733, 752, 1079.
- **`TOKEN_EXC` vuoto**: nessun pronome-token nel sorgente. Token presenti: `<planet>`, `<destination>`,
  `<last>`, `<date>`, `<origin>`, `<cargo>`, `<capacity>`, `<first>`, `<payment>`, `<bunks>`,
  `<stopovers>`, `<ship>`, `<system>`.
- **106 `MISSION_TEXT` non hanno il tab iniziale**: il tab va confrontato per unità, non per totale.
- **Citazioni a conteggio dispari note**: unità **800** e **1004** (verificate prima della parte che le
  contiene; l'elenco va ricalcolato con `english.count('"')` a ogni parte).
- **42 gruppi di duplicati inglesi / 110 unità**: l'italiano identico è ammesso solo dentro un gruppo.

## La sintassi dei popoli della Coalizione (decisione centrale del lotto)

Saryd, Kimek e Arachi parlano con **l'ordine della frase rovesciato**: il complemento o l'oggetto prima,
il soggetto esplicito, il verbo in fondo, e gli ausiliari in coda. Non è un refuso: è la loro voce, e
tutti e tre la condividono (parlano attraverso traduttori automatici).

Regola di resa, applicata in modo sistematico:

| inglese | italiano |
|---|---|
| `In the name of the Heliarchs, … we the human visitor greet.` | «In nome degli Heliarchs, … **noi il visitatore umano salutiamo**.» |
| `Our nearest and most recent neighbor you are.` | «Il nostro vicino più prossimo e più recente **voi siete**.» |
| `The wise Heliarchs, all your questions they will answer.` | «Gli Heliarchs saggi, a tutte le vostre domande **risponderanno**.» |
| `Once to the Heliarchs you have become known, … contribute you may.` | «Una volta che agli Heliarchs **sarete noti**, … **contribuire potrete**.» |

Tre vincoli per non renderla illeggibile:
1. **soggetto esplicito obbligatorio** (`noi`, `voi`, `loro`) quando il verbo è in fondo: senza, la frase
   diventa incomprensibile e non più riconoscibile come «voce aliena»;
2. **un solo verbo finale per proposizione**: se l'inglese ne accatasta due, si spezza in due proposizioni
   parallele, entrambe con il verbo in coda;
3. **i connettivi restano in italiano normale** (`e`, `ma`, `perché`, `quando`): l'inversione riguarda
   l'ordine dei costituenti, non la sintassi delle subordinate.

Le **voci fuori campo** (il narratore, i log, le descrizioni delle missioni) e i **personaggi non
Coalizione** usano **italiano normale**: Alitis l'Alpha (unità 549–578) parla come un umano, aggressivo
e diretto, ed è il contrasto che lo distingue dai tre popoli. Anche l'Heliarch militare che
spiega le regole usa italiano normale: la voce rovesciata è solo dei tre popoli della Coalizione.
È il contrasto che rende leggibile il testo: se tutto fosse rovesciato, il lotto diventerebbe illeggibile.

## Glossario L25 (aggiunte a quelle di L24)

| inglese | italiano | nota |
|---|---|---|
| `Heliarchs` / `Heliarch` | Heliarchs / Heliarch | invariato, sia singolare sia plurale |
| `Saryd(s)` | Saryd | invariato, plurale identico |
| `Kimek` | Kimek | invariato |
| `Arachi` / `Arach` | Arachi / Arach | invariato (specie / individuo) |
| `Coalition` | Coalizione | |
| `Quarg` | Quarg | invariato, come in L24 |
| `ringworld` | mondo ad anello |
| `Distant Home` | Casa Lontana | pianeta: nome tradotto e usato anche nel registro (1038) |
| `Ancient Light` | Luce Antica | pianeta |
| `Summit` | Vetta | pianeta |
| `Report: …` | Rapporto: … | nomi delle missioni |
| `Punisher` | Punisher | nave, invariata |
| `Sheragi` | Sheragi | specie estinta, invariata |
| `Saros` | Saros | regione Saryd, invariata |
| `Zug` | Zug | pianeta, invariato |
| `Albert Foster` | Albert Foster | invariato |
| `decryption pylon` | pilone di decrittazione | |
| `countersignals` | controsegnali | |
| unità 1004 | 5 virgolette nel sorgente (l'ultima non chiusa) | riprodotte esattamente: 5 in italiano |
| unità 1034 | 6 virgolette | 6 in italiano, con la seconda battuta introdotta da «Pensa per un momento, poi continua:» | |
| `yottrite` | yottrite | minerale, invariato |
| `Punisher`, `Neutralizer`, `Spindle` | invariati | nomi di nave |
| `Arach "Houses"` | «Case» Arach | corporazioni |
| `outfitter` | fornitore di equipaggiamento | coerente con L24 |
| `jump drive` | motore di salto | coerente con L24 |
| `civilians` / `citizens` | civili / cittadini | distinzione mantenuta |
| `Starlit University` | Starlit University | invariato (ateneo) |
| `Secret Sky` | Secret Sky | invariato (mondo) |
| `Arach rum` | rum Arach | |
| `Arach Courier` | Courier Arach | nome di nave |
| `House Idriss` | Casa Idriss | |
| `Department of Health` | Dipartimento della Salute | |
| `longcow` | longcow | animale da allevamento, invariato |
| `Leviathan` | Leviathan | nave di Betelgeuse, invariata |
| `Betelgeuse Shipyards` | Cantiere Betelgeuse | |
| `Syndicated Shipyards`, `Deep Sky` | Cantiere Sindacato, Deep Sky | |
| `Drugub` | Drugub | fumettista Arach |
| `foster home` | casa affidataria | |
| `Alitis` / `Athis` | Alitis / Athis | Alpha, nome proprio |
| `Alpha` | Alpha | invariato (come in L24) |
| `Fascia di Terra` (`Dirt Belt`) | Fascia di Terra | da `TITLES` di L24 |
| `Detention facility` | struttura di detenzione | |
| `xenology` | xenologia | |
| `Aelbris` | Aelbris | scienziato Saryd |
| `103°` | centotreesimo | il simbolo `°` è rifiutato dal controllo tipografico: si scrive in lettere |
| `Vellorae` / `Adfices` | Vellorae / Adfices | vedova Saryd e marito defunto |
| `Aul Kell` / `Velaulra` / `Magl Ina` | Aul Kell / Velaulra / Magl Ina | divinità Saryd, invariati |
| `Shrine of the World Shaper` | Santuario del Modellatore del Mondo | |
| `Caretaker's Blessing` | La Benedizione della Custode | |
| `Visit the Witch of Dusk` | In visita alla Strega del Crepuscolo | |
| `Master Hunter's Path` | Il sentiero del Maestro Cacciatore | |
| `Republic` / `Free Worlds` / `Syndicate` | Repubblica / Mondi Liberi / Sindacato | |
| `Unfettered` | gli Unfettered | fazione Hai, invariata |
| `Kor Sestor` / `Kor Mereti` / `Kor Efreti` / `Korath Exiles` | Kor Sestor / Kor Mereti / Kor Efreti / Korath Esuli | |
| `datapad` | datapad | invariato |
| `Lor Ie Vees` / `Ensu Uri` | Lor Ie Vees / Ensu Uri | divinità Saryd, invariati |
| `Woodland Thing` | Cosa del bosco | nome della missione |
| `Pilgrimage's End` | Fine del pellegrinaggio | |
| `Council of Ahr` | Consiglio di Ahr | |
| `houses Ablomab/Bebliss/Chamgar` | Casa Ablomab / Bebliss / Chamgar | |
| `Stronghold of Flugbu` / `Hammer of Debrugt` / `Delve of Bloptab` | invariati | nomi di stazioni Arach |
| `Bloptab's Furnace` | Fornace di Bloptab | |
| `Kimek Thorn` | Kimek Thorn | nave, invariata |
| `Dubug` | Dubug | rappresentante della Casa Ablomab |
| `House Oberegt` | Casa Oberegt | famiglia reale Arach |
| `House Mallob` / `House Garbarag` / `Debdo` | Casa Mallob / Casa Garbarag / Debdo | |
| `Lord`/`Lady Plubat` | Lady Plubat | due omonimi: Bebliss (donna) e Chamgar (uomo) |
| `Apri'ie` | Apri'ie | ricercatore Kimek |
| `Pale Waters` | Acque Pallide | centro di ricerca |
| `Second Cerulean` | Second Cerulean | invariato |
| `repair modules` | moduli di riparazione | |
| `Underwater Delivery` | Consegna sottomarina | |
| `Pressurized Stress Test` / `Tectonic Stress Test` | Prova di stress in pressione / tettonico | |
| `trucks with continuous tracks` | camion a cingoli | |
| `fjord` | fiordo | |
| peso dei sottomarini | circa 60 tonnellate | dato del testo, unità 875 |
| `Sedlitaris Quatcid` | Sedlitaris Quatcid | tribuna Heliarch Saryd |
| `Mimodum` | Mimodum | antenato, sparito mille anni prima |
| `Kicharri` | Kicharri | arbitro Kimek, superiore di Sedlitaris |
| `Repilor` | Repilor | fratello di Sedlitaris |
| `inspector` | ispettore | grado Heliarch per gli esploratori |
| `Tribune` | Tribuna | grado Heliarch |
| `arbiter` | arbitro | |
| `consuls` / `the council` | i consoli / il consiglio | |
| `Saryd Sojourner` / `Traveler` | Sojourner / Traveler | navi, invariate |
| `relay pylon` | pilone relè | |
| `Scouting Permit` / `Relay Pylon` / `Dusted Dead Drop` | Permesso di ricognizione / Pilone relè / Nascondiglio impolverato | |
| unità 800 | virgoletta aperta e non chiusa | riprodotta: il sorgente ha 1 virgoletta, l'italiano 1 |
| sepoltura in gemma | bracciale con le ceneri | pratica Saryd spiegata nel testo, non nel lessico |

## Chiusura (esito misurato)

```
check.py (intero lotto)   FAIL totale: 0
  tab 869/869 · virgolette 1746/1746 · token 331/331 · backtick 0/0
  rapporto 0,64-1,89 · caratteri non latini: nessuno · trattini lunghi: nessuno
verify.py                 24 controlli · FAIL: 0 · exit 0
translation.json          sha256[:16] fc850daffc4363da
```

`verify.py` asserisce, fra le altre cose, che il lotto **inizia alla riga 16** e che **restano 406 unità
dopo la 2907**: il file `coalition missions.txt` non è completo con questo lotto (1.174 di 1.580 unità,
74,3%) e il verificatore lo dichiara invece di pretendere il contrario.

Documenti di chiusura: `review.md` (8 sezioni) e `REPORT.md`. Le 1.174 unità sono **`PENDING`** nel DB:
lo staging **non** è approvazione, e nulla è mai stato renderizzato nel gioco.

## Dopo L25

Il resto di `data/coalition/coalition missions.txt`: **righe 2913–3868**, **406 unità**, **10.765 parole**
(riga di ripresa misurata con `next_section.py`). Chiude il file a 1.580/1.580.
