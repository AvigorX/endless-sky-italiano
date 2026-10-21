# L22 — revisione editoriale

`data/human/jobs.txt` **completo**: righe **15–4600**, **390 unità**,
**5.823 parole inglesi → 5.969 italiane**, 161 contesti.

È il file delle **job board**: lavori generati dal gioco, non missioni narrative. Registro
burocratico-commerciale, frasi formulaiche, ripetizione strutturale altissima — il contrario di
`intro missions.txt`, e va trattato come tale: coerenza terminologica prima dell'eleganza.

## 1. Struttura e tipi

| tipo | n | trattamento |
|---|---:|---|
| `DESCRIPTION` | 161 | descrizione del lavoro: tradotta |
| `VALUE` | 157 | titolo del lavoro: tradotto |
| `DIALOG` | 52 | messaggio di chiusura: tradotto |
| `MISSION_TEXT` | 20 | testo della missione: tradotto |

Nessuna unità non traducibile (`NT` vuoto): il file non contiene né `UI_LABEL` né `label` dentro
`CONVERSATION`. Nessun token-pronome: la parità dei token è **esatta**, 840 su 840.

## 2. Il file non ha virgolette esterne

Prima scoperta, e la più costosa: in `jobs.txt` il campo `english` del database **non** contiene le
virgolette che invece avvolgono la stringa nel file (le ha solo la riga grezza). Nella prima stesura
avevo replicato l'uso dei lotti precedenti (testo fra virgolette): 100 unità su 100 sono state
bocciate dal controllo virgolette. Corretto il criterio: **il confronto è con il campo `english`**,
e le virgolette si riproducono solo dove il campo le contiene davvero — cioè dentro le battute
(unità 53, 59, 65, 71, 79, `"Siamo sotto attacco! …"`, e 337/341/345/349, l'annuncio della Marina).

Stessa trappola con le tabulazioni: scrivere `\\t` in JSON produce **due caratteri** (barra
rovesciata + `t`), non una tabulazione. Le unità `54, 55, 60, 61, 66, 67, 72, 73, 80, 81`
(`\t(Resta qui…)`, `\t(Unisciti alla flotta…)`) richiedono il carattere 0x09.

## 3. Le famiglie di varianti

Il file è costruito per **permutazione**: una matrice di taglie × regioni × casi.

- **Escort** (1–50): 5 taglie × 3 regioni (`into` / `out of` / `through`) × 2 registri
  («Nonostante la tua relativa inesperienza…» vs «Il capitano della <npc> ti pagherà…»).
  Singular/plural e direzione sono l'unica differenza: la traduzione li mantiene distinguibili
  («dentro una regione pericolosa» / «fuori da questa regione pericolosa» / «attraverso questa
  regione pericolosa»).
- **Pirate attack** (51–68): struttura identica, cambia solo chi difende (milizia / guarnigione
  della Marina / forze di difesa del Sindacato). Il `MISSION_TEXT` comune resta **identico** in
  italiano perché è identico in inglese; le righe finali no.
- **Consegne e passeggeri** (85–130): `Delivery` / `Bulk delivery` / `Rush delivery`, poi
  `Passengers`, con `Payment is <payment>.` ripetuto decine di volte → «Il pagamento è <payment>.»
- **Turisti** (139–158): *out* / *back*, singolo / gruppo / facoltosi. «desiderano viaggiare su una
  nave di lusso» solo dove l'inglese lo dice.
- **Bounty hunting** (269–334): taglie crescenti, con la variante locale («in arrivo su <system>»)
  e quella camuffata («si spaccia per un mercantile»).

In questi casi il controllo `DUP_OK` **deriva dal sorgente**: se l'inglese è identico la ripetizione
è ammessa, se differisce di una parola la traduzione deve differire. Un caso ha fatto scattare il
controllo: `311` «Marauder near <system>» (singolare) e `321/323/325` «Marauders near <system>»
(plurale). La prima stesura li aveva resi uguali; ora sono «Un Marauder vicino a <system>» e
«Gruppo di Marauder vicino a <system>».

## 4. Decisioni terminologiche

| EN | IT | nota |
|---|---|---|
| Escort | scorta | «Scorta per <planet>» (titolo) |
| Bulk delivery | consegna all'ingrosso | |
| Rush delivery | consegna urgente | |
| Large bulk/rush delivery | consegna all'ingrosso/urgente di grandi quantità | il «Large» non è una taglia di merce ma di carico |
| Passenger transport | trasporto passeggeri | |
| Parolee | scarcerato | «Trasporto di scarcerati» |
| Strike breakers | crumiri | termine italiano esatto; il valore resta «Crumiri su <planet>» |
| Marauder | Marauder | nome di classe di nave, invariato |
| Korath | Korath | specie aliena, invariata |
| Quarg | Quarg | «pianeta Quarg di <destination>» |
| Syndicate | Sindacato | come nei lotti precedenti |
| Republic Navy Advisory System | Sistema di Allerta della Marina della Repubblica | nome di servizio pubblico |
| Earth Day / Dirt Belt / Deep / Core / Rim | invariati | nomi propri/regionali |
| <student research> | lasciato come token | il motore inserisce `farming`, `volcanic`, ecc. |

Nota su `<student research>` (380–390): la frase inglese è «field research on the `<student research>`
`<planet>`». Il token è un aggettivo inglese, quindi non può reggere un accordo italiano: reso con
«sul pianeta <planet>, di tipo <student research>», che conserva entrambi i segnaposto senza
produrre «il pianeta volcanic».

## 5. Correzioni effettuate

- 100 unità riscritte per togliere le virgolette esterne non presenti nel sorgente.
- 10 unità (54, 55, 60, 61, 66, 67, 72, 73, 80, 81) riscritte con tabulazione reale (0x09).
- 6 unità (380, 382, 384, 386, 388, 390) riallineate sui token: avevo perso `<planet>`.
- 3 unità (321, 323, 325) differenziate dal singolare 311.

## 6. Controlli

```
check.py    FAIL totale: 0    (390/390, tab 10/10, virgolette 18/18, token 840/840)
verify.py   24 controlli, 0 FAIL, exit 0
```

Rapporto IT/EN: min 0,70 · max 1,65. Il totale italiano **supera** l'inglese (5.969 vs 5.823, +2,5%):
atteso, perché le formule brevi («Payment is <payment>.» → «Il pagamento è <payment>.») si allungano,
mentre nella prosa narrativa l'italiano tende a restare più corto.

## 7. Cosa non è stato fatto

Nessuna scrittura in `state.db` o negli output approvati; nessuna patch K4; nessuna build o
applicazione al gioco; **rendering non verificato** (fuori dal perimetro di questo workflow).
