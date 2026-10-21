# -*- coding: utf-8 -*-
# part05: unita' 141-171 (ramo "epilogo b" + i due dialog finali, chiude il segmento).
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

P = {
141: "\"Allora non c'è modo che io possa lavorare con i Gegno?\"",
142: "\"Immagino che dovrei lasciarli stare.\"",
143: "dont know",
144: "\"Certo che no. Tollerare significa autorizzare un accadimento senza restrizioni nonostante una premessa indesiderata. In questo non sta l'interesse dei Gegno, come ho già detto una volta.\" Guarda in alto pensieroso per diversi momenti. \"Forse nel tuo giudizio ingenuo mi sbaglio. Gli umani tollerano i propri indesiderabili, quelli divenuti noti come corsari. Parti della tua specie ne permettono le azioni moleste, altre no. Ciò nonostante, supponi che una specie diversa dall'umanità cominci un'agitazione simile. Presumerei che il caso sarebbe diverso.\" Adrauni comincia allora una conversazione con gli altri Quarg nella stanza.",
145: "\"Stai dicendo che non c'è modo che io possa lavorare con i Gegno?\"",
146: "\"Immagino che dovrei lasciarli stare.\"",
147: "upset",
148: "\"Evidentemente sì, visto che quelli dei Vi sono entrati sfrontatamente nel nostro anello. Una dimostrazione di forza è del tutto inaudita, ancor più in opposizione ad altri mezzi di comunicazione meno immodesti. Avevo la minima speranza che tu avessi compreso i miei ammonimenti sulla non violenza, perché credo che ci sia beneficio nelle aspirazioni ottimistiche delle specie più giovani, ma alla fine le mie speranze si sono rivelate infondate.\" Alcuni degli altri Quarg nella stanza si rivolgono bruscamente ad Adrauni come se tu non fossi presente e cominciano un lungo periodo di dibattito, punteggiato ogni tanto da occhiatacce nella tua direzione.",
149: "\"Allora non c'è modo che io possa lavorare con i Gegno?\"",
150: "\"Immagino che dovrei lasciarli stare.\"",
151: "no idea",
152: "\"Sì, credo che sia un tema ricorrente in questa situazione superflua. È una pratica piuttosto pericolosa compiere un atto prima della conoscenza, come noi Quarg consigliamo da molti anni a voi impulsivi umani. Nelle nostre discussioni con voi è evidente che questo si è dimostrato vero. Tuttavia i grandi limiti superati qui vanno oltre ciò che possiamo permetterci di accogliere.\" Adrauni cambia leggermente espressione, fulminandoti di nuovo. \"Soprattutto dopo continui avvertimenti precedenti.\" Uno degli altri Quarg nella stanza dice qualcosa ad Adrauni, che avvia una conversazione nella propria lingua.",
153: "\"Allora non c'è modo che io possa lavorare con i Gegno?\"",
154: "\"Immagino che dovrei lasciarli stare.\"",
155: "work",
156: "Restate seduti in silenzio per un tempo scomodo, durante il quale persino i Quarg non si parlano. La strana struttura e le luci brillanti della stanza ti rassicurano poco mentre i Quarg riflettono tra sé. Qualche momento dopo ricominciano a parlare tra loro, ma non hai occasione di dire una parola. Dopo diversi altri minuti di discussione e sguardi strani, gli altri Quarg si alzano e ti affiancano da entrambi i lati, mentre Adrauni finalmente ti si rivolge di nuovo. \"Purtroppo, a questo punto degli eventi, né io né i Quarg possiamo darti una risposta alla tua richiesta. Siamo concordi nella nostra ferma opposizione a ulteriori interazioni tra te e i Gegno.\" Poi fa quello che pensi sarebbe l'equivalente Quarg di un sospiro.",
157: "alone",
158: "Restate seduti in silenzio per un periodo scomodo, durante il quale persino i Quarg non si parlano. La strana struttura e le luci brillanti della stanza ti rassicurano poco mentre i Quarg riflettono tra sé. Qualche momento dopo ricominciano a parlare tra loro, ma non hai occasione di dire una parola. Dopo diversi altri minuti di discussione e sguardi strani, gli altri Quarg si alzano e ti affiancano da entrambi i lati, mentre Adrauni finalmente ti si rivolge di nuovo. \"Certo, quella affermazione è nelle nostre più forti preferenze per questa faccenda.\" Si alza e incrocia le braccia dietro la schiena. \"Anche se suppongo che tu ed io immaginiamo che sia... improbabile.\"",
159: "visit b",
160: "La porta si apre alle tue spalle e i Quarg ti fanno cenno di seguirli di nuovo, scortandoti fuori dalla stanza e riportandoti all'hangar dove è parcheggiata la tua nave. Sembrano esserci più Quarg del solito nei corridoi, alcuni di stanza presso vari ingressi. Non puoi fare a meno di ricordare che questa è solo una piccola parte dell'anello, il che rende il resto ancora più incomprensibilmente grande e pieno di Quarg. Tornato all'hangar, trovi la vista dei guerrieri Vi bloccati da un gruppo più numeroso di Quarg, anche se non sembrano esserci intenzioni ostili, né conversazione, da nessuna delle due parti. Adrauni si ferma allora davanti a te. \"Non è più nella nostra giurisdizione assisterti in questo. Tuttavia, se davvero continui a perseguire questo desiderio di avere a che fare con i Gegno, devi cercare udienza da solo. Visita il mondo natale dei Gegno, Dueyu Eitch, e presentati nel modo in cui desideri essere percepito. Solo allora troverai risposta ai tuoi capricci.\"",
161: "epilogue b",
162: "\"Non mi impediranno di atterrare?\"",
163: "\"Non potevamo semplicemente chiedere a quel Gegno là?\"",
164: "\"Me ne andrò ora.\"",
165: "Dopo una pausa Adrauni risponde. \"Al contrario, credo piuttosto che ti stiano aspettando, considerate le loro esclamazioni sulla situazione.\"",
166: "there",
167: "\"Quelli dei Vi non rappresentano quelli dei Gegno, cioè di un'intera specie. I Vi qui presenti sono solo di una famiglia, e di gruppi simili ce ne sono molti.\" Adrauni considera la tua domanda per qualche momento, quasi sembrando provarne un lieve interesse. \"È diverso da ciò a cui voi umani siete abituati. La cultura Vi non designa una famiglia solo per discendenza o familiarità.\"",
168: "end b",
169: "\"Per quanto le tue azioni finora siano insoddisfacenti, aspiro a che le decisioni future si addicano ai saggi nel cammino che ti attende. Ti auguro un viaggio istruttivo, <first> <last>.\" Adrauni ti fa un lungo inchino, poi lascia l'hangar. Hai la sensazione che questa possa essere stata l'ultima volta che lo incontri. Mentre torni alla nave, i guerrieri Vi continuano a osservare da lontano, ma i Quarg li bloccano con fermezza. Tocca a te capire se i Gegno ti tollereranno ancora.",
170: "Dopo aver deciso di aprire il fuoco sulla flotta Gegno che sorvegliava la tua visita al loro mondo natale, ti trovi davanti a un'opposizione aggressiva e a quelle che suonano come innumerevoli chiamate furiose. Qualsiasi possibilità ti restasse di avere a che fare con i Gegno è ora svanita.",
171: "Dopo aver deciso di aprire il fuoco sulla flotta Gegno che sorvegliava la tua visita al loro mondo natale, ti trovi davanti a un'opposizione aggressiva e a quelle che suonano come innumerevoli chiamate furiose. Qualsiasi possibilità ti restasse di avere a che fare con i Gegno è ora svanita.",
}

json.dump({str(k): v for k, v in sorted(P.items())},
          open(os.path.join(HERE, 'parts', 'part05.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('part05:', len(P), 'unita', min(P), '-', max(P))
