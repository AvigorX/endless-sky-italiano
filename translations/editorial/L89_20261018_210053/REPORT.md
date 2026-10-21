# REPORT — L89 · `data/successors/successor outfits.txt` (chiude il file)

## 1. Contenuto

Dodici `DESCRIPTION` in sei contesti: le quattro varianti dell'**armatura in metamateriale** (ciascuna con un
paragrafo introduttivo identico e uno specifico), il **fucile railgun** e lo **shunt di scudi radioso** di Casa
Kaatrij (due paragrafi: il sospetto che sia un dispositivo di occultamento, e il vincolo di installazione).

## 2. Scelte

| nodo | scelta | perché |
|---|---|---|
| `metamaterial armor` | **armatura in metamateriale** | `metamaterial` è il termine tecnico |
| `nanoscale voids` | **vuoti nanometrici** | non «cavità»: sono vuoti strutturali |
| `in-combat repair efforts` | **riparazioni in combattimento** | non «sforzi di riparazione» |
| `railgun rifle` | **fucile railgun** | `railgun` resta invariato come nome d'arma |
| `intervening bulkheads` | **paratie interposte** | `intervening` è posizionale |
| `Radiant Shield Shunt` | nome inglese nei contesti | dato; in prosa «shunt di scudi radioso» |
| `one might be forgiven for guessing` | **si potrebbe essere perdonati se si supponesse** | l'ironia va tenuta |
| `period.` | **punto.** | l'enfasi è nel ritmo, non nel lessico |
| `non-specialists` | **non specialisti** | non «profani»: è un requisito tecnico |

## 3. Difficoltà

1. **Quattro unità identiche** (1, 3, 5, 7): il paragrafo introduttivo dell'armatura è ripetuto parola per
   parola. Reso **identico** e asserito in entrambi gli script.
2. **Sei tab su dodici unità**: il rapporto più alto del file; le unità con tab sono i secondi paragrafi.
3. **Zero virgolette** e **sette contesti con i due punti** nel nome (`Multimodal Armor: Light`): il nome si
   scrive intero, senza normalizzarlo.
4. **Chiusura del file**: invariante di file con copertura letta da tutti i `translation.json` del file.

## 4. Numeri osservati

```
unita' 12/12 · tab 6 (2,4,6,8,11,12) · virgolette 0 · token 0
rapporto 1.01 - 1.27 · parole EN 347 -> IT 388 · righe 574/647
CHIUDE il file: 0 dopo · 56 unita · max(line) 647 · copertura 56/56
FAIL totale: 0 (23 controlli) · verify exit 0 (25 controlli)
sha256[:16] c49081b925bee187
```

## 5. Stato del progetto

```
TOTALE staging: 24873 unita · 792339 EN · 751337 IT
successor outfits.txt: 56/56 (100%) · 2269 EN -> 2364 IT · 4 lotti
file completi: trentasei
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | parte, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` **e** `verify.py` exit **0**, **file 56/56** |
