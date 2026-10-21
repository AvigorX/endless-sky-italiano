# REPORT — L206 · `coalition news.txt` (primo lotto)

## 1. Contenuto

Primo lotto di un **nuovo file** e di un **nuovo tipo di unità**: `NEWS`, venti voci di notiziario, tutte citazioni.
Copre un servizio sugli arresti degli Heliarch, cinque battute di un allevatore di longcow, quattro di un contadino
Kimek e dieci di un agente Heliarch.

## 2. Difficoltà

1. **Il registro Saryd è il vero lavoro del lotto.** L'inglese dei Saryd è sintatticamente marcato (*«Caring for
   longcows, hard work it is»*, *«Too much space they take up»*). Tradurlo in ordine normale avrebbe cancellato la
   caratterizzazione; tradurlo in modo troppo libero avrebbe reso il testo illeggibile. La regola applicata è:
   complemento o predicato in testa, verbo in coda, soggetto dopo, con le virgole che il sorgente usa come pause.
2. **Il registro è verificabile.** Ho scelto un marcatore misurabile — la **chiusura con verbo flesso** — e il controllo
   verifica l'insieme esatto delle 9 unità che lo presentano, più il fatto che le due unità di narrazione non lo
   presentino. È una misura grezza, ma è una misura: non «mi sembra giusto».
3. **`Coalition Games`**: la mia prima asserzione lo elencava fra i nomi da conservare, mentre la resa lo traduce
   («Giochi della Coalizione»). Aveva torto l'asserzione: è un nome comune di evento, come «Giochi Olimpici». Ora c'è un
   controllo dedicato che verifica la scelta dichiarata.
4. **`longcow`**: invariato al singolare e al plurale. Il controllo confronta il numero di occorrenze nelle due lingue e
   rifiuta esplicitamente «longcowghi».
5. **40 virgolette**, tutte strutturali: nessuna è tipografia, tutte sono citazione. Verificate per unità, non a totale.

## 3. Numeri osservati

```
unita' 20 · {'NEWS': 20} · tutte PENDING
0 tab · 40 virgolette (2 per unita') · 5 apici EN / 9 IT · ZERO segnaposto
4 contesti · righe 28/94 · 0 prima · 92 dopo · confine riga 95 (stesso contesto)
parole 440 -> 415 · rapporto 0.90 - 1.28 (media 1.09)
registro: 9 unita' citate chiudono con un verbo, narrazione no
FAIL totale: 0 (25 controlli) · verify exit 0 (17 controlli) · sha256[:16] 7cff828f2fb7e44b
```

## 4. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/part01.json`, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (25), `verify.py` exit **0** (17) |

## 5. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 20 unità `PENDING`, nessuna scrittura su `state.db`.
- **Nessuna partita avviata**, nessuna schermata di notiziario vista, **nessuna revisione umana**.
- **Il registro Saryd va mantenuto** nelle 92 unità residue del file: è una convenzione nuova, non ancora validata da
  una revisione umana.
