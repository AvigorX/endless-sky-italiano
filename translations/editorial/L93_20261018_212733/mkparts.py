"""mkparts.py — L93: costruisce `parts/part01-03.json` (31 unita', righe 24-66).

Primo lotto di `coalition culture conversations.txt`. **Il parlato dei Saryd ha sintassi invertita** nel
sorgente («choose your path, you must», «That you enjoyed the spectacle, I hope»): e' caratterizzazione della
specie e si riproduce con un ordine marcato italiano, non si normalizza.

Le stringhe NON contengono tab iniziali (li antepone `check.py`). Le unita' 15, 20 e 25 hanno lo stesso
inglese (la descrizione del palco nei tre sentieri) e la stessa resa.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'parts')

STAGE = '''La luce che avevate visto si rivela un falò accanto a un palco di legno, grande circa un terzo dei palcoscenici d'opera umani, e trovate posto su uno dei tronchi disposti vicino al fuoco. Diverse luci illuminano il palco e, alzando lo sguardo, riuscite appena a scorgere alcuni riflettori nascosti in alto fra gli alberi. Quando il pubblico è radunato, il sipario si apre e rivela molte piccole figure fatte di quello che sembra carta, in uno stile che ricorda alla lontana gli origami. Sono sostenute da sottili aste di legno dal basso o da fili dall'alto. Alcune figure sono vicine al punto in cui era il sipario, altre più in fondo al palco: i vari strati danno profondità alla scena. Dopo un breve momento, lo spettacolo comincia:'''

P1 = {
 1: '''Attraversando lo spazioporto, venite avvicinati da un Saryd vestito in modo insolitamente tradizionale, anche per gli standard Saryd. Vesti di seta non troppo diverse dai kimono umani gli coprono gran parte del corpo, e sottili corde stringono saldamente il tessuto vicino agli zoccoli.''',
 2: '''"Salute, Capitano. Interessati a partecipare a una celebrazione culturale, sareste?" chiede.''',
 3: '''"Che tipo di celebrazione?"''',
 4: '''"Mi dispiace, in questo momento ho da fare."''',
 5: '''"Una celebrazione del folklore Saryd, è", spiega. "Benché da molto tempo fra le stelle viviamo, i classici senza tempo di prima della nostra età spaziale, ancora celebriamo. Una serie di spettacoli teatrali su alcuni di essi, oggi ospitiamo. Guardarli gratis, chiunque può."''',
 6: '''"Ho sempre tempo per una storia. Fate strada."''',
 7: '''"Non è proprio il momento per una storia. Passo."''',
 8: '''Lo seguite fuori dalla città-spazioporto e nel profondo di una foresta vicina. Lungo la strada, altri Saryd con abiti antichi simili guidano altre persone che l'offerta aveva incuriosito.''',
 9: '''Arrivate a una radura da cui si diramano tre sentieri diversi, e in fondo a ciascuno distinguete una luce fioca. Dopo qualche minuto, sembra che tutti i Saryd coinvolti nella celebrazione siano arrivati. Prendono tre scrigni da dietro un cespuglio e li depongono davanti a voi e agli altri che hanno condotto fin lì.''',
 10: '''"Ora amici, scegliere il vostro sentiero, dovete", dice uno dei Saryd, e molti fra la folla prendono piccoli oggetti dagli scrigni, evidentemente già pratici del rito. Vi avvicinate a guardare dentro gli scrigni e vedete che ognuno contiene cose diverse: quello di sinistra è pieno di semi, quello centrale di conchiglie e quello di destra di piume.''',
}

P2 = {
 11: '''(Prendi un seme.)''',
 12: '''(Prendi una conchiglia.)''',
 13: '''(Prendi una piuma.)''',
 14: '''Quando avete la piuma fra le mani, gli organizzatori vi dicono di imboccare il sentiero di destra.''',
 15: STAGE,
 16: '''Entrando in una radura, una cacciatrice Saryd dai capelli grigi si avvicina furtiva a un grande uccello posato su una roccia. Si muove lungo i bordi della radura, nascondendosi dietro cespugli e alberelli. Cerca il punto migliore da cui colpire l'uccello con una freccia, arco e freccia pronti fra le mani. Solo quando si avvicina a un grande ingresso della radura, sul lato opposto a quello da cui è entrata, trova il punto e prende la mira.''',
 17: '''Viene interrotta da un ruggito fragoroso e si getta a terra, evitando per un soffio la bestia che le era arrivata alle spalle. Non sapete quanto fedele sia la raffigurazione di carta della creatura, ma non potete descriverla altrimenti che come un "leone da siepe": un po' più grande dei leoni della Terra, con aculei al posto della criniera. Gli aculei proseguono in fila lungo la schiena fino alla punta della coda.''',
 18: '''Schivato l'assalto, la cacciatrice corre oltre l'uccello in cerca di copertura, ma la foresta non è abbastanza fitta per fermare l'avanzata della bestia. La belva attacca di nuovo e la ferisce in cima a una delle zampe anteriori. Lei la colpisce con un'altra zampa e prepara una freccia, ma riesce solo a graffiarle il muso. L'animale si solleva sulle zampe posteriori per colpirla dall'alto, ma resta stordito: l'uccello gli ha attaccato gli occhi, accecandolo! La cacciatrice è rapida a prendere la mira nello spiraglio che le si offre, e una freccia trafigge il torso della creatura. Caduto il leone da siepe, l'uccello vola via e il sipario si chiude.''',
 19: '''Quando avete il seme fra le mani, gli organizzatori vi dicono di imboccare il sentiero di sinistra.''',
 20: STAGE,
}

P3 = {
 21: '''La figura al centro è un giovane Saryd che galoppa in una foresta fitta. Cominciano effetti sonori di tuono, sempre più frequenti, che echeggiano intorno a voi come in un vero temporale. Un pezzo di carta bianca a forma di fulmine scende rapido e colpisce uno degli alberi sulla strada del ragazzo. Pieghe a forma di fiamma piovono dall'alto del palco e si attaccano all'albero che cade, bloccando il passaggio. Il ragazzo si volta e corre altrove. Un altro fulmine, un altro albero che crolla. Dopo qualche ripetizione, il ragazzo è troppo stanco per correre. Ferito da alcune fiamme, ora zoppica nella foresta.''',
 22: '''Mentre guaisce e il tuono si avvicina di nuovo, scorge un albero diverso dagli altri: una grande quercia con rami più spessi di quelli degli alberi intorno. La raggiunge, si sdraia alla sua base e poco dopo si addormenta, mentre il sipario si chiude.''',
 23: '''Si riapre dopo qualche istante, con il ragazzo che si sveglia nel buio. Quando si alza, ai rumori profondi si accompagnano raggi di luce che raggiungono il suolo, e capisce che la grande quercia aveva abbassato i rami intorno a lui. Sollevandoli, i vari alberelli caduti sui rami della quercia durante la tempesta vengono scagliati lontano. Con il sole come guida, il ragazzo riesce a uscire dalla foresta e il sipario si chiude di nuovo.''',
 24: '''Quando avete la conchiglia fra le mani, gli organizzatori vi dicono di imboccare il sentiero centrale.''',
 25: STAGE,
 26: '''Un Saryd sta in cima a una specie di lunga piattaforma di legno, con uno sfondo blu profondo sotto di essa. Solo quando vedete la canna da pesca capite che è su una barca, a pescare in mare. Sente un morso, ma quando tira su non c'è nulla sull'amo. Sente un altro morso e di nuovo non trova nulla. Più e più volte guarda l'amo e trova l'esca ancora lì, intatta, eppure continua a sentire morsi, alcuni così forti che persino la barca si muove un po'. La giornata passa in fretta, con un pezzo di carta che rappresenta il sole che si sposta rapido da un lato del "cielo" all'altro.''',
 27: '''Quando scende la notte, le onde si fanno sempre più forti e il Saryd smette del tutto di pescare. Posa la canna sulla barca e cerca di dirigerla verso la riva, ma non trova la via. Si avvicina un'onda enorme che supera l'altezza del palco e inghiotte la barca.''',
 28: '''Il pescatore scalcia e lotta per l'aria, avendo perso la barca ed essendo ancora in balia delle grandi onde. La scena sul palco comincia a scendere, seguendo i calci, e qualcosa comincia a salire incontro alle zampe del Saryd. Mentre riporta la scena verso l'alto, una creatura che ricorda una balena, ma con pinne molto più grandi e lunghe che quasi si collegano alla coda, affiora in superficie. Sale piano e con cura, come se cercasse di offrire un terreno al marinaio. Si avvicina un'altra onda, grande abbastanza da inghiottirli entrambi, ma la balena continua a salire finché non è fuori dall'acqua.''',
 29: '''Mentre vola nel cielo notturno, la balena bada a non far cadere il Saryd, aspettando sempre che trovi un appoggio stabile prima di virare. Per il resto della notte danza lentamente nel cielo e, quando arriva il mattino e le onde si calmano, torna al mare e nuota vicino alla riva. Quando il Saryd è sulla spiaggia, si volta e vede la coda della balena colpire l'acqua mentre si tuffa di nuovo negli abissi, e il sipario si chiude.''',
 30: '''Il pubblico comincia ad alzarsi e a fare un breve inchino verso il palco, con le mani strette insieme vicino al petto, come per applaudire in silenzio lo spettacolo. Quando quasi tutti hanno finito, si preparano ad andarsene e voi li seguite. Tornati alla radura, rimettete il piccolo oggetto nel suo scrigno dopo aver visto gli altri fare lo stesso, e gli organizzatori riaccompagnano tutti allo spazioporto.''',
 31: '''Arrivati là, il Saryd che vi aveva avvicinato per primo dice: "Che lo spettacolo vi sia piaciuto, spero", e vi saluta.''',
}

src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units']
eng = {u['idx']: u['english'] for u in src}
for idx, txt in list(P1.items()) + list(P2.items()) + list(P3.items()):
    assert not txt.startswith('\t'), idx
    assert txt.count('\t') == 0, idx
    assert txt.count('"') == eng[idx].count('"'), (idx, txt.count('"'), eng[idx].count('"'))
    assert txt.strip(), idx
assert sorted(P1) == list(range(1, 11)), sorted(P1)
assert sorted(P2) == list(range(11, 21)), sorted(P2)
assert sorted(P3) == list(range(21, 32)), sorted(P3)
# le tre unita' del palco sono identiche anche in italiano (l'inglese e' identico)
assert P2[15] == P2[20] == P3[25] == STAGE

os.makedirs(OUT, exist_ok=True)
for name, d in (('part01.json', P1), ('part02.json', P2), ('part03.json', P3)):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        json.dump({str(k): v for k, v in sorted(d.items())}, f, ensure_ascii=False, indent=1)
print('scritte %d unita (10 + 10 + 11)' % (len(P1) + len(P2) + len(P3)))
