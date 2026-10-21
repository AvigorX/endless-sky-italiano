"""mkparts.py — L148: `data/coalition/coalition jobs.txt`, righe 309-435 (16 unita').

Arrivano due cose nuove: il **primo `DIALOG`** del file (unita' 1: tono narrativo, non burocratico) e il simbolo
**`<destination>`** (6 occorrenze), che in L147 non esisteva. La parita' si rifa' sul **nuovo** multiset: 31 occorrenze
su 4 simboli, verificando anche l'**ordine dei simboli per unita'**.

I `VALUE` restano identici: `Interpreters to <planet>` (**senza «the»**, a differenza di `Workers to the <planet>`),
`Peacekeepers to <planet>`, `Saryds to <planet>`.

`Lunarium`, `Heliarch`, `Saryd` sono nomi propri e restano; `peacekeeper` resta come prestito, coerente col `VALUE`.
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

DESC_INT = ("Porta questi <bunks> agenti Heliarch, addestrati come interpreti e mediatori, a <destination>. Il "
            "compenso è di <payment>.")
DESC_PEA = ("Trasporta questo corpo di <bunks> peacekeeper a <destination> per indagare su segnalazioni di attività "
            "dei Lunarium. Il compenso è di <payment>.")

D = {
    1: "Gli agenti Heliarch vengono incontro alla tua nave appena attracca e ricevono il candidato che hai trasportato, "
       "con una piccola cerimonia. Pochi minuti dopo ricevi un bonifico di <payment>.",
    2: "Scarichi gli interpreti su <planet>. Pochi minuti dopo ricevi un bonifico di <payment>.",
    3: "Interpreters to <planet>",
    4: DESC_INT,
    5: "Interpreters to <planet>",
    6: DESC_INT,
    7: "Interpreters to <planet>",
    8: DESC_INT,
    9: "Scarichi i peacekeeper su <planet>. Pochi minuti dopo ricevi un bonifico di <payment>.",
    10: "Peacekeepers to <planet>",
    11: DESC_PEA,
    12: "Peacekeepers to <planet>",
    13: DESC_PEA,
    14: "Scarichi i coloni su <planet>. Pochi minuti dopo ricevi un bonifico di <payment>.",
    15: "Saryds to <planet>",
    16: "Nell'ambito del Programma di Scambio tra Specie, questi <bunks> coloni volontari hanno bisogno di essere "
        "trasportati a <destination>. Il governo pagherà la loro tariffa di trasporto di <payment>.",
}

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ST = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(ST.values()) == {'PENDING'}, {k: v for k, v in ST.items() if v != 'PENDING'}

assert collections.Counter(u['kind'] for u in SRC) == {'DIALOG': 1, 'TEXT': 3, 'VALUE': 6, 'DESCRIPTION': 6}
assert sum(1 for u in SRC if u['english'].startswith('\t')) == 0
assert sum(u['english'].count('"') for u in SRC) == 0
assert [u['idx'] for u in SRC if u['kind'] == 'LOGBOOK'] == []
assert [u['idx'] for u in SRC if u['kind'] == 'UI_LABEL'] == []
assert [u['idx'] for u in SRC if u['kind'] == 'DIALOG'] == [1]
assert len(set(u['context'] for u in SRC)) == 10
tok = collections.Counter(t for u in SRC for t in TAGS.findall(u['english']))
assert dict(tok) == {'<payment>': 10, '<planet>': 9, '<bunks>': 6, '<destination>': 6}, dict(tok)
assert sum(tok.values()) == 31
assert (min(u['line'] for u in SRC), max(u['line'] for u in SRC)) == (309, 435)
assert sorted(D) == list(range(1, 17)), [i for i in range(1, 17) if i not in D]
VAL = {u['idx']: ENG[u['idx']].rstrip() for u in SRC if u['kind'] == 'VALUE'}
assert list(VAL.values()) == ['Interpreters to <planet>'] * 3 + ['Peacekeepers to <planet>'] * 2 + \
    ['Saryds to <planet>'], list(VAL.items())
assert 'the' not in ' '.join(VAL.values()).replace('Interpreters', '').replace('Peacekeepers', '').replace(
    'Saryds', ''), list(VAL.values())
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
assert len(dup) == 10, len(dup)
assert T[4] == T[6] == T[8] and T[11] == T[13]
assert '<destination>' in T[4] and '<planet>' not in T[4]
assert '<planet>' in T[2] and '<destination>' not in T[2]

for n, (lo, hi) in enumerate(((1, 8), (9, 13), (14, 16))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('16 unita (8+5+3) · 1 DIALOG + 3 TEXT + 6 VALUE + 6 DESCRIPTION · 10 contesti · 10 testi distinti')
print('31 token su 4 simboli (<payment> 10, <planet> 9, <bunks> 6, <destination> 6) · zero tab · zero virgolette')
