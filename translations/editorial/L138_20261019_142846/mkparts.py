"""mkparts.py — L138: `data/starts.txt`, righe 215-358 (47 unita'). Quarto inizio: gli Hai.

**Due inizi con lo stesso nome**: `Hai Origins` alle righe 215 e 227 (1ª e 5ª unita'). Sono due blocchi distinti dello
stesso `start:hai space` (uno bloccato, uno sbloccabile), non un doppione: le due `DESCRIPTION` differiscono e le
`DESCRIPTION` finali dicono cose diverse («Questo inizio è bloccato» / «Per sbloccare questo inizio...»).

**Cinque unita' (10-14) sono le stesse di L135**: rilette dal suo `translation.json` dopo il confronto dell'inglese.

**Quattro unita' con UNA sola virgoletta** (26, 36, 37, 38 = righe 307, 327, 331, 335): il sorgente apre una battuta e
non la chiude. La resa riproduce il difetto, non lo ripara.

Numeri: 1.431.000 reso **1,431 milioni**, 0,3%, 4.836 al giorno, 1.132.000 reso **1,132 milioni**.
"""
import collections
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PARTS = os.path.join(HERE, 'parts')
PREV = os.path.join(L10N, 'staging/editorial/L135_20261019_131024/translation.json')
SRC = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units']
ENG = {u['idx']: u['english'] for u in SRC}
KEY = {i: e.lstrip('\t') for i, e in ENG.items()}
TAGS = re.compile(r'<[^<>]+>')

prev = {u['english']: u['italian'] for u in json.load(open(PREV, encoding='utf-8'))['units']}
SHARED = (10, 11, 12, 13, 14)

GREENWATER = ("Sei cresciuto su Greenwater, un mondo Hai dalla cultura ricca e mista grazie al suo clima. Sogni di "
              "possedere una flotta tutta tua da quando, bambino, ti hanno regalato astronavi giocattolo")
DOCKS = ("Ora, mentre il traghetto attracca allo spazioporto principale, senti che questo è l'inizio di una nuova vita "
         "come capitano.")

