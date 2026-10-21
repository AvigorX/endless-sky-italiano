"""mkparts.py — L151: `data/coalition/coalition jobs.txt`, righe 799-1171 (37 unita').

Le unita' sono **corte** e i testi si ripetono: 37 unita' ma solo **14 stringhe distinte**. La resa e' quindi una mappa
per **stringa inglese**, non una traduzione per unita' — cosi' due copie dello stesso testo non possono divergere.

`Cargo 1..4` e `Bulk 1..4` condividono **la stessa `DESCRIPTION`** (`Deliver <cargo> to <destination>. Payment is
<payment>.`): 8 unita', una resa. `Fast Courier` ha la variante con `<date>` e `Rush` quella con «needs a shipment».
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
KEY = {i: e.rstrip() for i, e in ENG.items()}
TAGS = re.compile(r'<[^<>]+>')

MAP = {
    ('VALUE', 'Fast courier to <planet>'): 'Fast courier to <planet>',
    ('DESCRIPTION', 'Deliver <cargo> to <destination> by <date>. The payment is <payment>.'):
        'Consegna <cargo> a <destination> entro il <date>. Il compenso è <payment>.',
    ('TEXT', 'You drop off the <commodity> on <planet>, and receive <payment> in payment.'):
        'Scarichi il <commodity> su <planet> e ricevi <payment> come compenso.',
    ('VALUE', 'Cargo to <planet>'): 'Cargo to <planet>',
    ('DESCRIPTION', 'Deliver <cargo> to <destination>. Payment is <payment>.'):
        'Consegna <cargo> a <destination>. Il compenso è <payment>.',
    ('VALUE', 'Bulk cargo to <planet>'): 'Bulk cargo to <planet>',
    ('VALUE', 'Rush Delivery to <planet>'): 'Rush Delivery to <planet>',
    ('DESCRIPTION', '<destination> needs a shipment of <cargo> by <date>. Payment will be <payment>.'):
        '<destination> ha bisogno di una partita di <cargo> entro il <date>. Il compenso sarà <payment>.',
    ('VALUE', 'Doctors to <planet>'): 'Doctors to <planet>',
    ('DESCRIPTION', 'The government will pay you <payment> to bring this team of <bunks> doctors to <destination>, to '
                    'address a viral outbreak. They must arrive by <date>.'):
        "Il governo ti pagherà <payment> per portare questa squadra di <bunks> medici a <destination>, per fronteggiare "
        "un'epidemia virale. Devono arrivare entro il <date>.",
    ('DIALOG', 'The doctors methodically pack up their equipment and leave your ship. From their lack of urgency, it '
               'appears that this is a routine event, not a crisis. A few minutes later you receive a transfer of '
               '<payment>.'):
        'I medici ripongono metodicamente la loro attrezzatura e lasciano la nave. Dalla loro mancanza di fretta sembra '
        'che si tratti di un evento di routine, non di una crisi. Pochi minuti dopo ricevi un bonifico di <payment>.',
    ('TEXT', 'You drop off the cadets on <planet>. A few minutes later you receive a transfer of <payment>.'):
        'Scarichi gli allievi su <planet>. Pochi minuti dopo ricevi un bonifico di <payment>.',
    ('VALUE', 'Cadets to <planet>'): 'Cadets to <planet>',
    ('DESCRIPTION', 'These <bunks> new recruits need transport to the Academy on <destination>. Payment is <payment>.'):
        "Queste <bunks> reclute hanno bisogno di essere trasportate all'Accademia su <destination>. Il compenso è "
        "<payment>.",
}

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ST = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(ST.values()) == {'PENDING'}, {k: v for k, v in ST.items() if v != 'PENDING'}

assert collections.Counter(u['kind'] for u in SRC) == {'VALUE': 17, 'DESCRIPTION': 17, 'TEXT': 2, 'DIALOG': 1}
assert sum(1 for u in SRC if u['english'].startswith('\t')) == 0
assert sum(u['english'].count('"') for u in SRC) == 0
assert [u['idx'] for u in SRC if u['kind'] in ('LOGBOOK', 'UI_LABEL')] == []
assert [u['idx'] for u in SRC if u['kind'] == 'DIALOG'] == [32]
assert len(set(u['context'] for u in SRC)) == 19
tok = collections.Counter(t for u in SRC for t in TAGS.findall(u['english']))
assert dict(tok) == {'<planet>': 19, '<payment>': 20, '<destination>': 17, '<cargo>': 14, '<date>': 7,
                     '<bunks>': 3, '<commodity>': 1}, dict(tok)
assert sum(tok.values()) == 81
assert (min(u['line'] for u in SRC), max(u['line'] for u in SRC)) == (799, 1171)
assert len({(u['kind'], u['english']) for u in SRC}) == 14
for u in SRC:
    assert (u['kind'], u['english']) in MAP, (u['idx'], u['kind'], u['english'][:50])

T = {u['idx']: MAP[(u['kind'], u['english'])] for u in SRC}

for idx, txt in T.items():
    eng = ENG[idx]
    assert txt.count('\t') == eng.count('\t') == 0, idx
    assert txt.count('"') == eng.count('"') == 0, idx
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
    dup.setdefault(KEY[u['idx']], set()).add(T[u['idx']])
assert not [(k, v) for k, v in dup.items() if len(v) > 1]
assert len(dup) == 14, len(dup)
# le 8 copie di Cargo/Bulk condividono la resa
cargo = [i for i in T if ENG[i] == 'Deliver <cargo> to <destination>. Payment is <payment>.']
assert len(cargo) == 8 and len({T[i] for i in cargo}) == 1

for n, (lo, hi) in enumerate(((1, 13), (14, 25), (26, 37))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('37 unita (13+12+12) · 17 VALUE + 17 DESCRIPTION + 2 TEXT + 1 DIALOG · 19 contesti · 14 testi distinti')
print('81 token su 7 simboli · 8 copie di una sola DESCRIPTION · zero tab · zero virgolette')
