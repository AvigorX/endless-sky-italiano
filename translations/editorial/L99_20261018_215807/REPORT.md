# REPORT — L99 · `hai culture conversations.txt` (tre missioni sportive + il gioco d'azzardo)

## 1. Contenuto

| contesto | righe | unità | cosa succede |
|---|---|---|---|
| `Wrestling Star` | 119–128 | 7 | folla che trilla, tavolo con stendardi, firma degli autografi — atleta muscoloso |
| `Fencing Star` | 142–151 | 7 | la stessa scena — schermitrice in divisa |
| `Mystery Sport Star` | 165–174 | 7 | la stessa scena — coppia con rete e frisbee a lame, disciplina mai spiegata |
| `Gambling Judgment` | 188–211 | 17 | i capitani umani a poker, gli sguardi torvi, i principi della maturità |

Le tre missioni sportive **non sono identiche**: condividono sei unità su sette (apertura, due scelte, la folla,
l'evento, il trillo) e differiscono in una (la descrizione dello stendardo) — più, nella terza, un'unità in più
perché l'atleta è una coppia e il testo cambia «certain human customs» in «celebrity signings».

## 2. Scelte

| nodo | scelta | perché |
|---|---|---|
| `trilling` | **trillare** | è il suono di gola degli Hai, distinto dal «cinguettio» (chitters, L95) |
| `signing event` | **sessione di autografi** | resa unica per tutte e tre le missioni |
| `of all things` | **nientedimeno** | |
| `buff looking` · `svelte` | **dall'aria piuttosto muscolosa** · **snello** | |
| `bladed frisbee` | **frisbee con lame** | |
| `maturity tenets` | **principi della maturità** | è il nome in-world della dottrina Hai |
| `To be honest in dealings` | **'Essere onesti negli affari'** | apici semplici dentro la citazione, come nel sorgente |
| `To gamble only on skill, not chance` | **'Scommettere solo sull'abilità, non sul caso'** | |
| `To have clear separation of fantasy and reality` | **'Avere una chiara separazione fra fantasia e realtà'** | |
| `taboo` | **tabù** | |
| `bluffing and manipulation` | **il bluff e la manipolazione** | |
| `base` (very immature and base) | **basso** | non «volgare»: è un giudizio morale, non sociale |
| `barkeep` | **barista** | |
| `diner`, `ground-side` | **tavola calda**, **a terra** | |
| `dark looks` | **sguardi torvi** | |
| `order pad` | **blocchetto degli ordini** | |
| `my gran` | **mia nonna** | |

## 3. Difficoltà

1. **Una virgoletta dispari voluta**: l'unità 32 apre la citazione del barista e **non la chiude**, perché la
   battuta continua nell'unità 33. In L97 e L98 il `check.py` cercava «nessuna virgoletta dispari»: qui il
   controllo è **l'opposto**, `odd == [32]`, e il `verify.py` lo riasserisce indipendentemente. Pareggiarla
   avrebbe aggiunto una virgoletta che il gioco mostrerebbe a schermo.
2. **Sette gruppi di ripetizioni**: cinque triple e due coppie. Sono rese da **costanti uniche** nel costruttore,
   quindi `assert P1[1] is P1[8] is P2[15]`: non possono divergere per distrazione.
3. **Le unità 5, 12, 19, 20 devono restare diverse** fra loro: `check.py` verifica che nessuna delle quattro
   coincida con un'altra — l'errore opposto a quello delle ripetizioni.
4. **`<last>` non c'è**: zero token e zero quadre sono **asserzioni**, non omissioni (misurate sul `source.json`).
5. **Un errore mio nel contratto, corretto dal `verify.py`**: `HANDOFF_L99` diceva «77 unità prima della riga
   119»; misurato sul DB sono **39** (le unità di L98), perché fra la 106 e la 118 non c'è nulla. 77 era il
   totale cumulativo. Corretti il contratto e la costante del `verify.py`; il lotto non cambia.

## 4. Numeri osservati

```
unita' 38/38 · tab 34 · virgolette 23 = 23 (una sola nella 32) · token 0 · quadre 0
parole EN 1183 -> IT 1151 · rapporto 0.94 - 1.33
righe 119/211 · file 147 unita · max(line) 386 · 39 prima / 70 dopo
FAIL totale: 0 (30 controlli) · verify exit 0 (28 controlli)
sha256[:16] 545c18fca521b07f · copertura file 77/147 (52,4%)
```

## 5. Stato del progetto

```
TOTALE staging: 25221 unita · 808811 EN · 766679 IT
hai culture conversations.txt: 77/147 (52,4%) · 2 lotti
file completi: 38 · residuo traducibile (formula state.py): 6709
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | tre parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (30 controlli), `verify.py` exit **0** (28 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 38 unità restano `PENDING`; il gioco non è stato caricato.
- **Il file non è completo**: 70 unità su 4 contesti (`Academy Motto`, `Robotic Musical 1`, `Hai Film Release`,
  `Sick of Acorn Bread`); prossimo contratto `HANDOFF_L100_20261018.md` (righe 212–320).
- **`HANDOFF_L99` non passa più il checker** ora che il lotto è aperto: i totali di staging sono cambiati
  (25.221 unità, 103 directory). È atteso, e il contratto va marcato `OBSOLETO` a fine lotto.
- **Nessuna revisione umana**.
