# L29 — rapporto di chiusura

Lotto `L29_20261018_103254` · `data/hai/hai missions.txt` · righe 23–2696 · 823 unità ·
tradotto a mano, chiuso il 2026-10-18.

## 1. Che cosa contiene il lotto

Questo è l'intero `hai missions.txt`: 823 unità, 54 contesti, dalla prima missione dopo
l'intestazione alla fine del file. I nuclei narrativi, nell'ordine in cui compaiono:

- **Primo contatto con gli Hai** a Greenwater: il pianeta di roditori giganti intelligenti,
  il cunicolo che collega il loro spazio a una regione isolata dello spazio umano, i mercanti
  umani che vivono lì per sfuggire alla guerra. Le domande del giocatore sui motori di salto
  restano senza risposta, e il testo lo dice esplicitamente.
- **La storia degli Slegati** raccontata da un anziano Hai: le incursioni dei Korath, gli Hai
  che si sono ritrovati senza guerra, la scelta della stabilità contro l'espansione, il fuoco
  che brucia alto e poi diventa braci. Il finale è una metafora, non una risposta politica.
- **L'avvertimento del mercante**: le fazioni fra i mercanti Hai, i «Simpatizzanti», il fatto
  che per uno straniero la legittima difesa non sia un argomento adeguato quando muoiono
  cittadini Hai.
- **Elliot**, il ragazzo scappato dalla fattoria di famiglia e nascosto nella stiva di un
  mercantile, che torna a casa dopo quasi sei anni.
- **Il bambino Hai nella stiva**, con le due varianti (traduttore assente o presente).
- **David Turner**, l'imprenditore dei Paradise Worlds: fornitore di equipaggiamenti umani
  nello spazio degli Hai, poi cantiere navale con licenza Megaparsec. Due archi di missione
  con lo stesso schema (convoglio da scortare, costruzione, rendita giornaliera).
- **Arthur e Kiru** alla convention cosplay di Vinci; **Anaya e Touhar**, coppia interspecie
  in viaggio di nozze su Featherweight.
- **La Legione di Scar**: pirati che scoprono il cunicolo, il covo in un asteroide svuotato,
  il tributo di tecnologia Hai, il duello con il capo. Include il sospetto che dietro gli
  «umani slegati» ci siano gli Alpha.
- **Nanachi**, la giovane capitana Hai con un prestito da pagare: le prime consegne, la
  famiglia Hai con tre figli, le spezie Quarg per la festa di Allhome, il convoglio d'arte
  attaccato e il salvataggio su Prime.
- **Le missioni Strider**: la tecnologia di riparazione dello scafo, la delegazione di
  Yashili, i due percorsi alternativi (Remnant e Coalizione), il `Pond Strider` e il drone
  `Flea` come risposta al `Solifuge` degli Slegati.
- **La troupe cinematografica di Likeet** che gira un film dell'orrore sulla stazione
  abbandonata di Darkrest; gli studenti in gita a caccia di fantasmi, con le conseguenze
  legali se il capitano li abbandona.
- **Hareek**, la guida spirituale che viaggia con una pietra chiave e predica agli Slegati.
- **Eeeya e Anoo**: la nonna con tre tonnellate di biscotti alle ghiande, la nipote chirurga
  traumatologa che ha scelto gli Slegati, e le due varianti di finale.

## 2. Come è stato verificato

Due verifiche indipendenti, entrambe con exit code:

| strumento | esito |
|---|---|
| `check.py` (completo, senza `--range`) | `FAIL totale: 0` · 823/823 · 10 parti · 0 unità mancanti |
| `verify.py` | **25 controlli**, `FAIL: 0`, exit 0 |
| `state.py` | `ESITO: OK` su 7 controlli di integrità |

`verify.py` non riusa la logica di `check.py`: rilegge il file sorgente originale riga per riga,
confronta `english/kind/path` con `state.db`, verifica che nessuna unità sia `APPROVED`, conta
token, tab, virgolette e backtick sul sorgente e sulla traduzione, e ricostruisce
`translation.json` dalle parti su disco. Include inoltre un controllo sulla **distribuzione dei
kind** (685 `MISSION_TEXT`, 41 `DESCRIPTION`, 35 `VALUE`, 34 `DIALOG`, 15 `UI_LABEL`,
13 `LOGBOOK`) confrontata con un valore atteso scritto a mano: se un giorno il parser cambiasse
comportamento, quel controllo diventerebbe rosso.

