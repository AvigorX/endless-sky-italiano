# -*- coding: utf-8 -*-
# part01: unita' 1-17 (Exotic Life: New Greenland, Exotic Life: Mainsail).
# NB: l'unita' 10 ha UNA virgoletta dispari nel sorgente: si riproduce, non si chiude.
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

P = {
1: "Scendi sulla piattaforma di atterraggio e il tuo fiato forma un alone bianco. Lo spazioporto è insolitamente nebbioso, e il vento gelido ti fa correre un brivido alla base della nuca.",
2: "Dalla nebbia emerge un uomo incartapecorito, con un'andatura tranquilla e senza fretta, un fucile laser a tracolla. Al suo fianco avanza pesante una bestia enorme: un segugio grande come un cavallo, avvolto in una folta pelliccia lanosa orlata di brina. Due zanne enormi gli sporgono dal muso come sciabole pallide. Il vapore esce a ondate dalle narici dilatate mentre gira la testa quasi con pigrizia verso di te. I suoi occhi hanno una pazienza cupa.",
3: "L'uomo ti vede e grugnisce: \"Non fissare un Mastino Mammut.\"",
4: "\"Cos'è un Mastino Mammut?\"",
5: "\"Non dirmi cosa devo fare!\"",
6: "(Distogli lo sguardo e torna alla mia nave.)",
7: "\"Un fantasma di tempi più duri, allevato su Hestia quando era ancora ghiaccio senza vita. Ora non è più che uno strumento del mestiere.\" Dà una pacca alla creatura, che emette un ringhio basso.",
8: "L'uomo scoppia in una risata profonda mentre la nebbia si infittisce. Gli occhi della creatura sono l'ultima cosa che trapassa la foschia prima che uomo e mastino svaniscano. Ti ritrovi di nuovo solo.",
9: "Ti reggi sulla città-nave galleggiante mentre la collana di chiatte, moli e gru scricchiola e ondeggia sotto l'influsso delle onde senza fine di Mainsail. Lo spruzzo salmastro ti punge il viso mentre ti dirigi verso l'anello. Una chiatta si avvicina ondeggiando, la coperta viscida di alghe, mentre un locale passeggia senza paura al guinzaglio una creatura quadrupede simile a una balena: una massa compatta di muscoli grande come una foca sotto un pelo ardesia, con zampe palmate che ticchettano sulle assi, un lungo muso baffuto irto di denti aghiformi e una larga coda appiattita che scodinzola di aspettativa.",
10: "Il locale ti coglie a fissare, abbozza un sorriso segnato dal sale e chiama: \"Non hai mai visto un cane di mare?",
11: "\"Non posso dire di sì!\"",
12: "\"Cos'è quella cosa?\"",
13: "\"Certo che ho già visto un cane di mare!\"",
14: "(Distogli lo sguardo e torna alla mia nave.)",
15: "\"Ah, quello, amico mio, è un Cane di Mare di Mainsail, il miglior segugio acquatico dei Mondi del Paradiso. Allevati circa quattro secoli fa negli atelier di questo stesso pianeta, uniscono vecchi ceppi di cani d'acqua con sangue di delfino e di lontra, con un tocco di castoro per la coda, di coccodrillo per le mascelle e di barracuda per lo scatto\", dice con un occhiolino. \"Fiutano un banco, tirano su il pesce migliore e ti posano una testa umida e riconoscente sugli stivali: una rarità pregiata, da quando la Repubblica ha chiuso i laboratori genetici.\"",
16: "\"Sono contento di sentirlo, amico mio! Oggi troppo pochi hanno visto la rarità pregiata di un Cane di Mare di Mainsail, da quando la Repubblica ha chiuso i laboratori.\"",
17: "Con un movimento esperto salta dalla chiatta su uno skiff snello e senza motore. Il cane di mare scivola dalla chiatta come un nastro, si tuffa pulito in mare e mette la larga coda alle onde. In uno spruzzo di sale la creatura d'acciaio li trascina via, e la barca si allontana come un carro di Poseidone nella foschia del porto.",
}

json.dump({str(k): v for k, v in sorted(P.items())},
          open(os.path.join(HERE, 'parts', 'part01.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('part01:', len(P), 'unita', min(P), '-', max(P))
