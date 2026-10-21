# REPORT — L72 · `data/successors/successor 2 ghosts myurej.txt`

## 1. Cosa contiene il lotto

**La fuga e la consegna** (unità 1–17, contesto `Myurej 6` + `7`). Il giocatore fugge dalle navi da guerra
dei Predecessori e si raduna nello spazio dei Successori. Su un mondo disabitato, accanto a un cargo Myaede,
Ijaset consegna i manufatti: il capitano è lo stesso mercante di Kasii-Tuur-Saqru. Ijaset spiega che le navi
erano **antiche**, non di Myurej, e che forse aspettavano qualcuno come loro; ammette anche che Myurej vuole
mettere i «ninnoli» in mani che non ne capiscono il valore — «Non si fidano di te, e puoi biasimarli?». Paga
la tariffa (`<payment>`) e si congeda.

**Il messaggio e le forniture** (18–29, contesto `Myurej 8`). Una sfera di dati convoca il giocatore; allo
spazioporto un **addetto portuale** stressato lo scambia per il corriere delle forniture di nozze (`<tons>`)
e insiste finché non le carica.

**Il matrimonio subacqueo** (30–50). Un ascensore scende sotto l'oceano fino a un complesso sul fondo, fra
corridoi trasparenti e un oculo con i pesci. Arriva **Khiajsore**, erede di Myurej, coperto d'oro rosso:
parla in modo affettato e ridondante, si presenta due volte, e accompagna il giocatore fra piante di
zafferano e canali. Il discorso si fa politico: Kaatrij è «ferito e instabile», qualcuno muove i pezzi
«dietro le quinte», e le Casate prometteranno navi e tecnologie «mentre le nostre inibizioni svaniscono».
Chiude con l'invito al matrimonio di Myurej, «sotto le onde», dove il giocatore potrà perorare la propria
causa davanti a tutte le Casate — e con un fiore dorato offerto in dono. L'ultima immagine rovescia quella
iniziale: la finestra sull'oceano scuro somiglia allo schermo nero di Myurej.

## 2. Scelte editoriali

| nodo | scelta | perché |
|---|---|---|
| `scion` | **erede** | forma già usata in L45 per gli eredi delle Casate |
| `Khiajsore` | invariato; «Myurej M- Khiajsore» come nel sorgente | nome e titolo di Casa: non si traducono né si abbreviano |
| `biped fever` | **«febbre dei bipedi»** fra virgolette | è una moda raccontata come voce; le virgolette sono nel testo |
| `Ribbons of Iret` | invariato fra virgolette | nome di un fenomeno naturale |
| `oculus` | **oculo** | termine architettonico corretto, e il testo parla di un'apertura circolare |
| `mirth` | **ilarità** | usato due volte (43, 46), come l'inglese |
| `pastels` | **tinte pastello** | il corpo dell'erede «gioioso» |
| `saffron-colored flowers` | **fiori color zafferano** | colore, non spezia |
| `dockworker` | **addetto portuale** | evita «scarricatore», che qui non è il ruolo |
| `wedding supplies` | **forniture per il matrimonio** | formula amministrativa ripetuta tre volte |
| `waypoint` | **punto di rotta** | termine della mappa, non «waypoint» |
| `a grand project of restoration` | «un grande progetto di restauro» | coerente con il lessico delle Casate |
| `Fuggi verso lo spazio dei Successori` | titolo con verbo | forma dei nomi di missione già fissata |

## 3. Difficoltà incontrate

1. **Tre contesti in un lotto solo**: il piano (`HANDOFF_L72`) prevedeva 402–464 (20 unità). Chiudere il
   file in un lotto da 50 evita un ultimo lotto da 30 senza struttura e porta la copertura a 211/211. La
   deviazione è dichiarata, non silenziosa.
2. **`DIALOG` per la prima volta nel file**: le due unità sono **descrizioni di evento**, non etichette.
   Tradotte, e il `verify.py` asserisce che non siano identiche all'inglese: se fossero un'etichetta
   mascherata, il controllo la scoprirebbe.
3. **Un personaggio che si presenta due volte** (unità 38 e 39 finiscono con la stessa frase): è nel
   sorgente, in due risposte diverse. Non è un duplicato (l'inglese complessivo è diverso) e non è stato
   normalizzato: la ripetizione è caratterizzazione.
4. **Il discorso politico di Khiajsore** (unità 46 e 47) è quasi un doppione narrativo: due versioni della
   stessa promessa («le Casate ti prometteranno navi e tecnologie…»). Rese con parole diverse **dove
   l'inglese è diverso**, mantenendo la stessa idea: non sono due scelte identiche.
5. **`<tons>`, `<payment>`, `<stopovers>`**: segnaposto in mezzo a frasi amministrative. Parità per simbolo,
   non solo sul totale.

## 4. Numeri osservati (output letto)

```
unita' tradotte nell'intervallo   50/50
copertura del lotto               50/50
tab IT 36 / EN 36
virgolette IT 96 / EN 96
token IT 18 / EN 18
rapporto IT/EN 0.85 - 1.79
parole EN 1763 -> IT 1679
prima/ultima riga del segmento: 407/531
duplicati inglese: 0 gruppi
FAIL totale: 0                     (35 controlli)
verify.py exit 0                   (46 controlli)
sha256[:16] translation.json      bd09dd6de0b9ff04
```

## 5. Stato del progetto dopo il lotto

```
TOTALE staging: 24414 unita · 780024 EN · 739250 IT
APPROVED 364 · PENDING 32560 · totale 32924
lotti con translation.json: 76
file completi: 32 (era 31 prima di questo lotto)
residuo traducibile (formula): 7516
```

`successor 2 ghosts myurej.txt` è **completo**: 211/211 in cinque lotti (L68–L72), 6.612 EN → 6.329 IT.

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 3 parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`/`REPORT.md`/`review.md` |
| ESEGUITO | sì | `check.py` e `verify.py` lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` → `FAIL totale: 0` (35 controlli) **e** `verify.py` → `FAIL: 0`, exit **0** (46 controlli), chiusura 211/211 |
