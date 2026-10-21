# REPORT — L297 (`data/coalition/coalition outfits.txt`, righe 26–187)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **22 controlli**; `verify.py` esce 0 con **23 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 15 (tutte `DESCRIPTION`) | 15 |
| parole | 461 | **487** (1,06) |
| tab | **3** | **3** |
| virgolette / segnaposto / alternative | 0 / 0 / 0 | **0 / 0 / 0** |
| apici | 1 | 9 |
| contesti | **12** | 12 |

Rapporto per unità **1,00 – 1,35**.

## 2. Le tre coppie con tabulazione

| contesto | prima scheda | seconda scheda |
|---|---|---|
| `outfit:Small Reactor Module` | 54 — «L'energia solare basta al commercio…» | **55** — `\t`«Un fascio di antiprotoni innesca la fusione…» |
| `outfit:Large Reactor Module` | 69 — «Ancora incapaci di replicare la tecnologia Quarg…» | **70** — `\t`«Questo reattore a fusione avanzato…» |
| `outfit:Small Cogeneration Module` | 84 — «I Kimek crearono in origine versioni molto più grandi…» | **85** — `\t`«Questo progetto compatto recupera…» |

Il **`\t`** è ciò che nel pannello del gioco produce il rientro della seconda metà della scheda. È verificato come **primo
carattere** in entrambe le lingue, e il test conta che siano **esattamente tre**.

## 3. Nove contesti con una sola unità

`Small Collector`, `Large Collector`, `Large Cogeneration`, `Small Battery`, `Large Battery`, `Small Shield`, `Large Shield`,
`Overcharged Shield`, `Small Repair`. Il test verifica l'**elenco esatto delle righe**, non solo il conteggio: una coppia
«inventata» (due unità dello stesso contesto non dichiarate) farebbe fallire la lista.

## 4. La citazione interna

L'unità 14 dice «Le aggiunte apportate al **Large Shield Module**…»: si riferisce al modulo dell'unità 13, che **non nomina se
stesso**. Il test verifica la relazione **sui contesti** (`at[156]['context'] == 'outfit:Large Shield Module'`), non la presenza
della stringa: un controllo «la stringa c'è» sarebbe passato anche con il riferimento sbagliato.

## 5. Registro e lessico

Nessuna seconda persona in tutto il lotto: sono **schede tecniche** in terza persona. Il lessico viene dal corpus: «marina
mercantile», «pannelli solari», «torri della fame» (le torri Kimek, già presenti altrove con le **virgolette**), «cella a
combustibile».

## 6. Verifica

```
check.py   22 controlli · FAIL totale: 0 · exit 0
verify.py  23 controlli · FAIL: 0 · exit 0
segmento   0 prima · 15 qui · 34 dopo la 187 · file 15/49 (30,6%)
```

**Un rosso al primo giro** (controllo mio): chiedevo che **anche l'unità 13** contenesse «Large Shield Module». Non è così — la 13
**descrive** il modulo, la 14 lo **cita**. Corretto il controllo in una relazione fra contesti.

## 7. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 15 unità `PENDING`; **nessuna revisione umana**.
- **Nessun testo visto nel gioco**: l'effetto della tab nel pannello è **dedotto** dalla struttura dei dati, non osservato.
- **Il file resta aperto**: 15/49; restano **34 unità**.
