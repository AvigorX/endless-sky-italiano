# REPORT — L205 · `hai outfits.txt` (quinto e ultimo lotto) — **file chiuso 65/65**

## 1. Contenuto

Tredici unità che chiudono il file: i propulsori atomici Hai (`"Bondir"`, `"Bufaer"`), i tre retropulsori
(`"Basrem"`, `"Benga"`, `"Biroo"`), tre descrizioni dei motori atomici come merce rara e costosa, il Pulse Rifle, e
il ciondolo Shield Beetle regalato da Nanachi con la sua teca.

## 2. Difficoltà

1. **Il lotto è terminale, e cambia il tipo di verifica.** Non c'è un confine da misurare: si verifica l'**invariante di
   file**. Le cinque finestre devono coprire esattamente le 65 righe del database, senza buchi e senza sovrapposizioni.
   È il controllo più forte della serie, perché non si può superare per caso: basta una riga dimenticata e cade.
2. **Coppia oggetto/confezione** (12–13): la seconda unità è indentata e descrive la scatola, non ripete il ciondolo.
   Come per la chiave di volta in L203, il tab è asserito in entrambe le lingue.
3. **Punteggiatura che sembra un errore e non lo è**: i tre punti dell'unità 10 stanno a metà frase; i due trattini
   dell'unità 13 sono trattini semplici. La prima asserzione che avevo scritto (`endswith('...')`) è caduta — e aveva
   torto lei, non il testo. Ora il controllo confronta i conteggi inglesi e italiani.
4. **Nomi di persona**: `Nanachi` resta invariato. È la prima volta nella campagna che un nome proprio di persona
   compare in una descrizione di equipaggiamento.

## 3. Numeri osservati

```
unita' 13 · {'DESCRIPTION': 13} · tutte PENDING
1 tab (unita' 13) · 2 virgolette (unita' 3) · 1 apice EN / 4 IT · ZERO segnaposto
12 contesti · righe 805/984 · 52 prima · 0 dopo (fine file) · confine: nessuno
parole 520 -> 524 · rapporto 1.00 - 1.27 (media 1.12)
FAIL totale: 0 (23 controlli) · verify exit 0 (16 controlli) · sha256[:16] 968d32112e56b1d4
FILE CHIUSO: 65/65 righe distinte, nessun buco, nessuna sovrapposizione
```

## 4. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/part01.json`, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (23), `verify.py` exit **0** (16) con invariante di file |

## 5. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 13 unità `PENDING`, nessuna scrittura su `state.db`.
- **Nessun caricamento nel gioco**, **nessuna revisione umana**.
- **Il file è completo in staging, non nel gioco**: `hai outfits.txt` è tradotto al 100% e nessuna delle sue 65 unità è
  approvata.
