# STATO — L293 (`data/avgi/avgi culture conversations.txt`, righe 260–270)

**Stato: CHIUSO — LOTTO TERMINALE.** Il file è **completo: 46/46 (100%)**, **ventiquattresimo file interamente tradotto** su 167.

| voce | valore |
|---|---|
| directory | `staging/editorial/L293_20261020_193311/` |
| file | `data/avgi/avgi culture conversations.txt` (**46/46 unità · 1.657 parole · righe 24–270**) |
| righe | 260–270 (le righe **268–269 non sono unità**) |
| unità | **9**, tutte `MISSION_TEXT` |
| parole | **274 EN → 270 IT** (0,99) |
| rapporto | **0,95 – 1,31** |
| contesto | **1** — `mission:Avgi Culture: Fencing` |
| tab | **9 su 9**, primo carattere |
| virgolette | **10**, per unità |
| apici | **5 EN / 14 IT** |
| segnaposto / alternative | **0 / 0** (asserzioni vuote) |
| `check.py` | **21 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **20 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di FILE**: 46 unità · somma lotti **8+12+17+9** · righe distinte · prima **24** · ultima **270** · **0 dopo** |
| `sha256[:16]` | **`c1bf446c7b612229`** |

## Comandi

```bash
python staging/editorial/L293_20261020_193311/check.py     # FAIL totale: 0 (21 controlli)
python staging/editorial/L293_20261020_193311/verify.py    # FAIL: 0 (20 controlli, FILE 46/46)
```

## Il duello, fino in fondo

Il primo round dura **meno di un minuto** e finisce con un **ding**: uno dei duellanti cade «con l'ala ripiegata». Poi il
**secondo round**, ancora vinto da **Zomp**. L'annunciatore dichiara — con la solita etichetta — «**Stupore**», «**Riposo**»,
«**Sconcerto**»; uno spettatore grida «**Isteria**! Sapevo che avrebbe vinto! Sono in vantaggio **dieci a uno** su questa
scommessa!», e un Avgi **rosa** urla «**Adorazione**! Ti amo, Zomp!».

La resa conserva **la scommessa con i numeri** («dieci a uno»), il **punto esclamativo** di «Adorazione!» e la **scherma come
spettacolo** — «un caos di acclamazioni, fischi e frullii sordi d'ali».

## Il distacco finale

L'ultima unità (riga 270) scioglie la scena: «**Lasci che i due volino via**, e prosegui per i fatti tuoi». È il ramo in cui il
giocatore **non** entra nell'arena: il file si chiude **due volte** — con la festa (267) e con l'uscita dal dialogo (270).

## Coerenza con L292

`reigning champion` → **«campione in carica»**, la stessa forma usata in L292 (logbook e annuncio): il test la verifica
esplicitamente sull'unità 263.

## Limiti dichiarati

Nessuna approvazione (9 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Il file è **finito in
staging**, non approvato.
