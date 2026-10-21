# L35 — revisione editoriale

Lotto `L35_20261018_120433` · `data/human/free worlds 1 start.txt` · righe 16–2343 · 663 unità ·
21.140 parole EN → 20.273 IT · `check.py` `FAIL totale: 0` · `verify.py` 27 controlli, exit 0.

Questo documento registra **le decisioni**, non i numeri: i numeri stanno in `REPORT.md` e sono
rigenerabili con i due comandi di verifica.

---

## 1. Che cosa copre il lotto

`free worlds 1 start.txt` è il secondo atto della campagna delle Free Worlds e, come i file di L32–L34,
**finisce con il lotto**: riga 16 è la prima unità, riga 2343 l'ultima. La copertura 663/663 è quindi un
invariante legittimo.

Il contenuto, in ordine: la liberazione di Kornephoros e il rilascio sulla parola dei prigionieri della
Marina; la nascita degli Oathkeepers; la diplomazia con il Sindacato (e la storia tra Alondo e Samuel
Remington); Tarazed e la CEO Emily Lane; Poisonwood, la Sparizione e gli Alphas; il sistema di allerta
precoce su Hope; la torretta al plasma di Barmy Edward; la scelta del Senato di negoziare con i pirati;
la disobbedienza di Tomek e l'invasione di Greenrock; il fallimento dei colloqui con Hines a Harmony;
l'udienza al Senato e la sospensione dal servizio; il discorso finale di Tomek in video.

È il lotto in cui la campagna **si spacca politicamente**: fino a L34 le Free Worlds erano un blocco
compatto contro la Repubblica; qui nasce la frattura fra Consiglio e Senato, e Tomek — che in L34 era il
mentore — diventa l'antagonista interno. La traduzione non ha ammorbidito nessuno dei due lati.

## 2. Ricognizione (misurata sul `source.json`, non dedotta)

```
MISSION_TEXT 550 · DESCRIPTION 33 · VALUE 32 · LOGBOOK 25 · DIALOG 22 · UI_LABEL 1
contesti 37 · tab 518 caratteri (500 unità con tab iniziale) · virgolette 1.346 · token 139
unità con parentesi quadre [a, b]: 0
unità con numero dispari di virgolette: 10
righe `log`: 25 → 25 unità LOGBOOK (1:1)
```

Due fatti che hanno richiesto preparazione e **non** si potevano copiare da L34:

- **`UI_LABEL` torna a 1** (in L34 era 0): è la `label` di salto `no casualties`, bersaglio di `goto`.
  Va in `NT`, identica. Copiare `NT = {}` da L34 avrebbe fatto tradurre la label e rotto il salto.
- **La lacuna `log` ha due forme nello stesso file**: 24 unità sono il testo del diario, una (547) è la
  **categoria** `People`. È il primo caso in cui le due forme convivono; la scelta è in §7.

## 3. Metodo

1. `export_section.py` su righe 16–2343 → 663 unità, 37 contesti.
2. Ricognizione dei tipi, della `UI_LABEL` sul `raw`, delle righe `log`, delle virgolette dispari.
3. `check.py` derivato da L34 con `NT = {513, 547}`, `TOKEN_EXC` vuoto, nessun controllo parentesi quadre
   (0 unità: asserito nel `verify.py`).
4. Traduzione in 10 parti a fine missione, ognuna chiusa con `check.py --range A B` verde.
5. `check.py` completo (duplicati, copertura, tipografia, token) e `verify.py` indipendente.

Le parti: 1–76, 77–135, 136–194, 195–271, 272–345, 346–409, 410–471, 472–544, 545–620, 621–663.

## 4. Le voci di questo file

Stessi personaggi di L34, ma in ruoli cambiati: la voce si mantiene, il tono no. Cinque registri.

**Tomek Voigt — da mentore a ribelle.** In L34 era asciutto e paterno («Sei ancora con noi in questa
battaglia?»). Qui passa dal comando al furore: urla in pubblico, insulta il Senato, definisce i senatori
«quei folli» e parla di «evirazione del nostro esercito». In italiano il registro si alza di violenza ma
resta militare: nessun insulto inventato, nessuna parola che il testo non ha. La frase chiave, unità 392
(«È stata la forza della NOSTRA milizia»), conserva la maiuscola enfatica come segno di voce che si
rompe, non come scelta tipografica casuale.

**JJ (Jean-Jacques Soleau).** È l'unico che tiene: parla piano, interrompe le liti, ricorda il processo
democratico. In italiano usa frasi brevi e verbi al presente; quando alza la voce (unità 401, «Tomek!
Basta così!») il contrasto funziona perché tutto il resto è sottovoce.

**Alondo Gruyere.** Il diplomatico: frasi lunghe, condizionali, precisazioni. Con Remington mostra una
crepa personale che il testo non spiega, e la traduzione non la spiega di più («abbiamo... un passato»).

**Freya Winters.** In L34 era la reclutatrice calorosa; qui è la logistica che fa i conti e non perdona.
La sua frase più dura (unità 448, «Sono molto delusa da voi. Da entrambi.») è resa senza aggiunte: la
brevità è la durezza.

**Barmy Edward.** Comico, veloce, sprezzante verso la burocrazia e la raffinatezza («Se cerchi la
bellezza, vai a comprarti uno di quei cannoncini mollaccioni che sfornano ai Lovelace Labs»). Il registro
è quello di un artigiano che si diverte, non di uno scienziato pazzo.

## 5. Il bivio di Greenrock

