# STATO — L217 · `deep jobs.txt` (sesto e **ultimo** lotto) — **FILE CHIUSO**

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L217_20261019_220809` |
| Righe / unità | **935–1234** / **29** — file a **186/187 tradotte + 1 `UI_LABEL` (100% dei traducibili)** |
| Tipi | {'VALUE': 12, 'DESCRIPTION': 12, 'DIALOG': 5} |
| Tab · virgolette · apici | **0** · **2** (unità 7) · **0 EN / 4 IT** |
| Segnaposto | **56** su **9 simboli** — il numero più alto della campagna |
| Contesti | **12** — da `Transport Consultants (Deep Security) [0]` a `Deep Hovercraft Large Racer Transport` |
| Parole | **375 EN → 398 IT** (rapporto 0,88–1,21, media 1,05) |
| sha256 | `379596a8a8be9b81…` |
| Esiti | `check.py` **27** (`FAIL totale: 0`) · `verify.py` **18** (`FAIL: 0`) |

## Perché è un lotto terminale

L'ultima unità del file è la **1234** e `line > 1234` vale **0**. Il `verify.py` usa l'**invariante di FILE**:

```
45 + 22 + 35 + 25 + 30 + 29 = 186 tradotte
186 + 1 UI_LABEL (riga 683) = 187 unità del file
```

| finestra | righe | unità |
|---|---|---|
| L212 | 16–322 | 45 |
| L213 | 333–453 | 22 |
| L214 | 457–682 | 35 |
| L215 | 684–864 | 25 |
| L216 | 866–929 | 30 |
| L217 | 935–1234 | 29 |
| **totale** | **16–1234** | **186 + 1 label** |

## Il tratto del lotto: 56 segnaposto su 9 simboli

È il numero più alto della campagna in un singolo lotto: `<destination>` 15, `<payment>` 12, `<date>` 8, `<planet>` 7,
`<cargo>` 6, `<bunks>` 4, `<fare>` 2, `<last>` 1, `<passengers>` 1. Il controllo confronta **l'ordine**, non solo il
multiset: con quindici `<destination>` un riordino silenzioso è possibile e non si vedrebbe contando i simboli.

## Cosa contiene

Le missioni della **Deep Security** (trasporto di consulenti, consegna urgente con scadenza), le **spedizioni** verso le
sedi della **Lionheart Industries** e della **Deep Sky**, e i **trasporti di corridori su hovercraft**, uno singolo e uno
per una squadra di `<passengers>` membri.

## Difficoltà

1. **Dodici `VALUE` restano inglesi**, anche quelli che contengono `<planet>` («Shipment to `<planet>`»); le dodici
   `DESCRIPTION` si traducono con le rese fissate («su `<destination>`», «Il pagamento è `<payment>`»).
2. **Famiglie**: 6 testi di `VALUE` (dimensioni `[1,1,1,2,2,5]` — «Shipment to `<planet>`» compare **cinque** volte) e 7
   testi di `DESCRIPTION` (`[1,1,1,2,2,2,3]`). La mia prima asserzione dava le `VALUE` `[1,1,1,1,2,2]`: sbagliata.
3. **Due `DIALOG` gemelli** (10 e 13, la stessa scena due volte): la resa deve essere identica, e il controllo lo verifica.
4. **`<passengers>-member racing team`** → «squadra da corsa di `<passengers>` membri»: l'inglese usa il segnaposto come
   aggettivo composto, l'italiano no.
5. **Zero apici in inglese, quattro in italiano**: solo elisioni (`dall'aria`, `all'avanguardia`).

## Verifica

```bash
cd staging/editorial/L217_20261019_220809
python check.py     # FAIL totale: 0 (27 controlli)
python verify.py    # FAIL: 0 (18 controlli) · FILE CHIUSO 186 + 1 label = 187
```

**Non verificato**: nessuna missione giocata, nessuna schermata vista; 29 unità `PENDING`.
