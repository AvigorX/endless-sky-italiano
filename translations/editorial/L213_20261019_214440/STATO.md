# STATO — L213 · `deep jobs.txt` (secondo lotto)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L213_20261019_214440` |
| Righe / unità | **333–453** / **22** — file al **67/187 (35,8%)** |
| Tipi | {'TEXT': 12, 'DIALOG': 7, 'DESCRIPTION': 3} |
| Tab · virgolette · apici | **0** · **0** · **3 EN / 9 IT** |
| Segnaposto | **24** su 7 simboli, identici **per unità** |
| Contesti | **6** — da `Transport scientists` a `secure package pickup` |
| Parole | **436 EN → 413 IT** (rapporto 0,67–1,52) |
| sha256 | `a1c19c89ae374d9f…` |
| Esiti | `check.py` **25** (`FAIL totale: 0`) · `verify.py` **18** (`FAIL: 0`) |

## Cosa contiene

Missioni scientifiche e un nuovo blocco di frammenti: il **trasporto di scienziati** al laboratorio che deve analizzare
i risultati, il **dipartimento** di scienziati con lo stesso incarico, la **scorta a una nave scientifica** (`<npc>`), la
**registrazione di una conferenza accademica** e il **prelievo di un pacco sicuro** con quattro varianti di banco, luogo
e aspetto del pacco.

## Difficoltà

1. **Primo blocco di `DIALOG`** (7 unità): prosa parlata di missione, italiano naturale, **senza** l'inversione Saryd.
   Il controllo verifica che in quei testi non compaiano né «Coalizione» né i marcatori della Coalizione — se qualcuno
   applicasse la regola del registro per abitudine, il controllo cadrebbe.
2. **24 segnaposto su 7 simboli**, con `<npc>` che ricorre **quattro volte** e cambia posizione: apre la frase con
   l'articolo («La `<npc>` atterra»), sta nel genitivo («il capitano della `<npc>``) e nel soggetto («la `<npc>` non avrà
   visitato»). Il confronto è **per unità**, non a totale.
3. **Secondo blocco di frammenti** (unità 14–22, quattro gruppi di alternative): «Come da istruzioni, tu» + «ritiri il
   pacco da un banco bagagli sorvegliato» + «in una zona tranquilla dello spazioporto.» + «È una cassa grande…». Le
   alternative devono restare **distinte** (due banchi, due luoghi, tre pacchi) e l'iniziale deve restare quella inglese.
4. **Coerenza cross-lot**: «la struttura su `<stopovers>`» riprende l'unità 45 di L212, e «Il pagamento è `<payment>`» è
   la resa fissata in L198. Entrambe verificate come asserzioni.
5. **Zero virgolette ma 9 apici italiani**: solo elisioni (`un po'`, `dall'aria`, `l'aula`, `L'esperienza`,
   `dell'umanità`), legate alle unità.

## Verifica

```bash
cd staging/editorial/L213_20261019_214440
python check.py     # FAIL totale: 0 (25 controlli)
python verify.py    # FAIL: 0 (18 controlli) · confine riga 457, stesso tipo
```

**Non verificato**: nessuna missione giocata, nessuna schermata vista; 22 unità `PENDING`.
