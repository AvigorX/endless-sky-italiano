# -*- coding: utf-8 -*-
# part02: unita' 13-26 (News Reporter - Paradise, seconda meta') - chiude il segmento.
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

P = {
13: "\"Il Parlamento ha preso la decisione giusta rifiutando le richieste.\"",
14: "La reporter si acciglia. \"Può spiegare la sua risposta per i nostri spettatori?\"",
15: "\"Gli interessi di ogni mondo dovrebbero essere considerati, che siamo d'accordo o no.\"",
16: "\"Le Free Worlds non sono rappresentate abbastanza da ottenere risultati per i canali normali.\"",
17: "\"La Marina difende a malapena quel territorio, quindi le tasse non dovrebbero essere così alte.\"",
18: "\"Preferirei non rispondere.\"",
19: "\"Non sono sicura che il Parlamento sarebbe d'accordo con lei, ma voglio ringraziarla per le risposte e per il tempo che ci ha dedicato!\" dice.",
20: "I droni tornano a seguirla mentre prosegue per lo spazioporto.",
21: "La reporter sorride. \"Può spiegare quella risposta per i nostri spettatori?\"",
22: "\"Ci sono canali adeguati per presentare le proprie lamentele, e questo non è uno di quelli.\"",
23: "\"È una cosa molto ingrata da fare, quando è il Parlamento a proteggerli.\"",
24: "\"Preferirei non rispondere.\"",
25: "\"Siamo fortunati che molte persone la pensino così! Grazie per le risposte e per il tempo che ci ha dedicato!\" dice.",
26: "I droni tornano a seguirla mentre prosegue per lo spazioporto.",
}

json.dump({str(k): v for k, v in sorted(P.items())},
          open(os.path.join(HERE, 'parts', 'part02.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('part02:', len(P), 'unita', min(P), '-', max(P))
