# -*- coding: utf-8 -*-
# part01: unita' 1-23 (Gegno Intervention).
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

P = {
1: "Convocazione dei Gegno",
2: "Presentati ai Gegno su <destination> entro i prossimi 8 giorni, dove scoprirai se hai un futuro con loro.",
3: "Mentre sei in fase di attracco al mondo ad anello, noti una grande nave Gegno color marrone chiaro già presente nell'hangar assegnato, circondata da diverse navi di entrambe le fazioni, Vi e Scin. Lì vicino un piccolo gruppo di Quarg discute qualcosa con un gruppo più piccolo di Gegno che sembrano piuttosto scontenti. Appena esci dalla nave, entrambi i gruppi tacciono e guardano verso di te. Riconosci Adrauni che ti si avvicina rapidamente insieme a un Gegno che indossa un'armatura molto elaborata, dall'aspetto né Scin né Vi.",
4: "Adrauni non esita a rivolgersi a te. \"<first> <last>. Presumo che tu comprenda il significato di questa faccenda.\"",
5: "\"Non sono sicuro di cosa stia succedendo.\"",
6: "\"Credo di aver capito il senso.\"",
7: "Il Quarg ora ti sta davanti, leggermente abbassato per parlarti. \"Come capita nella difficile situazione, diverse lamentele noi Quarg abbiamo ricevuto dai Gegno. Ti sei immischiato nei loro affari, una volta di troppo. Per quanto io desideri parlarti ancora della questione, né io né i Quarg ti saremo di ulteriore aiuto nelle tue imprese qui.\" Adrauni si volta verso il Gegno, che sembra quasi indifferente, o quanto meno cerca di evitare il tuo sguardo. Dopo una breve discussione di cui non capisci nulla, il Gegno si avvia verso la nave marrone chiaro. Come per un segnale, tutti gli altri Gegno nell'hangar tornano alle rispettive navi.",
8: "Mentre guardi tutte le navi andarsene, Adrauni parla di nuovo. \"Otto rivoluzioni ti sono state date dai Gegno per comparire sul loro mondo. Se non ottemperi, allora sei, nelle loro parole, congedato dal loro spazio.\"",
9: "\"Congedato?\"",
10: "\"Verrai con me?\"",
11: "\"Va bene, andrò.\"",
12: "Adrauni riflette per un breve momento. \"Un'espressione più appropriata sarebbe esiliato, o forse ripudiato? La cultura Gegno considera tutto come un'unica grande casa. La tua presenza nel loro spazio equivale a dire che sei già entrato, ma ora è un invito al quale non sei più gradito.\"",
13: "\"Non sono già indesiderato?\"",
14: "\"Non possono decidere dove vado.\"",
15: "\"È una filosofia difficile da spiegare. Anche noi Quarg siamo stati soggetti a inospitalità. In alcune notevoli capacità lo siamo ancora, ma in modo diverso da questo.\"",
16: "where",
17: "\"Sia come sia, non confondere precipitosamente questo con un'azione impunibile. Sui loro mondi vale il loro prudente arbitrio. Tuttavia, qualsiasi azione tu decida infine di compiere nel loro spazio non è priva di osservazione.\"",
18: "coming",
19: "\"Non lo sarò. Certo, è spiacevole che non possa più essere d'aiuto, ma il destino di questa faccenda appartiene solo a te e ai Gegno.\"",
20: "end",
21: "Adrauni si alza in tutta la sua altezza davanti a te un'ultima volta. \"Per conservare le poche relazioni che abbiamo con i Gegno, devo informarti che non possiamo più permettere l'accesso ai nostri mondi qui nel loro spazio. Nonostante questa disgrazia, aspiro a decisioni sagge da parte tua nel cammino che ti attende, <first> <last>.\" Adrauni ti fa un lungo inchino e lascia l'hangar; questa è probabilmente l'ultima volta che lo incontrerai. Ora tocca a te cercare una qualche base comune con i Gegno, se è ancora possibile.",
22: "Dopo aver deciso di aprire il fuoco sulla flotta Gegno che sorvegliava la tua visita al loro mondo natale, ti trovi davanti a un'opposizione aggressiva e a quelle che suonano come innumerevoli chiamate furiose. Qualsiasi possibilità ti restasse di avere a che fare con i Gegno è ora svanita.",
23: "Dopo aver deciso di aprire il fuoco sulla flotta Gegno che sorvegliava la tua visita al loro mondo natale, ti trovi davanti a un'opposizione aggressiva e a quelle che suonano come innumerevoli chiamate furiose. Qualsiasi possibilità ti restasse di avere a che fare con i Gegno è ora svanita.",
}

json.dump({str(k): v for k, v in sorted(P.items())},
          open(os.path.join(HERE, 'parts', 'part01.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('part01:', len(P), 'unita', min(P), '-', max(P))