D = {
    1: "Hai Origins",
    2: GREENWATER + ". Per raggiungere quell'obiettivo hai lavorato sodo in un'agenzia di viaggi, consigliando "
       "destinazioni nello spazio umano.",
    3: DOCKS,
    4: "Questo inizio è bloccato.",
    5: "Hai Origins",
    6: GREENWATER + ", e hai lavorato sodo in un'agenzia di viaggi per raggiungere quell'obiettivo.",
    7: DOCKS,
    8: "Per sbloccare questo inizio devi completare la campagna umana principale.",
    9: "Finalmente ho messo insieme abbastanza soldi per un anticipo su un'astronave. Gli interessi sul mutuo sono "
       "esorbitanti.",
    15: "Gli Hai sono una specie di roditori giganti e intelligenti, che vivono a nord dello spazio umano. Permettono a "
        "qualunque umano scopra il loro territorio di vivere accanto a loro, di commerciare con loro e di acquistare "
        "la loro tecnologia.",
    16: "Gli \"Unfettered\" sono una fazione interna alla specie Hai, meno pacifica del resto e di norma non amichevole "
        "verso gli umani. Sostengono che molto tempo fa i Drak alterarono gli Hai per renderli docili e pacifici, e "
        "che gli Unfettered discendono da quegli Hai che evitarono quell'alterazione. Cercano motori di salto per "
        "fuggire dalla \"prigione\" in cui sono ora bloccati: alcuni mondi in degrado sul confine più settentrionale "
        "dello spazio Hai.",
    17: "Una specie estinta da tempo, simile a un drago, chiamata \"Sheragi\" viveva nello spazio umano, quando gran "
        "parte di quello che oggi è territorio umano era occupato dagli Hai.",
    18: "Andare al Polo Nord ti fa già sentire come su un altro mondo; anche solo all'interno della banchina del tuo "
        "traghetto vedi più Hai di quanti ce ne siano nella tua città natale. Dopo qualche annuncio dall'impianto "
        "audio, tu e gli altri passeggeri sbarcate, e il flusso di umanità si infrange contro la folla di Hai.",
    19: "Mentre ti dirigi verso il cantiere navale, apri la versione in lingua umana del tuo contratto di prestito per "
        "rileggerlo: hai preso in prestito 1,431 milioni di crediti, da restituire nell'arco di due anni. Il tuo tasso "
        "d'interesse è dello 0,3%, il che rende le tue rate 4.836 crediti al giorno.",
    20: "Alzi lo sguardo dal tablet appena prima di andare a sbattere contro un Hai dal pelo grigio in tuta da volo, "
        "facendolo cadere. Mentre ti chini per aiutarlo, lui dà un'occhiata ai documenti del tuo mutuo. \"Stai per "
        "diventare capitano, vero?\" dice dopo essersi spolverato.",
    21: "\"Sì, è così.\"",
    22: "\"Come hai fatto a capirlo?\"",
    23: "\"Chi ha detto che potevi guardare?\"",
    24: "\"Allora forse posso aiutarti. Seguimi.\"",
    25: "\"Dal tuo prestito,\" risponde. \"C'è una sola ragione per avere esattamente quel numero di crediti. A "
        "proposito, credo di poterti aiutare.\"",
    26: "Si gratta la nuca. \"Scusa. Volevo solo aiutare, ma se ti sto creando troppo disturbo, mi tolgo di mezzo.",
    27: "\"Non mi dispiace.\"",
    28: "\"Preferisco cavarmela da solo.\"",
    29: "Si inchina. \"Grazie.\"",
    30: "L'Hai ti porta alle piazzole di Greenwater, dove una gran folla di umani e Hai si è radunata attorno a diverse "
        "navi. Dalla folla un altro Hai si avvicina al tuo compagno e gli parla in Hai. L'Hai dal pelo grigio si "
        "limita a fare un cenno e consegna all'altro un mazzo di chiavi in cambio di un gettone di credito. L'altro "
        "Hai si inchina in fretta e corre verso una delle navi atterrate.",
    31: "\"Sto vendendo la mia flotta prima di andare in pensione,\" dice l'Hai. \"Certo, potrei semplicemente andare al "
        "cantiere navale, ma non avrei mai potuto cominciare se un altro capitano in pensione non mi avesse venduto "
        "una nave a poco prezzo quando ero giovane. Così ho deciso di restituire il favore e aiutare altri futuri "
        "capitani.\"",
    32: "L'Hai si avvicina a una delle navi più piccole della flotta, un intercettore Grasshopper. \"Questa è la "
        "Pristine Jewel. Mi ha servito bene nell'ultimo secolo, ma sono certo che sarà al sicuro nelle tue mani.\"",
    33: "\"Me la stai regalando?\"",
    34: "\"C'è un mercantile che potrei prendere al suo posto?\"",
    35: "\"E le altre persone qui? Non dovrebbero avere la precedenza?\"",
    36: "L'Hai ridacchia. \"Sarebbe bello, vero? Purtroppo la pensione non è economica. Sarei però felice di "
        "separarmene per 1,132 milioni di crediti; meno di un Aphid, figuriamoci di un Grasshopper nuovo.",
    37: "\"Purtroppo tutti i miei Aphid sono stati comprati stamattina. Comunque sono certo che sopravviverai; gli "
        "Unfettered saranno un osso duro, ma i pirati nello spazio umano non saranno un gran problema. E se proprio "
        "non ce la fai, puoi sempre venderla. Ti costerà solo 1,132 milioni di crediti, e potrai usare i pezzi vecchi "
        "della Pristine Jewel per comprare un Aphid con uno sconto.",
    38: "L'Hai scuote la testa. \"Non preoccuparti. La maggior parte della folla sono solo spettatori. Di solito è un "
        "capitano umano a fare un colpo di testa come vendere pubblicamente la propria flotta; la maggior parte degli "
        "Hai in pensione dona la flotta al governo. E non sto esattamente regalando queste navi. Se la vuoi, la "
        "Pristine Jewel costa 1,132 milioni di crediti.",
    39: "\"Allora, affare fatto?\"",
    40: "\"Affare fatto!\"",
    41: "\"Credo che mi converrebbe comprare dal cantiere navale.\"",
    42: "\"Ottimo!\" Tende un tablet. \"Firma qui e sarà tua.\"",
    43: "L'Hai ti dà le chiavi del Grasshopper dopo che gli hai consegnato il tablet e il pagamento. \"Sembra che "
        "questo sia il tuo primo passo per diventare un imprenditore interstellare. Direi che ci rivedremo un giorno, "
        "ma preferisco non mentire. In tutti questi anni non ho mai più incontrato il capitano che mi ha venduto la "
        "prima nave. Non che importi: questa è la tua storia, non la mia.\"",
    44: "Ti fa un ultimo saluto e torna tra la folla a vendere un'altra nave.",
    45: "Fa un cenno col capo mentre ti avvii verso il cantiere navale.",
    46: "All'ingresso c'è un chiosco di sicurezza automatico. Compili in fretta il modulo sullo schermo, poi prendi lo "
        "stilo e firmi il tuo nome:",
    47: "Attraversi porte scorrevoli di vetro ed entri nel cantiere di Greenwater. Nella maggior parte delle banchine "
        "gli operai sono impegnati a rimettere a nuovo vecchie navi per la rivendita, ma in alcune baie più lontane "
        "vedi il lampo delle torce di saldatura su scheletri di navi nuove di zecca. Navi di ogni dimensione sono "
        "allineate nel cantiere, ma per te c'è una sola opzione...",
}

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ST = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(ST.values()) == {'PENDING'}, {k: v for k, v in ST.items() if v != 'PENDING'}

