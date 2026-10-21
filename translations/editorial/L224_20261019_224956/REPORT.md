# REPORT — L224 · `remnant outfits.txt` (secondo lotto)

## 1. Contenuto

Quattro equipaggiamenti e le loro storie. La **Teciimach Bay**, ultima revisione del lanciasiluri EMP, con due
miglioramenti: un meccanismo che modifica l'energia di ogni siluro perché ignori gli alleati, e un caricatore più grande di
un terzo. La **Teciimach Pod**, la versione per intercettori: lancia tutti i siluri pronti insieme, per le tattiche mordi e
fuggi. L'**Ember Tear**, l'arma che produce micro-strappi nello spazio-tempo e poi li ricuce, con il tecnico che alla domanda
se il nome significhi *strappare* o *piangere* risponde *'both.'*. Il **Crystal Capacitor**, cristalli di Viminal che
immagazzinano energia e, disperdendola, accelerano la dissipazione della ionizzazione.

## 2. Difficoltà

1. **Primato negativo: niente da copiare.** Tutte e 13 le unità sono `DESCRIPTION`. Non c'è un `VALUE` né un `TEXT`: il
   confronto è **0 identiche / 13 tradotte**. L'ho scritto come asserzione, non omesso: un controllo che si aspetta «qualche
   unità identica» qui sarebbe semplicemente sbagliato.
2. **9 tab su 13 unità.** È la densità più alta della campagna (prima: 1–3 per lotto). Un tab perso non si vede leggendo un
   paragrafo di quaranta parole: si vede solo contando per unità in entrambe le lingue.
3. **Tre unità con la stessa frase.** 1, 5 e 8 dicono tutte *Ammunition for this weapon can be restocked at any outfitter.*
   La resa è identica nelle tre — confronto con `==` su tre valori — perché sono tre equipaggiamenti dello stesso sistema
   d'arma e una divergenza sarebbe una svista invisibile.
4. **Il gioco di parole di `Ember Tear`.** *Tear* è sia «strappo» sia «lacrima», e il nome funziona su entrambi i sensi: il
   tecnico risponde *'both.'*, reso «'entrambe le cose'» fra **apici singoli**, come il sorgente. La domanda finale —
   *Should not the Ember Waste cry at the necessity of such weapons?* — diventa «Non dovrebbe forse l'Ember Waste piangere
   per la necessità di simili armi?», e il verbo «piangere» tiene il secondo senso del nome.
5. **`micro-tears … cauterizing them together again`** → «micro-strappi … li ricuce insieme»: la metafora chirurgica resta,
   senza spiegazioni.
6. **`ionizing`** → «ionizzare»: è l'effetto di gioco (la ionizzazione che blocca i motori), non chimica.
7. **Il rapporto più alto del lotto** — 1,58 nelle tre righe di servizio — viene da `outfitter` → «negozio di
   equipaggiamenti», termine fissato nei lotti precedenti. Preferisco un rapporto alto e un termine coerente a un termine
   più corto e incoerente.

## 3. Un errore mio, corretto prima di chiudere

Il controllo di coerenza cercava **«originariamente» dentro il testo inglese**, dove c'è `originally`. `FAIL 1`, corretto in
`'originally'`, aggiungendo l'asserzione che la forma italiana **senza** l'avverbio non compaia: così il controllo verifica
la differenza rispetto a L223/12, non solo la somiglianza.

## 4. Numeri osservati

```
unita' 13 · {'DESCRIPTION': 13} · tutte PENDING
9 tab (unita' 1, 3, 4, 5, 7, 8, 10, 11, 13) · 2 virgolette (unita' 3) · 3 apici EN / 16 IT · 0 segnaposto
5 contesti · righe 298/565 · 12 prima (L223) · 32 dopo · confine riga 581 DESCRIPTION
0 unita' identiche all'inglese, 13 tradotte (primato)
parole 472 -> 483 · rapporto 0.98 - 1.58 (media 1.22)
FAIL totale: 0 (28 controlli) · verify exit 0 (18 controlli) · sha256[:16] bee38f3d2fc80881
```

## 5. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/part01.json`, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (28), `verify.py` exit **0** (18) |

## 6. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 13 unità `PENDING`, nessuna scrittura su `state.db`.
- **Nessun equipaggiamento visto nel gioco**: né il funzionamento del Teciimach né l'Ember Tear sono stati osservati in
  partita.
- Restano **32 unità** nel file, **21** dopo la riga 674: L225 riparte dalla 581.
