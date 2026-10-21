# REPORT — L223 · `remnant outfits.txt` (primo lotto, file nuovo)

## 1. Contenuto

Sei equipaggiamenti dei Remnant e la loro storia. L'**Inhibitor Cannon** nasce da un'arma aliena che l'equipaggio di un
esploratore decise di rubare invece di tornare a casa; l'**Inhibitor Turret** la adatta a una torretta per ostacolare gli
inseguitori; il **Thrasher Cannon** e il **Thrasher Turret** derivano per ingegneria inversa da un proiettile energetico
aliena; il **Point Defense Turret** viene copiato dai sistemi di difesa che sorvegliavano i depositi sotto **Aventine**; i
**siluri EMP** e la loro stiva chiudono il lotto.

## 2. Difficoltà

1. **Il lotto è quasi tutto traduzione.** 11 `DESCRIPTION` e un solo `VALUE`. In `successor ships.txt` copiavo 20 nomi e ne
   traducevo 6; qui il rapporto è invertito, e con 463 parole in 12 unità il lavoro per unità è più del doppio.
2. **La linea fra nome e parola comune.** `Inhibitor Cannon` è un nome e resta inglese anche dentro la prosa; *cannon* come
   parola comune diventa «cannone/cannoni». Se avessi tradotto il nome, il giocatore avrebbe visto «Inhibitor Cannon» nel
   negozio e «Cannone Inibitore» nella descrizione. Il controllo verifica **i due lati**: i nomi presenti, le forme inglesi
   assenti fuori dai nomi.
3. **L'unità 1 è una storia con una battuta.** La capitana dice: «Non torneremo a casa finché non ci impadroniremo di
   quell'arma.» Fra virgolette dritte, come parlato dentro la narrazione — e sono le **uniche due virgolette** del lotto.
4. **`reverse engineer`** → «ricostruire con l'ingegneria inversa». Il calco «fare reverse engineering» sarebbe gergale in
   una scheda di gioco.
5. **`strong torques`** → «forti coppie». In meccanica `torque` è la coppia, non la torsione: la torretta girevole non
   funzionava per le sollecitazioni, non perché si torcesse.
6. **`point-defense`** → «difesa puntuale»: termine tecnico, mentre `Point Defense Turret` resta il nome dell'oggetto.
7. **L'italiano è più corto**: 458 parole contro 463, rapporto 0,99–1,15. Non è un errore — è l'effetto di «cannoni»,
   «torrette», «siluri» al posto dei composti inglesi — ma è la prima volta nella campagna che il totale scende.

## 3. Un errore mio, corretto prima di chiudere

Il controllo sulle parole comuni cercava la stringa **«cannone»** al singolare. Il testo usa «cannoni» (unità 3), quindi
l'asserzione è caduta con `FAIL 1`. Aveva torto il controllo, non la traduzione: ora cerca le forme con una regex
(`cannon[ei]`, `torrett[ae]`, `silur[oi]`) e stampa le occorrenze trovate, così un eventuale fallimento futuro si legge
senza dover riaprire il file.

## 4. Numeri osservati

```
unita' 12 · {'DESCRIPTION': 11, 'VALUE': 1} · tutte PENDING
3 tab (unita' 2, 4, 11) · 2 virgolette (unita' 1) · 4 apici EN / 16 IT · 0 segnaposto
8 contesti, uno per equipaggiamento · righe 48/297 · 0 prima (primo lotto) · 45 dopo · confine 298 DESCRIPTION
1 unita' identica all'inglese (il VALUE), 11 tradotte
parole 463 -> 458 · rapporto 0.99 - 1.15 (media 1.08)
FAIL totale: 0 (28 controlli) · verify exit 0 (18 controlli) · sha256[:16] 865540cb64989e26
```

## 5. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/part01.json`, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (28), `verify.py` exit **0** (18) |

## 6. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 12 unità `PENDING`, nessuna scrittura su `state.db`.
- **Nessun equipaggiamento visto nel gioco**: la scelta di lasciare i nomi in inglese è coerente col database, non
  osservata nella schermata di allestimento.
- Restano **45 unità** nel file: L224 riparte dalla riga 298.
