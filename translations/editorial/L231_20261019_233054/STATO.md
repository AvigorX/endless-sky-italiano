# STATO — L231 · `korath outfits.txt` (quarto lotto)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L231_20261019_233054` |
| Righe / unità | **596–808** / **21** — file a **82/92 (89,1%)** |
| Tipi | **13 `DESCRIPTION`** · **8 `VALUE`** |
| Tab · virgolette · apici | **0** · **0** · **2 EN / 6 IT** |
| Segnaposto | **0** |
| Contesti | **13** — Comet Thruster e i quattro GP ibridi 1 unità, gli altri 2 |
| Parole | **455 EN → 498 IT** (1,04–1,37, media 1,08) |
| sha256 | `39c7cbdeb1825d8b…` |
| Esiti | `check.py` **27** (`FAIL totale: 0`) · `verify.py` **19** (`FAIL: 0`) |

## I tab tornano a zero

| lotto | tab |
|---|---|
| L228 | 0 |
| L229 | 3 |
| L230 | 7 |
| **L231** | **0** |

Quattro conteggi diversi in quattro lotti consecutivi dello stesso file. Il numero si misura **ogni volta**: ereditare
l'ultimo avrebbe fatto cercare sette tab in un lotto che non ne ha nessuno.

## Due nomi di scena nuovi

**Quarg** (5 occorrenze) e **Efreti** (5) restano invariati: sono popoli, come `Kor Efret`, `Mereti` e `Kor Sestor`. Il
controllo li conta in entrambe le direzioni, e la prima versione sbagliava il numero — vedi sotto.

## Il rapporto più alto della campagna

L'unità 1 arriva a **1,37**: *Like most Korath technology, this thruster's power is offset by its energy requirements and
heat output* → «Come gran parte della tecnologia Korath, la potenza di questo propulsore è compensata dalle sue esigenze
energetiche e dal calore che produce». L'inglese comprime in un possessivo (`thruster's power`) ciò che l'italiano distende in
una frase nominale. Resta nel gate (max 1,90), ed è il valore più alto registrato finora.

## Cosa contiene

I **Thruster** Lunar, Planetary e Stellar (e il Comet già iniziato in L230) — motori che producono più calore dei sistemi
d'arma di altre specie, con i **Quarg** che li guardano con disapprovazione e la leggenda della flotta accorsa a evacuare una
nave che invece stava solo accelerando. I cinque **Steering** (Asteroid, Comet, Lunar, Planetary, Stellar). E i quattro
**GP Hybrid Thruster** — **Arkrof**, **Farves**, **Gaktem**, **Nelmeb** — che uniscono propulsione gravitazionale e plasma,
con gli **Efreti** che superano le congetture della Teoria delle Stringhe.

## Difficoltà

1. **`the dubious distinction`** → «il dubbio primato»: l'ironia è nel sostantivo e va tenuta.
2. **`view … with particular distaste`** → «guardano … con particolare disgusto».
3. **La leggenda dei Quarg** (unità 7): due frasi lunghe, con *what they assumed was a dying ship* e *its intended mode of
   propulsion*. Rese come «quella che credevano essere una nave in fin di vita» e «il suo sistema di propulsione previsto».
4. **`small, powerful, and woefully inefficient`** → «piccolo, potente e tristemente inefficiente».
5. **`the forced retreat from research into interstellar jump drive technology`** → «il ritiro forzato dalla ricerca sulla
   tecnologia del jump drive interstellare»: `jump drive` resta invariato.
6. **`gravitoplasma-based thrusters`** → «propulsori a gravitoplasma»; **`synthesizing gravitational propulsion with …
   plasma thrusters`** → «sintetizzare la propulsione gravitazionale con … propulsori al plasma».
7. **`mathematically self-consistent, but stubbornly unfalsifiable, conjectures of String Theory`** → «le congetture
   matematicamente coerenti ma ostinatamente non falsificabili della Teoria delle Stringhe».
8. **`quantum gravity and the forces that bind quarks and gluons together`** → «la gravità quantistica e le forze che
   tengono insieme quark e gluoni».
9. **`thruster` e `steering`** → «propulsore» e «sistema di sterzata», termini distinti: il controllo verifica che entrambi
   compaiano senza scambi.

## Due errori miei, corretti prima di chiudere

1. **Residuo senza `VALUE`**: avevo scritto che nel residuo dopo la 808 ci fossero 2 `VALUE`. La query dice **0**: le 10
   unità rimaste sono tutte `DESCRIPTION`, quindi L232 chiuderà il file con **0 identiche / 10 tradotte**. Correzione nel
   controllo, e il dato è passato al contratto.
2. **Conteggio dei nomi di scena**: avevo fissato Quarg ed Efreti a **4** ciascuno; sono **5** e **5**. Anche qui il
   controllo è caduto e ho corretto lui.

Entrambi sono dello stesso tipo: **un numero dedotto invece che misurato**.

## Verifica

```bash
cd staging/editorial/L231_20261019_233054
python check.py     # FAIL totale: 0 (27 controlli)
python verify.py    # FAIL: 0 (19 controlli) · 82/92 · 10 dopo la 808 · confine 809
```

**Non verificato**: nessun equipaggiamento visto nel gioco; 21 unità `PENDING`.