Le unità 410–471 contengono una scelta che cambia il rapporto con il Senato. Il testo offre due rami
(attaccare disobbedendo, o rinunciare e seguire gli ordini) e il gioco registra la scelta nei `LOGBOOK`.
La traduzione ha reso **entrambi i rami con lo stesso peso**: nessuna formula che faccia sembrare
"giusto" un ramo e "sbagliato" l'altro. In particolare:

- unità 413: «La Marina non è riuscita a conquistare Longjump. Perché mai una flotta di dimensioni simili
  dovrebbe riuscire a conquistare Greenrock?» — il dubbio resta un dubbio, non un avvertimento.
- unità 440: la scena in cui Freya spara al giocatore è un *game over* ironico («Devi aver beccato Freya
  in una giornata particolarmente storta. Riprova.»). In italiano il tono resta quello del gioco, non
  viene reso più cupo.

## 6. Decisioni lessicali

| inglese | italiano | perché |
|---|---|---|
| parole (dei prigionieri) | la parola (dare la parola) | istituto militare; «parola d'onore» è già nel testo alla riga 25 |
| Oathkeepers | Oathkeepers | nome del reggimento, invariato come le altre fazioni in L32–L34 |
| Conservatory | Conservatorio | istituzione nuova; tradotto perché il testo la descrive |
| CCOR | CCOR | sigla invariata; nome sciolto la prima volta: «Consigli Confederati del Bordo Esterno (CCOR)» — il nome inglese per esteso non poteva restare, contiene `the`/`of` |
| Plasma Turret | torretta al plasma | |
| Quad Blaster Turrets | torrette blaster quadruple | |
| Barmy Edward | Barmy Edward | soprannome; il `LOGBOOK` 234 ne spiega l'origine, e tradurlo («Edward il Pazzo») perderebbe il riferimento alla resina epossidica |
| don't call me "sir", I'm not wearing a suit | non chiamarmi "signore", non porto la cravatta | reso culturale: in italiano «abito» è ambiguo, «cravatta» rende l'idea di formalità |
| wussy guns | cannoncini mollaccioni | spregiativo, coerente con il personaggio |
| janitor, quartermaster, sitrep | inserviente, quartiermastro, rapporto | registro militare corrente |
| Star Barge, Falcon, Protector, Bastion, Boxwing | invariati | modelli di nave |

**I numeri**: «2,100 credits» → «2.100 crediti», «ten tons» → «dieci tonnellate». Separatore delle
migliaia italiano, come da convenzione.

## 7. La lacuna `log`: due forme nello stesso file

Misurato, non dedotto:

- **25 righe `log`** → **25 unità `LOGBOOK`** (1:1).
- **4 righe** hanno la forma `log "Categoria" "Nome" `testo`` (253, 254, 781, 1918): l'unità è il **testo**,
  categoria e nome restano in inglese.
- **1 riga** (unità 547) ha prodotto la **categoria** `People` invece del testo: è il caso che in L30
  riguardava tutto il file e che qui compare una volta sola.

La scelta su 547: **resta `People`, identica, e va in `NT`**. Motivo: le altre categorie dello stesso file
(`People`, `Factions`) non sono inventariate e quindi restano in inglese; tradurre solo questa
creerebbe due categorie diverse per la stessa cosa nel diario del giocatore. La scelta è scritta nella
docstring del `check.py` e nel `verify.py`, così chi riprende il lavoro non la riconsidera da capo.

Non è riparabile da questo lotto: `tools/l10n.py` e `state.db` sono protetti.

## 8. Cosa è stato corretto e perché

- **50 / 470**: `what do we do now` e `what do we do next` erano resi uguali; differenziati in «Allora,
  che cosa facciamo adesso?» e «E allora qual è il prossimo passo?». Il controllo dei duplicati scatta
  solo sul lotto completo.
- **197, 502, 626, 302**: battute brevissime sotto la banda comoda (0,48–0,69). Riscritte allungando
  senza aggiungere contenuto («(Certo, altroché!)», «(Entra pure.)», «E come facciamo a farlo?»,
  «E i sistemi pirata che stanno a nord di Men?»).
- **278**: titolo `Escort Supply Convoy` a 1,75, al limite alto della banda; accorciato in «Scorta
  rifornimenti».
- **355**: conteneva «shock and awe» non tradotto, e il controllo delle parole inglesi residue lo ha
  fermato; reso «un assalto di shock e terrore».
- **537**: refuso di stesura («Origlierai per ascoltarli») corretto in «(Metti l'orecchio alla porta.)».
- **Le dieci battute aperte** sono state riprodotte, non chiuse.

## 9. Controlli e limiti

`check.py` (21 controlli) verifica: copertura, unità vuote, `NT` identiche, duplicati italiano spiegati
dal sorgente, tab e virgolette per unità e come totale, token `<...>`, backtick, spazi, rapporto
lunghezze, tipografia, caratteri non latini, parole inglesi residue, stato del database. **Non** contiene
il controllo delle parentesi quadre (0 unità nel sorgente).

`verify.py` (27 controlli) **non riusa** la logica di `check.py`: ricostruisce tutto da `source.json`, dal
file sorgente e da `state.db` in sola lettura, e in più asserisce (a) che l'unica `UI_LABEL` sia la 513,
(b) che non ci siano parentesi quadre, (c) che le virgolette dispari siano esattamente quelle del
sorgente, (d) che le 10 parti ricostruiscano `translation.json`.

Limiti, dichiarati:

- **Il lotto non è nel gioco.** Nessuna approvazione nel database, nessun caricamento: 663 unità
  `PENDING`.
- **Nessuna verifica nell'editor.** In particolare i due monologhi di Tomek (unità 392 e 400) sono lunghi
  e non è verificato come vengano impaginati a schermo.
- **Il rapporto 0,71–1,67 non è un giudizio di qualità.**
