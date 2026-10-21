# L18 — `data/human/human missions.txt` 985–1806

**Data:** 2026-10-17 · **Esito: lotto completo, 187/187 unità, 0 omissioni · FAIL totale: 0**
**Directory:** `endless-sky-l10n/staging/editorial/L18_20261017_200248/`

---

## 1. Blocco tradotto

| Voce | Valore |
|---|---|
| File | `data/human/human missions.txt` |
| Intervallo | righe **985–1806** |
| Unità | **187** (`PENDING`) |
| Parole | **4.255** inglesi → **4.050** italiane |
| Rapporto | 0,65 – 1,86 |
| Missioni | **17** (`There Might Be Riots` 2, 3A, 3B · `Drug Running` 1–3 · `Hallucination` · `Shady passenger transport` 1, 2, 3, 3 double cross, 3 double cross big payment · `Rescue Miners` 1–2 · `Courier` 1–3) |
| Blocchi `phrase` | **1** (`generic human package offer`, 27 frammenti) |
| Tab | 81 |
| Virgolette | 191 |
| Token `<...>` | 109 |

Progresso del file: **501 unità su 4.253** (11,8%). Restano 3.752 unità / 91.126 parole dopo la riga 1806.

---

## 2. Classificazione delle 27 `TEXT` e delle 3 `UI_LABEL`

### 3 `UI_LABEL` → **non traducibili**

`label "shoot and die"` (124), `label "more money"` (131), `label "shoot and live"` (137): bersagli di
`goto` nella sequenza della missione *double cross*. Lasciate identiche, elencate in `check.py`.

### 27 `TEXT` → **traducibili, con vincoli di formato**

Sono le opzioni di **11 slot** della `phrase "generic human package offer"`, che il motore concatena per
costruire l'offerta. 25 tradotte, **2 identiche** perché sono pura punteggiatura (` "` all'idx 164, `"` all'idx
180).

| Slot | Unità | Nota |
|---|---|---|
| soggetto (5) | 154–158 | tradotto |
| spazio | — | ` `: non è un'unità del database |
| verbo (5) | 159–163 | terza persona, **senza participi concordati** |
| virgoletta ` "` | 164 | identico |
| saluto (4) | 165–168 | **tutti chiusi con il punto** |
| spazio | — | ` ` |
| frase (4) | 169–172 | iniziano con la maiuscola |
| spazio | — | ` ` |
| domanda (4) | 173–176 | — |
| pagamento (3) | 177–179 | **spazio iniziale conservato** |
| virgoletta `"` | 180 | identico |

**Frase composta** (prima opzione di ogni slot, misurata da `check.py`):

```
Uno del posto spunta dal nulla e chiede, "Capitano. Ho un pacchetto che deve arrivare su <planet> entro
<day>. Riesce a portarlo per me? Le darò <payment> per il disturbo."
```

Due scelte sono imposte dalla concatenazione, non dal gusto:

1. tutti i **saluti finiscono con il punto** (165 `Captain,` → "Capitano.", 167 `Sorry to interrupt, but` →
   "Scusi se la disturbo."), perché lo slot successivo inizia con la maiuscola;
2. i **verbi non hanno participi concordati** ("spunta", "ti si avvicina e dice"), perché il soggetto può
   essere maschile o femminile.

---

## 3. Esempi rappresentativi

**Unità 14 — il concerto-protesta**

> A second after you realize that the whole thing is a thinly veiled critique of the Syndicate, a group up
> front unrolls a banner that reads "End Wage Slavery!"...

> Un secondo dopo aver capito che il tutto è una critica appena velata al Sindacato, un gruppo in prima fila
> srotola uno striscione che recita "Fine della schiavitù salariale!"...

**Unità 70 — la voce nella stella nuvolosa**

> "And the voice told me he was sad. Sad, because that part of space used to be the home of another species,
> and now they're all dead. He said we humans built our cities on the graveyards of a great civilization and
> didn't even know it."

> "E la voce mi disse che era triste. Triste, perché quella parte di spazio era un tempo la casa di un'altra
> specie, e ora sono tutti morti. Disse che noi umani abbiamo costruito le nostre città sui cimiteri di una
> grande civiltà, e non lo sapevamo nemmeno."

