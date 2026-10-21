# review.md — L266 (`data/kahet/aberrant ships.txt`, righe 686–1007) — LOTTO TERMINALE

Registro delle decisioni editoriali dell'**ultimo lotto** delle navi Aberrant: cinque scafi, quattro schede «di serie» e una
scheda che racconta un **errore di crescita**.

## 1. Le cinque navi

| nave | unità | che cosa aggiunge |
|---|---|---|
| Aberrant Pike | 1 (coda) | `grown into a sleek, elongated shape` → «cresciuta fino a diventare una forma snella e allungata» |
| Aberrant Mole | 3–7 | `sharp, bladed prow capable of fitting more forward weapons` → «prua affilata a lama, capace di ospitare più armi frontali» |
| Aberrant Whiskers | 8–12 | `tail-like structure, increasing its agility` → «struttura a coda, che ne aumenta l'agilità» |
| Aberrant Trip | 13–17 | **difetto di germinazione** (vedi §3) |
| Aberrant Triplet | 18–22 | `composite of two or three individuals, fused together` → «composto di due o tre individui, fusi insieme in un'unica massa» |

La scheda di **Pike** è l'unica unità di questo lotto appartenente a una nave iniziata in L265: il confine del lotto cade
**dentro** una nave, non fra due navi.

## 2. La formula organo-metallica, quarta e quinta volta

La nota compare **4 volte** (Mole, Whiskers, Trip, Triplet) ed è **identica** alla resa di L265:

> «Sembra essere una sorta di entità organo-metallica, composta da uno strano mosaico di tessuto organico, materiale
> convenzionale e una materia esotica che sfugge all'analisi convenzionale.»

Il `check.py` la confronta con la resa **letta da `L265/translation.json`**, non con una costante scritta a mano: la fonte di
verità è il lotto precedente, e il test lo interroga.

## 3. La scheda anomala: Trip

> `Something appears to have gone terribly wrong in the germination of this variant. It is a lopsided, deformed mass of
> malformed material, which survives only through sheer luck.`
> «Qualcosa sembra essere andato terribilmente storto nella germinazione di questa variante. È una massa sbilenca e deforme
> di materiale malformato, che sopravvive solo grazie alla pura fortuna.»

Tutte le altre otto schede del file descrivono una variante **riuscita** (più armata, più veloce, più grande). Questa
descrive un **incidente**: un germoglio che è andato male e che vive per caso. La tentazione è di addolcirla («presenta
malformazioni»), ma il testo inglese è **esplicito e duro** (`terribly wrong`, `malformed`, `sheer luck`), e la resa lo è
altrettanto.

`germination` → **«germinazione»**: è la parola che il testo usa per il «germogliare» degli scafi-organismo, e la metafora
vegetale è coerente con il resto del file (forme che «crescono», «si allungano», «sviluppano code»).

## 4. Lessico

| inglese | resa | nota |
|---|---|---|
| `bladed prow` | **prua a lama** | `prow` = prua, non «muso» |
| `forward weapons` | **armi frontali** | |
| `tail-like` | **a coda** | |
| `agility` | **agilità** | |
| `composite` | **composto** | «fusione di più individui» |
| `fused together` | **fusi insieme** | |
| `single mass` | **un'unica massa** | |
| `sleek, elongated` | **snella e allungata** | |

## 5. Struttura

| cosa | inglese | italiano |
|---|---|---|
| tab | **0** | **0** |
| virgolette | **18** (9 designazioni) | **18**, mappa identica |
| apici | **0** | **6** (4 da `all'analisi`, più `l'agilità` e `un'unica`) |
| segnaposto | **0** | **0** |

I **quattro plurali** (`Moles`, `Whiskers`, `Trips`, `Triplets`) non hanno virgolette, come i nove di L265; nessuna sigla nuda
in questo lotto, e il test lo verifica in negativo.

## 6. Il file chiuso

`data/kahet/aberrant ships.txt`: **65 unità** in due lotti (L265–L266), **65 righe distinte**, dalla 16 alla 1007. Nove navi,
26 designazioni, 17 schede che sono **13 stringhe distinte** (la nota organo-metallica ripetuta 13 volte in tutto il file).

## 7. Cosa resta aperto (dichiarato)

- **Nessuna approvazione**: le 65 unità del file sono `PENDING`.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Anomalia `Ember Waste`**: «Distesa di Braci» 69 unità contro `Ember Waste` 16 su 85 — sanatoria solo con autorizzazione
  globale sui lotti chiusi.
- **Il resto della campagna**: 2.436 unità su 92 file.
