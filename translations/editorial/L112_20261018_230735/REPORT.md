# REPORT — L112 · `_ui/tooltips.txt` (120 unità: scafo, messa fuori uso, scudi)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| scafo e riparazione | 1–8, 21–26 | 331–406 | calore e carburante della riparazione, ritardo, soglia di messa fuori uso, protezione, moltiplicatori |
| nave messa fuori uso | 9–20 | 355–388 | tempo, energia, carburante, calore e **otto tipi di danno** dell'autoriparazione |
| equipaggiamento come merce | 27–28, 52, 60–61, 99 | 409–415, 484, 511–514, 625 | multa, reddito, manutenzione, costi operativi, valore di vendita |
| inerzia e massa | 29, 54–55 | 415–418, 490–493 | riduzione dell'inerzia, massa senza carico |
| scansioni | 62–66, 96 | 514–526, 616 | equipaggiamenti, portata, velocità, efficienza, opacità, interferenza |
| spazio | 67–69 | 529–535 | spazio generico, occupato, libero |
| surriscaldamento | 70–71 | 538–541 | danni al secondo, soglia |
| missili guidati | 72–73, 77 | 544–550, 559 | disturbo ottico, dimensione ottica, disturbo radar |
| perforazione | 74–76 | 550–556 | percentuale, protezione, resistenza |
| rifornimento e salto | 41–46, 78, 97 | 460–481, 562, 619 | ramscoop, iperguida, motore di salto, portata, costo di massa |
| equipaggio | 79–81 | 565–571 | cuccette, equipaggio richiesto, obbligatorio |
| spinta inversa | 82–95 | 574–613 | spinta, energia, calore, sei tipi di danno accumulato |
| autodistruzione | 98 | 622 | probabilità in abbordaggio |
| scudi | 100–120 | 628–688 | ricarica (energia, carburante, calore, ritardo, moltiplicatori), rigenerazione, permeabilità, robustezza, ritardo |

## 2. Scelte

| nodo | scelta | perché |
|---|---|---|
| `hull strength` | **robustezza dello scafo** | già approvato in L111 unità 97 |
| `disabled` (ship) | **messa fuori uso** | approvato in L111 unità 97–98; non «distrutta» |
| `repair delay period` | **periodo di ritardo della riparazione** | L111 unità 100 |
| `hull threshold` · `absolute threshold` | **soglia di messa fuori uso** · **soglia assoluta** | |
| `illegal` | **illegale** («puoi essere multato») | |
| `income` · `operating income` | **reddito** · **reddito operativo** | |
| `maintenance costs` · `operating costs` | **costi di manutenzione** · **costi operativi** | |
| `depreciate` · `plunder` | **si deprezzano** · **bottino** | |
| `inertia reduction` | **riduzione dell'inerzia** | |
| `mass with no cargo` | **massa senza carico** | |
| `turn rate` | **velocità di virata** | |
| `max speed` · `w/ afterburner` | **velocità massima** · **con postbruciatore** | |
| `jump drive` · `jump range` · `jump mass cost` | **motore di salto** · **portata del salto** · **costo di massa del salto** | iperguida resta per *hyperdrive* |
| `ramscoop` | **ramscoop** invariato | glossario |
| `stellar wind` | **vento stellare** | |
| `outfit space` · `general-purpose space` | **spazio equipaggiamenti** · **spazio generico** | |
| `ion` · `scramble` · `disruption` · `slowing` · `discharge` · `corrosion` · `leak` · `burning` · `piercing` | **ionizzazione · disturbo · disruzione · interferenza sui motori · scarica · corrosione · perdita di carburante · ustione · perforazione** | nove famiglie, una resa ciascuna |
| `optical jamming` · `radar jamming` | **disturbo ottico** · **disturbo radar** | |
| `optical size` | **dimensione ottica** | |
| `piercing weapons` | **armi perforanti** | |
| `mandatory crew` | **equipaggio obbligatorio** | |
| `reverse thrust` | **spinta inversa** | |
| `scram drive` | **motore scram** | |
| `self destruct` | **autodistruzione** | |
| `shield permeability` | **permeabilità degli scudi** | |
| `shields (charge)` | **robustezza totale degli scudi e velocità di rigenerazione** | |
| `shield generation` | **rigenerazione degli scudi** | |
| `depleted` | **esauriti** | |

## 3. Difficoltà

1. **Otto varianti dello stesso stampo** (unità 13–20): la frase è identica e cambia solo il tipo di danno. Una resa
   diversa in una sola unità romperebbe la simmetria visibile in sequenza; il `check.py` verifica che tutte
   contengano «quando una nave messa fuori uso si ripara da sola».
2. **Lo stesso stampo torna nella spinta inversa** (unità 88–95, con «accumulata/o» al posto di «applicata/o»): le
   due famiglie vanno tenute distinte, e lo sono per costruzione del testo.
3. **`the more … the greater … the greater …`** (unità 72, 77): tre comparativi consecutivi in una frase lunga.
   Reso con «Più … è installato, maggiore è la distanza … e maggiore la probabilità …», senza perdere la terza
   proposizione.
4. **`thermal`-family**: qui non ricorre, ma i tooltip usano `heat` per due cose diverse — il calore prodotto e il
   **danno** da calore. La distinzione è esplicita («danni da calore») solo dove serve.
5. **`A value of one has the same influence … as one more ton`**: valore **1** come unità di misura, non «uno» come
   numero. Reso «Un valore di uno ha lo stesso effetto … di una tonnellata in più», come nel blocco approvato.
6. **`w/` abbreviato nel contesto** (`tip:    w/ afterburner:` ha anche **quattro spazi** dopo i due punti): il
   contesto non si tocca e non entra in traduzione; l'inglese dell'unità è invece una frase intera.
7. **Zero virgolette, zero token**: asseriti vuoti, non omessi. In L111 le virgolette erano 14 e i tab 0: un
   controllo copiato avrebbe reso rosso questo lotto.
8. **Il registro**: 120 unità nuove accanto a 52 approvate negli stessi pannelli; il `check.py` verifica l'assenza
   di «voi» e la presenza di 12 termini chiave.

## 4. Numeri osservati

```
unita' 120/120 · TUTORIAL_TIP 120 · tutte PENDING (misurato prima di scrivere)
contesti 120, tutti distinti · tab 0 · virgolette 0 · token 0 · quadre 0 · ripetizioni 0
parole EN 1813 -> IT 2044 (1.127) · rapporto per unita 0.89 - 1.62, media 1.21
righe 331/688 · file 667 unita · max(line) 1865 · 104 prima / 443 dopo
FAIL totale: 0 (29 controlli) · verify exit 0 (33 controlli)
sha256[:16] 3ff21c44bf59b9fc · copertura file 224/667 (33,6%)
```

## 5. Stato del progetto

```
TOTALE staging: 25851 unita · 825677 EN · 783308 IT
tooltips.txt: 224/667 (33,6%) · 2 lotti
file completi: quarantuno · residuo traducibile (formula state.py): 6079
residuo misurato: 6710 unità / 151305 parole su 125 file
avanzamento: 25851/32924 unità (78,5%) · 825677/979975 parole (84,3%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 4 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (29 controlli), `verify.py` exit **0** (33 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 120 unità restano `PENDING`; il gioco non è stato caricato e **nessun tooltip è stato
  visto nel pannello**.
- **Il file non è completo**: **443 unità** residue; prossimo contratto `HANDOFF_L113_20261018.md` (righe 691–973,
  **96 unità**, **87 contesti**, **22 virgolette**).
- **Nessuna revisione umana**.
