# REPORT — L67 · `data/human/culture conversations.txt` (righe 1062–1122)

**Esito: CHIUSO, e chiude il file a 374/374.** `check.py` `FAIL totale: 0`, `verify.py` exit 0.

## 1. Che cosa contiene il lotto

| Contesto | Unità | Scena |
|---|---|---|
| `Exotic Life: Delve` | 1–17 | I teredini di Delve: il diario (unità 1), il tecnico che decontamina un Sunder, la diagnosi, il sigillante, la battuta legale sul marchio |
| `Exotic Life: Ada` | 18–35 | La guardia dei Lovelace Labs e il pilota con dodici tonnellate di statuine in acciaio inossidabile |

## 2. Le scelte di traduzione che contano

**`shipworm`** → «teredine» (sing. «teredine», pl. «teredini»). È il nome zoologico italiano del mollusco
che buca il legno e le superfici sommerse: rende l'idea meglio di «verme di nave», che suona inventato.
Il toponimo resta: «teredini di Delve».

**Il `LOGBOOK`** (unità 1) è l'unico diario del file: «Heard about some tiny creatures called "Delvan
shipworms"…» → «Ho sentito parlare di piccole creature chiamate "teredini di Delve"…». Il testo è in prima
persona e la traduzione lo mantiene in prima persona.

**Il tecnico** parla da dipendente consapevole: «As a model Syndicate employee… I can tell you that the
rumors… are untrue» → «Come modello di dipendente del Sindacato… posso dirti che le voci… sono false».
L'ironia sta nella formula burocratica, non in un commento aggiunto.

**La guardia** ha il ritmo della noia professionale: «Not here you've not», «Rules are rules», e la domanda
spezzata «What. Are. They. Made of?» → «Di. Cosa. Sono. Fatte?». I punti sono nel sorgente e restano.

**Il pilota** cede con una frase fiacca: «Alright, alright. I'll get the decon procedure done. Okay? You
win.» → «Va bene, va bene. Farò la procedura di decon. Ok? Hai vinto.» La resa mantiene il «decon» breve.

## 3. Difficoltà

- **Il controllo `LOGBOOK` andava cambiato di segno.** Il `check.py` derivato da L66 asseriva «0 attese:
  assenza dichiarata»; con un diario nel lotto la riga era rossa pur essendo il testo tradotto. È stata
  resa positiva («1 attesa: controllo positivo») e affiancata dall'asserzione sulle forme `log`
  (backtick, tre argomenti, diretta). Decisione 221.
- **La trappola 192 si è ripresentata**: la prima patch inseriva `LOG = set([1])` lasciando in piedi un
  `LOG = set()` precedente, e Python usava l'ultimo. Risolto con un filtro **per riga** sul file, non con
  `str.replace`.
- **Nessun duplicato, nessuna virgoletta dispari**, 2 token dello stesso simbolo.

## 4. Verifica osservata

```
check.py   → 33 controlli · FAIL totale: 0
verify.py  → 38 controlli · exit 0
             unita 35 · righe 1062-1122 · 339 prima / 0 dopo · file 374 · max(line) 1122
             copertura del file 374/374 su L58-L67
             tipi 34 MISSION_TEXT + 1 LOGBOOK (unita 1, forma backtick)
             token 2 / 2 (<ship> x2) · tab 32 / 32 · virgolette 68 / 68 · dispari 0
             rapporto 0,81 - 1,38 · duplicati 0 gruppi
             parole 811 EN -> 787 IT
             sha256 translation.json ad997eaa9007d7c2…
```

## 5. Stato del progetto dopo L67

| Voce | Prima (L66) | Dopo L67 |
|---|---|---|
| File completi | 30 | **31** |
| Unità in staging | 24.168 | **24.203** |
| `culture conversations.txt` | 339/374 | **374/374 (100%)** |

`culture conversations.txt` è il **trentunesimo file completo** (10 lotti: L58–L67, 374 unità, 11.269 EN →
10.858 IT).

## 6. Prossimo passo

**L68** apre un file nuovo: `data/successors/successor 2 ghosts myurej.txt`, righe **16–113**, **49 unità**,
1 contesto (`Successors: Ghosts Myurej 1`), 1.502 parole, tab 42, virgolette 90, **1 `UI_LABEL`** (unità 20),
**2 `LOGBOOK`** (unità 23, 24), **13 token** in 5 famiglie (`<first>` 3, `<last>` 3, `<ship>` 2,
`<destination>` 1, `<planet>` 1). Confine: riga 118 apre `mission:Successors: Ghosts Myurej 2`.
