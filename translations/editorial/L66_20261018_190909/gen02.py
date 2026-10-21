# -*- coding: utf-8 -*-
# part02: unita' 18-45 (Struggling Author Gone Missing, Exotic Life: Bloodsea).
# NB: l'unita' 34 ha UNA virgoletta dispari nel sorgente: si riproduce, non si chiude.
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

P = {
18: "Mentre la tua nave si posa sulla piattaforma A5B, si avvicinano due giovani. Uno prende la parola: \"Salve, capitano. Ha visto da qualche parte una donna di nome Anna Fangvin? È stata vista l'ultima volta nello spazioporto, e dev'essere partita sulla nave di qualcuno.\"",
19: "Intorno allo spazioporto vedi altri gruppi che fanno la stessa cosa. Anna forse era più popolare di quanto pensasse.",
20: "\"È andata in un altro sistema stellare, molto lontano da qui. Non potrete raggiungerla.\"",
21: "\"No, non lo so. Mi dispiace.\"",
22: "\"Se mai la rivedrà, le dica che la Coalizione degli Amanti dei Libri apprezza il suo lavoro. Non sarebbe possibile per lei portarci da lei?\" Rispondi di no, e i due si dirigono verso gli altri gruppi a spargere la notizia.",
23: "Sui muri di molti spazioporti ci sono manifesti; anche qui, dunque i libri di Anna dovevano essere famosi. I manifesti dicono:",
24: "SPARITA:",
25: "Anna Fangvin, giovane autrice i cui libri sono stati condivisi su tutto il pianeta. Si prega di segnalare qualsiasi notizia alla Coalizione degli Amanti dei Libri, indirizzo 5662 Myrtle Lane, Sizertown, Zug.",
26: "Ti fai lentamente strada nel sudicio spazioporto improvvisato. È pieno di venditori e pirati che contrattano merci illegali. In lontananza il sole tramonta sull'oceano rosso sangue che dà il nome a Bloodsea.",
27: "Nell'ombra dietro una baracca malridotta, sopra la quale un'insegna pubblicizza \"il gas nervino più economico da questa parte del Sol\", vedi un uomo che tossisce. Raschia e rantola per un po', e quando finalmente si riprende noti che ha le labbra macchiate di sangue. Mentre ti volti, incroci lo sguardo di un vecchio incartapecorito al banco accanto.",
28: "Ti fai lentamente strada nel sudicio spazioporto. È pieno di venditori e personaggi loschi che contrattano merci di dubbia provenienza. In lontananza il sole tramonta sull'oceano rosso sangue che dà il nome a Bloodsea.",
29: "Nell'ombra dietro una baracca malridotta, sopra la quale un'insegna pubblicizza \"le granate più economiche da questa parte del Sol\", vedi un uomo che tossisce. Raschia e rantola per un po', e quando finalmente si riprende noti che ha le labbra macchiate di sangue. Mentre ti volti, incroci lo sguardo di un vecchio incartapecorito al banco accanto.",
30: "\"Ha la Fioritura\", sentenzia il vecchio gravemente. \"Sarà morto in poche settimane. È la marea di sangue che lo fa, gli sciocchi.\"",
31: "\"Cos'è?\"",
32: "\"È contagioso?\"",
33: "(Vattene.)",
34: "Ride con disprezzo. \"Il mare spruzza veleno. Nessuno ci va, tranne spaziali e sciocchi. Mare di sangue e sciocchi di sangue.",
35: "\"Sì\", dice semplicemente. Ti ritrai d'istinto dall'uomo che tossisce.",
36: "\"Prima ti prudono gli occhi, poi la gola, poi i polmoni. A quel punto è troppo tardi, troppo tardi. Ma c'è sempre chi non impara.\"",
37: "Sorride con derisione. \"Beh, ti farò a pezzi e ti getterò alla Fioritura se non mi compri del pesce. Tre barili.\" Ficca la mano dentro e tira fuori un pesce. \"Ancora fresco. 1000 crediti l'uno.\"",
38: "(Compra tre barili di pesce da lui.)",
39: "(Compra due barili di pesce da lui.)",
40: "(Compra un barile di pesce da lui.)",
41: "(Scappa.)",
42: "Ti giri di colpo e ti allontani in fretta nella direzione opposta. Senti ancora le imprecazioni nelle orecchie quando arrivi alla nave.",
43: "Tiri fuori i soldi per tre barili e glieli consegni. Li soppesa con sospetto. Quando è soddisfatto, rotoli i barili fino allo spazioporto. Dopo qualche ora estenuante di una trattativa dopo l'altra, riesci a venderli al pannello commerciale dello spazioporto per 2100 crediti.",
44: "Tiri fuori i soldi per due barili e glieli consegni. Li soppesa con sospetto e borbotta qualcosa sull'unico barile rimasto. Rotoli i barili fino allo spazioporto e, dopo un'ora di duro lavoro, riesci a venderli al pannello commerciale per 1400 crediti.",
45: "Tiri fuori i soldi e glieli consegni. Li strofina, poi esplode di rabbia. \"Fuori!\" urla, lanciandoti in faccia i gettoni di credito. Scappi, e quando arrivi alla nave ti rendi conto di aver lasciato 294 crediti con il vecchio nella fretta di fuggire.",
}

json.dump({str(k): v for k, v in sorted(P.items())},
          open(os.path.join(HERE, 'parts', 'part02.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('part02:', len(P), 'unita', min(P), '-', max(P))
