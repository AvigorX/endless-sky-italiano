# REPORT — L309 (`data/avgi/avgi weapons.txt`, righe 716–969) — **LOTTO TERMINALE**

**Esito: lotto CHIUSO, file CHIUSO a 46/46.** `check.py` esce 0 con **26 controlli**; `verify.py` esce 0 con **25 controlli**.
`state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | **13** (10 `DESCRIPTION` + 2 `TEXT` + 1 `VALUE`) | 13 |
| parole | 446 | **465** (1,04) |
| tab | **6** | **6** |
| virgolette | **4** | **4** |
| segnaposto / alternative | 0 / 0 | **0 / 0** |
| apici | 3 | 17 |
| contesti | **6** | invariati |

Rapporto per unità **0,97 – 1,29**.

## 2. Invariante di FILE

```
FILE         46/46 (100%) · 46 righe distinte · prima 25 · ultima 969 · zero dopo
SOMMA LOTTI  12 (L307) + 21 (L308) + 13 (L309) = 46
OVERLAP      nessun altro lotto rivendica le righe 716-969
```

`data/avgi/avgi weapons.txt` è il **ventinovesimo** file chiuso nel progetto (**88** su 167).

## 3. Il cerchio si chiude sulle munizioni

L307 e L308 **citavano** le munizioni (`"Nettle" KKV`, `"Orchid" Nuclear Missile`, `"Ophrys" Nuclear Torpedo`) come `TEXT`; qui
le **schede complete** le descrivono:

| munizione | che cos'è |
|---|---|
| **`Nettle` KKV** | veicolo cinetico **economico**: si apre in **barre di tungsteno** che formano un cono; «solo una frazione colpisce, ma la nuvola è difficile da eliminare» |
| **`Orchid` Missile** | **termo-nucleare** a più stadi, «rapporto resa-peso molto più alto» di qualsiasi cosa umana; l'**asso nella manica** contro gli `Aberrant` |
| **`Ophrys` Torpedo** | lo **stadio terminale** dell'`Orchid` con **corazzatura ablativa**: «permette persino ai droni piccoli di minacciare una nave capitale» |

## 4. «Ammunition for» ×3, contenitori diversi

| riga | contenitore/i |
|---|---|
| 717 | `Vertical Launch Array` |
| 803 | `External Launch Tube` |
| 951 | `External Launch Rail` **o** `Ophrys Stockpile` |

Il test verifica **tre** cose: che tutte dicano «è munizione per…», che ognuna citi **il proprio** contenitore, e che la **nota
munizioni** di L307/L308 **non compaia** (verifica dell'**assenza**: le terzine qui finiscono in altro modo).

## 5. Un contesto `(root)`

La `TEXT` della riga **788** ha contesto **`(root)`**: è la **radice del file**, non un outfit. Il test verifica il contesto
letteralmente — è l'unico caso del progetto.

## 6. Verifica

```
check.py   26 controlli · FAIL totale: 0 · exit 0
verify.py  25 controlli · FAIL: 0 · exit 0
FILE       46/46 (100%) · ventinovesimo file completo
```

**Primo giro verde**: i contesti con **virgolette nel nome** (`outfit:"Nettle" KKV`) erano già stati previsti nel contratto, scritti
fra **virgolette doppie** Python.

## 7. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 13 unità `PENDING`; il file è **finito in staging**, non approvato.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Il file è completo al 100%** solo in staging.
