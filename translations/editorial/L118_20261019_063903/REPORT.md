# REPORT — L118 · `pirate jobs.txt` (schiavi, scorte, eliminazioni, razzie)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| criminale galattico (Core, Sud) | 1–8 | 1627–1815 | gli stessi testi di L117, ripresi dalla memoria |
| trasporto di schiavi | 9–18 | 1820–1924 | cinque missioni in celle sicure, con la pena di morte come avvertimento |
| mercenari e scorte | 19–36 | 1994–2469 | protezione, scorta di carico illegale, scorta di nave rubata, tre regioni |
| eliminare le forze dell'ordine | 37–60 | 2469–2654 | Marina, Sindacato, milizia, due taglie ciascuna |
| eliminare la concorrenza | 61–96 | 2654–2890 | bande rivali e predoni, cinque varianti |
| razzie ai mercanti | 97–104 | 2890–2955 | Repubblica e Sindacato, con la quota del bottino |

## 2. Scelte

| nodo | scelta | perché |
|---|---|---|
| `Transfer slaves to <planet>` | **identico** (`VALUE`) | nome di missione |
| `slaves in secure cells` | **schiavi in celle sicure** | |
| `local warlord` | **signore della guerra locale** | |
| `Slavery is punishable by death` | **La schiavitù è punita con la morte** | |
| `protection` · `protect cargo` · `protect ship` | **protezione** · **proteggere il carico** · **proteggere la nave** | nei nomi restano inglesi |
| `help them escape local law enforcement` | **aiutarla a sfuggire alle forze dell'ordine locali** | il capitano è la nave |
| `law-enforced space` | **spazio controllato dalle forze dell'ordine** | |
| `by <date>` | **entro `<date>`** | senza articolo: il token può essere una data o un intervallo |
| `by <day>` | **entro `<day>`** | idem |
| `Navy` · `Syndicate` · `militia` | **Marina** · **Sindacato** · **milizia** | `Marauders` resta inglese nei nomi |
| `rival gang` · `marauder gang` | **banda rivale** · **banda di predoni** | |
| `the ruling Marauder gang` | **la banda di predoni che lo governa** | |
| `bounty payment` | **compenso** | |
| `cut of the loot` | **una parte del bottino** | |
| `gratefully pay you <payment>` | **ti pagano con gratitudine `<payment>`** | formula ripetuta 8 volte |
| `destroying them` (flotta mercantile) | **distruggerla** | concordanza con «flotta» |

## 3. Difficoltà

1. **La forma cambia dentro lo stesso file**: 36 `DIALOG` contro 5, 2 `MISSION_TEXT` contro 31, nove famiglie di
   token contro sei. Il `check.py` è stato riscritto sul `Counter(kind)` misurato.
2. **Zero virgolette**: il controllo è stato scritto come **asserzione vuota** (`0 = 0`); omettere il caso
   avrebbe lasciato passare in silenzio un cambio di inventario.
3. **Un errore di numero, corretto**: l'handoff dichiarava «181 dopo la riga 2955», che è il residuo **dopo
   1624**, non dopo 2955. Il `verify.py` ha misurato **77** (279 − 98 − 104) e ha fatto fallire il lotto; il
   numero è stato corretto **nel documento** (handoff e due checkpoint), non nell'asserzione.
4. **`<date>` e `<day>`**: i token portano già il numero, quindi la frase usa «entro `<date>`» senza articolo;
   un «entro il `<date>`» avrebbe potuto produrre «entro il 3 giorni».
5. **I nomi contengono token** (`Merchants near <system>`): restano identici e il token resta protetto.
6. **Tre testi ripresi da L117**: la resa è stata letta dal `translation.json` del lotto precedente e verificata
   identica su 8 unità — un controllo che nessun conteggio strutturale sostituisce.
7. **Gate**: minimo 0,88 (unità 39, `The fleet has been eliminated…`), massimo 1,27 (unità 96), media 1,04.

## 4. Numeri osservati

```
unita' 104/104 · DIALOG 36 · VALUE 33 · DESCRIPTION 33 · MISSION_TEXT 2 · tutte PENDING
contesti 33 (19 da quattro, 14 da due) · testi distinti 39 (11 nomi + 28 prosa, 3 da L117)
tab 0 · virgolette 0 (asserito) · token 192 in 9 famiglie · quadre 0 · backtick 0
parole EN 1753 -> IT 1774 (1.012) · rapporto 0.88 - 1.27, media 1.04
righe 1627/2955 · file 279 unita · max(line) 3706 · 98 prima / 77 dopo
FAIL totale: 0 (28 controlli) · verify exit 0 (38 controlli)
sha256[:16] 31bb9438bee96230 · copertura file 202/279 (72,4%)
```

## 5. Stato del progetto

```
TOTALE staging: 26496 unita · 837695 EN · 795400 IT
pirate jobs.txt: 202/279 (72.4%) · 2 lotti · 3557 EN -> 3489 IT
file completi: quarantadue · residuo traducibile (formula state.py): 5434
residuo misurato: 6065 unità / 139287 parole su 124 file
avanzamento: 26496/32924 unità (80,5%) · 837695/979975 parole (85,5%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 4 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (28 controlli), `verify.py` exit **0** (38 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 104 unità restano `PENDING`; nessuna missione è stata caricata nel gioco.
- **Il file non è completo**: **77 unità** residue (righe 2958–3706), un solo segmento: il prossimo lotto lo
  chiude (`HANDOFF_L119_20261019.md`, 77 unità, 1.223 parole, 20 contesti, 12 `CONVERSATION`, 9 tab).
- **Nessuna revisione umana**.
