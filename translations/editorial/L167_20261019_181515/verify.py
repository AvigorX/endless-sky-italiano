r"""verify.py — L167 (`data/human/paradise world jobs.txt`, 28 unita', righe 16-221).

Invariante di **segmento**: il lotto **apre il file** (0 unita' prima della riga 16), 131 unita' nel file, **103 dopo**
la 221, confine alla riga 225 (`MISSION_TEXT` di `mission:Paradise Job: Clothing Donations`).
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


ck('riga grezza identica al sorgente (28/28)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('idx 1..28 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 29)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 28 righe 16 - 221', len(tu) == 28 and (first, last) == (16, 221), (len(tu), first, last))
ck('il lotto APRE il file: 0 unita prima della riga 16', db.execute(
    'select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 0)
ck('131 unita nel file, 103 dopo la riga 221', db.execute(
    'select count(*) from units where path=?', (PATH,)).fetchone()[0] == 131
   and db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 103)
ck('max(line) del file = 1413, min(line) = 16', db.execute(
    'select min(line),max(line) from units where path=?', (PATH,)).fetchone() == (16, 1413))
ck('confine alla riga 225 (VALUE di Clothing Donations)', db.execute(
    'select line,kind,context from units where path=? and line>? order by line limit 1',
    (PATH, last)).fetchone() == (225, 'VALUE', 'mission:Paradise Job: Clothing Donations'))
ck('tipi: 9 VALUE + 9 DESCRIPTION + 9 DIALOG + 1 MISSION_TEXT',
   collections.Counter(u['kind'] for u in su)
   == {'VALUE': 9, 'DESCRIPTION': 9, 'DIALOG': 9, 'MISSION_TEXT': 1})
ck('ZERO UI_LABEL e ZERO tab', [u['idx'] for u in su if u['kind'] == 'UI_LABEL'] == []
   and [u['idx'] for u in su if '\t' in u['english']] == [] == [u['idx'] for u in tu if '\t' in u['italian']])
TOK = {'<payment>': 18, '<planet>': 10, '<destination>': 9, '<commodity>': 7, '<date>': 6, '<tons>': 5,
       '<cargo>': 4, '<bunks>': 2, '<origin>': 1}
ck('62 token su 9 simboli, stesso multiset e stesso ordine per unita',
   dict(collections.Counter(t for u in su for t in TAGS.findall(u['english']))) == TOK
   == dict(collections.Counter(t for u in tu for t in TAGS.findall(u['italian'])))
   and not [u['idx'] for u in tu if TAGS.findall(u['italian']) != TAGS.findall(u['english'])])
ck('i 9 VALUE sono identici al sorgente',
   len([u for u in tu if u['kind'] == 'VALUE']) == 9
   and [u['idx'] for u in tu if u['kind'] == 'VALUE' and u['italian'] != u['english']] == [])
ck('2 virgolette in idx 21, identiche in traduzione',
   sum(u['english'].count('"') for u in su) == 2 == sum(u['italian'].count('"') for u in tu)
   and by[21]['italian'].count('"') == 2)
ck('27 testi distinti su 28 unita (coppia 19/23)',
   len({u['english'] for u in tu}) == 27 and by[19]['italian'] == by[23]['italian'])
ck('9 contesti distinti', len({u['context'] for u in tu}) == 9)
ck('tutte PENDING', not [u['idx'] for u in su
                         if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('spazi iniziali e finali identici al sorgente (28/28)',
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
ck('le parti ricostruiscono translation.json (1..28)',
   sorted(merged) == list(range(1, 29)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica le righe 16-221',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and os.path.abspath(os.path.join(L10N, 'staging/editorial', f)) != HERE
        and any(u['path'] == PATH and first <= u['line'] <= last for u in json.load(open(os.path.join(
            L10N, 'staging/editorial', f, 'translation.json'), encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('segmento: 28/131 unita del file (21,4%) · 0 prima / 28 nel lotto / 103 dopo · confine riga 225')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L167 superato' if not fail else 'verify L167 fallito')
raise SystemExit(0 if not fail else 1)
