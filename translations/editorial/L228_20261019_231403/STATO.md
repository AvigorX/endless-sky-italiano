# STATO — L228 · `korath outfits.txt` (primo lotto — **file nuovo**)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L228_20261019_231403` |
| Righe / unità | **16–195** / **20** — file a **20/92 (21,7%)** |
| Tipi | **7 `VALUE`** · **13 `DESCRIPTION`** — file misto |
| Tab · virgolette · apici | **0** · **0** · **3 EN / 3 IT** |
| Segnaposto | **0** |
| Contesti | **13** — i tre Generator e i quattro Systems Core hanno 2 unità, gli altri 1 |
| Parole | **434 EN → 474 IT** (1,00–1,26, media 1,08) |
| sha256 | `49228f599876094f…` |
| Esiti | `check.py` **27** (`FAIL totale: 0`) · `verify.py` **20** (`FAIL: 0`) |

## Due primati negativi, entrambi asseriti

1. **Zero tab.** Ogni lotto della campagna finora ne aveva almeno uno; qui sono **0**, in inglese e in italiano.
2. **Zero virgolette**, terzo lotto consecutivo.

Nessuno dei due è un'omissione: entrambi sono scritti come `== 0` in `check.py` e `verify.py`. Un controllo che tace su uno
zero non distingue «non ce ne sono» da «non li ho guardati».

## Primo file misto

| | `successor ships.txt` | `remnant outfits.txt` | **`korath outfits.txt`** |
|---|---|---|---|
| composizione | 100 `TEXT` + 31 `DESCRIPTION` + 15 `VALUE` | 55 `DESCRIPTION` + 2 `VALUE` | **63 `DESCRIPTION` + 29 `VALUE`** |
| cosa si copia | quasi tutto | quasi nulla | **7 su 20 in questa finestra** |
| cosa si traduce | poco | quasi tutto | **13 su 20** |

È la prima volta che i due tipi convivono in proporzione simile: il controllo verifica che le **7 identiche siano tutti e
soli i `VALUE`** e le **13 tradotte siano tutte e sole le `DESCRIPTION`**, non solo i due totali.

## La linea fra nome e parola comune, con un caso nuovo

`Systems Core`, `Plasma Core` e **`Fusion Reactor`** (maiuscolo) restano inglesi: sono nomi di equipaggiamento, e
`Fusion Reactor` compare come tale anche nel database (missioni della Coalition). Ma all'unità 9 il testo dice *the Korath
designed a fusion reactor far more powerful…* — **minuscolo**, parola comune — e lì si traduce: «un reattore a fusione».

Stesso sintagma, due trattamenti, decisi dal **ruolo nel testo**. Il controllo verifica entrambe le forme: che `Fusion
Reactor` sia presente e che l'unità 9 dica «reattore a fusione» **e** che l'unità 7 **non** lo dica.

## Cosa contiene

Le tre classi di generatore Korath — **Candle**, **Furnace**, **Inferno** — e la loro incoscienza ambientale; i **Plasma
Core** singolo, doppio e triplo (il reattore delle navi capitali); i dissipatori di calore **Small** e **Large** e il
**Liquid Sodium Cooler** con il suo circuito a sodio; e i **Systems Core** in quattro taglie, con computer, scudi, energia di
riserva e sciami di microbot riparatori.

## Difficoltà

1. **`environmental impacts`** → «impatto ambientale»: i Korath non se ne curano, e il testo lo dice con *typical disregard*.
2. **`rather alarming isotopes`** → «isotopi piuttosto allarmanti»: l'aggettivo è ironico e va lasciato.
3. **`This compact Fusion Reactor is an ancient Korath design, and served as the mainstay of their war fleets`** → «fu il
   pilastro delle loro flotte da guerra»: `mainstay` già reso «pilastro» in L219 (Myaede).
4. **`a pair of the ancient and robust Korath Plasma Cores into a single package`** → «una coppia di Plasma Core Korath,
   antichi e robusti, in un unico blocco».
5. **`The sheer inefficiency … has forced them to become exceptionally good at one thing`** → «La pura e semplice
   inefficienza … li ha costretti a diventare eccezionalmente bravi in una cosa».
6. **`would overheat within seconds as soon as they began to fire their weapons`** → «si surriscalderebbe in pochi secondi
   non appena iniziasse a sparare»: l'inglese ripete *fire their weapons*, l'italiano «sparare» basta.
7. **`keep the sodium from freezing when the system is inactive`** → «così che il sodio non si congeli quando il sistema è
   inattivo»: il sodio liquido congela senza riscaldamento, ed è tutto il senso del sistema secondario.
8. **`dispense with Systems Cores`** → «rinuncia ai Systems Core»: `dispense with` è fare a meno, non distribuire.
9. **`only civilian small craft operators`** → «solo i piloti civili di piccoli vascelli».
10. **`a small reservoir which stores, produces and recycles a small microbot swarm`** → «un piccolo serbatoio che conserva,
    produce e ricicla un piccolo sciame di microbot».

## Verifica

```bash
cd staging/editorial/L228_20261019_231403
python check.py     # FAIL totale: 0 (27 controlli)
python verify.py    # FAIL: 0 (20 controlli) · 20/92 · 72 dopo la 195 · confine 208
```

**Non verificato**: nessun equipaggiamento visto nel gioco; 20 unità `PENDING`.
