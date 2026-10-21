# REPORT — L286 (`data/gegno/gegno ships.txt`, righe 53–302)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **25 controlli**; `verify.py` esce 0 con **23 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 7 (tutte `DESCRIPTION`) | 7 |
| parole | 454 | **466** (1,03) |
| tab | 1 | 1 (unità 6) |
| virgolette | 0 | **0** |
| segnaposto / alternative | 0 / 0 | **0 / 0** |
| apici | 4 | 6 |
| parentesi tonde | 1 (unità 1) | 1 |

Rapporto per unità **1,01 – 1,11**: tutte sopra 1, come è normale per la prosa tecnica italiana, più lunga dell'inglese.

## 2. Asserzioni vuote, dichiarate

Questo è il primo lotto **senza virgolette, senza segnaposto e senza alternative**. Il metodo prevede che **l'assenza sia
verificata**, non saltata:

```python
sum(u['english'].count('"') for u in cov) == 0 == sum(u['italian'].count('"') for u in cov)
sum(len(TAG.findall(...))) == 0 == ...
sum(len(ALT.findall(...))) == 0 == ...
```

Se un giorno comparisse una virgoletta in più, il test la vede. Un controllo **assente** non è un controllo.

## 3. `Gypsum`: due unità, un testo

| riga | inizio | resa |
|---|---|---|
| 243 | `To fuel their increasing need for materials…` | «Per alimentare il loro crescente bisogno…» |
| 244 | `\tBecause Gegno engines are not very powerful…` | «\tPoiché i motori Gegno non sono molto potenti…» |

La seconda metà **non ricomincia**: continua. Il test verifica tre cose: stesso contesto, righe consecutive, e che la resa non
si apra con «Il Gypsum» ma con `Poiché`. È lo stesso schema dei frammenti di `phrase` (L271), ma qui il legame è **narrativo**
e non di concatenazione.

## 4. Il refuso

L'inglese dell'unità 7 scrive **`Gypusm's`** — un refuso, non un nome alternativo. In italiano la nave si chiama `Gypsum`,
quindi la resa usa **`Gypsum`** e il refuso **non si riproduce**. Verificato in due direzioni: `Gypusm` **assente**, `del Gypsum`
**presente**.

La regola generale, per non confondere i casi: **citazione non chiusa → si riproduce** (L257–L259); **refuso su nome proprio →
si neutralizza** (L286); **testo rotto che non si può correggere senza alterare la visibilità → si dichiara** (L281).

## 5. Terminologia

| inglese | resa | nota |
|---|---|---|
| `generation ships` | **navi generazionali** | |
| `hyperspace lanes` | **rotte dell'iperspazio** | |
| `Shuttle` | **Shuttle** | nome di modello, invariato |
| `cargo vessel` / `passenger liners` | **nave da carico** / **navi passeggeri** | |
| `bunks` | **cuccette** | lessico del corpus |
| `raw and refined ore` | **minerale grezzo e raffinato** | |
| `flying drill` | **trapano volante** | |
| `bridge` | **ponte di comando** | |
| `Excavator Drill` | **Excavator Drill** | equipaggiamento, invariato |
| `drill systems` | **sistemi di trivellazione** | |
| `the Vi and Scin factions` | **le fazioni Vi e Scin** | |

## 6. Verifica

```
check.py   25 controlli · FAIL totale: 0 · exit 0
verify.py  23 controlli · FAIL: 0 · exit 0
segmento   0 prima (apre il file) · 7 qui · 30 dopo la 302 · 6 contesti
```

**Primo giro verde**, senza correzioni: il contratto aveva già isolato le tre trappole (due unità del `Gypsum`, un solo tab,
asserzioni vuote) e la resa le ha rispettate.

## 7. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 7 unità `PENDING`.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Il file resta aperto**: 7/37; restano **30 unità** (29 `DESCRIPTION` + 1 `VALUE`).
