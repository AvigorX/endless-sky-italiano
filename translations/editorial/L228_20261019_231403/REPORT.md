# REPORT — L228 · `korath outfits.txt` (primo lotto, file nuovo)

## 1. Contenuto

Gli equipaggiamenti dei Korath, un popolo che consuma energia senza guardare all'impatto. Le tre classi di generatore —
**Candle**, **Furnace**, **Inferno** — tutte radiotermiche, con isotopi sempre meno rassicuranti. I **Plasma Core** singolo,
doppio e triplo, il reattore a fusione delle navi capitali. I dissipatori di calore **Small** e **Large** e il **Liquid
Sodium Cooler**, con il suo circuito a sodio che deve restare caldo anche da inattivo. E i **Systems Core** in quattro
taglie: computer, generatori di scudi, energia di riserva e sciami di microbot che riparano lo scafo in volo.

## 2. Difficoltà

1. **Primo file misto.** 29 `VALUE` e 63 `DESCRIPTION`: la finestra ne prende 7 e 13. In `successor ships.txt` copiavo quasi
   tutto, in `remnant outfits.txt` quasi niente; qui il rapporto è ~1:2 e il controllo deve verificare **quali** unità sono
   identiche, non solo quante. Un «7 identiche» generico sarebbe compatibile con una descrizione lasciata in inglese e un
   nome tradotto per errore.
2. **Zero tab, per la prima volta.** Ogni lotto della campagna ne aveva almeno uno. Un `0` asserito è un fatto; un `0` non
   controllato sarebbe indistinguibile da una svista.
3. **`Fusion Reactor` / `fusion reactor`.** Lo stesso sintagma compare maiuscolo (nome di equipaggiamento, presente come tale
   anche nelle missioni della Coalition) e minuscolo (parola comune). Ho tradotto il minuscolo e lasciato il maiuscolo, e il
   controllo verifica **entrambe** le forme — compresa l'assenza di «reattore a fusione» nell'unità dove il nome è un nome.
4. **`keep the sodium from freezing when the system is inactive`**: il sodio liquido congela se non riscaldato, ed è tutto
   il senso del sistema secondario che assorbe energia anche a impianto spento. Una resa che saltasse quel dettaglio
   renderebbe inutile metà della scheda.
5. **`dispense with`** → «rinuncia a», non «distribuisce»: falso amico facile da sbagliare.
6. **`with their typical disregard for the environmental impacts`** → «con la loro tipica indifferenza per l'impatto
   ambientale»: l'ironia del testo sta nell'aggettivo *typical*, e va tenuta.

## 3. Numeri osservati

```
unita' 20 · {'VALUE': 7, 'DESCRIPTION': 13} · tutte PENDING
ZERO tab · ZERO virgolette (in EN e IT) · 3 apici EN / 3 IT · 0 segnaposto
13 contesti · righe 16/195 · 0 prima (primo lotto) · 72 dopo · confine riga 208 DESCRIPTION
7 identiche (tutti e soli i VALUE), 13 tradotte (tutte e sole le DESCRIPTION)
parole 434 -> 474 · rapporto 1.00 - 1.26 (media 1.08)
FAIL totale: 0 (27 controlli) · verify exit 0 (20 controlli) · sha256[:16] 49228f599876094f
```

## 4. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/part01.json`, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (27), `verify.py` exit **0** (20) |

## 5. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 20 unità `PENDING`, nessuna scrittura su `state.db`.
- **Nessun equipaggiamento visto nel gioco**: la distinzione `Fusion Reactor` / `fusion reactor` è dedotta dal database e
  dal testo, non osservata nella schermata di allestimento.
- Restano **72 unità** nel file: L229 riparte dalla riga 208.
