# review.md — L274 (`data/korath/korath ships.txt`, righe 364–602)

Registro delle decisioni editoriali del **secondo lotto** delle navi Korath: un caccia, una sonda, un ospedale e una fabbrica.

## 1. Quattro funzioni, quattro testi

| unità | che cosa installa il gioco | tono |
|---|---|---|
| `'olofez` | un **caccia** che sta in una baia | breve: origine del nome + regola tecnica |
| `Kas'ik Tek 7` | **sonde** che raccolgono e riciclano | tecnico: economia dei microbot |
| `Rai'alorej` | un **rifugio-ospedale** | umano: i Korath muoiono facilmente se feriti |
| `Ikatila'ej` | una **fabbrica** che tiene in piedi stazioni e navi-mondo | organizzativo: procedura delle commissioni |

Il primo è una scheda di **gioco** («non puoi trasportarlo senza una baia»), gli altri tre sono **racconto**. La resa li
distingue: registro asciutto per il primo, esplicativo per gli altri.

## 2. Scelte

| inglese | resa |
|---|---|
| `a fighter carried by most Exile capital ships` | **un caccia trasportato dalla maggior parte delle navi capitali dell'Esilio** |
| `named for a renowned artist who painted their visions of ancient hunts` | **intitolato a un rinomato artista che dipingeva le proprie visioni di antiche cacce** |
| `small probes are primarily deployed … to scan for intruders` | **piccole sonde … per cercare intrusi** |
| `evaluate foreign vessels, and analyze system bodies` | **valutare vascelli stranieri e analizzare i corpi del sistema** |
| `small debris and deactivated microbots` | **piccoli detriti e microbot disattivati** |
| `processing them in bulk yields a valuable gestalt of information` | **elaborarli in massa produce una preziosa sintesi d'informazioni** |
| `do not easily recover from injury` | **non si riprendono facilmente dalle ferite** |
| `a stranded, injured Korath faces poor odds of survival` | **un Korath ferito e isolato ha scarse probabilità di sopravvivere** |
| `thoroughly appointed with lifeform scanners, locator beacon receivers, ambulances` | **dotato di tutto: scanner per forme di vita, ricevitori di radiofari di localizzazione, ambulanze** |
| `incubators and nurseries … to treat the young who grow up aboard ship` | **incubatrici e nidi per curare i piccoli che crescono a bordo** |
| `the acceptability for failure and downtime is slim to nonexistent` | **la tolleranza verso guasti e fermi di produzione è scarsa o nulla** |
| `provide critical support` | **fornire un supporto critico** |
| `an all-in-one recycling, mining, refining, and factory ship` | **una nave tuttofare: riciclaggio, estrazione, raffinazione e fabbrica** |
| `whatever products the civilian economic planning committees have determined` | **qualunque prodotto i comitati civili di pianificazione economica abbiano stabilito** |

## 3. Tre nomi che restano

| inglese | resa | perché |
|---|---|---|
| `microbot` | **microbot** | invariato in tutto il corpus (8 unità) |
| `Systems Core` | **Systems Core** | è un **oggetto** del gioco: nome proprio |
| `Shunt-Strike` | **Colpi Shunt** | termine nuovo, dichiarato |

`Kas'ik Tek 7`, `Rai'alorej`, `Ikatila'ej`, `'olofez` restano **invariati**, apostrofi compresi.

## 4. La divergenza delle baie

`fighter bay` ha **due** rese nel corpus: «baia di caccia» (9 unità) e «baia per caccia» (2). Il lotto ha scelto la
**maggioritaria** e il `check.py` lo dimostra confrontando la resa con tutte quelle presenti nello staging. Le due unità
difformi restano **aperte**: stanno in lotti chiusi, e correggerle è una passata globale da autorizzare.

Per i droni non c'è ambiguità: «baia per droni» è l'unica forma nel corpus.

## 5. Struttura

| cosa | inglese | italiano |
|---|---|---|
| tab | **4** (unità 3, 5, 7, 9) | **4**, primo carattere |
| virgolette | **0** | **0** |
| apici | **5** (tutti nei nomi) | **13** (`dell'Esilio`, `d'informazioni`, `l'aiuto`, `un'apparecchiatura`, `L'Ikatila'ej`, `l'Ikatila'ej`, …) |
| segnaposto | **0** | **0** |

## 6. Cosa resta aperto (dichiarato)

- **Nessuna approvazione**: 9 unità `PENDING`.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Divergenza aperta**: «baia di caccia» vs «baia per caccia» (9 contro 2).
- **Il file è a 17/50**: L275 riparte dalla riga 606 con **sette contesti** (`Lor'kas Ik 577`, `Ra'gru Ik 618`,
  `Kas'lor Ik 582`, `Lor'nag Ik 590`, `Ra'at Ik 621`, `Kasichara A'awoj`, `Korsmanath A'awoj`) e **cinque `VALUE`**.
