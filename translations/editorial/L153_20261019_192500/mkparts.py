"""mkparts.py — L153: `data/coalition/coalition jobs.txt`, righe 1360-1469 (20 unita').

La delegazione delle tre specie: il Saryd e il Kimek parlano normale, **l'Arach inverte le frasi** («like all civilians
… to you our weapons and warships we still cannot sell»). La resa conserva l'inversione, come in L152.

Poi tre lavori `Contain Criminals` quasi identici, che differiscono per **una parola** («on site» / «on the site»): la
resa li distingue («sul posto» / «sul luogo»), e i tre `DIALOG` raccontano esiti diversi (successo, fuga, sorpresa).

La descrizione `Sell a jump drive to the Heliarchs for <payment>.` esiste gia' in L152: **riletta** dopo aver verificato
che l'inglese sia identico.
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

PREV152 = json.load(open(os.path.join(L10N, 'staging/editorial/L152_20261019_190200/translation.json'),
                         encoding='utf-8'))['units']
P152 = {u['english']: u['italian'] for u in PREV152}

DESC_152 = 'Sell a jump drive to the Heliarchs for <payment>.'
assert DESC_152 in P152, 'la descrizione della vendita non e in L152'

MAP = {
    ('LOGBOOK', 'The spider-like Arachi were the last of the three Coalition species to discover interstellar travel. '
                'Most members of their society owe allegiance to one of the great Arach "Houses," organizations that '
                'are somewhat similar to guilds and that each specialize in one particular form of industry or '
                'technology.'):
        "Gli Arachi, simili a ragni, sono stati l'ultima delle tre specie della Coalizione a scoprire il viaggio "
        "interstellare. La maggior parte dei membri della loro società deve fedeltà a una delle grandi \"Case\" Arach, "
        "organizzazioni in qualche modo simili a corporazioni, ognuna specializzata in una particolare forma di "
        "industria o tecnologia.",
    ('MISSION_TEXT', 'She thanks you yet again, salutes, and leaves to follow the entourage guarding the newly '
                     'purchased jump drive. Not a minute after she has left, three more Heliarchs arrive at your ship, '
                     'a delegation consisting of a member of each of the three Coalition species, all wearing golden '
                     'circlets denoting their rank and authority. "A most unexpected, but greatly value contribution '
                     'this is," the Saryd says, "to think that so eager would our visitor be to prove their diligence '
                     'and commitment."'):
        "Ti ringrazia ancora una volta, fa il saluto e si allontana per seguire il corteo che scorta il motore di "
        "salto appena acquistato. Nemmeno un minuto dopo che se n'è andata, altre tre Heliarch arrivano alla tua nave: "
        "una delegazione composta da un membro di ciascuna delle tre specie della Coalizione, tutti con cerchietti d'oro "
        "che indicano rango e autorità. \"Un contributo del tutto inatteso, ma di grande valore è questo,\" dice il "
        "Saryd, \"pensare a quanto fosse desideroso il nostro visitatore di dimostrare diligenza e impegno.\"",
    ('MISSION_TEXT', 'The Kimek says, "As aided you have our society in breaking free of the Quarg\'s cages, with our '
                     'society\'s technology may you be trusted."'):
        "Il Kimek dice: \"Come hai aiutato la nostra società a liberarsi dalle gabbie dei Quarg, così della tecnologia "
        "della nostra società puoi fidarti.\"",
    ('MISSION_TEXT', '"But," says the Arach, "like all civilians, even citizens, to you our weapons and warships we '
                     'still cannot sell."'):
        "\"Ma,\" dice l'Arach, \"come a tutti i civili, e perfino ai cittadini, a te le nostre armi e le nostre navi da "
        "guerra ancora non possiamo vendere.\"",
    ('MISSION_TEXT', '"Thank you."'): "\"Grazie.\"",
    ('MISSION_TEXT', '"Why don\'t you allow civilians to purchase weapons or warships?"'):
        "\"Perché non permettete ai civili di acquistare armi o navi da guerra?\"",
    ('MISSION_TEXT', '"For the sake of peace it is," says the Saryd. "The Heliarch military, well-trained to use '
                     'weapons only for defense and only for justice, they are. And to place the needs of the Coalition '
                     'over the ambitions of their own native species, each one committed is. No such discipline do '
                     'civilians have, even you. But as a respectful guest you are, to maintain your weapons we shall '
                     'allow."'):
        "\"Per amore della pace,\" dice il Saryd. \"L'esercito Heliarch, ben addestrato a usare le armi solo per difesa "
        "e solo per giustizia, è. E a mettere i bisogni della Coalizione sopra le ambizioni della propria specie "
        "d'origine, ognuno è impegnato. Nessuna disciplina simile hanno i civili, nemmeno tu. Ma poiché un ospite "
        "rispettoso sei, a mantenere le tue armi ti permetteremo.\"",
    ('MISSION_TEXT', 'Apparently nothing is for sale here, but they assure you that many Coalition worlds will now '
                     'grant you access to their shipyards and outfitters. The three Heliarchs all express their deep '
                     'gratitude for your generosity with providing them a fresh jump drive, and wish you well.'):
        "A quanto pare qui non c'è niente in vendita, ma ti assicurano che molti mondi della Coalizione ti daranno ora "
        "accesso ai loro cantieri e ai loro fornitori. I tre Heliarch esprimono tutti la loro profonda gratitudine per "
        "la generosità con cui hai fornito loro un motore di salto nuovo, e ti augurano il meglio.",
    ('VALUE', 'Sell Jump Drive'): 'Sell Jump Drive',
    ('DESCRIPTION', DESC_152): P152[DESC_152],
    ('DIALOG', 'A team of Heliarch engineers carefully removes the spare jump drive from your ship and brings it to a '
               'restricted section of the ring. You\'re approached by the Heliarch who supervised the procedure, who '
               'thanks you for bringing in another drive, and hands you the pay of <payment>.'):
        "Una squadra di ingegneri Heliarch rimuove con cura il motore di salto di riserva dalla tua nave e lo porta in "
        "una sezione riservata dell'anello. Ti si avvicina l'Heliarch che ha sovrinteso alla procedura, che ti ringrazia "
        "per aver portato un altro motore e ti consegna il compenso di <payment>.",
    ('VALUE', 'Contain Criminals'): 'Contain Criminals',
    ('DESCRIPTION', 'Fly to <destination> by <date> so that you and <bunks> other Heliarch agents can combat criminals '
                    'on site. Payment is <payment>.'):
        'Vola a <destination> entro il <date> così che tu e altri <bunks> agenti Heliarch possiate combattere i '
        'criminali sul posto. Il compenso è <payment>.',
    ('DESCRIPTION', 'Fly to <destination> by <date> so that you and <bunks> other Heliarch agents can combat criminals '
                    'on the site. Payment is <payment>.'):
        'Vola a <destination> entro il <date> così che tu e altri <bunks> agenti Heliarch possiate combattere i '
        'criminali sul luogo. Il compenso è <payment>.',
    ('DIALOG', "You and the other agents converge on the marked area and quickly move to cut off any exits. After a "
               "brief firefight, the criminals surrender and a Heliarch ship swoops in to pick them up. You bid your "
               "Heliarch colleagues farewell and return to your ship, where you are happy to see that <payment> have "
               "already been transferred to your account."):
        "Tu e gli altri agenti convergete sull'area indicata e vi muovete rapidamente per tagliare ogni via di fuga. "
        "Dopo un breve scontro a fuoco i criminali si arrendono e una nave Heliarch piomba a prelevarli. Saluti i "
        "colleghi Heliarch e torni alla tua nave, dove scopri con piacere che <payment> sono già stati trasferiti sul "
        "tuo conto.",
    ('DIALOG', 'You and the other agents head to the marked area, but when you arrive it becomes evident that whoever '
               'occupied the place has managed to escape. You bring the other agents to the spaceport as they lament '
               'the failed job.'):
        "Tu e gli altri agenti vi dirigete verso l'area indicata, ma quando arrivate è evidente che chiunque occupasse il "
        "posto è riuscito a fuggire. Riporti gli altri agenti allo spazioporto mentre si lamentano del lavoro fallito.",
    ('DIALOG', 'Your team pounces and catches the targets entirely by surprise. They offer no resistance, '
               'relinquishing their weapons immediately. You call for a Heliarch ship to pick them up and then bid the '
               'other agents farewell as you leave. An extra <payment> is already waiting in your account when you '
               'return to your ship.'):
        "La tua squadra piomba sui bersagli e li coglie del tutto di sorpresa. Non oppongono resistenza e consegnano "
        "subito le armi. Chiami una nave Heliarch perché li prelevi e poi saluti gli altri agenti mentre te ne vai. Un "
        "<payment> extra ti aspetta già sul conto quando torni alla tua nave.",
}

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ST = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(ST.values()) == {'PENDING'}, {k: v for k, v in ST.items() if v != 'PENDING'}

assert collections.Counter(u['kind'] for u in SRC) == {'LOGBOOK': 1, 'MISSION_TEXT': 7, 'VALUE': 4, 'DESCRIPTION': 4,
                                                       'DIALOG': 4}
assert sum(1 for u in SRC if u['english'].startswith('\t')) == 7
assert sum(u['english'].count('"') for u in SRC) == 20
assert [u['idx'] for u in SRC if u['english'].count('"') % 2] == []
tok = collections.Counter(t for u in SRC for t in TAGS.findall(u['english']))
assert dict(tok) == {'<payment>': 7, '<destination>': 3, '<date>': 3, '<bunks>': 3}, dict(tok)
assert sum(tok.values()) == 16
assert (min(u['line'] for u in SRC), max(u['line'] for u in SRC)) == (1360, 1469)
assert len({(u['kind'], u['english'].lstrip('\t')) for u in SRC}) == 17
for u in SRC:
    assert (u['kind'], u['english'].lstrip('\t')) in MAP, (u['idx'], u['kind'], u['english'][:60])
# le due descrizioni «Contain Criminals» differiscono per una parola
assert ENG[12].replace('on site', 'on the site') == ENG[18]

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
assert len(dup) == 17, len(dup)
assert T[10] == P152[DESC_152]
assert 'sul posto' in T[13]
assert 'sul luogo' in T[19] and 'sul posto' not in T[19]
assert 'ancora non possiamo vendere' in T[4]

for n, (lo, hi) in enumerate(((1, 7), (8, 14), (15, 20))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('20 unita (7+7+6) · 1 LOGBOOK + 7 MISSION_TEXT + 4 VALUE + 4 DESCRIPTION + 4 DIALOG · 17 testi distinti')
print('16 token su 4 simboli · 7 tab · 20 virgolette · 1 frase riletta da L152')
