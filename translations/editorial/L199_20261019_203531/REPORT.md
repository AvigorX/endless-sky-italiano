# REPORT — L199 · `hai jobs.txt` (quarto lotto)

## 1. Contenuto

Il **turismo culturale Hai**: quattro eventi in due taglie (cinema, musica, sicurezza informatica, fantascienza),
più la chiusura della convention d'affari aperta in L198 e il primo pezzo di `Superstitious Hai [1]`.

| blocco | unità | righe | contenuto |
|---|---|---|---|
| convention [2] | 1 | 1579 | l'arrivo: «Percepisci un pizzico di nervosismo…» |
| cinema | 2–7 | 1586–1621 | `[1]` piccolo e `[2]` grande |
| musica | 8–13 | 1628–1663 | la musica si sente già dallo spazioporto |
| sicurezza informatica | 14–19 | 1670–1705 | conversazioni che passano sopra la testa |
| fantascienza | 20–25 | 1711–1746 | il gesto riconosciuto da una vecchia serie |
| `Superstitious Hai [1]` | 26 | 1750 | apre la missione che continua in L200 |

## 2. Difficoltà

1. **La struttura è la prova**: quattro coppie che devono differire solo per `grande` e quattro coppie di `DIALOG` che devono essere identiche. Il `check.py` verifica le relazioni (sottrazione di `grande`, uguaglianza nella coppia), non unità isolate: un errore in una delle otto unità rompe il confronto.
2. **Una stringa ha già una resa** (unità 1, identica a L198 unità 49): il controllo la confronta con lo staging e pretende la stessa. Le altre 25 stringhe sono nuove: nessun precedente da rispettare, quindi nessuna scelta forzata.
3. **Il confine anomalo**: 1750 e 1753 sono la stessa missione, con tipi diversi. Il `verify.py` misura l'identità del contesto e la differenza del tipo — è l'unico punto in cui il file non rispetta «un confine, una missione».
4. **Zero virgolette e zero apici italiani**: tre asserzioni vuote scritte; l'unica asimmetria è il possessivo inglese (2 apici contro 0).

## 3. Numeri osservati

```
unita' 26 · {'VALUE': 9, 'DESCRIPTION': 8, 'DIALOG': 9} · tutte PENDING
0 tab · 0 virgolette · 2 apici EN / 0 IT · 42 segnaposto su 3 simboli
10 contesti · righe 1579/1750 · 126 unita' prima · 23 dopo · confine riga 1753 (stessa missione)
parole 489 -> 488 · rapporto 0.89 - 1.22 (media 1.03)
FAIL totale: 0 (28 controlli) · verify exit 0 (21 controlli) · sha256[:16] 6af91de2eec66a88
```

## 4. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/part01.json`, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (28 controlli), `verify.py` exit **0** (21 controlli) |

## 5. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 26 unità `PENDING`, nessuna scrittura su `state.db`.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**, **nessuna revisione umana**.
- **Il file non è chiuso**: 23 unità dopo la riga 1750; resta **L200**, che è l'ultima finestra.
