"""mkparts.py — L102: costruisce `parts/part01-04.json` (48 unita', righe 1-117).

Primo lotto di `quarg missions.txt` e **primo `LOGBOOK` della campagna**: le unita' 1 e 2 sono le schede dei
**Quarg** e dei **Drak** (prosa descrittiva, non etichette).

Due voci distinte per i Quarg: il primo individuo (5-27) parla con frasi brevi e solenni e si riferisce a sé
come «questo uno» (in inglese *this one*); quello di **Kuwaru Efreti** (29-48) parla in inglese arcaico con
sintassi invertita («Whither came you», «bring you can we no succor», «lest awaken in you we»). La resa italiana
usa un registro elevato e l'ordine marcato, senza arcaismi finti.

**2 token** nella stessa unita' (42): `<first>` e `<last>`. **0 quadre**.
**3 ripetizioni**: 17/20 (`"Who are the Drak?"`), 35/40, 37/38 — rese da costanti uniche.
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'parts')

DRAK_Q = '''"Chi sono i Drak?"'''
MACHINES = '''"Navi stellari robotiche, e fabbriche autonome che le creano. Sebbene ora non siano dirette da alcun essere vivente, si riproducono ancora e si fanno guerra insensata fra loro. Guardatevi dalle loro navi se vagate a nord e a est di qui, ché impugnano armi diverse e strane, e nessun soccorso possiamo recarvi entro i confini del loro spazio."'''
NOSPEAK = '''"Di questo non parleremo, che non si risvegli in voi il desiderio di seguirne le orme. Ma potete osservare i rottami delle loro abominazioni e trarne avvertimento."'''
THANKS = '''Lo ringraziate del tempo, e la folla di Quarg che vi fissava si disperde lentamente.'''

P1 = {
 1: '''I Quarg sono alieni alti, sottili e imperscrutabili, evoluti su un pianeta molto piccolo, e possono vivere comodamente su mondi con un'atmosfera così sottile che un essere umano non potrebbe respirarla. Hanno scoperto il volo spaziale milioni di anni fa. Molti di loro vivono su mondi ad anello costruiti artificialmente, compreso uno nello spazio umano. Vivono in pace con la maggior parte delle specie senzienti e affermano di essere in comunicazione con una specie ancora più antica, chiamata Drak.''',
 2: '''I Drak sarebbero la specie vivente più antica della galassia. I Quarg dicono che i Drak agiscono come una sorta di pacificatori o poliziotti galattici, e intervengono se una specie inventa un'arma così terribile da poterla portare all'estinzione.''',
 3: '''Avevate già visto immagini e video dei Quarg, ma è la prima volta che entrate in uno spazioporto di loro proprietà. L'architettura è davvero aliena: soffitti scomodamente alti, colori strani e pareti che non sembrano mai incontrarsi ad angolo retto. I Quarg stessi sono altrettanto strani: torreggiano su di voi, alcuni alti quasi tre metri. Le loro gambe si piegano all'indietro in basso, come un cane che cammina sulle zampe posteriori, e si muovono con grazia e quasi in silenzio.''',
 4: '''La maggior parte dei Quarg che vedete è vestita interamente in tonalità di grigio, o solo con lievi accenni di colore. La moda Quarg sembra ruotare non intorno al colore, ma alla trama: tessuti grossolani e fini, motivi come squame di lucertola o ciottoli, e occasionali frange decorative di materiale spugnoso. La loro pelle è grigio scuro, a volte con un accenno di verde, blu o marrone sotto, con un fine disegno a squame come quello di un rettile. Ma ciò che rende sconcertanti i loro occhi è che sembrano molto umani, tranne che alcuni hanno iridi d'oro o viola invece che verdi, blu o marroni. Non hanno capelli, ma molti indossano piccoli berretti di stoffa o cappucci.''',
 5: '''Uno dei Quarg si accorge che lo state fissando a bocca aperta e si avvicina. Si accovaccia sui garretti finché i suoi occhi non sono all'altezza dei vostri e dice: "Salve." La sua voce è profonda, e suona come una fisarmonica o il ronzio di un alveare mescolato al sibilo del motore di una nave.''',
 6: '''"Salve."''',
 7: '''Parlando lentamente e con deliberazione, dice: "Credo che tu sia nuovo qui. Sei quello che chiamano un turista?"''',
 8: '''"Sì."''',
 9: '''"No, sono un capitano mercantile, sono qui per comprare e vendere carico."''',
 10: '''"Capisco." Il Quarg sbatte le palpebre lentamente. Le sue palpebre vengono dai lati degli occhi, invece che dall'alto e dal basso. In un occhio per il resto così umano, l'effetto è sconcertante. "Molti umani hanno molte domande quando ci vedono, e noi Quarg viviamo per molte vite umane, quindi non è un peso per questo uno parlare con te."''',
 11: '''"Mi puoi parlare dei Quarg?"''',
 12: '''"Ci sono altre specie aliene nella galassia?"''',
 13: '''"È un onore parlare con te, ma non ho domande."''',
 14: '''"Molte. La maggior parte giovani, molto più giovani dei Quarg. Molte sciocche. Poche sagge. Molte viaggiano solo lungo le antiche vie fra le stelle. Poche non hanno bisogno di vie per viaggiare. E alcune rimodellano la galassia a piacimento. Ma i Quarg non sono come nessun altro, perché non abbiamo nulla che gli altri bramino."''',
 15: '''"Che cosa vuoi dire?"''',
 16: '''"Noi Quarg siamo unici fra tutte le specie della galassia. La nostra specie è nata sulla luna di un grande gigante gassoso, su un pianeta molto piccolo, che raccoglieva intorno a sé pochissima aria. Non possiamo muovere molti passi sui mondi che gli Hai, i Korath e le altre specie desiderano. E i mondi come il nostro, voi non potreste respirarne l'aria così sottile, perché i nostri polmoni sono assai delicati. E siamo una razza antica, e non uccidiamo per diletto o per capriccio, così i Drak ci hanno dato il dono, che possiamo andare fra le altre razze e stabilirci dove vogliamo, e farci amici di tutti, perché nessuno osa essere nostro nemico."''',
 17: DRAK_Q,
 18: '''"Perché nessuno osa esservi nemico?"''',
 19: '''"Perché siamo molto forti, e perché parliamo con i Drak."''',
 20: DRAK_Q,
 21: '''"I Drak sono i più anziani fra i viventi. Non i primogeniti, perché quelli sono scomparsi da tempo, ma i più anziani fra i viventi, eppure sono molto più giovani delle stelle. Curano e coltivano i sentieri fra le stelle, e potano via le vie per cui una specie potrebbe viaggiare per fare guerra a un'altra. E custodiscono il segreto del viaggio oltre quei sentieri, e lo danno solo a pochi degni, perché la pace prevalga." Si tocca il petto con una mano, segnalando che i Quarg sono fra quei pochi.''',
 22: '''"Non che i Drak siano estranei alla guerra. Pianeti e lune e persino stelle furono consumati nelle loro guerre e non esistono più. Ma poi appresero la saggezza, e non hanno più combattuto guerre, per molti milioni di anni umani. Vivono qui vicino, ma se ne stanno per conto loro, e intervengono negli affari delle altre razze solo per impedirne la distruzione o l'uso di oscene tecnologie di guerra."''',
}

P2 = {
 23: '''"Noi umani abbiamo usato armi piuttosto distruttive gli uni contro gli altri, e nessuna specie aliena è mai intervenuta per fermarlo."''',
 24: '''"Beh, spero che non faremo mai nulla di abbastanza brutto da costringerli a intervenire."''',
 25: '''"Avete fatto che cosa? Risvegliato l'atomo? Ci sono armi molto peggiori di quella. Consumare pianeti. Spegnere stelle. Strappare la carne dello spazio e del tempo stesso. Armi del caos che prego la tua razza sconsiderata non riesca nemmeno a concepire. Queste cose attireranno l'attenzione dei Drak, perché una volta hanno quasi distrutto questa galassia, e non si deve permettere che lo facciano di nuovo."''',
 26: '''"Beh, se là fuori ci sono tecnologie così pericolose, spero che i Drak continuino a riuscire a impedirne l'uso."''',
 27: '''"Lo spero anch'io, umano." Il Quarg si alza, torreggiando di nuovo su di voi. "Finché sei un cercatore di pace, sei il benvenuto sui nostri mondi in qualunque momento." Vi fa un inchino. Non siete sicuri che sia anch'esso un gesto Quarg, o che stia semplicemente imitando un'usanza umana, ma ricambiate l'inchino, e il Quarg si allontana in silenzio.''',
 28: '''Per la vostra esperienza passata, non avete mai visto i Quarg muoversi con qualcosa che somigli alla fretta o all'eccitazione, ma quando atterrate su questa stazione un gruppo di loro vi corre incontro, muovendosi più velocemente di quanto pensavate fossero capaci. Per un minuto o due vi fissano e parlano fra loro nella loro lingua; credete di riconoscere la parola "Humani" e forse "Eartha".''',
 29: '''Alla fine compare un Quarg che parla la vostra lingua, o almeno è disposto a provarci. Dice: "Saluti, sorprendente viaggiatore. Donde venite, e perché ci visitate qui nell'inquieto cimitero dei Korathi?"''',
 30: '''"Sono qui solo per esplorare. Mi puoi dire di più sui Korath?"''',
 31: '''"Sono venuto a scoprire che cosa è successo ai Korath."''',
 32: '''"Ah, gli stolti Korath," dice. "Un tempo un impero potente, ora tristemente diviso e diminuito. Le loro macchine da guerra pensanti, che ora si riproducono senza freno e sono nemiche di tutti, danno la caccia ai superstiti. E alcuni di loro, anche, furono esiliati per i loro grandi crimini."''',
 33: '''"Che crimini hanno commesso?"''',
 34: '''"Che cosa vuoi dire con 'macchine da guerra pensanti'?"''',
 35: MACHINES,
 36: '''"Hai parlato di 'crimini'. Che crimini hanno commesso?"''',
 37: NOSPEAK,
}

P3 = {
 38: NOSPEAK,
 39: '''"Hai parlato di 'macchine da guerra pensanti'. Che cosa sono?"''',
 40: MACHINES,
 41: '''Siete interrotti mentre uno dei Korath che abitano questo mondo ad anello passa accanto, e il Quarg dice: "Amico Korath, incontra l'umano."''',
 42: '''"<first> <last>," dite, tendendo una mano d'istinto. Il Korath non vi stringe la mano, ma vi saluta sollevando entrambe le mani, con i palmi verso di voi. Dice qualcosa nella sua lingua, poi si allontana in fretta.''',
 43: '''Il Quarg vi dice: "Una fazione fra i Korathi cercò la pace. Si fanno chiamare 'Korath Efreti', che significa 'Amici dei Korath'. Sono sotto la nostra protezione e non intendono farti alcun male. Ma non hanno la tua lingua; qui gli umani sono rari. Un'altra domanda hai?"''',
 44: '''"I Korath amichevoli mi lasceranno comprare la loro tecnologia?"''',
 45: '''"Perché non distruggete i robot, se sono una tale minaccia?"''',
 46: '''"No, ma sono lieto di conoscerti."''',
 47: '''"Visitate i loro mondi," dice il Quarg. "Sebbene non imparino le vostre parole, siete scaltro e potete parlare come fa chi è senza parole, indicando le cose." ''' + THANKS,
 48: '''Fa scattare i denti l'uno contro l'altro, che potrebbe essere l'equivalente Quarg di una risata. "Si sperava che una fazione di robot distruggesse l'altra, e ci lasciasse meno lavoro da fare, ma purtroppo sono troppo pari. Ci limitiamo invece a trattenerli dall'espandersi, come si isola un fuoco che non si riesce a spegnere e lo si lascia bruciare fino a esaurirsi." ''' + THANKS,
}

src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units']
eng = {u['idx']: u['english'] for u in src}
kind = {u['idx']: u['kind'] for u in src}
TAGS = re.compile(r'<[^<>]+>')
for idx, txt in list(P1.items()) + list(P2.items()) + list(P3.items()):
    assert not txt.startswith('\t'), idx
    assert txt.count('\t') == 0, idx
    assert txt.count('"') == eng[idx].count('"'), (idx, txt.count('"'), eng[idx].count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng[idx]), (idx, TAGS.findall(eng[idx]), TAGS.findall(txt))
    assert '[' not in txt and ']' not in txt, idx
    assert txt.strip(), idx
assert sorted(P1) == list(range(1, 23)) and sorted(P2) == list(range(23, 38)) and sorted(P3) == list(range(38, 49))
# i due LOGBOOK sono le unita' 1 e 2: prosa, tradotte per intero
assert [i for i in range(1, 49) if kind[i] == 'LOGBOOK'] == [1, 2]
assert P1[1] != eng[1] and P1[2] != eng[2]
# ripetizioni da costante unica
assert P1[17] is P1[20] is DRAK_Q and P2[35] is P3[40] is MACHINES and P2[37] is P3[38] is NOSPEAK
# due token nella stessa unita', nell'ordine
assert TAGS.findall(P3[42]) == ['<first>', '<last>'] == TAGS.findall(eng[42])

os.makedirs(OUT, exist_ok=True)
for name, d in (('part01.json', P1), ('part02.json', P2), ('part03.json', P3)):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        json.dump({str(k): v for k, v in sorted(d.items())}, f, ensure_ascii=False, indent=1)
print('scritte %d unita (22 + 15 + 11)' % (len(P1) + len(P2) + len(P3)))
