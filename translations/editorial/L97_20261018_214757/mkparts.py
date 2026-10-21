"""mkparts.py — L97: costruisce `parts/part01-03.json` (36 unita', righe 251-462).

Quinto e **ultimo** lotto di `coalition culture conversations.txt`: chiude il file (157/157).
Sette contesti: `Departing Trouble - A/B/C`, `Incident: Secret Sky`, `Hunger Tower`, `Arach Store`,
`Ring of Wisdom`.

**14 token** da riprodurre identici: `<origin>` x8, `<ship>` x5, `<last>` x1.
**Ripetizione tripla** (unita' 7, 9, 11): stesso inglese, resa identica, da una costante unica.
Le unita' 15 e 17 differiscono per la **virgoletta e la virgola** (`"cooperating,"` contro `"cooperating",`):
sono due unita' distinte e la punteggiatura va riprodotta.
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'parts')

BOARDING = '''Sembrano abbordare le poche navi non danneggiate abbastanza da avere lo scafo squarciato. Dopo pochi minuti sembrano averne preso il controllo e le fanno seguire le navi da guerra fuori dal sistema.'''

P1 = {
 1: '''La vostra nave evita per un soffio alcune piccole navi della Coalizione mentre uscite dall'atmosfera di <origin>. Nemmeno un secondo dopo, mentre siete ancora storditi dallo scampato urto, la <ship> rischia di nuovo di essere colpita da navi in arrivo, questa volta da navi da guerra Heliarch, in quella che sembra un inseguimento serrato alle navi di prima.''',
 2: '''Dopo che sono passate tutte, controllate le comunicazioni e il radar e trovate altre navi civili nei paraggi che sembrano aver provato uno shock simile al vostro. Alcune navi restano sospese sopra <origin> per un po', come se non sapessero cosa fare. Altre scattano via con i motori a piena potenza e lasciano il sistema in un battito di ciglia; altre ancora decidono alla fine di atterrare di nuovo, o troppo curiose della situazione, o forse desiderose di evitare guai.''',
 3: '''Qualche minuto dopo, vedete alcune navi Heliarch fra quelle che vi erano passate vicine lasciare il pianeta. Non vi badano e, con vostro grande sollievo, questa volta mantengono una distanza di sicurezza dalla vostra nave.''',
 4: '''Qualche minuto dopo, vedete alcune navi Heliarch fra quelle che vi erano passate vicine lasciare il pianeta, mantenendo questa volta una distanza di sicurezza dalla vostra nave. Il capitano di una di esse, un Interdictor Heliarch, vi chiama, si scusa per il disturbo di prima e accenna brevemente al fatto che hanno riportato la situazione sotto controllo. Vi augura buona giornata e si prepara a lasciare il sistema.''',
 5: '''Qualche minuto dopo, vedete alcune navi Heliarch fra quelle che vi erano passate vicine lasciare il pianeta. Non vi badano e, con vostro grande sollievo, questa volta mantengono una distanza di sicurezza dalla vostra nave. Non potete fare a meno di chiedervi se le navi che stavano inseguendo portassero membri del Lunarium, o se fossero soltanto altri civili sfortunati.''',
 6: '''Quando siete a buona distanza da <origin>, i sensori vi segnalano pericolo nel sistema: diverse esplosioni e un torrente di proiettili attraversano lo spazio vicino. Vi preparate in fretta alla minaccia, per scoprire poi che sono navi civili della Coalizione a saltare in aria verso il centro del sistema. Alcune navi da guerra Heliarch stanno in mezzo a loro e passano dall'una all'altra, indifferenti ai rottami mentre i vascelli esplodono intorno a loro.''',
 7: BOARDING,
 8: '''Una delle navi vi chiama brevemente, apparentemente di buon umore mentre festeggia la cattura dei criminali. Vi augura buona giornata e buona fortuna nei vostri incarichi, e chiude le comunicazioni mentre si prepara a partire.''',
 9: BOARDING,
 10: '''Mentre date un'occhiata ai rottami delle navi civili, provate un senso di disagio. Peggio ancora è il pensiero che vi colpisce poco dopo: se qualcuno dei capi del Lunarium che avete incontrato fosse a bordo di una di quelle navi.''',
 11: BOARDING,
 12: '''Partite e trovate una specie di schermo di navi da guerra Heliarch intorno a <origin>, che la circondano e si avvicinano a tutte le navi civili in partenza. Non va diversamente per la vostra <ship>, e ben presto venite chiamati da un Punisher Heliarch che si avvicina alla vostra posizione.''',
}

P2 = {
 13: '''"Saluti, Capitano <last>. Un'ispezione di routine, stiamo facendo. Vi abbordiamo tra un momento, per verificare la sicurezza della vostra nave, poi vi lasciamo ai vostri affari."''',
 14: '''Chiudono la comunicazione prima che possiate rispondere, e il Punisher si prepara ad abbordare la <ship>, mentre altre navi da guerra si radunano intorno alla scena. Decine di agenti Heliarch armati entrano in silenzio nella vostra nave e controllano con diligenza le cuccette, la cabina di pilotaggio, la sala macchine...''',
 15: '''In pochi minuti sembrano soddisfatti di aver messo la vostra nave sottosopra, e tornano tutti al Punisher. Vi ringraziano per la "collaborazione," e le navi vi aprono la strada per ripartire.''',
 16: '''Chiudono la comunicazione prima che possiate rispondere, e il Punisher si prepara ad abbordare la <ship> mentre altre navi da guerra si radunano intorno alla scena. Benché non stiate svolgendo alcun incarico per il Lunarium, la preoccupazione cresce mentre il Punisher si avvicina e si collega alla vostra nave. Fate del vostro meglio per mantenere un contegno calmo mentre decine di agenti Heliarch armati entrano in silenzio nella vostra nave e controllano con diligenza le cuccette, la cabina di pilotaggio, la sala macchine...''',
 17: '''In pochi minuti sembrano soddisfatti di aver messo la vostra nave sottosopra, e tornano tutti al Punisher. Vi ringraziano per la "collaborazione", e le navi vi aprono la strada per ripartire. Quando sono abbastanza lontani dalla <ship>, cominciate a setacciarla in cerca di qualcosa che possano aver lasciato per tenervi d'occhio. Molto più tardi nella giornata, dopo aver verificato che non c'è nulla del genere, tirate un sospiro di sollievo.''',
 18: '''Vedete un capitano Arach che si aggira di fretta per lo spazioporto, parlando con chiunque sia disposto ad ascoltarlo. Conversa brevemente con ognuno, mostrando qualcosa in un piccolo monitor, e poco dopo passa al successivo. Dopo un po' arriva a voi.''',
 19: '''"Capitano? Un momento, se siete liberi?" chiede, agitando le zampe per accendere il monitor. Mostra l'immagine di un giovane Kimek. "Un mio passeggero. Fermato qui per far scendere alcuni pellegrini Saryd, ci eravamo, ma dopo averli salutati, ritrovare questo Kimek nella mia nave, non sono riuscito!" esclama, indicando un Transport Arach parcheggiato appena prima del punto in cui la nebbia fitta di <origin> vi toglie la vista. "Visto da qualche parte, l'avete?"''',
 20: '''"Mi dispiace, no. Avete provato a contattare gli Heliarch locali?"''',
 21: '''"Mi dispiace, ma non l'ho visto nemmeno io."''',
 22: '''Annuisce. "Contattati un paio d'ore fa, li avevo. Cercare il mio passeggero nelle sezioni riservate, avrei voluto, ma lì non sono ammesso, quindi ho pensato di chiedere il loro aiuto." Sospira. "Presentato un rapporto e mandato alcuni agenti a cercarlo, l'hanno fatto, ma finora nessuna notizia da loro, non ho ricevuto."''',
 23: '''Vi ringrazia comunque per averlo ascoltato e passa alla persona successiva nello spazioporto per chiedere del Kimek scomparso.''',
 24: '''Lo spazioporto qui su <origin> è nel pieno di un trambusto. Migliaia di Kimek sembrano organizzati in quella che, cosa strana per un mondo della Coalizione, somiglia a una protesta. Alcuni portano dispositivi che ripetono un messaggio in lingua Kimek. Altri tengono cartelli che raffigurano la solita dieta Kimek, con i loro molti raccolti che condividono lo spazio con qualche pesce. La cosa più strana, però, è come gli Heliarch locali stanno gestendo la situazione: sembrano quasi esitanti, parlano ai civili in tono difensivo per cercare di calmarli, a volte si scusano o sono semplicemente costretti ad ascoltare le lamentele mentre diversi Kimek si accalcano intorno a loro.''',
}

P3 = {
 25: '''Quando alla fine riuscite a trovare un Heliarch non impegnato a tenere in ordine la zona, un Saryd, vi spiega la situazione. "Mancato la sua consegna, un convoglio di cibo ha. Ancora indaghiamo sul problema, noi; sappiamo solo che, in qualche modo, scomparsa, l'intera flotta è..." Sospira, scuotendo la testa. "Tenere calmi i locali, dobbiamo." Si allontana ad aiutare gli altri Heliarch, senza aggiungere altro.''',
 26: '''In pochi minuti che agli agenti Heliarch di stanza saranno sembrati ore, battaglioni di droni cominciano a uscire dall'edificio più alto della città: la torre della fame. Trasportando ciascuno diversi pasti, con una precisione impressionante, i droni volano fra la massa dei civili e distribuiscono il cibo. Centinaia di droni più grandi si dirigono verso le zone residenziali, presumibilmente per fornire ai cittadini le scorte necessarie fino all'arrivo del prossimo convoglio. Apparentemente soddisfatti, almeno per il momento, i Kimek si disperdono via via dallo spazioporto verso casa, lasciando lo spazioporto agli agenti Heliarch ormai esausti.''',
 27: '''Una pattuglia Heliarch sembra discutere con un commesso Arach davanti a un grande negozio di abbigliamento Arach dall'aspetto prestigioso, nello spazioporto. Altri agenti impediscono a voi e agli altri presenti di avvicinarvi, ma dai loro gesti riuscite comunque a capire qualcosa. Sembra che gli Heliarch siano lì per confiscare alcuni capi del negozio che, immaginate, non rispettano le loro leggi, mentre il commesso cerca con preoccupazione di rispondere alle domande che gli pongono.''',
 28: '''Alla fine arriva la proprietaria del negozio. A giudicare dai suoi abiti raffinati e dalle reazioni degli Arach del posto, immaginate che sia molto famosa qui su <origin>, o forse che appartenga a una delle Casate Arach, anche se nulla nel suo abbigliamento sembra indicare una Casata precisa. Aiuta il commesso a calmarsi, poi si mette a conversare con gli agenti Heliarch mentre lui rientra nel negozio.''',
 29: '''Cerca di sdrammatizzare, parlando con calma e tentando di riportare i capi dentro il negozio, ma gli agenti Heliarch non cedono. Persa la pazienza, l'Heliarch a capo della pattuglia la interrompe mentre parla, prende con la forza tutti i capi in questione e fa strappare dagli agenti quelle che immaginate essere le parti incriminate dei tessuti. Sbalordita, l'Arach guarda mentre riducono la maggior parte dei capi a stracci inutilizzabili, tenendosi i pezzi che hanno tagliato e restituendole gli altri resti laceri. Senza aggiungere parola, lasciano la scena. L'Arach rientra, e da dove siete potete sentire la porta sbattere.''',
 30: '''Dopo qualche minuto che camminate per lo spazioporto di <origin>, l'illuminazione passa all'improvviso dalle solite tonalità riposanti a una cacofonia di segnalazioni lampeggianti. Messaggi di avviso diagnostico compaiono su ogni tipo di schermo, e le sirene sono interrotte solo da messaggi d'allarme ripetuti in tutte e tre le lingue della Coalizione. Notate che non solo i civili nell'anello sono allarmati come voi, ma ogni agente Heliarch in vista comincia a muoversi a passo frettoloso, anche se ordinato, verso le sezioni riservate, le stanze e i magazzini riservati agli Heliarch.''',
 31: '''Non passa molto prima che centinaia di altri Heliarch arrivino da altre sezioni dell'anello. Quando il flusso finalmente si ferma, li vedete prendere il controllo dei macchinari vicino al bordo della sezione, attivando un'enorme barriera retrattile che isola questa parte dal resto dell'anello. Anche il traffico delle navi viene interrotto del tutto: squadroni Heliarch impediscono a qualunque nave di partire e navi da guerra sbarrano visibilmente gli ingressi degli hangar. Gli Heliarch organizzano i civili in fretta, allontanandoli dalla zona dove si sta radunando la maggior parte degli agenti.''',
 32: '''Mentre anche voi venite sospinti via dagli agenti, riuscite a strappare qualche informazione a uno di loro: una squadra Heliarch che esplorava una delle sezioni sconosciute dell'anello ha avuto una specie di incidente, e uno dei membri dovrebbe tornare nella zona dove si sta radunando la maggior parte degli agenti. Gli Heliarch restano in armi, pronti, con le armi puntate verso una porta che dà alle sezioni riservate e, come resi muti dall'attesa, tutti nella sezione in quarantena sembrano trattenere il respiro.''',
 33: '''In effetti, i molti minuti di silenzio sono rotti da urla che riecheggiano e si fanno sempre più forti: un'unica voce, incessante, che arriva dal passaggio chiuso sorvegliato dalle canne di quello che dev'essere un centinaio di fucili Heliarch. Un tonfo alla porta chiusa si fa strada per un istante fra le grida continue. La porta si apre su un Saryd solo e fuori di sé, con lo sguardo profondamente sconvolto. Non si ferma alla vista delle canne puntate contro di lui: estrae la propria arma e la punta verso il punto da cui è venuto, sparando all'impazzata nel passaggio buio.''',
 34: '''Poi si ferma. Le urla e gli spari cessano di colpo, e il Saryd lascia cadere l'arma e crolla a terra. Resta lì, senza reagire, catatonico, mentre gli agenti Heliarch si avvicinano per esaminarlo e alla fine lo nascondono del tutto alla vista. Qualche secondo dopo alcuni Heliarch indietreggiano e poi corrono verso una stanza riservata. Altri restano saldi di guardia, con le armi puntate verso il Saryd o verso il passaggio da cui è venuto.''',
 35: '''Alla fine arriva una squadra con quello che somiglia vagamente a una barella molto grande e una specie di grosso sacco. Gli agenti Heliarch intorno al Saryd si fanno da parte per lasciar passare chi porta l'attrezzatura e, in pochi minuti, portano via il Saryd, chiuso nel sacco come in un sacco per cadaveri e trasportato sulla barella. A metà strada verso le porte chiuse della sezione si fermano, perché il Saryd si muove in modo irregolare dentro il sacco, scalciando e dimenandosi all'impazzata. Si ferma in pochi secondi, e riprendono la via fuori dalla porzione dell'anello in quarantena.''',
 36: '''Passano diversi minuti prima che gli agenti Heliarch considerino sicuro il passaggio da cui è corso fuori il Saryd; alcune squadre entrano, mentre altre si muovono per riportare la sezione alla normalità. Sollevata la quarantena, quasi tutti i civili corrono alle proprie navi e partono immediatamente.''',
}

src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units']
eng = {u['idx']: u['english'] for u in src}
TAGS = re.compile(r'<[^<>]+>')
for idx, txt in list(P1.items()) + list(P2.items()) + list(P3.items()):
    assert not txt.startswith('\t'), idx
    assert txt.count('\t') == 0, idx
    assert txt.count('"') == eng[idx].count('"'), (idx, txt.count('"'), eng[idx].count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng[idx]), (idx, TAGS.findall(eng[idx]), TAGS.findall(txt))
    assert txt.strip(), idx
assert sorted(P1) == list(range(1, 13)), sorted(P1)
assert sorted(P2) == list(range(13, 25)), sorted(P2)
assert sorted(P3) == list(range(25, 37)), sorted(P3)
assert P1[7] == P1[9] == P1[11] == BOARDING
# unita' 15 e 17 differiscono solo per la virgoletta e la virgola
assert P2[15].split('"')[1] == 'collaborazione,' and P2[17].split('"')[1] == 'collaborazione'

os.makedirs(OUT, exist_ok=True)
for name, d in (('part01.json', P1), ('part02.json', P2), ('part03.json', P3)):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        json.dump({str(k): v for k, v in sorted(d.items())}, f, ensure_ascii=False, indent=1)
print('scritte %d unita (12 + 12 + 12)' % (len(P1) + len(P2) + len(P3)))
