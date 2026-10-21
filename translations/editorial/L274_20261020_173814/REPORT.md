# REPORT — L274 (`data/korath/korath ships.txt`, righe 364–602)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **25 controlli**; `verify.py` esce 0 con **21 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 9 (8 `DESCRIPTION` + 1 `VALUE`) | 9 |
| parole | 430 | **477** (1,11) |
| tab | 4 | 4 · primo carattere |
| virgolette | 0 | 0 |
| apici | 5 | 13 |
| segnaposto | 0 | 0 |

Rapporto per unità **1,00 – 1,31**.

## 2. Il lotto

| contesto | righe | contenuto |
|---|---|---|
| `'olofez` | 364, 400, 401 | `VALUE` `'olofezes` + caccia imbarcato + nota «senza iperguida» |
| `Kas'ik Tek 7` | 442, 443 | sonde di ricognizione e **recupero di microbot** + nota «senza iperguida» |
| `Rai'alorej` | 524, 525 | **rifugio-ospedale** per i naufraghi Korath + dotazioni |
| `Ikatila'ej` | 601, 602 | **fabbrica volante** a supporto di stazioni e navi-mondo |

`'olofez` **non è contiguo**: la riga 364 è il `VALUE`, le righe 400-401 sono le descrizioni. Il `check.py` verifica i confini
per **contesto**, non per adiacenza.

## 3. Due stringhe riprese dal corpus

Le unità 3 e 5 sono **identiche** a stringhe già presenti decine di volte nello staging. Il `check.py` non si limita a
confrontarle con una: raccoglie **tutte** le rese di quel testo inglese in tutti i `translation.json` e verifica che quella
scelta sia la **più frequente**:

```
unita 3 → «…una nave con una baia di caccia.»      (9 occorrenze, la scelta)
unita 5 → «…una nave con una baia per droni.»      (8 occorrenze, unica forma)
```

**Divergenza aperta, dichiarata**: `fighter bay` ha **due** rese nel corpus — «baia di caccia» (9) e «baia per caccia» (2).
Il lotto usa la maggioritaria; le due unità difformi stanno in lotti chiusi e non si toccano senza autorizzazione.

## 4. Terminologia

| inglese | resa | fonte |
|---|---|---|
| `hyperdrive` | **iperguida** | 76 unità del corpus (tooltips) |
| `fighter bay` | **baia di caccia** | maggioritaria (9) |
| `drone bay` | **baia per droni** | unica forma (8) |
| `fighter` / `drone` | **caccia** / **drone** | categorie del gioco |
| `microbot` | **microbot** | invariato, 8 unità |
| `hospital ships` | **navi ospedale** | |
| `world-ship` | **nave-mondo** | da L273 |
| `Systems Core` | **Systems Core** | invariato nel corpus, come nome di oggetto |
| `escape pod` | **capsula di salvataggio** | |
| `Shunt-Strikes` | **Colpi Shunt** | termine nuovo, dichiarato |

## 5. Verifica

```
check.py   25 controlli · FAIL totale: 0 · exit 0
verify.py  21 controlli · FAIL: 0 · exit 0
segmento   8 prima · 9 qui · 33 dopo la 602 · copertura 17/50 (34,0%)
```

Un rosso **non di merito**: il primo `check.py` non compilava (apostrofo di `'olofez` dentro una stringa a virgolette
singole). Corretto il literal, non il contenuto — poi verde al primo giro.

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 9 unità `PENDING`.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Il file resta aperto**: 17/50.
