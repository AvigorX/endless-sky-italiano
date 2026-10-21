r"""verify.py — L169 (`data/human/paradise world jobs.txt`, 17 unita', righe 376-522).

Invariante di **segmento**: 52 unita' prima della riga 376 (L167+L168), 62 dopo la 522, 131 nel file; confine alla riga
526, tipo **`VALUE`** (`mission:Paradise Job: Pirate Retirees (Illegal)`) — **misurato sul database**.
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


ck('riga grezza identica al sorgente (17/17)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('idx 1..17 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 18)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 17 righe 376 - 522', len(tu) == 17 and (first, last) == (376, 522), (len(tu), first, last))
ck('52 unita prima della riga 376 (L167+L168)', db.execute(
    'select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 52)
ck('131 unita nel file, 62 dopo la riga 522', db.execute(
    'select count(*) from units where path=?', (PATH,)).fetchone()[0] == 131
   and db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 62)
ck('max(line) del file = 1413, min(line) = 16', db.execute(
    'select min(line),max(line) from units where path=?', (PATH,)).fetchone() == (16, 1413))
ck('confine alla riga 526, tipo VALUE (misurato)', db.execute(
    'select line,kind,context from units where path=? and line>? order by line limit 1',
    (PATH, last)).fetchone() == (526, 'VALUE', 'mission:Paradise Job: Pirate Retirees (Illegal)'))
ck('tipi: 3 VALUE + 6 DESCRIPTION + 8 DIALOG',
   collections.Counter(u['kind'] for u in su) == {'VALUE': 3, 'DESCRIPTION': 6, 'DIALOG': 8})
ck('ZERO UI_LABEL e ZERO tab', [u['idx'] for u in su if u['kind'] == 'UI_LABEL'] == []
   and [u['idx'] for u in su if '\t' in u['english']] == [] == [u['idx'] for u in tu if '\t' in u['italian']])
TOK = {'<payment>': 12, '<destination>': 7, '<planet>': 5, '<bunks>': 5, '<npc>': 4, '<stopovers>': 2,
       '<tons>': 2, '<commodity>': 1}
ck('38 token su 8 simboli, multiset e ordine per unita identici',
   dict(collections.Counter(t for u in su for t in TAGS.findall(u['english']))) == TOK
   == dict(collections.Counter(t for u in tu for t in TAGS.findall(u['italian'])))
   and not [u['idx'] for u in tu if TAGS.findall(u['italian']) != TAGS.findall(u['english'])])
ck('`<npc>` 4 volte: idx 5, 6, 7, 8 in entrambe le lingue',
   [u['idx'] for u in su if '<npc>' in u['english']] == [5, 6, 7, 8] == [u['idx'] for u in tu if '<npc>' in u['italian']])
ck('i 3 VALUE sono identici al sorgente',
   [u['idx'] for u in tu if u['kind'] == 'VALUE' and u['italian'] != u['english']] == [])
ck('le coppie 1/3 e 2/4 hanno la stessa resa',
   by[1]['italian'] == by[3]['italian'] and by[2]['italian'] == by[4]['italian'])
ck('2 virgolette in idx 13, 2 apici in idx 1 e 3',
   sum(u['english'].count('"') for u in su) == 2 == sum(u['italian'].count('"') for u in tu)
   and by[1]['italian'].count("'") == 2 == by[3]['italian'].count("'"))
ck('15 testi distinti, 6 contesti', len({u['english'] for u in tu}) == 15
   and len({u['context'] for u in tu}) == 6)
ck('tutte PENDING', not [u['idx'] for u in su
                         if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('spazi iniziali e finali identici al sorgente (17/17)',
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
ck('le parti ricostruiscono translation.json (1..17)',
   sorted(merged) == list(range(1, 18)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica le righe 376-522',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and os.path.abspath(os.path.join(L10N, 'staging/editorial', f)) != HERE
        and any(u['path'] == PATH and first <= u['line'] <= last for u in json.load(open(os.path.join(
            L10N, 'staging/editorial', f, 'translation.json'), encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('segmento: 69/131 unita del file (52,7%) · 52 prima / 17 nel lotto / 62 dopo · confine riga 526 (~VALUE)')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L169 superato' if not fail else 'verify L169 fallito')
raise SystemExit(0 if not fail else 1)
