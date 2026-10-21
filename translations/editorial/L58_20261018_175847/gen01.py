# -*- coding: utf-8 -*-
# part01: unita' 1-16 (Sad Gamblers Republic/Syndicate, Foiled Kidnapping, Gift Store, New China Mourners).
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

P = {
1: "Attraversando lo spazioporto vedi un gruppo consistente di persone in attesa di un'estrazione della lotteria. Senti un urlo di gioia, e la tua attenzione è catturata quando uno di loro vince una somma modesta con una vincita di dodicesima categoria. È il valore di uno o due giorni di paga normale.",
2: "È difficile non provare pietà mentre ricomprano subito altri biglietti con l'intera somma.",
3: "Attraversando lo spazioporto vedi un gruppo consistente di persone in attesa di un'estrazione della lotteria. Senti un urlo di gioia, e la tua attenzione è catturata quando uno di loro vince una somma modesta con una vincita di dodicesima categoria. È il valore di uno o due giorni di paga normale.",
4: "È difficile non provare pietà mentre ricomprano subito altri biglietti con l'intera somma.",
5: "Un posto di blocco interrompe il tuo percorso mentre ti avvii verso la città, costringendoti a rallentare al passaggio, abbastanza da capire di cosa si tratta. La polizia fa passare un'auto dopo l'altra provenienti dalla direzione opposta, guardando dentro i veicoli finché uno non viene tirato da parte, il che blocca brevemente tutto il traffico. Il conducente sembra in difficoltà e rifiuta di aprire il bagagliaio anche quando viene fermato; il suo viso diventa pallido quando dentro viene trovata una bambina.",
6: "Non sai bene cosa provare quando la polizia ti fa cenno di andare, togliendoti la vista della scena.",
7: "Mentre giri per lo spazioporto con uno spuntino, aspettando che la nave faccia rifornimento, passi davanti a un negozio di souvenir locale e ficchi la testa dentro per ammazzare un po' il tempo. Vedi una tazza dall'aspetto decoroso con la scritta \"Pace, Prosperità, Progresso\" stampata sotto l'insegna del Deep e la prendi in mano per sentire com'è. Il manico è solido, non troppo piccolo per le tue dita, e il bordo sembra comodo per bere.",
8: "Due giovani adulti entrano nel corridoio a un paio di metri da te, parlando in una lingua che non capisci, forse locale del Deep. Tubano su un oggetto che hanno trovato, ma quando uno lo gira per guardare il cartellino del prezzo c'è uno scambio immediato di sguardi ed espressioni che non ha bisogno di traduzione. L'oggetto torna sullo scaffale fra una risatina e un cenno del capo.",
9: "Curioso, giri anche la tua tazza e vedi che costa davvero almeno cinque volte quello che ti aspetteresti di pagare per una tazza, anche buona: 50 crediti. Comunque è senz'altro una curiosità...",
10: "(Compra la tazza.)",
11: "(Rimettila a posto.)",
12: "Alzi gli occhi al cielo e la rimetti a posto. Certe esperienze sono davvero universali.",
13: "Compri la tazza d'impulso. Almeno puoi buttare quella che hai, che ha una scheggiatura.",
14: "Curioso, giri la tua tazza e quando vedi il cartellino di 50 crediti ti si stringe il cuore. Non potresti mai permetterti una tazza così costosa. La rimetti a posto e ti allontani riflettendo sulla tua situazione finanziaria.",
15: "Il cielo si rovescia sul mondo sotto, piangendo insieme alla folla mentre una bara semplice ma imponente viene portata lentamente fuori da un pianterreno aperto. Un lamento ritmico si mescola alla pioggia sussurrante e riempie l'aria, mentre la bara è seguita da vicino da un corteo di persone in lutto che sembra un raduno esteso di famiglia. Anche quando viene sistemata nel furgone non lasciano il defunto: molte mani si posano su di essa come per spingere la persona verso il suo ultimo riposo. I due in lutto più avanti, una donna e un giovane, salgono e prendono posto accanto alla bara. Da qualche parte vicino comincia la musica, mentre il veicolo si muove lentamente.",
16: "Ti chiedi quanto fosse conosciuta la persona prima di morire, mentre quelli rimasti si voltano infine dal furgone che si allontana e cominciano a passare davanti ad alcuni addetti discreti che non avevi notato subito, accettando pantofole per i piedi scalzi prima di salire sugli autobus che li porteranno dietro al furgone.",
}

json.dump({str(k): v for k, v in sorted(P.items())},
          open(os.path.join(HERE, 'parts', 'part01.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('part01:', len(P), 'unita', min(P), '-', max(P))
