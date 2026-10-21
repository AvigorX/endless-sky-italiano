# review.md — L286 (`data/gegno/gegno ships.txt`, righe 53–302)

Registro delle decisioni editoriali del **primo lotto** delle navi **Gegno**: sette descrizioni tecniche, nessun dialogo.

## 1. Che cosa raccontano queste sette navi

I Gegno sono una fazione che ha **scoperto tardi** le rotte dell'iperspazio e si è trovata con **navi generazionali** enormi e
costose: la serie descritta è la loro **riconversione** — trasporto leggero, carico, estrazione.

| nave | riga | ruolo | dettaglio |
|---|---|---|---|
| `Shale` | 53 | trasporto leggero | «l'equivalente Gegno di una **Shuttle**» |
| `Dolomite` | 97 | carico più diffuso | grande «quasi come un incrociatore umano», ha dato origine alle varianti **Vi** e **Scin** |
| `Conglomerate` | 146 | trasporto di materiali | più facile da costruire delle navi generazionali, più grande delle navette |
| `Granofel` | 194 | solo carico | **senza cuccette** oltre l'equipaggio, va in coppia con una nave mineraria |
| `Gypsum` | 243–244 | estrazione | «un **trapano volante**», con l'**Excavator Drill** |
| `Corundum` | 302 | estrazione modulare | **due** sistemi di trivellazione regolabili |

## 2. Il registro: terza persona, presente, prosa tecnica

Nessun «tu», nessun dialogo, nessuna virgoletta. Le descrizioni sono **schede**: soggetto tecnico, funzione, storia del progetto.
La resa conserva questa **impersonalità**, ed è l'unica cosa che il test può controllare su un testo senza dialogo:

```python
not [u['idx'] for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])]
```

In un lotto di missioni lo stesso controllo sarebbe **sbagliato**: qui è necessario.

## 3. Le due metà del `Gypsum`

La 243 finisce con «facile da produrre»; la 244 comincia con «**Poiché** i motori Gegno non sono molto potenti…». Sono **un
solo testo** spezzato dal file:

- **non** si ripete il soggetto («Il Gypsum ha difficoltà…» è già implicito);
- **non** si ricomincia con un articolo dimostrativo («Questa nave…»), che suonerebbe come una seconda scheda;
- il **tab** iniziale della 244 resta: è il rientro della continuazione.

## 4. Il refuso `Gypusm's`

L'unità 7 scrive `the Gypusm's design` — una `m` di troppo. **Non è un nome alternativo**: è un refuso su un nome proprio che
altrove è scritto correttamente quattro volte. In italiano il nome resta `Gypsum` e il refuso **sparisce**: la resa dice «del
progetto del **Gypsum**».

Tre casi diversi, tre trattamenti diversi, e vale la pena tenerli distinti:

| caso | esempio | trattamento |
|---|---|---|
| citazione **non chiusa** nel sorgente | L257 u.12, L258 u.5, L259 u.2 | **si riproduce** |
| refuso su **nome proprio** | `Gypusm's` (L286 u.7) | **si neutralizza** con il nome corretto |
| testo **composto da frammenti** invisibili | `quarg news.txt` (L281) | **si dichiara** e non si ripara |

## 5. Scelte di resa

| inglese | resa |
|---|---|
| `too cumbersome to use for the purpose of interstellar commerce` | **troppo ingombranti per il commercio interstellare** |
| `the foundation of Gegno interstellar civilization` | **il fondamento della civiltà interstellare dei Gegno** |
| `its original design dating back to the early days of space colonization` | **con un progetto originale che risale ai primi tempi della colonizzazione spaziale** |
| `they lack bunks for anything beyond a proper crew` | **non hanno cuccette oltre a quelle per un equipaggio regolare** |
| `to extend the duration of a mining run` | **per prolungare la durata di un'uscita** |
| `not much more than a flying drill` | **non è molto più che un trapano volante** |
| `cost-efficient and easy to manufacture` | **economico e facile da produrre** |
| `shred asteroids in a matter of seconds` | **ridurre in pezzi un asteroide in pochi secondi** |
| `capable of mounting more advanced mining tools` | **capaci di montare strumenti minerari più avanzati** |

## 6. Struttura

| cosa | inglese | italiano |
|---|---|---|
| tab | **1** (unità 6) | **1**, primo carattere |
| virgolette | **0** | **0** |
| segnaposto | **0** | **0** |
| alternative | **0** | **0** |
| apici | **4** | **6** |
| parentesi tonde | **1** (unità 1) | **1** (`(e costose)`) |

## 7. Cosa resta aperto (dichiarato)

- **Nessuna approvazione**: 7 unità `PENDING`; **nessuna revisione umana**.
- **Il file è a 7/37**: L287 riparte dalla riga **303** con **9 unità**, **6 contesti** (`Corundum`, `Protolith`, `Dunite`,
  `Augen`, `Slate`, `Schist`), **466 parole**, **4 tab** e — di nuovo — **zero virgolette, zero alternative**. Tre nomi di
  nave nuovi e una coppia di unità consecutive (`Dunite` 417–418, `Augen` 553–554): **due** descrizioni spezzate, non una.
