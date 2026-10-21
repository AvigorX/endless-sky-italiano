# review.md — L239 (`data/avgi/avgi jobs.txt`, righe 20–656)

Registro delle decisioni editoriali del **primo lotto** di `avgi jobs.txt`: trentuno lavori, sei formule, un solo modo di
scrivere ognuna.

## 1. I `VALUE` restano inglesi (e la divergenza è dichiarata)

I 31 nomi di lavoro sono **dati**: si mostrano nella bacheca e il gioco li usa come identificatori visibili, quindi si
copiano **carattere per carattere**. Le misure sui precedenti, però, non sono uniformi:

| forma inglese | resa italiana nei lotti antichi | dove |
|---|---|---|
| `Rush delivery to <planet>` | «Consegna urgente a `<planet>`» (5) e «… su `<planet>`» (2) | `jobs.txt` L22, `intro missions.txt` L21b, `human missions.txt` L18, `remnant 1 introduction.txt` L24 |
| `Cargo to <planet>` | «Carico per `<planet>`» (1) | `human missions.txt` L19 |
| le stesse due forme | **invariate** (4 + 4) | **`coalition jobs.txt` L151** |
| `Rush delivery to <planet>` | **invariato** (4) | **`hai jobs.txt` L198** |

La linea scelta è quella dei **due lotti di lavori più recenti** e della regola del progetto (i `VALUE` sono dati): qui
restano inglesi **tutti e 31**. Chi riprende può allineare i cinque lotti antichi, ma non deve «correggere» questo.

## 2. Le sei formule, una resa ciascuna

| inglese | resa | n. |
|---|---|---|
| `Deliver <cargo> to <destination>. Payment is <payment>.` | **Consegna `<cargo>` su `<destination>`. Il pagamento è `<payment>`.** | 15 |
| `<destination> urgently needs a shipment of <cargo> by <date>. Payment is <payment>.` | **`<destination>` ha urgente bisogno di una partita di `<cargo>` entro il `<date>`. Il pagamento è `<payment>`.** | 9 |
| `Take these <bunks> specialists to <destination> to provide subject matter expertise in exchange for <payment>.` | **Porta questi `<bunks>` specialisti su `<destination>` per offrire competenze specifiche in cambio di `<payment>`.** | 2 |
| `Take these <bunks> researchers to <destination> to work for a term on the laboratory station in exchange for <payment>.` | **Porta questi `<bunks>` ricercatori su `<destination>` per lavorare per un periodo alla stazione di ricerca in cambio di `<payment>`.** | 2 |
| `Take these <bunks> diplomats to <destination> to negotiate with unhappy workers in exchange for <payment>.` | **Porta questi `<bunks>` diplomatici su `<destination>` per negoziare con operai scontenti in cambio di `<payment>`.** | 1 |
| `Take these <bunks> diplomats to <destination> to soothe dissatisfied Avgi in exchange for <payment>.` | **Porta questi `<bunks>` diplomatici su `<destination>` per placare gli Avgi scontenti in cambio di `<payment>`.** | 2 |

La prima è **ripresa identica** da 24 precedenti del corpus (`hai jobs.txt`, `deep jobs.txt`, `coalition jobs.txt`): è la
forma dominante, e cambiarla qui avrebbe creato una terza variante. La seconda è nuova: il file non aveva mai usato
`shipment of <cargo>` con `<date>`, e la resa tiene l'articolo su `<date>` come i **17 precedenti** («entro il
`<date>`») — senza articolo la frase si romperebbe con i valori che iniziano per preposizione.

## 3. Le scelte di parola

| inglese | resa | nota |
|---|---|---|
| `Deliver … to` | **su `<destination>`** | forma dominante (24 contro 9 «a»): la preposizione è dentro la frase, non davanti al segnaposto |
| `Payment is <payment>.` | **Il pagamento è `<payment>`.** | forma dominante del corpus |
| `in exchange for <payment>` | **in cambio di `<payment>`** | 20 occorrenze nel corpus |
| `subject matter expertise` | **competenze specifiche** | «materia» non renderebbe l'idea di *expertise*; «competenze» è già nel corpus |
| `to work for a term` | **per lavorare per un periodo** | «term» = periodo di servizio, non «termine» |
| `the laboratory station` | **la stazione di ricerca** | «laboratorio» da solo confonderebbe con l'edificio; la stazione degli Avgi (Ergastirio) è un impianto scientifico, e il corpus usa «nave scientifica» |
| `unhappy workers` | **operai scontenti** | |
| `dissatisfied Avgi` | **gli Avgi scontenti** | «scontenti» per entrambi, ma i referenti sono diversi: due frasi diverse, non una ripetuta |
| `to soothe` | **placare** | non «calmare»: è un intervento diplomatico, non un gesto affettuoso |
| `Take these <bunks> …` | **Porta questi `<bunks>` …** | `<bunks>` è un numero: «questi 4 specialisti» |

## 4. Segnaposto: la parità che conta è doppia

133 segnaposto in 6 famiglie. Due di esse hanno **lo stesso conteggio** (`<planet>` 31 e `<destination>` 31): un
confronto sui totali sarebbe cieco a uno scambio. Per questo il `verify.py` controlla **due cose**:

1. il **multiset per simbolo** (31 / 31 / 31 / 24 / 9 / 7 in entrambe le lingue);
2. **l'ordine dentro ogni unità** (`<destination>`, `<cargo>`, `<date>`, `<payment>` in quest'ordine, non solo presenti).

Nessuna unità ha segnaposto in una sola delle due lingue.

## 5. Struttura e assenze

- **Zero tab, zero virgolette, zero apici**: tre asserzioni negative scritte, non omesse. Il file è fatto di una riga per
  unità, senza dialoghi e senza citazioni.
- **31 contesti da due unità**: il `VALUE` e la sua `DESCRIPTION`. Nessun contesto è spezzato fra due lotti.
- **Le tre famiglie di merce** (`Generic`, `Avgi Cargo`, `Avgi Nuclear`) compaiono **solo nei contesti**, mai nel testo:
  non si traducono e non si citano.