Ogni parte è stata chiusa con `check.py --range A B` verde prima di scrivere la successiva, e
la normalizzazione di virgolette e tab è stata eseguita in blocco dopo ogni parte, non alla fine.

## 3. Chiusura del file

`hai missions.txt` è completo: 823 unità su 823, da un solo lotto. Lo staging ha ora **nove**
file completi:

| file | unità | lotti |
|---|---|---|
| `map planets.txt` | 1.544 | 18 |
| `human missions.txt` | 4.253 | 6 |
| `intro missions.txt` | 637 | 1 |
| `jobs.txt` | 390 | 1 |
| `deep missions.txt` | 1.355 | 1 |
| `remnant 1 introduction.txt` | 1.250 | 1 |
| `coalition missions.txt` | 1.580 | 2 |
| `kahet missions.txt` | 1.738 | 2 |
| `hai missions.txt` | 823 | 1 |

## 4. Numeri strutturali

| grandezza | valore |
|---|---|
| unità | 823 |
| parole EN → IT | 23.926 → 22.373 |
| rapporto complessivo | 0,935 |
| rapporto per unità | 0,64 – 1,68 |
| contesti | 54 |
| parti | 10 (9 × 85 + 1 × 63) |
| tab | 606 |
| virgolette | 1.260 |
| token | 247 |
| unità con virgolette dispari nel sorgente | 30 |
| non traducibili (NT) | 17 (15 `UI_LABEL` + 2 riferimenti di dato) |
| `CONVERSATION` | 0 |
| sha256[:16] `translation.json` | `b8bf47375f390542` |

## 5. Correzioni reali fatte durante il lotto

1. **455 e 599 non sono prosa.** `outfit/crystal pendant` (comando `scene`) e
   `thumbnail/hai pond strider` sono riferimenti di dato arrivati nel `source.json` come
   `MISSION_TEXT`. Aggiunti a `NT` con la motivazione scritta in `check.py`: restano identici.
2. **780 «Acorn Delights»** non poteva condividere la resa di 734/757/763 (`Acorns for Anoo`):
   sarebbe stato un duplicato non spiegato dal sorgente. Diventata «Delizie di Ghiande».
3. **675 `(Bail.)`** resa «(Tagliare la corda.)» con rapporto 2,625: riscritta «(Fuggi.)».
4. **Ventitré virgolette di troppo** rimosse su unità che il sorgente lascia aperte: le battute
   di questo file continuano nell'unità successiva, quindi non si chiudono.
5. **415** refuso «facendo di nuovo la avida» → «l'avida».
6. **68** «"Sono io."» portata a «"Sì, sono io."»: non era un FAIL, era una battuta monca.

## 6. Che cosa non è stato verificato

- **Nessun rendering nel gioco.** Lo staging non è stato caricato da Endless Sky: `check.py` e
  `verify.py` verificano testo, struttura e coerenza con il database, non l'aspetto a schermo.
  Vanno ancora controllate a mano le righe lunghe nelle schermate di dialogo.
- **Nessuna approvazione.** Le 823 unità restano `PENDING` nel database: lo staging non è
  approvazione, e nessun comando di questo lotto ha scritto su `state.db`.
- **Glossario locale.** «Slegati», «pietra chiave», «mondo ad anello», «porta-droni» sono scelte
  di questo lotto: non sono state riconciliate con eventuali occorrenze in altri file non ancora
  tradotti, e potrebbero richiedere un allineamento quando quei file verranno affrontati.

## 7. Effetto sullo staging

| | prima di L29 | dopo L29 |
|---|---|---|
| unità | 12.747 | **13.570** |
| parole EN | 407.807 | **431.733** |
| parole IT | 386.629 | **409.002** |
| residuo traducibile | 19.183 | **18.360** |
| directory con `translation.json` | 32 | **33** |
| file completi | 8 | **9** |

Database invariato: **APPROVED 364 · PENDING 32.560**, 32.924 unità, ultimo evento
`2026-10-17T14:33:18Z`, 630 `UI_LABEL` non traducibili.

## 8. Prossimo passo

L30 parte da un **file nuovo**: `hai missions.txt` non ha segmenti residui. Il prossimo file va
scelto misurando il residuo con `state.py` e la ricognizione dei file non ancora aperti, non a
memoria. Prima di aprire il lotto: `export_section.py`, poi `check.py` derivato con il proprio
`NT` misurato sul `source.json`.
