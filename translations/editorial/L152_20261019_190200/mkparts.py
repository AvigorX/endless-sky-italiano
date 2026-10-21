"""mkparts.py — L152: `data/coalition/coalition jobs.txt`, righe 1191-1359 (21 unita').

Cambio di carattere: dopo i lavori brevi arrivano **`MISSION_TEXT`** e **`LOGBOOK`** (la vendita del motore di salto agli
Heliarch e le schede delle tre specie della Coalizione). Due unita' hanno il **tab** (17 e 18) e **una** ha le
virgolette (17): la battuta dell'Arach, che parla con l'inversione tipica della sua specie («Honor us you do»).

Le chiavi della mappa sono **senza tab**: il tab lo antepone il costruttore, contato dal sorgente.
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
TAGS = re.compile(r'<[^<>]+>')

MAP = {
    ('TEXT', 'The passengers thank you for bringing them to <planet> and pay you <payment>.'):
        'I passeggeri ti ringraziano per averli portati su <planet> e ti pagano <payment>.',
    ('VALUE', 'Spectators to <planet>'): 'Spectators to <planet>',
    ('DESCRIPTION', 'These <bunks> passengers will pay <payment> for transportation to <planet> in time for the '
                    'Coalition Games (by <date>).'):
        'Questi <bunks> passeggeri ti pagheranno <payment> per essere trasportati su <planet> in tempo per i Giochi '
        'della Coalizione (entro il <date>).',
    ('VALUE', 'Passengers to <planet>'): 'Passengers to <planet>',
    ('DESCRIPTION', 'Transport <bunks> passengers, who were on <origin> for the Coalition Games, back to their home '
                    'world of <destination>. Payment is <payment>.'):
        "Trasporta <bunks> passeggeri, che si trovavano su <origin> per i Giochi della Coalizione, sul loro mondo "
        "d'origine, <destination>. Il compenso è <payment>.",
    ('VALUE', 'Sell Jump Drive'): 'Sell Jump Drive',
    ('DESCRIPTION', 'Sell a jump drive to the Heliarchs for <payment>.'):
        'Vendi un motore di salto agli Heliarch per <payment>.',
    ('MISSION_TEXT', "The Heliarchs thank you profusely when they see you've taken them up on their offer, and soon "
                     "enough several of their ships have landed near your own. Apparently they've learned of your "
                     "change of mind and are excited to see the exchange, leaving their ships and surrounding yours. "
                     "Soon enough, they make space for an army of engineers to come and remove the spare jump drive "
                     "from your ship. Still watching the scene, only now in formations, the Heliarch agents whisper "
                     "among themselves, rarely shifting their eyes, as if looking at a spectacle."):
        "Gli Heliarch ti ringraziano profusamente quando vedono che hai accettato la loro offerta, e ben presto diverse "
        "loro navi sono atterrate accanto alla tua. A quanto pare hanno saputo che hai cambiato idea e sono ansiosi di "
        "assistere allo scambio: lasciano le navi e circondano la tua. Ben presto fanno spazio a un esercito di "
        "ingegneri che vengono a rimuovere il motore di salto di riserva dalla tua nave. Sempre a guardare la scena, ora "
        "però in formazioni, gli agenti Heliarch sussurrano fra loro, spostando di rado lo sguardo, come se assistessero "
        "a uno spettacolo.",
    ('MISSION_TEXT', "Once the drive is out of your ship, it is secured in an excessively reinforced container and "
                     "transported to a restricted section of the ring, under the guard of hundreds of armed soldiers. "
                     "One of the Heliarchs who seem to be in charge of the procedure, an Arach, personally comes to "
                     "you, thanking you again and handing you <payment>. \"Honor us you do with such generosity, "
                     "Captain. Though made great progress in studying jump drives and their mechanisms, we have, still "
                     "incapable of creating our own, we are, and means of acquiring new copies we have not. "
                     "Tremendously valuable, each and every drive you could bring us is. If interested in selling any "
                     "more jump drives, you are, continue to offer you such jobs, we will.\""):
        "Appena il motore è fuori dalla nave, viene sistemato in un contenitore eccessivamente rinforzato e "
        "trasportato in una sezione riservata dell'anello, sotto la scorta di centinaia di soldati armati. Uno degli "
        "Heliarch che sembrano dirigere la procedura, un Arach, viene personalmente da te, ringraziandoti ancora e "
        "consegnandoti <payment>. \"Ci onori con tanta generosità, capitano. Sebbene grandi progressi nello studio dei "
        "motori di salto e dei loro meccanismi abbiamo fatto, ancora incapaci di crearne uno nostro siamo, e mezzi per "
        "procurarcene nuove copie non abbiamo. Enormemente prezioso è ogni singolo motore che potresti portarci. Se "
        "interessato a vendere altri motori di salto sei, continueremo a offrirti lavori simili.\"",
    ('MISSION_TEXT', 'She thanks you yet again, salutes, and leaves to follow the entourage guarding the newly '
                     'purchased jump drive.'):
        "Ti ringrazia ancora una volta, fa il saluto e si allontana per seguire il corteo che scorta il motore di "
        "salto appena acquistato.",
    ('LOGBOOK', 'Sold a jump drive to the Heliarchs and received permission to purchase Coalition civilian technology '
                'and ships.'):
        'Ho venduto un motore di salto agli Heliarch e ho ricevuto il permesso di acquistare tecnologia e navi civili '
        'della Coalizione.',
    ('LOGBOOK', 'Saryds are an alien species who look suspiciously similar to the centaurs found in early human '
                'mythology. They prefer to live on worlds with as much green space as possible, and even their major '
                'cities are full of parks and gardens. Most Saryds live in small communes with up to a few dozen of '
                'them per house.'):
        'I Saryd sono una specie aliena che somiglia in modo sospetto ai centauri della mitologia umana delle origini. '
        'Preferiscono vivere su mondi con quanta più vegetazione possibile, e perfino le loro grandi città sono piene di '
        'parchi e giardini. La maggior parte dei Saryd vive in piccole comunità, con al massimo qualche decina di '
        'individui per casa.',
    ('LOGBOOK', 'The Kimek are large insectoid aliens, and are members of the Coalition. They discovered spaceflight '
                'after the Saryds, but before the Arachi. They are intensely social creatures, preferring to live '
                'together in massive buildings with thousands of inhabitants, and many of their worlds have '
                'populations in the tens of billions, far more than any human world.'):
        'I Kimek sono grandi alieni insettoidi e fanno parte della Coalizione. Hanno scoperto il volo spaziale dopo i '
        'Saryd, ma prima degli Arachi. Sono creature intensamente sociali, che preferiscono vivere insieme in edifici '
        'enormi con migliaia di abitanti, e molti dei loro mondi hanno popolazioni nell\'ordine delle decine di '
        'miliardi, molto più di qualunque mondo umano.',
}

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ST = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(ST.values()) == {'PENDING'}, {k: v for k, v in ST.items() if v != 'PENDING'}

assert collections.Counter(u['kind'] for u in SRC) == {'TEXT': 1, 'VALUE': 7, 'DESCRIPTION': 7, 'MISSION_TEXT': 3,
                                                       'LOGBOOK': 3}
assert sum(1 for u in SRC if u['english'].startswith('\t')) == 2
assert [u['idx'] for u in SRC if u['english'].startswith('\t')] == [17, 18]
assert sum(u['english'].count('"') for u in SRC) == 2
assert [u['idx'] for u in SRC if u['english'].count('"')] == [17]
assert len(set(u['context'] for u in SRC)) == 8
tok = collections.Counter(t for u in SRC for t in TAGS.findall(u['english']))
assert dict(tok) == {'<planet>': 10, '<payment>': 9, '<bunks>': 6, '<date>': 3, '<origin>': 3,
                     '<destination>': 3}, dict(tok)
assert sum(tok.values()) == 34
assert (min(u['line'] for u in SRC), max(u['line'] for u in SRC)) == (1191, 1359)
assert len({(u['kind'], u['english'].lstrip('\t')) for u in SRC}) == 13
for u in SRC:
    assert (u['kind'], u['english'].lstrip('\t')) in MAP, (u['idx'], u['kind'], u['english'][:60])

T = {}
for u in SRC:
    eng = u['english']
    tabs = len(eng) - len(eng.lstrip('\t'))
    T[u['idx']] = '\t' * tabs + MAP[(u['kind'], eng.lstrip('\t'))].lstrip('\t')

for idx, txt in T.items():
    eng = ENG[idx]
    assert txt.count('\t') == eng.count('\t'), (idx, txt.count('\t'), eng.count('\t'))
    assert txt.count('"') == eng.count('"'), (idx, eng.count('"'), txt.count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng), (idx, TAGS.findall(txt), TAGS.findall(eng))
    assert len(txt) - len(txt.rstrip()) == len(eng) - len(eng.rstrip()), ('spazio finale', idx)
    assert not re.search(r'[\[\]`\u2019\u2014\u2013\u2026]', txt), idx
    assert not re.search(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", txt), idx
    if SRC[idx - 1]['kind'] == 'VALUE':
        assert txt == eng.rstrip(), idx
    else:
        assert txt.strip() and txt.strip() != eng.strip(), idx
    r = len(txt) / len(eng)
    assert 0.55 < r < 1.90, ('gate', idx, round(r, 3), eng[:60])

per = collections.Counter(t for i, txt in T.items() for t in TAGS.findall(txt))
assert dict(per) == dict(tok), (dict(per), dict(tok))
dup = {}
for u in SRC:
    dup.setdefault(u['english'].lstrip('\t').rstrip(), set()).add(T[u['idx']].lstrip('\t'))
assert not [(k, v) for k, v in dup.items() if len(v) > 1]
assert len(dup) == 13, len(dup)
assert 'ci onori' in T[17].lower() and T[17].count('"') == 2

for n, (lo, hi) in enumerate(((1, 7), (8, 14), (15, 21))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('21 unita (7+7+7) · 7 VALUE + 7 DESCRIPTION + 3 MISSION_TEXT + 3 LOGBOOK + 1 TEXT · 8 contesti · 13 testi distinti')
print('34 token su 6 simboli · 2 unita con tab (17, 18) · 1 unita con le virgolette (17, l Arach)')
