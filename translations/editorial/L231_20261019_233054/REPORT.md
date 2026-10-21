# REPORT — L231 · `korath outfits.txt` (quarto lotto)

## 1. Contenuto

I **Thruster** dei Korath — Comet, Lunar, Planetary, Stellar — motori che, per ammissione degli stessi Korath, producono più
calore disperso dei sistemi d'arma della maggior parte delle altre specie. Con la leggenda della flotta **Quarg** che si
avvicinò per evacuare l'equipaggio di quella che credeva una nave in fin di vita, e scoprì che le fiamme erano il sistema di
propulsione. Poi i cinque **Steering** (Asteroid, Comet, Lunar, Planetary, Stellar) e i quattro **GP Hybrid Thruster**
(**Arkrof**, **Farves**, **Gaktem**, **Nelmeb**), dove gli ingegneri **Efreti** uniscono propulsione gravitazionale e plasma.

## 2. Difficoltà

1. **Quattro conteggi di tab diversi in quattro lotti**: 0 (L228), 3 (L229), 7 (L230), **0** (L231). Il numero di struttura
   si misura ogni volta — e in questo lotto il controllo verifica esplicitamente che sia **zero**.
2. **Due nomi di scena nuovi** (Quarg, Efreti), con una trappola: la prima versione del controllo li contava **4** volte
   ciascuno, mentre il testo ne ha **5**. Il controllo è caduto e ho corretto lui.
3. **Il rapporto più alto della campagna** (1,37, unità 1): l'inglese comprime in un possessivo ciò che l'italiano distende.
   Resta nel gate, ed è un dato che vale la pena tenere d'occhio per i lotti futuri.
4. **La leggenda dei Quarg** (unità 7): due frasi lunghe con due subordinate in cascata. Ho spezzato in italiano mantenendo
   l'ordine degli eventi (avvicinamento → offerta di evacuazione → sorpresa).
5. **`jump drive`** resta invariato; **`gravitoplasma`** è un composto che si conserva; **`String Theory`** diventa «Teoria
   delle Stringhe» (nome di teoria, si traduce).
6. **`thruster` / `steering`**: due termini distinti, «propulsore» e «sistema di sterzata», verificati senza scambi.

## 3. Due errori miei, corretti prima di chiudere

1. **Residuo senza `VALUE`.** Avevo scritto che le 10 unità dopo la 808 contenessero 2 `VALUE`; la query dice **0**: sono
   tutte `DESCRIPTION`. Il controllo ora asserisce «10 unità, tutte `DESCRIPTION`, nessun `VALUE`», e il dato è nel contratto
   L232, che chiuderà il file con **0 identiche / 10 tradotte**.
2. **Conteggio dei nomi di scena.** Quarg ed Efreti sono **5** e **5**, non 4 e 4. Il controllo è caduto con `FAIL 1` e ho
   corretto il numero, non il testo.

Entrambi sono **numeri dedotti invece che misurati** — la stessa famiglia di errore del contratto L220 (le virgolette «2 ×
17») e di L229 (i contesti «2 a testa»).

## 4. Numeri osservati

```
unita' 21 · {'DESCRIPTION': 13, 'VALUE': 8} · tutte PENDING
ZERO tab (erano 7 in L230) · ZERO virgolette · 2 apici EN / 6 IT · 0 segnaposto
13 contesti · righe 596/808 · 61 prima (L228-L230) · 10 dopo · confine riga 809 DESCRIPTION (scheda spezzata)
8 identiche (tutti e soli i VALUE), 13 tradotte (tutte e sole le DESCRIPTION)
parole 455 -> 498 · rapporto 1.04 - 1.37 (media 1.08)
FAIL totale: 0 (27 controlli) · verify exit 0 (19 controlli) · sha256[:16] 39c7cbdeb1825d8b
```

## 5. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/part01.json`, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (27), `verify.py` exit **0** (19) |

## 6. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 21 unità `PENDING`, nessuna scrittura su `state.db`.
- **Nessun equipaggiamento visto nel gioco**: la resa di «gravitoplasma» e dei propulsori ibridi è testuale.
- Restano **10 unità** nel file, tutte `DESCRIPTION`: **L232 è terminale** e chiuderà `korath outfits.txt` a **92/92**, il
  settimo file completo della campagna.