**Unità 119–120 — il doppio gioco**

> But something feels wrong... You whirl around in your seat and come face-to-face with the entire gang.
> They're all armed. And their weapons are pointing at you. Your heart sinks.

> Ma qualcosa non va... Ti giri di scatto sulla poltrona e ti trovi faccia a faccia con l'intera banda. Sono
> tutti armati. E le loro armi sono puntate su di te. Il cuore ti sprofonda.

---

## 4. Controlli

| Controllo | Esito |
|---|---|
| Indici: 187 attesi, 187 presenti | OK |
| ID univoci, allineati a `source.json` | OK |
| `raw` identica alla riga del file (187/187) | OK |
| `english`/`kind`/`path` identici al DB · `state = PENDING` | 187/187 · 187/187 |
| Traduzioni vuote | 0 |
| Duplicati italiano | 0 |
| Duplicati inglese | **16** gruppi, tutti ripetizioni del sorgente (nomi di missione, testi identici, opzioni identiche) |
| Non traducibili lasciate identiche | 5/5 (3 `label` + 2 frammenti di punteggiatura) |
| Tab / virgolette / token / backtick | 81/81 · 191/191 · 109/109 · 0/0 |
| Firma dello spazio iniziale/finale | identica al sorgente, unità per unità |
| Rapporto di lunghezza | 0,65 – 1,86 |
| Tipografia | 0 accenti sostitutivi, 0 ellissi tipografiche, 0 caporali, 0 em dash, 0 apostrofi curvi |
| Parole inglesi residue | 0 (titoli di band/album/canzone esclusi: `TITLES`) |
| Anglicismi evitabili | 0 |
| `phrase`: 11 slot individuati | OK |
| `phrase`: composizione EN e IT pulita (spazi, punteggiatura, virgolette, maiuscole) | OK |
| Frammenti `TEXT` dentro il blocco `phrase` · opzioni non vuote 27 = unità 27 | OK |

Errori miei trovati e corretti: duplicato italiano 5/32, rapporto 3,00 sull'unità 154, rapporto 2,38
sull'unità 165, e cinque difetti di lingua in rilettura (§3 di `review.md`).

---

## 5. Integrità

| Voce | Atteso | Osservato | Esito |
|---|---|---|---|
| `endless-sky` HEAD / modifiche | `b4aa3bac3` / 0 | identico / 0 | OK |
| `state.db` | 364 / 32.560, nessuna scrittura | 364 / 32.560, `9125282973ddc8b9`, ultimo evento `14:33:18Z` | OK |
| Batch · glossario · inventario · `tools/l10n.py` · output approvati | invariati | hash invariati | OK |
| L1–L17 | intatti | hash invariati | OK |
| Patch K4 · build · test di gioco · packaging | non eseguiti | non eseguiti | OK |

---

## 6. Artefatti

```
endless-sky-l10n/staging/editorial/L18_20261017_200248/
├── source.json       187 unità (idx, id, riga, tipo, contesto, inglese, delimitatore, tab, riga grezza, hash)
├── translation.json   187 unità (…, italiano, ratio) — `kind` conservato
├── review.md          ricognizione e classificazione, convenzioni, interventi, decisioni aperte
├── REPORT.md          questo report
├── parts/             part01 (1–31), part02 (32–62), part03 (63–93), part04 (94–124),
│                      part05 (125–153), part06 (154–187)
└── check.py, verify.py
```

`check.py` di questo lotto introduce due controlli nuovi, entrambi dichiarati: **firma dello spazio** invece
del divieto assoluto di spazio iniziale, e **composizione della `phrase`** verificata in inglese e in italiano.

---

## 7. Cosa non è stato fatto

- Nessuna applicazione al gioco, nessun batch, nessuna build, nessun packaging.
- Nessuna modifica a `state.db`, glossario, inventario, output approvati, sorgenti o dati.
- **Rendering non verificato** (nessun avvio del gioco, come da mandato). In particolare non è osservato come
  il motore sceglie e concatena le opzioni della `phrase`: la verifica è sui dati, non sul runtime.
- Le 187 unità sono **tradotte in staging e restano `PENDING`** nel database.

**Totale editoriale complessivo: 2.045 unità · 97.056 parole inglesi → 96.036 italiane.**
