# review.md — L265 (`data/kahet/aberrant ships.txt`, righe 16–685)

Registro delle decisioni editoriali del **primo lotto** delle navi **Aberrant**: nove scafi-organismo, ognuno con una
designazione, un plurale e due schede.

## 1. Che cosa si copia e che cosa si traduce

| tipo | unità | trattamento |
|---|---|---|
| `VALUE` | **26** | **copiato** — sono designazioni e nomi di modello |
| `DESCRIPTION` | **17** | **tradotto** — sono le schede |

Le designazioni sono **codici militari**: `K-IA "Latte"`, `K-IIA "Junior"`, `K-IIC "Pike"`. Si copiano **con le virgolette**,
perché il codice e il soprannome sono un'unica etichetta; il plurale (`Lattes`, `Juniors`) è il nome della classe e resta
inglese.

**Irregolarità conservata**: la designazione `K-IC Pileup` è **senza virgolette** nel sorgente, mentre tutte le altre le
hanno. Non è stata «normalizzata»: il testo del gioco è quello.

## 2. La nota organo-metallica (9 volte)

> `This appears to be some kind of organo-metallic entity, made from a strange mosaic of organic tissue, conventional
> material, and an exotic matter that defies conventional analysis.`
> «Sembra essere una sorta di entità organo-metallica, composta da uno strano mosaico di tessuto organico, materiale
> convenzionale e una materia esotica che sfugge all'analisi convenzionale.»

Una sola resa per nove scafi. La formula descrive **che cosa sono** gli Aberrant: un mosaico di tessuto vivo, materiale
ordinario e materia esotica. «Entità» e non «creatura»: il testo le chiama *entity*, e la parola italiana tiene
l'ambiguità fra organismo e costruzione.

## 3. Le otto varianti

| inglese | resa | che cosa aggiunge |
|---|---|---|
| `as close to the baseline as can be expected` | «quanto più vicina al modello di base ci si possa aspettare» | è lo scafo «normale» |
| `much more heavily armed than most others of its kind` | «molto più armata della maggior parte delle altre della sua specie» | potenza di fuoco |
| `somewhat larger and sturdier than others` | «un po' più grande e più robusta delle altre» | mole |
| `lighter and capable of higher speeds … yet it still carries an enlarged armament` | «più leggera e capace di velocità superiori … eppure porta comunque un armamento maggiorato» | velocità **con** le armi |
| `grown extra thrusters around a lean, sleek fuselage` | «aver sviluppato propulsori supplementari attorno a una fusoliera snella e affusolata» | propulsione |
| `hardpoints designed to mount turrets` | «punti di attacco progettati per montare torrette» | torrette |
| `compact, smaller-than-average, and still in the process of growing` | «compatta, più piccola della media e ancora in fase di crescita» | esemplare giovane |
| `growing more elongated, and has a tougher hull` | «in fase di allungamento e ha uno scafo più resistente» | crescita |

Le formule sono **parallele** («Questa variante in particolare sembra…»), tranne due che usano `appears` invece di `seems`:
la resa le distingue appena («sembra avere» invece di «sembra essere»), senza appiattirle.

## 4. `Aberrant` resta inglese

Come `Ka'het` — che il corpus lascia invariato in **107** unità di `kahet missions.txt` — la parola `Aberrant` è il **nome
della classe di navi**: si scrive «navi Aberrant», non «navi aberranti». Le schede la contengono una volta sola (unità 19) e
il `check.py` verifica che non compaia invece nei `VALUE`, dove sarebbe un errore di copia.

## 5. Lessico delle navi

| inglese | resa | nota |
|---|---|---|
| `hardpoint` | **punto di attacco** | forma già usata nel corpus («punti di attacco esterni») |
| `turret` | **torretta** | termine fissato |
| `fuselage` | **fusoliera** | |
| `hull` | **scafo** | |
| `armament` | **armamento** | |
| `thrusters` | **propulsori** | |
| `exotic matter` | **materia esotica** | |
| `organo-metallic` | **organo-metallico** | nuovo nel corpus, dichiarato qui |

## 6. Struttura

| cosa | inglese | italiano |
|---|---|---|
| tab | **0** | **0** |
| virgolette | **32** (16 designazioni) | **32**, per unità identiche |
| apici | **0** | **10** (`all'analisi`, `un po'`, `della maggior parte`… no: sono 9 note + 1 variante) |
| segnaposto | **0** | **0** |

Gli apici italiani nascono tutti da **elisioni della formula** (`all'analisi`) e da **`un po'`** nella variante più grande:
la nota compare 9 volte, quindi 9 apici più 1.

## 7. Cosa resta aperto (dichiarato)

- **Nessuna approvazione**: 43 unità `PENDING`.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Il file è a 43/65**: L266 chiude le ultime 22 unità (Pike, Mole, Whiskers, Trip, Triplet) ed è **terminale**.
