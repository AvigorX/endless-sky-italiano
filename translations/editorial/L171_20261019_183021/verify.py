r"""verify.py — L171 (`data/human/paradise world jobs.txt`, 24 unita', righe 719-987).

Invariante di **segmento**: 89 unita' prima della riga 719 (L167…L170), 18 dopo la 987, 131 nel file; confine alla riga
1230, tipo **`VALUE`** (`mission:Martini Relief (Medical) [0]`) — **misurato**. Verifica anche il **salto vuoto**: fra la
987 e la 1230 non esiste alcuna unita'.
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


ck('riga grezza identica al sorgente (24/24)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('idx 1..24 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 25)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 24 righe 719 - 987', len(tu) == 24 and (first, last) == (719, 987), (len(tu), first, last))
ck('89 unita prima della riga 719 (L167…L170)', db.execute(
    'select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 89)
ck('131 unita nel file, 18 dopo la riga 987', db.execute(
    'select count(*) from units where path=?', (PATH,)).fetchone()[0] == 131
   and db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 18)
ck('SALTO VUOTO: zero unita fra la riga 988 e la 1229', db.execute(
    'select count(*) from units where path=? and line>? and line<1230', (PATH, last)).fetchone()[0] == 0)
ck('max(line) del file = 1413, min(line) = 16', db.execute(
    'select min(line),max(line) from units where path=?', (PATH,)).fetchone() == (16, 1413))
ck('confine alla riga 1230, tipo VALUE (misurato)', db.execute(
    'select line,kind,context from units where path=? and line>? order by line limit 1',
    (PATH, last)).fetchone() == (1230, 'VALUE', 'mission:Martini Relief (Medical) [0]'))
ck('tipi: 12 VALUE + 12 DESCRIPTION', collections.Counter(u['kind'] for u in su)
   == {'VALUE': 12, 'DESCRIPTION': 12})
ck('ZERO UI_LABEL, ZERO tab, ZERO virgolette; 1 apice in inglese, 2 in italiano (uomini d\'affari)',
   [u['idx'] for u in su if u['kind'] == 'UI_LABEL'] == []
   and [u['idx'] for u in su if '\t' in u['english']] == [] == [u['idx'] for u in tu if '\t' in u['italian']]
   and sum(u['english'].count('"') for u in su) == 0 == sum(u['italian'].count('"') for u in tu)
   and sum(u['english'].count("'") for u in su) == 1 == by[24]['english'].count("'")
   and sum(u['italian'].count("'") for u in tu) == 2
   and [u['idx'] for u in tu if "'" in u['italian']] == [18, 20]
   and [u['idx'] for u in tu if "d'affari" in u['italian']] == [18, 20])
TOK = {'<planet>': 28, '<payment>': 12, '<bunks>': 7, '<martini house>': 4, '<cargo>': 4}
ck('55 token su 5 simboli, multiset e ordine per unita identici',
   dict(collections.Counter(t for u in su for t in TAGS.findall(u['english']))) == TOK
   == dict(collections.Counter(t for u in tu for t in TAGS.findall(u['italian'])))
   and not [u['idx'] for u in tu if TAGS.findall(u['italian']) != TAGS.findall(u['english'])])
ck('`<martini house>` 4 volte: idx 2, 4, 6, 8',
   [u['idx'] for u in su if '<martini house>' in u['english']] == [2, 4, 6, 8]
   == [u['idx'] for u in tu if '<martini house>' in u['italian']])
ck('i 12 VALUE sono identici al sorgente',
   [u['idx'] for u in tu if u['kind'] == 'VALUE' and u['italian'] != u['english']] == [])
ck('10 VALUE distinti su 12: coppie 1/5 e 3/7 con resa identica',
   len({u['english'] for u in tu if u['kind'] == 'VALUE'}) == 10
   and by[1]['italian'] == by[5]['italian'] and by[3]['italian'] == by[7]['italian'])
ck('22 testi distinti, 12 contesti', len({u['english'] for u in tu}) == 22
   and len({u['context'] for u in tu}) == 12)
ck('tutte PENDING', not [u['idx'] for u in su
                         if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('spazi iniziali e finali identici al sorgente (24/24)',
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
ck('le parti ricostruiscono translation.json (1..24)',
   sorted(merged) == list(range(1, 25)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica le righe 719-987',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and os.path.abspath(os.path.join(L10N, 'staging/editorial', f)) != HERE
        and any(u['path'] == PATH and first <= u['line'] <= last for u in json.load(open(os.path.join(
            L10N, 'staging/editorial', f, 'translation.json'), encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('segmento: 113/131 unita del file (86,3%) · 89 prima / 24 nel lotto / 18 dopo · confine riga 1230 (~VALUE)')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L171 superato' if not fail else 'verify L171 fallito')
raise SystemExit(0 if not fail else 1)
