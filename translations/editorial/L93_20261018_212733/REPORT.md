# REPORT — L93 · `data/coalition/coalition culture conversations.txt`

## 1. Contenuto

Primo lotto del file, righe 24–66, un solo contesto (`Coalition Folklore: Saryd`, 31 unità):

- l'invito del Saryd in vesti tradizionali (2–7), con le prime due scelte del giocatore;
- il cammino nella foresta e la radura con tre sentieri e tre scrigni (8–13): semi, conchiglie, piume;
- il palco nel bosco, identico nei tre rami (15, 20, 25);
- tre spettacoli: **la caccia al leone da siepe** (16–18, ramo piuma), **il temporale e la grande quercia**
  (21–23, ramo seme), **il pescatore e la balena volante** (26–29, ramo conchiglia);
- la chiusura: l'inchino muto del pubblico, la restituzione dell'oggetto, il congedo del Saryd (30–31).

## 2. Scelte

| nodo | scelta | perché |
|---|---|---|
| sintassi Saryd | **ordine marcato italiano** («Una celebrazione del folklore Saryd, è») | è la voce della specie: normalizzarla cancella la caratterizzazione |
| `caskets` | **scrigni** | piccoli forzieri da rito, non «casse da morto» |
| `hedge-lion` | **leone da siepe** | calco trasparente, reso come nome inventato fra virgolette |
| `quills` | **aculei** | coerente con L91 (nessuna descrizione della specie li esclude) |
| `hoofs` | **zoccoli** | i Saryd sono ungulati nel gioco |
| `a third of the size of human opera stages` | **un terzo dei palcoscenici d'opera umani** | il paragone è del giocatore terrestre |
| `origami` | **origami** | prestito acclimatato |
| `the sun as his guide` | **con il sole come guida** | sintassi piana: qui parla il narratore, non un Saryd |

## 3. Difficoltà

1. **La voce invertita dei Saryd**: 4 unità (2, 5, 10, 31). Va resa con un ordine marcato che resti leggibile
   — non con un italiano sgrammaticato, che sarebbe una caricatura.
2. **Tre unità identiche** (15/20/25, 141 parole ciascuna): il costruttore le scrive da un'unica costante, così
   la resa non può divergere.
3. **0 token**: il controllo è `tok == 0`, asserito e stampato; ometterlo avrebbe lasciato un verde che non
   dice nulla.
4. **Unità 5 con 4 virgolette** (due battute citate nella stessa unità): il conteggio è per unità, non sul
   totale del lotto.
5. **Il giocatore non ha genere**: l'unità 2 è resa al plurale («Interessati a partecipare…, sareste?»), che
   elimina il problema senza perdere la cortesia della forma «voi».

## 4. Numeri osservati

```
unita' 31/31 · tab 30 · virgolette 22 = 22 (4 nell'unita 5) · token 0 = 0
parole EN 1744 -> IT 1616 · rapporto 0.93 - 1.55
righe 24/66 · file 157 unita · max(line) 462 · 0 prima / 126 dopo
FAIL totale: 0 (28 controlli) · verify exit 0 (27 controlli)
sha256[:16] f11dbf2fa0744173
```

## 5. Stato del progetto

```
TOTALE staging: 25018 unita · 798146 EN · 756826 IT
coalition culture conversations.txt: 31/157 (19,7%) · 1 lotto
residuo traducibile (formula state.py): 6912 · misurato: 7476 unità / 177879 parole su 129 file
file completi: 37
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | tre parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (28 controlli) **e** `verify.py` exit **0** (27 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 31 unità restano `PENDING`; il gioco non è stato caricato con questa traduzione.
- **Il file non è completo**: 126 unità restano; il contratto successivo è `HANDOFF_L94_20261018.md`
  (`Coalition Folklore: Arach`, righe 67–133).
- **Nessuna revisione umana**.
