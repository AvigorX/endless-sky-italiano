# -*- coding: utf-8 -*-
# part01: unita' 1-11 (Curious Waiter).
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

P = {
1: "Per un capriccio decidi di cenare in un ristorante lontano dallo spazioporto affollato. Ti ritrovi presto a scorrere un elenco di prelibatezze su un menù cartaceo mentre la gente passa davanti alla vetrina accanto al tuo tavolo, tutti con l'aria provata da una lunga giornata di lavoro. Ordinata presto la cena, continui a guardare la folla finché non arriva, una versione locale del katsu don, e ti metti a mangiare.",
2: "Il locale è silenzioso, forse è ancora presto per l'ora di punta della cena, e sei a metà del pasto quando un cameriere si ferma accanto a te e tossisce per attirare la tua attenzione.",
3: "\"Posso aiutarla?\"",
4: "\"Sì?\"",
5: "\"Cosa vuole?\"",
6: "\"Mi scusi\", dice, afferrando i lembi della camicia. \"Ma... posso chiedere... com'è vedere le stelle? Visitare altri mondi?\"",
7: "\"La maggior parte dei mondi è uguale a questo, o peggio.\"",
8: "\"Le stelle sono più belle sotto un'atmosfera.\"",
9: "\"È un'avventura, ma non per i deboli di cuore.\"",
10: "\"Oh... non ho mai visto nessun pilota, quindi non ho mai potuto chiedere\", dice, un po' abbattuto. \"Grazie mille però per avermelo raccontato!\"",
11: "Torna al suo lavoro, con un'espressione pensierosa di neutra soddisfazione sul viso.",
}

json.dump({str(k): v for k, v in sorted(P.items())},
          open(os.path.join(HERE, 'parts', 'part01.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('part01:', len(P), 'unita', min(P), '-', max(P))
