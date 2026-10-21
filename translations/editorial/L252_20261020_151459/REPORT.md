# REPORT — L252 (`data/wanderer/wanderer jobs.txt`, righe 15–261)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **32 controlli**; `verify.py` esce 0 con **27 controlli** (invariante di
segmento: 0 prima, 26 qui, 66 dopo). `state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`: le 26 unità
restano `PENDING`.

## 1. Cosa contiene il lotto

Cinque lavori dei **Wanderer**, ciascuno in **due contesti** (`[0]` e `[1]`) con la **stessa prosa**: operai, agricoltori,
piccoli in gita di studio, scienziati in missione per inquinamento e per fenomeno naturale.

## 2. Misure

```
unità             26            (10 VALUE + 10 DESCRIPTION + 6 DIALOG)
parole            430 EN -> 426 IT       rapporto 0,93 - 1,12 (media 1,06)
contesti          10            cinque missioni × due contatori
tab               0             asserzione negativa scritta
virgolette        0             asserzione negativa scritta
apici             0 EN / 4 IT
segnaposto        58 in 6 famiglie, multiset E ordine per unità
gruppi identici   12            (11 con 2 copie, 1 con 4)
```

## 3. Le tre cose che il lotto ha di proprio

1. **Il lotto è quasi tutto ripetizione interna.** Ogni stringa compare **due volte** e la battuta degli scienziati
   **quattro** (due missioni × due contesti): **12 gruppi**, una resa ciascuno. Il controllo asserisce la distribuzione
   esatta delle molteplicità (`[2] × 11 + [4]`), così un gruppo che perde una copia si vede.
2. **`<bunks>` e `<destination>` sono 10 e 10.** Il multiset da solo sarebbe **cieco** a uno scambio: il confronto è anche
   **per ordine dentro ogni unità**, e il controllo dice esplicitamente perché.
3. **`Wanderer` resta invariato al singolare e al plurale.** Il corpus alterna «i Wanderer» (315) e «i Wanderers» (290):
   vince la forma **invariata**, più frequente, e il `verify.py` asserisce che `Wanderers` **non compaia**.

## 4. Le decisioni editoriali

| punto | decisione | perché |
|---|---|---|
| `These <bunks> Wanderer workers require transportation to <destination>. They will pay you <payment> to take them there.` | «Questi `<bunks>` lavoratori Wanderer hanno bisogno di un trasporto fino a `<destination>`. **Ti pagheranno `<payment>` per portarli fin là**.» | |
| `farmers` | **agricoltori** | non «contadini»: registro dei lavori |
| `younglings` | **i piccoli** | è una specie, non una scuola |
| `terraforming process` | **processo di terraformazione** | termine già nel corpus |
| `Payment will be <payment>.` | **«Il pagamento sarà `<payment>`.»** | il corpus alterna «compenso» e «pagamento» (3 e 3): scelto **pagamento**, coerente col resto del file (`Il pagamento è`) — la divergenza è dichiarata |
| `spike in atmospheric pollutants` | **picco di inquinanti atmosferici** | |
| `rare natural phenomenon` | **raro fenomeno naturale** | |
| `You wish the scientists the best of luck` | **«Fai gli auguri agli scienziati…»** | prima resa era «Auguri agli…» (un frammento): riscritta per rendere il verbo inglese |

## 5. Difetti trovati

Due rossi, **entrambi nell'asserzione**:

1. pretendevo parentesi **tonde e quadre** in **tutti** i 10 contesti: le tonde ci sono solo nei **quattro** degli
   scienziati (2 missioni × 2 contesti). Corretto il numero e la descrizione;
2. la prima resa della battuta degli scienziati era un frammento («Auguri agli scienziati su `<planet>`…») con rapporto
   0,87: riscritta con il verbo («Fai gli auguri…»), rapporto 0,93.

## 6. Copertura del file

```
L252   26 unità   righe  15 - 261
residuo 66 unità  righe 264 - 891
---------------------------------
26 + 66 = 92 = unità del file
```

## 7. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: le 26 unità sono `PENDING`.
- **Nessun testo visto nel gioco**.
- **Nessuna revisione umana**.
- **Il file non è completo**: 26/92 (28,3%).
