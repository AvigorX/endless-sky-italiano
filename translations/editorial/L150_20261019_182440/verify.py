r"""verify.py — L150 (`data/coalition/coalition jobs.txt`, 14 unita', righe 639-794).

Invariante di **segmento**: 197 unita' nel file, **64 prima** della riga 639, **119 dopo** la 794, confine alla riga
**799** (`Fast Courier 1`).

Misure proprie: **33 token su 6 simboli** con `<commodity>` una volta sola; due famiglie di turisti che differiscono per
«home» e hanno **rese diverse**; 6 `VALUE` identici.
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
PATH = 'data/coalition/coalition jobs.txt'
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


ck('riga grezza identica al sorgente', not [u for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('idx 1..14 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 15)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 14 righe 639 - 794', len(tu) == 14 and (first, last) == (639, 794), (len(tu), first, last))
ck('64 unita prima della riga 639 (L147…L149)', db.execute(
    'select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 64)
ck('197 unita nel file, 119 dopo la riga 794', db.execute(
    'select count(*) from units where path=?', (PATH,)).fetchone()[0] == 197
   and db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 119)
ck('confine alla riga 799 apre Fast Courier 1', db.execute(
    'select line,context from units where path=? and line>? order by line limit 1',
    (PATH, last)).fetchone() == (799, 'mission:Coalition: Fast Courier 1'))
ck('tipi: 6 VALUE + 6 DESCRIPTION + 2 TEXT',
   collections.Counter(u['kind'] for u in su) == {'VALUE': 6, 'DESCRIPTION': 6, 'TEXT': 2})
ck('ZERO LOGBOOK, DIALOG, UI_LABEL (tre asserzioni vuote)',
   [u['idx'] for u in su if u['kind'] in ('LOGBOOK', 'DIALOG', 'UI_LABEL')] == [])
TOK = {'<payment>': 8, '<planet>': 6, '<bunks>': 6, '<destination>': 6, '<date>': 6, '<commodity>': 1}
ck('33 token su 6 simboli, stesso multiset in italiano',
   dict(collections.Counter(t for u in su for t in TAGS.findall(u['english']))) == TOK ==
   dict(collections.Counter(t for u in tu for t in TAGS.findall(u['italian'])))
   and sum(TOK.values()) == 33)
ck('`<commodity>` una sola volta, e al suo posto (unita 14)',
   TOK['<commodity>'] == 1 and '<commodity>' in by[14]['italian']
   and sum(1 for u in tu for _ in re.findall('<commodity>', u['italian'])) == 1)
ck('parita per unita: stesso ordine di simboli in tutte le 14',
   not [u['idx'] for u in tu if TAGS.findall(u['italian']) != TAGS.findall(u['english'])])
ck('6 VALUE identici al sorgente', [u['idx'] for u in tu if u['kind'] == 'VALUE'
                                    and u['italian'].rstrip() != u['english'].rstrip()] == []
   and len([u for u in tu if u['kind'] == 'VALUE']) == 6)
ck('DESCRIPTION e TEXT tradotti',
   not [u['idx'] for u in tu if u['kind'] != 'VALUE' and u['italian'].strip() == u['english'].strip()])
ck('le due famiglie differiscono per «home» e hanno rese diverse',
   su[1]['english'].replace('bring them to', 'bring them home to') == su[8]['english']
   and by[2]['italian'] != by[9]['italian']
   and 'riportarli a casa' in by[9]['italian'] and 'riportarli a casa' not in by[2]['italian'])
ck('tutte PENDING', not [u['idx'] for u in su
                         if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('spazi iniziali e finali identici al sorgente (14/14)',
   not [u['idx'] for u in tu
        if len(u['italian']) - len(u['italian'].rstrip()) != len(u['english']) - len(u['english'].rstrip())])
ck('zero tab e zero virgolette (due asserzioni vuote)',
   sum(1 for u in su if u['english'].startswith('\t')) == 0
   and sum(u['english'].count('"') for u in su) == 0 == sum(u['italian'].count('"') for u in tu))
ck('8 contesti', len(set(u['context'] for u in su)) == 8)
ck('5 testi inglesi distinti', len({u['english'] for u in tu}) == 5)
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
ck('le tre parti ricostruiscono translation.json (1..14)',
   sorted(merged) == list(range(1, 15)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica le righe 639-794',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and os.path.abspath(os.path.join(L10N, 'staging', 'editorial', f)) != HERE
        and any(u['path'] == PATH and first <= u['line'] <= last for u in json.load(open(os.path.join(
            L10N, 'staging', 'editorial', f, 'translation.json'), encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('segmento: 78/197 unita del file (39,6%) · 64 prima / 119 dopo · confine riga 799')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L150 superato' if not fail else 'verify L150 fallito')
raise SystemExit(0 if not fail else 1)
