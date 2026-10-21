"""mkparts.py — L120: apre `data/human/campaign events.txt` (52 unita', righe 28-242).

Forma diversa da tutte le precedenti: **41 `MISSION_TEXT`**, **9 `DESCRIPTION`**, **2 `LOGBOOK`**, **nessun
`VALUE`**, **41 unita' su 52 con tab iniziale** (il tab qui e' la norma, non l'eccezione), **58 virgolette** che
sono **dialogo** (si traducono, a differenza delle chiavi `Preferences` di L115-L116) e solo **5 token**.

**45 testi distinti** per 52 unita': sette coppie ripetono lo stesso inglese (le risposte del giocatore e un
paragrafo di cronaca), e la resa ripete.

Controllo «i `VALUE` sono identici» scritto come **asserzione vuota** (`0 = 0`): il file non ne ha.
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
    ("genetically engineered super-soldiers",
     "Gli Alphas furono progettati secoli fa come super-soldati geneticamente modificati, privi di compassione e di "
     "empatia. Fuggirono dai loro padroni, resero schiavi interi pianeti e comandarono enormi flotte di navi. Alla "
     "fine furono sconfitti, e vennero uccisi o si nascosero. Si riconoscono dalla pelle verde, fotosintetica."),
    ("can live for centuries",
     "Gli Alphas possono vivere per secoli, ed è probabile che molti siano sopravvissuti, nascosti su mondi "
     "anarchici o da qualche parte oltre lo spazio umano. Per fortuna si riproducono molto più lentamente degli "
     "umani comuni."),
    ("Today, throughout human space",
     "Oggi, in tutto lo spazio umano, è il Giorno del Ricordo, l'anniversario dell'inizio delle guerre degli "
     "Alphas, più di cinque secoli fa. Gli Alphas erano soldati geneticamente modificati, con agilità e "
     "intelligenza sovrumane e una totale mancanza di compassione ed empatia. Al culmine della guerra, decine di "
     "pianeti erano stati resi schiavi dagli Alphas."),
    ("commemorates the beginning of the war",
     "Il Giorno del Ricordo commemora l'inizio della guerra, non la sua fine, come monito perpetuo che la guerra "
     "non è finita: sebbene gli Alphas siano stati sconfitti, alcuni fuggirono e restarono nascosti, e si presume "
     "che loro e la loro discendenza siano ancora presenti nella galassia oggi."),
    ("genetic resequencing technology",
     "Dalla guerra degli Alphas, la tecnologia di riordino genetico è stata controllata con grande severità. Poiché "
     "gli Alphas erano il prodotto di una manipolazione genetica sperimentale e non dell'evoluzione naturale, si "
     "ritiene che i loro geni siano meno robusti di quelli dei veri esseri umani, e che siano quasi incapaci di "
     "avere prole vitale senza accedere a tecnologie speciali. Per questo la maggior parte delle enclavi di Alphas "
     "scoperte dopo la guerra ha avuto popolazioni molto ridotte, non più di qualche decina di individui."),
    ("bogeyman",
     "In questi tempi in cui la Marina garantisce la pace in gran parte della galassia, su molti mondi gli Alphas "
     "non sono altro che una storia per spaventare i bambini. Poiché il tratto fisico più evidente degli Alphas era "
     "la pelle fotosintetica, su alcuni mondi i bambini corrono persino in giro con il viso dipinto di verde il "
     "Giorno del Ricordo, cercando di spaventare la gente. Ma su altri mondi, soprattutto ai margini dello spazio "
     "dove la Marina pattuglia di rado, degli Alphas si parla ancora con paura."),
    ("Geminus was home to the Republic Navy Yard",
     "Fino a poco tempo fa Geminus ospitava l'Arsenale della Marina della Repubblica, il più grande cantiere navale "
     "dello spazio umano. Ora dell'arsenale non resta altro che un cratere spalancato nel terreno, lasciato dal "
     "recente attentato terroristico."),
    ("spaceport and residential areas survived",
     "Per fortuna lo spazioporto e le zone residenziali sono sopravvissuti all'attentato, che ha colpito solo "
     "l'Arsenale ed è avvenuto di prima mattina, quando pochissime persone erano al lavoro."),
    ("no time for anyone who is not enlisted",
     "Gli ufficiali della Marina che comandano qui non hanno tempo per chi non è arruolato nella Marina e non "
     "partecipa alle indagini in corso."),
    ("Martini is a world of exotic beaches",
     "Martini è un mondo di spiagge esotiche e clima perfetto. Qui avevano sede la banca centrale della Repubblica "
     "e la Borsa Galattica, prima che un attacco terroristico le distruggesse insieme a gran parte della capitale."),
    ("massive rescue and evacuation operation",
     "Al momento è in corso una massiccia operazione di soccorso e di evacuazione dentro e intorno alla capitale, "
     "per trovare e curare i sopravvissuti e contenere le radiazioni. Come prevedibile, le scorte del pianeta si "
     "stanno pericolosamente esaurendo, e quel che resta del governo di Martini ha chiesto alle navi civili di "
     "aiutare a consegnare beni e provviste per l'operazione."),
    ("immaculate spaceport",
     "Al posto dello spazioporto immacolato che Martini un tempo vantava, questo spazioporto temporaneo è fatto di "
     "piazzole di fortuna sparse alla rinfusa, per sostenere il gran numero di navi della Marina e civili che "
     "assistono alle operazioni di soccorso ed evacuazione."),
    ("Bourne is a well-developed industrial world",
     "Bourne è un mondo industriale ben sviluppato, colonizzato per la prima volta quattro secoli fa. Le sue città "
     "ospitano alcuni degli individui più ricchi di questa parte della galassia, ma anche decine di migliaia di "
     "senzatetto e molte altre persone il cui lavoro in fabbrica basta a malapena a far quadrare i conti."),
    ("climate is somewhat dry",
     "Fuori dalle città il clima è piuttosto secco, ma le valli profonde e alcune zone costiere sono adatte "
     "all'agricoltura. Resta molto poco del pianeta che non sia stato toccato dalla mano dell'uomo."),
    ("seat of government for the newly-formed",
     "Bourne è anche la sede del governo dei Mondi Liberi, di recente formazione."),
    ("collection of local governments",
     "I Mondi Liberi sono un insieme di governi locali del braccio meridionale della galassia che hanno dichiarato "
     "l'indipendenza dalla Repubblica dopo che il Parlamento si è rifiutato di affrontare le questioni che avevano "
     "sollevato su dazi commerciali, tassazione e rappresentanza. Potrebbero essere legati ai recenti attentati "
     "terroristici all'Arsenale e alla borsa galattica, anche se negano ogni responsabilità."),
    ("The spaceport is eerily quiet",
     "Appena scendi dalla nave capisci che qualcosa non va affatto. Lo spazioporto è inquietantemente silenzioso, e "
     "una gran folla si è radunata attorno a uno schermo video nel bar locale."),
    ("amounted to an ultimatum",
     "Chiedi che cosa succede, e qualcuno te lo spiega. Di recente un insieme di governi planetari del braccio "
     "meridionale della galassia ha inviato alla Repubblica quello che equivale a un ultimatum: il rifiuto di "
     "pagare le tasse finché non saranno fatte riforme nell'elezione dei rappresentanti planetari. Questo gruppo, "
     "che si fa chiamare \"Mondi Liberi\", ha chiesto anche una rivalutazione immediata di tutti i dazi commerciali "
     "e delle norme sulla registrazione dei piloti. Il Parlamento ha rifiutato di prendere in considerazione una "
     "sola di queste richieste."),
    ("in the early morning, nuclear explosions",
     "Poi, di prima mattina, esplosioni nucleari su Geminus e Martini hanno distrutto l'Arsenale della Marina della "
     "Repubblica e la Borsa Galattica, azzoppando il centro militare ed economico della Repubblica. I \"Mondi "
     "Liberi\" negano ogni responsabilità per gli attentati, nonostante i tempi e il fatto che questi servano molto "
     "bene ai loro scopi."),
    ("Unless the terrorists can be found",
     "Se i terroristi non saranno trovati o non si consegneranno, la guerra civile è imminente. È passato meno di "
     "un anno da quando hai comprato la tua nave, e la galassia ti sta già crollando addosso."),
    ("heavy plasma cannon",
     "Appena scendi dalla nave capisci che qualcosa non va affatto. Personale della Marina pesantemente armato "
     "fiancheggia l'uscita dell'edificio dello spazioporto, e altri soldati pattugliano il porto. Un ufficiale di "
     "collegamento sta radunando un gruppo di civili verso un bunker basso accanto a una piazzola vicina. Sulla "
     "piazzola stessa, i soldati faticano a installare un possente cannone al plasma montato su una torretta "
     "antiaerea."),
    ("Carrier squadron coming in",
     "Con i civili al sicuro nel bunker, l'ufficiale di collegamento si volta verso di te. \"Mi dispiace, capitano, "
     "ma devo chiederti di lasciare il pianeta. Sta arrivando uno squadrone di navi portatrici e ci servono tutte "
     "le piazzole libere.\""),
    ('"Of course."',
     "\"Certo.\""),
    ("What's happening",
     "\"Che succede?\""),
    ("training exercise",
     "\"È una specie di esercitazione?\""),
    ("order me to leave",
     "\"E cosa ti fa pensare che tu possa solo ordinarmi di andarmene?\""),
    ("here on Geminus was bombed",
     "L'ufficiale di collegamento sospira. \"Capitano, temo che il pianeta sia in stato di emergenza. Ieri alcuni "
     "pianeti ribelli del sud hanno deciso di voler secedere dalla Repubblica. Hanno mandato al Parlamento un "
     "ultimatum: volevano la riforma elettorale e fiscale, il libero scambio, tutte le stesse cose di cui si "
     "lamentano da anni. Niente di grave. Tre ore fa, però, l'Arsenale qui su Geminus è stato bombardato insieme "
     "alla Borsa Galattica su Martini. Non sappiamo se sia opera dei ribelli 'Mondi Liberi' o no, e non posso "
     "prometterti che non ci saranno altri attacchi. So solo che chiunque l'abbia fatto ha usato armi nucleari, "
     "quindi abbiamo tremila feriti da portare subito a cure mediche fuori dal pianeta.\""),
    ("get out of the way, then",
     "\"Allora mi tolgo di mezzo.\""),
    ("out of your hair as soon as I can lift off",
     "\"Scusa, non lo sapevo. Ti lascio in pace appena riesco a decollare.\""),
    ("Is there any way I can help",
     "\"C'è qualcosa che posso fare per aiutare?\""),
    ("uncharacteristic layer of thick cloud",
     "Mentre scendi verso la superficie di Martini, ti accoglie uno strato di nubi spesse e inconsuete, quasi "
     "fumose. Le nubi occultano completamente lo spazioporto principale di Martini, e anche il resto della "
     "capitale. Forse per questo il controllore di atterraggio ti ordina di dirigerti verso uno spazioporto "
     "ausiliario a una decina di chilometri dai confini della città."),
    ("makeshift field hospital",
     "Appena scendi dalla nave capisci che qualcosa non va affatto. Personale della Marina pesantemente armato "
     "fiancheggia l'uscita dell'edificio dello spazioporto, e altri soldati pattugliano il porto. La strada "
     "principale verso la città risuona di sirene, e un ufficiale di collegamento sta radunando un gruppo di civili "
     "verso un trasporto militare parcheggiato precariamente in un campo vicino. Altre persone ancora sono stese su "
     "brandine in un ospedale da campo improvvisato al centro dello spazioporto."),
    ("another transport fleet coming in",
     "Appena l'ultimo civile mobile è al sicuro sul trasporto, l'ufficiale di collegamento si volta verso di te. "
     "\"Mi dispiace, capitano, ma devo chiederti di lasciare il pianeta. Sta arrivando un'altra flotta di trasporti "
     "e ci servono tutte le piazzole libere.\""),
    ("quite possibly this same",
     "L'ufficiale di collegamento sospira. \"Capitano, temo che il pianeta sia in stato di emergenza. Ieri alcuni "
     "pianeti ribelli del sud hanno deciso di voler secedere dalla Repubblica. Hanno mandato al Parlamento un "
     "ultimatum: volevano la riforma elettorale e fiscale, il libero scambio, tutte le stesse cose di cui si "
     "lamentano da anni. Niente di grave. Tre ore fa, però, qualcuno - molto probabilmente questo stesso gruppo dei "
     "'Mondi Liberi' - ha sganciato una bomba nucleare sulla Borsa Galattica, proprio qui su Martini. Almeno, "
     "presumiamo che l'obiettivo fosse la Borsa, visto che la bomba ha portato via circa un quarto della città, "
     "oltre allo spazioporto principale e metà delle risorse mediche del pianeta. Abbiamo più di un milione di "
     "feriti e altri cinque milioni da evacuare. Per completare l'opera, i terroristi hanno bombardato anche "
     "l'Arsenale su Geminus, il che significa che non abbiamo abbastanza personale per gestire l'evacuazione e "
     "occuparci anche degli altri civili.\""),
    ("under martial law",
     "\"Ascolta, capitano. Il governo qui su <planet> ha dichiarato lo stato di emergenza, e questo significa che lo "
     "spazioporto è sotto legge marziale. Non so come tu abbia fatto a ottenere l'autorizzazione all'atterraggio, ma "
     "non dovresti essere qui. Abbiamo migliaia di feriti da portare fuori dal pianeta, anche ignorando la "
     "possibilità di un grande attacco di ritorsione. Se rifiuti di obbedire, ti farò arrestare dalla polizia "
     "militare e la tua nave sarà sequestrata. Se il tuo equipaggio rifiuterà il cambio di comando, sarà "
     "sostituito da truppe del Comando della Riserva Navale. Pensa quello che vuoi, ma qui abbiamo delle vite "
     "umane da salvare e non ci fermeremo solo perché un capitano presuntuoso si sente tanto importante. È "
     "chiaro?\""),
    ("that's clear",
     "\"Sì, è chiaro.\""),
    ("You won't have any trouble from me",
     "\"Scusa, non lo sapevo. Non avrai problemi da me.\""),
    ("No way are you going to seize my ship",
     "\"Certo, come no. Non ti azzarderai a sequestrare la mia nave.\""),
    ("Permanently Revoked",
     "L'ufficiale di collegamento ti lancia un'occhiataccia, poi si volta e fa cenno a un altro soldato. Agenti "
     "della polizia militare in tenuta da combattimento completa ti appaiono alle spalle, ti afferrano per le "
     "braccia e ti ammanettano stretto. Mentre ti portano via a forza verso un bunker, vedi la <ship> decollare "
     "senza di te e lasciarti bloccato qui. Nel bunker uno dei soldati che ti hanno arrestato ti perquisisce, ti "
     "sequestra la licenza di pilota e la consegna a un sergente che vi appone il timbro \"Revocata in via "
     "definitiva\". Con quelle due parole, ti è vietato lo spazio per sempre. È passato meno di un anno da quando "
     "hai comprato la tua nave, e hai già perso il diritto di usarla mentre la galassia ti crolla addosso."),
    ("Glad to hear it",
     "\"Ne sono felice\", rispondono, voltandosi a calmare un gruppo di Paradisiani isterici."),
    ("left the video screen in your ship on",
     "Rientri nella <ship>, decolli e ti dirigi in orbita, mancando per un soffio lo squadrone di navi portatrici "
     "di cui parlava l'ufficiale. Solo allora ti accorgi di aver lasciato acceso lo schermo video nella nave, che "
     "trasmette immagini quasi identiche a quelle che hai visto a terra poco fa. Secondo il giornalista, tutto "
     "questo disastro è cominciato ieri, quando un gruppo di pianeti del sud della galassia ha inviato al "
     "Parlamento della Repubblica un ultimatum: il rifiuto di pagare le tasse finché non saranno fatte riforme "
     "nell'elezione dei rappresentanti planetari. Questo gruppo, che si fa chiamare \"Mondi Liberi\", ha chiesto "
     "anche una rivalutazione immediata di tutti i dazi commerciali e delle norme sulla registrazione dei piloti. "
     "Il Parlamento ha rifiutato di prendere in considerazione una sola di queste richieste."),
    ("only hours before you landed",
     "Poi, solo poche ore prima del tuo atterraggio, esplosioni nucleari su Geminus e Martini hanno distrutto "
     "l'Arsenale della Marina della Repubblica e la Borsa Galattica, azzoppando il centro militare ed economico "
     "della Repubblica. I \"Mondi Liberi\" negano ogni responsabilità per gli attentati, nonostante i tempi e il "
     "fatto che questi servano molto bene ai loro scopi."),
    ("curt thank-you",
     "L'ufficiale di collegamento risponde con un ringraziamento secco e si volta a calmare un Paradisiano "
     "isterico. Rientri nella <ship> e ti prepari a decollare. È passato meno di un anno da quando hai comprato la "
     "tua nave, e la galassia ti sta già crollando addosso."),
    ("trained for responding to nuclear disasters",
     "\"Sì. Puoi decollare come ti ho chiesto.\" L'ufficiale fa una pausa. \"Scusa, capitano, ma è la verità. La "
     "Marina ha personale addestrato a rispondere ai disastri nucleari, e tutto quello che faresti qui adesso è "
     "occupare spazio. Se vuoi davvero aiutare, faresti meglio ad aspettare un giorno che coordiniamo per bene un "
     "piano di risposta al disastro con i pianeti vicini e le loro bacheche dei lavori.\""),
    ("interrupted by the shrieks",
     "L'ufficiale si volta, interrotto dalle strida di un Paradisiano nel panico. Rientri nella <ship> e ti prepari "
     "a decollare."),
]

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ST = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(ST.values()) == {'PENDING'}, {k: v for k, v in ST.items() if v != 'PENDING'}

assert collections.Counter(u['kind'] for u in SRC) == {'MISSION_TEXT': 41, 'DESCRIPTION': 9, 'LOGBOOK': 2}
assert sum(1 for u in SRC if u['kind'] == 'VALUE') == 0          # asserzione vuota, dichiarata
assert sum(1 for u in SRC if u['english'].startswith('\t')) == 41
assert sum(u['english'].count('"') for u in SRC) == 58
assert sum(u['english'].count('`') for u in SRC) == 0
ctx = collections.Counter(u['context'] for u in SRC)
assert len(ctx) == 3 and collections.Counter(ctx.values()) == {6: 1, 9: 1, 37: 1}, ctx
TOK = {'<ship>': 4, '<planet>': 1}
assert collections.Counter(t for u in SRC for t in TAGS.findall(u['english'])) == TOK

distinct = list(dict.fromkeys(ENG.values()))
assert len(distinct) == 45 and len(UNIQ) == 45, (len(distinct), len(UNIQ))


def resolve(eng):
    hits = [t for s, t in UNIQ if s in eng]
    assert len(hits) == 1, (len(hits), eng[:90], hits)
    return hits[0]


cover = {e: resolve(e) for e in distinct}
assert len(set(cover.values())) == 45, 'due testi distinti con la stessa resa'

T = {}
for u in SRC:
    eng, txt = u['english'], cover[u['english']]
    assert not txt.startswith('\t'), u['idx']
    T[u['idx']] = '\t' * (len(eng) - len(eng.lstrip('\t'))) + txt

for idx, txt in T.items():
    eng = ENG[idx]
    assert txt.count('\t') == eng.count('\t'), idx
    assert txt.count('"') == eng.count('"'), (idx, txt.count('"'), eng.count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng), (idx, TAGS.findall(txt), TAGS.findall(eng))
    assert not re.search(r'[\[\]`\u2019\u2014\u2013\u2026]', txt), idx
    assert not re.search(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", txt), idx
    assert txt.strip() and txt.strip() != eng.strip(), idx
    r = len(txt) / len(eng)
    assert 0.55 < r < 1.90, ('gate', idx, round(r, 3), eng[:60])

for n, (lo, hi) in enumerate(((1, 18), (19, 36), (37, 52))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('52 unita (18+18+16) · 45 testi distinti · 41 unita con tab · 58 virgolette · 5 token · 0 VALUE')
