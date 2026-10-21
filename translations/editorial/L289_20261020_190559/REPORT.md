# REPORT — L289 (`data/gegno/gegno ships.txt`, righe 1193–1616) — **LOTTO TERMINALE**

**Esito: lotto CHIUSO, file CHIUSO a 37/37.** `check.py` esce 0 con **24 controlli**; `verify.py` esce 0 con **21 controlli**.
`state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 12 (tutte `DESCRIPTION`) | 12 |
| parole | 647 | **718** (1,11) |
| tab | 5 | 5 (righe 1193, 1194, 1481, 1548, 1616) |
| virgolette | 0 | **0** |
| segnaposto / alternative | 0 / 0 | **0 / 0** |
| apici | 4 | 5 |

Rapporto per unità **1,06 – 1,27**.

## 2. Invariante di FILE

```
FILE         37/37 (100%) · 37 righe distinte · prima 53 · ultima 1616 · zero dopo
SOMMA LOTTI  7 (L286) + 9 (L287) + 9 (L288) + 12 (L289) = 37
COPERTURA    nessuna unità del file fuori dallo staging
OVERLAP      nessun altro lotto rivendica le righe 1193-1616
```

Il `verify.py` riapre **tutti** i `translation.json` dello staging, conta i lotti del file e confronta la **lista** `[7, 9, 9, 12]`,
non solo la somma: un lotto che avesse rubato righe a un altro sarebbe emerso.

## 3. L'istruzione di gioco

L'unico testo in **seconda persona** del file:

> «I velivoli da combattimento non sono dotati di iperguida. **Non puoi trasportare** un velivolo da combattimento se non hai
> nella **tua** flotta una nave con una **baia di caccia**.»

Non è dialogo: è il gioco che **spiega una regola** al giocatore. Il controllo sul registro è quindi:

```python
[line for u in tu if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te|puoi)\b', italian)] == [1194]
```

La lista esatta, non `not any(...)`: se un'altra scheda scivolasse nella seconda persona, il test lo vedrebbe.

## 4. Le quattro coppie e i cinque tab

| coppia | tab | seconda metà apre con |
|---|---|---|
| `Halite` 1193–1194 | **due** (anche la prima) | «I velivoli da combattimento…» |
| `Feldspar` 1480–1481 | sulla seconda | «Capaci di mantenere una buona posizione…» |
| `Epidote` 1547–1548 | sulla seconda | «Come le altre navi dei Gegno Scin…» |
| `Kyanite` 1615–1616 | sulla seconda | «Il sistema di scanner…» |

## 5. Terminologia

| inglese | resa |
|---|---|
| `swarm of instant damage` | **sciame di danni istantanei** |
| `under protective shielding` | **sotto uno scudo protettivo** |
| `take on a shuttlecraft` | **versione di una navetta** |
| `almost twice as fast` | **quasi due volte più veloce** |
| `always be orbiting and firing on the move` | **orbitare e sparare sempre in movimento** |
| `small luxury transport` | **piccolo vascello di trasporto di lusso** |
| `top ranking Scin scientists` | **scienziati Scin di grado più alto** |
| `in exchange for less durability` | **in cambio di minore robustezza** |
| `a Scin creation to behold` | **una creazione Scin che vale la pena vedere** |
| `dangerously well-rounded ship` | **nave pericolosamente completa** |
| `putting down artillery fire` | **riversano fuoco d'artiglieria** |
| `rear fighter docking bay` | **baia di attracco per velivoli nella parte posteriore** |
| `three dorsal turrets` | **tre torrette dorsali** |
| `intricately-built test platforms` | **piattaforme di prova dalla costruzione complessa** |
| `littering the two long structures` | **disseminati sulle due lunghe strutture** |

## 6. Verifica

```
check.py   24 controlli · FAIL totale: 0 · exit 0
verify.py  21 controlli · FAIL: 0 · exit 0
FILE       37/37 (100%) · ventitreesimo file completo
```

**Primo giro verde**, senza correzioni: il contratto aveva già isolato le tre trappole (continuità del `Halite`, tab doppio sulla
stessa nave, seconda persona nell'istruzione).

## 7. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 12 unità `PENDING`; il file è **finito in staging**, non approvato.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Il file è completo al 100%** solo in staging.
- **Le istruzioni di gioco** sono verificate **per forma e registro**, non eseguite a schermo.
