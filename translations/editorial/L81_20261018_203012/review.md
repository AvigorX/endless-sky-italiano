# REVIEW — L81 · `data/successors/predecessors.txt`

## 1. Coerenza con la linea Successors (L68–L80)

- **`Multimodal Armor`** era già reso «corazza plurimodale» in **prosa** (L73, unità 51; L76): qui compare
  come **nome di equipaggiamento** (`Multimodal Armor: Regen`) e resta in inglese. Non è incoerenza: la prosa
  descrive, il dato nomina. La distinzione è dichiarata nel `STATO.md`.
- **`Resja`** è la stessa entità del poema: il nome della nave (`Resjan`) e il poema (`Resja incideva…`) sono
  coerenti fra loro e con il resto della linea.
- **Nessun dialogo, nessun registro**: il file è documentazione di gioco.

## 2. Nodi traduttivi aperti (dichiarati)

- **I nomi di equipaggiamento** sono lasciati in inglese: se un giorno si decidesse di tradurre le
  definizioni degli oggetti (`data/**/outfits.txt`), questa scheda andrebbe **rigenerata insieme** a loro,
  non da sola. È il rischio principale del lotto.
- **`"Iasa," Lethal Word`** e **`"Kis," Lethal Wish`**: le virgolette fanno parte del nome, e la virgola
  interna è nel nome. Non vanno «ripulite».
- **`Resjan` / `Hasuran`** sono forme aggettivali del nome (`Resja`, `Hasur`): restano invariati, come
  `Kasii-Cavasaa-Oa`.
- **La rima** è ricostruita, non tradotta: `dimora / divora / ancora / ignora` mantiene lo schema AAAA
  dell'inglese, ma è una scelta, non un equivalente letterale.

## 3. Il rapporto 1,00

Il rapporto complessivo è **1,00** perché 17 unità su 22 sono **copiate identiche** (dati). Non è un caso di
«non tradotto»: è la conseguenza della decisione, e il `check.py` lo dichiara con un controllo positivo
(`VALUE e TEXT restano identici`). Le uniche variazioni sono nelle cinque `DESCRIPTION` (1,00–1,21).

## 4. Cosa NON è stato fatto

- **Nessuna scrittura su `state.db`**: 22 unità `PENDING`.
- **Nessun caricamento nel gioco**: le schede delle due navi non sono state viste a schermo.
- **Nessuna traduzione dei nomi di oggetto**: scelta dichiarata, reversibile solo insieme ai file degli
  equipaggiamenti.
- **La poesia non è verificata come poesia**: il controllo misura solo la desinenza finale dei quattro versi.

## 5. Rischi residui

- **Se il gioco mostrasse questa scheda accanto a un elenco di equipaggiamenti tradotti**, il lettore
  vedrebbe due lingue. Oggi non accade: gli equipaggiamenti sono in inglese ovunque.
- **`1,21` è il massimo** (unità 14, il verso finale): dentro il gate.
- **Il `verify.py` asserisce 0 prima / 37 dopo**: se L82 non partisse dalla 208, diventerebbe rosso.

## 6. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 1 parte, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (30 controlli), `verify.py` exit 0 (34 controlli), sha256 `26f957d5edbd1958` |
