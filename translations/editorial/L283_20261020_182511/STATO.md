# STATO — L283 (`data/wanderer/wanderer missions.txt`, righe 42–88)

**Stato: CHIUSO.** Secondo lotto del file: **tre missioni** della serie della pianta (`The Plant 1` → `2` → `3`), con **18
alternative fra parentesi quadre**. File a **27/54 (50,0%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L283_20261020_182511/` |
| righe | 42–88 |
| unità | **14** — 9 `MISSION_TEXT` + 2 `DESCRIPTION` + 2 `VALUE` + 1 `DIALOG` |
| parole | **495 EN → 435 IT** (0,88) |
| rapporto | **0,90 – 1,07** |
| contesti | **3** — `The Plant 1` (42–45) · `The Plant 2` (56–74) · `The Plant 3` (79–88) |
| tab | **7** (unità 1, 6–11) |
| virgolette | **18**, per unità |
| **alternative `[...]`** | **18** su 6 unità, due opzioni ciascuna |
| segnaposto | **4** in 3 famiglie — `<origin>` 1 · `<planet>` 2 · `<system>` 1 |
| apici | **9 EN** / **15 IT** (`Va'ika` ×9) |
| `check.py` | **27 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **24 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 13 prima · 14 qui · **27 dopo** la 88 |
| `sha256[:16]` | **`21980307855f6086`** |

## Comandi

```bash
python staging/editorial/L283_20261020_182511/check.py     # FAIL totale: 0 (27 controlli)
python staging/editorial/L283_20261020_182511/verify.py    # FAIL: 0 (24 controlli, 27/54)
```

## Le 18 alternative e il problema della concordanza

Il doppio del numero di L282, e con un vincolo in più: **l'articolo e gli aggettivi stanno fuori** dalla parentesi, quindi
tutte le combinazioni devono restare corrette. Tre casi hanno deciso una parola diversa dal dizionario:

| inglese | resa | perché |
|---|---|---|
| `in the [territory, region] of` | **nel `[territorio, dominio]`** | «nel **regione**» sarebbe sgrammaticato: due maschili |
| `it would have [grown, originated] here` | **sarebbe `[cresciuta, nata]` qui** | due participi femminili, concordi con «pianta» |
| `similar [regions, environments]` | **`[regioni, ambienti]` simili** | «simili» è invariabile: regge entrambi |

Le altre quindici sono coppie di verbi (`[creare, progettare]`, `[crescere, prosperare]`, `[crediamo, sospettiamo]`) o di
aggettivi con lo stesso genere e numero (`[artificiali, innaturali]`, `[danneggiati, distrutti]`).

## Il contenuto

- **`The Plant 2`** (56–74): arriva **Keti Va'ika**, specialista in **xenobotanica**. I Wanderer hanno **ripristinato** la
  pianta, ma la pianta «[ha origine, appartiene] allo spazio Korath»; Va'ika indica `<planet>` come prima tappa, perché è
  vicino ai Mereti e **fuori dal territorio dei loro rivali**. Alla domanda se siano davvero decisi a cedere i mondi agli
  **Slegati**, risponde «seccamente»: è il loro scopo guarire i mondi e poi **cederli** ad altre specie.
- **`The Plant 3`** (79–88): le **steppe alte e fresche** di un mondo Korath. L'aria **pizzica gli occhi**; Va'ika è troppo
  immersa nei pensieri. «Sarebbe cresciuta qui, ne sono certa. Ma non lo farà più, non per molti anni». China il capo e tiene
  **un'ala** davanti a sé.

## Limiti dichiarati

Nessuna approvazione (14 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Restano **27 unità** su
`wanderer missions.txt`.
