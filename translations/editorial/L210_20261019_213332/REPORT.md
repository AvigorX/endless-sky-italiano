# REPORT — L210 · `coalition news.txt` (quinto lotto)

## 1. Contenuto

Diciannove voci. Il lotto ha due anime: i **Giochi della Coalizione** (un venditore che vende miniature di arcologie e
repliche di armature Arachi; sei spettatori, tra cui un ex atleta che ora aiuta a organizzare l'evento; un addetto che
chiede scusa per una fila in ritardo di cinque minuti) e la **spedizione dell'ispettrice Sedlitaris**, promossa *arbiter*
al ritorno dall'esterno, con i consoli che litigano fra loro e un civile che non ci crede.

## 2. Difficoltà

1. **`Coalition Games` è un nome comune di evento** e si traduce (scelta di L206). Sette occorrenze, tutte «Giochi della
   Coalizione». Il controllo confronta i due conteggi invece di fissare un numero: se una delle due lingue cambia, cade.
2. **La gerarchia della Coalizione ha titoli misti.** `arbiter` resta prestito latino — «arbitro» in italiano è il
   direttore di gara, e il fraintendimento sarebbe immediato. `consuls` diventa «consoli» e `tribune` «tribuno»: sono
   titoli comuni, e in italiano hanno una forma naturale. La distinzione è dichiarata, non casuale.
3. **Il registro regge anche sui testi lunghi.** L'unità 10 è la più complessa del lotto: *«Though a success, that Saryd
   inspector's expedition was, turned many of the consuls furious at one another, her return has. Expected her to make it
   back, many of them had not.»* L'inversione è tripla e va riprodotta senza perdere il senso: «Per quanto un successo,
   la spedizione di quell'ispettrice Saryd è stata, ha reso molti consoli furiosi l'uno con l'altro, il suo ritorno. Che
   ce la facesse a tornare, molti di loro non se lo aspettavano.»
4. **22 apici italiani**: il testo è pieno di elisioni obbligatorie. Il controllo lega ogni apice all'unità, così si
   distingue l'elisione dalla citazione.
5. **Due errori miei, entrambi sulle asserzioni.** Il primo: cercavo `'field trip'` senza la virgola, che nel testo sta
   **dentro** le virgolette. Il secondo: `endswith('acquisto')` su una stringa che finisce `acquisto."` — il punto e la
   virgoletta fanno parte della stringa; serviva `rstrip`. In nessuno dei due casi ho toccato il testo.

## 3. Numeri osservati

```
unita' 19 · {'NEWS': 19} · tutte PENDING
0 tab · 38 virgolette (2 per unita') · 4 apici EN / 24 IT · ZERO segnaposto
5 contesti · righe 309/400 · 77 prima · 16 dopo · confine riga 401 (stesso contesto)
Coalition Games -> «Giochi della Coalizione»: 7 occorrenze in entrambe le lingue
parole 458 -> 437 · rapporto 0.94 - 1.30 (media 1.09)
FAIL totale: 0 (23 controlli) · verify exit 0 (17 controlli) · sha256[:16] ee5ce8eed7ac5542
```

## 4. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/part01.json`, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (23), `verify.py` exit **0** (17) |

## 5. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 19 unità `PENDING`, nessuna scrittura su `state.db`.
- **Nessuna schermata vista**, **nessuna revisione umana**.
- **Restano 16 unità** in questo file: L211, che lo chiuderà.
