# -*- coding: utf-8 -*-
# part01: unita' 1-10 (Sol-Bound Shuttle).
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

P = {
1: "Entrando nello spazioporto immenso, noti che un gruppo di operai di fabbrica sta parlando con una capitana. Quando ti avvicini, vedi che la sua nave ammiraglia, uno Shuttle che ha conosciuto giorni migliori, è priva di iperguida.",
2: "\"Dov'è la tua iperguida?\"",
3: "\"Come farai a viaggiare da qualche parte con quella nave?\"",
4: "(Torna alla mia nave.)",
5: "La capitana ride. \"La maggior parte dei piloti è del tipo avventuroso. Io no. Faccio un buon gruzzolo solo portando gente dalla Terra a Marte e ritorno. Ogni tanto faccio viaggi sulla Luna per i turisti.\" Noti che usa il termine arcaico per Luna. Dev'essere un'espressione locale.",
6: "\"Non diventa noioso?\"",
7: "\"C'è davvero abbastanza traffico dentro il Sol perché tu ci possa vivere?\"",
8: "\"Rimarresti sorpreso. In questo sistema c'è molta gente, dopotutto, e molta di quella gente ha abbastanza soldi per lasciare la Terra ma non abbastanza per lasciare il Sol. È una bella nicchia che mi sono ritagliata.\"",
9: "\"Per te, forse. Dal tuo accento capisco che hai viaggiato un po' dal tuo pianeta natale. Io però preferisco restare vicina a casa. Con tutta l'instabilità della galassia, pirati, alieni e chissà cos'altro, restare nel Sol mi tiene al sicuro. Dimmi che sono paranoica, ma stare in un posto dove non devo preoccuparmene è qualcosa che tengo.\" Guarda di lato una nave a cui stanno riparando lo scafo. Il danno sembra essere stato causato da un'arma a raggio.",
10: "Vi salutate mentre salite sulle rispettive navi. Anche se siete entrambi capitani, le traiettorie delle vostre vite hanno preso strade molto diverse.",
}

json.dump({str(k): v for k, v in sorted(P.items())},
          open(os.path.join(HERE, 'parts', 'part01.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('part01:', len(P), 'unita', min(P), '-', max(P))
