"""mkparts.py — L123: apre `data/human/ships.txt` (54 unita', righe 78-2044, da `Aerie` a `Fury`).

Primo lotto di un file di **navi**. Forma propria: **48 `DESCRIPTION`** e **6 `VALUE`**, **33 contesti** (18 da
una sola unita'), **14 unita' con tab**, **16 virgolette**, **zero token**, **zero quadre**.

- **I 6 `VALUE` sono nomi di nave al plurale** (`Argosies`, `Auxiliaries` ×3, `Finches`, `Furies`): restano
  **identici al sorgente** (decisione 259), e il `check.py` li elenca.
- **48 testi distinti** per 54 unita': il testo «Fighters do not come equipped with a hyperdrive…» compare
  **cinque volte** (un caccia sì, ma con la stessa nota), il nome `Auxiliaries` tre volte.
- **Zero token**: asserzione scritta (`== {}`), non omissione.
"""
import collections
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PARTS = os.path.join(HERE, 'parts')
SRC = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units']
ENG = {u['idx']: u['english'] for u in SRC}
KIND = {u['idx']: u['kind'] for u in SRC}
TAGS = re.compile(r'<[^<>]+>')

UNIQ = [
    ("four fighter bays",
     "La Lionheart Aerie è una portatrice leggera, progettata per essere appena abbastanza grande per quattro baie "
     "di caccia e per un armamento decente. Varianti dello stesso progetto sono in uso nel Deep da quasi mezzo "
     "millennio, ma questo modello arriva con la tecnologia più recente in fatto di generatori e armi."),
    ("Southbound Shipyards is very popular",
     "L'Argosy dei Southbound Shipyards è molto amata dai mercanti non per la sua capacità, che è in effetti un po' "
     "inferiore a quella della Freighter del Sindacato, ma perché sa difendersi in combattimento anche contro una "
     "piccola flotta pirata."),
    ("easy ship to upgrade",
     "L'Argosy è anche una nave molto facile da potenziare con motori più veloci o armi più potenti, secondo "
     "necessità, così molte Argosy di proprietà privata hanno capacità molto diverse dal modello di serie."),
    ("very rich passengers",
     "L'Arrow è un trasporto leggero, progettato per portare un piccolo numero di passeggeri molto ricchi, "
     "amministratori delegati del Sindacato per esempio, da un pianeta all'altro con velocità e stile. Compensa il "
     "suo armamento leggero con la capacità di seminare quasi ogni altra nave del cielo."),
    ("logistical backbone",
     "L'Auxiliary è la spina dorsale logistica della Marina della Repubblica. Grande e resistente come una nave "
     "capitale, ma con più spazio per il carico e i passeggeri di qualsiasi altra nave della Marina, l'Auxiliary "
     "viene usata ogni volta che la Marina deve trasportare grandi quantità di truppe o di carico con la garanzia "
     "che arrivino a destinazione."),
    ("modularity in mind",
     "L'Auxiliary è stata costruita pensando alla modularità, così la nave può essere allestita con più spazio per "
     "il carico o per le cuccette secondo la missione. Questa modularità la rende però piuttosto costosa da "
     "costruire, e quindi rara da vedere."),
    ("last of the great city-ships",
     "La Lionheart Bactrian è l'ultima delle grandi navi-città, un progetto che risale ai primi tempi della "
     "colonizzazione spaziale, quando una nave a lungo raggio doveva essere un mondo autosufficiente, capace di "
     "sopravvivere per settimane senza incontrare un pianeta abitato. Non è solo una nave da carico, ma una "
     "portatrice, e una nave da guerra capace sia a distanza ravvicinata sia da lontano."),
    ("vetted by the local government",
     "Naturalmente questa versatilità la rende anche estremamente costosa, e la Bactrian di solito è in vendita solo "
     "a cittadini che sono stati verificati dal governo locale del Deep."),
    ("testing the waters",
     "Sebbene il Sindacato non costruisca portatrici di caccia, sta tastando il terreno con la Barb, un velivolo "
     "economico e flessibile lanciato dalle portatrici, dotato di motori ionici miniaturizzati di nuovo sviluppo. La "
     "filosofia progettuale della Barb sembra essere stata \"più brutta della Protector\", e guardando l'abitacolo "
     "incastrato tra il grosso portello del cannone e l'alloggiamento della torretta, ti chiedi dove dovrebbero "
     "stare i sistemi di alimentazione. Sebbene sia una nave dall'aspetto sgraziato, sembra abbastanza flessibile da "
     "diventare un'aggiunta pericolosa per qualsiasi flotta con portatrici."),
    ("pressurized suit",
     "Per poter montare un Proton Gun mantenendo comunque un alloggiamento per torretta, la Syndicated Systems ha "
     "dovuto rimuovere vari sistemi di supporto vitale, obbligando il pilota a indossare una tuta pressurizzata "
     "invece di avere una cabina completamente pressurizzata. Anche se questo rende il pilotaggio di una Barb "
     "un'esperienza scomoda, il risultato è un livello di potenza di fuoco a corto raggio inaudito per un velivolo "
     "delle sue dimensioni."),
    ("Fighters do not come equipped",
     "I caccia non sono dotati di iperguida. Non puoi trasportare un caccia a meno che tu non abbia nella tua flotta "
     "una nave con una baia di caccia."),
    ("heavy defense platform",
     "La Southbound Shipyards Bastion è progettata come piattaforma di difesa pesante per accompagnare i convogli di "
     "navi da carico, oltre ad avere capacità di carico sufficiente a servire essa stessa da nave da carico. A causa "
     "del suo armamento pesante è classificata come nave da guerra, non come nave da carico."),
    ("alternative to the Syndicate Bulk Freighter",
     "La Behemoth è un progetto recente dei Betelgeuse Shipyards, pensato come alternativa alla Bulk Freighter del "
     "Sindacato. Sebbene la sua capacità di carico sia un po' inferiore, è anche più manovrabile e di serie monta un "
     "armamento più pesante."),
    ("interceptor-class ships",
     "Un tempo tra le navi intercettori più diffuse, la popolarità della Berserker sta calando a favore di navi più "
     "moderne e versatili come la Hawk. Sebbene i Betelgeuse Shipyards ne producano ancora un numero limitato, la "
     "maggior parte delle Berserker in servizio oggi ha più di mezzo secolo."),
    ("high-class passenger transport",
     "La Tarazed Blackbird è un trasporto passeggeri di alta classe, progettato per spostare grandi numeri di "
     "persone attraverso la galassia con velocità e sicurezza. Sebbene non sia dotata di molte armi, una Blackbird è "
     "ben protetta e abbastanza veloce da evitare gli attacchi dei pirati, e la sua capacità di carico è sufficiente "
     "a permettere al capitano di prendere missioni di corriere nel frattempo."),
    ("scout ship and courier",
     "La Megaparsec Bounder è una nave esploratrice e corriere, progettata non per la battaglia ma per portare "
     "passeggeri e piccole quantità di carico attraverso grandi distanze in fretta."),
    ("F6-C",
     "Dopo l'introduzione del modulo cargo \"Type F\" per la Hauler, ai capitani mercantili fu chiaro che le nuove "
     "portatrici potevano offrire più flessibilità alla loro flotta, se solo ci fosse stata una cassa cargo da "
     "agganciare ai bracci dei caccia. Ecco la \"F6-C: Boxwing\", il caccia che non combatte, ma trasporta carico. "
     "Le attrezzature per la conservazione del carico danno alla Boxwing molta più massa e una dissipazione del "
     "calore molto scarsa rispetto agli altri caccia. Che non possa portare armi è solo una parte del motivo per cui "
     "i piloti la chiamano tra loro \"bara volante\"; oltre a somigliare a una bara ed essere molto lenta, il "
     "\"sedile\" del pilota funge anche da cuccetta, ed è più angusto di quanto la maggior parte delle persone "
     "tolleri. Il finestrino panoramico interattivo con H.U.D. è l'unica cosa che impedisce agli attacchi di "
     "claustrofobia di diventare un problema serio."),
    ("ultimate cargo ship",
     "La Bulk Freighter è la nave da carico per eccellenza, capace di trasportare tanto carico quanto quattro normali "
     "Freighter del Sindacato. I suoi ingranaggi di bordo le permettono di servire anche le colonie più primitive, "
     "anche se gli scaricatori dei porti più trafficati scherzano spesso dicendo che sarebbe più semplice portare "
     "navi da carico più piccole dentro le sue stive gigantesche."),
    ("incredibly slow",
     "È anche una nave incredibilmente lenta e difficile da manovrare, soprattutto quando è carica. Alcune carovane "
     "di merci usano normali navi da carico invece delle Bulk Freighter solo per evitare il fastidio di dover "
     "aspettare ogni volta che la Bulk Freighter si allinei correttamente per il salto iperspaziale."),
    ("welding a bunch of scrap metal",
     "La Bulwark è in pratica quello che ottieni saldando un mucchio di rottami su una Bastion. È un combattente "
     "robusto e lento, usato per lo più dai signori della guerra per proteggere i loro beni, siano navi o covi, "
     "dalle incursioni delle autorità o dei rivali. A causa della loro lentezza e del poco spazio per il carico, "
     "queste navi partecipano raramente alle razzie contro i convogli mercantili fuori dal loro sistema d'origine."),
    ("mobile space station",
     "La Carrier è più di una semplice nave da guerra: è praticamente una stazione spaziale mobile, con baie di "
     "attracco per un intero squadrone di droni e caccia, e un equipaggio sufficiente a riempire un piccolo "
     "villaggio. È progettata per restare in disparte durante gli scontri, affidandosi ai droni e ai caccia che "
     "porta per impegnare direttamente il nemico, mentre fornisce fuoco di supporto con le sue armi a lungo raggio."),
    ("Q-ship",
     "La \"Freighter\" di classe C è una Q-ship, una nave da guerra stealth progettata dal Sindacato per attirare i "
     "pirati con l'offerta di quella che sembra una Bulk Freighter inerme e comune."),
    ("Interference Plating",
     "All'interno, uno strato di Interference Plating nasconde l'equipaggiamento di livello militare e una dozzina di "
     "droni da combattimento sistemati nelle stive convertite, mentre i finti ingranaggi celano emettitori di scudi "
     "supplementari."),
    ("smaller sister ship",
     "La Clipper è la sorella minore della popolare Argosy dei Southbound Shipyards. Sebbene non possa portare "
     "altrettanto carico, le Clipper sono navi versatili che possono essere usate come trasporti passeggeri, "
     "corrieri o persino navi da guerra in caso di necessità, e arrivano con abbastanza spazio libero per essere "
     "personalizzate secondo le esigenze del singolo capitano."),
    ("pilotless attack ships",
     "I droni da combattimento sono navi d'attacco senza pilota usate principalmente dalla Marina della Repubblica. "
     "Sebbene siano molto deboli e facili da distruggere, possono essere molto efficaci in grandi numeri. Poiché i "
     "droni non hanno bisogno di un abitacolo, possono essere riempiti interamente di equipaggiamento e metallo "
     "solido, il che rende i loro scafi più robusti di quelli delle altre navi piccole."),
    ("Drones do not come equipped",
     "I droni non sono dotati di iperguida. Non puoi trasportare un drone a meno che tu non abbia nella tua flotta "
     "una nave con una baia per droni."),
    ("intermodal containers",
     "La Container Transport è una configurazione più recente e diffusa della Bulk Freighter, che sostituisce le "
     "stive esterne sciolte con container intermodali per un più efficiente ciclo di scarico nei porti più grandi e "
     "meglio attrezzati."),
    ("geared cousin",
     "Come la sua cugina a ingranaggi, però, resta una nave lenta e difficile da manovrare, soprattutto quando è "
     "carica. Alcune carovane di merci usano normali navi da carico invece delle Container Transport solo per "
     "evitare il fastidio di dover aspettare ogni volta che la Container Transport si allinei correttamente per il "
     "salto iperspaziale."),
    ("experimental lightweight materials",
     "La Lionheart Corvette, che incorpora nuovi materiali leggeri sperimentali, unisce la velocità e l'agilità di "
     "un caccia all'armamento di una nave da guerra pesante. Il suo scafo debole è più che compensato dalla sua "
     "avanzata matrice di scudi."),
    ("much larger version of the Frigate",
     "La Cruiser della Repubblica è un progetto relativamente recente, una versione molto più grande della Frigate "
     "pensata per poter affrontare un'intera flotta pirata se necessario. Oltre a un'ampia varietà di armi, le "
     "Cruiser hanno spazio per portare quattro droni d'attacco: caccia veloci e senza pilota che possono essere "
     "controllati a distanza."),
    ("engine pods bolted on",
     "I pirati chiamano questa Clipper pesantemente modificata \"Cutthroat\". Con un paio di pod di motori "
     "imbullonati apposta per massimizzare la velocità, può seminare tutte le navi del cielo tranne quelle messe a "
     "punto nel migliore dei modi, permettendo ai suoi utilizzatori di superare quasi ogni blocco."),
    ("intended to be carried by their Aerie",
     "La Dagger è un caccia progettato dalla Lionheart Industries, pensato per essere portato dalla loro nave da "
     "guerra Aerie, anche se altre navi sono state viste portarli. Come molte navi Lionheart, il suo telaio è "
     "composto in gran parte di materiali compositi leggeri, il che lo rende notevolmente più veloce degli altri "
     "caccia."),
    ("provide a large capital ship",
     "La Dreadnought è una nuova nave da guerra progettata dai Southbound Shipyards per dare alle flotte dei Mondi "
     "Liberi una grande nave capitale, qualcosa capace di tener testa a una Cruiser della Marina o persino a una "
     "Carrier."),
    ("forward operating bases",
     "Le Dropship sono state progettate pensando all'Auxiliary della Marina. Le Auxiliary atterrate fungono spesso da "
     "basi operative avanzate, così le truppe che devono essere trasportate altrove si affidano spesso alle loro "
     "Dropship. Questa nave angusta e scomoda è in grado di spostare una squadra di soldati della Repubblica a grande "
     "velocità per le sue dimensioni."),
    ("governing corporate entities",
     "Prima della formazione della Repubblica galattica, molti sistemi stellari appartenevano a \"entità aziendali "
     "di governo\", con la maggior parte dello spazio inaccessibile ai privati cittadini. L'unica eccezione a questa "
     "regola erano le bande pirata, le cui poche navi erano spesso flotte aziendali rubate o ribelli, ma che avevano "
     "un impatto sproporzionato sul commercio interstellare. La necessità per le corporazioni di proteggere le "
     "proprie attività fece sì che l'Enforcer fosse una delle navi più comuni usate per la sicurezza e la difesa. La "
     "nave vanta un armamento di quattro portelli per cannoni e un alloggiamento per torretta, tutto su uno scafo "
     "piccolo ma difendibile, potente per la sua epoca."),
    ("no longer on the market",
     "Sebbene non sia più sul mercato, l'Enforcer si trova in possesso di un piccolo numero di mercanti e, "
     "ironicamente, di vari gruppi di pirati, come nave da combattimento invecchiata, facilmente superata da altre "
     "navi da guerra leggere o persino da intercettori di dimensioni simili."),
    ("sleeker and more maneuverable",
     "La Tarazed Falcon è una delle navi da guerra più potenti che i civili possano comprare, un'alternativa più "
     "affusolata e manovrabile alla venerabile e un po' superata Leviathan."),
    ("Over 85% of the parts",
     "Quando i Mondi Liberi iniziarono a chiedere ai loro cantieri una soluzione per le portatrici, i Tarazed "
     "Shipyards capirono subito che poche modifiche potevano trasformare il loro intercettore di base in un caccia "
     "di primo livello. Oltre l'85% dei pezzi che compongono la Finch è condiviso con la linea di montaggio della "
     "Sparrow, quindi non sorprende che, anche ridotta al minimo per entrare (a stento) in una baia di caccia, la "
     "velocissima Finch somigli molto alla sua cugina capace di viaggiare nell'iperspazio."),
    ("long and storied past",
     "La Betelgeuse Shipyards Firebird è una nave da guerra con un passato lungo e glorioso; le Firebird "
     "combatterono su entrambi i fronti delle guerre degli Alphas più di mezzo millennio fa, e sebbene da allora "
     "equipaggiamenti e sistemi siano stati aggiornati di continuo, il progetto di base è rimasto quasi identico. La "
     "Firebird è anche una nave molto robusta e facile da riparare; si dice che alcune delle Firebird che "
     "combatterono in quelle guerre siano ancora in servizio oggi."),
    ("only selling point is speed",
     "Senza spazio né per il carico né per i passeggeri né per armamenti pesanti, l'unico punto di forza della "
     "Flivver è la velocità. Le Flivver sono vendute soprattutto a individui facoltosi che vogliono viaggiare tra le "
     "stelle senza dover condividere una cuccetta su un trasporto mercantile con la gente comune."),
    ("efficient means of carrying cargo",
     "La Freighter è progettata dal Sindacato per essere un mezzo efficiente di trasporto del carico da un sistema "
     "all'altro, ma è così lenta e difficile da far atterrare che la maggior parte dei piloti odia pilotarla."),
    ("obvious target for pirates",
     "Le navi da carico sono un bersaglio ovvio per i pirati, ma girano troppo lentamente per poter puntare i "
     "cannoni frontali su un nemico in avvicinamento. Di conseguenza, l'ultimo modello di nave da carico è "
     "equipaggiato solo con torrette, compresa una torretta antimissile per impedire agli attaccanti di bombardarla "
     "fino alla resa da una distanza sicura."),
    ("largest warship produced by the Republic Navy Yard",
     "Per secoli la Frigate è stata la più grande nave da guerra prodotta dall'Arsenale della Marina della "
     "Repubblica, ma ora sembra piuttosto piccola rispetto a una Cruiser o a una Carrier. Armata con varie armi, la "
     "Frigate è ugualmente capace di respingere piccoli caccia o di bombardare navi più grandi. A suo tempo aveva "
     "una manovrabilità relativamente buona per una nave delle sue dimensioni, ma oggi continua a essere usata "
     "soprattutto per il numero enorme di esemplari già costruiti per il servizio."),
    ("most popular design of escort ship",
     "La Fury è il progetto di nave scorta più diffuso dei Southbound Shipyards. Hanno più potenza di fuoco di "
     "qualsiasi altro intercettore, il che significa che qualsiasi pirata che voli da solo ci penserà due volte "
     "prima di attaccare un convoglio scortato da una Fury. Però le Fury sono anche molto meno manovrabili delle "
     "altre navi piccole."),
]

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ST = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(ST.values()) == {'PENDING'}, {k: v for k, v in ST.items() if v != 'PENDING'}

