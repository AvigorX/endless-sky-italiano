r"""verify.py — L173 (`data/human/paradise world jobs.txt`, 6 unita', righe 1356-1413). **CHIUDE IL FILE.**

Invariante di **FILE**: le **7 finestre** (L167…L173) devono sommare **131 unita'** su **131 righe distinte**, con
`min(line) = 16` e `max(line) = 1413`; nessuna unita' oltre la 1413 (ultima del file), nessuna riga rivendicata due volte,
copertura esatta dell'insieme delle righe del file.
"""
import collections
import hashlib
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/human/paradise world jobs.txt'
TAGS = re.compile(r'<[^<>]+>')
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
by = {u['idx']: u for u in tu}
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-70s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (6/6)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('idx 1..6 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 7)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 6 righe 1356 - 1413', len(tu) == 6 and (first, last) == (1356, 1413), (len(tu), first, last))
ck('125 unita prima della riga 1356 (L167…L172)', db.execute(
    'select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 125)
ck('131 unita nel file, ZERO dopo la riga 1413 (fine file)', db.execute(
    'select count(*) from units where path=?', (PATH,)).fetchone()[0] == 131
   and db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 0)
ck('max(line) del file = 1413, min(line) = 16', db.execute(
    'select min(line),max(line) from units where path=?', (PATH,)).fetchone() == (16, 1413))
lots, claimed = [], []
for f in sorted(os.listdir(os.path.join(L10N, 'staging/editorial'))):
    p = os.path.join(L10N, 'staging/editorial', f, 'translation.json')
    if not os.path.isdir(os.path.join(L10N, 'staging/editorial', f)) or not os.path.exists(p):
        continue
    us = [u for u in json.load(open(p, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        lots.append((f, len(us)))
        claimed.extend(u['line'] for u in us)
ck('7 lotti su questo file (L167…L173)', len(lots) == 7
   and [f[:4] for f, _ in lots] == ['L167', 'L168', 'L169', 'L170', 'L171', 'L172', 'L173'], lots)
ck('somma delle finestre = 131 unita del file', sum(n for _, n in lots) == 131, [n for _, n in lots])
ck('zero sovrapposizioni: 131 righe rivendicate, 131 distinte',
   len(claimed) == 131 == len(set(claimed)), (len(claimed), len(set(claimed))))
ck('copertura esatta: min 16, max 1413, nessun buco',
   (min(claimed), max(claimed)) == (16, 1413)
   and sorted(set(claimed)) == sorted(r[0] for r in db.execute(
       'select line from units where path=?', (PATH,)).fetchall()))
ck('tipi: 3 VALUE + 3 DESCRIPTION', collections.Counter(u['kind'] for u in su)
   == {'VALUE': 3, 'DESCRIPTION': 3})
ck('ZERO UI_LABEL, ZERO tab, ZERO virgolette, 1 apice in inglese e 0 in italiano',
   [u['idx'] for u in su if u['kind'] == 'UI_LABEL'] == []
   and [u['idx'] for u in su if '\t' in u['english']] == [] == [u['idx'] for u in tu if '\t' in u['italian']]
   and sum(u['english'].count('"') for u in su) == 0 == sum(u['italian'].count('"') for u in tu)
   and sum(u['english'].count("'") for u in su) == 1 == by[4]['english'].count("'")
   and sum(u['italian'].count("'") for u in tu) == 0)
TOK = {'<bunks>': 3, '<martini relief occupations>': 3, '<planet>': 3, '<payment>': 3}
ck('12 token su 4 simboli, multiset e ordine per unita identici',
   dict(collections.Counter(t for u in su for t in TAGS.findall(u['english']))) == TOK
   == dict(collections.Counter(t for u in tu for t in TAGS.findall(u['italian'])))
   and not [u['idx'] for u in tu if TAGS.findall(u['italian']) != TAGS.findall(u['english'])])
ck('`<martini relief occupations>` intero in idx 2, 4, 6',
   [u['idx'] for u in su if '<martini relief occupations>' in u['english']] == [2, 4, 6]
   == [u['idx'] for u in tu if '<martini relief occupations>' in u['italian']])
ck('i 3 VALUE sono lo stesso testo e identici al sorgente',
   by[1]['english'] == by[3]['english'] == by[5]['english']
   and [u['idx'] for u in tu if u['kind'] == 'VALUE' and u['italian'] != u['english']] == [])
ck('4 testi distinti, 3 contesti', len({u['english'] for u in tu}) == 4
   and len({u['context'] for u in tu}) == 3)
ck('tutte PENDING', not [u['idx'] for u in su
                         if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('spazi iniziali e finali identici al sorgente (6/6)',
   not [u['idx'] for u in tu
        if len(u['italian']) - len(u['italian'].rstrip()) != len(u['english']) - len(u['english'].rstrip())
        or len(u['italian']) - len(u['italian'].lstrip()) != len(u['english']) - len(u['english'].lstrip())])
ck('nessun carattere tipografico e nessun non latino fuori dai token',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in TAGS.sub('', u['italian']))])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
merged = {}
for f in sorted(os.listdir(os.path.join(HERE, 'parts'))):
    if f.endswith('.json'):
        for k, v in json.load(open(os.path.join(HERE, 'parts', f), encoding='utf-8')).items():
            merged[int(k)] = v
ck('le parti ricostruiscono translation.json (1..6)',
   sorted(merged) == list(range(1, 7)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica le righe 1356-1413',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and os.path.abspath(os.path.join(L10N, 'staging/editorial', f)) != HERE
        and any(u['path'] == PATH and first <= u['line'] <= last for u in json.load(open(os.path.join(
            L10N, 'staging/editorial', f, 'translation.json'), encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('file CHIUSO: 131/131 unita (100%) · 7 finestre (L167…L173) · 125 prima / 6 nel lotto / 0 dopo · max(line) 1413')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L173 superato' if not fail else 'verify L173 fallito')
raise SystemExit(0 if not fail else 1)
