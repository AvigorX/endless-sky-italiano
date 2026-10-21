r"""verify.py — L157 (`data/human/weapons.txt`, 16 unita', righe 625-983).

Invariante di **segmento**: 90 unita' nel file, **21 prima** della riga 625, **53 dopo** la 983, confine alla riga 1015
(`DESCRIPTION` di `outfit:Sidewinder Missile`). Misure proprie: 1 `VALUE`, 4 tab, due coppie identiche (12/14, 13/16).
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
PATH = 'data/human/weapons.txt'
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


ck('riga grezza identica al sorgente (16/16)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('idx 1..16 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 17)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 16 righe 625 - 983', len(tu) == 16 and (first, last) == (625, 983), (len(tu), first, last))
ck('21 unita prima della riga 625 (L155+L156)', db.execute(
    'select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 21)
ck('90 unita nel file, 53 dopo la riga 983', db.execute(
    'select count(*) from units where path=?', (PATH,)).fetchone()[0] == 90
   and db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 53)
ck('confine alla riga 1015 (DESCRIPTION di Sidewinder Missile)', db.execute(
    'select line,kind,context from units where path=? and line>? order by line limit 1',
    (PATH, last)).fetchone() == (1015, 'DESCRIPTION', 'outfit:Sidewinder Missile'))
ck('tipi: 15 DESCRIPTION + 1 VALUE', collections.Counter(u['kind'] for u in su) == {'DESCRIPTION': 15, 'VALUE': 1})
ck('ZERO UI_LABEL, ZERO token, ZERO virgolette',
   [u['idx'] for u in su if u['kind'] == 'UI_LABEL'] == []
   and [u['idx'] for u in tu for t in TAGS.findall(u['italian'])] == []
   and sum(u['english'].count('"') for u in su) == 0 == sum(u['italian'].count('"') for u in tu))
ck('il VALUE e identico al sorgente', [u for u in tu if u['kind'] == 'VALUE'][0]['italian']
   == [u for u in su if u['kind'] == 'VALUE'][0]['english'] == 'Meteor Missile Boxes')
ck('4 unita con tab: idx 7, 13, 15, 16, le stesse in traduzione',
   [u['idx'] for u in su if u['english'].startswith('\t')] == [7, 13, 15, 16]
   == [u['idx'] for u in tu if u['italian'].startswith('\t')])
ck('coppie identiche in inglese restano identiche in italiano (12/14, 13/16)',
   by[12]['italian'] == by[14]['italian'] and by[13]['italian'] == by[16]['italian'])
ck('14 testi inglesi distinti su 16 unita', len({u['english'] for u in tu}) == 14)
ck('tutte PENDING', not [u['idx'] for u in su
                         if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('spazi iniziali e finali identici al sorgente (16/16)',
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
ck('le parti ricostruiscono translation.json (1..16)',
   sorted(merged) == list(range(1, 17)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica le righe 625-983',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and os.path.abspath(os.path.join(L10N, 'staging/editorial', f)) != HERE
        and any(u['path'] == PATH and first <= u['line'] <= last for u in json.load(open(os.path.join(
            L10N, 'staging/editorial', f, 'translation.json'), encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('segmento: 37/90 unita del file (41,1%) · 21 prima / 16 nel lotto / 53 dopo · confine riga 1015')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L157 superato' if not fail else 'verify L157 fallito')
raise SystemExit(0 if not fail else 1)
