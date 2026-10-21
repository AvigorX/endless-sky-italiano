"""mkparts.py — L149: `data/coalition/coalition jobs.txt`, righe 455-634 (18 unita').

**Due frasi esistono gia'** in lotti precedenti e si **rileggono**, verificando prima che l'inglese sia identico:
- la `DESCRIPTION` dei coloni (identica a L148 unita' 16) -> `SHARED` da L148;
- il `TEXT` degli operai **NON** e' quello di L147: la' c'era «on **the** <planet>», qui «on <planet>». Stringa diversa,
  resa diversa («su <planet>» contro «sul <planet>»), e il confronto lo dimostra.

**36 token su 4 simboli con due coppie di conteggi uguali** (`<planet>`/`<payment>` 10, `<bunks>`/`<destination>` 8):
il multiset e' cieco a uno scambio, quindi conta l'**ordine dei simboli per unita'**.
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

PREV148 = json.load(open(os.path.join(L10N, 'staging/editorial/L148_20261019_174022/translation.json'),
                         encoding='utf-8'))['units']
PREV147 = json.load(open(os.path.join(L10N, 'staging/editorial/L147_20261019_171044/translation.json'),
                         encoding='utf-8'))['units']
P148 = {u['english']: u['italian'] for u in PREV148}
P147 = {u['english']: u['italian'] for u in PREV147}

DESC_SET = ("As part of the Interspecies Exchange Program, these <bunks> volunteer settlers need transportation to "
            "<destination>. The government will pay their transport fee of <payment>.")
DESC_EMP = ("As a part of the Full Employment Program, these <bunks> workers need transportation to <destination>. "
            "The government will pay their transport fee of <payment>.")
TXT_WORK = "You drop off the workers on <planet>. A few minutes later you receive a transfer of <payment>."
TXT_WORK_147 = "You drop off the workers on the <planet>. A few minutes later you receive a transfer of <payment>."
TXT_TOUR = "The tourists thank you for bringing them to <planet> and pay you <payment>."

assert DESC_SET in P148, 'la DESCRIPTION dei coloni non e in L148'
assert TXT_WORK not in P147, 'la variante senza «the» non deve esistere in L147'
assert TXT_WORK_147 in P147, 'la variante con «the» deve stare in L147'
SET_IT = P148[DESC_SET]
WORK_IT = "Scarichi gli operai su <planet>. Pochi minuti dopo ricevi un bonifico di <payment>."

D = {
    1: "Saryds to <planet>",
    2: SET_IT,
    3: "Kimek to <planet>",
    4: SET_IT,
    5: "Kimek to <planet>",
    6: SET_IT,
    7: "Arachi to <planet>",
    8: SET_IT,
    9: "Arachi to <planet>",
    10: SET_IT,
    11: WORK_IT,
    12: "Transfer to <planet>",
    13: "Nell'ambito del Programma di Piena Occupazione, questi <bunks> lavoratori hanno bisogno di essere trasportati "
        "a <destination>. Il governo pagherà la loro tariffa di trasporto di <payment>.",
    14: "Transfer to <planet>",
    15: "Nell'ambito del Programma di Piena Occupazione, questi <bunks> lavoratori hanno bisogno di essere trasportati "
        "a <destination>. Il governo pagherà la loro tariffa di trasporto di <payment>.",
    16: "Transfer to <planet>",
    17: "Nell'ambito del Programma di Piena Occupazione, questi <bunks> lavoratori hanno bisogno di essere trasportati "
        "a <destination>. Il governo pagherà la loro tariffa di trasporto di <payment>.",
    18: "I turisti ti ringraziano per averli portati su <planet> e ti pagano <payment>.",
}

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ST = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(ST.values()) == {'PENDING'}, {k: v for k, v in ST.items() if v != 'PENDING'}

assert collections.Counter(u['kind'] for u in SRC) == {'VALUE': 8, 'DESCRIPTION': 8, 'TEXT': 2}
assert sum(1 for u in SRC if u['english'].startswith('\t')) == 0
assert sum(u['english'].count('"') for u in SRC) == 0
assert [u['idx'] for u in SRC if u['kind'] in ('LOGBOOK', 'DIALOG', 'UI_LABEL')] == []
assert len(set(u['context'] for u in SRC)) == 10
tok = collections.Counter(t for u in SRC for t in TAGS.findall(u['english']))
assert dict(tok) == {'<planet>': 10, '<payment>': 10, '<bunks>': 8, '<destination>': 8}, dict(tok)
assert sum(tok.values()) == 36
assert tok['<planet>'] == tok['<payment>'] == 10 and tok['<bunks>'] == tok['<destination>'] == 8
assert (min(u['line'] for u in SRC), max(u['line'] for u in SRC)) == (455, 634)
assert sorted(D) == list(range(1, 19)), [i for i in range(1, 19) if i not in D]
VAL = {u['idx']: ENG[u['idx']].rstrip() for u in SRC if u['kind'] == 'VALUE'}
assert list(VAL.values()) == ['Saryds to <planet>', 'Kimek to <planet>', 'Kimek to <planet>',
                             'Arachi to <planet>', 'Arachi to <planet>', 'Transfer to <planet>',
                             'Transfer to <planet>', 'Transfer to <planet>'], list(VAL.items())
for i, v in VAL.items():
    assert D[i] == v, (i, D[i], v)

T = {u['idx']: D[u['idx']] for u in SRC}

for idx, txt in T.items():
    eng = ENG[idx]
    assert txt.count('\t') == eng.count('\t') == 0, idx
    assert txt.count('"') == eng.count('"') == 0, idx
    assert TAGS.findall(txt) == TAGS.findall(eng), (idx, TAGS.findall(txt), TAGS.findall(eng))
    assert len(txt) - len(txt.rstrip()) == len(eng) - len(eng.rstrip()), ('spazio finale', idx)
    assert not re.search(r'[\[\]`\u2019\u2014\u2013\u2026]', txt), idx
    assert not re.search(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", txt), idx
    if idx in VAL:
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
assert len(dup) == 8, len(dup)
assert T[2] == T[4] == T[6] == T[8] == T[10] == SET_IT
assert T[13] == T[15] == T[17]
assert T[11] == WORK_IT
assert T[2] == P148[DESC_SET]
assert T[11] != P147[TXT_WORK_147], 'la resa senza «the» non puo coincidere con quella con «the»'
assert 'su <planet>' in T[11] and 'sul <planet>' in P147[TXT_WORK_147]

for n, (lo, hi) in enumerate(((1, 7), (8, 13), (14, 18))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('18 unita (7+6+5) · 8 VALUE + 8 DESCRIPTION + 2 TEXT · 10 contesti · 8 testi distinti')
print('36 token su 4 simboli con DUE coppie di conteggi uguali (10/10 e 8/8) · zero tab · zero virgolette')
print('1 frase riletta da L148 (inglese identico); il TEXT degli operai ha una variante senza «the», resa nuova')
