"""mkparts.py — L94: costruisce `parts/part01-03.json` (36 unita', righe 81-133).

Secondo lotto di `coalition culture conversations.txt`, contesto `Coalition Folklore: Arach`.
**Il parlato degli Arach ha la stessa sintassi invertita dei Saryd** («appreciate the fine arts, do you?»):
si riproduce con ordine marcato italiano, non si normalizza.

Ripetizioni dichiarate: `(Stay for the next play.)` alle unita' 16 e 22, `(Leave.)` alle 17, 23 e 29 —
l'inglese e' identico, la resa deve esserlo.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'parts')

STAY = '''(Resta per il prossimo spettacolo.)'''
LEAVE = '''(Vai via.)'''

P1 = {
 1: '''Poco dopo il vostro ingresso nello spazioporto, notate un'Arach in quello che immaginate essere un "abito" formale: un delicato drappo di seta che le copre gran parte del corpo, con ogni zampa avvolta in una gonna ricamata. Grida qualcosa a voce alta in un dispositivo di comunicazione personale, poi lo ripone con uno scatto. Come tutti quelli che l'hanno vista per un istante, cercate di distogliere lo sguardo, ma l'Arach si è già guardata intorno, vi ha visti e si è subito avvicinata. "Nostro onorevole visitatore umano, saluto", dice a voce alta mentre colma la distanza. "Dica, Capitano, apprezzate le belle arti, voi? A una serata culturale sono diretta, ma occupato dal lavoro il mio caro papà è, quindi vuoto il suo posto riservato è. Mi accompagnate, volete?"''',
 2: '''"Di che evento si tratta?"''',
 3: '''"In questo momento ho da fare, quindi passo."''',
 4: '''"Non un semplice ritrovo, ma una raccolta di opere di professionisti stimati, completata da un'orchestra dedicata, la serata è", spiega. "Una celebrazione del folklore Arach, è, a cui nei nostri abiti migliori noi patroni locali partecipiamo. Trasmesso in diretta per gli altri, lo spettacolo è anche, ma paragonarsi all'esecuzione dal vivo, non può."''',
 5: '''"Va bene, mi interessa. Dove si tiene questa 'serata'?"''',
 6: '''"Il teatro non mi appassiona, mi dispiace."''',
 7: '''La seguite attraverso la parte centrale della città fino a un edificio che dall'esterno sembra una specie di auditorium; lì alcuni Arachi in uniforme controllano gli ingressi dei "patroni" dell'evento. "Un umano? Un ospite piuttosto esotico, avete portato, signora Matlub", dice uno di loro alla vostra guida mentre lei gli mostra un touchpad con due biglietti. Lui li verifica e vi lascia entrare. L'interno vi ricorda un teatro d'opera: un grande palco davanti a decine di file di poltrone e sei ordini di balconate su entrambi i lati. Matlub vi conduce a due ottimi posti in una delle prime file e vi aiuta a "regolare" la poltrona perché stiate più comodi. Subito davanti al palco c'è una zona qualche gradino sotto il livello dei posti, con alcuni musicisti Arach che accordano strumenti diversi. Sul soffitto e su tutte le balconate vedete piccole telecamere puntate verso il palco, per trasmettere l'evento a chi non ha potuto assistervi dal vivo.''',
 8: '''Mentre file e balconate si riempiono di altri ospiti, notate qualche Kimek e qualche Saryd fra le masse di Arach; quasi tutti accompagnano un patrone Arach, qualcuno sembra essere a sua volta patrone, entrato da solo. Molti di loro vi notano mentre vi guardate intorno, ma la vostra patrone ignora l'attenzione con studiata indifferenza.''',
 9: '''"Capisco perché ne parlavate con tanto entusiasmo: sembra un evento davvero ben organizzato."''',
 10: '''"Non capita tutti i giorni che si veda un umano a una serata così, immagino?"''',
 11: '''Annuisce. "Un evento prestigioso, questo è. Portare amici da tutta la Coalizione a vedere, i patroni lo fanno. L'ospite più singolare che abbiamo avuto, voi siete."''',
 12: '''Quando tutti i posti sono occupati, le porte si chiudono e un Arach sale sul palco. "Accogliervi, stimati ospiti, a questa celebrazione di saga e canto, il nostro teatro ha il piacere di", dice. "Farvi aspettare ancora, non voglio, quindi per la nostra prima opera, un classico senza tempo caro a tutti, vi presento: Toccato dalla Luna."''',
}

P2 = {
 13: '''Esce rapidamente di scena mentre il sipario si apre su una parete rocciosa con due gallerie laterali. L'orchestra comincia a suonare un tema lento e dolce su strumenti simili a fisarmoniche, e un giovane Arach entra in scena dalla galleria di sinistra. Si tiene aggrappato alla parete rocciosa, con una piccola lanterna appesa all'addome e un grosso sacco legato sulla schiena. Poi stacca pietre dagli angoli della parete, gettandone la maggior parte a terra ma mettendone alcune nel sacco che porta. Quando il sacco è pieno, entra nella galleria di destra e la parete rocciosa ruota per mostrare l'altro lato; lì il giovane minatore è mostrato sotto il cielo notturno mentre fonde il minerale raccolto. Mentre guarda verso l'alto del palco con la schiena rivolta al pubblico, le fisarmoniche si fanno più sommesse, un'arpa comincia a suonare lentamente e una luna piena compare in cima allo sfondo del cielo.''',
 14: '''Il sipario si chiude mentre la scena cambia, e si riapre con le fisarmoniche che accelerano. L'Arach è ora su una parete più grande, con una sola galleria in alto. Graffia via gli angoli rocciosi e le fisarmoniche seguono il suo ritmo. Quando ha estratto quasi tutto il minerale, la parete comincia a tremare, come se la miniera stesse crollando. Le fisarmoniche diventano irregolari mentre lui si precipita verso la galleria di fuga. Con un clamore febbrile, la parete rocciosa sembra smontarsi sul palco: grandi massi scendono con grazia dalla torre scenica e fanno crollare la miniera. Le fisarmoniche tacciono, ma dopo una lunga pausa riprendono piano, insieme all'arpa. Il giovane Arach emerge allora alla vista e spinge via un masso, poi un altro, poi un altro ancora. Va avanti così finché l'Arach non si ritrova in cima a una montagna di metallo scavata nella roccia, con la mano tesa verso la luna. Quando quasi la tocca, il sipario si chiude e la musica si ferma.''',
 15: '''Gli Arachi del pubblico strofinano due zampe l'una contro l'altra, come per applaudire alla fine dello spettacolo. Poco dopo alcuni si alzano e si dirigono verso l'uscita, mentre le porte si riaprono. Nello stesso tempo altri patroni entrano per occupare i posti rimasti vuoti. "Interessati solo ad alcune opere, alcuni patroni sono, quindi solo per quelle che vogliono vedere, restano", spiega Matlub. "Andare via dopo qualsiasi esecuzione, potete, se altrove dovete essere, ma restare per il resto dello spettacolo, io lo farò."''',
 16: STAY,
 17: LEAVE,
 18: '''Quando tutti sono seduti, lo stesso Arach di prima torna sul palco. "Una sorpresa per voi, stasera abbiamo. Un'opera nuovissima, commissionata da un gruppo anonimo di patroni. Una critica a una delle questioni che ancora permangono nella nostra società, descritta è. Per la nostra seconda opera: Bebliss Balbettante."''',
 19: '''Mentre esce, il sipario si apre su una scenografia di strada Arach, dove un piccolo sta comprando una specie di dolciume. Da dietro un edificio della scena emerge un Arach che indossa alti "calzini" blu e bianchi, mentre trombe e tube attaccano un motivo fastidioso. Corre verso il piccolo e gli fa cadere i dolci a terra emettendo una specie di gorgoglio. Matlub sospira: "Un garbuglio, è. Insensatezze, e parole che è meglio non tradurre." L'attore Arach continua aggrappandosi alle pareti dell'edificio e prendendo cose dalla bottega di dolci, gettandole all'impazzata. Ormai molti patroni ben vestiti, probabilmente membri di Casa Bebliss, si alzano e lasciano il teatro. Nel frattempo un gruppo di Arach su una delle balconate non cerca nemmeno di soffocare le risate.''',
 20: '''La scena continua con una coppia che arriva in scena camminando lungo la strada. Mentre stanno per chinarsi in quello che sembra un bacio, l'Arach salta dall'edificio e atterra sul giovanotto con un tonfo. Ruba il bacio, mentre tube e trombe soffiano con tutta la loro forza. Dopo un po' arrivano le autorità, e l'Arach se la dà a gambe lungo la strada. L'orchestra suona un motivo tanto scoordinato quanto i suoi movimenti, e il sipario si chiude. Non molti in platea si esprimono: quasi tutti sospirano o si preparano ad andarsene, tranne il gruppo che rideva prima, che ora proclama a voce alta il proprio apprezzamento. "Di sottigliezza, Casa Chamgar non ne ha", dice Matlub. "Un peccato, è, che abbiano sporcato la serata con questa rivalità."''',
 21: '''Le porte si riaprono mentre nuovi patroni entrano per la terza opera.''',
 22: STAY,
 23: LEAVE,
 24: '''Tutti prendono posto e l'annunciatore Arach torna sul palco. "Una tragedia catartica, la nostra terza opera di questa sera è. Per la prossima rappresentazione: Fino alla Morte."''',
}

P3 = {
 25: '''Le luci del palco si spengono mentre il sipario si apre su un solo riflettore, che illumina un vecchio Arach che si veste dentro una piccola baracca sul lato destro della scena. Tossisce, e qualcosa di simile a un organo comincia a suonare una melodia malinconica. Quando esce, la baracca resta al buio e il riflettore lo segue al centro del palco, dove percorre con cautela una strada vuota. Gli è consentito oltrepassare il riflettore, che si spegne mentre la prospettiva cambia e un secondo riflettore rinnova la messa a fuoco. Il lato sinistro del palco si illumina finalmente: lì l'Arach comincia a curare un giardino davanti all'ingresso di una villa. L'organo interrompe il suo pianto ogni tanto, proprio quando l'Arach tossisce, per riprendere appena ha finito. Uscendo dalla villa, un Arach vestito con ricchezza indica uno dei fiori del giardino, mostrando che è avvizzito e morto. Lo coglie, lo getta a terra e se ne va. Il giardiniere raccoglie il fiore, se lo infila nei vestiti e riprende il suo lavoro.''',
 26: '''Finito il lavoro, torna alla sua baracca, e i riflettori lo seguono mentre si muove per il palco. Una volta dentro, fruga in una piccola cassetta, prende un vaso semplice e ci mette il fiore. Il palco si oscura mentre si corica e il pianoforte tace; solo qualche colpo di tosse riecheggia nel teatro. Quando la luce torna sulla baracca, l'Arach si alza lentamente ed esce di nuovo per il suo lavoro, fermandosi un momento nella parte del palco che è la strada durante un accesso di tosse violento. Finito il lavoro, mentre comincia a tornare a casa, ricomincia a tossire senza tregua, senza pause di più di un secondo. Intanto i riflettori passano alla sezione successiva del palco e il pianoforte suona una breve nota. Entrato nella baracca, crolla a terra rovesciando il vaso del fiore. Il pianoforte suona qualche accordo lento e l'ultimo riflettore si spegne sull'ultima nota.''',
 27: '''Sentite il sipario che si chiude e le luci del teatro si riaccendono mentre il pubblico è preso da un applauso. Quando si calma, l'annunciatore sale di nuovo sul palco. "E con questo, conclusa, la nostra serata è. Ringraziarvi tutti per averci onorato della vostra presenza, io, a nome del teatro, voglio." Abbassa il capo in un inchino e lascia il palco mentre quasi tutti i patroni in sala si alzano e si dirigono verso l'uscita; questa volta nessuno entra a occupare i posti. Nello stesso tempo l'orchestra comincia a riporre gli strumenti. Alcuni, però, restano seduti, compresa Matlub.''',
 28: '''(Resta.)''',
 29: LEAVE,
 30: '''Ringraziate Matlub per l'invito e, anche se non sembra darvi molto peso, sentite gli sguardi degli altri patroni Arach su di voi, che sussurrano fra loro mentre ve ne andate.''',
 31: '''I tecnici del teatro escono uno dopo l'altro, lasciando voi e gli altri ospiti davanti a un palco vuoto. Dopo un po' le luci si spengono. Un paio di minuti più tardi, però, sentite il sipario che si apre, mentre alcuni violini cominciano a suonare all'unisono. La loro musica non viene da dove era seduta l'orchestra, ma come se fosse diffusa in tutto il teatro, dietro di voi e perfino sulle balconate. Una luce forte arriva dal palco, in gran parte bloccata da un'alta figura scura. Non è un attore: sembra fatta di parti di legno tenute su da fili sottili che riuscite appena a scorgere guardando la sommità del palco. Il canto dei violini è interrotto da colpi di tamburo sordi e successivi, e a quel punto la figura si muove, con le "braccia" che si aprono ai lati; diventa ancora più alta mentre si alza in piedi. È una creatura umanoide, e comincia a muoversi lentamente per il palco, come se danzasse su un pendolo. I violoncelli si uniscono alle urla dei violini e poi entra un coro, le cui parole non riuscite a capire. Riconoscete però che non sta cantando in nessuna lingua della Coalizione.''',
 32: '''La creatura sembra avvicinarsi al pubblico, crescendo di dimensioni, e mentre coro e strumenti diventano più intensi, alza un braccio e stacca i fili. Nonostante questo resta in piedi e continua a muoversi. Avvicina entrambe le braccia e colpisce la propria testa formando due piccoli fori da cui passa la luce dello sfondo. Poi cade in ginocchio, con un braccio teso verso il pubblico, mentre la luce dietro di essa si spegne e coro e musica si attenuano.''',
 33: '''Le luci si riaccendono e rivelano il sipario ancora aperto, ma il palco vuoto. Qualche tecnico entra per riordinare, e gli ospiti rimasti si alzano per andarsene. "La serata vi è piaciuta, Capitano?", chiede Matlub, alzandosi a sua volta per andare. "Venite, ora: davvero finito, lo spettacolo adesso è."''',
 34: '''"Che diavolo era quella cosa?"''',
 35: '''"Se è finito solo adesso, perché quell'annunciatore è salito dopo la terza opera per congedare gli ospiti?"''',
 36: '''Non risponde e si dirige dritta verso l'uscita. La seguite fuori e lei vi guida di nuovo alla vostra nave. "Grata che mi abbiate accompagnata, io sono, Capitano. Buon viaggio, possiate avere."''',
}

src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units']
eng = {u['idx']: u['english'] for u in src}
for idx, txt in list(P1.items()) + list(P2.items()) + list(P3.items()):
    assert not txt.startswith('\t'), idx
    assert txt.count('\t') == 0, idx
    assert txt.count('"') == eng[idx].count('"'), (idx, txt.count('"'), eng[idx].count('"'))
    assert txt.strip(), idx
assert sorted(P1) == list(range(1, 13)), sorted(P1)
assert sorted(P2) == list(range(13, 25)), sorted(P2)
assert sorted(P3) == list(range(25, 37)), sorted(P3)
assert P2[16] == P2[22] == STAY and P2[17] == P2[23] == P3[29] == LEAVE

os.makedirs(OUT, exist_ok=True)
for name, d in (('part01.json', P1), ('part02.json', P2), ('part03.json', P3)):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        json.dump({str(k): v for k, v in sorted(d.items())}, f, ensure_ascii=False, indent=1)
print('scritte %d unita (12 + 12 + 12)' % (len(P1) + len(P2) + len(P3)))
