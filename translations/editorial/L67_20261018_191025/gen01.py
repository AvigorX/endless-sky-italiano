# -*- coding: utf-8 -*-
# part01: unita' 1-17 (Exotic Life: Delve) - comprende l'unico LOGBOOK del file.
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

P = {
1: "Ho sentito parlare di piccole creature chiamate \"teredini di Delve\" che riescono a mangiare lo scafo di una nave. A quanto pare le infestazioni stanno diventando più frequenti.",
2: "L'aria di montagna sa di fresco dopo aver respirato a lungo l'aria sempre riciclata della <ship>, così ti prendi un momento per fare un bel respiro pieno e goderti la vista. Poco alla tua destra, tecnici di terra in tuta sottile e maschere respiratorie stanno spruzzando una specie di sostanza chimica sullo scafo di un Sunder parcheggiato. La nebbiolina sottile riflette un arcobaleno vivido che contrasta in modo sorprendente con il grigio opaco del metallo dello scafo.",
3: "Ti avvicini, attento a non finire troppo vicino allo spruzzo, che supponi tossico. Uno dei tecnici scende da una scala appoggiata allo scafo mentre ti avvicini, poi si volta verso di te e si toglie la maschera, rivelando un uomo dalla pelle scura sulla ventina, con i capelli incollati alla fronte da copiose quantità di sudore.",
4: "\"È la tua nave?\", chiede con un'espressione professionalmente neutra.",
5: "\"No, sono solo curioso. Cosa ci stai facendo?\"",
6: "\"Sì. Come procede il lavoro?\"",
7: "Il tecnico scuote la testa con aria mesta.",
8: "\"È confermato. Teredine. Caso brutto, anche: mi sorprende che il tuo scafo tenesse ancora l'atmosfera.\" Guarda di nuovo il Sunder, misurandolo con gli occhi. \"Dovremmo finire la decontaminazione in un paio d'ore, ma poi dovremo passarla tutta con il sigillante. Probabilmente due mani. Finiremo domani pomeriggio, al più presto.\"",
9: "\"Teredine? Mai sentite.\"",
10: "\"Oh. Va bene, continua.\"",
11: "Ti guarda da capo a piedi, forse chiedendosi se si metterà nei guai a parlarti della nave di un altro capitano, poi alza le spalle e si apre.",
12: "\"Infestazione di teredine. La terza questa settimana.\" Si tira indietro il cappuccio e si passa la mano tra i capelli unti. \"Sinceramente mi sorprende che i media non ne abbiano ancora parlato. Forse aspettano la prima depressurizzazione spontanea per avere qualcosa di davvero succoso di cui parlare.\"",
13: "\"Teredine? Cosa sono?\"",
14: "\"Credi che sia un insabbiamento?\"",
15: "\"Sono piccole creature, grandi più o meno come una capocchia di spillo, e finiscono dappertutto se non stai attento. Si nutrono di un mucchio di metalli diversi, la cosa fa saltare la testa ai cervelloni della scienza. Finora non hanno trovato una lega che questi cosini non riescano a digerire.\"",
16: "\"Come modello di dipendente del Sindacato\", dice sardonicamente, \"posso dirti che le voci secondo cui le teredine sono autoctone di questo pianeta sono false, e che i minatori non le tirano assolutamente fuori dal terreno insieme al minerale. Anzi, se usi anche solo l'espressione 'teredine di Delve' ci sono buone probabilità che gli avvocati del Sindacato ti facciano causa per diffamazione.\"",
17: "Ringrazi il tecnico per la disponibilità e torni verso la <ship>, chiedendoti se non sia il caso di parcheggiarla un po' più lontano.",
}

json.dump({str(k): v for k, v in sorted(P.items())},
          open(os.path.join(HERE, 'parts', 'part01.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('part01:', len(P), 'unita', min(P), '-', max(P))
