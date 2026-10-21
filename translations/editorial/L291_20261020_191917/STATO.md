# STATO — L291 (`data/avgi/avgi culture conversations.txt`, righe 122–227)

**Stato: CHIUSO.** Secondo lotto del file: **dodici scene** con gli **atti dichiarati** degli Avgi. File a **20/46 (43,5%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L291_20261020_191917/` |
| righe | 122–227 |
| unità | **12**, tutte `MISSION_TEXT` |
| parole | **451 EN → 464 IT** (1,03) |
| rapporto | **0,96 – 1,21** |
| contesti | **8** — `Graffiti 1` ×2 · `We Live In A Society` · `Realism` · `Doomed Korath` · `General Ripper` ×2 · `Criminal Mischief` ×2 · `False Alarm` ×2 · `Fencing` |
| coppie consecutive | **3** — 182–183, 197–198, 212–213 (tab sulla **seconda**) |
| coppia non adiacente | **1** — il graffito 122+126 |
| tab | **3** (righe 183, 198, 213) |
| virgolette | **16**, per unità |
| segnaposto | **3** — `<planet>` |
| apici | **16 EN / 10 IT** |
| `check.py` | **26 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **23 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 8 prima · 12 qui · **26 dopo** la 227 |
| `sha256[:16]` | **`af1c7ffcd6ec5b6e`** |

## Comandi

```bash
python staging/editorial/L291_20261020_191917/check.py     # FAIL totale: 0 (26 controlli)
python staging/editorial/L291_20261020_191917/verify.py    # FAIL: 0 (23 controlli)
```

## Il tic linguistico degli Avgi

Ogni battuta comincia con l'**atto linguistico dichiarato**, ed è la forma già stabilita in `avgi news` («Rifiuto.»,
«Rabbia.», «Esasperazione.»):

| inglese | resa |
|---|---|
| `Unbelievable.` | **Incredibile.** |
| `Appreciation.` | **Apprezzamento.** |
| `Proclamation.` | **Proclama.** |
| `Declaration.` | **Dichiarazione.** |
| `Attention!` | **Attenzione!** |
| `Taunt!` | **Scherno!** |
| `Command.` | **Comando.** |
| `Abashment.` | **Imbarazzo.** |

Il test verifica **tutti e otto**: se uno solo sparisse dalla resa, la voce degli Avgi si sfalderebbe.

## Il gioco di parole che resta inglese

Nel graffito: `'Twilight Guard? More like Twilight Gourd.'` — un gioco **Guard/Gourd**. `Twilight Guard` è il nome della
fazione (40 occorrenze nel corpus, sempre in inglese): tradurlo in «Guardia del Crepuscolo» avrebbe **rinominato** una fazione
per salvare una battuta.

Scelta: **i nomi restano inglesi** e il gioco di parole resta **inglese**, dichiarato nel `REPORT` come limite: chi legge in
italiano non lo coglie. L'alternativa («Zucca del Crepuscolo») è stata scartata perché rompeva la coerenza con il corpus.

## La ladra

L'inglese dice `her`, `she`, `Stop, thief!` — la ladra è **femminile**, e la resa lo mantiene: «**Fermo, ladra!**», «Non mi
prenderete mai **viva**!», «la **ladra** grida», «la portano via in manette».

## Limiti dichiarati

Nessuna approvazione (12 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Restano **26 unità** (24
`MISSION_TEXT` + **2 `LOGBOOK`**).
