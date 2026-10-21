"""mkparts.py — L125: chiude `data/human/ships.txt` (20 unita', righe 3491-4266, `fine file`).

Coda del file: **20 `DESCRIPTION`**, **nessun `VALUE`**, **zero token**, **15 contesti** (10×1, 5×2), **5 unita'
con tab**, **14 virgolette**, **20 testi distinti**.

- **Nessun `VALUE`**: l'asserzione «i `VALUE` sono identici al sorgente» e' **vuota** e viene scritta come tale.
- **Zero token**: asserzione (`== {}`), non omissione.
- **1 testo viene da L123/L124** (la nota sui droni): resa riletta e confrontata.
"""
import collections
import glob
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

PREV = {}
for lot in ('L123_*', 'L124_*'):
    for f in glob.glob(os.path.join(L10N, 'staging/editorial', lot, 'translation.json')):
        for u in json.load(open(f, encoding='utf-8'))['units']:
            PREV[u['english']] = u['italian']

UNIQ = [
    ("fighter-carrying containers",
     "I nuovi container portacaccia dei Southbound Shipyards hanno dato un nuovo impiego a quello che molti "
     "consideravano un progetto superato. Quattro baie di caccia esterne ne fanno la più grande portatrice civile "
     "sul mercato, sebbene un po' sgraziata come nave da guerra. Dopo che gli operai della linea di montaggio "
     "Southbound ebbero battezzato con successo la \"Nest\", la \"Hauler II: Type F\" fu subito ribattezzata "
     "\"Roost\" per continuare il tema."),
    ("caravan era",
     "Durante l'era delle carovane, un boom di sviluppo economico si diffuse lungo le rotte delle flotte mercantili "
     "più armate e tecnologicamente avanzate provenienti dal Deep, il che portò allo sviluppo di navi come la Saber. "
     "Questa nave da guerra media fu una delle potenze militari della sua epoca, armata fino ai denti con cinque "
     "portelli per cannoni a prua e un alloggiamento per torretta dorsale per sparare a tutto ciò che non fosse "
     "davanti. Quando i pirati iniziarono a unirsi in bande più grandi in risposta ai mercanti meglio difesi, la "
     "Saber divenne popolare anche tra loro. A differenza di altre navi come la Firebird, sbiadì lentamente con "
     "l'aumentare della concorrenza, ma resta comunque cara a chi ne possiede ancora una."),
    ("Scoutship was designed back in the days",
     "La Lionheart Scoutship fu progettata ai tempi in cui la galassia era più scarsamente popolata, e le navi che "
     "cercavano mondi abitabili o ricchi di risorse viaggiavano spesso lontano da qualsiasi porto abitato dove "
     "potersi rifornire. Sebbene la galassia sia ormai esplorata molto più a fondo, la Scout resta una nave "
     "popolare per i viaggi a lungo raggio."),
    ("family of vessels cobbled together",
     "Più che un modello specifico di nave, gli Scrapper sono una famiglia di vascelli messi insieme con i resti di "
     "shuttle rotti. Nelle rare occasioni in cui le autorità della Repubblica si curano di riconoscerne "
     "l'esistenza, gli Scrapper sono trattati come trappole mortali quasi illegali e in violazione di brevetto. "
     "Nonostante ciò, è su queste navi che molti capitani (e pirati) di origini povere iniziano."),
    ("majority of their profits come from sales of the Shuttle",
     "Sebbene i Betelgeuse Shipyards producano anche altri modelli, la maggior parte dei loro profitti viene dalla "
     "vendita della Shuttle. Questa nave versatile serve ugualmente bene come trasporto passeggeri o come corriere "
     "di carico. È anche la nave più economica che si possa comprare capace di viaggiare nell'iperspazio."),
    ("as useless as a blaster cannon",
     "Gli Shuttle non sono progettati per resistere a combattimenti di alcun tipo, ma sono abbastanza veloci e "
     "manovrabili da togliersi dai guai se attaccati da una nave più grande e lenta. Sebbene di solito siano "
     "disarmati, hanno spazio per un'arma, ed è da qui che viene il detto popolare \"inutile come un cannone "
     "blaster su uno shuttle\"."),
    ("cockpit and engine set",
     "Questo particolare insieme di abitacolo e motore si è ritrovato attaccato a tre dei nuovi pod portacaccia "
     "\"Type F\" dei Southbound Shipyards. Quando i Mondi Liberi chiesero una portatrice, non si aspettavano una "
     "nave in grado di trasportare quasi tanti caccia quante le navi da guerra più pesanti della Marina. Visto "
     "questo, i Mondi Liberi hanno chiesto ai Southbound e ai Tarazed di limitare la vendita della \"Hauler III: "
     "Type F\", la \"Skein\", alla sola milizia."),
    ("Classified as an interceptor rather than a fighter",
     "Classificata come intercettore anziché come caccia perché ha una propria iperguida invece di dover essere "
     "trasportata dentro una nave più grande, la Tarazed Sparrow è la nave da combattimento più piccola ed "
     "economica disponibile. A causa del poco spazio per carico e passeggeri, il modo principale con cui un pilota "
     "di Sparrow paga i conti è potenziare le armi e dare la caccia ai pirati... o diventarlo. In entrambi i casi, "
     "è un modo pericoloso di guadagnarsi da vivere."),
    ("two out of every three first-time ship buyers",
     "I rapporti governativi indicano che ben due su tre degli acquirenti di prima nave che scelgono di pilotare "
     "una Sparrow perdono la nave (e spesso anche la vita) entro il primo mese dal possesso. I piloti sopravvissuti "
     "più a lungo tendono a giurare di sostituire le armi di serie con lanciatori di missili."),
    ("largest warship produced by the Megaparsec shipyard",
     "La Splinter è la più grande nave da guerra prodotta dal cantiere Megaparsec. È progettata per essere più "
     "veloce e manovrabile di altre navi di dimensioni simili, per servire come nave scorta pesante o come parte di "
     "una flotta di difesa e pattuglia planetaria. Data la destinazione d'uso nei convogli mercantili, ha anche un "
     "discreto spazio per il carico."),
    ("cluster of cargo containers",
     "Il Syndicate CT-50 Star Barge è poco più di un grappolo di container da carico con un motore a un'estremità e "
     "un abitacolo all'altra. È una nave lenta e brutta, ma può portare abbastanza carico da garantire al capitano "
     "un reddito stabile anche nelle parti della galassia dove è difficile trovare passeggeri o missioni da "
     "corriere."),
    ("common target of pirates",
     "Poiché trasportano spesso carichi di valore, e poiché sono troppo lente per evitare qualsiasi attaccante, le "
     "Star Barge sono un bersaglio comune dei pirati."),
    ("luxury liner for high-end tourists",
     "La Star Queen è un reperto di un periodo più pacifico della storia galattica: un transatlantico di lusso per "
     "turisti facoltosi. Ogni cabina ha il suo minibar, e i bagni hanno piastrelle di marmo e docce che usano vera "
     "acqua calda invece di prodotti chimici o vibrazioni soniche."),
    ("solar panels as their only source of energy",
     "A sostegno dei movimenti ambientalisti di tutta la galassia, tutte le Star Queen escono di serie con una "
     "serie di pannelli solari come unica fonte di energia, al posto dei più diffusi generatori come celle a "
     "combustibile o reattori nucleari che producono una certa quantità di scorie. Sebbene alcuni sostengano che "
     "sia una scelta inutile data la diffusione dei reattori a fusione puliti, altri l'hanno applaudita e hanno "
     "citato i costi proibitivi dei reattori a fusione come ragione per usare i pannelli solari."),
    ("versatile mining platform",
     "La Sunder è una piattaforma mineraria versatile equipaggiata con attrezzature di prospezione dedicate, in "
     "particolare un sottoscocca che sostiene due Mining Drone. La discendenza di questa nave risale alle vecchie "
     "navi minerarie per asteroidi usate secoli fa nella Cintura Principale del Sol; tuttavia, a causa dei recenti "
     "sforzi del Sindacato per sfruttare ulteriormente la ricchezza mineraria del Nucleo, l'ultimo modello della "
     "Sunder è ora prodotto dai Syndicated Shipyards."),
    ("unarmed drones used by the Republic navy",
     "I droni da sorveglianza sono droni disarmati usati dalla Marina della Repubblica per scansionare navi e "
     "pianeti in un sistema stellare."),
    ("modified Aeries",
     "Le Valkyrie sono Aerie modificate che convertono due delle loro baie e lo spazio per le cuccette in più spazio "
     "per il carico destinato al contrabbando, oltre a più spazio per montare due alloggiamenti per cannoni "
     "aggiuntivi e una maggiore protezione corazzata. Questo permette alle Valkyrie di incassare e infliggere "
     "quantità notevoli di danni, ma a causa del peso extra sono un po' più lente e perdono un po' di efficienza "
     "degli scudi."),
    ("heavy anti-pirate defense market",
     "La Vanguard è la più recente nave da guerra della Syndicated Systems destinata al mercato della difesa "
     "pesante antipirateria. Le Vanguard offrono una dotazione inusuale, incentrata su potenti cannoni fissi e sulle "
     "più recenti tecnologie di automazione della Syndicated Systems, con il risultato di un equipaggio "
     "insolitamente ridotto per una nave di quelle dimensioni. Poche navi capitali resistono a lungo sotto la "
     "fucileria sferzante che può scatenare contro chi le sta davanti."),
    ("medium-strength interceptor",
     "La Wasp è un intercettore di forza media, progettato dai Syndicated Shipyards per servire come scorta alle "
     "navi da carico. Come la maggior parte delle navi del Sindacato non è particolarmente bella, ma almeno serve "
     "allo scopo per cui è stata costruita."),
]

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ST = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(ST.values()) == {'PENDING'}, {k: v for k, v in ST.items() if v != 'PENDING'}