assert collections.Counter(u['kind'] for u in SRC) == {'DESCRIPTION': 48, 'VALUE': 6}
assert sum(1 for u in SRC if u['english'].startswith('\t')) == 14
assert sum(u['english'].count('"') for u in SRC) == 16
ctx = collections.Counter(u['context'] for u in SRC)
assert len(ctx) == 33 and collections.Counter(ctx.values()) == {1: 18, 2: 11, 3: 3, 5: 1}, ctx
assert collections.Counter(t for u in SRC for t in TAGS.findall(u['english'])) == {}   # zero token

names = {u['english'] for u in SRC if u['kind'] == 'VALUE'}
assert names == {'Argosies', 'Auxiliaries', 'Finches', 'Furies'}, names
prose = [e for e in dict.fromkeys(u['english'] for u in SRC) if e not in names]
assert len(prose) == 44 and len(UNIQ) == 44, (len(prose), len(UNIQ))
assert sum(1 for u in SRC if u['english'].strip().startswith('Fighters do not come')) == 5


def resolve(eng):
    hits = [t for s, t in UNIQ if s in eng]
    assert len(hits) == 1, (len(hits), eng[:90], hits)
    return hits[0]


cover = {e: resolve(e) for e in prose}
assert len(set(cover.values())) == 44, 'due testi distinti con la stessa resa'

T = {}
for u in SRC:
    eng = u['english']
    if u['kind'] == 'VALUE':
        T[u['idx']] = eng          # nome di nave: identico al sorgente (decisione 259)
    else:
        T[u['idx']] = '\t' * (len(eng) - len(eng.lstrip('\t'))) + cover[eng]

for idx, txt in T.items():
    eng, kind = ENG[idx], KIND[idx]
    assert txt.count('\t') == eng.count('\t'), idx
    assert txt.count('"') == eng.count('"'), (idx, eng.count('"'), txt.count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng) == [], idx
    assert not re.search(r'[\[\]`\u2019\u2014\u2013\u2026]', txt), idx
    assert not re.search(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", txt), idx
    if kind == 'VALUE':
        assert txt == eng, idx
    else:
        assert txt.strip() and txt.strip() != eng.strip(), idx
    r = len(txt) / len(eng)
    assert 0.55 < r < 1.90, ('gate', idx, round(r, 3), eng[:60])

for n, (lo, hi) in enumerate(((1, 18), (19, 36), (37, 54))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('54 unita (18x3) · 48 testi distinti · 6 VALUE identici (4 nomi) · 14 tab · 16 virgolette · 0 token')
