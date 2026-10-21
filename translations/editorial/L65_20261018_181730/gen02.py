# -*- coding: utf-8 -*-
# part02: unita' 22-43 (Exotic Life: Buccaneer Bay) - chiude il segmento.
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

P = {
22: "Passeggi sul lungomare sbiancato dal sole del pianeta, passando davanti a decine di bar impregnati di rum. Alla fine vedi un ristorante angusto incastrato tra un negozio di souvenir chiuso e l'ennesimo bar. L'edificio è dipinto color corallo e ha una pensilina di lamiera ammaccata, e sopra la porta pende un cartello scritto a mano con le parole \"Pesce Piatto Fresco e Squisito\".",
23: "Un cameriere allampanato con una barba argentata intrecciata e l'occhio sinistro cibernetico ti fa cenno con insistenza di entrare e lancia un grido ben esercitato: \"Il miglior Pesce Piatto della città! Esperienza irripetibile, più un souvenir famoso in tutto il mondo! Prova il Pesce Piatto: il pesce che è un piatto!\"",
24: "\"Cosa?\"",
25: "\"Quanto costa?\"",
26: "\"No, grazie.\"",
27: "\"Pesce Piatto! È un pesce che è un piatto. Buccaneer Bay è famosa per questi.\" Il cameriere ti fulmina con un fastidio moderato. \"È un pesce piatto con una testa grande. Il cranio è piatto e ha tre corna, quindi sta in piedi da solo come un piatto, e il resto del pesce lo cuciniamo per servirlo lì sopra. Il cranio te lo puoi tenere come piatto. Piatto. Pesce.\"",
28: "Il cameriere ti mette una mano sulla spalla. \"Solo 99 crediti, che affare! Il cranio da solo costerebbe 200 crediti ovunque. Che ne dici, vuoi il pasto di una vita?\"",
29: "\"Certo.\"",
30: "\"No, grazie.\"",
31: "\"Perfetto! Il costo del servizio è incluso.\" Il cameriere ti strappa i crediti, ti sbatte in mano un menù plastificato e uno scontrino, e ti spinge in un box angusto prima di correre via verso la cucina. Guardi lo scontrino e scopri che ti hanno addebitato 20 crediti per il 'posto a sedere', 30 per 'servizio di comodità', 50 per 'pulizia del pesce', 80 per 'montaggio del piatto' e 100 per 'oneri di servizio': un totale di 379 crediti.",
32: "Seduto dentro, il ristorante è ancora più stretto di quanto sembrasse da fuori. C'è un'unica fila di tavolini, un soffitto basso e una manciata di altri clienti che sembrano turisti spaesati. Il menù stesso copre pesce e cibo affine al mare come la Torta Nove Occhi, l'Elmo Pestato a Mano, la Lasagna Idrozoica e un 'Pescato del Capitano' dal nome sospetto. In cima al menù c'è un piatto in evidenza scritto in un corsivo sciatto, con sotto un riquadro vistoso che occupa un terzo dell'intero menù:",
33: "Pesce Piatto: meraviglia naturale e souvenir - 99 crediti",
34: "(oneri aggiuntivi non inclusi)",
35: "- Gli oceani di Buccaneer Bay sono pieni di creature senza mascelle simili a pesci, comunemente note come Teste d'Osso di Buccaneer Bay, che hanno una singola placca ossea sopra la testa e il corpo, un cranio sovradimensionato!",
36: "- Dal punto di vista ecologico sono per lo più filtratori, detritivori e brucatori, che consumano piccoli organismi o detriti dall'acqua, dal sedimento o dal fondo oceanico.",
37: "- I Pesci Piatti differiscono dalle altre Teste d'Osso di Buccaneer Bay: hanno una placca cranica quasi perfettamente circolare, tre piccole corna per respingere i predatori e nessun occhio, perché vivono sui fondali oceanici profondi e poco illuminati.",
38: "- Questi tratti rendono la placca cranica del Pesce Piatto il piatto-souvenir perfetto: rotondo, sigillato, con un treppiede integrato. Prendi il tuo oggi!",
39: "Il cameriere torna, e il piatto è inconfondibile. Porta un disco d'avorio di dimensioni rispettabili, l'osso liscio e lucidato, sostenuto sul tavolo da tre corna affusolate. Sul piatto c'è una singola coda carbonizzata, infilzata e grigliata finché la pelle sfrigola. È impressionante e appetitoso insieme.",
40: "(Dai un morso.)",
41: "(Ringrazia il cameriere e vattene.)",
42: "Dai un morso. La carne è... un tentativo atroce di cibo. All'inizio c'è una nota muffita e sulfurea, come compost bagnato, e sotto c'è un sapore quasi marcio che smentisce la freschezza visiva del pesce. La cosa più vicina a un sapore che salvi il tutto è un debole retrogusto terroso di fango salato.",
43: "Il cameriere arriva a pulire il Pesce Piatto con uno straccio, ti ringrazia di aver onorato il locale e fa un cenno col pollice verso la porta: una chiusura col botto per il tuo 'pasto di una vita'.",
}

json.dump({str(k): v for k, v in sorted(P.items())},
          open(os.path.join(HERE, 'parts', 'part02.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('part02:', len(P), 'unita', min(P), '-', max(P))
