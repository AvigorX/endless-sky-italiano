# -*- coding: utf-8 -*-
# part01: unita' 1-12 (News Reporter - Paradise, prima meta').
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

P = {
1: "Stai attraversando lo spazioporto quando vedi una giovane donna che cammina verso di te. Dietro di lei sfilano moltissimi droni-fotocamera, ciascuno contrassegnato da un logo composto da due curve che puntano verso l'interno.",
2: "(Aspetta che si avvicini.)",
3: "(Spera che non mi noti.)",
4: "(Cerca di evitarla.)",
5: "Prendi un corridoio laterale per sfuggirle. Proprio quando pensi di essere fuori vista, senti una voce. \"Mi scusi!\" Ti volti e vedi la reporter che ti segue.",
6: "Mentre continui a camminare, la senti chiamare: \"Mi scusi!\" Soffocando un sospiro, ti volti verso la reporter.",
7: "Quando ti si avvicina, sorride. \"Salve, capitano! Sarebbe disposto a rispondere a qualche domanda per i nostri spettatori?\"",
8: "\"Certo, non mi dispiace.\"",
9: "\"No, preferirei di no.\"",
10: "I droni-fotocamera ti girano intorno mentre lei si prepara all'intervista. Dopo qualche secondo sorride a uno dei droni e comincia.",
11: "\"Bentornati. Sono qui su <origin> per riferire della situazione con le Free Worlds. Mi accompagna un capitano mercantile attualmente tra un viaggio e l'altro. Capitano, cosa pensa dell'ultimatum inviato al Parlamento?\"",
12: "\"Penso che il Parlamento dovrebbe riconsiderare e riflettere un po' sulla situazione.\"",
}

json.dump({str(k): v for k, v in sorted(P.items())},
          open(os.path.join(HERE, 'parts', 'part01.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('part01:', len(P), 'unita', min(P), '-', max(P))
