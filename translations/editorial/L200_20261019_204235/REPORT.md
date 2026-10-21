# REPORT — L200 · `hai jobs.txt` (quinto lotto, **chiude il file: 175/175**)

## 1. Contenuto

Dodici lavori di una famiglia numerata, `Superstitious Hai [1]…[12]`: gente che vuole viaggiare **solo su navi
dotate di chiave di volta Hai autentica**. Un solo `VALUE` ripetuto undici volte e dodici `DESCRIPTION` che cambiano
soggetto — matriarca, allevatori, anziano, braccianti, anziani in vacanza, famiglia — e, nelle prime sei, portano in
coda la richiesta esplicita del keystone.

| coppia | con keystone | senza | soggetto |
|---|---|---|---|
| 1 / 7 | unità 1 | unità 13 | matriarca e famiglia |
| 2 / 8 | 3 | 15 | allevatori |
| 3 / 9 | 5 | 17 | anziano → casa di riposo |
| 4 / 10 | 7 | 19 | braccianti |
| 5 / 11 | 9 | 21 | anziani in vacanza |
| 6 / 12 | 11 | 23 | famiglia Hai |

## 2. Difficoltà

1. **Chiusura del file**: il `verify.py` non confronta un confine ma l'**invariante di FILE**. Le altre quattro finestre sono lette dai rispettivi `translation.json`: se una fosse stata alterata, la somma non tornerebbe e il controllo fallirebbe.
2. **La struttura a coppie**: `[n]` e `[n+6]` sono la stessa `DESCRIPTION`, meno la frase sul keystone. Il controllo la toglie e confronta — un errore di una parola in una delle dodici rompe l'uguaglianza.
3. **Accordo grammaticale**: «Ha chiesto» (matriarca, anziano) vs «Hanno chiesto» (famiglie, gruppi). La frase condivisa ha due forme, e il controllo verifica che ognuna sia nel posto giusto.
4. **Terminologia contesa**: in staging `keystone` è reso sia «chiave di volta» sia «pietra chiave». Il lotto sceglie **chiave di volta** — la resa del lavoro che introduce l'oggetto (`Fetching keystones` → «Recuperare le chiavi di volta») — e il controllo pretende che l'altra non compaia.
5. **Due asserzioni corrette prima dell'esecuzione**: il conteggio delle occorrenze di «chiave di volta» (18, non 12) e il controllo dei contesti, che confrontavo per unità invece che per contesti distinti. La prima avrebbe dato un FAIL falso, la seconda l'ha dato davvero (`FAIL 1`) ed è stata corretta **nell'asserzione**.

## 3. Numeri osservati

```
unita' 23 · {'VALUE': 11, 'DESCRIPTION': 12} · tutte PENDING
0 tab · 0 virgolette · 0 apici · 57 segnaposto su 5 simboli
12 contesti (Superstitious Hai [1]…[12]) · righe 1753/2067 · 152 prima · 0 dopo
parole 354 -> 422 · rapporto 1.00 - 1.22 (media 1.09)
FAIL totale: 0 (25 controlli) · verify exit 0 (17 controlli) · sha256[:16] 3ff06bf4f8b326c1
FILE CHIUSO: 175/175 unita (100%) in 5 finestre
```

## 4. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/part01.json`, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto (compreso il `FAIL 1` intermedio) |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (25 controlli), `verify.py` exit **0** con `FILE CHIUSO: 175/175` |

## 5. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 23 unità `PENDING`, nessuna scrittura su `state.db`.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**, **nessuna revisione umana**.
- **Il file è chiuso in staging, non nel gioco**: 175 unità tradotte e verificate, zero approvate.