assert collections.Counter(u['kind'] for u in SRC) == {'CONVERSATION': 32, 'LOGBOOK': 7, 'DESCRIPTION': 6, 'VALUE': 2}
assert sum(1 for u in SRC if u['english'].startswith('\t')) == 32
assert sum(u['english'].count('"') for u in SRC) == 56
odd = [(u['idx'], u['english'].count('"')) for u in SRC if u['english'].count('"') % 2]
assert odd == [(26, 1), (36, 1), (37, 1), (38, 1)], odd
ctx = collections.Counter(u['context'] for u in SRC)
assert list(ctx.items()) == [('start:hai space', 8), ('conversation:hai intro', 39)], list(ctx.items())
assert collections.Counter(t for u in SRC for t in TAGS.findall(u['english'])) == {}
assert [(u['idx'], ENG[u['idx']]) for u in SRC if u['kind'] == 'VALUE'] == [(1, 'Hai Origins'), (5, 'Hai Origins')]
assert [u['idx'] for u in SRC if u['kind'] == 'UI_LABEL'] == []
assert (min(u['line'] for u in SRC), max(u['line'] for u in SRC)) == (215, 358)

for k in SHARED:
    assert KEY[k] in prev, ('condivisa assente da L135', k, KEY[k][:50])
own = {i: D[i] for i in D}
assert sorted(own) == [1, 2, 3, 4, 5, 6, 7, 8, 9] + list(range(15, 48)), sorted(own)
assert len(own) == 42

T = {}
for u in SRC:
    eng = u['english']
    body = prev[KEY[u['idx']]] if u['idx'] in SHARED else own[u['idx']]
    T[u['idx']] = '\t' * (len(eng) - len(eng.lstrip('\t'))) + body.lstrip('\t')

for idx, txt in T.items():
    eng = ENG[idx]
    assert txt.count('\t') == eng.count('\t'), idx
    assert txt.count('"') == eng.count('"'), (idx, eng.count('"'), txt.count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng) == [], idx
    assert len(txt) - len(txt.rstrip()) == len(eng) - len(eng.rstrip()), ('spazio finale', idx)
    assert not re.search(r'[\[\]`\u2019\u2014\u2013\u2026]', txt), idx
    assert not re.search(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", txt), idx
    if idx in (1, 5):
        assert txt == eng, idx
    else:
        assert txt.strip() and txt.strip() != eng.strip(), idx
    r = len(txt) / len(eng)
    assert 0.55 < r < 1.90, ('gate', idx, round(r, 3), eng[:60])

for k in SHARED:
    assert T[k] == prev[KEY[k]], k

dup = {}
for u in SRC:
    dup.setdefault(KEY[u['idx']], set()).add(T[u['idx']])
assert not [(k, v) for k, v in dup.items() if len(v) > 1]
assert len(dup) == 45, len(dup)

for n, (lo, hi) in enumerate(((1, 10), (11, 20), (21, 30), (31, 40), (41, 47))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('47 unita (10+10+10+10+7) · 42 testi propri + 5 riletti da L135 · 45 distinti')
print('2 VALUE identici (Hai Origins, unita 1 e 5) · 32 tab · 56 virgolette · 4 dispari (26, 36, 37, 38)')
