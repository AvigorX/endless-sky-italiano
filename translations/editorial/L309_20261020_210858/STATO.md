# STATO — L309 (`data/avgi/avgi weapons.txt`, righe 716–969)

**Stato: CHIUSO — LOTTO TERMINALE.** Il file è **completo: 46/46 (100%)**, **ventinovesimo file interamente tradotto**
(**88** su 167 nel progetto).

| voce | valore |
|---|---|
| directory | `staging/editorial/L309_20261020_210858/` |
| file | `data/avgi/avgi weapons.txt` (**46/46 unità · 1.432 parole · righe 25–969 · 35 `DESCRIPTION` + 7 `TEXT` + 4 `VALUE`**) |
| righe | 716–969 |
| unità | **13** — **10 `DESCRIPTION` + 2 `TEXT` + 1 `VALUE`** |
| contesti | **6** — `"Nettle" KKV` (2) · `Nettle Flecks` (1) · `(root)` (1) · `"Orchid" Nuclear Missile` (3) · `"Ophrys" Nuclear Torpedo` (3) · `Ophrys Stockpile` (3) |
| parole | **446 EN → 465 IT** (1,04) |
| rapporto | **0,97 – 1,29** |
| tab | **6** — righe **717, 802, 803, 950, 951, 969** |
| virgolette | **4** — 2 coppie (788, 967) |
| segnaposto / alternative | **0 / 0** (asserzioni vuote) |
| apici | **3 EN / 17 IT** |
| seconda persona | **3 unità** (2, 7, 10) — avvisi di gioco |
| `check.py` | **26 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **25 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di FILE**: 46 unità · somma **12+21+13** · righe distinte · prima **25** · ultima **969** · **0 dopo** |
| `sha256[:16]` | **`2562eff1fd37187c`** |

## Comandi

```bash
python staging/editorial/L309_20261020_210858/check.py     # FAIL totale: 0 (26 controlli)
python staging/editorial/L309_20261020_210858/verify.py    # FAIL: 0 (25 controlli, FILE 46/46)
```

## Il file si chiude sulle **munizioni**

Le ultime schede sono le **tre munizioni** del file (`Nettle` KKV, `Orchid` Missile, `Ophrys` Torpedo) e il **magazzino** che le
rifornisce. Sono i pezzi che L307 e L308 citavano senza descrivere: **il cerchio si chiude**.

| riga | oggetto | idea |
|---|---|---|
| 716/717 | **`Nettle` KKV** | veicolo cinetico **economico**, si apre in **dozzine di barre di tungsteno** formando un cono |
| 742 | **`Nettle Flecks`** | `VALUE` — **copiato** |
| 788 | `"Nettle" KKV` | `TEXT` con contesto **`(root)`**: prima e unica unità radice del progetto |
| 801–803 | **`Orchid` Missile** | testata **termo-nucleare** a più stadi: «l'asso nella manica contro gli **Aberrant**» |
| 949–951 | **`Ophrys` Torpedo** | **stadio terminale** dell'`Orchid` con **corazzatura ablativa**: minaccia anche per una **nave capitale** |
| 967–969 | **`Ophrys Stockpile`** | baia di ricarica **remota** per portaerei; richiede **supervisione** |

## La frase «ammunition for» in tre varianti

| riga | arma | contenitore |
|---|---|---|
| 717 | `Nettle KKV` | **`Vertical Launch Array`** |
| 803 | `Orchid Missile` | **`External Launch Tube`** |
| 951 | `Ophrys Torpedo` | **`External Launch Rail`** *o* **`Ophrys Stockpile`** |

Stessa **struttura**, tre **contenitori** diversi (e la 951 ne ammette **due**). Il test verifica che tutte e tre dicano «è
munizione per…» e che ognuna citi il **proprio** contenitore.

**La nota munizioni di L307/L308** («si possono rifornire in qualsiasi emporio») **qui non compare**: le terzine finiscono invece
con questa frase. Il test verifica **l'assenza**, non solo la presenza.

## La seconda persona sono avvisi

Le unità 2, 7 e 10 dicono «**non puoi** comprare né usare»: sono **istruzioni di gioco** sull'equipaggiamento, non prosa. Il test
le elenca `[2, 7, 10]` e verifica che altrove la seconda persona **non compaia**.

## Refuso del sorgente

La riga 803 dice `without **a External** Launch Tube`: articolo sbagliato. Non si riproduce — l'italiano è «senza **un** External
Launch Tube».

## Limiti dichiarati

Nessuna approvazione (13 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Il file è **finito in
staging**, non approvato.