assert collections.Counter(u['kind'] for u in SRC) == {'DESCRIPTION': 20}
assert sum(1 for u in SRC if u['kind'] == 'VALUE') == 0            # asserzione vuota, dichiarata
assert sum(1 for u in SRC if u['english'].startswith('\t')) == 5
assert sum(u['english'].count('"') for u in SRC) == 14
ctx = collections.Counter(u['context'] for u in SRC)
assert len(ctx) == 15 and collections.Counter(ctx.values()) == {1: 10, 2: 5}, ctx
assert collections.Counter(t for u in SRC for t in TAGS.findall(u['english'])) == {}   # zero token

distinct = list(dict.fromkeys(ENG.values()))
assert len(distinct) == 20, len(distinct)
reused = [e for e in distinct if e in PREV]
assert len(reused) == 1, reused
assert len(UNIQ) == 19, len(UNIQ)


def resolve(eng):
    if eng in PREV:
        return PREV[eng]
    hits = [t for s, t in UNIQ if s in eng]
    assert len(hits) == 1, (len(hits), eng[:90], hits)
    return hits[0]


cover = {e: resolve(e) for e in distinct}
assert len(set(cover.values())) == 20, 'due testi distinti con la stessa resa'

T = {}
for u in SRC:
    eng = u['english']
    T[u['idx']] = '\t' * (len(eng) - len(eng.lstrip('\t'))) + cover[eng].lstrip('\t')

for idx, txt in T.items():
    eng = ENG[idx]
    assert txt.count('\t') == eng.count('\t'), idx
    assert txt.count('"') == eng.count('"'), (idx, eng.count('"'), txt.count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng) == [], idx
    assert not re.search(r'[\[\]`\u2019\u2014\u2013\u2026]', txt), idx
    assert not re.search(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", txt), idx
    assert txt.strip() and txt.strip() != eng.strip(), idx
    r = len(txt) / len(eng)
    assert 0.55 < r < 1.90, ('gate', idx, round(r, 3), eng[:60])

for n, (lo, hi) in enumerate(((1, 10), (11, 20))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('20 unita (10+10) · 20 testi distinti · 0 VALUE · 0 token · 1 nota da L123/L124 · 5 tab · 14 virgolette')
