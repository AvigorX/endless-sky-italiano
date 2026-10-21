# -*- coding: utf-8 -*-
# part01: unita' 1-29 (Tarazed Ship Christening).
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

P = {
1: "Mentre passi davanti a diverse navi e a equipaggi al lavoro nello spazioporto, un piccolo capannello davanti a uno Shuttle attira la tua attenzione. Una giovane donna con un'uniforme da pilota piuttosto pacchiana è al centro di un gruppetto di persone che festeggiano insieme. Mentre passi, un uomo in piedi in cima a una scala rompe una bottiglia di champagne sullo scafo della nave (chiaramente non nuova). Dal gruppo esplode un grido di esultanza, che fa arrossire la giovane donna per l'imbarazzo.",
2: "(Guardare più da vicino.)",
3: "(Gridare gli auguri mentre passo.)",
4: "(Ignorarli, ho cose più importanti da fare.)",
5: "Ti affretti oltre il gruppo chiassoso, infastidito dal trambusto.",
6: "pass by",
7: "Ti affretti oltre il gruppo mentre si calmano. Approfittando della pausa momentanea, gridi verso di loro: \"Buona fortuna! Ce la puoi fare!\" Rispondono con un altro grido di esultanza, tranne la giovane donna, che si copre il viso con le mani.",
8: "Ti avvicini al gruppo mentre si calmano, notando un accenno di ansia nell'aria.",
9: "\"Non c'è niente come comprare la propria prima nave stellare\", dici sopra le loro chiacchiere. Il festeggiamento si spegne mentre si voltano a vedere chi ha interrotto la loro piccola festa.",
10: "\"È stata senz'altro un'esperienza...\", risponde la giovane donna quando sei a distanza comoda per parlare.",
11: "\"Hai programmi importanti con la nave?\"",
12: "(Dare qualche consiglio.)",
13: "\"Allora, chi è il pilota fortunato?\"",
14: "Indichi lo Shuttle e ti guardi intorno come se dovesse essere qualcun altro.",
15: "\"Ehm... sarei io\", dice la donna, guardandosi intorno con imbarazzo.",
16: "(Provare a salvare la situazione imbarazzante.)",
17: "(Andarsene finché posso.)",
18: "\"Ti sto solo prendendo in giro; anche il mio psichiatra non la trova divertente quando lo faccio a lui.\"",
19: "\"Oh\", dice la donna piano, \"che... carino, credo.\"",
20: "get out",
21: "Ti rendi conto di aver messo parecchio a disagio questa giovane signora piombandole addosso con il tuo parere.",
22: "\"Beh, buona fortuna!\", dici con un cenno della mano mentre ti allontani in fretta. Senti a malapena il \"grazie\" sommesso sopra il bruciore alle orecchie.",
23: "\"Al momento\", dice con un sospiro, \"l'unico programma che ho è liberarmi del debito enorme in cui sono per colpa sua.\"",
24: "\"Il mutuo non è così terribile se sei disposta a lavorare sodo\", dici con un sorriso, \"e non mancano di certo le persone che hanno bisogno di una nave e di un buon pilota.\"",
25: "\"Sapevo che con una nave si può vivere decentemente, ma è davvero così facile?\", chiede.",
26: "\"Il lavoro non è facile, ma trovare un impiego è il minore dei tuoi problemi. Sono sicuro che estinguerai il debito della nave in men che non si dica.\"",
27: "Resti lì a parlare con l'aspirante pilota per qualche minuto, dandole consigli e suggerimenti, prima di dire che hai del lavoro da fare. Mentre ti volti per andartene, un uomo più anziano ti mette una mano sul braccio e ti ferma.",
28: "\"Prima che vada\", dice l'uomo, \"all'inizio non eravamo molto convinti di tutta questa faccenda del 'pilota', ma è bello sentire che mia figlia ha preso la decisione giusta. Grazie per questo.\"",
29: "\"È il minimo che potessi fare\", dici prima di allontanarti.",
}

json.dump({str(k): v for k, v in sorted(P.items())},
          open(os.path.join(HERE, 'parts', 'part01.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('part01:', len(P), 'unita', min(P), '-', max(P))
