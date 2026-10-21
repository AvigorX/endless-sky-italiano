# REPORT — L105 · `quarg missions.txt` (chiude il file: la storia della Coalizione secondo i Quarg)

## 1. Contenuto

Un solo contesto, 61 unità, diviso in blocchi:

| blocco | unità | cosa succede |
|---|---|---|
| apertura | 1–8 | due domande d'apertura alternative (grado di Heliarch / Lunarium) con tre scelte identiche |
| l'incontro | 9–13 | Gohl: la veste bianca con le catene rosse, la cicatrice, l'occhio d'oro, la panca |
| la storia | 14–28 | la genesi delle tre specie, la guerra, la perdita degli anelli, la resa |
| la diramazione Heliarch | 29–35 | il copricapo, l'avvertimento, «le tue ragioni sono tue» |
| la diramazione Lunarium | 36–42 | l'«intervista», il rifiuto di combattere, «Non essere arrogante» |
| la casa | 43–55 | «Dov'è la tua casa?», sette risposte, quattro repliche di Gohl |
| il commiato | 56–61 | «Chi sei?», la scheda, i dodici Quarg corazzati, l'ultimo riflesso dell'occhio |

## 2. Scelte

| nodo | scelta | perché |
|---|---|---|
| `UI_LABEL` | **identiche** | etichette di salto (`heliarch 2`, `heliarch ask`…) |
| `LOGBOOK` | **tradotto per intero** | è la scheda di Gohl nel diario, non un'etichetta |
| `Gohl Salyi Memt-Wrik Laz` | **invariato** | nome proprio |
| `crack or a creak` | **scricchiolio o un cigolio** | |
| `out-of-tune cello` | **violoncello scordato** | |
| `the Saryds … the Kimek … the Arachi` | **i Saryd … i Kimek … gli Arach** | nomi di specie già fissati |
| `their two seniors` | **le altre due, più anziane** | «senior» qui è cronologico, non gerarchico |
| `maturity`-less | — | non ricorre in questo lotto |
| `jumped to conclusions` | **saltammo alle conclusioni** | |
| `defenders arose by the billions` | **A miliardi si levarono difensori** | |
| `ceasefire` | **cessate il fuoco** | |
| `headpiece` | **copricapo** | il dispositivo Heliarch |
| `safe passage` · `landing clearance` | **passaggio sicuro** · **permesso di atterrare** | |
| `interview` | **'intervista'** | fra apici come nel sorgente |
| `Dirt Belt` · `the Deep` · `Paradise Worlds` | **Dirt Belt** · **Deep** · **Paradise Worlds** | nomi di regione: invariati (come i nomi di sistema) |
| `Earth` | **Terra** | è il pianeta, non una regione |
| `my ship is my home` | **La mia nave è la mia casa** | |
| `materalized from the very walls` | **sembrati materializzarsi dalle pareti** | refuso del sorgente (`materalized`), reso corretto |
| `armor-clad` | **corazzati** | |

## 3. Difficoltà

1. **Tre tipi nello stesso lotto con tre regole diverse**: 56 `MISSION_TEXT` (tradotti), 4 `UI_LABEL` (identiche,
   asserite per indice), 1 `LOGBOOK` (tradotto e verificato come prosa). Un controllo unico per i tipi «non
   `MISSION_TEXT`» sbaglierebbe su uno dei due estremi.
2. **Sette token in cinque famiglie, due nuovi**: `<start planet>` e `<start system>` nell'unità 49. I nomi
   contengono uno **spazio**, quindi il riconoscitore `<[^<>]+>` è l'unico corretto.
3. **Una citazione aperta** (unità 26) su 61 unità: la risposta di Gohl continua dopo la domanda retorica.
4. **La voce di Gohl** è lunga e interrotta: le pause sono nel testo («Si ferma», «chiude l'occhio», «resta così
   per un minuto circa») e la resa le conserva invece di compattare i periodi.
5. **Cinque ripetizioni**, di cui una **tripla** (la domanda «Anche ora siete più avanzati di loro…», posta in tre
   rami diversi): resa identica da costante unica.
6. **Le sette risposte sulla casa** (44–51) sono scelte del giocatore e ognuna resta autonoma: nessuna costante
   condivisa, nessuna resa «economica».
7. **`New Boston`, `Midgard`, `Mainsail`, `Greenwater`** restano invariati; le **regioni** (`Dirt Belt`, `Deep`,
   `Paradise Worlds`) pure, perché il gioco le mostra con il nome inglese nelle mappe.

## 4. Numeri osservati

```
unita' 61/61 · 56 MISSION_TEXT + 4 UI_LABEL + 1 LOGBOOK · tab 54 · virgolette 99 = 99 (una aperta, unita 26)
token 7 = 7 in cinque famiglie · quadre 0 · cinque ripetizioni (una tripla)
parole EN 2155 -> IT 2073 · rapporto 0.73 - 1.32
righe 356/506 · file 178 unita · max(line) 506 · 117 prima / 0 dopo
FAIL totale: 0 (29 controlli) · verify exit 0 (31 controlli, invariante di file)
sha256[:16] 4ae2c9e490a62867 · file 178/178 · 4 lotti (48+42+27+61) · 5417 EN -> 5184 IT
```

## 5. Stato del progetto

```
TOTALE staging: 25469 unita · 816786 EN · 774313 IT
quarg missions.txt: 178/178 (100%) · 4 lotti · CHIUSO
file completi: 40 · residuo traducibile (formula state.py): 6461
residuo misurato: 7040 unità / 159269 parole su 126 file
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | quattro parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (29 controlli), `verify.py` exit **0** (31 controlli), file **178/178** |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 61 unità restano `PENDING`; il gioco non è stato caricato.
- **Il file è chiuso, la campagna no**: restano **7.040 unità / 159.269 parole** su **126 file**; il prossimo
  contratto è `HANDOFF_L106_20261018.md` (`korath missions.txt`, righe 1–120), dove compaiono **16 coppie di
  quadre** — la convenzione dei Wanderer, che elenca due rese possibili.
- **Nessuna revisione umana**.
