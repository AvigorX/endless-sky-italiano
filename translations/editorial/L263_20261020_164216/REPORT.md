# REPORT — L263 (`data/remnant/remnant jobs.txt`, righe 491–682)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **23 controlli**; `verify.py` esce 0 con **21 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 24 (13 `MISSION_TEXT`, 6 `DESCRIPTION`, 5 `VALUE`) | 24 |
| parole | 432 | **410** (0,95) |
| tab | **1** (unità 21) | **1**, primo carattere |
| virgolette | **2** (unità 20) | **2** |
| apici | **0** | 13 su 11 unità |
| segnaposto | 28 (<npc> 17, <destination> 6, <payment> 5) | 28, stesso ordine |

Rapporto **0,68 – 1,19**: il minimo è la battuta breve `You have returned, yet the <npc> has not.` → «Sei tornato, ma la
`<npc>` no.» (9 parole contro 13); il massimo è la `DESCRIPTION` di `Rescue 4` con la telemetria.

## 2. Traduzione manuale, nessun generatore

Le 24 rese sono state **scritte a mano** nel `parts/part01.json`, unità per unità, leggendo il sorgente; nessuno script ha
prodotto o riscritto testo. Le **8 unità ereditate** (3, 6, 7, 8, 12, 15, 16, 17) sono state **copiate carattere per
carattere** dal `translation.json` di L262, dopo averlo letto — non ricostruite a memoria — e il `check.py` lo riverifica
rileggendo quel file.

## 3. `<npc>` è una nave

Su 17 occorrenze l'accordo è sempre femminile: «la `<npc>`», «è **scomparsa**», «è stata **distrutta**», «risulta ancora
**dispersa**», «è **andata perduta** con tutto l'equipaggio», «**Trovala**», «**aiutala**», «il capitano **della** `<npc>`».
Due controlli indipendenti vietano le forme maschili.

## 4. Anomalia misurata: `Ember Waste`

| resa nel corpus | unità |
|---|---|
| **«Distesa di Braci»** | **69** |
| `Ember Waste` (invariato) | **16** |

Su **85** unità che contengono il nome. Il contratto del lotto prescrive l'invariato e il lotto lo rispetta (4 occorrenze,
`check.py` e `verify.py` verificano il conteggio), ma la **divergenza resta aperta**: sanarla significa toccare 69 unità di
lotti già chiusi, che questo ciclo non è autorizzato a fare. Il dato è registrato anche nel contratto di L264.

## 5. Il tab e le virgolette

Una sola unità è rientrata (**21**, «Poco dopo, il tuo comunicatore…») e una sola ha virgolette (**20**, la frase del
capitano: «Che le Braci ardano luminose per te.»). Tutte le altre `MISSION_TEXT` sono **prosa di diario** senza segni: il
lotto non introduce virgolette dove il sorgente non le ha.

## 6. Verifica

```
check.py   23 controlli · FAIL totale: 0 · exit 0
verify.py  21 controlli · FAIL: 0 · exit 0
segmento   54 prima · 24 qui · 9 dopo la 682 · copertura 78/87 (89,7%)
```

Tre rossi al primo giro, **tutti nel `check.py` e tutti per asserzioni mie sbagliate**, corrette dopo aver misurato:

| controllo | dichiarato | misurato |
|---|---|---|
| apici italiani | 12 su 10 unità | **13 su 11** (mancava l'unità 2, `un'assegnazione`) |
| `Graveyard` | assente dall'italiano | presente **una volta**, nel `VALUE` copiato (unità 18) |
| `Ember Waste` | 3 occorrenze | **4** (due «recupero tecnologico», due «rifornimento») |

Inoltre il contratto di L263 dichiarava **«33 dopo la 682»** in un punto (il metodo, §4 passo 6): le unità dopo la 682 sono
**9**, e 33 è il residuo del file dopo L262. La discrepanza è stata corretta nel `check.py` e dichiarata qui: **vince il
workspace**.

## 7. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 24 unità `PENDING`.
- **Nessun testo visto nel gioco**.
- **Nessuna revisione umana**.
- **Il file resta aperto**: 78/87; restano 9 unità (`Rescue 5` coda e `Disable 1`).
