# L19 — REPORT · `data/human/human missions.txt`, righe 1811–6428

**Data:** 2026-10-17 · **Directory:** `staging/editorial/L19_20261017_201414/`
**Esito:** `check.py` **FAIL totale 0** · `verify.py` **17/17 OK, exit 0** · `state.py` **exit 0** ·
`check_handoff.py` **0 FAIL / 30, exit 0** sull'handoff corrente (`HANDOFF_L20_20261017.md`)
**Stato delle unità:** tutte `PENDING` nel database. Il lotto vive **solo** in staging.

---

## 1. Blocco tradotto

| Voce | Valore misurato |
|---|---:|
| File | `data/human/human missions.txt` |
| Righe | **1811–6428** |
| Unità | **1.611** |
| Parole inglesi | **39.968** |
| Parole italiane | **37.324** |
| Rapporto | 0,93 · per unità 0,57–1,88 |
| Contesti | **70 missioni + 3 `event`** |
| Da / a | `mission:Courier 4` … `mission:Blind Man from Martini` |
| Tipi | `MISSION_TEXT` 1359 · `DESCRIPTION` 71 · `VALUE` 60 · `DIALOG` 59 · `LOGBOOK` 23 · `UI_LABEL` 39 |
| Tab (unità con tab iniziale) | 1.232 |
| Virgolette | 2.321 |
| Token `<...>` | 489 |
| Unità successive nel file | riga **6432**, `mission:Care Package to South 1` |
| Parole residue nel file | **51.158** (2.141 unità) |
| `translation.json` sha256[:16] | `a56041126bb484e8` |

**Deviazione dal target di 40.000 parole:** −32 parole (−0,08%), causata dal confine a fine missione
(riga 6484 avrebbe tagliato `Care Package to South 1`). Dettaglio in `review.md` §1 e §8.

---

## 2. Copertura dopo L19

| File | Prima | Dopo |
|---|---|---|
| `data/map planets.txt` | 1.544 / 1.544 (100%) | 1.544 / 1.544 (100%) |
| `data/human/human missions.txt` | 501 / 4.253 (11,8%) | **2.112 / 4.253 (49,7%)** |
| Totale staging | 2.045 unità · 97.056 EN | **3.656 unità · 137.024 EN · 133.360 IT** |
| Residuo traducibile | 29.885 unità | **28.274 unità** |

---

## 3. Esempi di resa

**Missione `Terraforming` (voce di Amy, §1):**
> EN — «It would cost fifteen million just to bring a specialist out for an initial consultation.»
> IT — «Solo per far venire uno specialista per una prima consulenza ci vorrebbero quindici milioni.»

**`Riley` (il congedo, unità 1289):**
> EN — «Whatever happens, please don't think ill of me. I will always love you.»
> IT — «Qualunque cosa succeda, per favore non pensare male di me. Ti amerò sempre.»

**`Blind Man from Martini` (unità 1587, il racconto di Douglas):**
> EN — «I remember that Pollux was especially bright and colorful that day, and the songbirds that inhabited the city were alive with sound.»
> IT — «Ricordo che Pollux era particolarmente luminoso e colorato quel giorno, e gli uccelli canterini che abitavano la città erano pieni di suoni.»

**Acrostico di `Dangerous Games 2` (unità 1106–1110), iniziali N-O-R-T-H conservate:**
```
Nessun'altra via ti è concessa
Oliate pelli guizzano e lampeggiano
Rasoi di spine sorgono dal profondo
Titaniche pareti schiacciano e frantumano
Hai da badare agli inizi, se vuoi vivere
```

---

## 4. Controlli

`check.py` (22 righe di controllo, tutte OK — `FAIL totale: 0`):

```
unità 1611/1611 · copertura 1611/1611 · vuote 0
label non traducibili: 39/39 identiche
duplicati italiani non spiegati: 0
tab 1236/1236 · tab iniziale 1232/1232 · virgolette 2321/2321 · token 489/489 · backtick 0/0
firma dello spazio: ok · spazi doppi: 0 · ratio 0,57–1,88
tipografia 0 · caratteri non latini 0 · inglese residuo 0
state.db 364/32560 · unità del lotto fuori da PENDING: 0
```

`verify.py` (indipendente, 17 controlli, exit 0): riga grezza identica al sorgente per tutte le 1.611 unità;
`english`/`kind`/`path` identici al DB; `state = PENDING`; id univoci e ordine uguale al sorgente; confine e
unità successiva verificati; 39 `label` identiche con kind `UI_LABEL`; nessuna riga multi-unità.

**Tre difetti trovati dai controlli, non dall'occhio:** la virgoletta in più dell'unità 61, i 17 duplicati
italiani su inglese diverso (unità elencate in `review.md` §5) e il rapporto 0,54 dell'unità 1572.

**Un difetto trovato da un controllo aggiunto in questa sessione:** un carattere cirillico omografo
(`а`, U+0430) infilato in «echeggiа» (unità 1102). Nessun controllo precedente lo vedeva: `check.py` ora
include la riga «caratteri non latini», e il difetto è corretto.

---

## 5. Integrità

```
state.db                                     OK
glossary.csv                                 OK
staging/inventory_fields.csv                 OK
tools/l10n.py                                OK
output/l10n-it/data/_ui/{interfaces,tooltips,help}.txt   OK
endless-sky HEAD                             b4aa3bac3 (modifiche: nessuna)
ESITO: OK
```

Nessuna scrittura in `state.db`, nei batch, nel glossario, nell'inventario o negli output approvati. Nessuna
patch applicata, nessuna build, nessun packaging, nessuna traduzione applicata al gioco.

**Unico strumento condiviso modificato:** `tools/check_handoff.py`, che aveva i valori attesi cablati sulla
transizione L18→L19 e falliva su un documento corretto (8 FAIL su 29, riprodotto). La correzione è
documentata in `review.md` §9, con tre prove di falsificabilità; la versione precedente resta come
`tools/check_handoff.py.bak_L19`. `state.py`, `export_section.py`, `next_section.py` e `protected.sha256`
sono invariati.

---

## 6. Cosa **non** è stato fatto

- **Nessuna verifica nel runtime.** Il gioco non è stato avviato: non è verificato come il motore presenti le
  39 `label`, gli acrostici, i testi con citazioni non chiuse, né il layout delle unità più lunghe.
- **Le 1.611 unità non sono approvate.** Sono `PENDING` nel database e restano in staging.
- **Nessuna ratifica delle decisioni aperte** (`Free Worlds` invariato, `Cavalcaladri`, `sottopodi`, `Core`
  invariato, `piastre di interferenza`): servono una decisione editoriale e, per alcune, i file delle navi.
- **Il bisticcio *beast/bee*** del secondo indovinello è perduto: non recuperabile senza riscrivere
  l'indovinello e la soluzione.
- **Nessuna delle 630 `label` del corpus** è stata classificata o tradotta (patch K4 non ratificata).

---

## 7. Prossimo passo

**L20**, misurato con `next_section.py`: righe **6432–10806**, **1.676 unità**, **40.112 parole**,
62 contesti da `Care Package to South 1` a `Stone to Hope`, confine successivo riga **10812**
(`Stone to Ice Queen`). Nessun `TEXT`, nessuna `phrase`, **71 `UI_LABEL`** da lasciare identiche
(più del doppio di L19).
