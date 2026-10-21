# REPORT — L238 (`data/avgi/avgi news.txt`, righe 418–507)

**Esito: lotto CHIUSO, e con lui il file.** `check.py` esce 0 con **37 controlli** (`FAIL totale: 0`); `verify.py` esce 0
con **21 controlli** e l'**invariante di FILE** `22 + 20 + 15 + 23 + 14 + 21 = 115`. `state.py` esce 0 (`ESITO: OK`,
8/8). Nessuna scrittura su `state.db`: le 21 unità restano `PENDING`.

`data/avgi/avgi news.txt` è **completo in staging: 115/115 (100%)**, 2.164 EN → 2.124 IT, **sei lotti** (L233–L238).
È l'**ottavo file chiuso** della campagna.

## 1. Cosa contiene il lotto

| contesto | righe | unità | contenuto |
|---|---|---|---|
| `news:avgi engineer` | 418–424 | 7 | gli scudi che risolvono più problemi di quanti si creda; la scienza dei materiali contro gli scafi degli Aberrant; l'iperpropulsore; la manutenzione di una torcia a fusione; le navi a torcia prima degli scudi energetici; l'officina meccanica contro la «tolleranza al nanometro» |
| `news:avgi artist` | 452–454 | 3 | un'opera finita l'altro giorno; nessuno compra arte; l'arte non toglie risorse allo sforzo bellico (con l'etichetta a metà frase) |
| `news:avgi performer` | 478–480 | 3 | l'esibizione davanti all'Assemblea; la Twilight Guard che scrittura per le Guardie di ritorno dal fronte; la paga di chi si è comprato l'uscita dall'assedio |
| `news:avgi doctor` | 500–507 | 8 | i sessant'anni di vita naturale; i mediciti sopravvalutati; i cervelli di quarzo opaco; la morte che spegne i ricordi; il sistema nervoso ottico; la luce ultravioletta di Anax; due ricordi di lavoro (nave mercantile a torcia, manifattura su asteroide) |

## 2. Misure

```
unità             21            (tutte NEWS)
parole            502 EN -> 508 IT
rapporto          0,95 - 1,23 (media 1,10)   gate 0,55-1,90
contesti          4             (engineer 7, artist 3, performer 3, doctor 8)
tab               0             asserzione negativa scritta
virgolette        42            esattamente 2 per unità, in tutte e 21
apici             15 EN su 10 unità / 20 IT su 11 (massimo 4, unità 11)
segnaposto        0             asserzione negativa scritta
identiche         0             21 tradotte
etichette         20 in testa + 1 a metà frase (454)
```

## 3. Le tre cose che il lotto ha di proprio

1. **Cinque etichette nuove**, decise una volta e verificate nel conteggio: `Appreciation` → «Apprezzamento» (3),
   `Fascination` → «Fascinazione» (2), `Consideration` → «Considerazione» (2), `Recollection` → «Rievocazione» (2),
   `Advisement` → «Avviso» (1). Due di queste sono state scelte **contro** la prima idea: `Recollection` non è
   «Ricordo» (quello è `Remembrance`, 2 precedenti) e `Advisement` non è «Avvertenza» (quello è `Warning`, 1
   precedente). Il controllo asserisce **l'assenza** delle due forme scartate.
2. **Un'etichetta a metà frase** (454): `art is a waste, emphasis.` L'Avgi dichiara la modalità **dopo** una virgola e in
   minuscolo. È lo stesso dispositivo di L236 (etichetta in coda), spinto dentro il periodo. La resa lo riproduce
   (`, enfasi.`) e il controllo verifica sia la posizione sia la minuscola.
3. **`Twilight Guard` invariato, i membri tradotti**: il nome della fazione resta inglese (30 precedenti nello staging,
   decisione 16), ma `the Guards coming back from the front lines` sono «le Guardie che tornano dal fronte». Nome = dato,
   prosa = traduzione.

## 4. Copertura del file (invariante di FILE)

```
L233   22 unità   righe  32 -  91
L234   20 unità   righe 115 - 180
L235   15 unità   righe 197 - 280
L236   23 unità   righe 301 - 344
L237   14 unità   righe 369 - 399
L238   21 unità   righe 418 - 507
------------------------------------
22 + 20 + 15 + 23 + 14 + 21 = 115 = unità del file (min 32, max 507)
```

La finestra di L238 è **discontinua** (425–451, 455–477, 481–499 non producono unità): non è un buco, e il `check.py`
lo asserisce come tale. La copertura si legge dai **sei** `translation.json`, si confronta con il database e pretende
**115 id distinti su 115 righe distinte**, `max(line) = 507`, `line > 507` vuoto.

## 5. Controlli che hanno morso

Due rossi al primo giro, **entrambi nell'asserzione**:

1. il controllo tipografico elencava `un|una|la|di|da` fra le parole da cui un apostrofo è sospetto, e bocciava
   `un'opera`, `un'officina`, `un'arte` — che sono **elisioni corrette**. La lista è stata ristretta alle parole che in
   italiano vogliono un **accento** (`e'`, `piu'`, `perche'`, `cosi'`, `gia'`, `puo'`, `cioe'`, `percio'`), con
   `(?![a-z])` per non colpire `l'` e `un'`;
2. il controllo sui tre puntini leggeva `cov[15]` (unità 16) invece di `cov[14]` (unità 501): un **off-by-one** in un
   indice. Ora l'asserzione porta anche il numero di riga, così un errore simile si vede subito.

Nessuno dei due riguardava la traduzione. È la conferma della regola già nota: le asserzioni cadono per colpa
dell'asserzione.

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: le 21 unità sono `PENDING`; il file è completo **in staging**, non nel database.
- **Nessuna notizia vista nel gioco**.
- **Nessuna revisione umana**.
- **I nomi dei mestieri non compaiono nel testo**: i contesti `news:avgi engineer`/`artist`/… sono etichette del
  database, non stringhe da tradurre.
