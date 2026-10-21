# REPORT — L327 (`data/_ui/help.txt`, righe 15–69) — **PRIMO DI TRE LOTTI** (segmento, non file)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **20 controlli**; `verify.py` esce 0 con **14 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). **Nessuna scrittura su `state.db`**, verificata anche dal **mtime**.

## 1. Il fatto principale: qui non si traduce, si **trascrive**

Le 28 unità della finestra sono **già `APPROVED`** nel database. Il lotto ha preso il testo approvato come **autorità** e l'ha portato
in staging.

| voce | inglese | italiano |
|---|---|---|
| unità | 28 (`HELP`) | 28 (**tutte approvate**) |
| parole | 1.138 | **1.043** (0,917) |
| contesti | 14 | **14** |
| segnaposto | **14** in **5 forme** | **14**, identici |
| virgolette | **12** (4 righe) | **12** |
| tab | **0** | **0** |

Rapporto **0,82 – 1,38**: il minimo è la riga 11 («I membri dell'equipaggio occupano spazio…»), il massimo la riga 18 (il vuoto tra le
stelle).

## 2. Come è emerso, e perché conta

Il primo `check.py` conteneva — come in tutti i lotti precedenti — l'asserzione «tutte le 28 unità sono `PENDING`». È diventata
**ROSSA**: le unità erano **`APPROVED`**. Da lì l'indagine:

```
data/_ui/help.txt         113 unità = 68 APPROVED + 45 PENDING
data/_ui/interfaces.txt   244 unità = 244 APPROVED
data/_ui/tooltips.txt     667 unità =  52 APPROVED + 615 PENDING
                          TOTALE APPROVED 364, in SOLI 3 file
```

**Tutte le 364 unità approvate del progetto vivono in tre file di interfaccia.** Nessuna, in nessun altro file, era già approvata: i
326 lotti precedenti hanno lavorato su unità davvero `PENDING`.

E un controllo su **tutto lo staging** dice che le unità approvate già trascritte in passato — **52** dei tooltips — sono **identiche**
al database: **80 su 80** dopo questo lotto, zero divergenze. Il metodo delle trascrizioni precedenti ha tenuto.

## 3. Venticinque divergenze su ventotto, tutte da scartare

La traduzione indipendente che avevo preparato coincideva col testo approvato in **3 unità su 28**. Non erano errori ma **scelte**:

| riga | approvato | mia versione | chi vince |
|---|---|---|---|
| 15–16 | **mutui** / **mutuo** | ipoteche / ipoteca | **approvato** |
| 19 | **trilioni** | bilioni | **approvato** |
| 27–29 | **neutralizzata** | disabilitata | **approvato** |
| 36–38 | **incarichi** / bacheca degli **incarichi** | lavori / bacheca dei lavori | **approvato** |
| 38 | **ricercati** | taglie | **approvato** |
| 24 | "**Gestisci piloti**", "**Entra nella nave**" | "Manage Pilots", "Enter Ship." | **approvato** |
| 45 | "**Preferenze**", "**Manuale**" | "Preferences", "Manual." | **approvato** |

Il valore operativo: **prima di tradurre un file, guardare la colonna `italian`**. Un testo approvato è una revisione già fatta, e la
mia resa non ha titolo per sostituirla.

## 4. Due convinzioni sbagliate, e la correzione

1. **«Le etichette di interfaccia restano in inglese.»**
   Falso per le citazioni **dentro la prosa**: il testo approvato traduce «Gestisci piloti», «Entra nella nave», «Preferenze»,
   «Manuale». Le **630 `UI_LABEL` in attesa** sono un'altra cosa — sono le etichette **dentro `_ui/tooltips.txt`** (615 `PENDING` su
   667) — e **non** le citazioni nella prosa di aiuto.
2. **«Le 364 approvate non ci riguardano.»**
   Sono in tre file di interfaccia, e due di quei file hanno unità **non** approvate: `help.txt` 45, `tooltips.txt` 615. Sono lavoro
   residuo **vero**, non finito.

## 5. La scala comica dei `lost`

Il file non è solo istruzioni: le sette sezioni `lost` sono una **parodia progressiva** del giocatore che resta a vagare nello spazio.

| sezione | tono | riga |
|---|---|---|
| `lost 1` | **pratica**: «L'unico modo per raggiungere un altro sistema stellare è saltare» | 41 |
| `lost 2` | **paziente**: «nessuno ti terrà per mano» | 45 |
| `lost 3` | **lirica**: «Il vuoto tra le stelle è freddo e vuoto» | 48 |
| `lost 4` | **pubblicitaria**: «sei libero di fare ciò che vuoi con la tua piccola nave nuova» | 52 |
| `lost 5` | **ironica**: «O forse sei solo davvero, davvero scarso a capire come si gioca» | 57 |
| `lost 6` | **mistica**: «Il Tao che può essere detto non è il vero Tao» | 60 |
| `lost 7` | **nichilista**: «un minuscolo granello di calore… tace...» | 64–65 |

I segnaposto **restano comandi** anche dentro la parodia: nella 60 il testo cita `<Show main menu>`, `<View star map>` e `<Initiate
hyperspace jump>` **come desideri da lasciar andare**. Tradurli avrebbe rotto sia il tono sia la funzione.

## 6. Cosa NON è verificato (dichiarato)

- **Il testo non è una nuova traduzione**: è quello approvato, trascritto e verificato.
- **Copertura parziale dichiarata**: **28 su 113** unità del file (25%). Restano **85**: 40 approvate e **45 `PENDING`**.
- **Nessun testo visto nel gioco**; nessuna revisione umana **nuova**.
- **L1 e L2** restano senza `verify.py`: lacuna storica.
